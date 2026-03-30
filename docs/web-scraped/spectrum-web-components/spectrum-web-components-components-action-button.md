# Source: https://opensource.adobe.com/spectrum-web-components/components/action-button/

Title: Action Button: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/action-button/

Markdown Content:
Action Button: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-action-button
================

 Deprecation Warning 

 The link API features (href, target, download, referrerpolicy, rel) in @spectrum-web-components/action-button are deprecated and will be removed in a future release. Use a native HTML anchor element with the spectrum-ActionButton class and @spectrum-web-components/styles/global-elements.css instead. 

NPM 1.11.2

View Storybook

Try it on Stackblitz

Overview API Changelog

Overview
--------

#Section titled Overview

An `<sp-action-button>` represents an action a user can take.

### Usage

#Section titled Usage

![Image 4: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/action-button?style=for-the-badge)![Image 5: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/action-button?style=for-the-badge)![Image 6: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/action-button
Import the side effectful registration of `<sp-action-button>` via:

import '@spectrum-web-components/action-button/sp-action-button.js';
When looking to leverage the `ActionButton` base class as a type and/or for extension purposes, do so via:

import { ActionButton } from '@spectrum-web-components/action-button';

### Anatomy

#Section titled Anatomy

<sp-action-button>Try me</sp-action-button>

#### Content

#Section titled Content

`<sp-action-button>` elements can be provided a visible label, a label and an icon, or just an icon.

An icon is provided by placing an icon element in the `icon` slot.

If the button is `icon-only`, a non-visible label can be provided via the `label` attribute on an `<sp-action-button>` or on an `<sp-icon*>` element child to appropriately fulfill the accessibility contract of the button.

Label only<sp-action-button variant="primary">Label only</sp-action-button>Icon + label<sp-action-button variant="primary">
  <sp-icon-help slot="icon"></sp-icon-help>
  Icon + Label
</sp-action-button>SVG Icon + label<sp-action-button variant="primary">
  <svg slot="icon" viewBox="0 0 36 36" focusable="false" aria-hidden="true" role="img" >
    <path d="M16 36a4.407 4.407 0 0 0 4-4h-8a4.407 4.407 0 0 0 4 4zm9.143-24.615c0-3.437-3.206-4.891-7.143-5.268V3a1.079 1.079 0 0 0-1.143-1h-1.714A1.079 1.079 0 0 0 14 3v3.117c-3.937.377-7.143 1.831-7.143 5.268C6.857 26.8 2 26.111 2 28.154V30h28v-1.846C30 26 25.143 26.8 25.143 11.385z" ></path>
  </svg>
  SVG Icon + Label
</sp-action-button>Icon only<sp-action-button variant="primary" label="Icon only">
  <sp-icon-help slot="icon"></sp-icon-help>
</sp-action-button>

### Options

#Section titled Options

#### Sizes

#Section titled Sizes

Extra Small<sp-action-group size="xs">
  <sp-action-button>Edit</sp-action-button>
  <sp-action-button>
    <sp-icon-edit slot="icon"></sp-icon-edit>
    Edit
  </sp-action-button>
  <sp-action-button label="Edit">
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
  <sp-action-button label="Edit" hold-affordance>
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
</sp-action-group>Small<sp-action-group size="s">
  <sp-action-button>Edit</sp-action-button>
  <sp-action-button>
    <sp-icon-edit slot="icon"></sp-icon-edit>
    Edit
  </sp-action-button>
  <sp-action-button label="Edit">
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
  <sp-action-button label="Edit" hold-affordance>
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
</sp-action-group>Medium<sp-action-group size="m">
  <sp-action-button>Edit</sp-action-button>
  <sp-action-button>
    <sp-icon-edit slot="icon"></sp-icon-edit>
    Edit
  </sp-action-button>
  <sp-action-button label="Edit">
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
  <sp-action-button label="Edit" hold-affordance>
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
</sp-action-group>Large<sp-action-group size="l">
  <sp-action-button>Edit</sp-action-button>
  <sp-action-button>
    <sp-icon-edit slot="icon"></sp-icon-edit>
    Edit
  </sp-action-button>
  <sp-action-button label="Edit">
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
  <sp-action-button label="Edit" hold-affordance>
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
</sp-action-group>Extra Large<sp-action-group size="xl">
  <sp-action-button>Edit</sp-action-button>
  <sp-action-button>
    <sp-icon-edit slot="icon"></sp-icon-edit>
    Edit
  </sp-action-button>
  <sp-action-button label="Edit">
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
  <sp-action-button label="Edit" hold-affordance>
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
</sp-action-group>

#### Variants

#Section titled Variants

The `<sp-action-button>` can be customized with either or both of the `emphasized` and `quiet` attributes. These will pair with either or both of the state attributes (`selected` and `disabled`) to decide the final visual delivery of the `<sp-action-button>`. Content addressed to the `icon` slot can also be provided and will be positioned just before the rest of the the supplied button content.

Default<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 2em;">
  <div>
    <sp-field-label for="standard">Default</sp-field-label>
    <sp-action-group id="standard">
      <sp-action-button>Edit</sp-action-button>
      <sp-action-button>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit">
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-selected">Selected</sp-field-label>
    <sp-action-group id="standard-selected">
      <sp-action-button selected>Edit</sp-action-button>
      <sp-action-button selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" selected hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled">Disabled</sp-field-label>
    <sp-action-group id="standard-disabled">
      <sp-action-button disabled>Edit</sp-action-button>
      <sp-action-button disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" disabled hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled-selected">
      Disabled + Selected
    </sp-field-label>
    <sp-action-group id="standard-disabled-selected">
      <sp-action-button disabled selected>Edit</sp-action-button>
      <sp-action-button disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" disabled selected hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>
</div>Quiet<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 2em;">
  <div>
    <sp-field-label for="standard">Default</sp-field-label>
    <sp-action-group quiet id="standard">
      <sp-action-button quiet>Edit</sp-action-button>
      <sp-action-button quiet>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" quiet>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" quiet hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-selected">Selected</sp-field-label>
    <sp-action-group quiet id="standard-selected">
      <sp-action-button quiet selected>Edit</sp-action-button>
      <sp-action-button quiet selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" quiet selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" quiet selected hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled">Disabled</sp-field-label>
    <sp-action-group quiet id="standard-disabled">
      <sp-action-button quiet disabled>Edit</sp-action-button>
      <sp-action-button quiet disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" quiet disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" quiet disabled hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled-selected">
      Disabled + Selected
    </sp-field-label>
    <sp-action-group quiet id="standard-disabled-selected">
      <sp-action-button quiet disabled selected>Edit</sp-action-button>
      <sp-action-button quiet disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" quiet disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" quiet disabled selected hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>
</div>Emphasized<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 2em;">
  <div>
    <sp-field-label for="standard">Default</sp-field-label>
    <sp-action-group emphasized id="standard">
      <sp-action-button emphasized>Edit</sp-action-button>
      <sp-action-button emphasized>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-selected">Selected</sp-field-label>
    <sp-action-group emphasized id="standard-selected">
      <sp-action-button emphasized selected>Edit</sp-action-button>
      <sp-action-button emphasized selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized selected hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled">Disabled</sp-field-label>
    <sp-action-group emphasized id="standard-disabled">
      <sp-action-button emphasized disabled>Edit</sp-action-button>
      <sp-action-button emphasized disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized disabled hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled-selected">
      Disabled + Selected
    </sp-field-label>
    <sp-action-group emphasized id="standard-disabled-selected">
      <sp-action-button emphasized disabled selected>Edit</sp-action-button>
      <sp-action-button emphasized disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized disabled selected hold-affordance >
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>
</div>Emphasized + quiet<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 2em;">
  <div>
    <sp-field-label for="standard">Default</sp-field-label>
    <sp-action-group emphasized quiet id="standard">
      <sp-action-button emphasized quiet>Edit</sp-action-button>
      <sp-action-button emphasized quiet>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-selected">Selected</sp-field-label>
    <sp-action-group emphasized quiet id="standard-selected">
      <sp-action-button emphasized quiet selected>Edit</sp-action-button>
      <sp-action-button emphasized quiet selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet selected hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled">Disabled</sp-field-label>
    <sp-action-group emphasized quiet id="standard-disabled">
      <sp-action-button emphasized quiet disabled>Edit</sp-action-button>
      <sp-action-button emphasized quiet disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet disabled>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet disabled hold-affordance>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>

  <div>
    <sp-field-label for="standard-disabled-selected">
      Disabled + Selected
    </sp-field-label>
    <sp-action-group emphasized quiet id="standard-disabled-selected">
      <sp-action-button emphasized quiet disabled selected>
        Edit
      </sp-action-button>
      <sp-action-button emphasized quiet disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
        Edit
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet disabled selected>
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
      <sp-action-button label="Edit" emphasized quiet disabled selected hold-affordance >
        <sp-icon-edit slot="icon"></sp-icon-edit>
      </sp-action-button>
    </sp-action-group>
  </div>
</div>

### Behaviors

#Section titled Behaviors

#### Action button with hold affordance

#Section titled Action button with hold affordance

The use of the `hold-affordance` attribute signifies that the `<sp-action-button>` in question will be delivered with a visual affordance outlining that special interaction with the button will dispatch a `longpress` event. Via a pointer input, this even will be dispatched when 300ms has passed after a `pointerdown` event without the presence of a `pointerup` or `pointercancel` event. Via the keyboard, an event with a code of `Space` or or `ArrowDown` while `altKey === true` will dispatch the event.

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 2em;">
  <overlay-trigger placement="bottom-start">
    <sp-action-button label="Edit" hold-affordance slot="trigger">
      <sp-icon-edit slot="icon"></sp-icon-edit>
    </sp-action-button>
    <sp-popover slot="longpress-content" dialog tip>
      <p style="color: var(--spectrum-neutral-content-color-default);">
        This content is triggered by the "longpress" interaction.
      </p>
    </sp-popover>
  </overlay-trigger>

  <overlay-trigger placement="top">
    <sp-action-button hold-affordance quiet slot="trigger">
      Show Longpress Content
    </sp-action-button>
    <sp-popover slot="longpress-content" dialog tip>
      <p style="color: var(--spectrum-neutral-content-color-default);">
        This content is triggered by the "longpress" interaction.
      </p>
    </sp-popover>
  </overlay-trigger>

  <overlay-trigger placement="top-end">
    <sp-action-button hold-affordance selected slot="trigger">
      <sp-icon-edit slot="icon"></sp-icon-edit>
      Extended Content with Longpress
    </sp-action-button>
    <sp-popover slot="longpress-content" dialog tip>
      <p style="color: var(--spectrum-neutral-content-color-default);">
        This content is triggered by the "longpress" interaction.
      </p>
    </sp-popover>
  </overlay-trigger>
</div>

#### Toggles

#Section titled Toggles

With the application of the `toggles` attribute, the button will self manage its `selected` property on `click`. When this value is updated, a cancellable `change` event will be dispatched to inform the parent application.

Default<sp-action-button toggles id="toggles-default">Toggle button</sp-action-button>
<sp-action-button toggles selected id="toggles-default">
  Toggle button
</sp-action-button>Quiet<sp-action-button toggles quiet id="toggles-quiet">
  Toggle button
</sp-action-button>
<sp-action-button toggles quiet selected id="toggles-quiet">
  Toggle button
</sp-action-button>Emphasized<sp-action-button toggles emphasized id="toggles-emphasized">
  Toggle button
</sp-action-button>
<sp-action-button toggles emphasized selected id="toggles-emphasized">
  Toggle button
</sp-action-button>Emphasized + Quiet<sp-action-button toggles emphasized quiet id="toggles-emphasized-quiet">
  Toggle button
</sp-action-button>
<sp-action-button toggles emphasized quiet selected id="toggles-emphasized-quiet">
  Toggle button
</sp-action-button>

#### Handling events

#Section titled Handling events

Events handlers for clicks and other user actions can be registered on a `<sp-action-button>` as on a standard HTML `<button>` element.

<sp-action-button onclick="spAlert(this, '<sp-action-button> clicked!')">
  Click me
</sp-action-button>
If you intend to create a link with a `href` attribute, we instead offer CSS classes for creating button-styled links. See more information in the accessibility section.

<a class="spectrum-ActionButton" href="https://github.com/adobe/spectrum-web-components">
  Link action button
</a>

#### Link API deprecation

#Section titled Link API deprecation

> **Deprecated**: The `href`, `target`, `download`, `referrerpolicy`, and `rel` attributes on `<sp-action-button>` are deprecated and will be removed in a future release. Use a native HTML anchor (`<a>`) element with the `spectrum-ActionButton` class instead.

Using `<sp-action-button href="...">` conflates button and link semantics, which creates accessibility issues: screen reader users navigating by form controls will not find link-styled buttons, and vice versa. Native HTML elements provide correct semantics by default.

If you intend to create a link with a `href` attribute, we instead offer CSS classes for creating button-styled links. To migrate, import the global elements stylesheet and apply action button classes to native `<a>` elements:

@import '@spectrum-web-components/styles/global-elements.css';
**Before (deprecated):**

<sp-action-button href="https://opensource.adobe.com/spectrum-web-components" target="_blank">
  Visit docs
</sp-action-button>
**After (recommended):**

<a class="spectrum-ActionButton spectrum-ActionButton--quiet" href="/docs" target="_blank">
  Visit docs
</a>
See the accessibility section for more details.

### Accessibility

#Section titled Accessibility

#### Include a label

#Section titled Include a label

A button is required to have either a visible text label or a `label` attribute on either the `<sp-button>` itself, or on an `<sp-icon*>` element child.

#### Don't override color

#Section titled Don't override color

Do not use custom colors for buttons. The colors of different button variations have been designed to be consistent and accessible.

#### Use a static button-styled native link if including href

#Section titled Use a static button-styled native link if including href

> **Deprecated**: The `href` attribute and other link-related properties (`target`, `download`, `referrerpolicy`, `rel`) on `<sp-action-button>` are deprecated and will be removed in a future release.

You may use a native link with classes to style it like a button. Refer to the Storybook examples that include `href` for the appropriate classes to use.

For styles to be fully available to slotted links, you must include the stylesheet for `@spectrum-web-components/styles/global-elements.css`.

To successfully receive button styling, the link must be one of the following:

*   A direct child of `<sp-theme>`
*   A slotted child of a component within `<sp-theme>`

To allow button-styled native links in the shadow DOM of extended components, ensure their stylesheet also imports `@spectrum-web-components/styles/global-elements.css`.

**Note**: native button-styled links do not support disabled or pending states, or hold affordances.

<!-- Include in your own application stylesheet and extended component styles: @import '@spectrum-web-components/styles/global-elements.css'; -->

<a class="spectrum-ActionButton" href="https://github.com/adobe/spectrum-web-components">
  Link action button
</a>
<a class="spectrum-ActionButton spectrum-ActionButton--quiet" href="https://github.com/adobe/spectrum-web-components">
  <!-- Use icon components and continue to define slot="icon" for the best styling support -->
  <sp-icon-help slot="icon"></sp-icon-help>
  Quiet link action button
</a>

#### Don't mix href and non-href buttons in a set of buttons

#Section titled Don't mix href and non-href buttons in a set of buttons

A screen reader user will not encounter href buttons when navigating by buttons or form controls. While they can both be used in the same page, problems could occur if mixing the types in close proximity to each other.

#### Use static black or static white to contrast with backgrounds and images

#Section titled Use static black or static white to contrast with backgrounds and images

To ensure maximum contrast with the background, use static black for light backgrounds and images, and static white for dark backgrounds and images. Avoid placing static components on top of busy images with a lot of variance in contrast.

Static black on light background<div style="background-color: #ccffee; padding: 20px">
  <sp-action-button static="black">Click me</sp-action-button>
  <sp-action-button static="black" selected>Click me</sp-action-button>
</div>Static white on dark background<div style="background-color: #220033; padding: 20px">
  <sp-action-button static="white">Click me</sp-action-button>
  <sp-action-button static="white" selected>Click me</sp-action-button>
</div>

#### Clearly state the action

#Section titled Clearly state the action

Make sure that an action button’s label clearly states the outcome of the action. Use the same word or phrase as found elsewhere in the experience.

Changelog
---------

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

1.11.1
------

#Section titled 1.11.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1

1.11.0
------

#Section titled 1.11.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

1.10.0
------

#Section titled 1.10.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/shared@1.10.0

1.9.1
-----

#Section titled 1.9.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

1.9.0
-----

#Section titled 1.9.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

1.8.0
-----

#Section titled 1.8.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

1.7.0
-----

#Section titled 1.7.0

### Minor Changes

#Section titled Minor Changes

*   #5204`c1669d2` Thanks @Rajdeepc! - - **Fixed** : Action buttons with href attributes now properly detects modifier keys and skips the proxy click, allowing only native browser behavior to proceed.

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

1.6.0
-----

#Section titled 1.6.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`00eb0a8`]: 
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

1.5.0
-----

#Section titled 1.5.0

### Patch Changes

#Section titled Patch Changes

*   #5325`6c58f50` Thanks @renovate! - #​3644 Thanks @​marissahuysentruyt!

This patch update fixes support for `--mod-actionbutton-border-radius` to make sure it is accessible by consumers and overwrites the default border radius setting when used.

*   Updated dependencies [`4e06533`]:

    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

1.4.0
-----

#Section titled 1.4.0

### Patch Changes

#Section titled Patch Changes

*   #5190`72dbe62` Thanks @Rajdeepc! - update action button fast follows for spectrum 2

*   Updated dependencies []:

    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

1.3.0
-----

#Section titled 1.3.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

1.2.0 (2025-02-27)
------------------

#Section titled 

### Features

#Section titled Features

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 1.1.1 (2025-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

1.1.0 (2025-01-29)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

### 1.0.3 (2024-12-09)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **action-button:** action-button with href can be perceived by screen reader (#4927) (2a0b3a5)

### 1.0.1 (2024-11-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

1.0.0 (2024-10-31)
------------------

#Section titled 

### BREAKING CHANGES

#Section titled BREAKING CHANGES

*   remove action-button variant property (#4741)
*   remove deprecated 'static' references (#4818)

0.49.0 (2024-10-15)
-------------------

#Section titled 

### Features

#Section titled Features

*   add `static-color` to replace `static` (#4808) (43cf086)

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.48.0 (2024-09-17)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **picker:** added a custom class to make `:focus-visible` styles consistent across all browsers (#4724) (d667d08)

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.47.1 (2024-08-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.42.4 (2024-05-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.42.0 (2024-03-19)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

### Features

#Section titled Features

*   **asset:** use core tokens (99e76f4)

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.41.0 (2024-02-13)
-------------------

#Section titled 

### Features

#Section titled Features

*   **icon:** use core tokens (a11ef6b)

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.40.1 (2023-12-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.40.0 (2023-11-16)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.39.4 (2023-11-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.39.2 (2023-10-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.39.1 (2023-10-06)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **action-button:** allow change events to bubble and pierce shadowdom (#3614) (3f76e04)

0.39.0 (2023-09-25)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.37.0 (2023-08-18)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   handle longpress and over filter overlays (483e52d)

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.35.0 (2023-07-31)
-------------------

#Section titled 

### Features

#Section titled Features

*   **action-bar:** use core tokens (4e21edf)

0.34.0 (2023-07-11)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **action-button,action-menu,picker,split-button:** expand and update application of aria-* attributes (52c0156)
*   **action-group:** ensure Action Button clicks are attributed to the right element (#3292) (ddccab7)

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.32.0 (2023-06-01)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.31.0 (2023-05-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Bug Fixes

#Section titled Bug Fixes

*   **action-button:** add support for XS t-shirt size (75440ce)
*   **action-button:** all "selected" Action Buttons should be "aria-pressed=true" (d85e235)
*   **action-button:** ensure disabled buttons are not interactable (b81c3ba)
*   **action-button:** expand Spectrum CSS processing (ff1a424)
*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   correct specificity of webkit appearance work around (f0d06bf)
*   correctly delivery visuals and mouse interactions for litAnchor and extensions (0ae889a)
*   expand sized functionality to support no default and returning to default values (acf3cfb)
*   prevent default hoisting of custom pseudo elements (7f66346)
*   prevent longpress when interacting with context menu (f8b0732)
*   support a wider number of sizes (ee44978)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update export patterns (b2da444)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   allow activation of longpress content (55e71fd)
*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage latest Spectrum button API (9caf2f6)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   support Spectrum Token consumption and update Action Button to use them (743ab16)
*   support static white and static black variants of Action Button (7f1e25b)
*   **tabs:** add sp-tab-panel element (b17d276)
*   update lit-* dependencies, wip (377f3c8)
*   use latest exports specification (a7ecf4b)
*   use SixedMixin to manage "size" property (8819821)

### Performance Improvements

#Section titled Performance Improvements

*   accept new Spectrum CSS featuring simpler DOM structure (a0b042b)

### 0.10.16 (2023-04-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.15 (2023-04-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.14 (2023-03-22)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   prevent default hoisting of custom pseudo elements (7f66346)

### Performance Improvements

#Section titled Performance Improvements

*   accept new Spectrum CSS featuring simpler DOM structure (a0b042b)

### 0.10.13 (2023-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.12 (2023-02-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.11 (2023-02-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.10 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.9 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.8 (2022-12-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.7 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.6 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.5 (2022-10-28)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.4 (2022-10-17)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.3 (2022-10-10)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **action-button:** add support for XS t-shirt size (75440ce)

### 0.10.2 (2022-09-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.10.1 (2022-08-24)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   prevent longpress when interacting with context menu (f8b0732)

0.10.0 (2022-08-09)
-------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

### 0.9.1 (2022-08-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.9.0 (2022-07-18)
------------------

#Section titled 

### Features

#Section titled Features

*   support Spectrum Token consumption and update Action Button to use them (743ab16)

### 0.8.7 (2022-06-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.8.6 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.8.5 (2022-05-27)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update consumption of Spectrum CSS for latest version (ed2305b)

### 0.8.4 (2022-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.8.3 (2022-04-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.8.2 (2022-03-30)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.8.1 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.8.0 (2022-03-04)
------------------

#Section titled 

### Features

#Section titled Features

*   leverage latest Spectrum button API (9caf2f6)
*   support static white and static black variants of Action Button (7f1e25b)

### 0.7.4 (2022-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.7.3 (2022-01-26)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.7.2 (2022-01-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.7.1 (2021-12-13)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   **action-button:** all "selected" Action Buttons should be "aria-pressed=true" (d85e235)

0.7.0 (2021-11-08)
------------------

#Section titled 

### Features

#Section titled Features

*   update lit-* dependencies, wip (377f3c8)

### 0.6.1 (2021-11-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.6.0 (2021-11-02)
------------------

#Section titled 

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)

### 0.5.9 (2021-10-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.8 (2021-09-20)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.7 (2021-09-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.6 (2021-08-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.5 (2021-08-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.4 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.3 (2021-07-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.2 (2021-06-16)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.5.1 (2021-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.5.0 (2021-05-24)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **action-button:** ensure disabled buttons are not interactable (b81c3ba)

### Features

#Section titled Features

*   **tabs:** add sp-tab-panel element (b17d276)

### 0.4.7 (2021-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.4.6 (2021-04-15)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.4.5 (2021-04-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.4.4 (2021-03-29)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **action-button:** expand Spectrum CSS processing (ff1a424)

### 0.4.3 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.4.2 (2021-03-22)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   correctly delivery visuals and mouse interactions for litAnchor and extensions (0ae889a)

### 0.4.1 (2021-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.4.0 (2021-03-04)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   support a wider number of sizes (ee44978)

### Features

#Section titled Features

*   use latest exports specification (a7ecf4b)

0.3.0 (2021-02-11)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   expand sized functionality to support no default and returning to default values (acf3cfb)
*   update to latest spectrum-css packages (a5ca19f)

### Features

#Section titled Features

*   allow activation of longpress content (55e71fd)

### 0.2.2 (2021-02-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

### 0.2.1 (2021-01-28)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/action-button

0.2.0 (2021-01-21)
------------------

#Section titled 0.2.0 (2021-01-21)

### Bug Fixes

#Section titled Bug Fixes

*   correct specificity of webkit appearance work around (f0d06bf)
*   update export patterns (b2da444)
*   use icons without "size" values (3fc7c91)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

### Features

#Section titled Features

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

0.1.0 (2021-01-13)
------------------

#Section titled 0.1.0 (2021-01-13)

### Bug Fixes

#Section titled Bug Fixes

*   update export patterns (b2da444)
*   use icons without "size" values (3fc7c91)

### Features

#Section titled Features

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `active``active``boolean``false``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `emphasized``emphasized``boolean``false``holdAffordance``hold-affordance``boolean``false``href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `quiet``quiet``boolean``false``referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `role``role``string``'button'``selected``selected``boolean``false` Whether an Action Button with `role='button'` should also be `aria-pressed='true'` `staticColor``static-color``'white' | 'black' | undefined` The static color variant to use for the action button. `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `toggles``toggles``boolean``false` Whether to automatically manage the `selected` attribute on interaction and whether `aria-pressed="false"` should be used when `selected === false` `type``type``'button' | 'submit' | 'reset'``'button'` The default behavior of the button. Possible values are: `button` (default), `submit`, and `reset`. `value``value``string`

### Slots

#Section titled Slots

 Name  Description `default slot` text label of the Action Button `icon` The icon to use for Action Button 

### Events

#Section titled Events

 Name  Type  Description `change``Event``Announces a change in the `selected` property of an action button``longpress``CustomEvent``Synthesizes a "longpress" interaction that signifies a `pointerdown` event that is >=300ms or a keyboard event where code is `Space` or code is `ArrowDown` while `altKey===true`.`

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/action-button/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/action-button/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
