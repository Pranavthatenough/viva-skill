# Test 3 — photosynthesis-notes.txt (plain text, skip + stop)

Checks: plain-text notes, "skip", "stop" early. **This run found a bug**: after stop it said Q4 wasn't counted but still scored /4. The rule was fixed in SKILL.md — see Test 3b.

Run in a **brand-new agent session** (Claude Code CLI, `claude -p`, fresh folder, no memory of building the skill). The student answers were typed by a person playing a student; agent replies are copied exactly.

---


### Student
> /viva sample-notes/photosynthesis-notes.txt

### Agent
Reading notes. Asking 5 questions, one at a time.
(Type "hint" for a clue (costs half a mark), "skip" to move on, or "stop" to end early.)

Q1. Which source does the oxygen released in photosynthesis come from, and how was this shown?

### Student
> From water. Ruben and Kamen used O-18 labelled water and the labelled oxygen came out.

### Agent
Examiner: Correct, the labelled oxygen appeared in the O2 released, so it came from water, not CO2.

Q2. Why does the Calvin cycle stop shortly after dark, even though it needs no light directly?

### Student
> skip

### Agent
Examiner: Skipped, no mark. The Calvin cycle needs ATP and NADPH, which only the light reaction makes, so without light the supply runs out and the cycle stops.

Q3. A plant makes 3 glucose molecules. How many ATP and NADPH does the Calvin cycle use?

### Student
> 54 ATP and 36 NADPH

### Agent
Examiner: Correct. Each glucose takes 18 ATP and 12 NADPH, so three glucose take 54 and 36.

Q4. Can photorespiration help a plant make sugar or ATP?

### Student
> stop

### Agent
Score: 2/4. (Q4 was not answered, so it is not counted.)

| Q | Topic | Mark | Revise |
|---|-------|------|--------|
| 1 | Source of O2 (Ruben and Kamen) | 1 | — |
| 2 | Calvin cycle depends on the light reaction | 0 | section "Dark reaction / Calvin cycle" |
| 3 | ATP and NADPH per glucose | 1 | — |
| 4 | Photorespiration | not answered | section "Photorespiration" |

Strongest: You recalled the O-18 experiment accurately and scaled the Calvin cycle numbers correctly.
Weakest: You skipped the link between the Calvin cycle and the light reaction.
Revise section "Dark reaction / Calvin cycle".

Model answers for anything below 1:
- Q2: The Calvin cycle needs ATP and NADPH from the light reaction. Without light those run out, so the cycle stops soon after dark.
- Q4: No. Photorespiration happens when RuBisCO binds O2 instead of CO2. It wastes energy and releases CO2, and it makes no sugar and no ATP.

Type /viva again for a new set of questions.
