# Source: https://docs.flux.ai/reference/reference-inspector-assets.md

# Assets

External assets are used to leverage existing files (STEP, SVG, KICAD_MOD, etc) to improve Flux designs. Currently available formats are:

- .step, .stp, .dxf, .glb,: [3D models](https://docs.flux.ai/flux/tutorials/tutorial-import-part#4--importing-a-3d-model)
- .kicad or .kicad_mod: [Importing Components from Other EDA Tools to Flux](https://docs.flux.ai/flux/tutorials/tutorial-import-part)
- .svg: [Symbols](https://docs.flux.ai/flux/tutorials/tutorial-import-part#2--importing-a-symbol), [PCB outline](https://docs.flux.ai/flux/tutorials/tutorial-board-outline-shape) and [Creating Custom Shapes in Flux](https://docs.flux.ai/flux/tutorials/custom-pad-shapes)
- .dxf: [PCB outline](https://docs.flux.ai/flux/tutorials/tutorial-board-outline-shape) and [Creating Custom Shapes in Flux](https://docs.flux.ai/flux/tutorials/custom-pad-shapes)

![](https://uploads.developerhub.io/prod/86Yw/r8m99ss6ppmgr0xvqz9kp9s7yqhkqrdzmftgmay05ayf4mqr65soym2triu8vxwy.png)

**Important:** the assets menu is only available when no object has been selected. You can click on the empty canvas to make sure nothing is selected.

### Adding an external asset

To add an external file as an asset:

1. Make sure no object has been selected (click on the empty canvas)
2. On the right drawer, scroll down until you find the assets panel. Open it and click on "Add" (or "Manage"). This will open the assets dialogue.
3. Then click on "Add item" and select the file from your local drive.

![](https://uploads.developerhub.io/prod/86Yw/8q3wuyrzh618a2cv8i3stlqogtqo7h944hfggcykwa3de9vi47garqmndilx7dpp.gif)

## File Requirements

Depending on what element you'll be using the shape in, there might be specific requirements:

- **Symbols**
    - Every shape and line should be white, with 1px stroke width and no fill.
    - Pins are typically 10 to 18 pixels long.
    - Basic parts (i.e. resistors, caps, transistors) typically fit in a 40x40 px area. Larger, more complicated parts, such as ICs, may require a larger area.

- **Pads, Zones and Layout**
    - Lines need to form a single closed shape.
    - Do not include any holes or cutouts. Those will need to be added afterward [using holes.](https://docs.flux.ai/flux/reference/pads#pad-type)
    - When using SVG files, multiple lines need to be converted into a single polyline.

- **Silkscreen**
    - No specific requirements.

### Specific Requirements for DXF

A DXF is a type of vector file commonly used in CAD software. [Learn more](https://www.adobe.com/creativecloud/file-types/image/vector/dxf-file.html)

To work in Flux, a DXF file must meet the following criteria:

- Only contain [lines](https://documentation.help/AutoCAD-DXF/WS1a9193826455f5ff18cb41610ec0a2e719-79fe.htm), [splines](https://documentation.help/AutoCAD-DXF/WS1a9193826455f5ff18cb41610ec0a2e719-79e1.htm), [arcs](https://documentation.help/AutoCAD-DXF/WS1a9193826455f5ff18cb41610ec0a2e719-7a35.htm), [circles](https://documentation.help/AutoCAD-DXF/WS1a9193826455f5ff18cb41610ec0a2e719-7a2d.htm), and [ellipses](https://documentation.help/AutoCAD-DXF/WS1a9193826455f5ff18cb41610ec0a2e719-7a15.htm)
- **Cannot** contain any [polylines](https://documentation.help/AutoCAD-DXF/WS1a9193826455f5ff18cb41610ec0a2e719-79f0.htm).

Specific Requirements for SVG

The SVG is a type of vector file commonly used to display illustrations online. [Learn more](https://www.adobe.com/creativecloud/file-types/image/vector/svg-file.html)

To work in Flux, an SVG file must meet the following criteria:

- Unless being used for a silkscreen, the shape must be composed of a single, uninterrupted path. In most tools (like [Inkscape](https://inkscape.org/)), you can use the "Join selected nodes" tool to combine several shapes.
- Scale the SVG down. Due to a mismatch between SVG and Flux units, you will need to scale it down.

## Scaling SVG Files

Most SVG files are unit-less, meaning Flux doesn't know what what units (m, mil, cm, etc) the SVG file was designed on. For that reason, it will assume the file is in meters. 

If you need to change the scale of the file, you need to add a **"Scale"** [rule.](https://docs.flux.ai/flux/reference/object-specific-pcb-rules) to the object you're linking the asset to.