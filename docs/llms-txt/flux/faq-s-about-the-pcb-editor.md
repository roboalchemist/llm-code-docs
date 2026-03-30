# Source: https://docs.flux.ai/faq/faq-s-about-the-pcb-editor.md

# PCB Editor FAQs

### How can I import a PCB Layout?

Flux doesn't currently support importing PCB layouts or gerber files.

### How do I export the gerber files for a project?

Open the Flux menu in the top-left corner of the screen. From there, choose the "Export" option and select "Manufacturing Files" to export an archive containing Gerber files.

### Can I export a 3D model of my board?

To export a 3D model of your board, click the Flux menu and choose the "Export" option, and under that "3D Model". The "STEP" file option will output a precise 3D model of just your bare board. The "STL" file option will output a mesh of your assembled board, including all components that have valid 3D models.

### How do I start the PCB layout after completing the schematic?

Click the **PCB** tab. Your schematic components become footprints on the board. Define the board outline and arrange components based on the ratsnest. For more information checkout this [Getting started tutorial](https://docs.flux.ai/Introduction/getting-started-in-flux--pcb-layout-and-routing)

### How do I rotate or flip components?

- **Rotate**: Use the ] or [ keys or the context menu.
- **Flip**: Press F while a component is selected.

### How do I delete a component, wire, or trace?

- Select the object and press Del.
- Right-click and choose Delete.
- Use  Ctrl + Z to undo changes.

### How do I use the grid snapping feature?

Flux does not use a grid system for alignment instead Flux offers a variety of tools to make sure components are perfectly and easily aligned, these include;

- Snapping
- Alignment guides
- “Space Evenly” and “Align” tools

More details in the [Layout Rules – Grid Spacing guide](https://docs.flux.ai/reference/layout-rules-types).

### How do I add via stitching to a copper pour?

Define a **Fill Stitching Density** rule for the net (usually ground). Flux will automatically generate a grid of stitching vias.

### How do I run a design rule check (DRC) and fix errors?

Flux continuously performs real-time DRCs. Errors appear in the **Inspector** panel. Adjust placements, clearances, or rules to resolve issues.

### How do I toggle (enable/disable) airwires?

Open the PCB editor and locate the "Layer" menu in the bottom left side. Inside the "Layer" menu you will find a "Metadata" option. Use the "Airwire" icon to enable/disable airwires.

### Can I do rigid-flex PCBs in Flux?

Rigid-flex PCBs are not currently supported in Flux.

## Export & Manufacturing

### How do I export my PCB design as Gerber files?

- Open the **Export Menu** from the Flux logo or project dashboard.
- Choose **Export** and select **Gerber** as the output format.

Get more details about [exporting and manufacturing](https://docs.flux.ai/Introduction/getting-started-in-flux--export-and-manufacturing) files here

### Can I order a fabricated PCB or assembly directly through Flux?

No, Flux does not offer in-app ordering. After exporting your files, you must use an external manufacturer.

### What formats can Flux export?

PDF export is not supported right now. Flux currently only supports the following formats:

#### Manufacturing Files:

- Gerber RS-274X
- Bill of Materials (CSV)
- Pick and Place (CSV)

Part Exports:

- JEP30 PartModel (XML)

#### Netlist Files:

- IPC-D-356

#### 3D Files:

- Collada
- STL
- STEP