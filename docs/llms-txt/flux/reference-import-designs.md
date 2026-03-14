# Source: https://docs.flux.ai/reference/reference-import-designs.md

# Importing Schematics from Cadence and Altium to Flux

Transfer your existing schematics into Flux from industry-standard tools like Cadence and Altium, allowing you to continue your design work without starting from scratch.

![](https://uploads.developerhub.io/prod/86Yw/q7l875o3xocc0pzgs826bu304htpgzyy3q54ieergljaecyhvrnqmsicel85pwbe.png)

## Overview

Flux allows you to import complete schematics from Cadence and Altium, making it easy to continue working on your designs without starting from scratch. For Cadence, we support **EDIF** files, and for Altium, we support the **ASCII** version.

## Getting Started

### Preparing Files for Import

#### Cadence

Depending on the product type and version you're using, the way of exporting an EDIF 300 file will vary. Please refer to the Cadence instruction manual. As an example, to export EDIF files on Cadence OrCAD:

1. Open your design in Cadence
2. Navigate to the export menu and select **Export as EDIF**
3. Save the EDIF file to a location on your computer

#### Altium

![](https://uploads.developerhub.io/prod/86Yw/mwy54kr6gcwti0fa2ywv6zq60b4la3y58rueo92phddm2712t2xd4k28hb7rol0f.png)

To export schematics from Altium:

1. Open your project in Altium Designer
2. Go to **File &gt; Save As** and select the **ASCII** file format
3. Save the file to your desired location

## Importing into Flux

Once you have your exported files ready, follow these steps to import them into Flux:

![](https://uploads.developerhub.io/prod/86Yw/q7l875o3xocc0pzgs826bu304htpgzyy3q54ieergljaecyhvrnqmsicel85pwbe.png)

1. Open the **Flux** menu on the top left
2. Go to the **Import** menu
3. Select **Cadence** or **Altium** based on your file type
4. Click **Upload** and select your exported file
5. Wait for the import process to complete
6. Review your imported schematic

### Keyboard Shortcuts

Use these keyboard shortcuts to speed up the import process:

| Action | Shortcut | 
| ---- | ---- | 
| Open Flux menu | Alt + F | 
| Import menu | Alt + I | 


> Make sure your design is saved in the correct format before attempting to import. Flux only supports EDIF for Cadence and ASCII for Altium.

## What Gets Imported

When importing schematics from Cadence or Altium, the following elements are transferred to Flux:

- Component symbols and footprints
- Net connections
- Component properties and values
- Part numbers and references
- Sheet organization

> Footprints and traces will not be imported from Altium or Cadence projects.

## Post-Import Steps

After importing your schematic, you should:

1. Verify all components were imported correctly
2. Check that all connections are maintained
3. Review component properties and values
4. Update any missing information

## Troubleshooting

### My file isn't importing correctly

- Verify that the file format is correct: EDIF for Cadence or ASCII for Altium
- Check if the file is complete and not corrupted

### Missing Components

- **Issue**: Some components don't appear in the imported schematic
- **Solution**: Check if the missing components use custom libraries in the original design; you may need to recreate these components in Flux

### Connection Issues

- **Issue**: Some connections between components are missing
- **Solution**: Review the original schematic and manually add any missing connections

## What's Next

Now that you've imported your schematic, you might want to explore:

- [PCB Layout Tutorial](https://docs.flux.ai/flux/tutorials/routing-tutorial) - Learn how to create a PCB layout from your imported schematic
- [Schematic Editor Reference](https://docs.flux.ai/flux/reference/reference-schematic-editor) - Master the Flux schematic editor
- [Component Library](https://docs.flux.ai/flux/reference/reference-library) - Learn how to manage components in Flux