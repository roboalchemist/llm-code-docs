# Source: https://opensource.adobe.com/spectrum-web-components/components/picker-button/

Title: Picker Button: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/picker-button/

Markdown Content:
An `<sp-picker-button>` is used as a sub-component of patterns like the `<sp-combobox>` (release pending) to pair a button interface with a text input. With its many custom states and alterations, it isn't likely to be leveraged directly outside of more complex UIs.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/picker-button?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/picker-button?style=for-the-badge)

yarn add @spectrum-web-components/picker-button

Import the side effectful registration of `<sp-picker-button>` via:

import '@spectrum-web-components/picker-button/sp-picker-button.js';

When looking to leverage the `PickerButton` base class as a type and/or for extension purposes, do so via:

import { PickerButton } from '@spectrum-web-components/picker-button';

With the use of the `label` slot, you can deliver an `<sp-picker-button>` with both an icon and a text label:

<sp-picker-button><span slot="label">All</span></sp-picker-button>
Without content addressed to the `label` slot, the `<sp-picker-button>` with both an icon and a text label:

<sp-picker-button></sp-picker-button>
You can customize the icon in an `<sp-picker-button>` by addressing a new icon to the `icon` slot:

<sp-picker-button><sp-icon-add slot="icon"></sp-icon-add></sp-picker-button>Small<sp-picker-button size="s"></sp-picker-button>
<br />
<sp-picker-button size="s"><span slot="label">All</span></sp-picker-button>Medium<sp-picker-button size="m"></sp-picker-button>
<br />
<sp-picker-button size="m"><span slot="label">All</span></sp-picker-button>Large<sp-picker-button size="l"></sp-picker-button>
<br />
<sp-picker-button size="l"><span slot="label">All</span></sp-picker-button>Extra Large<sp-picker-button size="xl"></sp-picker-button>
<br />
<sp-picker-button size="xl"><span slot="label">All</span></sp-picker-button>
When delivered as part of the `express` system, an `<sp-picker-button>` with the `rounded` attribute will be given deeply rounded corners:

<sp-picker-button rounded></sp-picker-button>
<br />
<sp-picker-button rounded><span slot="label">All</span></sp-picker-button>
When delivered with the `quiet` attribute, the `<sp-picker-button>` will take a less pronounced visual delivery:

<sp-picker-button quiet></sp-picker-button>
<br />
<sp-picker-button quiet><span slot="label">All</span></sp-picker-button>
By default the `<sp-picker-button>` will be given a `position` attribute with the value `right`, which is best leveraged at the right edge of an associated `<sp-textfield>` element. If your UI desires that the `<sp-picker-button>` be placed to the left of the related input, use the `position` attribute and set it to `left`:

<sp-picker-button position="left"></sp-picker-button>
<br />
<sp-picker-button position="left">
  <span slot="label">All</span>
</sp-picker-button>
When paired with an expanded UI, e.g. an `<sp-combobox>` with its autocomplete options visible, an `<sp-picker-button>` should be given the `open` attribute to visual match the delivered state in the larger UI:

<sp-picker-button open></sp-picker-button>
<br />
<sp-picker-button open><span slot="label">All</span></sp-picker-button>
Leveraging the `disabled` attribute will dim the `<sp-picker-button>` and alter its presentation in the accessibility tree:

<sp-picker-button disabled></sp-picker-button>
<br />
<sp-picker-button disabled><span slot="label">All</span></sp-picker-button>
When delivered as part of the `spectrum` system, an `<sp-picker-button>` with the `invalid` attribute will be given a red border:

<sp-picker-button invalid></sp-picker-button>
<br />
<sp-picker-button invalid><span slot="label">All</span></sp-picker-button>
The example below is for demonstration purposes. For an example implementation of `<sp-picker-button>` view `Combobox.ts`. For comprehensive information on menu button accessibility, see WAI ARIA Authoring Practice Guide's Menu Button Pattern.

<sp-field-label for="color">Color</sp-field-label>
<sp-textfield id="color"></sp-textfield>
<overlay-trigger type="modal">
  <sp-picker-button aria-controls="colors-menu" aria-expanded="false" aria-haspopup="menu" aria-describedby="color" slot="trigger" ></sp-picker-button>
  <sp-tray slot="click-content">
    <sp-menu id="colors-menu">
      <sp-menu-item>Red</sp-menu-item>
      <sp-menu-item>Blue</sp-menu-item>
    </sp-menu>
  </sp-tray>
</overlay-trigger>
To ensure menu items can be read by assistive technology, do _one_ of the following:

*   Place visible text in the component's `label` slot.
*   Use `aria-label` attribute.
*   Set the `aria-labelledby` attribute to the ID reference of the menu element.

To indicate to assistive technology what the button does, do _all_ of the following:

*   Set the `aria-controls` property to the ID reference of the menu element.
*   Set the `aria-haspopup` property to `"menu"` or `"true"`.
*   Set the `aria-expanded` property to `"menu"` or `"true"` or `"false"` depending on whether the menu is displayed.

Ensure that picker button can be operated by keyboard users:

*   Required: Open the menu and focus on first menu item when Enter or Space is pressed.
*   _Optional_: Open the menu and focus on first menu item when Down Arrow is pressed.
*   _Optional_: Open the menu and focus on last menu item when Up Arrow is pressed.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1

*   Updated dependencies [`f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`00eb0a8`]: 
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5202`fa4be70` Thanks @Rajdeepc! - Updates the picker button component from version 6.0.0-s2-foundations.16 to 6.1.2. The update should bring the background colors for the picker button in line with S2-foundations design specs:

default state: `gray-50` to `gray-100` hover state: `gray-100` to `gray-200` key-focus state: `gray-100` to `gray-200`

*   Updated dependencies [`4e06533`]:

    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   **picker-button:** update quiet styles (#4383) (42bf291)

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   **icon:** use core tokens (a11ef6b)

*   **combobox:** add combobox pattern (#3894) (47d7d71), closes #3887

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   update deps graph, update link docs (#3709) (2deb284)

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   **picker-button:** include missing dependency on @spectrum-web-components/button (#3515) (ed44c2b)

*   **picker-button:** migrate to core tokens (b39219c)

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   add Picker Button pattern (31337b8)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

**Note:** Version bump only for package @spectrum-web-components/picker-button

*   add Picker Button pattern (31337b8)

Property  Attribute  Type  Default  Description `active``active``boolean``false``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `invalid``invalid``boolean``false``label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `position``position``'left' | 'right'``'right'``referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `type``type``'button' | 'submit' | 'reset'``'button'` The default behavior of the button. Possible values are: `button` (default), `submit`, and `reset`.

Name  Description `default slot` text content to be displayed in the Button element `icon` icon element(s) to display at the start of the button
