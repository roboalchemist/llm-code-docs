# KiCad 9.0 GerbView (Gerber Viewer) Documentation

## Introduction to GerbView

GerbView functions as a specialized viewer for Gerber files (RS-274X format) and Excellon drill files. The application supports simultaneous display of up to 32 files.

For technical specifications, users can consult:

- [The Gerber File Format Specification](http://www.ucamco.com/files/downloads/file/81/the_gerber_file_format_specification.pdf)
- [The Excellon format description](http://web.archive.org/web/20071030075236/http://www.excellon.com/manuals/program.htm)

## Interface Components

### Top Toolbar Functions

The top toolbar provides access to essential operations:

- **File Management**: Clear all layers, load Gerber files, load Excellon drill files
- **Page Setup**: Set page size for printing
- **View Controls**: Print, redraw, zoom in/out, fit to page, zoom to selection
- **Layer Selection**: Choose active layer and display layer information
- **Gerber X2 Features**: Highlight components, nets, or attributes
- **D Code Highlighting**: Emphasize items using selected D codes on active layer

### Left Toolbar Tools

Navigation and display toggles include:

- **Selection and Measurement**: Item selection and point-to-point distance measurement
- **Display Options**: Grid visibility, polar coordinate display, full-screen cursor
- **Rendering Modes**: Sketch mode for flashed items, lines, and polygons
- **Layer Management**: Visibility controls, diff/compare mode, contrast adjustment
- **Additional Features**: Layer manager toggle, mirror image display

### Layers Manager Panel

The Layers Manager presents a comprehensive control interface with these interactions:

- Left-click selects the active layer
- Right-click reveals layer sorting and visibility options
- Middle-click or double-click modifies layer color
- The Layers tab governs visibility and coloring of all loaded content
- The Items tab manages grid, D Code, and negative object display properties

## Menu Bar Commands

### File Menu

The File menu includes an export feature: Export to PCB Editor provides conversion of Gerber files into KiCad PCBs with limitations based on RS-274X features used.

Conversion capabilities include:

- Flashed items convert to vias
- Lines convert to track segments (or graphics for non-copper layers)
- Rasterized items cannot be converted

### Tools Menu

Available tools include:

- **List DCodes**: Displays D Code information across all layers
- **Show Source**: Opens active layer Gerber file contents in text editor
- **Measure Tool**: Calculates distance between two points
- **Clear Current Layer**: Removes contents from active layer

## Printing Guidelines

Access printing via the toolbar icon or File menu. Before printing:

1. Verify items exist within the printable area
2. Use page size selection to choose appropriate format
3. Consider that photoplotters typically support larger plottable areas than standard printers
4. Reposition layer sets if necessary to fit within printer boundaries

---

**Documentation Version**: Based on KiCad 9.0.8
**License**: Creative Commons Attribution 3.0+ or GNU General Public License v3+
**Repository**: Available at GitLab under the KiCad project
