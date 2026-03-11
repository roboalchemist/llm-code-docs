# Source: https://docs.flux.ai/tutorials/intermediate-designer.md

# Intermediate Designer


**You’re here if:**

- You’re comfortable with microcontrollers and common components
- You’ve built and maybe even manufactured a board or two
- You want to start learning better design practices

### Introduction

This guide helps experienced builders get productive in Flux Editor quickly. You’ll learn how to combine Flux with Layout Rules, Knowledge Base (KB), and core PCB features to move faster without losing control.l.

- **Outcome:** Reduce layout time by ~30–50% while maintaining quality.
- **Assumes:** You can complete the Beginner flow (placement → scoped wiring → export). If not, review Beginner first.


> Tip: If you’re coming from KiCad, skim the KiCad ↔ Flux Quick Map below to locate familiar features.


### 1. AI Workflow Basics


#### 1.1 Troubleshooting prompts

Flux can surface plans, pin maps, assumptions, and alternatives on demand.

**Prompts to know**

- Explain your plan — shows a step‑by‑step approach before edits.
- Show pin map for @U1 — returns a table of pins, names, and functions.
- List assumptions — makes reasoning explicit.
- Propose 2 alternatives — compares viable options.

**Useful starters**

- Review this design for potential issues.
- Recommend a replacement for {designator} with similar specs.

