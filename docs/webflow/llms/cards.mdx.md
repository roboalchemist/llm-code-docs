# Source: https://developers.webflow.com/flowkit/components/cards.mdx

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

Cards are layout containers used to group and display content like text, images, and interactive elements. They are styled using the base class <span class="sg-selector sg-class">card</span> for standard cards and <span class="sg-selector sg-class">card-link</span> for interactive cards.

These classes can be extended using modifiers for different styles, backgrounds, and layouts.

## Surface Modifiers

Use these modifiers (combo classes) to adapt the card appearance based on the background context.

Naming convention:
<span class="sg-selector sg-class">card</span> <span class="sg-selector sg-class">on-`Surface`</span> and <span class="sg-selector sg-class">card-link</span> <span class="sg-selector sg-class">on-`Surface`</span>, where card surface can be `primary`, `secondary`, `inverse`, `accent-primary`, `accent-secondary`, `accent-tertiary`

Example:

* <span class="sg-selector sg-class">
    card
  </span>
  <span class="sg-selector sg-class">
    on-accent-primary
  </span>
* <span class="sg-selector sg-class">
    card-link
  </span>
  <span class="sg-selector sg-class">
    on-inverse
  </span>

## Card Elements

These modifiers allow additional control over spacing and card behavior across responsive layouts.

| Class                                                                                                | Description                                                              |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| <span class="sg-selector sg-class">card\_body</span>                                                 | Default card padding.                                                    |
| <span class="sg-selector sg-class">card\_body\_small</span>                                          | Small card padding.                                                      |
| <span class="sg-selector sg-class">card</span> <span class="sg-selector sg-class">is-featured</span> | Makes the card stand out from others. Useful for featured pricing cards. |
