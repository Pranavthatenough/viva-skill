# Test 3b — retest after fixing the stop rule (5 questions, easy)

Checks: stop scoring is now correct (Q3 unanswered → left out → 0/2). Also: an off-topic answer is recognised; different questions from Test 3 on the same notes.

Run in a **brand-new agent session** (Claude Code CLI, `claude -p`, fresh folder, no memory of building the skill). The student answers were typed by a person playing a student; agent replies are copied exactly.

---


### Student
> /viva sample-notes/photosynthesis-notes.txt 5 easy

### Agent
Reading notes. Asking 5 questions, one at a time.
(Type "hint" for a clue (costs half a mark), "skip" to move on, or "stop" to end early.)

Q1. Write the overall equation for photosynthesis, and say where the oxygen released comes from.

### Student
> Chlorophyll absorbs blue and red light and reflects green

### Agent
Examiner: That's true, but it doesn't answer the question. The equation is 6CO2 + 12H2O → C6H12O6 + 6O2 + 6H2O (light, chlorophyll), and the oxygen comes from water, not CO2.

Q2. Why does the Calvin cycle, though called the "dark reaction", still run during the day?

### Student
> skip

### Agent
Examiner: The Calvin cycle needs ATP and NADPH, which only the light reaction makes, so it runs in the day.

Q3. Which enzyme carries out carboxylation in the Calvin cycle, and how many 3-PGA molecules does one CO2 plus RuBP produce?

### Student
> stop

### Agent
Score: 0/2.
1 question (Q3) was asked but not answered, so it's left out of the total.

| Q | Topic | Mark | Revise |
|---|-------|------|--------|
| 1 | Overall equation and source of O2 | 0 | section "What it is" |
| 2 | Why the "dark reaction" needs daytime | 0 | section "Dark reaction / Calvin cycle" |

Strongest: You know chlorophyll absorbs blue and red light and reflects green, but that wasn't what Q1 asked.
Weakest: Q1. The equation and the origin of the oxygen were missing, and this is the core idea of the topic.
Revise section "What it is".

Model answers for anything below 1:
- Q1: 6CO2 + 12H2O → C6H12O6 + 6O2 + 6H2O, with light and chlorophyll. The O2 comes from water, shown with O-18 labelled water.
- Q2: The Calvin cycle needs ATP and NADPH made in the light reaction, so it can only run while those are being supplied, which is in the day.

Type /viva again for a new set of questions.
