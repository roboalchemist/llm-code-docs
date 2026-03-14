# Source: https://docs.flux.ai/tutorials/creating-copper-cutouts.md

# Creating copper cutouts

Define copper-free regions on any layer

![](https://uploads.developerhub.io/prod/86Yw/c6wkohua5n632ue7qh4rp90tgod4e7blxhfblv4aasxgkgxxxis5bcsqfikijfd1.png)

## Overview

In some cases you may be designing a PCB that requires a copper cutout. For example when using an IC that contains an antenna that cannot have any underlying copper on any  layers beneath it. This tutorial will explain how to accomplish this in Flux.

There are two options for creating copper cutouts:

- **Keep Out Rule:** can be applied to any object. Will keep copper fills (and any other object) away from the element that the rule is applied to.
- **Zones:** is an object on its own. Can be placed on the design and configured to create a cutout on any layer.

## Keep Out Rule

In the case where you’d like to create a copper cutout around a pre-existing element simply add a [Keep Out](https://docs.flux.ai/flux/reference/layout-rules-types#keep-out) rule. This will push the auto-generated copper planes away from the part at the distance specified. **The keep out rule will only be applied to the layer where the object exists. To create multi-layer cutouts, you'll need to use a zone.**

- Select the object to create a copper fill around (such as an SMA connector or a mounting hole.)
- Navigate to the layout rules on the right and add a keep out rule.
- Add the keep out size. Remember you can select different x and y keep outs by typing `10mm 5mm`
- Flux should automatically regenerate the copper fill, thus creating a copper cut-out around the component

![](https://uploads.developerhub.io/prod/86Yw/f60qadecb9k29rvqsi05nwqrkkz7jd8rniv2u0ykcnq1nn6o8luoaqflcnky8x07.png)

## Zones

Zones are elements whose unique purpose is to create keep out regions with any shape or size, and on any layer.

### Adding a Zone

To add a new zone:

1. Find the object menu in the PCB editor
2. Click on the three dots menu next to the layout object
3. Select Add-&gt;Zone

![](https://uploads.developerhub.io/prod/86Yw/3u6yx6kdtz7vbtt2h6r4ahlzzz6810c7joekhd2v2wvh15ij5ue0het2r0hewz2o.png)

### Adjusting the Size

To adjust the zone size, select the zone and use the size menu in the toolbox. Remember you can select different x and y sizes by typing `15mm 29mm` .

![](https://uploads.developerhub.io/prod/86Yw/nmgan43peurtev8wwbh8opu8dsr2vm7baj5p00lrk5c8wzgms1v21cnf4s7obnq4.png)

### Modifying the Shape

Zones can easily be adjusted to be rectangular or circular by adding a Zone Shape rule. 

1. Select the zone
2. Navigate to the layout rules on the right and add a "Zone Shape" rule.
3. Simply type `circular` or `rectangular` in the "Zone Shape" text box.

![](https://uploads.developerhub.io/prod/86Yw/gak3jz1txexcgkn882qwb24wkn0hopu72qcev01fvzrnywctv81bguf3anhk1nhp.png)

#### Custom shapes

Zones can be modified to follow any shape. To do so, you'll need an SVG or DXF file. We have a full tutorial on [Creating Custom Shapes in Flux](https://docs.flux.ai/flux/tutorials/custom-pad-shapes) if you want to learn more about creating custom shapes.

![](https://uploads.developerhub.io/prod/86Yw/919n1vb8mevu3pfmy3n6in11a3816akycsy18wcx6jkydjk2aoyehm3d9px2mh9f.png)

### Selecting Target Layers

By default, zones are configured to apply to every layer in your design. To configure the zone for specific layers:

1. Select the zone
2. Navigate to the layout rules on the right and add a "Connected Layers" rule.
3. Click on the text box and select the layers you want to apply the keep out zone to.

![](https://uploads.developerhub.io/prod/86Yw/61ipwzopcfq6548vvcxoctkipxrctu1ftb3p0bk63t9xy966zligsh2ol66q4lsn.png)