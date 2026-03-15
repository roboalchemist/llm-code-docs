# KiCad 9.0 Schematic Editor (eeschema) Documentation

## Introduction to the KiCad Schematic Editor

The KiCad Schematic Editor represents a comprehensive schematic capture application, distributed across Linux, Apple macOS, and Windows platforms. All KiCad files maintain 100% compatibility across these operating systems.

### Core Capabilities

The editor integrates schematic drawing, PCB footprint selection, library management, and data transfer functionalities. It communicates directly with the KiCad PCB Editor for printed circuit board design while supporting netlist export for third-party packages.

#### Essential Integrated Functions

- **Electrical Rules Check (ERC)**: Automatic detection of incorrect and missing connections
- **Circuit Simulation**: ngspice-based simulation capabilities
- **Plot Export**: Multiple formats including Postscript, PDF, HPGL, and SVG
- **Bill of Materials Generation**: Python or XSLT script-based flexible formatting

### Hierarchical Schematic Support

The editor accommodates three organizational approaches:
1. Flat hierarchies (unconnected schematic sheets)
2. Simple hierarchies (single-use sheets)
3. Complex hierarchies (multi-use sheets)

## Initial Configuration

First-time execution prompts users to establish the global symbol library table (`sym-lib-table`). Three configuration options are available:

1. **Recommended**: Copy default global symbol library table
2. Custom path selection for existing tables
3. Construction from scratch

On systems where standard KiCad symbol libraries are separately packaged, users can navigate to the library installation directory.

## User Interface Overview

### Main Canvas and Surrounding Elements

The central editing canvas displays the active schematic, surrounded by:

- **Top Toolbars**: File management, zoom controls, editing tools
- **Left Toolbar**: Display options, Hierarchy Navigator, Properties Manager, selection filters
- **Message Panel & Status Bar**: Bottom-positioned feedback display
- **Right Toolbar**: Drawing and design tools, Design Block panel

### Cursor Position Information

The status bar continuously displays:
- Current X and Y coordinates
- Zoom factor (Z)
- Relative cursor position (dx, dy, distance)
- Current grid settings
- Display units

Pressing Space resets relative coordinates to zero, useful for measuring distances or aligning objects.

## Navigation and Zoom Controls

### Available Zoom Tools

| Tool | Function |
|------|----------|
| Zoom In | Centers viewport zoom increase |
| Zoom Out | Centers viewport zoom decrease |
| Zoom to Page | Fits frame around drawing sheet |
| Zoom to Objects | Fits all schematic items (including off-sheet elements) |
| Zoom to Selection | User-defined rectangular zoom area |

### Canvas Panning

By default, middle or right mouse button dragging pans the view, while mouse wheel scrolling adjusts zoom. These behaviors are configurable in Preferences under Mouse and Touchpad settings.

## Hotkeys and Keyboard Shortcuts

Hotkeys are displayed via Ctrl+F1. The documentation's Actions Reference section includes the default hotkey list.

### Platform-Specific Modifiers

On Apple keyboards:
- Replace Ctrl with Cmd
- Replace Alt with Option

### Hotkey Management

Hotkeys are stored in `user.hotkeys` files located at platform-specific paths:
- **Windows**: `%APPDATA%\kicad\9.0\user.hotkeys`
- **Linux**: `~/.config/kicad/9.0/user.hotkeys`
- **macOS**: `~/Library/Preferences/kicad/9.0/user.hotkeys`

The hotkey editor supports importing settings via the **Import Hotkeys** button.

## Selection Mechanisms

### Single-Item Selection

Left-clicking selects objects. Box selection works through:
- **Left-to-right**: Exclusive selection (yellow box, items fully inside only)
- **Right-to-left**: Inclusive selection (blue box, items touching the box)

### Selection Modifier Keys

#### Windows/Linux Modifiers

| Modifier | Effect |
|----------|--------|
| Ctrl | Toggle selection |
| Shift | Add to existing selection |
| Ctrl+Shift | Remove from existing selection |
| Long click or Alt | Clarify selection via pop-up menu |

#### macOS Modifiers

| Modifier | Effect |
|----------|--------|
| Cmd | Toggle selection |
| Shift | Add to existing selection |
| Cmd+Shift | Remove from existing selection |
| Long click or Option | Clarify selection via pop-up menu |