Learn more: [Getting Started with Flux](https://docs.flux.ai/tutorials/getting-started-copilot) · [Flux Use Cases: Testing & Debugging](https://docs.flux.ai/tutorials/copilot-use-cases)


#### 1.2 Scope for speed

Break complex work into focused requests; validate between steps.

- One focus per prompt: one rail, one bus, or one block.
- Plan → approve → apply: ask for a multi‑step plan, then apply in small chunks.
- Build context: tag parts (e.g., @U1) so Flux pulls correct datasheet info.
- Branch options: explore “what‑ifs” in separate threads.
- Review before apply: verify suggestions against rules and constraints.

Learn more: [AI for Hardware Design](https://www.flux.ai/p/blog/flux-copilot-under-the-hood) · [Getting Started with Flux](https://docs.flux.ai/tutorials/ai-for-hardware-design)


#### 1.3 Knowledge Base (KB)

Teach Flux your rules and preferences so good decisions persist.

- Project‑level: constraints (limits, env), calculated values (sizing), system decisions (architecture and rationale).
- User‑level: clearances, footprints, supplier/manufacturer preferences.


> Info: When conflicts occur, project‑level entries override user‑level. Disable or prune stale entries before re‑running a plan.


Learn more: [Knowledge Base](https://docs.flux.ai/reference/knowledge-base) · [How to craft knowledge base entries](https://www.flux.ai/p/blog/teach-copilot-how-you-work-with-knowledge)

### 2. EDA Capabilities Overview

The sections below summarize how common PCB tasks work in Flux, with KiCad comparisons for orientation.

{% image url="https://uploads.developerhub.io/prod/86Yw/92f8bvnhyttgsraqh5s8lufei3yu2d2g5ay3tdscvmlmhdl6kjj4zm40vbfqb22y.png" mode="responsive" height="985" width="1130" %}
{% /image %}


> Tip: If you’re coming from KiCad, check out the [KiCad to Flux Migration Guide](https://docs.flux.ai/Introduction/kicad-to-flux).



#### 2.1 Net classes & rules

What it is: Consistent widths, clearances, and via policies per signal type (power, clock, high‑speed, analog).

**How it works in Flux**

- Create selector‑based rules targeting nets by name, tag, or property (more granular than fixed classes).
- Tie rules to stackup (impedance targets) and set precedence so critical nets receive correct geometry.

**KiCad ↔ Flux**

- KiCad: Board Setup → Design Rules → Net Classes.
- Flux: Rules Browser with selector syntax ("net classes++").

Learn more: [PCB Rules Reference](https://docs.flux.ai/reference/pcb-rules) · Layout Rules Deep Dive · [High‑Speed Routing](https://docs.flux.ai/reference/impedance-control)


#### 2.2 Polygons, planes, and keep‑outs

What it is: Copper strategy for PDN, thermals, and clean routing.

**How it works in Flux**

- Ground fills default on all layers; power fills are opt‑in via Connected Layers rules.
- Toggle fill visibility to inspect. Use keep‑outs for mechanical/RF boundaries.
- Configure via stitching (density, offset). Islands are handled automatically with through‑hole vias when appropriate.

**KiCad ↔ Flux**

- KiCad: Filled Zones + stitching/island plugins.
- Flux: Copper Fills + Stitching rules; per‑layer enablement via rules.

Learn more: [Polygons Reference](https://docs.flux.ai/reference/polygons-reference) · [Copper Fills Reference](https://docs.flux.ai/reference/reference-ground-fills)


#### 2.3 Differential pairs (intro)

What it is: Paired routing with controlled spacing and length to meet high‑speed requirements.

**How it works in Flux**

- Recognized interfaces (USB, HDMI, PCIe, GbE) enable paired routing with mirrored pad entries.
- Live length and impedance awareness driven by stackup.

**KiCad ↔ Flux**

- KiCad: Route Differential Pair + Length Tuning.
- Flux: Paired routing with live targets; tune via geometry and layer strategy.

Learn more: [High‑Speed Routing](https://docs.flux.ai/tutorials/advanced-routing)


#### 2.4 Stackups & vias

What it is: Layer and via planning that sets SI/PDN behavior and cost.

**How it works in Flux**

- Start with proven 2‑/4‑/6‑layer patterns; customize via Stackup Editor.
- Via types: through, blind, buried, micro; define size groups for consistency.
- Switch layers while routing; minimize vias; mind thermal paths.

**KiCad ↔ Flux**

- KiCad: Layer Stack Manager + via settings per class.
- Flux: Stackup Editor + via groups with rule precedence.

Learn more: [Multi‑Layer PCB Design](https://docs.flux.ai/tutorials/routing-across-multiple-layers-on-a-pcb) · [Stackup Editor](https://docs.flux.ai/reference/stackup-editor) · [Vias Reference](https://docs.flux.ai/reference/vias)


#### 2.5 Libraries, footprints, and pin maps

What it is: Correct symbols/footprints and verified pin mapping to avoid downstream errors.

**How it works in Flux**

- Use Library/Marketplace parts; request pin‑map tables from Flux for @U* designators.
- Swap footprints with Inspector; verify orientation/courtyards.

**KiCad ↔ Flux**

- KiCad: Assign Footprints; library tables.
- Flux: Part Inspector + Flux pin‑map tables.

Learn more: [Creating a Part From Scratch](https://docs.flux.ai/tutorials/tutorial-creating-a-part-from-scratch#creating-parts) · [Parts & Sublayouts](https://docs.flux.ai/tutorials/tutorial-parts-and-sublayouts) · [Importing KiCad Libraries](https://docs.flux.ai/tutorials/tutorial-import-part)

### 3. Quality, Procurement, and Reuse


#### 3.1 Design reviews

- AI Design Review checks decoupling, pull‑ups/downs, enables/resets, and strays; context actions assist fixes.
- DRC runs in parallel; add recurring checks to KB for team consistency.

**KiCad ↔ Flux**

- KiCad: Inspect → DRC.
- Flux: DRC plus AI reviews; captured as reusable knowledge.

Learn more: [AI Design Reviews](https://docs.flux.ai/reference/design-rule-check--drc-)


#### 3.2 BOM management

- Live pricing and availability across distributors.
- Set manufacturing quantity for volume pricing.
- Track lifecycle/obsolescence; alerts for price/lead‑time changes.
- Maintain alternates; consolidate to reduce complexity.

**KiCad ↔ Flux**

- KiCad: BOM scripts/tools; external pricing add‑ons.
- Flux: Built‑in sourcing/lifecycle + alternates and alerts.

Learn more: [Components & Procurement](https://docs.flux.ai/tutorials/start-to-finish-tutorial---schematics#component-selection-guidelines) · Pricing & Availability Reference


#### 3.3 Templates and patterns

- Convert validated blocks to reusable components; parametrize via properties.
- Maintain personal/org template libraries; version, document, and share.

**KiCad ↔ Flux**

- KiCad: New Project from Template; project copy.
- Flux: Templates + Convert to Component + community projects.

Learn more: Reusing Community Projects · Convert to Component · Parts & Sublayouts

### What’s Next

- Hitting fundamentals? See Beginner §3–5 (placement, scoped wiring, export).
- Pushing high‑speed or complex constraints? See Advanced §2–4 (diff pairs, impedance, PDN, parity).
- After each win, capture it in KB or a Template to compound speed on future projects.


#### 📘 Tutorials

- [Designing a Power Regulator in Flux](https://docs.flux.ai/flux/tutorials/power-regulator-example-project)
    - A step up from the basics, this tutorial walks you through designing a real, useful power system, with a focus on layout and signal integrity.


#### Next Level Concepts

- Working with [modules](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts)  to keep your design clean and reusable.
- [Customizing Flux](https://docs.flux.ai/flux/tutorials/adapt-copilot-to-your-goals) to automate repetitive tasks.
- Introduction to [High-speed routing](https://docs.flux.ai/flux/tutorials/advanced-routing).
- Designing [multi-layer PCBs](https://docs.flux.ai/flux/tutorials/routing-across-multiple-layers-on-a-pcb).


#### 🎥 Recommended Videos

- _[PCB Design, Start to Finish](https://www.youtube.com/watch?v=Nz-XvvlozK4&amp;list=PLHdtNLTgt1Ud)_
- [Full Project - Arduino Mega](https://www.youtube.com/watch?v=zflsd-k0SQA&amp;list=PLHdtNLTgt1UcT4vniv8lnTMAjUtNSe0er)
- [Understanding Design Rules](https://www.youtube.com/watch?v=nahBWKQCpcU&amp;list=PLHdtNLTgt1UcaBSvAkHEVVLYtzqTKnUWw)
