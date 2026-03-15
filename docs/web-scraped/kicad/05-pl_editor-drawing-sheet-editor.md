# KiCad 9.0 Drawing Sheet Editor (pl_editor) Documentation

## Overview

The Drawing Sheet Editor is a specialized tool within KiCad designed to create customizable drawing sheets for use in schematic and PCB designs. These sheets can incorporate title blocks, frames, logos, and other graphic elements.

## Core Components

### Basic Drawing Sheet Items

The editor supports several fundamental element types:

- **Lines**: Segments defined by start and end points
- **Rectangles**: Two-point shapes with defined corners
- **Text**: Strings with optional keyword replacement functionality
- **Poly-polygons**: Complex vector shapes (created via Image Converter tool)
- **Bitmaps**: Raster images in common formats (PNG, JPEG, BMP)

**Note**: Bitmaps render only in PDF and PostScript; other formats show bounding boxes.

## File Format

Drawing sheets are stored as `.kicad_wks` files. The default sheet loads automatically when the editor starts; alternative sheets can be opened through the standard file dialog.

## Coordinate System

### Position Definition

All item positions reference a specific page corner, enabling sheets to adapt automatically when paper sizes change. This prevents repositioning when dimensions shift.

### Reference Corners

Four corners serve as reference points: top-left, top-right, bottom-left, and bottom-right. Title blocks typically anchor to the bottom-right corner by default.

For multi-point items like lines and rectangles, each endpoint can reference different corners.

## Text and Keywords

### Keyword Syntax

Keywords follow the pattern `${KEYWORD}` and are replaced with actual values during use:

| Keyword | Function |
|---------|----------|
| `KICAD_VERSION` | Software version number |
| `#` | Current sheet number |
| `##` | Total sheet count |
| `COMMENT1`-`COMMENT9` | User-defined comment fields |
| `COMPANY` | Organization name |
| `FILENAME` | Source file name with extension |
| `ISSUE_DATE` | Release date field |
| `LAYER` | Active PCB layer (plots only) |
| `PAPER` | Current paper size designation |
| `REVISION` | Revision identifier |
| `SHEETNAME` | Current sheet designation |
| `SHEETPATH` | Hierarchical sheet location |
| `TITLE` | Project title |

**Example**: "Size: ${PAPER}" displays "Size: A4" when A4 is selected.

### Multi-line Text

Two methods enable line breaks:

1. Insert `\n` character sequence (primarily in Page Setup dialogs)
2. Press Enter directly in the Design window

To display literal `\n` text, enter `\\n`.

## Display Modes

**Preview Mode**: Displays the sheet as end-users see it, with keywords replaced by actual values.

**Edit Mode**: Shows raw content including unreplaced keywords.

## Constraints and Limitations

### Page-Specific Display

Items can be configured to display on:

- All pages
- First page only
- Subsequent pages only

This setting appears in the Item Properties panel dropdown.

### Text Size Constraints

Text elements support maximum height and width boundaries. When text exceeds these limits, it compresses to fit—potentially causing visual distortion. Setting either parameter to `0` disables that constraint.

## Rotation and Repetition

### Rotation

Text and poly-polygons support angular rotation (measured in degrees). Lines and rectangles cannot rotate.

### Repeat Option

Items can be duplicated across the sheet. Repeated text accepts increment values for numeric or alphabetic sequences—useful for gridlines and labels.

## Interface Components

### Main Toolbar Icons

| Icon | Function |
|------|----------|
| New | Create new sheet |
| Open | Load existing sheet |
| Save | Save to `.kicad_wks` format |
| Settings | Configure page size and user data |
| Print | Print current view |
| Undo/Redo | Revert/restore changes |
| Zoom controls | Navigation and magnification |

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| F1 | Zoom in |
| F2 | Zoom out |
| F3 | Refresh display |
| F4 | Center view |
| Home | Fit to window |
| Space | Set relative coordinates |
| Arrow keys | Cursor movement (grid-based) |

### Mouse Operations

- **Scroll wheel**: Zoom at cursor position
- **Ctrl + Scroll**: Horizontal panning
- **Shift + Scroll**: Vertical panning
- **Right-click**: Context menu with add/zoom/grid options

## Properties Editor

The right panel displays item-specific settings when an item is selected. Two tabs appear:

**Item Properties**: Type-dependent parameters for the selected element

**General Options**: Default values and margins for the entire sheet

Changes require clicking the **Apply** button to take effect.

## Design Inspector

This table view lists all sheet elements and their attributes. Accessible via **Inspect** → **Show Design Inspector**, it provides an alternative selection method and maintains selections when closed.

## Workflow: Adding Items

### Creating Elements

1. Click the appropriate toolbar icon (line, rectangle, text, or bitmap)
2. Click the canvas to place the item
3. Configure properties in the right panel
4. Click **Apply** to finalize

Alternative: Right-click canvas and select from context menu.

### Moving Items

Use keyboard shortcut `M` or drag directly on canvas. Multi-point shapes allow individual point manipulation.

### Adding Logos

1. Use the Image Converter tool to create a poly-polygon
2. Select **Append Existing Drawing Sheet** in the menu
3. Choose the converted file
4. Position and adjust the imported logo

### Importing Bitmaps

Supported formats include PNG, JPEG, and BMP. Default resolution is 300 PPI; adjust in properties editor. Higher PPI values increase file size and rendering time.

## Practical Considerations

### Corner Reference Best Practices

For stable sheets across size changes, use consistent corner references for both endpoints of lines and rectangles.

### Bitmap Limitations

- PDF and PostScript support full rendering
- Other output formats display only bounding boxes
- Plan accordingly when selecting export methods

---

**Document Status**: Based on KiCad 9.0.8
**License**: Content available under Creative Commons Attribution 3.0 or GNU General Public License v3
