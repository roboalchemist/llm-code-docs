# Source: https://docs.flux.ai/reference/data-portability.md

# Data Portability - Export Formats & Capabilities

Flux provides comprehensive data portability features, allowing you to export your designs in industry-standard formats for manufacturing, collaboration, and integration with other tools.

## Overview

Data portability ensures that your PCB designs created in Flux can be exported and used across different tools and manufacturing processes. Whether you're sending files to a PCB manufacturer, integrating with external CAD tools, or creating visualizations of your board, Flux supports all the essential export formats you need.

> Flux features world-class real-time collaboration capabilities. When working with other Flux users, you can simply share your project within Flux—there's typically no need to export files for collaboration purposes.

All export options are accessible through the Flux menu in the top-left corner of your workspace under the **Export** submenu.

## Manufacturing File Exports

These files are essential for PCB fabrication and assembly. Manufacturers use these formats to program their equipment and verify your design specifications.

### Gerber RS-274X Files

Gerber files are the industry-standard format for PCB manufacturing. Flux exports a complete set of Gerber files packaged in a ZIP archive.

**File Format:** `.zip`

**What's Included:**

- Top and bottom copper layers
- Soldermask layers (top and bottom)
- Silkscreen layers (top and bottom)
- Solderpaste layers (top and bottom)
- Inner copper layers (for multi-layer boards)
- NC drill files for holes and vias

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **Manufacturing Files (Gerbers, etc)**
3. The ZIP file will be downloaded automatically

**Validation:** After exporting, it's recommended to validate your Gerber files using an online viewer like [tracespace.io](https://tracespace.io/view/) before sending to your manufacturer. Learn more in the [Manufacturing & Export Guide](https://docs.flux.ai/flux/Introduction/getting-started-in-flux--export-and-manufacturing).

> Use **Flux** to review your design before exporting. Ask questions like "Are there any design rule violations I should fix before manufacturing?" to catch issues early.

### Bill of Materials (BOM)

The Bill of Materials is a detailed list of all components needed to assemble your PCB, including quantities, part numbers, and specifications.

**File Format:** `.zip` (contains multiple CSV files)

**What's Included:**

- Component designators and values
- Manufacturer Part Numbers (MPN)
- Manufacturer names
- Package/footprint information
- Quantities required
- Multiple CSV formats for different manufacturers

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **Bill of Materials**
3. The ZIP archive with multiple CSV formats will be downloaded

**Requirements:** All components must have valid Manufacturer Part Numbers (MPNs) for the BOM to be useful for assembly.

> Ensure all components in your design have MPNs assigned. Missing MPNs can cause issues during the assembly process.

### Pick and Place Files

Pick and Place files contain the X-Y coordinates and rotation information for each component, essential for automated PCB assembly machines.

**File Format:** `.zip` (contains CSV files)

**What's Included:**

- Component designators
- X and Y coordinates for each component
- Rotation angles
- Layer information (top or bottom)
- Component reference information

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **Pick & Place**
3. The ZIP file will be downloaded automatically

**Use Case:** Required when ordering assembled PCBs from manufacturers who use automated pick-and-place machines.

### IPC-2581C Format

IPC-2581C is a modern, comprehensive format that encapsulates all PCB manufacturing data in a single file, including design intent, stackup, and manufacturing requirements.

**File Format:** `.ipc2581c`

**Advantages:**

- Single file contains all manufacturing data
- Includes intelligent design information
- Reduces errors from multiple file formats
- Growing industry adoption

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **IPC-2581C**
3. The .ipc2581c file will be downloaded

**Availability:** This format is available on select plans. Check with your manufacturer to confirm they support IPC-2581C before using this format.

## Netlist Exports

Netlist files describe the electrical connectivity of your design and are used for verification, testing, and integration with other tools.

### EDIF Schematic Netlist

Electronic Design Interchange Format (EDIF) is a standard format for representing electronic schematics and netlists.

**File Format:** `.edif`

**What's Included:**

- Component list from your schematic
- Net connections between components
- Component properties and attributes
- Hierarchical design structure

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **Schematic Netlist (.edif)**
3. The .edif file will be downloaded

**Use Case:** Useful for design verification, simulation, or importing connectivity information into other EDA tools.

### IPC-D-356 Layout Netlist

IPC-D-356 is a standard netlist format that describes the electrical connectivity from the PCB layout perspective, including exact pad locations.

**File Format:** `.d356`

**What's Included:**

- Net connectivity from PCB layout
- Pad coordinates and layer information
- Component placement data
- Test point information

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **Layout Netlist (.d356)**
3. The .d356 file will be downloaded

**Use Case:** Commonly used for electrical testing (flying probe or bed-of-nails testers) and design verification against the schematic.

## 3D Model Exports

Export 3D representations of your PCB for visualization, mechanical integration, and documentation purposes.

### STL Format

STL (Standard Tessellation Language) exports a mesh representation of your assembled board with all components that have 3D models.

**File Format:** `.stl`

**What's Included:**

- 3D mesh of the PCB
- Component 3D models (where available)
- Assembled board visualization

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **3D Model** &gt; **STL (.stl)**
3. The .stl file will be downloaded

**Use Case:** Ideal for 3D printing enclosures, mechanical fit verification, and creating realistic renders. Compatible with most 3D modeling and CAD software.

