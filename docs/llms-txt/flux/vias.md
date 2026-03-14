# Source: https://docs.flux.ai/reference/vias.md

# Vias in PCB Design



Learn how to use the different kind of vias (blind, buried, micro and through-hole) to connect traces across multiple layers.

![](https://uploads.developerhub.io/prod/86Yw/selxhzk1v2u4czh7w1f3p18bqxp3hnmslrufmzf7lfos88mqvxpakfnmlqe2m6ge.png)


## Overview

Vias are conductive connections that allow signals to pass between different layers of a PCB. Here's a short overview of the different via types:

- **Through vias:** Connect the two outer layers (Top and Bottom), and every layer in between
- **Blind vias:** Connect an outer layer to an inner layer without going all the way through to the other outer layer
- **Buried vias:** Connect two internal layers without reaching any outer layer
- **Microvias:** Very small vias typically used to connect adjacent layers

## Via Configuration

To configure the via types that will be available to route the project you'll need to use the stackup editor:

1. Select the layout object from the object tree on the left-side panel
2. Locate the "object-specific" rules menu on the "Inspector" panel on the right-side
3. Add a new Stackup [rule](https://docs.flux.ai/flux/reference/pcb-rules)
4. Click on the pencil icon

![](https://uploads.developerhub.io/prod/86Yw/fyn1zybto7stpdnxrpc40na02m1phyhcw660t83sec17m8tvci09nv7ozk0fwgfh.gif)


### Configuring Via Types

By default, only through-hole vias are configured. To add more via types on the stackup editor:

1. Scroll all the way to the right on the stackup editor
2. Click on `+ Via Config` at the top-right of the stackup editor
- A new Via config column will be created
- You can edit the name of the via type by double-clicking on the column name

3. Click on `+ Via` at the bottom of the column to add new vias to the type
- You can click the +Via button as many times as you need to add more vias

4. Click to select the newly added via and configure it with the via panel on the right
- Use "Laser Drill" for microvias and "Mechanical Drill" for all the rest of the types
- Hole Size and Size parameters can be typed directly, or configured as a group as mentioned in the next step

![](https://uploads.developerhub.io/prod/86Yw/ce82v44qhrnh1llcy4ti1newlmlln2pehfknvow6p3qaw7voxjk5i2yzl5df87c8.gif)


### Configuring Via Size

You can configure pre-determined via and via hole sizes for quicker via configuration. To add via size configuration groups:

1. Navigate to the "Via Hole Configs" tab within the stackup editor
2. Modify the default "Mechanical Drill" group, or add a new group by clicking the "+Via Hole Config" button on the bottom-left corner of the editor
3. The configured groups will be visible when configuring a via on the "Stackup and Vias" tab

![](https://uploads.developerhub.io/prod/86Yw/9q1pzvgwk038ncl67lt00uyfarvai83tadmqjtxg296kq1g9m8rzorzi6riqtghz.gif)


## What's Next

Now that you understand how to configure and use vias in Flux, you might want to explore:

- [PCB Routing Tutorial](https://docs.flux.ai/flux/tutorials/routing-tutorial) - Learn how to route your PCB using vias for layer transitions
- [Stackup Editor](/reference/reference-pcb-editor/stackup-editor) - Understand how to configure your PCB layer stackup
- [Smart Vias](/reference/vias/smart-vias) - Learn about advanced via features in Flux
- [Layout Rules Reference](https://docs.flux.ai/flux/reference/pcb-rules) - Understand how to use rules to control your PCB design
