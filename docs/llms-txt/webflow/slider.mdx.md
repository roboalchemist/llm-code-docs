# Source: https://developers.webflow.com/flowkit/components/slider.mdx

***

title: Slider
slug: components/slider
description: >-
Sliders are interactive components that allow users to select a value from a
range.
'og:title': Flowkit - Slider
'og:description': >-
Sliders are interactive components that allow users to select a value from a
range.
------

## Class Naming

| Class                                                   | Description                                                |
| ------------------------------------------------------- | ---------------------------------------------------------- |
| <span class="sg-selector sg-class">slider</span>        | The main wrapper element for the slider                    |
| <span class="sg-selector sg-class">slider\_mask</span>  | A container that clips and holds the visible slide content |
| <span class="sg-selector sg-class">slider\_arrow</span> | Navigation button used to go to the next/previous slide    |

## Navigation

Sliders use arrows for navigation. These arrows are styled using a base class, and surface modifiers can be added to adapt to different backgrounds.

The base class is <span class="sg-selector sg-class">slider\_arrow</span>.

### Directional Modifiers

This can be extended with directional modifiers for navigation:

* <span class="sg-selector sg-class">
    slider_arrow
  </span>
  <span class="sg-selector sg-class">
    is-previous
  </span>
* <span class="sg-selector sg-class">
    slider_arrow
  </span>
  <span class="sg-selector sg-class">
    is-next
  </span>

## Surface Modifiers

Use these to adapt the slider arrows to dark backgrounds.

<span class="sg-selector sg-class">
  slider_arrow
</span>

<span class="sg-selector sg-class">
  is-inverse
</span>
