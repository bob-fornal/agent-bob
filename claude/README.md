# agent-bob

Personal collection of [Claude Code](https://claude.com/claude-code) skills. A skill is a `SKILL.md` file (plus optional reference docs and scripts) that Claude Code reads automatically when a request matches its description, so it applies the guidance below without being asked to load it explicitly.

## Skills

| Skill | Triggers on | What it does |
|---|---|---|
| [`humanize-writing/`](humanize-writing/) | Any substantive writing task (emails, posts, docs, PR descriptions, essays...) | Actively avoids generic "AI-sounding" tells -- overused vocabulary, boilerplate phrases, robotic sentence rhythm, formulaic structure. |
| [`write-like-bob/`](write-like-bob/) | Requests for a blog post, dev.to article, or write-up meant to sound like Bob Fornal | Reproduces Bob's actual writing voice, built from reading all 121 of his published [dev.to](https://dev.to/rfornal) articles. |

Also included: [`write-like-bob.skill`](write-like-bob.skill) -- a packaged, portable copy of the
`write-like-bob` skill for installing elsewhere without cloning this repo.

## Installation

Claude Code loads skills from `~/.claude/skills/<skill-name>/` (personal, all projects) or
`.claude/skills/<skill-name>/` (a single project). To install one of these:

```bash
cp -r humanize-writing ~/.claude/skills/
cp -r write-like-bob ~/.claude/skills/
```

Or drag the `.skill` file into Claude Code / claude.ai when prompted to save a skill.

Once installed, no manual invocation is needed -- each skill's `description` frontmatter tells Claude Code when to use it, and it applies automatically on a matching request.

---

## `humanize-writing`

Every commonly-cited "sign of AI writing" -- Wikipedia's own [[igns of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guideline, journalism on the topic (Rolling Stone, Reuters Institute, NPR, Washington Post), NLP/stylometric research, and detection-tool writeups -- converges on the same short list of tells: a cluster of overused vocabulary (`delve`, `tapestry`, `robust`, `leverage`...), boilerplate phrases ("it's important to note," "in today's fast-paced world"), suspiciously uniform sentence rhythm, and a handful of formulaic structural moves (rule-of-three lists, a canned "challenges and future outlook" section). None of these individually proves anything -- the research is unanimous that no single word or habit is a reliable tell on its own, and reflexively stripping something like every em dash can itself read as stilted. What actually reads as generic is leaning on the whole cluster of defaults at once instead of making real choices.

**Contents:**
- `SKILL.md` -- the checklist-driven workflow: write normally first, then pass the draft against a   vocabulary/phrase/rhythm/structure/specificity checklist before delivering.
- `references/signs-of-ai-writing.md` -- the exhaustive word/phrase/pattern list, the em-dash caveat   (that specific "tell" is the most viral and the most overstated -- see the sourcing inside), and full citations.
- `scripts/check_ai_tells.py` -- an objective scanner for banned vocabulary/phrase hits, em-dash rate, and a sentence-length "burstiness ratio" (stdev / average -- low means suspiciously uniform rhythm). Run it against a draft for a second opinion:
  ```bash
  python scripts/check_ai_tells.py path/to/draft.txt
  ```
- `evals/evals.json` -- test prompts and objective assertions used to validate the skill.

## `write-like-bob`

A voice profile built by reading all 121 articles at [dev.to/rfornal](https://dev.to/rfornal) (2019-2026, ~95,000 words), analyzed in five independent chronological passes and cross-checked for patterns that held steady across all seven years -- not just a couple of articles. The result is a distinctive, well-evidenced voice: short declarative sentences, an ellipsis used as a mid-sentence pause rather than just a trail-off, sentence-openers like "So,"/"Then,"/"Basically,"/"Now,", a Problem &rarr; Attempt &rarr; Failure &rarr; Resolution arc, bold-italic (`***word***`) for emphasis, a closing Summary/Conclusion that echoes the opening almost verbatim, and a self-deprecating, first-person voice that frames technical facts as personal experience.

**Contents:**
- `SKILL.md` -- the operational guide: how to open, how to build sentences, how to structure a piece, how to handle emphasis and voice, plus a worked before/after example.
- `references/voice-notes.md` -- the full evidence behind every rule in `SKILL.md`, organized the same way (sentence habits, structure, recurring phrases, tone, punctuation), with direct quotes and source article filenames for each pattern.
