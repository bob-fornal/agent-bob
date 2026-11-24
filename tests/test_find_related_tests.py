import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "find_related_tests.py"


class FindRelatedTestsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.write("src/foo.py", "original\n")
        self.write("tests/test_foo.py", "test\n")
        self.write("src/removed.py", "removed\n")
        self.git("add", ".")
        self.git("commit", "-qm", "base")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args, check=True):
        return subprocess.run(
            ["git", "-c", "commit.gpgsign=false", "-C", str(self.repo), *args],
            check=check,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ).stdout.strip()

    def write(self, name, content):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo", str(self.repo), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def test_merge_and_worktree_changes_include_candidates_and_unmatched_files(self):
        self.git("checkout", "-qb", "source")
        self.write("src/bar file.js", "source\n")
        self.write("tests/bar file.test.js", "test\n")
        self.git("add", ".")
        self.git("commit", "-qm", "source")
        self.git("checkout", "-qb", "pr", self.base)
        self.write("src/foo.py", "changed\n")
        self.git("rm", "-q", "src/removed.py")
        self.git("add", ".")
        self.git("commit", "-qm", "pr")
        before = self.git("rev-parse", "HEAD")
        self.git("merge", "--no-ff", "--no-commit", "source")
        self.write("tests/test_extra.py", "untracked test\n")

        result = self.run_script("--base", self.base, "--before-merge", before)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(
            set(data["changed_files"]),
            {"src/foo.py", "src/removed.py", "src/bar file.js",
             "tests/bar file.test.js", "tests/test_extra.py"},
        )
        self.assertEqual(data["related_test_candidates"]["src/foo.py"], ["tests/test_foo.py"])
        self.assertEqual(data["related_test_candidates"]["src/bar file.js"], ["tests/bar file.test.js"])
        self.assertEqual(data["changed_tests"], ["tests/bar file.test.js", "tests/test_extra.py"])
        self.assertIn("src/removed.py", data["unmatched_changed_files"])
        self.assertIn("not a dependency or coverage analysis", data["limitations"])

    def test_completed_merge_still_includes_incoming_changes(self):
        self.git("checkout", "-qb", "source")
        self.write("src/foo.py", "incoming\n")
        self.git("add", ".")
        self.git("commit", "-qm", "source")
        self.git("checkout", "-qb", "pr", self.base)
        self.write("src/other.py", "pr\n")
        self.git("add", ".")
        self.git("commit", "-qm", "pr")
        before = self.git("rev-parse", "HEAD")
        self.git("merge", "--no-ff", "-qm", "merge", "source")

        result = self.run_script("--base", "source", "--before-merge", before)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(json.loads(result.stdout)["changed_files"]), {"src/foo.py", "src/other.py"})

    def test_invalid_ref_and_unresolved_conflicts_are_errors(self):
        result = self.run_script("--base", "missing", "--before-merge", self.base)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("find_related_tests:", result.stderr)
        self.git("checkout", "-qb", "source")
        self.write("src/foo.py", "source\n")
        self.git("commit", "-qam", "source")
        self.git("checkout", "-qb", "pr", self.base)
        self.write("src/foo.py", "pr\n")
        self.git("commit", "-qam", "pr")
        before = self.git("rev-parse", "HEAD")
        self.git("merge", "--no-commit", "source", check=False)
        result = self.run_script("--base", self.base, "--before-merge", before)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("resolve and stage merge conflicts", result.stderr)


if __name__ == "__main__":
    unittest.main()
