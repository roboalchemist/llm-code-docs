# Source: https://docs.flux.ai/tutorials/advanced-designer.md

# Advanced Designer


**You’re advanced if:**

- You care about signal integrity, EMC, thermal management, and manufacturing constraints
- You design high-density boards or work in production environments
- You already know what you’re doing—you just need to know how to do it _in Flux_


#### Introduction

This guide is for professional EEs who want to cut the labor out of complex designs in Flux. You’ll pair Flux with stackup‑driven controls, Layout Rules, and Knowledge Base (KB) to move faster while keeping engineering review in the loop.p.

- **Outcome:** Ship high‑speed, constraint‑heavy boards faster without sacrificing rigor.
- **Assumes:** You’re comfortable with the Intermediate flow (rules, polygons/keep‑outs, diff‑pairs intro, multi‑rail power). See [Intermediate §3–5] if needed.

Tip: Importing from Altium/Cadence? See §2.1 Parity & Migration to bring schematics forward and re‑layout in Flux.

### 1) Reliability with Flux


#### 1.1 What to expect

Strong today
Schematic/system reasoning, plan synthesis, calculations, reviews.

Use with review
Dense HS routing and tight‑tolerance clearances.

**Limitations to plan around**

- Context is thread‑scoped.
- Knowledge may lag brand‑new parts/standards.
- Complex tasks work best when decomposed.

**Workflow pattern**

1. Ask for plan + assumptions + alternatives
2. Reference datasheets (@file); request calculations + rationale
3. Apply scoped edits (one rail/bus/block); review between steps
4. Capture final decisions in KB

Learn more:


#### 1.2 Context‑first prompting (examples)

**Isolated Flyback (18–72 V → 12 V @ 0.8/1.2 A)**


> `Select PWM/integrated flyback IC; design/choose transformer; size snubber/clamp; choose I/O caps, rectifier, opto/PSR feedback; EMI input filter. Follow app notes; meet isolation ≥1.5 kVrms and η > 85%. Include creepage/clearance guidance, Y‑cap, CM choke.`


**USB‑C PD from 24 V (two‑IC control architecture)**


> `Convert 24 V to PD source (5/9/12 V up to 18 W). Attach PD controller + buck datasheets. Show interface (comp‑pin behavior, control scheme); calculate peripherals; justify selections. Meet ripple/transient per PD spec; 400 kHz–1.5 MHz; mechanical limits; optimize for small SMD + cost.`


Helpful follow‑ups

- “List assumptions, unknowns, and two alternatives.”
- “Produce a bring‑up checklist and test points.”
- “Generate KB entries for decisions we’ll reuse.”
Related:

### 2) High‑Speed & Constraint‑Driven Layout


#### 2.1 Differential pairs (advanced)

What it is
Paired routing with controlled impedance/length and bounded skew for HS interfaces.

**How it works in Flux**

- Dual‑trace routing when you start from a diff‑pair pad.
- Skew controls: PN Skew Max (intra‑pair) and Pair‑to‑Pair Skew Max (bus‑level).
- Stackup‑driven Z; automatic shape mirroring; return‑path awareness via planes.
- Naming conventions auto‑recognize USB/HDMI/PCIe/MIPI/DDR3/4 pairs.

**Checklist**

- Lock stackup + target Z/tolerances.
- Confirm pair nets; route from pad; watch live length/Z in Properties.
- Tune length; verify uninterrupted return paths.

Learn more:


#### 2.2 Impedance strategies (stackup, calculators, pours)

What it is
Correct widths/spacing driven by your stackup—no hand calculators.

**How it works in Flux**

- Stackup Editor with fab‑aligned templates (e.g., JLCPCB); editable materials.
- Assign target Z (Ω, tolerance) → Flux computes width/spacing automatically.
- Reference planes via pours; live Z in Properties.

**Checklist**

- Choose/edit stackup; lock early; reuse across variants.
- Assign impedance to nets/pairs; confirm computed geometry.
- Keep planes continuous; stitch across slots/crossings; re‑verify Z after edits.

Learn more:


#### 2.3 Power integrity (PI): PDN, stitching, copper balance, thermals

What it is
Practical PI controls to avoid solver‑heavy loops.

**How it works in Flux**

- Ground pours across layers for short returns/shielding.
- Via stitching/fields to tie planes and spread current/heat.
- Thermal relief rules; copper balance to reduce warp risk.
- Custom polygons to shape high‑current paths.

**Checklist**

- Tighten high‑di/dt loops; avoid plane interruptions under HS nets.
- Stitch near layer changes and around cutouts.
- Size thermal spokes to package dissipation.

Learn more:

### 3) Parity, System‑Level Flow, and KB at Scale


#### 3.1 Parity & migration (Cadence/Altium → Flux)

What transfers
Schematics via EDIF (Cadence) or ASCII (Altium): symbols, nets, values, refs. PCB routing does not transfer—plan to re‑layout.

Flow
Export → Import in Flux → verify symbols/params → re‑establish diff‑pair/Z constraints → proceed to placement/routing with rules + AI reviews.

Learn more:


#### 3.2 Multi‑rail / multi‑IC orchestration

What it is
Integration planning and execution with Flux as a design‑decision partner.

**How to run it**

- Front‑load context (rails, budgets, interfaces, acceptance criteria).
- Attach datasheets with @file; ask for an integration plan before calculations.
- Lock constraints first (PDN targets, timing, keep‑outs).
- Execute stepwise: one rail/bus/block → review → commit.

Learn more:


#### 3.3 Knowledge Base (KB) at scale

What it is
A way to stop re‑deciding solved decisions and make results repeatable.

**Use KB for**

- Component/library standards; naming conventions; review checklists.
- User‑level preferences reused across projects.
- Project‑level constraints/decisions that override user‑level.
- Curate Flux‑suggested entries; prune stale/conflicting rules.

Learn more:

### What’s Next

- Revisit Intermediate §3.1 Net Classes & Rules, §3.2 Polygons & Keep‑Outs, §3.3 Diff Pairs (intro) for teammates stepping up.
- For hand‑off, see Beginner → Export & Order.
- After each block, codify it in KB or a Template to compound speed on future projects.


#### 📘 Docs & References

- [**Flux Reference Page**](https://docs.flux.ai/reference)
    - A fast-loading, no-fluff guide that shows you how to perform common advanced actions in Flux. If you already know how to do something in another tool, this is where you learn how to do it here.


#### Pro Design Topics

- Streamlined [Component Procurement](https://docs.flux.ai/flux/tutorials/components-procurement)
- Tips for [High Density Designs (HDI)](https://docs.flux.ai/flux/tutorials/high-density-designs--hdi-) design
- Ensuring [supply chain](https://docs.flux.ai/flux/tutorials/components-procurement)  readiness


#### 🎥 Recommended Videos

- _[Impedance Control in Flux](https://youtu.be/dUDQljNwZ_s)_
- [AI Design Reviews](https://youtu.be/hAt-jUNllAM)
- [Working with Polygons](https://youtu.be/EravpUm7hWQ)
