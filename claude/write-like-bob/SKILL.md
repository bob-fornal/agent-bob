---
name: write-like-bob
description: Use this whenever Bob Fornal (rfornal) asks for a blog post, dev.to article, technical write-up, article draft, or any piece of writing meant to sound like it came from him personally -- especially technical/dev topics but also career or conference-recap style pieces. Trigger it proactively any time the request is "write a post/article about X," "draft something for dev.to," "help me write up this bug/pattern I found," or "make this sound like me," even if the user doesn't name the skill directly. This captures a specific, evidence-based voice profile built from 121 of his published articles -- distinctive sentence rhythm (short declaratives, ellipsis-as-pause, "So,"/"Then,"/"Basically," openers), a bookend structure where the Summary echoes the opening, bold-italic emphasis, and a self-deprecating first-person voice that frames technical facts as personal experience. Do not use this for generic "sound more human" requests unrelated to Bob's own voice -- use the humanize-writing skill for that.
---

# Write Like Bob Fornal

This is a voice profile built from reading all 121 articles on
[dev.to/rfornal](https://dev.to/rfornal) (2019–2026, ~95,000 words) and cross-checking the patterns
across five independent chronological passes. The patterns below held steady across seven years of
writing, so this is a real, stable voice, not a one-off tic. Full quoted evidence for every rule here
lives in `references/voice-notes.md` -- read it if you want more examples than fit below.

The goal is not to insert keywords from a list. It's to reproduce the underlying habit: **write like
you're narrating something that actually happened to you, out loud, and only afterward organize it
into headings.** Everything below follows from that one instinct.

## Before you start writing

Figure out which register this piece is:
- **A technical "I hit this / here's the fix" post** (the majority of the corpus) -- terser, more
  code, faster pace, staccato sentences.
- **A career/reflective/conference-recap piece** -- longer paragraphs, more personal/family detail,
  quoted epigraphs, more rhetorical questions used as section pivots.

Both share the same underlying voice; the technical register is just a tighter, faster version of it.

## How to open

Never open with throat-clearing ("In this article, I'll walk you through..."). Get straight into it
with one of:
- A one-or-two sentence personal hook that states what happened: "Recently, I was attempting to..."
  / "For a client project, I had..." / "A few days ago I had to search to find out..."
- A blockquoted error message, the literal question that prompted the piece, or a theme-setting
  quote, dropped in before the first heading.

## How to build sentences and paragraphs

- Default to short, plain declarative sentences. Save the ellipsis, not a semicolon or an em dash,
  for the pause-before-the-reveal move: "Then, everything changed ..." / "So, on to the second
  iteration ..." Use it as connective tissue mid-thought, not just as a trailing-off at the end.
- Open sentences and paragraphs with spoken-cadence connectors rather than subordinating them:
  "So,", "Then,", "Basically,", "Now,", "In fact,", "Additionally,", "Also,", "And,", "But,". These
  do the transition work that "however" or "furthermore" would do in a more formal register.
  (Compare this to the humanize-writing skill's advice to avoid "furthermore/moreover" -- for this
  voice specifically, the plainer conversational connectors are correct and the formal ones are not.)
- Stack short one-line sentences for a rhythmic punch, especially right after a longer explanatory
  passage: "This worked." / "I read them. I got angry." / "Problem solved."
- Use rhetorical questions to pivot into a new section, and usually answer them fast and plainly
  right after asking.

## How to structure the piece

- `##` headings in Title Case, short and generic and reusable: "The Problem," "The Solution," "A
  Failed Attempt," "Conclusion," "Summary." For a technical post, the Problem → Attempt → Failure →
  Resolution arc is a good default skeleton.
- End with `## Summary` or `## Conclusion` almost always. The distinctive move here: **have the
  closing section echo the opening** -- restate the core claim or list from the intro, close to
  verbatim, rather than introducing new synthesis. This reads as a deliberate bookend in the real
  corpus, not sloppiness -- don't "fix" it into a fresh restatement.
- Enumerable content (steps, causes, options, a recap of takeaways) goes into a numbered or bulleted
  list. Anecdote and framing stay in prose. Don't blend the two.
- For technical fixes, show the broken version and the working version as separate fenced code
  blocks with a short line of narration between them ("This worked." / "Here's the working version
  ..."), not a single annotated diff.
- If there's a repo or live demo, link it once near the top and it's fine to link it again near the
  bottom.

## How to handle emphasis

- Reach for bold-italic (`***word***`) on a term or claim you want to lean on hard -- this stands in
  for both italics and an em dash in this voice. Use plain **bold** for a first-use term definition
  or the one-sentence thesis of a paragraph. Save ALL CAPS for a rare, deliberate shout, not routine
  emphasis.

## How to handle voice and opinion

- Write in first person even for purely technical content. Frame the discovery as something that
  happened to you: "I got bit by...", "I was stumped for a minute," not "developers often
  encounter...".
- State an opinion as an opinion, then commit to it anyway: "In my opinion, X" / "I'm not saying this
  is for everyone, but I personally think Y" / "I firmly believe..." -- hedge the frame, not the
  conviction.
- Let self-deprecating humor land in a parenthetical aside, dry and quick, not a bit you announce:
  "(Sorry, lazily reused the same graphic above.)"
- It's fine, even good, to have a section that's just "here's where I was wrong" or "here's what
  failed" -- literal headings like "The Failure" or "A Failed Attempt" are on-brand, not a weakness
  to hide.
- A personal or family detail dropped in without ceremony (a spouse's one-liner, a kid's name used as
  sample data) is consistent with the voice -- don't sand it down into something more "professional."
- Close by inviting the reader in rather than asserting the last word: "Please let me know your
  thoughts." / "If anyone has a better pattern, let me know."
- Credit other people by name when a fix or idea came from them (a coworker, a Stack Overflow
  answer, a commenter). This voice shares credit generously and specifically.

## A worked mini-example

Generic AI-sounding version:
> When implementing debounce functionality in JavaScript, developers should be aware that the
> `setTimeout` reference must be cleared on each invocation. This is a common pitfall that can lead
> to unexpected behavior if not handled correctly.

Bob-voice version:
> Recently, I added a debounce to a search box and it just... didn't work. Every keystroke fired a
> request anyway.
>
> ## The Problem
>
> The `setTimeout` reference wasn't getting cleared. So, every call created a new timer instead of
> resetting the old one.
>
> ## The Fix
>
> ```javascript
> let timer;
> function debounce(fn, delay) {
>   clearTimeout(timer);
>   timer = setTimeout(fn, delay);
> }
> ```
>
> This worked.
>
> ## Summary
>
> I added a debounce to a search box, and the fix was clearing the old timer before setting a new
> one. Simple once you see it ... painful until you do.

For the full evidence behind every rule above -- direct quotes, article filenames, and the handful of
places the pattern *doesn't* hold -- see `references/voice-notes.md`.
