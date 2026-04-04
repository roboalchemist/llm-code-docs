# Source: https://developers.webflow.com/flowkit/components/buttons.mdx

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
  button
</span>

<span class="sg-selector sg-class">
  is-secondary
</span>

<span class="sg-selector sg-class">
  is-small
</span>

<span class="sg-selector sg-class">
  on-accent-primary
</span>

For example:

<span class="sg-selector sg-class">
  button
</span>

<span class="sg-selector sg-class">
  is-secondary
</span>

<span class="sg-selector sg-class">
  on-accent-primary
</span>

These modifiers adjust button styling for contrast and visual clarity when buttons are placed over colored or dark backgrounds.

**Size Modifiers**

* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    is-small
  </span>
* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    is-large
  </span>

**Type Modifiers**

* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    is-secondary
  </span>

**Surface Modifiers: On Accent**

* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    on-accent-primary
  </span>
* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    is-secondary
  </span>
  <span class="sg-selector sg-class">
    on-accent-primary
  </span>
* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    on-accent-secondary
  </span>
* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    is-secondary
  </span>
  <span class="sg-selector sg-class">
    on-accent-secondary
  </span>
* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    on-accent-tertiary
  </span>
* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    is-secondary
  </span>
  <span class="sg-selector sg-class">
    on-accent-tertiary
  </span>

**Surface Modifiers: On Inverse**

* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    on-inverse
  </span>
* <span class="sg-selector sg-class">
    button
  </span>
  <span class="sg-selector sg-class">
    is-secondary
  </span>
  <span class="sg-selector sg-class">
    on-inverse
  </span>

## Button Group

Buttons should be wrapped in a parent element with the class  <span class="sg-selector sg-class">button-group</span> to maintain vertical spacing and horizontal gaps between buttons. This helps enforce consistent layout and rhythm across UI elements.

You can further modify alignment and layout behavior using combo classes:

| Class                                                                                                                | Description                                   |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| <span class="sg-selector sg-class">button-group</span>                                                               | Aligns buttons to the left (default)          |
| <span class="sg-selector sg-class">button-group</span> <span class="sg-selector sg-class">is-align-center</span>     | Aligns buttons to the center                  |
| <span class="sg-selector sg-class">button-group</span> <span class="sg-selector sg-class">is-align-right</span>      | Aligns buttons to the right                   |
| <span class="sg-selector sg-class">button-group</span> <span class="sg-selector sg-class">is-vertical-stretch</span> | Stretches buttons to fill the container width |

***

## Text Button

Text Buttons are lightweight, inline-style buttons often used in navigation patterns, CTAs, or subtle interactions. They follow the same structure as standard buttons with color, size, and on-surface placement variations.

The base class is <span class="sg-selector sg-class">text-button</span>

**Size Modifiers:**

* <span class="sg-selector sg-class">
    text-button
  </span>
  <span class="sg-selector sg-class">
    is-small
  </span>

**Type Modifiers:**

* <span class="sg-selector sg-class">
    text-button
  </span>
  <span class="sg-selector sg-class">
    is-secondary
  </span>

**Surface Modifiers:**

These combinations allow for subtle yet clear interactions across all background contexts.

* <span class="sg-selector sg-class">
    text-button
  </span>
  <span class="sg-selector sg-class">
    on-inverse
  </span>
* <span class="sg-selector sg-class">
    text-button
  </span>
  <span class="sg-selector sg-class">
    on-accent-primary
  </span>
* <span class="sg-selector sg-class">
    text-button
  </span>
  <span class="sg-selector sg-class">
    on-accent-secondary
  </span>
* <span class="sg-selector sg-class">
    text-button
  </span>
  <span class="sg-selector sg-class">
    on-accent-tertiary
  </span>

***

## Text Link

Text Links resemble hyperlinks and are meant for in-line use. They follow the same class structure logic as buttons and text buttons.

The base class is <span class="sg-selector sg-class">text-link</span>

**Size Modifiers:**

* <span class="sg-selector sg-class">
    text-link
  </span>
  <span class="sg-selector sg-class">
    is-small
  </span>

**Type Modifiers:**

* <span class="sg-selector sg-class">
    text-link
  </span>
  <span class="sg-selector sg-class">
    is-secondary
  </span>

**Surface Modifiers:**

Text Links work well inside body copy, feature sections, or anywhere link-level interactions are required.

* <span class="sg-selector sg-class">
    text-link
  </span>
  <span class="sg-selector sg-class">
    on-inverse
  </span>
* <span class="sg-selector sg-class">
    text-link
  </span>
  <span class="sg-selector sg-class">
    on-accent-primary
  </span>
* <span class="sg-selector sg-class">
    text-link
  </span>
  <span class="sg-selector sg-class">
    on-accent-secondary
  </span>
* <span class="sg-selector sg-class">
    text-link
  </span>
  <span class="sg-selector sg-class">
    on-accent-tertiary
  </span>