### Selection Filter Panel

The lower-left corner panel controls which object types are selectable. The "All items" checkbox toggles all types simultaneously. Right-clicking any object type restricts selection to that type only.

## Schematic Creation and Editing

### Schematic Composition

A schematic consists primarily of:
- Symbols (from libraries)
- Wires and buses
- Labels and junctions
- Power symbols
- Graphical elements (comments, polylines)

These components enable validation through ERC, bill of materials generation, netlist creation, and PCB design transfer.

### Multi-Sheet Organization

Schematics can span multiple sheets, organized hierarchically with a root sheet and sub-sheets. Each sheet is an independent `.kicad_sch` file functioning as a complete schematic.

## Schematic Editing Tools

The right toolbar houses editing tools, which remain active until cancelled (Esc key) or replaced by another tool selection.

### Core Tool Set

| Tool | Function |
|------|----------|
| Selection Tool | Default interaction mode |
| Highlight Net | Mark net wires and labels with contrasting color |
| New Symbol | Open symbol selector for placement |
| Add Power | Place power/ground symbols |
| Draw Wire | Create electrical connections |
| Draw Bus | Create grouped signal bundles |
| Wire-to-Bus Entry | Create graphical entry points |
| No-Connection Flag | Mark intentionally unconnected pins |
| Junction | Connect crossing wires or wire-to-pin |

### Labeling and Connectivity

| Tool | Function |
|------|----------|
| Local Label | Sheet-specific signal naming |
| Net Class Directive | Assign net classes via labels |
| Directive Rule Area | Define rule-based areas |
| Global Label | Cross-sheet signal connection |
| Hierarchical Label | Parent-child sheet connection |
| Hierarchical Subsheet | Create nested sheet structure |
| Hierarchical Sheet Pin | Sync sheet pins with hierarchical labels |

### Text and Graphics

| Tool | Function |
|------|----------|
| Place Text | Add text annotations |
| Place Text Box | Create bordered text regions |
| Place Table | Insert structured data tables |
| Draw Rectangle | Create rectangular shapes |
| Draw Circle | Create circular shapes |
| Draw Arc | Create arc segments |
| Draw Bezier Curve | Create curved paths |
| Draw Graphic Lines | Create non-connecting lines |
| Place Bitmap | Insert image files |

### Utilities

| Tool | Function |
|------|----------|
| Interactive Delete | Remove clicked items |

## Grids and Snapping

### Snapping Behavior

Schematic elements snap to grid during movement, dragging, and drawing. Wire and label tools additionally snap to connected items (pins, wires, labels) regardless of grid snapping status.

### Grid Snapping Modifiers

| Modifier | Effect |
|----------|--------|
| Ctrl | Disable grid snapping |
| Shift | Disable connected object snapping |

### Recommended Grid Settings

