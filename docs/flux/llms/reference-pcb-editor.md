# Source: https://docs.flux.ai/reference/reference-pcb-editor.md

# The Flux PCB Editor


## What is the PCB Editor?

The PCB editor is where you transform your schematic designs into physical circuit board layouts. It's seamlessly synchronized with the Schematic editor and simulator, allowing you to see changes in real-time across all aspects of your design.

The PCB editor is where the schematics come to life. We designed a completely integrated, web-based PCB editor that automatically synchronizes with the Schematic editor and simulator.

![**Left Side - Chat Menu:** interact with Flux AI Agent. **Right Side -** **Object tree:** lists every object in the PCB canvas. **Rules:** layout rules that apply to objects matching the selector

**- Layout rules:** layout rules that apply to the selected object only.](https://uploads.developerhub.io/prod/86Yw/how3cygd32jnw3d78nrg5aos8cx548c54c0cx6fqtrbwgbuteplfaizxyxtdgwr2.png)


## Key Components of the PCB Editor

### Flux Menu

The PCB editor integrates with Flux to provide AI-assisted design capabilities. While Flux currently has limited understanding of PCB layout (it primarily works with schematics), you can still get help with:

- Understanding layout rules
- Troubleshooting design rule violations
- Learning PCB design best practices

ℹ️ **Flux Tip:** Struggling with routing your PCB? Ask Flux for help by opening the Flux Chat tab and typing "Can you help me route these components for better signal integrity?" Flux can assist with routing suggestions even though it can't position components yet.

### The Object Tree

The [Object Tree](https://docs.flux.ai/flux/reference/reference-object-tree-pcb) contains a structured map of all the elements present in the PCB editor, from parts to nets to traces. This hierarchical view helps you navigate and manage complex designs efficiently.

### Inspector

The Layout Inspector panel on the right side shows contextual information about the selected object. When nothing is selected, the inspector shows document-level information like the description, layout rules, and other properties. When a part is selected, it shows contextual information about it.

The Layout Inspector includes several important sections:

- [Properties](https://docs.flux.ai/flux/reference/reference-inspector-properties): Carry additional part metadata like Manufacturer part number, value, etc.
- [Pricing and Availability](https://docs.flux.ai/flux/reference/reference-inspector-pricing-and-availability): Flux automatically searches for pricing and availability in parts with an MPN.
- [Layout Rules](https://docs.flux.ai/flux/reference/pcb-rules): Contains [Object-Specific PCB Rules](https://docs.flux.ai/flux/reference/object-specific-pcb-rules). If you're not sure what the difference is between selector-based and object-specific layout rules, please refer to this [guide](https://docs.flux.ai/flux/reference/pcb-rules).
- [Assets](https://docs.flux.ai/flux/reference/reference-inspector-assets): Leverage existing files (STEP, SVG, etc.) to use as footprints, pad, silk, or board shapes inside Flux designs.
