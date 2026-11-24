# agent-bob

Personal workspace for writing-assistant assets used with Claude Code and GitHub Copilot.

This repository currently contains:

- `claude/`: skill packages, subagent definitions, and references for Claude Code.
- `copilot/`: Copilot agent instructions and persistent memory notes.

## Repository Layout

```text
claude/
  README.md
  write-like-bob.skill
  agents/
    socratic-tutor.md
    update-pr.md
  humanize-writing/
    SKILL.md
    evals/
      evals.json
    references/
      signs-of-ai-writing.md
    scripts/
      check_ai_tells.py
  write-like-bob/
    SKILL.md
    references/
      voice-notes.md
copilot/
  update-pr.agent.md
  sections/pr-update/01-workflow.md
  persistent-memory.md
tools/
  find_related_tests.py
```

## Claude Skills

### `humanize-writing`

Use for substantive prose where the output should read naturally and avoid common AI-writing tells.

- Main guide: `claude/humanize-writing/SKILL.md`
- Deep reference: `claude/humanize-writing/references/signs-of-ai-writing.md`
- Optional checker: `python claude/humanize-writing/scripts/check_ai_tells.py <path-to-draft>`

### `write-like-bob`

Use when drafting content in Bob Fornal's established writing voice (for example dev.to posts and technical write-ups).

- Main guide: `claude/write-like-bob/SKILL.md`
- Voice evidence notes: `claude/write-like-bob/references/voice-notes.md`
- Portable package: `claude/write-like-bob.skill`

For additional details on installation and usage, see `claude/README.md`.

## Claude Subagents

Unlike skills (which apply automatically when a request matches), subagents are invoked by name via Claude Code's Agent tool or Task delegation.

### `socratic-tutor`

Given a document and the correct answers/derivations, runs a Socratic dialogue that leads the student to the answer through questions rather than direct instruction, allows genuine counter-argument, and closes with a written assessment of understanding depth and session effectiveness.

- Definition: `claude/agents/socratic-tutor.md`

Install by copying into `~/.claude/agents/` (all projects) or `.claude/agents/` (a single project):

```bash
cp claude/agents/socratic-tutor.md ~/.claude/agents/
```

### `update-pr`

Merges `main` into a PR branch, resolves conflicts, tests changed code and fixes integration issues, then commits and pushes the result. Include `main=develop` in the agent request to use `develop` instead, or set `main=<branch>` to another source branch.

- Claude definition: `claude/agents/update-pr.md`
- Copilot definition: `copilot/update-pr.agent.md` (with its linked `sections/pr-update/` workflow)

The optional test-discovery helper uses Python 3 and Git. Install it where both agents can find it:

```bash
mkdir -p ~/.local/share/agent-bob
cp tools/find_related_tests.py ~/.local/share/agent-bob/
```

Record the PR head commit before the merge, then run the helper from the target repository after resolving and staging conflicts:

```bash
python3 ~/.local/share/agent-bob/find_related_tests.py --base <fetched-pr-base-ref> --before-merge <pre-merge-pr-head-commit>
```

It reports changed files, changed tests, and filename-based test candidates as JSON. It includes staged, unstaged, and untracked files; unrelated changes must be handled before the merge. Filename matches cannot identify all affected tests, especially indirect dependencies or shared configuration, so use the project's test-selection tools or coverage data and run a broader suite when needed. The helper does not run tests.

## Copilot Memory

The `copilot/persistent-memory.md` file stores durable guidance that can be reused across sessions.

Current themes include:

- Cloudflare preference (Worker Script API over Cloudflare APIs)
- Angular defaults (separation of concerns, LTS, Angular Material)
- Backend-first implementation preference when appropriate
- Angular TS6+ `rootDir` requirements when `outDir` is set
- Hash-tag URL notation for Angular apps hosted on Cloudflare

See `copilot/README.md` for maintenance guidelines.

## Maintenance

- Keep `SKILL.md` files focused on trigger conditions and operating rules.
- Put evidence, examples, and long explanations under each skill's `references/` folder.
- Keep `copilot/persistent-memory.md` concise, factual, and stable.
- Update this root README when folders are added, removed, or renamed.
