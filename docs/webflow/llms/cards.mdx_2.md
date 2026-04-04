# Source: https://developers.webflow.com/flowkit/v1.0.0/components/cards.mdx

***

title: Cards
slug: components/cards
description: >-
Cards are layout containers used to group and display content like text,
images, and interactive elements.
hidden: null
'og:title': Flowkit - Cards
'og:description': >-
Cards are layout containers used to group and display content like text,
images, and interactive elements.
---------------------------------

## Class Naming

Cards are layout containers used to group and display content like text, images, and interactive elements. They are styled using the base class <span class="sg-selector sg-class">Card</span> for standard cards and <span class="sg-selector sg-class">Card Link</span> for interactive cards.

These classes can be extended using modifiers for different styles, backgrounds, and layouts.

## Surface Modifiers

Use these to adapt the card appearance based on the background context.

Naming convention for combo classes is:
<span class="sg-selector sg-class">Card On `Surface`</span> and <span class="sg-selector sg-class">Card Link On `Surface`</span>, where card surface can be `Primary`, `Secondary`, `Inverse`, `Accent Primary`, `Accent Secondary`, `Accent Tertiary`

Example:

* <span class="sg-selector sg-class">
    Card
  </span>
  <span class="sg-selector sg-class">
    Card On Accent Primary
  </span>
* <span class="sg-selector sg-class">
    Card Link
  </span>
  <span class="sg-selector sg-class">
    Card On Inverse
  </span>

## Card Elements

These modifiers allow additional control over spacing and card behavior across responsive layouts.

| Class                                                   | Description                                                                                           |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| <span class="sg-selector sg-class">Card Body</span>     | Default card padding applied through a variable <span class="sg-selector sg-var">Card Padding</span>. |
| <span class="sg-selector sg-class">Card Body SM</span>  | Small card padding.                                                                                   |
| <span class="sg-selector sg-class">Featured Card</span> | Makes the card stand out from others. Useful for featured pricing cards.                              |
