# Source: https://developers.webflow.com/flowkit/v1.0.0/components/images.mdx

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

Use the base class <span class="sg-selector sg-class">Image</span> to define the image element.
Use the combo class <span class="sg-selector sg-class">Cover Image</span> to ensure the image covers its container fully.

**Radius**

All images — including elements with the tag <span class="sg-tag">Image</span>, or using the classes <span class="sg-selector sg-class">Image</span> and <span class="sg-selector sg-class">Cover Image</span> — have rounded corners applied through the variable <span class="sg-var">Image Radius</span>.

To override this and make the corners square, use the combo class <span class="sg-selector sg-class">\[Utility] Radius All 0</span>

### Aspect Ratio

Aspect ratio combo classes must be applied on top of the <span class="sg-selector sg-class">Cover Image</span> class to take effect.

Why? Because the image needs to stretch to fill the area defined by the ratio box — if only the ratio is set without forcing coverage, the image may not respect the ratio area.

Available combo classes:

* <span class="sg-selector sg-class">
    \[Utility] Aspect 1x1
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Aspect 16x9
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Aspect 3x2
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Aspect 4x3
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Aspect 2x2.5
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Aspect 2x3
  </span>

Exasmple:

<span class="sg-selector sg-class">
  Cover Image
</span>

<span class="sg-selector sg-class">
  \[Utility] Aspect 2x3
</span>

### Responsive Modifiers

You can use responsive combo classes to change aspect ratio behavior on different breakpoints. For example, you may want to simplify layouts on smaller screens or reset custom ratios back to `auto`.

**Tablet**

* <span class="sg-selector sg-class">
    \[Utility] Tablet Aspect 3x2
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Tablet Aspect 1x1
  </span>

**Mobile Landscape**

* <span class="sg-selector sg-class">
    \[Utility] Mobile Landscape Aspect Auto
  </span>

These modifiers are added in combination with the base <span class="sg-selector sg-class">Cover Image</span> class and optionally other aspect combo classes.

***

## Icons

Icons are scalable, visual indicators used throughout the UI. They rely on a base class for consistent sizing and alignment, and support modifiers for scale and contextual styling.

The base class is <span class="sg-selector sg-class">Icon</span>

**Size Modifiers**

These adjust the scale of the icon element relative to the surrounding layout.

* <span class="sg-selector sg-class">
    Icon Extra Small
  </span>
* <span class="sg-selector sg-class">
    Icon Small
  </span>
* <span class="sg-selector sg-class">
    Icon Large
  </span>
* <span class="sg-selector sg-class">
    Icon Extra Large
  </span>

**Surface Modifiers**

Use these to ensure icons maintain clarity and contrast when placed on dark or colored backgrounds.

* <span class="sg-selector sg-class">
    Icon On Inverse Icon
  </span>
* <span class="sg-selector sg-class">
    Icon On Accent Primary
  </span>
* <span class="sg-selector sg-class">
    Icon On Accent Secondary
  </span>
* <span class="sg-selector sg-class">
    Icon On Accent Tertiary
  </span>

**Enhancing Visibility with Icon Container**

You can wrap the icon with an additional background highlight using the combo class
<span class="sg-selector sg-class">Icon Container</span>

This applies a soft tint using the icon’s color, creating a subtle button-like effect that draws visual attention without overwhelming the interface.

This can be combined with any surface modifier. For example:

<span class="sg-selector sg-class">
  Icon
</span>

<span class="sg-selector sg-class">
  Icon On Accent Primary 
</span>

<span class="sg-selector sg-class">
   Icon Container
</span>

***

## Avatars

Avatars are circular images used to visually represent a user, team, or content author. The base class defines the image as an avatar, and combo classes adjust the size.

The base class is <span class="sg-selector sg-class">Avatar</span>

**Size Modifiers**

Use these modifiers to adjust the avatar size while keeping alignment and proportions consistent across the UI.

* <span class="sg-selector sg-class">
    Small Avatar
  </span>
* <span class="sg-selector sg-class">
    Large Avatar
  </span>
