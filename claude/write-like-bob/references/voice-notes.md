# Bob Fornal Voice Notes — Full Corpus Evidence

Derived from reading all 121 dev.to articles at https://dev.to/rfornal (2019–2026, ~95,000 words),
split into 5 chronological batches and analyzed independently, then cross-checked. Every pattern
below showed up consistently across all 5 batches spanning 7 years, not just a couple of articles —
this is a stable, long-running voice, not a phase.

Use this file when you want the receipts behind a rule in SKILL.md, or when you need more example
phrasing than the main file carries. Organized by the same 5 dimensions each batch was analyzed on.

## 1. Sentence-level habits

**The ellipsis is the single most identifiable fingerprint in this corpus.** It shows up in nearly
every article, multiple times, used mid-sentence as a pause or pivot -- not just a trailing-off:
- "Then, everything changed ..."
- "And ... something in my brain clicked."
- "So, on to the second iteration ..."
- "Now, examining a possible test ..." (used ~8 times verbatim as an opener in one article)
- "No. Not what you think." (a fragment, then a pause, then the reveal)

**Sentence-openers that function as spoken-aloud connective tissue** rather than grammatical
subordination -- "So,", "Then,", "Basically,", "Now,", "Additionally,", "In fact,", "Certainly,",
"Also,", "And,", "But,":
- "So, I decided to test this out myself."
- "Basically, this issue was about scope."
- "Then, someone said, 'this should be an open-source library.'"
- "In fact, it was several years before I caught the PWA bug..."
- "And, what we can do with NOW can make our past right..."

**Short, staccato one-line sentences or paragraphs, often stacked for rhythm**, usually right after
a longer build-up:
- "This worked." / "It failed." / "I was perplexed." / "Problem solved."
- "I read them. I got angry."
- "The issue was that it wasn't my code. The issue was that it wasn't always great code."
- "Yes. I said Bull Semen."

**Rhetorical questions**, frequently used as section pivots or headings, often answered immediately
and tersely: "Does this mean technical debt should never be accrued? Yes and no." / "Is there a
place for AI in the coding world?" (asked at both the open and close of one piece).

