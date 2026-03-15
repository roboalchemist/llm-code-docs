# KiCad 9.0 Getting Started Documentation

## Overview

KiCad is a free, open-source software suite for creating electronic schematics, printed circuit boards (PCBs), and component descriptions. It supports integrated design workflows where schematics and PCBs are designed together, plus specialized standalone workflows.

**Key capabilities:**
- Supports PCBs with up to 32 copper layers
- Suitable for designs of all complexity levels
- Cross-platform (Windows, macOS, Linux)
- Includes integrated SPICE simulator, PCB calculator, Gerber viewer, and 3D visualization

## Installation & Support

### Getting Started
Download and install from https://www.kicad.org/download/. If you encounter system-specific issues, check the [known issues page](https://www.kicad.org/help/known-system-related-issues/).

### Support Resources
- Official user forum: [forum.kicad.info](https://forum.kicad.info/)
- Real-time chat: Discord or IRC communities
- Learning resources available at [kicad.org/help/learning-resources/](https://www.kicad.org/help/learning-resources/)

## Fundamental Concepts

### Schematic Design
The schematic is a symbolic representation showing components and their connections. Schematic symbols are pictorial representations—zigzags for resistors, triangles for op-amps, etc.

### PCB Layout
The board is the physical realization of the schematic, with component footprints (copper pads matching component pins) positioned on the board and copper tracks making the connections.

### Project-Based Workflow
A KiCad project is a folder containing:
- Project file (`.kicad_pro`)
- Schematic file (`.kicad_sch`)
- Board file (`.kicad_pcb`)
- Optional: custom symbol/footprint libraries, simulation data, purchasing information

Keep all files together; opening designs outside their project context may result in missing information.

## PCB Design Workflow

### Standard Process
1. **Schematic entry**: Add symbols, draw connections, select footprints
2. **Design verification**: Run electrical rules check (ERC)
3. **Transfer to layout**: Import schematic data into board editor
4. **Component placement**: Position footprints carefully considering electrical and routing factors
5. **Track routing**: Draw copper connections between pads
6. **Design validation**: Run design rules check (DRC)
7. **Manufacturing outputs**: Generate Gerber files and drill specifications

### Iterative Updates
Schematics can be modified after layout begins; changes pull into the board design automatically. Board-level changes can push back to the schematic for consistency.

## Tutorial Part 1: Creating a New Project

### Project Setup
1. Launch KiCad to open the Project Manager
2. Select **File** → **New Project**
3. Browse to desired location and enter project name (e.g., "getting-started")
4. Check "Create a new folder for the project"
5. Click **Save**

This creates three files sharing your project name with extensions `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`.

### Project Features
- **Automatic backups**: KiCad creates backup copies when saving and at configurable intervals
- **Backup settings**: Manage via **Preferences** → **Preferences** → **Common** → **Project Backup**
- **Tool launchers**: Use buttons on the right side of Project Window to open Schematic Editor, PCB Editor, and other tools

## Tutorial Part 2: Schematic Design

### Library Configuration (First Launch)
When opening the schematic editor initially, you'll configure the symbol library table—the list telling KiCad which symbol libraries to use and their locations.

**Recommended setup:**
Select "Copy default global symbol library table (recommended)". If unavailable, choose "Copy custom global symbol library table" and browse to:
- **Windows**: `C:\Program Files\KiCad\9.0\share\kicad\template\`
- **Linux**: `/usr/share/kicad/template/`
- **macOS**: `/Applications/KiCad/KiCad.app/Contents/SharedSupport/template/`

Select the `sym-lib-table` file.

### Navigation Controls
- **Pan**: Middle-click + drag or right-click + drag
- **Zoom**: Mouse wheel, or press F1/F2
- **Laptop adjustments**: Customize mouse controls via **Preferences** → **Mouse and Touchpad**

### Schematic Sheet Setup
Before drawing, configure the sheet itself:
1. Click **File** → **Page Settings**
2. Add title and date
3. Adjust paper size if needed

### Adding Components

#### Opening the Symbol Chooser
- Click the **Add Symbols** button (or press **A**)
- Browse available libraries and select symbols

#### Footprint Library Setup (First Component Addition)
On first component addition, the footprint library table dialog appears. Select "Copy default global footprint library table (recommended)" or the custom option, then locate `fp-lib-table`.

#### Basic Device Placement
The `Device` library contains common components:
- **LED**: Look up by searching or browsing
- **Resistor**: Search for "R" (IEC-style rectangular) or use "R_US" for ANSI zigzag style
- **Battery**: Use "Battery_Cell" symbol

Click to place each component on the schematic.

### Selecting and Moving Objects

#### Selection Methods
- **Default tool**: Selection is active when no other tool is engaged; press **Esc** to return to selection mode
- **Shift+click**: Add objects to selection
- **Ctrl+Shift+click**: Remove from selection (macOS: Cmd+Shift+click)
- **Ctrl+click**: Toggle selection state (macOS: Cmd+click)
- **Drag selection**: Left-to-right selects fully enclosed; right-to-left selects partially enclosed

#### Manipulation
- **Move**: Press **M** on selected objects; **G** (drag) keeps attached wires, **M** leaves wires behind
- **Rotate**: Press **R** on selected objects
- **Delete**: Press **Delete** key

### Wiring Connections

#### Drawing Wires
1. Click the **Add a Wire** button (or press **W**)
2. Click and release to start
3. Click symbol pins to draw connections
4. Double-click to finish or press **Escape** to cancel

#### Alternative Method
Hover over unconnected pins—the cursor changes to indicate wire-drawing capability. Clicking automatically begins the wire.

### Power and Ground Symbols

#### Quick Addition
Click the **Add a Power Symbol** button (or press **P**) to see power and ground symbols specifically.

Add VCC and GND symbols and connect them with wires. This clarifies large schematics even if not strictly necessary for simple designs.

### Net Labeling
1. Click the **Draw Net Labels** button (or press **L**)
2. Enter label name (e.g., "led")
3. Place so the square attachment point overlaps the wire

**Important**: Labels and power symbols with identical names are automatically connected—even without visible wire connections.

### Component Annotation

Annotation assigns unique reference designators (like R1, D1) to each symbol.

**Status**: Symbols are auto-annotated by default upon addition. Manual or re-annotation uses the **Fill in schematic symbol reference designators** button in the toolbar.

### Setting Component Values

1. Select a component and right-click
2. Choose **Properties** (or press **E**)
3. Modify the **Value** field

Examples:
- LED: "red" (or manufacturer part number)
- Battery: "3V" (for a lithium coin cell)
- Resistor: "1k"

### Assigning Footprints

Many symbols have multiple possible footprints; selection ensures correct PCB attachment.

#### Using the Footprint Assignment Tool
1. Click the **icon cvpcb** button in the toolbar
2. **Left pane**: Available footprint libraries
3. **Middle pane**: Schematic symbols needing footprints
4. **Right pane**: Available footprints for the selected symbol
5. Double-click a footprint to assign it

#### Filtering Options
- **Leftmost button**: Activates symbol-defined filters (sometimes restrictive)
- **Middle button**: Filters by pin count—highly useful
- **Right button**: Filters by selected library
- **Text box**: Filters by footprint name match

#### Example Assignments
| Symbol | Footprint |
|--------|-----------|
| BT1 (Battery) | `Battery:BatteryHolder_Keystone_1058_1x2032` |
| D1 (LED) | `LED_THT:LED_D5.0mm` |
| R1 (Resistor) | `Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal` |

### Electrical Rules Check (ERC)

#### Purpose
ERC detects common connection errors:
- Unconnected pins
- Multiple power outputs shorted together
- Unpowered power inputs
- Unannotated symbols
- Mismatched net labels

#### Running ERC
1. Click the **ERC** button in the toolbar
2. Click **Run ERC**
3. Violations are listed with arrows pointing to locations
4. Select violations to highlight the corresponding error

#### Addressing Common Issues
**Power net violations** ("Input Power pin not driven by any Output Power pins"):
Power symbols require an output power pin on the same net (like from a voltage regulator). Use the special `PWR_FLAG` symbol from the `Power` library to explicitly indicate that power nets are driven (even by batteries). Add PWR_FLAG to VCC and GND nets.

### Bill of Materials (BOM)

#### Generation
1. Click **Tools** → **Generate Bill of Materials**
2. Configure metadata export in the **Edit** tab
3. Configure output format in the **Export** tab
4. Specify output file location
5. Click **Export**

The BOM spreadsheet lists all components with their values, reference designators, and quantities.

## Tutorial Part 3: Circuit Board Layout

### Opening the PCB Editor
From the Project Window, click the PCB Editor button or open the board file directly.

### Navigation
- **Pan**: Middle-click + drag or right-click + drag
- **Zoom**: Mouse wheel or F1/F2
- **Display modes**: Left toolbar offers outline/filled display toggles for tracks, vias, pads, zones

### Interface Overview
- **Left toolbar**: Display options (units, rendering modes)
- **Right toolbar**: PCB design tools
- **Right sidebar**: Appearance panel (layer visibility, colors, opacity) and selection filters
- **Active layer**: Changed by clicking layer names in the Appearance panel

### Board Setup

#### Page Configuration
1. **File** → **Page Settings**
2. Set paper size
3. Enter date, revision, and title

#### Design Configuration
1. **File** → **Board Setup**
2. **Board Stackup** → **Physical Stackup**: Define copper and dielectric layers
3. **Design Rules** → **Constraints**: Set track widths, clearances, via sizes
4. **Design Rules** → **Net Classes**: Define design rule groups for specific nets

#### Net Classes
A net class groups nets with identical design rules. The `Default` net class applies to all nets unless specifically assigned. For complex boards, create specialized classes like:
- **High Current**: Wider tracks
- **50 ohm**: Controlled-impedance specifications

### Importing Schematic Data

#### Process
1. Click **Tools** → **Update PCB from Schematic** (or press **F8**)
2. Review messages in **Changes To Be Applied** window
3. Click **Update PCB**
4. Place footprints on canvas by clicking

#### Important
Updating is manual—designers control when PCB reflects schematic changes. After each schematic edit, explicitly update the PCB.

### Drawing the Board Outline

#### Layer Selection
1. Click **Edge.Cuts** in the Layers panel (Appearance)
2. Select the rectangle tool from the right toolbar
3. Place corners to create a closed shape surrounding components

#### Grid Adjustment
For easier outline drawing, switch to a coarse grid (1mm) via the Grid dropdown above the canvas.

#### Accepted Methods
Use rectangle, line, arc, circle, polygon, or Bézier tools. Requirement: Single closed, non-self-intersecting shape.

### Component Placement

#### Considerations
- **Fixed positions**: Connectors, buttons, switches
- **Electrical placement**: Bypass caps near IC power pins; analog components away from digital noise
- **Courtyard clearance**: Component courtyards generally shouldn't overlap
- **Routing ease**: Connected components positioned to minimize track complexity

#### Practical Placement
1. **Select** component (click to select)
2. **Move** (press **M**)
3. **Flip** to opposite side (press **F**)—flipped items appear mirrored with color-coded layer
4. **Rotate** (press **R**)

#### Visual Aids
Ratsnest (thin lines between pads) shows connections; minimize tangles for simplified routing.

### Routing Tracks

#### Basic Process
1. Set active layer to **F.Cu** (front copper) via Appearance panel
2. Click **Route Tracks** (or press **X**)
3. Click starting pad; release mouse button
4. Click target pad to complete track
5. Ratsnest disappears once connection is made in copper

#### Layer Switching
Active layer automatically changes when clicking pads on different layers (e.g., back-side pads switch to **B.Cu**).

#### Through-Hole Advantages
Through-hole pads connect to multiple layers, enabling cross-layer connections without vias.

#### Via Insertion
1. While routing, press **V**
2. Click to place via at intermediate location
3. Active layer automatically switches
4. Continue routing on new layer

### Copper Zones

#### Purpose
Copper zones are large regions automatically connecting to matching nets while avoiding others. Often used for ground and power distribution.

#### Creation
1. Switch to target copper layer (**B.Cu** for bottom)
2. Click **Add a filled zone** button
3. Click corners to define zone boundary
4. In properties dialog: Select net and layer
5. Click **OK**
6. Double-click final corner to complete

#### Filling
Zones require manual filling: **Edit** → **Fill All Zones** (or press **B**).

#### Features
- **Thermal reliefs**: Thin tracks connecting pads to zone for easier soldering
- **Visibility toggle**: **Show only zone boundaries** button hides fills while retaining fill status
- **Transparency**: Adjust via Appearance panel

### Design Rule Checking (DRC)

#### Purpose
Detects layout errors:
- Schematic-layout mismatches
- Insufficient copper clearances
- Shorted regions
- Unconnected tracks

#### Running DRC
1. **Inspect** → **Design Rules Checker** (or toolbar button)
2. Click **Run DRC**
3. Errors display with arrows pointing to violations
4. Click violations to zoom and highlight

#### Configuration
**File** → **Board Setup** → **Design Rules** → **Violation Severity** allows rule customization.

#### Zone Refilling
Check **Refill all zones before performing DRC** to ensure zone fills are current. Alternatively, manually refill zones (press **B**) before running DRC.

### 3D Viewer

#### Access
**View** → **3D Viewer**

#### Navigation
- **Pan**: Middle-click + drag
- **Orbit**: Left-click + drag
- **Zoom**: Scroll wheel

#### Rendering
Switch to raytracing mode via **Preferences** → **Raytracing** for higher-quality, slower renders.

#### 3D Models
Many KiCad footprints include 3D models. Users can add custom models to footprints.

### Fabrication Outputs

#### Gerber Files
1. **File** → **Plot**
2. Specify output directory
3. Verify essential layers are checked:
   - Copper layers (`*.Cu`)
   - Board outline (`Edge.Cuts`)
   - Solder mask (`*.Mask`)
   - Silkscreen (`*.Silkscreen`)
   - Paste layers (`*.Paste`) for stencils
   - Adhesive (`*.Adhesive`) if needed
4. Click **Plot**

#### Drill Files
1. In Plot dialog, click **Generate Drill Files**
2. Click **Generate Drill File**

These files specify hole locations and diameters for PCB manufacturing.

## Tutorial Part 4: Custom Symbols and Footprints

### Library Fundamentals

#### Organization
- Libraries hold either symbols **or** footprints, not both
- **Global libraries**: Available in all projects
- **Project libraries**: Available only within a specific project

#### Library Tables
KiCad tracks libraries in two tables:
- **Symbol library table**: **Preferences** → **Manage Symbol Libraries** (Schematic/Symbol Editor)
- **Footprint library table**: **Preferences** → **Manage Footprint Libraries** (Board/Footprint Editor)

#### Path Substitution
Libraries often use path variables enabling relocation without manual updates:
- `${KIPRJMOD}`: Points to current project directory
- Custom variables: **Preferences** → **Configure Paths**

#### Table File Locations
- **Windows**: `%APPDATA%\kicad\9.0\sym-lib-table` and `fp-lib-table`
- **Linux**: `~/.config/kicad/9.0/sym-lib-table` and `fp-lib-table`
- **macOS**: `~/Library/Preferences/kicad/9.0/sym-lib-table` and `fp-lib-table`

To reconfigure tables, delete or rename these files (backup first).

### Creating New Libraries

#### Symbol Library
1. Open Symbol Editor from Project Manager
2. **File** → **New Library**
3. Select **Project** for project-specific storage
4. Name the library (e.g., `getting-started.kicad_sym`)
5. Save in project directory
6. Library is automatically added to project library table

#### Footprint Library
1. Open Footprint Editor
2. **File** → **New Library**
3. Select **Project**
4. Name the library (e.g., `getting-started.pretty`)
5. Save in project directory

### Creating Custom Symbols

#### Symbol Creation
1. With library selected in Libraries pane, **File** → **New Symbol**
2. Enter **Symbol name** (e.g., manufacturer part number)
3. Set **Default reference designator** (e.g., "SW" for switches)
4. Accept other defaults

#### Adding Pins
1. Click **Add a pin** button
2. Set properties:
   - **Pin name**: Logical identifier (A, B, etc.)
   - **Pin number**: Matches datasheet numbering
   - **Electrical type**: Passive, Input, Output, Power In, etc.
   - **Orientation**: Right, Left, Up, Down
   - **Position**: X/Y coordinates

#### Grid Importance
**Always use 50 mil (1.27 mm) grid for symbol pins.** KiCad's built-in library uses 50 mil; misaligned pins cannot connect to wires.

Metric grids in schematic editing have no physical meaning but must align with 50 mil standard for connectivity.

#### Graphical Elements
Use line, circle, arc, polygon, and Bézier tools to draw symbol appearance. Switch to finer grids (e.g., 5 mil) for graphics, then return to 50 mil for any additional pins.

#### Symbol Properties
**File** → **Symbol Properties** (or double-click canvas):
- **Value**: Component designation or part number
- **Keywords**: Search terms
- **Show pin names**: Toggle to hide verbose pin labels

### Creating Custom Footprints

#### Footprint Creation
1. Open Footprint Editor
2. **File** → **New Footprint**
3. Edit properties:
   - **Footprint name**: Descriptive identifier
   - **Value**: Reference identifier
   - **Component type**: Through hole, SMD, etc.

#### Pad Placement
1. Use **Add a pad** tool
2. Set properties:
   - **Pad number**: Matches datasheet
   - **Position**: X/Y coordinates
   - **Hole diameter**: Through-hole size
   - **Pad diameter**: Copper pad size (hole diameter + 2 × annular ring)
3. Place pad on canvas
4. Repeat for additional pads (numbering auto-increments; properties copy)

#### Grid Strategy
Set custom grids matching pad spacing for precise alignment. Right-click grid icon → **Edit Grids** to create new grids.

#### Copper Pad Sizing
For example, 1.17 mm × 0.8 mm pins:
- Maximum diagonal: 1.42 mm
- Recommended hole: 1.42 + 0.2 = 1.62 mm
- Recommended pad: 1.62 + 2(0.15) = 1.92 mm (with 0.15 mm annular ring each side)

Larger annular rings improve solderability and mechanical robustness.

#### Graphical Layers

**Fabrication Layer (F.Fab):**
- Precise part outline matching physical dimensions
- Use line, rectangle, polygon tools
- Line width: Typically 0.10 mm

**Silkscreen Layer (F.Silkscreen):**
- Assembly reference outline, slightly larger than fab layer
- Offset: ~0.11 mm outside fab lines
- Line width: Typically 0.12 mm

**Courtyard Layer (F.Courtyard):**
- Boundary surrounding entire footprint
- Prevents overlaps with adjacent footprints
- Recommended clearance: 0.25 mm from part outline

### Linking Symbols, Footprints, and 3D Models

#### Default Footprint Assignment
1. Open symbol in Symbol Editor
2. **File** → **Symbol Properties**
3. Click in **Footprint** field
4. Click library book icon
5. Browse and double-click desired footprint
6. Save symbol

Once assigned, the footprint is preselected; manual reassignment can override this default.

#### Footprint Filters
Symbols can specify compatible footprints, restricting displayed options in the footprint assignment tool.

**Example**: `74HC00` symbol filters show only DIP and SO14 footprints.

#### 3D Model Association
1. Footprint Editor: Edit footprint properties
2. **3D Models** tab
3. Add model filename(s):
   - **STEP format** (`.step`): High dimensional accuracy
   - **VRML format** (`.wrl`): Visual appeal
4. Set scale, rotation, offset, and opacity

#### Supported Formats
- STEP: Industry-standard, suitable for mechanical CAD export
- VRML: Faster rendering, better visuals

#### Model Creation Tools
[FreeCAD](https://www.freecad.org/) with [StepUp Workbench](https://github.com/easyw/kicadStepUpMod/) is commonly used for KiCad's official library models.

## Additional Resources

### Documentation
- Full manual: https://docs.kicad.org/
- Version-specific docs: Available for 5.1, 6.0, 7.0, 8.0, 9.0, and nightly builds

### Community Support
- **Forum**: [forum.kicad.info](https://forum.kicad.info/)
- **Real-time chat**: Discord and IRC
- **Learning resources**: [kicad.org/help/learning-resources/](https://www.kicad.org/help/learning-resources/)
- **Showcase**: [Made With KiCad](https://www.kicad.org/made-with-kicad/)

### Contribution Opportunities
- **Bug reports/features**: **Help** → **Report a Bug** or [Gitlab issues](https://gitlab.com/kicad/code/kicad/-/issues)
- **Development**: [Developer Contribution page](https://dev-docs.kicad.org/en/contribute/)
- **Libraries**: [Contribute to libraries](https://www.kicad.org/libraries/contribute/)
- **Documentation**: [Docs team](https://www.kicad.org/contribute/docs-team/)
- **Financial support**: [Donation FAQ](https://www.kicad.org/donate/faq/)

---

**License Information**

Documentation is licensed under either:
- **Creative Commons Attribution License** 3.0+
- **GNU General Public License** v3+

This does not include KiCad source code, libraries, or third-party tools. See [kicad.org/about/licenses/](https://www.kicad.org/about/licenses/) for details.
