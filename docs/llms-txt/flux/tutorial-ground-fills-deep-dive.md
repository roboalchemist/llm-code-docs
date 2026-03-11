# Source: https://docs.flux.ai/tutorials/tutorial-ground-fills-deep-dive.md

# Copper Fills in PCB Design: A Comprehensive Guide

Improve heat transfer, design RF circuits, or create efficient and reliable ground and power connections with copper fills.



## Overview

If you’ve never seen a copper fill in a real PCB, it may not be evident because fills are often covered by a solder mask. Copper fills essentially “fill in” all the unused area on a layer in a PCB with copper. Depending on what they are connected to, we can identify two main types of copper fills:

- **Ground fills** are copper fills connected to a ground net.
- **Power fills** are copper fills connected to one of the power nets.

## Ground Fills (Ground Planes)

Most PCB designs will benefit from having a ground-connected copper fill in every layer. This includes top companies like Apple, where they use ground fills everywhere to improve the quality of their boards.

For this reason, **ground fills are enabled by default in Flux.** Whenever there's a ground symbol in the schematic editor, every layer of the PCB layout will contain a fill connected to the ground (GND) net. It's also possible to [modify this behavior](https://docs.flux.ai/flux/reference/reference-ground-fills#enabling-fills-on-specific-layers) for those designs where ground fills need to be completely disabled or enabled in specific layers only.

### Why Ground Fills by default?

- **Improved signal integrity**: Ground acts as a shield for important signals. Having ground between noisy nets and the signals you care about will keep them clean, reduce ringing, and help your board function as expected.
- **Improved power distribution**: Ground is the universal return path for all signals on the board, especially for your power nets. The more ground you have, the more robust your return path will be. This allows all of your different parts to work in harmony instead of causing noise for each other with small return paths.
- **Improved heat distribution:** On larger boards, your components can generate heat, and that heat will start to diffuse around the board. When copper fill is present, the heat can be easily carried away from the heat source by the copper fill. The result is a more even temperature distribution throughout the PCB that reduces local hotspots which may cause damage.
- **Improved board stability:** No more worrying about keeping an even copper distribution on matched pair layers. When you have ground fills everywhere, this is taken care of automatically. This leads to higher yield and better warp/twist performance.
- **No added cost**: There may have been a time when copper fills added cost to the manufacturing process, but not anymore. Boards start as solid sheets of copper, and then that copper is etched away to create the traces and channels needed for your design. Keeping copper where there would have been empty space saves etchant and, at the same time, improves board performance as well.

### When Should You Disable Ground Fills?

Although fills generally can provide some useful benefits in many PCBs, there are instances where it is important to disable fills on one or more layers. Therefore, we made ground fills [very easy to disable.](https://docs.flux.ai/flux/reference/reference-ground-fills#enabling-fills-on-specific-layers)

Some examples of when fills should be disabled on one or more layers include:

- Antenna designs and analog circuits have very specific grounding requirements where copper should not be placed below these elements.
- You have a high density of traces on one layer, and it will be very difficult to place the stitching vias to connect fills to these layers. Because the fill could leave behind unconnected islands, it may be best to omit fills.
- Controlled impedance traces (such as D+ and D- lines forUSB) will have their impedance modified if copper fill is brought too close.

If you do decide to remove copper fills, make sure to apply the removal symmetrically in the layer stack. This will ensure that you have still achieved copper balance and will experience maximum board stability.

## Power Fills (Power Planes)

In certain situations, you might need to create copper fills that are connected to a power net, instead of a ground net. Benefits of creating power fills (power planes) include:

- **Greater current carrying capacity:** Copper fills handle larger currents and result in lower operating temperatures making them a good alternative to using traces for delivering power.
- **Shorter return paths:** Copper fills provide shorter return paths compared to traces, improving EMC performance.
- **Better decoupling:** improved decoupling helps stop noise and energy from spreading from circuit to circuit in the power supply.

Unlike ground fills, **power fills are not enabled by default.** [Here's more information](https://docs.flux.ai/flux/reference/reference-ground-fills) on how to enable them.

> Fills can be connected to any net, but ground and power planes are generally the most widely used.

## Stitching Vias

The easiest way to connect fills on different layers is through an array of vias in a regular pattern. This array of vias (known as stitching vias) [can be set up automatically](https://docs.flux.ai/flux/reference/reference-ground-fills#via-stitching) inside the PCB editor in Flux. There's no need to place these vias manually. You can still add strategically placed vias to a net if your design requires it.

## Automatic Island Removal

Island removal works a bit differently in Flux than you might be used to. We've designed the island removal algorithm to perform just like an experienced engineer would, but automatically.

Before removing any copper islands, Flux’s algorithm tries to connect them using vias (we call these 'Island Vias'). This happens automatically—copper will only be removed if there is absolutely no way to connect it to the rest of the fill. You don’t need to do anything; if it’s possible to connect the fill copper, our algorithm will ensure it happens. If not, the island will be automatically removed. [Here’s more information about how the island removal algorithm works](https://docs.flux.ai/flux/reference/reference-ground-fills#copper-islands-removal).

## Using Copper Fills

Now that we know why and when you should be using copper fills, let's cover the basics on how to use them. If you need more information on how to enable, disable or connect fills to specific traces or layers, please refer to the [copper fills reference section.](https://docs.flux.ai/flux/reference/reference-ground-fills)



## Changing Edge Clearance for Copper Fills

In the case you'd like to change the default clearance value for copper fills, see below. Clearance values for copper fills can be set individually for the following objects:

- Board outline
- Traces
- Pads and vias
- Any other components

There are two ways to accomplish this, both through the [keep out](https://docs.flux.ai/reference/layout-rules-types#keep-out) rule.

### Option 1: Editing the Copper Fill's Layout Rules

For this option, select the _GND net_ associated with the copper full and add a _keep out_ rule. Then specify the desired edge clearances:

- For all objects simply enter the desired clearance value in mm'
- For specific objects, enter the object name followed by parentheses and the desired clearance value.
    - For example: `0.15mm vias(0.5mm) pad(2mm)` will keep all vias 0.5mm away and all pads 2mm away, while every other object type will stay away by 0.15mm

### Option 2: Editing the Object's Layout Rules

This second option relies on editing the object's rules pushing the copper fill out.

Select the object you'd like to create clearance from it and the copper net and add a _keep out_ rule. Then specify the desired edge clearances:

> Element, Pad, Trace, Via, Layout, Net

- Since you are specifically interested in creating a clearance value between it and a copper fill, enter the desired distance as follows: `fills(0.5mm)` replacing 0.5mm with the desired clearance value.

### Applying Spacing from Board Edge

The way to apply spacing between copper fills and the board edge is with a rule called [Board Inset Margin](https://docs.flux.ai/flux/reference/layout-rules-types#board-inset-margin) that can be applied to the layout object. This rule applies to everything element on the editor.

## Troubleshooting Common Issues

### Unconnected Islands

If you notice isolated copper islands that aren't connecting to the main fill:

- Check that your via stitching settings are appropriate for your design
- Verify that there's enough space for the algorithm to place vias
- Consider manually adding vias in critical areas

### Clearance Issues

If you're experiencing DRC errors related to copper fill clearances:

- Review your keep-out rules for the specific objects
- Check for conflicting rules that might be causing unexpected behavior
- Ensure your clearance values meet your manufacturer's requirements

### Performance Impact

If copper fills are causing slow performance in the editor:

- Consider temporarily hiding fills while working on dense areas
- Use layer-specific fills rather than fills on all layers
- Optimize your rule settings to reduce computational complexity

## Custom-Shaped Copper Areas with Polygons

If you need more control over the shape of your copper areas beyond what standard copper fills provide, you should consider using polygons. Polygons allow you to create custom-shaped copper areas with precise control over their geometry.

For detailed instructions on creating and working with polygons, refer to the [Working with Polygons](/tutorials/routing-tutorial/working-with-polygons) tutorial.