**Deliberate fragments** as staging devices before code or lists ("Here's the code.", "Setup code
here ..."), and as standalone punchlines ("No real surprise.", "That's enough.").

## 2. Structural conventions

**Opens in medias res, almost never with throat-clearing.** No "In this article, I'll show you...".
Instead: a one-or-two sentence personal hook ("Recently, I was attempting to sum the values of an
array..."), or a blockquoted error message / question / theme line right before the first heading
("&gt; VirtualizedList: missing keys for items...", opening with the literal error text).

**Closes with `## Summary` or `## Conclusion`** (used interchangeably, occasionally "Conclusions"
plural) in the large majority of articles -- close to a template, though not universal; a handful of
short "notes to self" pieces just trail off instead.

**The single most distinctive structural habit: the closing section often echoes the opening almost
verbatim** -- a deliberate bookend. Real examples of this near-repetition:
- Opens: "Being able to import JSON files can make development easier..." / Summary: "Being able to
  import and process JSON files can make development easier, more efficient, and overall a better
  experience when used correctly..."
- An 8-item list stated in the intro reappears unchanged in the Summary.
- "I firmly believe there is..." opens an article; "I also firmly believe..." closes it.

**Headings are generic, reusable, Title Case noun phrases**: "The Problem," "The Solution," "The
Issue," "A Failed Attempt," "Conclusion," "Summary." A recognizable arc recurs across many technical
articles: Problem → Attempt → Failure → Resolution, each as its own heading.

**Lists carry the enumerable payload; prose carries the anecdote.** Steps, causes, pros/cons, and
especially "recap" content at the end of an article get turned into numbered or bulleted lists, even
inside an otherwise narrative piece.

**Bold-italic (`***word***`) is a signature typographic tic**, functioning almost like verbal
air-quotes around jargon, proper nouns, or a word he wants to lean on hard: ***only***, ***never***,
***trigger***, ***my own opinion***, ***NOT SOMETHING I WOULD RECOMMEND***. Plain bold marks a
first-use term definition or the "thesis" phrase of a paragraph. ALL-CAPS shows up occasionally for
a shouted beat ("PERFECT!", "EYES WIDE OPEN").

**Code blocks are always fenced with a language tag**, often with the filename as its own line right
before the fence, and frequently structured as a before/after or BAD/GOOD/OK contrast, sometimes with
inline comments labeling the teaching intent directly (`/* BAD PATTERN */`, `/* GOOD PATTERN */`).

**A repo/demo link section** (`* [DEMO HERE](...)`, `* [REPO HERE](...)`) shows up often, sometimes
near the top and again near the bottom of the same article.

## 3. Recurring words and phrases (a phrasebook, not a mandate)

These aren't things to force into every piece -- they're evidence of the register. Reach for one or
two, not all of them:

- "Basically, ..." / "So, ..." / "Then, ..." / "Now, ..." / "In fact, ..." / "Certainly, ..." as
  paragraph or sentence openers.
- "I decided to ..." / "I recently ..." / "Recently, I ..." as a way into a technical story.
- "A quick search found ..." (his version of "I googled it").
- "Here's a look at ..." / "Here's the code that ..." as a code-intro tic.
- "As you can see, ..." after a code block.
- "Problem solved." as a closing beat.
- "I'm not saying this is for everyone, but I personally think ..." / "In my opinion, ..." / "These
  conclusions are ***my own opinion***" as an opinion-hedge formula.
- "I firmly believe ..." as a hedge-but-commit phrase.
- "Please let me know your thoughts." / "If anyone has a better pattern, let me know." as a
  direct-address closer.
- "I hope this helps as you move forward." / "I hope you found this useful." as a closing courtesy.
- "Notes for myself" or "this is intended primarily for myself" as a reason-to-exist framing for a
  post.
- Numeral-then-parenthetical-digit habit: "two (2) issues and one (1) bug."
- Generous, specific credit to named people (Stack Overflow answerers, coworkers, commenters) rather
  than presenting a fix as solely his own.

## 4. Tone and voice

**First person, anecdote-driven, even in pure technical reference material.** A JS quirk isn't
presented as a neutral fact -- it's framed as something that happened to him: "I got bit by a simple
logic issue," "I was stumped for a minute." Reads like a trip report, not documentation.

**Self-deprecating, dry, deadpan humor**, usually tucked into a parenthetical rather than announced:
"(Sorry, lazily reused the same graphic above.)" / "(yes, a company that collects bull semen for
artificial insemination)" / "my designs are rudimentary, at best."

**Comfortable admitting mistakes and failure in public**, sometimes as literal section headings
("The Failure," "A Failed Attempt"): "We all failed miserably." / "That's what I get for assuming
from a Stack Overflow example."

**Opinions are explicitly flagged as opinion, then stated firmly anyway.** He doesn't claim neutral
authority -- he says "this is my opinion" and then commits to a clear position in the same breath:
"It is my humble opinion that everyone on the team should be included in the code reviews." /
"**Semicolons should be included when writing JavaScript.**"

**Family and personal life bleed into technical posts** without ceremony -- a wife's one-liner
becomes a section of a CSS debugging story, a son's name becomes sample data in a destructuring
example, a conference recap turns into a family travelogue.

**Direct, collaborative reader address**: "Now, let's look at some code." / "If anyone out there
knows where this came from, I would be happy to attribute it here." Invites disagreement rather than
asserting the last word.

## 5. Punctuation fingerprint

- **Ellipsis over em dash.** Where another writer reaches for an em dash, this corpus reaches for
  "..." instead. True em dashes are rare in his own prose -- they show up mainly inside quoted
  epigraphs from other people, or in more "polished" conference-recap sections, suggesting a register
  shift between raw voice and edited voice.
- **Spaced hyphens ("word - word")** sometimes substitute for a dash in casual/technical posts.
- **Bold-italic triple-asterisk** for emphasis, distinct from and more common than plain italics.
- **Parentheticals constantly, for asides, jokes, or qualifiers** -- not subordinate clauses.
- **Scare quotes** around borrowed, ironic, or informal terms ("attempt," "hate," "pixel-perfect,"
  "zombie-scrum") to flag a phrase as someone else's framing or a knowingly loose usage.
- **Semicolons used sparingly**, mostly to join two short, tightly related independent clauses for a
  contrast beat, not for complex compound sentences.
- Mild, authentic grammatical looseness (a dangling parenthesis, an informal comma splice) shows up
  in the real corpus and reads as part of the unedited, conversational texture -- this is evidence of
  how unpolished the voice is, not an instruction to inject typos on purpose.
