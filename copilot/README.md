# copilot

This folder contains persistent guidance used by GitHub Copilot in this workspace.

## Files

- `persistent-memory.md`: durable preferences and implementation defaults that should remain stable across tasks.

## Purpose

Use `persistent-memory.md` to capture high-value defaults that improve consistency, such as:

- architecture preferences
- framework defaults
- platform constraints
- recurring implementation rules

Keep entries short and specific so they are easy to apply and maintain.

## Update Guidelines

- Add only durable preferences, not one-off task notes.
- Prefer one bullet per rule.
- Avoid duplicates and merge overlapping statements.
- Remove outdated rules promptly.
- Keep wording implementation-focused (what to do, not long rationale).

## Current Memory Snapshot

The current memory emphasizes:

- Worker Script API preference over Cloudflare APIs
- Angular defaults (SoC, LTS, Angular Material)
- backend-first approach when appropriate
- explicit `rootDir` requirements in Angular TS6+ when `outDir` is set
- hash-tag URLs for Angular on Cloudflare
