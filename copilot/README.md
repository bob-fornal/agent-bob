# copilot

This folder contains persistent guidance used by GitHub Copilot in this workspace.

## Files

- `persistent-memory.md`: durable preferences and implementation defaults that should remain stable across tasks.
- `cloudflare_worker.agent.md`: parent instructions for Cloudflare Worker and D1 work; links to sectioned guidance in `sections/cloudflare/`.
- `typescript_linting.agent.md`: parent instructions for TypeScript linting and style enforcement; links to sectioned guidance in `sections/ts-lint/`.
- `sections/`: modular instruction content referenced by agent files (Cloudflare and TypeScript linting).

## Purpose

Use `persistent-memory.md` to capture high-value defaults that improve consistency, such as:

- architecture preferences
- framework defaults
- platform constraints
- recurring implementation rules

Keep entries short and specific so they are easy to apply and maintain.

Use the `*.agent.md` files to define task-focused operating instructions that can be split into reusable section files under `sections/`.

## Update Guidelines

- Add only durable preferences, not one-off task notes.
- Prefer one bullet per rule.
- Avoid duplicates and merge overlapping statements.
- Remove outdated rules promptly.
- Keep wording implementation-focused (what to do, not long rationale).
- Keep `*.agent.md` files as index documents that reference section files rather than embedding long rule sets inline.
- Update linked section documents when behavior/rules change, and keep parent agent file section lists in sync.

## Current Memory Snapshot

The current memory emphasizes:

- Worker Script API preference over Cloudflare APIs
- Angular defaults (SoC, LTS, Angular Material)
- backend-first approach when appropriate
- explicit `rootDir` requirements in Angular TS6+ when `outDir` is set
- hash-tag URLs for Angular on Cloudflare
