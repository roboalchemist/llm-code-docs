# KiCad 9.0 PCB Editor (pcbnew) Documentation

## Overview

The KiCad PCB Editor is a cross-platform layout application for designing printed circuit boards. It integrates footprint management, interactive routing, design rule checking, and fabrication output generation in a unified environment.

## Core Interface Components

**Main UI Elements:**
- Top toolbars for file management and zoom tools
- Left toolbar displaying options
- Right toolbar for design and drawing tools
- Appearance panel for layer and object management
- Selection filter panel
- Message panel and status bar

**Navigation:**
The editor supports pan and zoom operations via middle/right mouse button dragging and wheel scrolling. Multiple zoom tools enable fitting to page, objects, or custom areas.

## Layer System

The layer architecture supports:
- Up to 32 copper layers
- 14 technical layers (silkscreen, solder mask, adhesive, paste)
- 13 general-purpose drawing layers

The active layer is always drawn on top of other layers, with related layers displaying above unrelated ones based on the current active selection.

## Board Setup and Configuration

### Physical Parameters
Board stackup configuration includes:
- Copper layer count and thickness specifications
- Dielectric material parameters
- Solder mask and paste clearance settings
- Board finish designation

### Design Rules

Three-tier constraint system:
1. **Constraints section** - absolute minimums that cannot be overridden
2. **Net Classes** - routing rules for groups of nets
3. **Custom Rules** - scriptable design rule language for complex scenarios

No rule may override the minimum values set in the Constraints section.

### Text Variables

The system allows dynamic text substitution using "${VARIABLENAME}" syntax. Variables persist across schematics and boards within a project.

## Object Placement and Editing

### Footprint Operations

**Placement methods:**
- Automatic import from schematic
- Manual placement via Add Footprint tool
- Repositioning with Move, Drag, Flip, and Rotate commands

**Positioning Tools:**
- Standard Move (M) - ignores unselected tracks
- Drag (D) - maintains track connections using interactive router
- Move Exactly (Shift+M) - precise coordinate input
- Position Relative (Shift+P) - offset from reference points
- Position Interactively - vector-based positioning

**Multi-footprint operations:**
- Move Individually (Ctrl+M) - sequential repositioning
- Pack and Move (P) - grouped movement
- Swap (Alt+S) - exchange positions between footprints

### Grids and Snapping

The grid system features:
- Dynamic grid sizing via toolbar dropdown
- Custom grid creation with unequal X/Y spacing
- Grid overrides for specific object types
- Configurable origin points (grid, page, drill/place, local)

Tools only snap to objects on visible layers, with modifier keys disabling individual snap types:
- Ctrl disables grid snapping
- Shift disables object snapping

**Snapping to graphics** includes endpoints, midpoints, centers, and intersection points with auxiliary projection lines.

## Drawing and Placement Tools

Available tools from right toolbar:

| Tool | Function |
|------|----------|
| Selection | Default interaction mode |
| Footprint Placement | Add components to board |
| Route Tracks | Interactive trace routing with multiple modes |
| Add Vias | Standalone via placement |
| Add Zones | Filled copper regions |
| Rule Areas | Keepout and constraint zones |
| Graphical Shapes | Lines, arcs, rectangles, circles, polygons, beziers |
| Text/Textbox | Annotation objects |
| Dimensions | Orthogonal, aligned, center, radial, and leader annotations |
| Deletion | Remove selected objects |

## Routing System

The interactive router supports:
- Push-and-shove mode for obstacle avoidance
- Walkaround mode circumventing obstacles
- Highlight collisions mode showing blockages
- Differential pair routing with length/skew tuning
- Multiple via placement modes

Length tuning patterns allow:
- Single-track length adjustment
- Differential pair length matching
- Skew tuning for signal integrity

## Design Rule Checking

The DRC system validates:
- Clearance violations (copper spacing)
- Track width constraints
- Via diameter specifications
- Unconnected nets
- Malformed board outlines
- Courtyard collisions

