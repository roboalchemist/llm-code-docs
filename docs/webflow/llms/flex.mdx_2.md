# Source: https://developers.webflow.com/flowkit/v1.0.0/structure/flex.mdx

***

title: Flex Layout
slug: structure/flex
description: >-
Flexbox layout utilities for directional flow, spacing, and alignment in the
Webflow CSS Framework.
'og:title': Flowkit - Flex Layout
'og:description': >-
Flexbox layout utilities for directional flow, spacing, and alignment in the
Webflow CSS Framework.
----------------------

Flex layout utilities define how elements are laid out in one dimension (either horizontally or vertically).
Use direction, spacing, alignment, and child behavior modifiers to achieve flexible and consistent layouts.

***

## Flex Directions

Class <span class="sg-selector sg-class">Flex Horizontal</span> and <span class="sg-selector sg-class">Flex Vertical</span> define the element as a flex layout container in either row or column direction.

***

## Flex Spacing

Spacing between children is controlled with gap modifiers: <span class="sg-selector sg-class">Flex (Direction)</span> <span class="sg-selector sg-class">Flex Gap (X)</span>

| Label        | Combo Class Example                                                                                              |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| XX Small Gap | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Flex Gap XXS</span> |
| X Small Gap  | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Flex Gap XS</span>  |
| Small Gap    | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Flex Gap SM</span>  |
| Medium Gap   | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Flex Gap MD</span>  |
| Large Gap    | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Flex Gap LG</span>  |

***

## Flex Alignment

Use alignment combo-classes to control positioning of children inside a flex layout.
Alignment can be horizontal (`X`) or vertical (`Y`) depending on the direction of the parent container.

Common examples:

* <span class="sg-selector sg-class">
    Flex Horizontal
  </span>
  <span class="sg-selector sg-class">
    X Center
  </span>
* <span class="sg-selector sg-class">
    Flex Horizontal
  </span>
  <span class="sg-selector sg-class">
    X Right
  </span>
* <span class="sg-selector sg-class">
    Flex Horizontal
  </span>
  <span class="sg-selector sg-class">
    Y Bottom
  </span>
* <span class="sg-selector sg-class">
    Flex Vertical
  </span>
  <span class="sg-selector sg-class">
    X Center
  </span>
* <span class="sg-selector sg-class">
    Flex Vertical
  </span>
  <span class="sg-selector sg-class">
    Y Bottom
  </span>

**Align Horizontal Left**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">X Left</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Horizontal Center**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">X Center</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Horizontal Right**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">X Right</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Space Between**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">X Space Between</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Flex Wrap**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Flex Wrap</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Vertical Top**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Y Top</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Vertical Center**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Y Center</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Vertical Bottom**
<span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Y Bottom</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Horizontal Left**
<span class="sg-selector sg-class">Flex Vertical</span> <span class="sg-selector sg-class">X Left</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Horizontal Center**
<span class="sg-selector sg-class">Flex Vertical</span> <span class="sg-selector sg-class">X Center</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Horizontal Right**
<span class="sg-selector sg-class">Flex Vertical</span> <span class="sg-selector sg-class">X Right</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Vertical Bottom**
<span class="sg-selector sg-class">Flex Vertical</span> <span class="sg-selector sg-class">Y Bottom</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Align Vertical Center**
<span class="sg-selector sg-class">Flex Vertical</span> <span class="sg-selector sg-class">Y Center</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Expand Horizontally**
<span class="sg-selector sg-class">Flex Vertical</span> <span class="sg-selector sg-class">X Stretch</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

**Side by Side Vertically**
<span class="sg-selector sg-class">Flex Vertical</span> <span class="sg-selector sg-class">Space Between</span>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Content
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

***

## Flex Child Modifiers

These combo-classes define how children inside a flex container behave:

| Behavior  | Combo Class                                                    |
| --------- | -------------------------------------------------------------- |
| No Shrink | <span class="sg-selector sg-class">Flex Child No Shrink</span> |
| Expand    | <span class="sg-selector sg-class">Flex Child Expand</span>    |
| Shrink    | <span class="sg-selector sg-class">Flex Child Shrink</span>    |

Useful for allowing or preventing children from stretching, shrinking, or expanding based on available space.

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Element with `Flex Child No Shrink` applied
    </div>

    <div class="sg-element">
      Element with `[Utility] Width 100%` applied
    </div>
  </div>
</div>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Element with `Flex Child Expand` applied
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Element with `[Utility] Width 100%` applied
    </div>

    <div class="sg-element">
      Element with `Flex Child Shrink` applied
    </div>
  </div>
</div>

***

## Responsive Modifiers

On Tablet resolution (991px and below), <span class="sg-selector sg-class">Flex Horizontal</span> automatically changes to vertical layout by default.

To override this behavior, use responsive modifier combo classes, such as:

<span class="sg-selector sg-class">
  Tablet Flex Horizontal
</span>

<span class="sg-selector sg-class">
  Mobile Landscape Flex Horizontal
</span>

These allow you to force direction across breakpoints.

### Tablet

| Description                          | Combo Classes                                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Horizontal direction                 | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Tablet Flex Horizontal</span>                                                         |
| Vertical direction                   | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Tablet Flex Vertical</span>                                                           |
| Vertical direction, center content X | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Tablet Flex Vertical</span> <span class="sg-selector sg-class">Tablet X Center</span> |
| Vertical direction, center content Y | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Tablet Flex Vertical</span> <span class="sg-selector sg-class">Tablet Y Center</span> |

### Mobile Landscape

| Description          | Combo Classes                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Horizontal direction | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Mobile Landscape Flex Horizontal</span> |
| Vertical direction   | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Mobile Landscape Flex Vertical</span>   |

### Mobile Portrait

| Description          | Combo Classes                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Horizontal direction | <span class="sg-selector sg-class">Flex Horizontal</span> <span class="sg-selector sg-class">Mobile Landscape Flex Horizontal</span> |
| Vertical direction   | <span class="sg-selector sg-class">Mobile Landscape Flex Vertical</span>                                                             |
