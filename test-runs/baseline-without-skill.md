# Baseline — same task WITHOUT the skill

Same PDF, same kind of answers, fresh session with **no skill installed**. Prompt: *Give me a viva on my notes in sample-notes/thermo-notes.pdf*

Run in a **brand-new agent session** (Claude Code CLI, `claude -p`, fresh folder, no memory of building the skill). The student answers were typed by a person playing a student; agent replies are copied exactly.

---


### Student
> Give me a viva on my notes in sample-notes/thermo-notes.pdf

### Agent
Let's begin. I'll ask one question at a time, starting with the basics. Answer in your own words; short is fine.

**Q1.** Your notes say heat (Q) and work (W) are *not* state variables, but internal energy (U) is. What does that mean, and why does it matter for the first law?

Send your answer and I'll respond, then move on. I'll build up to harder questions on the Carnot theorem and entropy.

### Student
> they depend on the path

### Agent
Correct, but that's only half of it. Q and W depend on the path, while U depends only on the state.

**Q1b.** The first law is ∆U = Q − W. If Q and W each change with the path, why can the first law still hold for every path between the same two states? What stays the same, and what does that tell you about Q − W?

### Student
> Because of friction

### Agent
Not quite. Friction isn't involved here, and it doesn't appear in the first law at all.

Here's the key idea. ∆U depends only on the initial and final states, so it's the same for every path between them. Q and W can each differ from path to path, but they change together. Whatever extra heat goes in along one path comes out as extra work, so Q − W always equals the same ∆U.

Your own example shows it. The gas absorbs 500 J and does 200 J of work, so ∆U = 300 J. A different path between the same two states might absorb 700 J, but then it must do 400 J of work.

**Q1c (a quick retry).** Take the same two states as that example, so ∆U = 300 J. If a different path has the gas do 350 J of work, how much heat must it absorb?

### Student
> 650 J

### Agent
Correct. ∆U = Q − W gives Q = 300 + 350 = 650 J. Q and W changed, but Q − W stayed at 300 J.

**Q2.** Your notes say that for an isothermal process on an ideal gas, Q = W. Why is ∆U = 0 there? Then say what you'd expect for an adiabatic expansion, and why the gas cools.

### Student
> stop, how did I do?

### Agent
Here's where you stand after 3 questions, which cover only the first page or two of your notes.

**Q1: state variables vs path-dependent ones.** You got "they depend on the path" right. You didn't mention that U depends only on the state, so I'd call this partial.

**Q1b: why the first law holds on every path.** You said "because of friction", which is wrong. I had to give you the explanation: Q and W vary together, so Q − W stays equal to ∆U. This is your weak spot so far. You can recite that Q and W are path-dependent, but you didn't connect that to why the first law still holds.

**Q1c: Q for a path with W = 350 J.** You got 650 J, which is correct. Once the idea was explained, you applied it right away, so the gap looks like understanding rather than arithmetic.

**Overall:** 1 clean right answer, 1 partial, 1 wrong. I haven't tested most of your notes yet. That includes the processes, the second law, the Carnot theorem and entropy, and the Carnot theorem and entropy are the parts I expected to be hardest. So this isn't a verdict on the whole unit.

**What to revise:**
- Why ∆U is path-independent while Q and W aren't, and how that makes Q − W constant.
- Be ready to give the reason, not just the fact. "They depend on the path" was the fact, but the viva questions will ask why.

I can pick the viva back up at Q2 (isothermal and adiabatic processes), or skip ahead to Carnot and entropy if you'd rather.
