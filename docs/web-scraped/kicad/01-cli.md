# KiCad 9.0 Command-Line Interface (CLI) Documentation

## Overview

The KiCad CLI provides automated command-line tools for processing schematics, PCBs, symbols, and footprints. The `kicad-cli` binary has six main subcommands: `fp`, `jobset`, `pcb`, `sch`, `sym`, and `version`.

## Footprint Commands (`fp`)

### SVG Export (Footprints)

Export footprints to SVG format with layer selection and customization options.

**Key features:**

- Export individual or multiple footprints from a library
- Selective layer exporting
- DNP (Do Not Populate) footprint styling options
- Theme customization

### Footprint Upgrade

Convert legacy footprint libraries to the current KiCad format.

**Supported input formats:**

- KiCad modern and pre-5.0 libraries
- Altium, CADSTAR, EAGLE XML
- EasyEDA/JLCEDA formats
- GEDA/PCB libraries

## PCB Commands (`pcb`)

### Design Rule Checking (DRC)

Run electrical validation on board designs with configurable reporting.

**Report formats:** Plain text or JSON output with severity filtering.

### 3D Model Exports

Multiple 3D formats available: BREP, GLB, PLY, STEP, STL, XAO, and VRML.

**Common options across 3D exports:**

- Component filtering by reference designator
- Selective layer inclusion (tracks, pads, zones, copper)
- Via handling (cut or filled)
- Board origin selection (grid or drill)

### Fabrication Formats

- **Gerber files:** Generate files with one layer per output or combine multiple layers
- **Drill files:** Excellon or Gerber format with optional map generation
- **GenCAD:** Manufacturing interchange format
- **IPC-2581/ODB++:** Modern manufacturing standards

### 2D Exports

PDF, SVG, DXF with multi-page/multi-file options and comprehensive layer control.

### Position Files

Export component placement data in ASCII, CSV, or Gerber formats for assembly automation.

### Board Rendering

Generate photorealistic PNG/JPEG renderings with adjustable lighting, camera angles, and quality presets.

## Schematic Commands (`sch`)

### Electrical Rule Checking (ERC)

Validate schematic connectivity and design intent with configurable violation reporting.

### Bill of Materials (BOM)

An ordered list of fields to export with preset-based formatting and field customization.

**Filtering options:** DNP exclusion, BOM-marked items, field-based sorting.

### Netlist Export

Support for multiple standards: KiCad S-expression, XML, CADSTAR, OrCAD PCB2, SPICE, PADS, and Allegro formats.

### Document Exports

PDF, PostScript, DXF, HPGL, and SVG with per-sheet file output or consolidated formats.

### Legacy BOM Scripts

XML export for processing through custom Python/XSLT transformation scripts.

## Symbol Commands (`sym`)

### SVG Export

Individual symbol export with layer and theme options.

### Library Upgrade

Convert symbol libraries from legacy formats to current standards.

## Jobset Commands

Execute predefined manufacturing job sequences with destination-specific output control.

## General Features

**Variable Management:**

- Project variable override with `-D KEY=VALUE`
- Multiple definitions supported

**Output Control:**

- Custom output paths and filenames
- Batch processing capabilities

**Help System:**

- Built-in help accessible via `--help` or `-h` flags
- Subcommand-specific documentation

## Common Use Cases

### Automated Fabrication

```bash
kicad-cli pcb export gerbers design.kicad_pcb
```

### Design Validation

```bash
kicad-cli pcb drc design.kicad_pcb
kicad-cli sch erc schematic.kicad_sch
```

### Documentation Generation

```bash
kicad-cli sch export pdf schematic.kicad_sch
```

### Component Assembly

```bash
kicad-cli pcb export pos design.kicad_pcb
kicad-cli sch export bom schematic.kicad_sch
```
