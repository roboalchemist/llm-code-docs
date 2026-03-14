# Source: https://docs.flux.ai/tutorials/custom-pad-shapes.md

# Creating Custom Shapes in Flux



Create custom shapes for pads, symbols, silkscreen and board layout.

![](https://uploads.developerhub.io/prod/86Yw/uz9oqvpsfugfn36svxd2k6ustl8smfkxfnn9bwanmbkjbmyq3yh2vp67btlh3ssa.png)


## Overview

Some elements come in many different forms. IC footprints, antennas, and other connectors all may have specific pad-shape requirements, some symbols require many different shapes and board layouts have all sorts of different requirements.

In this tutorial, we'll cover how to create and add custom shapes to many different elements, including pads, silkscreen, board layout and zones.

## Creating a Custom Shape

Flux supports DXF and SVG files as input for custom shapes. You can use any CAD or drawing tool to generate these shapes, but if you're not used to creating shapes we'd suggest you start with [Onshape](https://onshape.com) for DXF files or [Inkscape](https://inkscape.org/) for SVG files.

### Shape Requirements

Depending on what element you'll be using the shape in, there might be specific requirements:

- **Symbols**
    - Every shape and line should be white, with 1px stroke width and no fill
    - Pins are typically 10 to 18 pixels long
    - Basic parts (i.e. resistors, caps, transistors) typically fit in a 40x40 px area. Larger, more complicated parts, such as ICs, may require a larger area

- **Pads, Zones and Layout**
    - Lines need to form a single closed shape
    - Do not include any holes or cutouts. Those will need to be added afterward [using holes](https://docs.flux.ai/flux/reference/pads#pad-type)
    - Multiple lines need to be converted into a single polyline

- **Silkscreen**
    - No specific requirements

### Creating DXF Shapes with Fusion360

The video below covers how to create DXF shapes using Fusion 360 for a symbol, but the same process can be used to create a shape for any other element (pad, footprint and layout):




### Creating SVG Shapes with Inkscape

[Inkscape](https://inkscape.org/) is an open source tool, and it's available for most platforms. Even if you're unfamiliar with SVG files, the steps in this tutorial should be enough to help you create your first shape.

The video below covers how to create a custom symbol shape, but the same process can be used to create a shape for any other element (pad, footprint and silkscreen):




## Importing the Shape into Flux

There are two ways of adding generated shapes into Flux:

- **Using an asset:** This works on every scenario, both for DXF and SVG files
- **Injecting code directly on a shape rule:** This option works only for SVG shapes, and cannot be used for symbols

### Option 1: Using an Asset File

You can use an external DXF or SVG file to dictate the shape of a pad. This is a two-step process; first, you must add the SVG or DXF as an asset and then link the asset to the target pad.


#### Step 1: Adding DXF/SVG Files as Assets

To add an external file as an asset:

1. Make sure no object has been selected (click on the empty canvas)
2. On the right drawer, scroll down until you find the assets panel. Open it and click on "Add" (or "Manage"). This will open the assets dialogue.
3. Then click on "Add item" and select the file from your local drive.

![](https://uploads.developerhub.io/prod/86Yw/8q3wuyrzh618a2cv8i3stlqogtqo7h944hfggcykwa3de9vi47garqmndilx7dpp.gif)


> If you're creating a custom symbol and have added multiple assets, click the "Set this as default symbol" button.


![](https://uploads.developerhub.io/prod/86Yw/vf1uce82at2wletknt7pam6wsty6bvl8aghb3ogxjcpov2vk3p5wwih0484ga1vi.png)



#### Step 2: Link the Asset to the Target Element

Once you've added the SVG or DXF file to the asset list, then link the asset to the target element.

> Skip this step if you're creating a custom symbol. You can now go back to the symbols tutorial.


To link an asset to an element:

1. Select the element you want to make into a custom shape
- Silkscreen: Object type -&gt; Silk Line
- Board shape: Object type -&gt; Layout
- Pad: Object type -&gt; Pad
- Zone: Object type -&gt; Zone

2. Locate the "Layout rules" drop-down menu on the right-side panel
3. Find the "Object-specific rules" submenu
4. Click on "Add"
5. Find and add the "Asset" rule
6. Inside the "Asset" text box, select the SVG/DXF file added in the previous step from the list

![Example: adding an asset to a pad.](https://uploads.developerhub.io/prod/86Yw/vcb4eccj3215glc2mpgd0weyxoos1ilyjd43yalakcnegp9vn144i98gt72f44k8.gif)



#### Step 3: Scaling an Asset

By default, Flux assumes the imported file will be in **meters**. You might need to adjust the scale of the asset using a [scale rule](https://docs.flux.ai/flux/reference/layout-rules-types#scale).

### Option 2: Using the Shape Rule for SVG Code

Some elements (pad, layout, line, zone) allow you to add SVG code directly into the rule. _Custom-shaped symbols can only be created via the asset method_. To add the SVG code directly into a shape rule:

1. Open the PCB editor
2. Select the element you want to convert to a custom shape
3. Locate the "Layout rules" drop-down menu on the right-side panel
4. Find the "Object-specific rules" submenu
5. Click on "Add"
6. Find and add the corresponding "Pad shape", "Line shape", "Zone Shape", or "Layout Shape" rule
7. Inside the rule's text box, paste the SVG code. See the SVG code below as an example

```javascript
M 0.005 0.005 L -0.005 0.005 L -0.005 -0.005 L 0.003 0.001 z
```




![Example: adding SVG code directly to a Pad Shape rule](https://uploads.developerhub.io/prod/86Yw/o793ucq951j0560ono2sfu6st05f2lj0wrlw3w1w0le8815ktb6qdvopp7nmjudq.gif)


## What's Next

Now that you understand how to create and use custom shapes in Flux, you might want to explore:

- [Board Outline Shape Tutorial](https://docs.flux.ai/flux/tutorials/tutorial-board-outline-shape) - Apply custom shapes to your board outline
- [PCB Routing Tutorial](https://docs.flux.ai/flux/tutorials/routing-tutorial) - Learn how to route your PCB with custom pad shapes
- [Component Placement](https://docs.flux.ai/flux/tutorials/component-placement) - Learn how to efficiently place components with custom shapes
- [Layout Rules Tutorial](https://docs.flux.ai/flux/tutorials/tutorial-layout-rules-deep-dive) - Understand how to use rules to control your PCB design
