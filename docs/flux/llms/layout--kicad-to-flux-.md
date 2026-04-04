# Source: https://docs.flux.ai/Introduction/layout--kicad-to-flux-.md

# Layout (KiCAD to Flux)

In this final section, we’ll transition from schematic to layout, build your stackup, route traces, and manage ground and power planes.



## Overview

If you’re in a hurry, here’s what you need to know:

- Netlist and ECO do not exist in Flux. **Schematic and PCB data are automatically synchronized.**
- Everything you’ll find on the layout properties panel in Kicad, **in Flux you can find in the inspector tab (right side of the screen) under rule**s. [Learn more.](https://docs.flux.ai/flux/reference/reference-inspector-layout)
- **Flux automatically creates ground fills (planes) connected to ground**. [Learn more.](https://docs.flux.ai/flux/reference/reference-ground-fills)

## Going from Schematic to Layout

### In KiCAD

To forward your schematic changes into the layout editor, you need to use the “Update PCB from Schematic” menu. The process involves generating a Netlist and using an ECO to sync.

![](https://uploads.developerhub.io/prod/86Yw/oz84vapg7n6vddkah4nsnk04h2uvokaon4sajcwprj80hdjvbjs8e5j8f7gdxe96.png)

### In Flux



The schematic and layout editors are bidirectionally synchronized in real time. Bidirectional Sync means any changes in the schematic automatically update the PCB layout and vice-versa without the need to create a netlist or ECO.

> Real-time synchronization eliminates the risk of design discrepancies.

## Creating a Stackup

### In KiCAD

Layer properties are defined through the Properties menu.

![](https://uploads.developerhub.io/prod/86Yw/q68qvg9dt5l28u5wg0yy0fc7hhc5zj8udumj7hwrhqnrheyy8e7c45r66ynr8ue0.png)

### In Flux



The stackup is a characteristic of the layout object. You can think of the layout object as the actual PCB, so things like board layout or stackup are modified through the layout object via rules.

Rules are one of the most important concepts in the PCB editor. They are similar to KiCad’s footprint properties, but they act on every object (footprints, pads, traces, layout, etc). You can learn more about rules [here](https://docs.flux.ai/flux/tutorials/tutorial-layout-rules-deep-dive).

To modify your stackup:

1. Select the Layout object
2. Find the “Layout Rules” section under the “Inspect” panel on the right.
3. Click on “edit” then “add” and find the rule called stackup
4. Select a stackup template from the list, or click on the pencil icon to create a custom one.

> The layout object can also be modified to create different board shapes. [Learn more.](https://docs.flux.ai/flux/tutorials/tutorial-board-outline-shape)

## Routing Traces

### In KiCAD

To create traces on KiCAD, you need to select the trace tool and then start routing. Design rule checks (DRC) need to be manually run, often times after routing is finished.

![](https://uploads.developerhub.io/prod/86Yw/tzhsxo418o6cpag2txh8e1d9mhahn1gwp5m4p1mhzbag0nql9nw2fdegsrm4m6b8.png)

### In Flux



To start routing, click on a routing touch point and a trace will appear.

- Press F to change the route angle (elbow) direction and W to change the size of traces.
- Connect the components based on the schematic and airwires

As you route, you'll see air wires disappear and be replaced by copper. You can also switch the layer you're routing on by clicking `V`, to place a via and switch layers. After routing our board looks like so.

> Real-time Design Rule Checks (DRC) guide you as you route, ensuring your design stays within manufacturing constraints.. [Learn more.](https://docs.flux.ai/flux/reference/design-rule-check--drc-)

## Managing Ground and Power Planes

### In KiCAD

You manually create and configure copper pours for ground and power planes.

![](https://uploads.developerhub.io/prod/86Yw/qqp8a5iwkwf44nl86wlg3i55h0k0uqrfacf10xa5ak8ergtwxpdb4pyw3c65s0xk.png)

### In Flux



Ground fills are managed automatically once a ground portal has been placed in the schematic. You can configure those fills to be tied to other nets. You can learn more about that here.

> Automatic handling of ground and power planes reduces setup time and ensures consistency.