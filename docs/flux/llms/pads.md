# Source: https://docs.flux.ai/reference/pads.md

# Pads and Holes

Pads enable real-world connection to components. In Flux, pads are also how you add holes. 

![](https://uploads.developerhub.io/prod/86Yw/chspx6fdk18tdf6yl2tvglhtci3qwtqcmlxz5fdsba5365igdup0kchio65ydpn4.png)

## Adding a Pad

In Flux, you can add a pad that'll be a part of a net, or you can add standalone pads.

### Adding a Net-connected Pad

The most common way to add a pad in Flux is to add a terminal to schematic. This is because every terminal automatically generates a corresponding pad on the PCB editor. So when you want to create a pad that will be connected to a net, simply add a terminal on schematic and connect that terminal to a net. 

This is useful for things like creating footprints for components, or when you want to create a test point for a net.

**To add a pad to footprint:**

1. On schematic, drag a terminal from the library onto the canvas.
2. Switch to PCB and configure the pad to your specification.

**To add a pad to a layout:**

1. On schematic, add drag a terminal from the library onto the canvas.
2. Connect the terminal to a net.
3. Switch to PCB and configure the pad to your specification.

### Adding a Standalone Pad

You may want to add a pad to PCB which isn't connected to a net. You can do this directly on the PCB canvas. Please note that this freestanding pad will have no corresponding terminal on schematic, and so cannot be included in a net.

**From the PCB canvas:**

1. Right click the PCB canvas to trigger the Context Menu.
2. Hover over Add in the Context Menu to reveal a submenu.
3. Click Pad in the submenu.

**From the PCB Object List:**

1. In the list, locate the object under which you'd like to add the pad. 
    1. If you're making a board, this is most likely the Layout object. 
    2. If you're making a component, this is most likely the Footprint object.

2. Click on the ... icon to the right of the object's name, or right click the object, to trigger the Context Menu.
3. Hover over Add in the Context Menu to reveal a submenu.
4. Click Pad in the submenu.

## Adding a Hole

In Flux, holes are a special type of pad. To create a hole, set a pad's Pad Type rule to HOLE.

This may sound strange, but it actually allows for a great deal of flexibility. You can move seamlessly between types without deleting anything. Start with a surface mount pad, then decide you need a through hole pad, or change the spec to a mounting hole, or add back an annular ring for better grounding.

Holes – also known as mounting holes, mechanical holes, or non-plated through-holes (NPTH) – serve a different function from vias. To connect a trace, polygon, or fill to another layer, [use a via](/flux---documentation/flux/reference/vias).

Flux currently only supports circular and pill shaped holes.

### Adding a Net-connected Hole

You might want to add a hole that's connected to a net. For example, if you want to connect a mounting hole to ground. This is done in the same way as adding a pad with a couple extra steps:

1. On schematic, drag a terminal from the library onto the canvas.
2. Connect the terminal to a net.
3. Switch to PCB.
4. Click on the pad to select it.
5. In the toolbar which shows up above the pad on the canvas, click Pad Type. (Look for the square icon.)
6. Select HOLE.

### Adding a Standalone Hole

You might want to add a hole that isn't associated with any net. This done just like adding a standalone pad:

**From the PCB canvas:**

1. Right click the PCB canvas to trigger the Context Menu.
2. Hover over Add in the Context Menu to reveal a submenu.
3. Click Pad in the submenu.
4. In the toolbar which shows up above the pad on the canvas, click Pad Type. (Look for the square icon.)
5. Select HOLE.

**From the PCB Object List:**

1. In the list, locate the object under which you'd like to add the pad. 
    1. If you're making a board, this is most likely the Layout object. 
    2. If you're making a component, this is most likely the Footprint object.

2. Click on the ... icon to the right of the object's name, or right click the object, to trigger the Context Menu.
3. Hover over Add in the Context Menu to reveal a submenu.
4. Click Pad in the submenu.
5. In the toolbar which shows up above the pad on the canvas, click Pad Type. (Look for the square icon.)
6. Select HOLE.

### Adding a Hole from the Library

Some Flux users have configured holes with certain specs and published them to the library. For example, you could find a component that contains a hole with shielding vias surrounding it. Try searching the library for holes to see if a component can save you time.

## Configuring a Pad

### Configure a Pad using the Toolbar

Configuring a pad is easy with the toolbar. When a pad is selected on PCB, a toolbar shows up above it on the canvas. From there, you can change its position, size, pad type, pad shape, and hole size.

### Configure a Pad using Layout Rules

If you need to get in deeper, you can use layout rules in the inspector. To learn how to add rules to objects, please refer to our documentation on [Layout Rules Reference](https://docs.flux.ai/flux/reference/pcb-rules).

#### Pad Type

![](https://uploads.developerhub.io/prod/86Yw/g4kkjv7o7rauucwq6dkdypdggl3c0h7zezk653ah45awenj8ikrce72dkuifkm5f.svg)

**Modifies the type of pad** to one of the following:

- SMD – a surface mount pad with no drill hole. 
- HOLE – a drill hole with no copper. 
- STD – a through-hole pad. (STD stands for "Standard".)
- CONN – a connector pad with no drill hole, often used at the edges of a board.

#### Pad Shape

![](https://uploads.developerhub.io/prod/86Yw/jr6fggfi6f02mvh3e1hprrfwhr3op7mkqy7qagm6btmzlq3zn8aidns5lmfft1cx.svg)

**Modifies the shape of the pad** to one of the following:

- Circular
- Rectangular
- [Custom shape with SVG syntax](https://docs.flux.ai/flux/tutorials/custom-pad-shapes#using-the-pad-shape-rule)

#### Solder Mask Expansion

![](https://uploads.developerhub.io/prod/86Yw/9k06mj6ty30a2dikbtm86re0i06by3lk8g2th2dk2ddp61ygxecw14hf2de3k4fn.svg)

**Defines the size of the opening in the solder mask relative to the pad edge**. All pads have a solder mask set by default that matches the size and shape of the pad. This rule allows the edge of the solder mask to expand beyond or contract within the edge of a pad. A positive value will expand the edge, a negative value will contract the edge, and a value of 0 will match the edge to the pad.

Graphically, this layer is _negative_ on the canvas. That means the shape you see covering the pad on the canvas is actually an opening in the solder mask. In other words, that area of the pad will be exposed to the air.

#### Solder Mask Expansion From Hole Edge

![](https://uploads.developerhub.io/prod/86Yw/y20fyap86mnyzpmu8iu92i0qdji6qrhhjifbhu6b28p3ffifymjcg0zv0tstawf2.svg)

**Defines the size of the opening in the solder mask relative to the hole.** This rule allows the edge of the solder mask to expand beyond or contract within the edge of a drill hole. A positive value will expand the edge, a negative value will reduce the edge, and a value of 0 will match the edge to the drill hole.

#### Solder Paste Mask Expansion

![](https://uploads.developerhub.io/prod/86Yw/85bw5k6r2wvumuiysrhdkfiyrsr4rqyzsy5dmyo8zavk9l7a6xs2s61atq2lqo91.svg)

**Defines the size of the solder paste mask**. All pads have a solder paste mask set by default that matches the size and shape of the pad. This rule allows the edge of the solder paste mask to expand beyond or contract within the edge of a pad or via. A positive value will expand the edge, a negative value will contract the edge, and a value of 0 will match the edge to the pad or via.

Graphically, this later is _positive_ on the canvas. That means that the shape you see covering the pad on the canvas will be covered by solder paste during the manufacturing process.

#### Hole Size

**Sets the size of a drill hole** in the pad.

#### Hole Position

**Defines the location of a drill hole in the pad**, measuring from the center of the drill hole relative to the center of the pad.

#### Thermal Relief

![](https://uploads.developerhub.io/prod/86Yw/3ievtug7wbvbdo3qdf9qqtgznr3y7fnq958gnuw7v0875uxiwbte3q1r3qqq8sw6.svg)

**Defines how a pad connects to a fill.** The Relief Connect option separates the pad from the fill and connects them with conductors. The distance of the separation is defined by the Keep Out rule. Useful when soldering a component to a pad. The Direct Connect option is essentially "no thermal reliefs". It removes the conductors and prevents Keep Outs from having an effect, allowing the pad and the fill to connect directly.

Related rules include Thermal Relief Conductors, Thermal Relief Conductor Width, and Thermal Relief Conductor Angle.