# Test 1 — thermo-notes.pdf (PDF, default 5 questions)

Skill installed at `.claude/skills/viva/SKILL.md`. Checks: PDF reading, page numbers, partly-right probe, the classic "friction" mistake, hint, numerical with new numbers.

Run in a **brand-new agent session** (Claude Code CLI, `claude -p`, fresh folder, no memory of building the skill). The student answers were typed by a person playing a student; agent replies are copied exactly.

---

### Student
> /viva sample-notes/thermo-notes.pdf

### Agent
Reading notes. Asking 5 questions, one at a time.
(Type "hint" for a clue (costs half a mark), "skip" to move on, or "stop" to end early.)

Q1. State the first law of thermodynamics, and say what each symbol means, including the sign convention for W.

### Student
> Delta U = Q - W. U is internal energy, Q is heat and W is work.

### Agent
Examiner: Partly. The equation and symbols are right, but you haven't said which direction heat and work are counted. Whose heat is Q, and who does the work W?

### Student
> Q is heat added to the system and W is work done by the system on the surroundings.

### Agent
Examiner: Correct, that fixes the gap.

Q2. Why can't even a frictionless, ideal engine be more efficient than a Carnot engine?

### Student
> Because of friction

### Agent
Examiner: Not right. The question said frictionless, and the limit comes from the second law itself. A more efficient engine, paired with a reversed Carnot engine, would move heat from cold to hot with no work, which breaks the Clausius statement.

Q3. An engine takes heat from a source at 800 K and rejects it to a sink at 320 K. What is its maximum efficiency?

### Student
> 1 - 320/800 = 0.6, so 60%

### Agent
Examiner: Correct, 1 − 0.4 = 60%, and kelvin was the right unit to use.

Q4. A system's entropy decreases. Does that break the second law?

### Student
> hint

### Agent
Examiner: Think about what else is involved besides the system itself. The law's ∆S ≥ 0 applies to what kind of system?

### Student
> No, it only has to increase for an isolated system. Like water freezing - the surroundings gain more entropy.

### Agent
Examiner: Correct. Total entropy of system plus surroundings still rises. (Hint was used, so this question is capped at ½.)

Q5. Which two processes make up the adiabatic steps of a Carnot cycle, and what happens to temperature in each?

### Student
> adiabatic expansion where it heats up, and adiabatic compression where it cools down

### Agent
Examiner: Not right, you have them reversed. In adiabatic expansion the gas cools from T1 to T2, and in adiabatic compression it warms from T2 back to T1.

Score: 2.5/5.

| Q | Topic | Mark | Revise |
|---|-------|------|--------|
| 1 | First law and sign convention | 1 | — |
| 2 | Why Carnot's limit isn't about friction | 0 | page 5 |
| 3 | Carnot efficiency calculation | 1 | — |
| 4 | Entropy decrease and the second law | ½ | page 6 |
| 5 | Adiabatic steps of the Carnot cycle | 0 | page 5 |

Strongest: Applying the Carnot formula, with temperatures in kelvin.
Weakest: Carnot engine concepts (Q2 and Q5). Both lost full marks, and you reversed the temperature changes in the adiabatic steps.
Revise page 5.

Model answers for anything below 1:
- Q2: The limit comes from the second law, not from friction. A more efficient engine, run with a reversed Carnot engine, would move heat from cold to hot with no work, which breaks the Clausius statement.
- Q4: No. ∆S ≥ 0 applies to an isolated system, so a system's own entropy can fall (e.g. water freezing) if the surroundings gain more.
- Q5: Adiabatic expansion cools the gas from T1 to T2. Adiabatic compression warms it from T2 back to T1.

Type /viva again for a new set of questions.
