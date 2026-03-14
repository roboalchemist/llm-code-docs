# Source: https://docs.flux.ai/tutorials/working-with-footprints.md

# Working with PCB Footprints

Create professional footprints that match your team's requirements and design specifications.

![](https://uploads.developerhub.io/prod/86Yw/1uv1vtx6aue4bkjx37q0k5a5g2dz9mlyhgdfv2zbhjr65gwzk2l836n2xvczjgkn.png)

## Overview

In this tutorial, we'll cover how to work with the PCB Editor to create custom footprints for your components. Whether you're designing a footprint from scratch or modifying an [imported footprint](https://docs.flux.ai/flux/reference/reference-import-designs), these techniques will help you create accurate, manufacturable component layouts.

Footprints define the physical layout of components on your PCB, including pad sizes, shapes, positions, and silkscreen markings. Creating precise footprints is essential for successful PCB manufacturing and assembly.

## Adding Pads

The first step in creating a footprint is adding pads for component pins or leads. Pads are the copper areas where component pins make electrical contact with the PCB.

Every terminal you add in your schematic will have a corresponding pad in the PCB Editor. If you want to add a pad that doesn't need to be connected to other pads (a mounting hole for example) follow the steps below:

- Click on the "Footprint" node in the right-side panel under "Objects"
    - If you don't have a "Footprint" object, click on the three dots of the "Root" object and add a Footprint.

- Click on the three-dots menu of the "Footprint" object and "Add" a "Pad."

Note: If you want to connect this pad to a terminal in the future, match the designators on the terminal and pad together.

To add pads to your footprint:

1. In the PCB Editor, click on the "Objects" tab in the right panel
2. Right-click on the footprint and hover over "Add"
3. Select "Pad" from the menu
4. Click to place the pad on the canvas
5. Repeat for each pad needed in your footprint

## Setting Pad Position

Precise pad positioning is crucial for component alignment and manufacturability. You can:

### Method 1: Drag and Drop

- Simply click and drag pads to position them visually

### Method 2: Precise Positioning

For exact placement:

1. Select the pad to move
2. Navigate to the "Object Specific Rules" in the right panel
3. Find the `Position` rule
4. Enter the desired x and y coordinates in millimeters

- You can also use "in" and "mil" for inches and mils (thousandths of an inch)

![](https://uploads.developerhub.io/prod/86Yw/p9qj6f74nlfmd47iem4ahgsaha1dj2tubxpxwlzoenzzqoadc1vxy5zfs7nhvw1b.gif)

## Modifying Pad Size and Shape

After positioning your pads, you'll need to set their size and shape according to your component's specifications.

### Individual Pad Modification

To modify a single pad:

1. Select the pad
2. In the right panel, add the "Pad Size" and "Pad Shape" rules
3. Set the desired dimensions and shape
4. Optionally, add "Pad Type" to create a through-hole pad

### Batch Pad Modification

To modify multiple pads at once:

1. Use selectors to target specific pads
2. For all pads, use the "pad" selector
3. For specific pads, use #Designator (e.g., "#VCC, #GND, #A0")
4. Apply the same rules to all selected pads

![](https://uploads.developerhub.io/prod/86Yw/g6drqp3l447wl4jooh4v14saaw2fhqdrjt7hss32lc4vrwdu4hz7150sepk4h5v8.gif)

For advanced pad shapes and customizations, refer to our [Custom Pad Shapes](https://docs.flux.ai/flux/tutorials/custom-pad-shapes) tutorial.

## Adding Silkscreen Shapes

Silkscreen markings help identify component orientation and boundaries during assembly. To add silkscreen elements:

### Adding Silkscreen Lines

1. Click on the "Objects" tab in the left panel
2. Right-click on the footprint, hover over "Add", and select "Silk line"
3. Add the `Shape Start` and `Shape End` rules to the silk line
4. Enter the desired x and y position values for each endpoint

- You can also drag endpoints or rotate lines (Right-click → Rotate)

5. Repeat to create an outline of your component

### Adding Text Labels

1. Click on the "Objects" tab in the left panel
2. Right-click on the footprint, hover over "Add", and select "Text"
3. Add the `Content` rule to the text node
4. Enter the desired text (e.g., component reference, pin 1 indicator)
5. Position the text appropriately

![](https://uploads.developerhub.io/prod/86Yw/f0qsbp1rs2ynunrtdlm5lnwhj7oss6ijxcfc0vf4yyl9w511cdsjwfxalht9nzrh.png)

## Setting the Origin

The origin point defines the reference position for your footprint when placed in a project. It's represented by the intersection of two blue lines in the PCB editor.

![](https://uploads.developerhub.io/prod/86Yw/c3boq21aiwu3wt1j287xzin1ou4mzafylq4d1cqai9q4jj16hzv3yc987mu5vlcm.png)

The origin placement affects how your component behaves when placed in a larger project:

### Centered Origin

For a centered origin (e.g., in a 3-pin part):

1. Position pads symmetrically around the origin
2. This makes the component's `location` rule correspond to the center of the component

![](https://uploads.developerhub.io/prod/86Yw/z0d3uceolw5imn88jjdmfko5lzl6pd47uqr0xwn1ur4pqrhla8d1g94jmhwskzhe.png)

### Pin-Centered Origin

To center the origin on a specific pin:

1. Position that pad at the origin (0,0)
2. This makes the component's position correspond to that specific pin

![](https://uploads.developerhub.io/prod/86Yw/pfoxqirrb55sn0oxgg54ns9rwo8zuqar6cqrv95snqb4hp0v10jdu21r9z89djm3.png)

## Best Practices for Footprint Creation

1. **Follow datasheets precisely**: Always refer to manufacturer datasheets for exact dimensions
2. **Include adequate clearance**: Design footprints with appropriate clearance for manufacturing tolerances
3. **Add polarity indicators**: Use silkscreen markings to clearly indicate pin 1 or component orientation
4. **Consider thermal relief**: For high-power components, ensure adequate thermal management
5. **Standardize when possible**: Use industry-standard footprints when available for consistency

## Troubleshooting Common Issues

### Pad Alignment Problems

- Double-check all measurements against the datasheet
- Ensure you're using the correct units (mm, mil, inches)
- Verify that the origin is set appropriately for your component

### Silkscreen Issues

- Make sure silkscreen lines don't overlap with pads
- Keep text size appropriate for manufacturing capabilities
- Ensure polarity indicators are clear and visible

### Footprint Compatibility

- Test your footprint with the actual component if possible
- Verify pad sizes are appropriate for both soldering and the component leads
- Check that the footprint works with your manufacturing process constraints

## What's Next

Now that you've learned how to create footprints, you might want to explore:

- [Working with Symbols](https://docs.flux.ai/flux/tutorials/working-with-symbols) - Learn how to create schematic symbols for your components
- [Custom Pad Shapes](https://docs.flux.ai/flux/tutorials/custom-pad-shapes) - Discover how to create specialized pad geometries
- [Publishing to the Library](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library) - Share your footprints with your team
- [Creating a Complete Part](https://docs.flux.ai/flux/tutorials/tutorial-creating-a-part-from-scratch) - Combine footprints with symbols to create complete components