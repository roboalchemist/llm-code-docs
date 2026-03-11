# Source: https://docs.flux.ai/reference/layout-rules-types.md

# Layout Rules List

List of available layout rules in Flux, including summary, examples, and related rules for each.

![](https://uploads.developerhub.io/prod/86Yw/kes7luxld834h9rotyfsmf5zcjoc9likdf7stdgxvmqekjrv70ihdwympj7vvaf3.png)

## Keep Out

Prevents other objects from getting closer than the defined distance outside the bounds of the target object. Other tools call it "spacing" or “clearance". The _Keep Out_ rule can be configured to apply to the target object against all other objects, or only against specified objects.

**Example 1:** Creating a _Keep Out_ rule between a specific pad and all other objects.

- Option 1: add an [object-specific rule](https://docs.flux.ai/flux/reference/object-specific-pcb-rules) to the target pad and write the _Keep Out_ distance. Typing `1.5mm` in the keep out rule will create a 1.5mm distancing.
- Option 2: create a new [selector-based rule](https://docs.flux.ai/flux/reference/pcb-layout-rule-selectors) and use the selector to match the target pad. You can use the pad designator to match it by typing `#[designator]` in the selector textbox. Then typing `1.5mm` in the _Keep Out_ rule will create 1.5mm distancing.

**Example 2:** One of the most common use cases for this rule is to set the distance between a net and [copper fill ](https://docs.flux.ai/flux/tutorials/tutorial-ground-fills-deep-dive)or a [polygon](https://docs.flux.ai/flux/reference/polygons-reference). Keep-out rules can now be applied directly to nets, making it easier to manage clearances.

- Find the net you'd like to target in the object tree.
    - Pro tip: change the net's designator to something easily identifiable.

- Add a Keep Out rule directly to the net
- Type `fills(1.5mm)` in the Keep Out rule textbox. This will make the Keep Out rule only apply to fills.
    - Pro tip: you can also type `0.5mm fills(1.5mm)` in the Keep Out rule. That will set a Keep Out of 0.5mm for every other object, but a 1.5mm Keep Out for fills.

> Keep out rules are bidirectional, meaning they apply in both directions between objects. For example:> > - If you apply a keep out rule to a pad, a polygon or fill might be moved to accommodate for the keepout> - If you apply a keep out rule to a fill or polygon, the polygon will also be moved to accommodate for the keepout.> > This bidirectional behavior ensures clearance is enforced regardless of which object was created first or which one has the rule applied to it.

## Board Inset Margin

Defines the spacing between board elements and the board edge. This rule can only be applied to layout objects and applies to all elements on the board.

**Example:** To create a consistent clearance between all copper elements and the board edge, add a Board Inset Margin rule to the layout. This replaces the previous method of applying layout rules to layouts or nets for board edge spacing.

## Auto Layout Gravity

Defines how close elements are laid out when initially positioned in the PCB editor. Accepts values from 0 to 1, with 0 putting elements close together and 1 putting elements farther apart.

**Example:** Add an “Auto Layout Gravity” rule from the layout rules sidebar. Once more in the “Layout Rules” in the bottom right sidebar, select a value between 0 and 1, this will set how close elements are by default when placed.

## Asset

Apply an asset file to an object. Select an asset that’s been added to a component’s Asset Panel and to associate it with a supported object.

**Example:** Suppose you have a specific ._SVG_ file you want to use as a custom symbol. Simply select the object (whether it be a footprint or model), and add an asset rule. Then [import your .SVG file](https://docs.flux.ai/reference/reference-inspector-assets#adding-an-external-asset) and associate it with the object through the asset rule. This also works for .DXF Files as well.

## Connected Layers

Defines which layers an object connects to. Useful for copper fills, vias or STD pads to set which layers have annular rings (or are connected to a fill) and which layers to skip.

**Example:** Select a via that connects to two or more layers. In the “Object Specific Rules” section, add a “Connected Layers” rule. Select which layers you want the via to be connected to. Selected layers will have an annular ring while unselected layers will simply have a hole.

## Content

Sets the string that a text object displays on the PCB canvas. Overrides any default string that may be present.

The _Content_ rule of an object defaults to be the same as the designator's name. In other words, the text displayed on a text-object is the same as the designator.

**Example:** Suppose you’d like to have a piece of text on your board that is the title of your project title. Add a _Content_ rule in the _Object-Specific rules_ section of a piece of text and input _=project.name_. Through this method, if your project name changes, then the text on your board will automatically change with it. In the case you would like the text to remain fixed, simply input the desired text.

## Corner Radius

Adds rounding to the corners of an object.

**Example:** Select any pad or rectangle that you’d like to round the corners of. For example, creating a round rectangle pad to solder to insert a rectangle. Then add the _corner radius_ rule. The number you enter for this rule corresponds to the radius of the circle as shown in the image.

#### Clamping Related Rules

- **Corner Radius Minimum**: Prevents the corner radius of an object from being smaller than this value.
- **Corner Radius Maximum**: Prevents the corner radius on an object from being larger than this value.

#### Specific Related Rules

- **Corner Radius Top Left**: Adds rounding to the top left corner on an object.
- **Minimum Corner Radius Top Left**: Prevents the top left corner radius of an object from being smaller than this value.
- **Maximum Corner Radius Top Left**: Prevents the top left corner radius of an object from being larger than this value.
- **Corner Radius Top Right**: Adds rounding to the top right corner on an object.
- **Minimum Corner Radius Top Right**: Prevents the top right corner radius of an object from being smaller than this value.
- **Maximum Corner Radius Top Right**: Prevents the top right corner radius of an object from being larger than this value.
- **Corner Radius Bottom Right**: Adds rounding to the bottom right corner on an object.
- **Minimum Corner Radius Bottom Right**: Prevents the bottom right corner radius of an object from being smaller than this value.
- **Maximum Corner Radius Bottom Right**: Prevents the bottom right corner radius of an object from being larger than this value.
- **Corner Radius Bottom Left**:  Adds rounding to the bottom left corner on an object.
- **Minimum Corner Radius Bottom Left**: Prevents the bottom left corner radius of an object from being smaller than this value.
- **Maximum Corner Radius Bottom Left**: Prevents the bottom left corner radius of an object from being larger than this value.

## Dynamic Trace Width

Configures [dynamic tracing](https://docs.flux.ai/flux/reference/dynamic-traces) for the target net.

**Example:** Suppose you want to route two 500um traces from two consecutive 200um pads. Select both nets under the _Nets_ section in your _Objects_ panel. Add a new _Dynamic Trace Width_ rule under the _Object-specific rule_ section to both nets and input _500um_ into the entry box. When you route these two nets, they will start at 200um to fit the pads, but will automatically expand to 500um as soon as they have enough clearance.

## Fill Stitching Density

Sets the density of vias for copper fill stitching.

**Example 1:** Suppose you want to create efficient heat distribution between your layers. Select your _GND_ net under the _Nets_ section in your _Objects_ panel. Add a new _Fill Stitching Density_ rule under the _Object-specific rule_ section. Input _3mm 5mm_ into the entry box to create vias spaced horizontally 3mm apart and vertically 5mm apart.

## Fill Stitching Offset

Sets the offset position of copper fill stitching pattern.

**Example 1**: Select your _GND_ net under the _Nets_ section in your _Objects_ panel. Add a new _Fill Stitching Offset_ rule under the _Object-specific rule_ section. Input _1mm 2mm_ into the entry box to offset vias 1mm horizontally and 2mm vertically from the edge.

## Font Size

Sets the size of the typeface that a text object displays.

**Example**:  Select the desired text. For example, that of a component reference designator. Add a `Font Size` rule to scale the text up or down.

#### **Clamping Related Rules:**

- **Font Size Maximum:** Prevents the font size of a text object from being larger than this value. Useful for tolerances.
- **Font Size Minimum**: Prevents the font size of a text object from being smaller than this value. Useful for tolerances.

## Grid Spacing

Sets the global grid spacing for the PCB layout. This rule can only be applied to the root object and cannot be overridden.

## Hole Position

Defines the location of a drill hole in this object, measuring from the center of the drill hole relative to the center of a parent object.

**Example**: Suppose you’d like to have a hole offset within a larger pad on your board. With the Pad Type rule set to STD, add a Hole Position rule. Here, you can set the X and Y offset from the center of the pad.

### Specific Related Rules

- **Hole Position X:**
Defines the location of a drill hole in this object - along the X axis only - measuring from the center of the drill hole relative to the center of a parent object.
- **Hole Position Y:** Defines the location of a drill hole in this object - along the Y axis only - measuring from the center of the drill hole relative to the center of a parent object.

## Hole Size

Sets the size of any drill holes in this object.

**Example 1:** Suppose you’d like to have a smaller hole within a larger pad on your board. With the _Pad Type_ rule set to _STD_, add a _Hole Size_ rule. Here, you can set the size of the smaller hole within the pad.

**Example 2:** Suppose you’d like to insert drill holes at the corner of your board. Add a pad to the board and set the _Pad Type_ to hole. Then simply position your object in the desired location and set the _Hole Size_ rule to the desired size as well.

#### Clamping Related Rules

- **Hole Size Minimum:** Prevents the size of any drill holes in this object from being smaller than this value. Useful for tolerances.
- **Hole Size Minimum X:** Prevents the size of any drill holes in this object - along the X axis only - from being smaller than this value.
- **Hole Size Minimum Y:** Prevents the size of any drill holes in this object - along the Y axis only - from being smaller than this value.
- **Hole Size Maximum:** Prevents the size of any drill holes in this object from being larger than this value. Useful for tolerances.
- **Hole Size Maximum X:** Prevents the size of any drill holes in this object - along the X axis only - from being larger than this value.
- **Hole Size Maximum Y:** Prevents the size of any drill holes in this object - along the Y axis only - from being larger than this value.

#### Specific Related Rules

- **Hole Size X:** Sets the size of any drill holes in this object along the X axis.
- **Hole Size Y:** Sets the size of any drill holes in this object along the Y axis.

## Line Path

Customizes the shape of silk lines using SVG path syntax.

**Example**: In the case you’d like a custom line path for your silk screen line, apply the line path rule. First, import [your custom .SVG file](https://docs.flux.ai/reference/reference-inspector-assets#adding-an-external-asset). Then, associate the files in the _Line Path_ rule’s input box.

## Pad Shape

Defines the shape of a pad, either circular or rectangular.

**Example 1**: Suppose you want to insert a circular pad for a testpoint. Ensure your pad is routed to the associated net and add a _Pad Shape_ rule. Setting it to rectangular will make the base shape rectangular. Setting it to circular will ensure that the shortest sides of the “rectangular” pad will always be rounded perfectly.

## Polygon Shape

Defines the shape of a polygon, either circular, rectangular or SVG path

**Example 1**: Suppose you want to create a perfectly circular polygon. If you want to create a basic rectangular or circular polygon, you can use the **shape** rule. To create a basic shape:

1. Create a [polygon](https://docs.flux.ai/flux/tutorials/working-with-polygons)
2. Select the polygon and find the **Inspect** menu on the top right.
3. Under **Object-specific rules**:
    1. Click on **Edit -&gt; Add**
    2. Find and add the **Polygon Shape** rule.
    3. On the newly added rule, delete the existing data and type **rectangle** or **circle**
        1. Keep in mind that the polygon might have moved out of position.
        2. You can also use the size [rule](https://docs.flux.ai/flux/reference/pcb-rules) to modify the shape

## Position

Sets the location of an object. It measures from the center of the object relative to the parent.

**Example 1**: Suppose you want to shift the location of a component to the  right by 4 mm. Open up the layout rules and navigate to the _Position_ rule under the _Object Specific Rules_ section. The position is given by _X_ and _Y_ coordinates. Simply add 4 to the current _X_ position to shift it to the right by 4mm.

#### **Clamping Related Rules**

**Shape Start X, Y:** sets the start location of a rectangle.

**Shape End X, Y:** sets the end location of a rectangle. For example, when used in conjunction with the shape start rule on a silk rectangle, the rectangle will span from (Xstart, Ystart,) to (Xend, Yend)

#### **Specific Related Rules**

- **Position X**: Sets the location of an object along the X axis. It measures from the center of the object relative to the parent.
- **Position Y**: Sets the location of an object along the Y axis. It measures from the center of the object relative to the parent.
- **Position Z**: Sets the location of an object along the Z axis. It measures from the center of the object relative to the parent.

## Preferred Trace Widths

Defines a set of widths which will show up in the Context Menu for easy access. The keyboard shortcut W will cycle through the set.

**Example 1:** Suppose you know you will be alternating between routing power traces and data traces. Add the _Preferred Trace Width_ Rule to the _Object-specific Rules_ of the _Nets_ object located in the _Objects_ panel. Then, in the entry box input the desired widths of these two types of traces, (150um and 500um for example). When routing, press _w_ to easily alternate between these trace widths.

## Rotation

Rotates the object. It measures relative to the center of the object relative to the parent.

**Example 1:** Suppose you want to rotate a component by 90 degrees in the plane. You can use the hotkeys to easily rotate it or add a _Rotation_ rule and specify the desired rotation about each axis. On the grid, a rotation of a component by 90 degrees corresponds to an inputted value of _0 0 90_, where each value is a rotation about the X, Y, and Z, axes. In this case we just want rotation about the Z axis.

#### **Specific Related Rules**

- **Rotation X:** Rotates the object along the X axis. It measures relative to the center of the object relative to the parent.
- **Rotation Y:** Rotates the object along the Y axis. It measures relative to the center of the object relative to the parent.
- **Rotation Z**: Rotates the object along the Z axis. It measures relative to the center of the object relative to the parent.

## Scale

Defines the scaling factor for the 3D model.

**Example 1:** Suppose you’d like to increase the size of a pad to make it large enough to be probed as a testpoint. Simply add a _Scale_ rule and modify the value for the desired size. In the case that you’d only like to increase the width, create a _Scale X_ rule and set this value. You can alternatively input 3 numbers into the _Scale_ rule separated by a linebreak with each corresponding to the _X, Y,_ and _Z_ values of the scale.

**Example 2:** Consider applying the _scale_ rule to silkscreen that is driven by an _.svg_ asset such as a logo. Using this rule will allow for proportionally changing the size avoiding any crooked or skewed effects.

#### **Specific Related Rules**

- **Scale X**: Defines the scaling factor for the 3D model along the X axis.
- **Scale Y**: Defines the scaling factor for the 3D model along the X axis.
- **Scale Z**: Defines the scaling factor for the 3D model along the X axis.

## Show Model Edges

Highlights the edges of selected 3D model with a black line. An edge is where two faces of the 3D model meet.

**Example:** Select any component with a 3D model in your object tree. Add a show model edges rule to it and open up the 3D view section from the bottom right of the pcb canvas. Turn on or off this rule to see the 3D edges where two faces meet.

## Silk Color

Defines the color of the silkscreen used during production. Preview this in 3D on PCB Mode.

**Example:** Suppose you’d like to change the silk color in the preview from the default white to yellow. Simply add a Silk Color rule in the Layout section and select yellow from the dropdown. Other colors include white, red, blue, black, yellow, and purple.

## Solder Mask Expansion

Allows the edge of the solder mask to expand beyond or contract within the edge of a pad or via. A positive value will expand the edge, a negative value will contract the edge, and a value of 0 will match the edge to the pad or via.

**Example:** Suppose you’d like a via to act as a test point and be able to be probed for testing. For this reason, you would not want the solder mask on top of it. Simply add a solder mask expansion rule to the via, and input a positive value. This will ensure that solder mask will not be applied onto this via.

#### Specific Related Rules

- **Solder Mask Expansion Top**:  Allows the edge of the solder mask - on the Top layer only - to expand beyond or contract within the edge of a pad or via. A positive value will expand the edge, a negative value will contract the edge, and a value of 0 will match the edge to the pad or via.
- **Solder Mask Expansion Bottom**: Allows the edge of the solder mask - on the Bottom layer only - to expand beyond or contract within the edge of a pad or via. A positive value will expand the edge, a negative value will contract the edge, and a value of 0 will match the edge to the pad or via.
- **Solder Mask Expansion From Hole Edge**: Allows the edge of the solder mask to expand beyond or contract within the edge of a drill hole. A positive value will expand the edge, a negative value will reduce the edge, and a value of 0 will match the edge to the drill hole.

## Solder Paste Mask Expansion

Allows the edge of the solder paste mask to expand beyond or contract within the edge of a pad or via. A positive value will expand the edge, a negative value will contract the edge, and a value of 0 will match the edge to the pad or via.

**Example:** Suppose you have created a pad to act as a testpoint, but do not want any solder paste applied when using a stencil. Add a Solder Paste Mask Expansion rule to the via with a negative value to ensure that a cutout is not generated for the solder paste stencil.

## Stackup

Defines the layer stackup for a Layout. Offers a number of standard defaults.

**Example:** Suppose you are designing a 10 layer board. Add a stackup rule to the layout section to set the number of layers.

If you are planning on working with a specific manufacturer such as  PCBWay, AISLER, or JLC, select the associated option from the dropdown to easily set up your board.

## Stroke Length

Sets the length of silk objects - lines, circles, and rectangles.

**Example:** In order to change the length of the dashes in a silk object such as a rectangle for a potential design, set this value.

## Stroke Spacing

Defines the spacing for dashed-style silk elements.

**Example**: In order to change the length of the spaces between the dashes in a silk object such as a rectangle for a potential design, set this value.

## Stroke Style

Sets the style of silk objects - lines, circles, and rectangles, such as solid or dashed.

**Example:** To create a circle with the perimeter dashed, add a silk object circle and give it this property. From the dropdown change the stroke style from solid to dashed.

## Stroke Width

Sets the width of silk objects - lines, circles, and rectangles.

**Example:** In order to change the width of the dashes in a silk object such as a rectangle for a potential design, set this value.

#### Related Clamping Rules

**Stroke Width Minimum**: Prevents the width of silk objects - lines, circles, and rectangles from being smaller than this value.

**Stroke Width Maximum**: Prevents the width of silk objects - lines, circles, and rectangles from being larger than this value.

## Text Align

Sets the alignment of the type displayed by a text object. Measures relative to the center of the text object.

**Example 1**: Suppose you’d like to write your organization’s name and revision number as silk screen text and ensure that it is perfectly centered in the middle of your board. Assuming your board shape is centered about 0, the position of the text should be 0 as well. If your board has a corner at 0, then set the text’s position to half the width and length. Then add a _Text Align_ rule with a value set to _center_. Through this method, regardless of the length of your text, it will always be centered about the center of the board.

## Thermal Relief

Defines how a pad connects to a [copper fill](https://docs.flux.ai/flux/reference/reference-ground-fills). _The default value is direct connect_.

The Thermal Relief rule can be configured with one of two options:

- **Relief Connect:** places an air gap between the pad and the fill and connects them with conductors.
- **Direct Connect** removes the air gap, allowing the pad and the fill to be fully in contact.

**Example:** In the case you are using a component that you expect to produce a lot of heat, consider inserting thermal relief pads. See the image below:

![P1 (left) has "Relief connect" configured, while P2 (right) has "Direct Connect"](https://uploads.developerhub.io/prod/86Yw/9m45gfk02rs6rhtwqg8g7y5jiu1iht1gj651u3l91rwfioplffs8zoi7oyqkz71g.png)

### Related Rules

#### Thermal Relief Conductors

Defines how many conductors are used for thermal relief. _The default value is 4 and can be configured with either 4 or 2 conductors._

**Example:** P1 (left) has been configured with 4 conductors, while P2 (right) has been configured with 2.

![](https://uploads.developerhub.io/prod/86Yw/1b43kzqcq4s3b9bufe0etczs1lexdjni12x5yijin53kxtxofu1tlvhih78urm71.png)

#### Thermal Relief Conductor Width

Defines the width of the conductors used for thermal relief.

**Example:** P1 (left) has been configured with 0.5mm width, while P2 (right) has been configured with 1mm width.

![](https://uploads.developerhub.io/prod/86Yw/phmw94e639236z6xe8uat7zk2esf108c2intqnvm4gilxqis9yjyqw3auesduvka.png)

#### Thermal Relief Conductor Angle

Defines the angle of the conductors used for thermal relief. _The default value is 90deg, and can be configured with either 90deg or 45deg conductors._

**Example:** P1 (left) has been configured with 90deg conductors, while P2 (right) has been configured with 45deg conductors.

![](https://uploads.developerhub.io/prod/86Yw/89aydowj5cyfjfcbqd6t0bbmb0vxjd2uvidgm4cyh7bhfgzh1jgn6v0znrfz0o86.png)

## Trace Shape

Defines the shape of a trace, either straight or curved (arc).

**Example:** Oftentimes for high-speed RF applications, it’s recommended to avoid sharp bends in traces. To create  arced traces for carrying data with optimal signal integrity, add a trace shape rule set to curved.

> This feature is unavailable

## Trace Width

Sets the width of traces in this object.

**Example:** Suppose you want to increase the width of a set of traces as you expect it to supply power with a larger current. In the object tree, find the related power net(s). Simply add a _Trace Width_ rule to each net, and set it to the desired width appropriate for the expected current. All traces that are part of the net with the added rule should will automatically then have their width set (unless overridden locally by another object-specific _trace width_ rule).

#### Clamping Related Rules

- **Trace Width Minimum**: Prevents the size of traces in this object from being smaller than this value.
- **Trace Width Maximum**: Prevents the size of traces in this object from being larger than this value.

## Via Type

Defines the type of a via. A through hole via is a plated drill hole with annular rings on every layer. A blind or buried via is a plated drill hole from a specific layer to another with annular rings on those layers. A micro-via is a conical hole bored with a laser from one layer to an adjacent layer.

**Example 1**: Suppose you are designing a high-speed 6-layer board. To create a connection from a component on the top layer to a component on the bottom layer without disturbing any of the internal signal, power, or ground layers, create a via as usual. Then, make sure to add a via type rule with blind or buried selected from the dropdown to ensure it does not short any of the internal layers.

## Z Axis is Up

Changes the up axis for 3D models.

**Example:** There may be some cases that when importing models from a different tool, the Z-axis may be oriented in a different direction, resulting in the model being on its side. To correct this, simply select the model in the object tree, and add a Z Axis is Up rule to easily reorient the 3D model.