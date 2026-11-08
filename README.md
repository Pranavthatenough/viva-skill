# Project 16 · Your Own Skill — `/viva`

**Section D · Video, skills and design** — GenAI Internship, Week 2, Bharat Space Education Research Centre

`/viva` turns your AI agent into a viva examiner. Give it your notes and it:
1. reads the whole file (PDF, Markdown, text or Word),
2. asks questions **one at a time**, from easy to hard,
3. probes a half-right answer once, without giving the answer away,
4. finishes with a **score**, a table of what you missed, and **"Revise page N"**.

```
> /viva thermo-notes.pdf
Reading notes. Asking 5 questions, one at a time.
Q2. Why can't even a frictionless, ideal engine be more efficient than a Carnot engine?
> Because of friction
Examiner: Not right. The question said frictionless, and the limit comes from the second law itself...
...
Score: 2.5/5.
Revise page 5.
```

## Install

The whole skill is one file: `viva/SKILL.md`.

**Claude Code**
- For one project: copy the `viva` folder to `<your project>/.claude/skills/viva/`
- For every project: copy it to `~/.claude/skills/viva/`

Then start a new session and type `/viva yournotes.pdf`.

**Claude app (claude.ai)**
Go to Settings → Capabilities → Skills, and upload `viva.zip` (included). Then attach your notes in a new chat and type `/viva`.

**Other agents**
Paste the contents of `SKILL.md` as custom instructions, then send your notes.

## How to use it
| Type | What happens |
|---|---|
| `/viva notes.pdf` | 5 questions, normal difficulty |
| `/viva notes.md 8 hard` | 8 questions, more "why" and "connect" questions |
| `hint` | a small clue; that question is capped at ½ mark |
| `skip` | 0 marks, it tells you the answer, moves on |
| `stop` | ends now and scores only what you answered |

## Done when — checklist

- [x] **It starts correctly in a fresh session.** Every test was run with the agent CLI in a brand-new session, in a clean folder, with only the skill installed. Each time it read the file and opened with exactly *"Reading notes. Asking N questions, one at a time."*
- [x] **It works well on 3 different inputs**, all in `sample-notes/`:

  | Test | Input | What it checked | Result |
  |---|---|---|---|
  | 1 | `thermo-notes.pdf` (PDF, 6 pages) | page numbers, probe, hint, new-number numerical | 2.5/5, "Revise page 5". All pages were correct. |
  | 2 | `current-electricity-notes.md` (4 hard) | options, section headings instead of pages, failed probe | 2.5/4, "Revise section 1. Current and drift" |
  | 3 | `photosynthesis-notes.txt` | skip, stop | **found a bug** in stop scoring, which I fixed |
  | 3b | same file, re-run after the fix | stop scoring, off-topic answer, new questions on repeat | 0/2, with the unanswered Q3 correctly left out |

- [x] **Run the same task without the skill. Show what got better.** See `comparison.md`. In short, the skill:
  - tests the whole chapter instead of just page 1,
  - gives a real score and the exact page to revise,
  - keeps replies short like a real examiner.

## Folder contents
```
viva/SKILL.md          the skill (this is the whole thing)
viva.zip               same folder, zipped for uploading to the Claude app
sample-notes/          3 harmless sample notes (PDF, Markdown, text)
make_thermo_pdf.py     script that made the sample PDF
test-runs/             exact transcripts of every test + the no-skill baseline
comparison.md          with-skill vs without-skill
prompts.md             every prompt used, in order
```

## How the skill works (so you can explain it)
- **The `description` line** in the top of `SKILL.md` is what the agent reads to decide *when* to use the skill. It names the trigger (`/viva`, "quiz me", "test me on my notes") and what it does.
- **Step 1–2 happen silently.** It reads everything and plans a mix of questions (recall, why, apply, misconception, connect) before asking anything. That's why it covers the whole chapter.
- **"Only ONE question per message"** is written in bold because that's the rule agents break most often.
- **A marking table (1 / ½ / 0)** makes scores consistent instead of a vague "good job".
- **The final report format is spelled out exactly**, so the output looks the same on every input.
- **A "Never" list** at the end blocks the common failure modes, like inventing page numbers or asking about things that aren't in the notes.

All notes are made-up sample notes, not real coursework.