**Requirements:** Components must have valid 3D models for accurate representation. The board must be in 3D visualization mode.

### STEP Format

STEP (Standard for the Exchange of Product Data) is a precise 3D CAD format that exports just the bare PCB board outline and shape.

**File Format:** `.step`

**What's Included:**

- Precise 3D representation of bare PCB board
- Board outline and shape
- Accurate dimensional data for mechanical CAD integration

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **3D Model** &gt; **STEP (.step)**
3. The .step file will be downloaded

**Use Case:** Best for mechanical CAD integration, enclosure design, and precise dimensional verification. STEP files can be imported into most mechanical CAD tools like SolidWorks, Fusion 360, or FreeCAD.

> STEP format is the preferred choice when integrating your PCB design with mechanical CAD systems for enclosure design and fit verification.

### COLLADA Format

COLLADA (COLLAborative Design Activity) is a 3D format designed for interchange between different 3D applications.

**File Format:** `.dae`

**What's Included:**

- 3D model of assembled board
- Component 3D representations
- Visual materials and colors

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **3D Model** &gt; **COLLADA (.dae)**
3. The .dae file will be downloaded

**Use Case:** Useful for importing into 3D visualization and rendering software, game engines, or web-based 3D viewers.

**Requirements:** The board must be in 3D visualization mode for COLLADA export.

## Project File Exports

### Flux Project Format

Export your complete Flux project in the native .flx format for backup purposes or for use in external applications.

**File Format:** `.flx`

**What's Included:**

- Complete schematic design
- PCB layout with all layers
- Component library references
- Design rules and constraints
- All project settings and configurations

**How to Export:**

1. Click the Flux logo in the top-left corner
2. Navigate to **Export** &gt; **Flux project (.flx)**
3. The .flx file will be downloaded

**Use Case:** Perfect for:

- Creating backups of your projects
- Importing into other EDA tools or applications
- Version control and archiving
- Long-term project preservation

> For collaboration with other Flux users, use Flux's built-in real-time collaboration features instead of exchanging .flx files. Simply share your project within Flux to work together seamlessly.

## Export Best Practices

### Before Exporting

1. **Run Design Rule Checks (DRC):** Ensure your design passes all DRC checks before exporting for manufacturing. Address any violations in the Inspector panel.
2. **Verify Component Data:** Check that all components have proper MPNs, values, and footprints assigned.
3. **Review 3D Visualization:** If exporting 3D models, review your board in 3D mode to ensure everything looks correct.
4. **Check Board Outline:** Verify your board outline is a closed shape with no gaps.

### After Exporting

1. **Validate Gerber Files:** Use an online Gerber viewer like [tracespace.io](https://tracespace.io/view/) to verify all layers exported correctly.
2. **Review BOM Data:** Open the exported BOM CSV files to confirm all component information is accurate.
3. **Check with Manufacturer:** Confirm your manufacturer supports the file formats you're providing before ordering.

> Before exporting for manufacturing, ask **Flux** to review your design. Try prompts like:> > - "Check my design for common manufacturing issues"> - "Are all my components properly specified for manufacturing?"> - "Review my board stackup for potential problems"

## Troubleshooting

### Export Not Available

**Issue:** An export option is grayed out or disabled.

**Solutions:**

- **Manufacturing/Gerber exports:** Ensure you have an active PCB layout
- **Pick & Place:** Verify components are placed on the PCB
- **BOM:** Check that components have valid data assigned
- **3D Models (STL/COLLADA):** Switch to 3D visualization mode first

### Missing Component Data in BOM

**Issue:** BOM export is missing component information.

**Solutions:**

- Verify all components have Manufacturer Part Numbers (MPNs) assigned
- Check component properties in the Inspector panel
- Ensure components are properly linked to library parts

### Gerber Validation Errors

**Issue:** Gerber viewer shows errors or unexpected results.

**Solutions:**

- Verify board outline is a closed shape
- Check that all layers are properly configured in stackup
- Review DRC violations and resolve before re-exporting
- Ensure traces and pads meet minimum feature sizes

### 3D Export Issues

**Issue:** 3D models look incorrect or incomplete.

**Solutions:**

- Verify components have 3D models assigned
- Check that board is in 3D visualization mode (for STL/COLLADA)
- Review component placement and orientation
- For STEP exports, verify board outline is correct

## What's Next

Now that you understand Flux's data portability features, explore these related topics:

- [Manufacturing & Export Guide](https://docs.flux.ai/flux/Introduction/getting-started-in-flux--export-and-manufacturing) - Detailed walkthrough of exporting for manufacturing
- [Design Rule Check (DRC)](https://docs.flux.ai/flux/reference/design-rule-check--drc-) - Ensure your design meets manufacturing requirements
- [Component Procurement](https://docs.flux.ai/flux/tutorials/components-procurement) - Learn how to source components for your design
- [JEP30 PartModel Import/Export](https://docs.flux.ai/flux/reference/jep30-partmodel-reference) - Exchange component data in JEP30 format (Enterprise feature)
- [Importing Schematics](https://docs.flux.ai/flux/reference/reference-import-designs) - Import designs from Cadence and Altium

> Once you've exported and validated your files, you're ready to send them to your PCB manufacturer. Check out our [Manufacturing Guide](https://docs.flux.ai/flux/Introduction/getting-started-in-flux--export-and-manufacturing) for tips on choosing a manufacturer and placing your order.