The default 50 mil (0.050") or 1.27mm grid represents the KiCad standard for symbol placement and wire routing. The standard symbol library adheres to this grid; using alternative grid sizes results in connectivity failures.

## Object Properties Editing

### Properties Dialog Access

Press E or select **Properties** from the right-click context menu to access object properties. Note: You can only open the properties dialog if all the items you have selected are of the same type. Multiple single-type item editing requires the Properties Manager.

### Properties Manager

The docked Properties Manager panel displays selected item properties for editing. When multiple items of differing types are selected, only shared properties are displayed.

**Access**: **View** → **Panels** → **Properties** or the Properties Manager button on the left toolbar.

Properties Manager modifications apply immediately. When multiple items are selected, changes apply to each item individually (not as a group).

## Working with Symbols

### Symbol Placement

Use the New Symbol button or press A to open the Choose Symbols dialog.

#### Symbol Chooser Features

The dialog displays symbols grouped by library, with name, library, and description columns shown by default. Additional columns are accessible via right-click header menu.

**Search Filtering**: Symbols filter by name, keywords, description, and additional symbol fields based on search input.

**Advanced Filter Options**

- **Wildcards**: `*` matches any number of characters (including none); `?` matches single characters
- **Key-value Pairs**: Match tags like "Key:123" using comparison operators (e.g., "Key>123", "Key<123")
- **Regular Expressions**: wxWidgets Advanced Regular Expression style (Perl-like)

### Symbol Movement

**Move Tool (M)**: Relocates symbols without maintaining wire connections to pins.

**Drag Tool (G)**: Moves symbols while preserving wire connections, adjusting connected wires as needed.

**Rotation and Mirroring**: Use R, X, or Y hotkeys respectively.

### Symbol Properties Editing

Double-click symbols or press E to open the Properties dialog, which displays all symbol fields in a table format.

#### Field Management

Fields can be added, deleted, edited, reordered, moved, or resized. Field names beginning with `ki_` (e.g., `ki_description`) are reserved by KiCad and should not be used for custom fields.

#### Special Field Behaviors

**Footprint Field**:
- Defines the corresponding PCB footprint
- Button opens footprint chooser

**Datasheet Field**:
- Contains manufacturer datasheet references
- Local file or remote URL support
- Right-click symbol to **Show Datasheet** (D hotkey)
- **Embed File** checkbox embeds datasheets in schematic

#### Symbol Attributes

**Exclude from Simulation**: Prevents SPICE inclusion

**Exclude from Bill of Materials**: Prevents component inclusion in BOM exports

**Exclude from Board**: Marks symbols as schematic-only without corresponding PCB footprints

**Do Not Populate (DNP)**: Indicates components that should not be attached to PCBs despite having PCB footprints

## Reference Designators and Symbol Annotation

### Reference Designator Concepts

Reference designators provide unique component identifiers consisting of:
- Letter(s) indicating component type (R for resistor, C for capacitor, U for IC)
- Sequential number
- Trailing letter for multi-unit symbols indicating the unit
- Question mark (?) for unannotated symbols

Reference designators must be globally unique within a design.

### Auto-Annotation

When enabled, symbols receive automatic reference designators upon addition to the schematic.

**Enable Auto-Annotation**:
- Check **Automatically annotate symbols** in **Schematic Editor** → **Annotation Options** preferences
- Toggle the auto-annotate button on the left toolbar

### Annotation Tool

Launch via the Annotate button in the top toolbar.

**Scope Options**:
- Entire schematic
- Current sheet only
- Selected symbols only
- **Recurse into subsheets**: Include subsheet symbols in scope

## Electrical Connections

Connections are established via wires (direct) or labels (implicit via matching names). Both appear in schematic diagrams alongside buses and hidden power pin connections.

### Wires

Wires establish direct electrical connections between points. Connections occur only at wire ends; crossing wires do not connect without explicit junctions.

#### Connection Indicators

- **Unconnected wire ends**: Small squares indicate connection points; disappear when connected
- **Unconnected pins**: Circles indicate connection points; disappear when connected

#### Grid Alignment Requirements

Wires connect with other wires or pins only if their ends coincide exactly. Grid alignment is critical; 50 mil grid is recommended for standard library compatibility.

### Wire Drawing and Editing

**Wire Tool**: Use the wire button in right toolbar (w hotkey).

**Automatic Initiation**: Left-clicking unconnected pins or wire ends automatically starts wire placement.

#### Wire Angle Modes

- 90-degree angle restriction
- 45-degree angle restriction
- Free angle (unrestricted)

**Mode Selection**: Cycle via Shift+Space or set in **Preferences** → **Schematic Editor** → **Editing Options**.

### Labels

Labels assign net names to wires and pins. Same-name labels create connections without direct wiring, enabling simplified schematics for complex designs.

#### Label Types

**Local Labels**: Sheet-specific connections

**Global Labels**: Cross-sheet connections

**Hierarchical Labels**: Parent-child sheet connections

All label types connect when names match within the same sheet.

### Buses

Buses group related signals to simplify complex designs. Buses are drawn like wires and named using labels.

#### Bus Member Types

**Vector Buses**: Collections of signals with common prefix and numeric suffix. Format: `<PREFIX>[M..N]` where M and N are non-negative numbers. Example: `DATA[0..7]` contains signals `DATA0` through `DATA7`.

**Group Buses**: Collections of signals and/or vector buses with different names. Syntax: `<OPTIONAL_NAME>{SIGNAL1 SIGNAL2 SIGNAL3}`.

### No-Connection Symbols

The "no-connection" flag marks intentionally unconnected pins. These flags indicate to ERC that unconnected pins are intentional (not errors).

## Hierarchical Schematics

Hierarchical organization enables management of complex multi-sheet designs with three supported structures:

1. **Flat hierarchies**: Independent sheets without explicit connections
2. **Simple hierarchies**: Single-use sheets
3. **Complex hierarchies**: Multi-use sheets

Each sheet is a separate `.kicad_sch` file functioning as a complete schematic.

### Drawing Hierarchical Sheets

Use the Hierarchical subsheet button to place subsheets. A file name dialog appears; specify the subsheet file name.

### Navigating Between Sheets

The Hierarchy Navigator panel displays the sheet structure. Click sheet entries to navigate between sheets.

### Hierarchical Labels and Sheet Pins

**Hierarchical Labels**: Added in subsheets. These create connection points with parent sheets.

**Hierarchical Sheet Pins**: Added to sheet symbols in parent sheets. These correspond to hierarchical labels in the subsheet.

## Inspecting a Schematic

### Find Tool

Located in the **Inspect** menu or accessible via Ctrl+F. Searches for symbols, nets, labels, and other objects by name or value.

### Net Highlighting

Use the Highlight net tool to mark a net's wires and labels with contrasting color. If PCB Editor is open, corresponding copper highlights as well.

### Electrical Rules Checking (ERC)

ERC automatically detects incorrect and missing connections. Launch via **Inspect** → **Electrical Rules Check** or Ctrl+Shift+V.

The ERC dialog displays detected violations, warnings, and informational messages. Double-clicking messages navigates to affected elements in the schematic.

## Assigning Footprints

Three methods assign footprints to symbols:

### Method 1: Symbol Properties Dialog

Open symbol properties (E hotkey or double-click). The **Footprint** field displays the assigned footprint. Click the library button to open the footprint chooser.

### Method 2: While Placing Symbols

During symbol placement, the footprint chooser is accessible before placing the symbol in the schematic.

### Method 3: Footprint Assignment Tool

Provides dedicated interface for bulk footprint assignment. Access via the right-click context menu or dedicated toolbar button.

## Generating Outputs

### Printing

**File** → **Print** (Ctrl+P) opens the print dialog. Configure printer settings, layout, and scaling.

### Plotting

**File** → **Plot** exports schematics to multiple formats:
- Postscript
- PDF
- HPGL
- SVG

Configure output format, scaling, and page settings in the plot dialog.

### Bill of Materials (BOM) Generation

Access the BOM tool via **Tools** → **Generate Bill of Materials** or use the Symbol Fields Table export function.

The tool supports custom formatting via Python or XSLT scripts, enabling flexible BOM creation matching design requirements.

### Netlist Generation

**Tools** → **Generate Netlist** creates netlist files for simulation and PCB layout. Multiple formats are supported for compatibility with third-party tools.

## Simulator

KiCad integrates ngspice for circuit simulation. Key features include:

### Simulation Model Assignment

The Simulation Model Editor (accessed via **Simulation Model…** button in Symbol Properties) specifies how symbols behave in simulations.

### Value Notation

Numeric values support metric prefixes and expressions (e.g., `10k`, `2.2u`, `1m`).

### Running Simulations

**Simulation** → **Run Simulation** (Ctrl+Shift+S) executes the simulation. The simulation window displays results and enables interactive probing.

### Viewing Results

Simulation results display as waveform plots with interactive cursors and measurements. Multiple nets can be displayed simultaneously.

## Advanced Topics

### Configuration and Customization

Preferences dialog (**Preferences** → **Preferences…**) controls display options, colors, fonts, hotkeys, and mouse behavior.

### Text Variables

Text variables enable dynamic text substitution. Variables are specified using `${VARIABLE_NAME}` syntax and expand to corresponding values at display or export time.

**Common Variables**:
- `${SYMBOL_NAME}`: Symbol name in library
- `${SYMBOL_LIBRARY}`: Library containing symbol
- `${INTERSHEET_REFS}`: Inter-sheet reference list for global labels
- Sheet and project variables

### Database Libraries

Database libraries link symbol libraries to external databases, enabling intelligent component selection and property management.

### HTTP Libraries

Remote symbol libraries accessed via HTTP connections. Supports library versioning and centralized management.

---

**Documentation Version**: Based on KiCad 9.0.8
**License**: GNU General Public License v3+ or Creative Commons Attribution License 3.0+
