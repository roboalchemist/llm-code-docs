# Source: https://docs.flux.ai/reference/reference-ground-fills.md

# Copper fills

Configure ground fills and power fills (ground planes and power planes).

![](https://uploads.developerhub.io/prod/86Yw/sgbnq6zqr7kbqcnz2frnbf8cef511l6o19w22ndzagg8w1ey0fbt401talziukb6.png)

## Overview

There are a few general guidelines to remember about using copper fills in Flux:

- All copper fills (ground and power) are **hidden by default.** Here's how to [make them visible](https://docs.flux.ai/flux/reference/reference-ground-fills#copper-fills-visibility).
- **Ground fills are enabled in every layer by default**. Here's how to [disable them.](https://docs.flux.ai/flux/reference/reference-ground-fills#enabledisable-copper-fills)
- **Power fills are disabled in every layer by default**. Here's how to [enable them.](https://docs.flux.ai/flux/reference/reference-ground-fills#enabledisable-copper-fills)
- **Stitching vias are not applied automatically.** Here's how to [configure them.](https://docs.flux.ai/flux/reference/reference-ground-fills#via-stitching)

## Enable/Disable Copper Fills

Fills can be enabled or disabled on each layer by assigning a "Connected Layers" rule to the target net. If the target net is a ground net it is known as a ground fill, while if the target net is a power net it's known as a power fill.

To enable or disable a copper fill for a target net:

1. Select the target net (nested under Root → Layout → Nets  in the Objects panel
2. Add a "Connected Layers" rule from the "object-specific rules" menu on the right.
3. Select all layers for which you want the fill to be enabled. Leaving the text box empty will disable the fill connected to that net on every layer.

![](https://uploads.developerhub.io/prod/86Yw/a5569h0f045no1zkt51yw9gypwlp3121r3ka4578476tg0xuxp6a14wci434zrzp.gif)

> Leaving the "Connected Layers" rule empty will **disable copper fills on every layer for that net.**

> Ground fill layers are not defined as negative layers in the Gerber files; they will appear as standard positive layers once the PCB is exported to Gerber files.

## Copper Fills Visibility

When fills are enabled, their visibility can be toggled within the _Layer_ panel in the PCB editor. As shown below, there is an option to disable only the fill visibility next to the layer visibility tool.

![**Drop icon**: Only toggles visibility of the copper fills - **Eye icon**: Shows or hides all copper in the respective layer](https://uploads.developerhub.io/prod/86Yw/jbstmz7l2f6kmmxm6kcv00s2lca59zudzm8yyifyyrz7cnco363f6p5ozh9wt1th.png)

**Note:** toggling the visibility button **will not disable the fill**, it will only hide it from the view. Removing the fill altogether can only be done through the ["Connected layers" rule](https://docs.flux.ai/flux/reference/reference-ground-fills#enabling-fills-on-specific-layers).

## Via Stitching

Via stitching can be enabled and configured with the use of two rules:

- **Fill Stitching Density**: vias will be spaced by the amount specified in this rule. Any non-zero value enables via stitching.
- **Fill Stitching Offset**: shifts the via stitching block by the amount specified. 

Follow these steps to add one or both of the rules:

1. Select the ground net (nested under Layout → Nets → GND in the Objects panel)
2. Add the desired rule from the "object-specific rules" menu on the right.
3. Enter the offset and/or density values as distances.

![](https://uploads.developerhub.io/prod/86Yw/reih2b1eye75vbwxlzx9j3k6utpgffupv73x8vjaun4wvf372bot3q70qx0wufrv.gif)

**Note:** both rules accept x and y input (vector rules). For example, typing "10mm 13mm" on Fill Density will create stitching with 10mm separation on the x-axis and 13mm separation on the y-axis.

## Copper Islands Removal

Copper Islands are defined as pieces of copper in a fill that are not directly connected to a pad or via. To minimize the removal of copper, Flux's island removal algorithm is designed to automatically insert vias (referred to as "Island Vias") where possible.

Any pieces of copper that cannot be directly connected or connected through vias to the target net are classified as islands and removed.

### Island Vias

The algorithm analyzes fill geometry to determine which pieces of copper can be connected to the net that the fill belongs to through an Island Via. It can retain islands even via complex, multi-layer routes to the target net. There's no need to worry about creating an easy path for the island vias; it will find a way. The process works according to the following specifications:

- **Island Vias are dynamically adjusted**. Meaning that whenever there is a change in the layout due to the addition or removal of a pad, or the creation or removal of a trace, the algorithm will recalculate connections and decide if an Island Via is necessary or possible.
- **Island Vias are always through vias**. Meaning they will only be inserted where a fill connected to the same net already exists on every layer both below and above.
- **Island Vias respect minimum trace widths**. Meaning they will not be inserted if the insertion of the Island Via would breach the minimum trace width on any layer.
- **Island Vias will only be connected to fills**. Meaning they will not be inserted on top of vias, pads, traces, or any other elements apart from fills.