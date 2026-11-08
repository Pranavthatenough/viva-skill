# Test 2 — current-electricity-notes.md (Markdown, 4 questions, hard)

Checks: options (question count + difficulty), section headings instead of page numbers, probe that the student fails.

Run in a **brand-new agent session** (Claude Code CLI, `claude -p`, fresh folder, no memory of building the skill). The student answers were typed by a person playing a student; agent replies are copied exactly.

---


### Student
> /viva sample-notes/current-electricity-notes.md 4 hard

### Agent
Reading notes. Asking 4 questions, one at a time.
(Type "hint" for a clue (costs half a mark), "skip" to move on, or "stop" to end early.)

Q1. Electrons drift at about 1 mm/s, yet a bulb lights immediately. Explain why.

### Student
> Because electrons move very fast in the wire

### Agent
Examiner: Not right. Electrons drift at only about 1 mm/s. The bulb lights instantly because the electric field travels through the wire at almost the speed of light, pushing all the free electrons at once.

Q2. A wire is stretched to three times its length at constant volume. By what factor does its resistance change?

### Student
> Length 3x and area becomes 1/3, so R = rho L/A goes up 9 times

### Agent
Examiner: Correct. Length ×3 and area ÷3 give 3 × 3 = 9 times the resistance.

Q3. Why does a car's headlight dim when the starter motor draws a large current?

### Student
> because the battery voltage drops

### Agent
Examiner: Partly. The terminal voltage does drop, but what inside the battery causes that drop?

### Student
> not sure, the battery gets weak?

### Agent
Examiner: Not quite, so ½ at best. The battery has internal resistance r, so terminal voltage V = ε − Ir falls when the large current flows.

Q4. Three identical resistors R are connected in parallel. What is the total resistance, and what happens to the total current from a fixed supply?

### Student
> R/3, and current becomes 3 times because I = V/R

### Agent
Examiner: Correct. The parallel total is R/3, so with the same voltage the current is three times what one resistor would draw.

Score: 2.5/4.

| Q | Topic | Mark | Revise |
|---|-------|------|--------|
| 1 | Drift speed vs. instant bulb response | 0 | Section "1. Current and drift" |
| 2 | Stretched wire and resistance | 1 | — |
| 3 | Internal resistance and dimming headlights | ½ | Section "7. EMF and internal resistance" |
| 4 | Resistors in parallel | 1 | — |

Strongest: Applying R = ρL/A to a stretched wire, with the length and area changes handled correctly.
Weakest: Why a bulb lights instantly even though electrons drift slowly. You said the electrons move fast, but it's the electric field that travels quickly.
Revise section "1. Current and drift".

Model answers for anything below 1:
- Q1: Electrons drift at only about 1 mm/s. The electric field travels through the wire at almost the speed of light and pushes all the free electrons at once, so the bulb lights immediately.
- Q3: The battery has internal resistance r. A large current from the starter motor makes the terminal voltage V = ε − Ir fall, so the headlights get less voltage and dim.

Type /viva again for a new set of questions.
