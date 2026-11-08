# With the skill vs without the skill

Same notes (`thermo-notes.pdf`), same kind of student answers, each run in a brand-new session.
Full transcripts: `test-runs/test-1-thermo-pdf.md` (with) and `test-runs/baseline-without-skill.md` (without).

To be fair: **without the skill, the agent was already good.** It asked one question at a time, noticed half-answers and explained mistakes well. The skill doesn't make it smarter. It makes it **behave like a real viva, the same way every time.**

| What I checked | Without the skill | With `/viva` |
|---|---|---|
| How many questions? | Never said. It kept adding Q1b, Q1c… | Says up front: "Asking 5 questions, one at a time." |
| How much of the notes was tested? | 3 exchanges, all on pages 1–2. It said itself that Carnot and entropy weren't touched. | 5 questions across pages 2, 4, 5 and 6, covering the first law, the Carnot theorem, a numerical and entropy. |
| Question style | Questions grew into 2–3 questions in one (Q2 asked three things) | One idea per question, easy to hard: recall → why → numerical → common mistake → connect |
| Numericals | Reused the numbers from the notes' own worked example | New numbers (800 K / 320 K), so you can't just remember the notes' answer |
| Half-right answer | Good follow-up question | One short probe, no answer given away. Same as the PDF preview: "Partly. … what about an ideal one?" |
| Wrong answer | A long explanation (about 100 words) | At most 3 sentences, then straight on to the next question |
| Score | None. It said "1 right, 1 partial, 1 wrong". | `Score: 2.5/5`, with half marks |
| Where to revise | General topic advice | A table with the exact page for each miss, plus one line: **"Revise page 5."** |
| Model answers | Only for the one it explained mid-viva | One or two lines for every question below full marks |
| Controls | None | `hint` (costs ½), `skip`, `stop`, `/viva notes 8 hard` |
| Same format next time? | Depends on the wording of your request | Same format on PDF, Markdown and text notes (Tests 1–3) |

## What got better, in three lines
1. **Coverage:** it tests the whole chapter, not just the first page.
2. **A real result:** a score out of 5 and the exact page to re-read, instead of a chat.
3. **Exam pressure:** short examiner replies with no lectures, and a hint costs marks, so it feels like a real viva.

## What the tests also caught
Test 3 found a bug. After `stop`, the skill scored an unanswered question (2/4 instead of 2/3). I made the rule in `SKILL.md` precise and re-ran it in a new session (Test 3b). It now gives the correct total and says which question was left out.
