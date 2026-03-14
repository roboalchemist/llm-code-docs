# Source: https://docs.flux.ai/reference/gerber-export.md

# Gerber Exports and Manufacturing Files

Gerber files are the industry-standard format for PCB manufacturing. Flux makes it easy to export complete manufacturing file packages for fabrication and assembly.

## Quick Export Guide

To export Gerber files and manufacturing data from Flux:

1. Click the **Flux logo** in the top-left corner
2. Navigate to **Export** &gt; **Manufacturing Files (Gerbers, etc)**
3. A ZIP file containing all necessary manufacturing files will be downloaded

## What's Included in the Export

The manufacturing files export includes:

- **Gerber RS-274X files** for all copper layers (top, bottom, and internal)
- **Soldermask layers** (top and bottom)
- **Silkscreen layers** (top and bottom)
- **Solderpaste layers** (top and bottom)
- **NC drill files** for holes and vias

## Additional Manufacturing Files

Beyond Gerber files, you may need additional files for assembly:

- **Bill of Materials (BOM)** - Component list with part numbers and quantities
- **Pick and Place files** - Component coordinates for automated assembly

## Comprehensive Export Guide

For complete information about all available export formats including netlists, 3D models, and project files, see the [Data Portability reference](https://docs.flux.ai/flux/reference/data-portability).

## Validation

After exporting Gerber files, it's recommended to validate them using an online viewer like [tracespace.io](https://tracespace.io/view/) before sending to your manufacturer.

Learn more about the complete manufacturing workflow in the [Manufacturing & Export Guide](https://docs.flux.ai/flux/Introduction/getting-started-in-flux--export-and-manufacturing).