# agent-bob

Personal workspace for writing-assistant assets used with Claude Code and GitHub Copilot.

This repository currently contains:

- `claude/`: skill packages and references for Claude Code.
- `copilot/`: persistent memory notes used to steer Copilot behavior.

## Repository Layout

```text
claude/
  README.md
  write-like-bob.skill
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
  persistent-memory.md
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
