# Source: https://developers.webflow.com/flowkit/v1.0.0/components/buttons.mdx

***

title: Buttons
slug: components/buttons
description: >-
Buttons are reusable components used to trigger actions or link to other
pages.
hidden: null
'og:title': Flowkit - Buttons
'og:description': >-
Buttons are reusable components used to trigger actions or link to other
pages.
------

## Class Naming

Buttons are reusable components used to trigger actions or link to other pages. They follow a consistent class structure for color type, size, and placement.

The class naming convention is:

<span class="sg-selector sg-class">
  Button
</span>

<span class="sg-selector sg-class">
   

  `Type Modifier`

   Button
</span>

<span class="sg-selector sg-class">
  `Size Modifer`

   Button
</span>

<span class="sg-selector sg-class">
  `Surface Modifier`

   Button
</span>

For example:

<span class="sg-selector sg-class">
  Button
</span>

<span class="sg-selector sg-class">
  Secondary Button
</span>

<span class="sg-selector sg-class">
  Primary On Accent Button
</span>

These modifiers adjust button styling for contrast and visual clarity when buttons are placed over colored or dark backgrounds.

**Size Modifiers**

* <span class="sg-selector sg-class">
    Small Button
  </span>
* <span class="sg-selector sg-class">
    Large Button
  </span>
* <span class="sg-selector sg-class">
    Secondary Small Button
  </span>

**Type Modifiers**

* <span class="sg-selector sg-class">
    Secondary Button
  </span>

**Surface Modifiers: On Accent**

* <span class="sg-selector sg-class">
    Primary Button On Accent Button
  </span>
* <span class="sg-selector sg-class">
    Secondary Button On Accent
  </span>
* <span class="sg-selector sg-class">
    Primary Button On Accent Secondary
  </span>
* <span class="sg-selector sg-class">
    Secondary Button On Accent Secondary
  </span>
* <span class="sg-selector sg-class">
    Primary Button On Accent Tertiary
  </span>
* <span class="sg-selector sg-class">
    Secondary Button On Accent Tertiary
  </span>

**Surface Modifiers: On Inverse**

* <span class="sg-selector sg-class">
    Primary Button On Inverse
  </span>
* <span class="sg-selector sg-class">
    Secondary Button On Inverse
  </span>

## Button Group

Buttons should be wrapped in a parent element with the class  <span class="sg-selector sg-class">Button Group</span> to maintain vertical spacing and horizontal gaps between buttons. This helps enforce consistent layout and rhythm across UI elements.

You can further modify alignment and layout behavior using combo classes:

| Class                                                      | Description                                   |
| ---------------------------------------------------------- | --------------------------------------------- |
| <span class="sg-selector sg-class">Align Left</span>       | Aligns buttons to the left (default)          |
| <span class="sg-selector sg-class">Align Center</span>     | Aligns buttons to the center                  |
| <span class="sg-selector sg-class">Align Right</span>      | Aligns buttons to the right                   |
| <span class="sg-selector sg-class">Vertical Stretch</span> | Stretches buttons to fill the container width |

***

## Text Button

Text Buttons are lightweight, inline-style buttons often used in navigation patterns, CTAs, or subtle interactions. They follow the same structure as standard buttons with color, size, and on-surface placement variations.

The base class is <span class="sg-selector sg-class">Text Button</span>

**Size Modifiers:**

* <span class="sg-selector sg-class">
    Small Text Button
  </span>

**Type Modifiers:**

* <span class="sg-selector sg-class">
    Secondary Text Button
  </span>

**Surface Modifiers:**

These combinations allow for subtle yet clear interactions across all background contexts.

* <span class="sg-selector sg-class">
    Text Button On Inverse
  </span>
* <span class="sg-selector sg-class">
    Text Button On Accent Primary
  </span>
* <span class="sg-selector sg-class">
    Text Button On Accent Secondary
  </span>
* <span class="sg-selector sg-class">
    Text Button On Accent Tertiary
  </span>

***

## Text Link

Text Links resemble hyperlinks and are meant for in-line use. They follow the same class structure logic as buttons and text buttons.

The base class is <span class="sg-selector sg-class">Text Link</span>

**Size Modifiers:**

* <span class="sg-selector sg-class">
    Small Text Link
  </span>

**Type Modifiers:**

* <span class="sg-selector sg-class">
    Secondary Text Link
  </span>

**Surface Modifiers:**

Text Links work well inside body copy, feature sections, or anywhere link-level interactions are required.

* <span class="sg-selector sg-class">
    Text Link On Inverse
  </span>
* <span class="sg-selector sg-class">
    Text Link On Accent Primary
  </span>
* <span class="sg-selector sg-class">
    Text Link On Accent Secondary
  </span>
* <span class="sg-selector sg-class">
    Text Link On Accent Tertiary
  </span>
