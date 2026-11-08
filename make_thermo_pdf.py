"""Builds sample-notes/thermo-notes.pdf — harmless sample notes used to test the /viva skill."""
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

pages = [
 ("Thermodynamics — Unit notes (Sem 4)", [
  "<b>System and surroundings.</b> A system is the part of the universe we study; everything else is the surroundings. An open system exchanges mass and energy, a closed system exchanges only energy, and an isolated system exchanges neither.",
  "<b>State variables.</b> Pressure (P), volume (V), temperature (T) and internal energy (U) describe the state of a system. They depend only on the state, not on how the system got there. Heat (Q) and work (W) are NOT state variables — they depend on the path.",
 ]),
 ("Zeroth and first law", [
  "<b>Zeroth law.</b> If A is in thermal equilibrium with C, and B is in thermal equilibrium with C, then A and B are in thermal equilibrium with each other. This is why a thermometer works.",
  "<b>First law.</b> ΔU = Q − W, where Q is heat added to the system and W is work done BY the system. It is the law of conservation of energy applied to heat and work.",
  "Example: a gas absorbs 500 J of heat and does 200 J of work on a piston. ΔU = 500 − 200 = 300 J.",
 ]),
 ("Thermodynamic processes", [
  "<b>Isothermal</b> (constant T): for an ideal gas ΔU = 0, so Q = W. Work = nRT ln(V2/V1).",
  "<b>Adiabatic</b> (Q = 0): ΔU = −W. Gas cools when it expands. PV^γ = constant, where γ = Cp/Cv.",
  "<b>Isochoric</b> (constant V): W = 0, so ΔU = Q.",
  "<b>Isobaric</b> (constant P): W = PΔV.",
  "On a P–V diagram, the work done is the area under the curve. An adiabatic curve is steeper than an isothermal curve through the same point.",
 ]),
 ("Second law and heat engines", [
  "<b>Kelvin–Planck statement.</b> No engine working in a cycle can turn all the heat it takes in into work. Some heat must always be rejected to a colder sink.",
  "<b>Clausius statement.</b> Heat cannot flow by itself from a colder body to a hotter body. A refrigerator needs work input to do this.",
  "<b>Efficiency of a heat engine:</b> η = W / Q1 = 1 − Q2/Q1, where Q1 is heat taken from the hot source and Q2 is heat rejected to the cold sink.",
 ]),
 ("Carnot engine", [
  "The Carnot cycle has four reversible steps: isothermal expansion at T1, adiabatic expansion (T1 → T2), isothermal compression at T2, adiabatic compression (T2 → T1).",
  "<b>Carnot efficiency:</b> η = 1 − T2/T1 (temperatures in kelvin).",
  "<b>Carnot's theorem.</b> No engine working between the same two temperatures can be more efficient than a reversible (Carnot) engine. If one could, combining it with a reversed Carnot engine would move heat from cold to hot with no work — breaking the second law. So the limit comes from the second law itself, not from friction.",
  "Real engines are less efficient because of friction, heat leaks and irreversible processes — but even an ideal, frictionless engine cannot beat Carnot.",
  "Example: T1 = 500 K, T2 = 300 K. η = 1 − 300/500 = 0.4 = 40%.",
 ]),
 ("Entropy", [
  "<b>Entropy (S)</b> measures how spread out energy is. For a reversible process, ΔS = Q/T.",
  "For an isolated system, entropy never decreases: ΔS ≥ 0. It stays constant only for reversible processes.",
  "Example: 1000 J of heat flows from a 400 K body to a 200 K body. ΔS = −1000/400 + 1000/200 = −2.5 + 5 = +2.5 J/K. Positive, so the process happens on its own.",
  "<b>Common mistake:</b> entropy of a system CAN decrease (e.g. water freezing), as long as the entropy of the surroundings increases by more.",
 ]),
]
st = getSampleStyleSheet()
def footer(c, d):
    c.setFont("Helvetica", 9); c.drawCentredString(A4[0]/2, 25, f"Page {d.page}")
doc = SimpleDocTemplate("sample-notes/thermo-notes.pdf", pagesize=A4, title="Thermodynamics notes")
story = []
for i, (h, paras) in enumerate(pages):
    story.append(Paragraph(h, st["Heading1"]))
    for p in paras: story += [Paragraph(p, st["BodyText"]), Spacer(1, 8)]
    if i < len(pages) - 1: story.append(PageBreak())
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("ok")
