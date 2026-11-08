# prompts.md — Project 16: Your Own Skill (/viva)

Agent used: Claude (Opus 5.5) to build, and Claude Code CLI in fresh sessions to test. Prompts are in order.

---

### Prompt 1 — Pick the skill and make test inputs
> I'm doing Project 16 and picking /viva. First make 3 harmless sample notes files to test it on, each in a different format: a 6-page thermodynamics PDF with page numbers (include the Carnot theorem and a "common mistake" about entropy), a Markdown file on current electricity with numbered sections, and a plain-text file on photosynthesis. Make them read like real student notes, with worked examples.

### Prompt 2 — Write the skill
> Write a skill at viva/SKILL.md. It should:
> - read my whole notes file first (PDF, md, txt), remembering page numbers or section headings
> - silently plan N questions (default 5), easy to hard, mixing recall, why, apply (with numbers different from the notes), common mistake and connect
> - ask ONE question at a time and wait
> - reply like a strict but fair examiner in at most 3 sentences; if I'm partly right, ask one probing follow-up without giving the answer
> - support hint (costs half a mark), skip and stop, plus options like "/viva notes.pdf 8 hard"
> - end with Score: X/N, a table with the page to revise for each miss, "Revise page N", and short model answers
>
> Write the description line carefully, because it decides when the skill runs.

### Prompt 3 — Test in a fresh session
> Install the skill in a clean folder and test it in a brand-new agent session that knows nothing about this chat. Run it on all 3 notes files. I'll play the student and give a mix of right, half-right and wrong answers, and try hint, skip and stop. Save every transcript exactly.

### Prompt 4 — Fix what broke
> In test 3, after "stop" it said Q4 wasn't counted but still scored 2/4. Fix the rule in SKILL.md so unanswered questions are left out of the total, and stop it hinting at per-question marks mid-viva. Then re-test the stop case in a new fresh session.

### Prompt 5 — Without the skill
> In another fresh folder with NO skill installed, run the same task on the same PDF: "Give me a viva on my notes in sample-notes/thermo-notes.pdf". Give similar answers. Then write comparison.md, a fair table of what the skill changed and what was already fine without it.

### Prompt 6 — Package
> Write a README with install steps, how to use it, the Done-when checklist with evidence, and a short "how it works" section so I can explain it. Zip the skill folder for uploading to the Claude app.
