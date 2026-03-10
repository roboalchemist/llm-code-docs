# Source: https://developers.webflow.com/flowkit/v1.0.0/components/slider.mdx

***

title: Slider
slug: components/slider
description: >-
Sliders are interactive components that allow users to select a value from a
range.
hidden: null
'og:title': Flowkit - Slider
'og:description': >-
Sliders are interactive components that allow users to select a value from a
range.
------

## Class Naming

| Class                                                  | Description                                                |
| ------------------------------------------------------ | ---------------------------------------------------------- |
| <span class="sg-selector sg-class">Slider</span>       | The main wrapper element for the slider                    |
| <span class="sg-selector sg-class">Slider Mask</span>  | A container that clips and holds the visible slide content |
| <span class="sg-selector sg-class">Slider Arrow</span> | Navigation button used to go to the next/previous slide    |

## Navigation

Sliders use arrows for navigation. These arrows are styled using a base class, and surface modifiers can be added to adapt to different backgrounds.

The base class is <span class="sg-selector sg-class">Slider Arrow</span>.
This can be extended with directional modifiers for navigation:

* <span class="sg-selector sg-class">
    Slider Arrow
  </span>
  <span class="sg-selector sg-class">
    Left
  </span>
* <span class="sg-selector sg-class">
    Slider Arrow
  </span>
  <span class="sg-selector sg-class">
    Right
  </span>

## Surface Modifiers

Use these to adapt the slider arrows to dark backgrounds.

<span class="sg-selector sg-class">
  Slider Arrow
</span>

<span class="sg-selector sg-class">
  Inverse Slider Arrow
</span>
