# Source: https://docs.flux.ai/tutorials/working-with-polygons.md

# Working with Polygons

Learn how to create and use custom copper shapes with the polygon feature in Flux.



## Overview

Polygons in Flux allow you to create custom copper shapes that are tied to specific nets. This feature is useful for creating:

- Custom ground planes
- Power distribution networks
- RF and antenna elements
- Thermal management areas
- Signal integrity improvements

## Getting Started

### Creating a Polygon

To create a polygon in Flux:

1. Hover over a pad in your PCB design
2. Right-click to open the context menu
3. Navigate to **Start Routing Polygon**
4. Click on the canvas to place points for your polygon
    1. **Shift** while placing points to enable free-angle mode (otherwise points snap to 45° angles)
    2. Right-click to remove the last point

5. To complete the polygon, either:

- Click on the middle of the pad you started from, or
- Double-click anywhere else on the canvas

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/0dzipdkhspk9bbk5h333colunav7bdx3dn5z1p1u9krf7ry0h2x1cdxyyumc7886.png)

### Editing Polygons

Once you've created a polygon, you can edit its shape:

1. Select the polygon in your design
2. Double-click on the polygon to enter edit mode
3. In edit mode, you can:
    1. Click and drag existing points to move them
    2. Double-click on a point to delete it
    3. Hover near an edge to reveal midpoints that can be clicked to add new points

4. Click on the **"Finish Editing"** toolbar

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/9jlhl8096ewn0h3q4wwxvvirriwxkibqsti2f2tqgmnahbu0418802hrj8qp50fe.png)

## Advanced Polygon Shapes

Polygons are normally used to create arbitrary or custom copper shapes. The easiest way of doing so is by using the polygon editing feature as described in the previous section. You can also create polygons with basic shapes provided by Flux, or use SVG syntax to import shapes from other CAD tools.

### Basic Shapes

If you want to create a basic rectangular or circular polygon, you can use the **shape** rule. To create a basic shape:

1. Create a polygon of any shape using the manual polygon creator as described in the previous section.
2. Select the polygon and find the **Inspect** menu on the top right.
3. Under **Object-specific rules**:
    1. Click on **Edit -&gt; Add**
    2. Find and add the **Polygon Shape** rule.
    3. On the newly added rule, delete the existing data and type **rectangle** or **circle**
        1. Keep in mind that the polygon might have moved out of position.
        2. You can also use the size [rule](https://docs.flux.ai/flux/reference/pcb-rules) to modify the shape

### Custom Shapes

If you need to import an existing shape from another CAD tool, you can use it through an SVG path:

1. Create a polygon of any shape using the manual polygon creator as described in the previous section.
2. Select the polygon and find the **Inspect** menu on the top right.
3. Under **Object-specific rules**:
    1. Click on **Edit -&gt; Add**
    2. Find and add the **Polygon Shape** rule.
    3. Change the existing SVG path for the one you want to import

## Multi-Layer Polygons

Polygons in Flux can span multiple copper layers, creating a unified copper structure across your PCB:

1. Create a polygon as described earlier
2. Select the polygon and find the **Inspect** menu on the top right.
3. Under **Object-specific rules**:
    1. Click on **Edit -&gt; Add**
    2. Find and add the **Connected Layers** rule.

4. Select the layers you want to connect from the dropdown menu
5. The polygon will now exist on all selected layers
6. Via stitching is automatically applied to connect the layers electrically
    1. You can adjust the [Fill Stitching Density](https://docs.flux.ai/flux/reference/layout-rules-types#fill-stitching-density) and [Fill Stitching Offset](https://docs.flux.ai/flux/reference/layout-rules-types#fill-stitching-offset) li rules to control the via pattern
    2. You can also manually place additional vias if needed

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/6kz9u106tplnbcnrm0cqsoyb315pp4epsudowjoc28udwuzuv3fu97tidvm6izcf.png)

Multi-layer polygons are particularly useful for:

- Creating power and ground planes that span multiple layers
- Implementing RF shields that enclose sensitive circuits
- Designing thermal management structures that distribute heat across layers

Flux automatically handles island removal for polygons, eliminating any disconnected copper areas that might form during the polygon creation process. This ensures that all copper within your polygon is electrically connected to the net.

## Polygon Hierarchy and Priority

When multiple polygons overlap, Flux uses a size-based priority system to determine which polygon takes precedence:

1. **All polygons take priority over [Copper fills](https://docs.flux.ai/flux/reference/reference-ground-fills)**
2. **Smaller polygons take priority** over larger polygons
3. Polygons of the same net will merge unless they have different properties

This automatic priority system allows you to:

- Create complex copper structures with cutouts by using smaller polygons
- Implement split planes for different power domains
- Design sophisticated RF structures with controlled impedance
- Create thermal relief patterns around component pads

## Keep Outs and Polygons

Keep Outs can be used to create spacing areas between your polygons and other elements in your project. To add a keep out to a polygon:

1. Create a polygon as described earlier
2. Select the polygon and find the **Inspect** menu on the top right.
    1. You can also select the entire net to apply a keep out to every object in that net. This is specially useful if you have several polygons in the same net.

3. Under **Object-specific rules**:
    1. Click on **Edit -&gt; Add**
    2. Find and add the **Keep Out** rule.

4. Select the distance you want the polygon to be removed from other elements.

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/m60tgpg7k7kfzgnugwk4dp4edqyemajv7stzqsag0u32670m2s2sne94mbamjmqd.png)

When a keep outs is applied to a polygon and other elements are present in the keep out space:

- **If the element colliding with the polygon has been generated by Flux** (other polygon, via sitching, etc), said element will be moved respecting the shape of the polygon.
- **If the element colliding with the polygon has been generated by the user** (components, pads, manual vias, etc) the polygon shape will be adjusted to stay away from that element

## Tips for Working with Polygons

- **Simplify shapes**: Complex polygons with many points can impact performance
- **Use with fills**: Polygons work well with copper fills to create custom ground planes
- **Layer selection**: Make sure to select the appropriate layers for your polygon
- **Hotkeys**: Use Shift while drawing to toggle between constrained (45°) and free angle modes
- **Via stitching**: Automatically applied for multi-layer polygons, but can be adjusted
- **Island removal**: Flux automatically removes disconnected copper areas within polygons

## Related Features

- [Copper Fills](https://docs.flux.ai/flux/tutorials/tutorial-ground-fills-deep-dive)
- [Via Stitching](https://docs.flux.ai/flux/reference/vias#via-stitching)
- [PCB Design Reviews (DRC)](https://docs.flux.ai/flux/tutorials/pcb-design-review)

You can also ask [Flux](https://docs.flux.ai/flux/reference/copilot) for help with creating and optimizing polygons for your specific design needs.