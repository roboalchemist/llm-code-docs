# Source: https://developers.webflow.com/flowkit/v1.0.0/variables/border.mdx

***

title: Border
slug: variables/border
description: Border variables and how they are used in the Webflow CSS Framework.
hidden: null
'og:title': Flowkit - Border
'og:description': Border variables and how they are used in the Webflow CSS Framework.
--------------------------------------------------------------------------------------

Border variables control visual boundaries between components like buttons, cards, input fields, and other UI elements. These are divided into:

* **Border Color** — Defines the visible stroke color.
* **Radius** — Defines the border corner roundness (border-radius).

These values can be applied using variables or utility classes.
They may vary between projects depending on style preferences.

***

## Border Color

Border color variables follow a naming pattern based on surface context or visual intent.

* <span class="sg-selector sg-var">
    Border Primary
  </span>
* <span class="sg-selector sg-var">
    Border Secondary
  </span>
* <span class="sg-selector sg-var">
    Border Inverse Primary
  </span>
* <span class="sg-selector sg-var">
    Border Inverse Secondary
  </span>
* <span class="sg-selector sg-var">
    Border Accent
  </span>

These reference foundational colors like Neutral or Accent and may include opacity (e.g. `Neutral Inverse A50`). The exact mapping is managed in the Variables panel.

Border color variables are applied to style border or box shadow style of elements. For example dividers and input fields are using border styles. Buttons and cards components are using box shadow style.

***

## Border Radius

Radius variables define how rounded the corners of elements should be. These values are used consistently across cards, buttons, input fields, etc.

Radius names use t-shirt sizing:

* <span class="sg-selector sg-var">
    SM Radius
  </span>
* <span class="sg-selector sg-var">
    MD Radius
  </span>
* <span class="sg-selector sg-var">
    LG Radius
  </span>
* <span class="sg-selector sg-var">
    XL Radius
  </span>
* <span class="sg-selector sg-var">
    Round
  </span>

***

<Note title="Utility Classes">
  To apply or override border radius styles consistently across elements, use the available utility classes. You can find the full list and usage examples in the [Border Radius Utilities](/flowkit/reference/utilities#border-radius) section.
</Note>
