# Source: https://developers.webflow.com/flowkit/components/images.mdx

***

title: Images
slug: components/images
description: >-
Images are styled using reusable classes that control fitting behavior and
aspect ratio.
hidden: null
'og:title': Flowkit - Images
'og:description': >-
Images are styled using reusable classes that control fitting behavior and
aspect ratio.
-------------

## Class Naming

Images are styled using reusable classes that control fitting behavior and aspect ratio. They also apply consistent styling like border-radius using a design token.

**Image Fit**

Use the base class <span class="sg-selector sg-class">image</span> or <span class="sg-selector sg-class">image\_cover</span> to define the image element.

**Radius**

All images — including elements with the tag <span class="sg-selector sg-tag">Image</span>, or using the classes <span class="sg-selector sg-class">image</span> and <span class="sg-selector sg-class">image\_cover</span> — have rounded corners applied through the variable <span class="sg-selector sg-var">Image Radius</span>.

To override this and make the corners square, use the combo class <span class="sg-selector sg-class">radius\_all-0</span>

### Aspect Ratio

Aspect ratio combo classes must be applied on top of the <span class="sg-selector sg-class">image\_cover</span> class to take effect.

Why? Because the image needs to stretch to fill the area defined by the ratio box — if only the ratio is set without forcing coverage, the image may not respect the ratio area.

Available combo classes:

* <span class="sg-selector sg-class">
    ratio_1x1
  </span>
* <span class="sg-selector sg-class">
    ratio_16x9
  </span>
* <span class="sg-selector sg-class">
    ratio_3x2
  </span>
* <span class="sg-selector sg-class">
    ratio_4x3
  </span>
* <span class="sg-selector sg-class">
    ratio_2x2.5
  </span>
* <span class="sg-selector sg-class">
    ratio_2x3
  </span>

Exasmple:

<span class="sg-selector sg-class">
  image_cover
</span>

<span class="sg-selector sg-class">
  ratio_2x3
</span>

### Responsive Modifiers

You can use responsive combo classes to change aspect ratio behavior on different breakpoints. For example, you may want to simplify layouts on smaller screens or reset custom ratios back to `auto`.

**Tablet**

* <span class="sg-selector sg-class">
    ratio_3x2_tablet
  </span>
* <span class="sg-selector sg-class">
    ratio_1x1_tablet
  </span>

**Mobile Landscape**

* <span class="sg-selector sg-class">
    ratio_auto_mobile-l
  </span>

These modifiers are added in combination with the base <span class="sg-selector sg-class">image\_cover</span> class and optionally other aspect combo classes.

***

## Icons

Icons are scalable, visual indicators used throughout the UI. They rely on a base class for consistent sizing and alignment, and support modifiers for scale and contextual styling.

The base class is <span class="sg-selector sg-class">icon</span>

**Size Modifiers**

These adjust the scale of the icon element relative to the surrounding layout.

* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    is-xsmall
  </span>
* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    is-small
  </span>
* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    is-large
  </span>
* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    is-xlarge
  </span>

**Surface Modifiers**

Use these to ensure icons maintain clarity and contrast when placed on dark or colored backgrounds.

* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    on-inverse
  </span>
* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    on-accent-primary
  </span>
* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    on-accent-secondary
  </span>
* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    on-accent-tertiary
  </span>

**Enhancing Visibility with Icon Container**

You can wrap the icon with an additional background highlight using the combo class
<span class="sg-selector sg-class">icon</span> <span class="sg-selector sg-class">is-background</span>

This applies a soft tint using the icon's color, creating a subtle button-like effect that draws visual attention without overwhelming the interface.

This can be combined with any surface modifier. For example:

<span class="sg-selector sg-class">
  icon
</span>

<span class="sg-selector sg-class">
  on-accent-primary
</span>

<span class="sg-selector sg-class">
  is-background
</span>

***

## Avatars

Avatars are circular images used to visually represent a user, team, or content author. The base class defines the image as an avatar, and combo classes adjust the size.

The base class is <span class="sg-selector sg-class">avatar</span>

**Size Modifiers**

Use these modifiers to adjust the avatar size while keeping alignment and proportions consistent across the UI.

* <span class="sg-selector sg-class">
    avatar
  </span>
  <span class="sg-selector sg-class">
    is-small
  </span>
* <span class="sg-selector sg-class">
    avatar
  </span>
  <span class="sg-selector sg-class">
    is-large
  </span>
