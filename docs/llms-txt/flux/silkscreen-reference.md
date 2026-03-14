# Source: https://docs.flux.ai/reference/silkscreen-reference.md

# Silkscreen

Silkscreen elements are one of the most basic elements in Flux. It's a layer of ink traces used to identify components, test points, parts of the PCB, warning symbols, logos, marks, etc.

![](https://uploads.developerhub.io/prod/86Yw/p164on4ob9esqmrufai39tv0q9vn4czrcfsaqdy36f2ylhdehegxidtxd7g4d5wf.png)

## Overview

 In this section we'll cover:

- Adding silkscreen elements
    - Text
    - Silk Line
    - Silk Circle
    - Silk Rectangle

- Modifying existing silkscreen
- Creating custom silkscreen

## Adding Silkscreen

![](https://uploads.developerhub.io/prod/86Yw/kbtl3uq2fr2k2dmadmluypb9np368uesjpoldqdy7a6qrqitin8fnk930f6mguo6.png)

Silkscreen objects are ink traces used to identify test points, components, warning symbols, or any additional desired graphical element on your PCB

To add a silkscreen element:

- Left-click on the _Layout_ object in the objects tree to ensure it's selected
- Right-click &gt; Add &gt; Silk Line / Silk Circle / Silk Rectangle

A silk text is a particular kind of silkscreen that lets you add text to your PCB.

A **silk line** is a line that stretches between two specified points. You can use a [line path rule](https://docs.flux.ai/reference/layout-rules-types#line-path) for any desired curves.

A **silk circle** is a circle with a specified origin and diameter.

A **silk rectangle** stretches between two specified points.

The stroke length, spacing, style, width, and width of these three silk elements can all be modified using the [appropriate rules](https://docs.flux.ai/reference/layout-rules-types#stroke-length).

## Modifying Existing Silkscreen

The tutorial below covers how to customize or modify existing silkscreen elements of components in Flux. For example, repositioning or hiding silkscreen content of a component that you've imported from the library or another tools.



### Moving and Hiding Silkscreen

#### Example 1: Hiding the silkscreen element of capacitor.

1. First select the individual silkscreen element that you'd like to modify. Hovering over the component and left-clicking selects all of it. Instead, double-click to select the individual element within the component, _or_ find it in the object tree, _or_ hover and press the command key to select the element directly. 
2. Once you've selected the silkscreen element, move it from its default position. In doing so, Flux will automatically generate a new `position` selector-rule  with an `!important` flag. The only way to modify individual elements (silkscreen content, pad, etc.) within a component is by using the`!important` flag.
3. To hide the element once Flux has auto-generated a `position`rule with `!important` flag, add an _additional_ `enable`rule and set it to `false`. To force the element to be hidden, add `!important` to it as well.

![_Adding a component override rule allows you to make modifications with the !important flag._](https://uploads.developerhub.io/prod/86Yw/rggk7tmeup296ot96qfa1e14wxndhzq3t08yqqmo5hsroazpzrbcsliwvwb3sor4.png)

Through this process you can hide any element you desire. As the `position`rule is no longer necessary, feel free to delete it. If you only care to change the position of the silkscreen content, rather than hide it, skip step 3. 

### Modifying Silkscreen in Bulk

Through this process you can modify a group of elements, such as hiding all the silkscreen _VALUE_ elements of all components in a design. Rather than selecting them all, it's easier to do in bulk.

1. First, notice that all elements have the word `VALUE` in a designator. Therefore, add selector-based rule with selector criteria set to `[name*="VALUE"]`_._ This selects all the _value_ silkscreen elements in the design allowing you to add an applicable rule to them all.
2. Then, add an `enable`rule set to `false`and add the `!important` flag. This will hide all the _VALUE_ elements

For a more complex example, consider hiding all _VALUE_ elements of only resistors in the design.

1. Simply add a selector based rule with the following syntax: `*[PartType=Resistor]`[name*="VALUE"]`` .
2. Then, as above, add an `enable`rule set to `false`and add the `!important` flag. 

## Creating Custom Silkscreen

In creating a new part, you can add an ._svg_ as a symbol. For example, notice that all parts in the library have an _.svg_ for the symbol. You can use also add an _.svg_ file to your project to create custom graphics to your board through a silkscreen.



If you want to learn more about creating custom silkscreen shapes, we have a full [custom shapes tutorial.](https://docs.flux.ai/flux/tutorials/custom-pad-shapes)

Alternatively, feel free to use our community library to search for premade graphics! For example, you can simply add the Flux logo by finding it in the library search and dragging it in.