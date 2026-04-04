# Source: https://developers.webflow.com/flowkit/structure/flex.mdx

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

Class <span class="sg-selector sg-class">flex\_horizontal</span> and <span class="sg-selector sg-class">flex\_vertical</span> define the element as a flex layout container in either row or column direction.

***

## Flex Spacing

Spacing between children is controlled with gap modifiers: <span class="sg-selector sg-class">flex\_`direction`</span> <span class="sg-selector sg-class">gap-`size`</span>

Size options: `xsmall`, `small`, `medium`, `large`, `xlarge`, `xxlarge`

***

## Flex Alignment

Use alignment combo-classes to control positioning of children inside a flex layout.
Alignment can be horizontal (`X`) or vertical (`Y`) depending on the direction of the parent container.

Common examples:

* <span class="sg-selector sg-class">
    flex_horizontal
  </span>
  <span class="sg-selector sg-class">
    is-x-center
  </span>
* <span class="sg-selector sg-class">
    flex_horizontal
  </span>
  <span class="sg-selector sg-class">
    is-x-right
  </span>
* <span class="sg-selector sg-class">
    flex_horizontal
  </span>
  <span class="sg-selector sg-class">
    is-y-bottom
  </span>
* <span class="sg-selector sg-class">
    flex_vertical
  </span>
  <span class="sg-selector sg-class">
    is-x-center
  </span>
* <span class="sg-selector sg-class">
    flex_vertical
  </span>
  <span class="sg-selector sg-class">
    is-y-bottom
  </span>

**Align Horizontal Left**
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">is-x-left</span>

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
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">is-x-center</span>

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
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">is-x-right</span>

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
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">is-x-space-between</span>

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
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">flex\_wrap</span>

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
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">is-y-top</span>

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
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">is-y-center</span>

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
<span class="sg-selector sg-class">flex\_horizontal</span> <span class="sg-selector sg-class">is-y-bottom</span>

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
<span class="sg-selector sg-class">flex\_vertical</span> <span class="sg-selector sg-class">is-x-left</span>

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
<span class="sg-selector sg-class">flex\_vertical</span> <span class="sg-selector sg-class">is-x-center</span>

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
<span class="sg-selector sg-class">flex\_vertical</span> <span class="sg-selector sg-class">is-x-right</span>

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
<span class="sg-selector sg-class">flex\_vertical</span> <span class="sg-selector sg-class">is-y-bottom</span>

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
<span class="sg-selector sg-class">flex\_vertical</span> <span class="sg-selector sg-class">is-y-center</span>

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
<span class="sg-selector sg-class">flex\_vertical</span> <span class="sg-selector sg-class">is-x-stretch</span>

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
<span class="sg-selector sg-class">flex\_vertical</span> <span class="sg-selector sg-class">is-space-between</span>

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

| Behavior  | Combo Class                                                      |
| --------- | ---------------------------------------------------------------- |
| No Shrink | <span class="sg-selector sg-class">flex-child\_no\_shrink</span> |
| Expand    | <span class="sg-selector sg-class">flex-child\_expand</span>     |
| Shrink    | <span class="sg-selector sg-class">flex-child\_shrink</span>     |

Useful for allowing or preventing children from stretching, shrinking, or expanding based on available space.

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Element with <span class="sg-selector sg-class">flex\_child\_no\_shrink</span> applied
    </div>

    <div class="sg-element">
      Element with <span class="sg-selector sg-class">width\_100percent</span> applied
    </div>
  </div>
</div>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Element with <span class="sg-selector sg-class">flex\_child\_expand</span> applied
    </div>

    <div class="sg-element">
      Content
    </div>
  </div>
</div>

<div class="sg-wrapper">
  <div class="sg-preview">
    <div class="sg-element">
      Element with <span class="sg-selector sg-class">width\_100percent</span> applied
    </div>

    <div class="sg-element">
      Element with <span class="sg-selector sg-class">flex\_child\_shrink</span> applied
    </div>
  </div>
</div>

***

## Responsive Modifiers

Available responsive combo classes

| Combo Class                                                 | Description                         |
| ----------------------------------------------------------- | ----------------------------------- |
| <span class="sg-selector sg-class">tablet-x-center</span>   | Center horizontally on tablet       |
| <span class="sg-selector sg-class">tablet-y-center</span>   | Center vertically on tablet         |
| <span class="sg-selector sg-class">mobile-l-x-center</span> | Center horizontally on mobile large |
| <span class="sg-selector sg-class">mobile-l-y-center</span> | Center vertically on mobile large   |
| <span class="sg-selector sg-class">mobile-x-center</span>   | Center horizontally on mobile       |
| <span class="sg-selector sg-class">mobile-y-center</span>   | Center vertically on mobile         |