Design rule violations such as incorrect and missing connections, copper clearance and minimum width violations trigger error or warning markers based on configured severity levels.

## Display Controls

### Appearance Panel Tabs

**Layers:** Manages visibility, color, and opacity of board layers with dynamic ordering based on active layer selection.

**Objects:** Controls visibility and opacity of tracks, vias, pads, zones, and other graphical elements independently from layers.

**Nets:** Displays all electrical connections with individual visibility controls and color assignment options for ratsnest visualization.

### Layer Presets and Viewports

Preset system stores layer visibility configurations for quick recall. Viewports save view location and zoom state. Both include quick-switcher access via Ctrl+Tab and Shift+Tab respectively.

### Display Modes

Non-active layer rendering options:
- Normal - all layers visible
- Dimmed - inactive layers reduced opacity; selection restricted to active layer
- Hidden - inactive layers invisible; selection restricted to active layer

## Selection Mechanics

**Single-click selection** allows item targeting with modifier behavior:
- Ctrl/Cmd - toggle selection
- Shift - add to selection
- Ctrl+Shift/Cmd+Shift - remove from selection
- Long-click/Alt/Option - clarify from popup menu

**Box selection:**
- Left-to-right (yellow box) - exclusive (fully inside only)
- Right-to-left (blue box) - inclusive (touching selected)

**Selection Filter Panel** controls which object types can be selected. Locked items checkbox independently manages locked object selectability.

## Net Highlighting and Cross-Probing

Net highlighting visualizes electrical routing by emphasizing selected nets and dimming others. Activation methods:
- Hotkey ` after selecting copper objects
- Right-click context menu
- Nets tab in Appearance panel
- Net Inspector double-click

**Cross-probing** enables bidirectional schematic-PCB synchronization:
- Selection cross-probing highlights corresponding items
- Highlight cross-probing synchronizes net emphasis
- Both can be configured independently in Preferences

## Fabrication Outputs

Supported export formats:
- Gerber with job files
- IPC-2581 (unified format)
- ODB++ (advanced format)
- GenCAD, PDF, SVG, HPGL
- STEP, GLB, BREP, XAO, PLY, STL, IDF, VRML (3D models)

Component placement and drill files support various CAM formats for manufacturing.

## Advanced Features

### Teardrops

Connection fillets at pad-track junctions configure:
- Round pad connections
- Rectangular pad connections
- Track-to-track connections

Parameters include length, height, and curve styling with individual override capability.

### 3D Viewer

Visualizes board in three dimensions with:
- Model viewing and rotation
- Layer color representation
- Stackup height visualization
- 3D export capability

### Custom Design Rules Language

Scriptable rule system enables:
- Complex conditional constraints
- Pattern-based net class assignments
- Syntax validation before application

### Properties Manager

Docked panel displaying editable properties of selected items. Supports multi-item editing with per-object application of changes rather than group transformations.

## Keyboard Shortcuts

**Key Navigation:**
- Ctrl+F1 - display hotkey list
- Space - reset relative coordinates to zero
- N/Shift+N - cycle to next/previous grid
- E - edit selected item properties
- A - add footprint
- M - move
- D - drag with track maintenance
- F - flip to opposite side
- R/Shift+R - rotate counter/clockwise
- Shift+M - move with exact coordinates
- Shift+P - position relative to reference
- Alt+S - swap footprint positions
- T - get and move footprint by reference
- O - select all unconnected footprints
- Shift+O - grab nearest unconnected footprint
- Ctrl+M - move footprints individually
- P - pack and move footprints
- ` - highlight net
- ~ - clear net highlight
- Ctrl+` - toggle net highlighting display
- Ctrl+H - cycle layer display mode
- Shift+S - toggle layer-specific snapping

---

**Documentation Version**: Based on KiCad 9.0.8
**License**: GNU General Public License v3+ or Creative Commons Attribution License 3.0+
