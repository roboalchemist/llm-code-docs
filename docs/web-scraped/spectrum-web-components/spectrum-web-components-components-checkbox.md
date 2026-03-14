# Source: https://opensource.adobe.com/spectrum-web-components/components/checkbox/

Title: Checkbox: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/checkbox/

Markdown Content:
`<sp-checkbox>` allow users to select multiple items from a list of independent options, or to mark an individual option as selected.

Should I use a checkbox or a switch? Use a switch when activating something instead of selecting.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/checkbox?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/checkbox?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/checkbox
Import the side effectful registration of `<sp-checkbox>` via:

import '@spectrum-web-components/checkbox/sp-checkbox.js';
When looking to leverage the `Checkbox` base class as a type and/or for extension purposes, do so via:

import { Checkbox } from '@spectrum-web-components/checkbox';
A checkbox consists of a box that can be checked or unchecked, and a label that describes its purpose. The checkbox can also be in an indeterminate state, which is visually distinct from both checked and unchecked states.

Small<sp-field-group horizontal label="Small Checkboxes">
  <sp-checkbox size="s">Small</sp-checkbox>
  <sp-checkbox size="s" checked>Small Checked</sp-checkbox>
  <sp-checkbox size="s" indeterminate>Small Indeterminate</sp-checkbox>
</sp-field-group>Medium<sp-field-group horizontal label="Medium Checkboxes">
  <sp-checkbox size="m">Medium</sp-checkbox>
  <sp-checkbox size="m" checked>Medium Checked</sp-checkbox>
  <sp-checkbox size="m" indeterminate>Medium Indeterminate</sp-checkbox>
</sp-field-group>Large<sp-field-group horizontal label="Large Checkboxes">
  <sp-checkbox size="l">Large</sp-checkbox>
  <sp-checkbox size="l" checked>Large Checked</sp-checkbox>
  <sp-checkbox size="l" indeterminate>Large Indeterminate</sp-checkbox>
</sp-field-group>Extra Large<sp-field-group horizontal label="Extra Large Checkboxes">
  <sp-checkbox size="xl">Extra Large</sp-checkbox>
  <sp-checkbox size="xl" checked>Extra Large Checked</sp-checkbox>
  <sp-checkbox size="xl" indeterminate>Extra Large Indeterminate</sp-checkbox>
</sp-field-group>Standard Checkboxes
Standard checkboxes are the default style for checkboxes. They are optimal for application panels where all visual elements are monochrome in order to direct focus to the content.

<div style="display: flex; justify-content: space-between;">
  <div style="display: flex; flex-direction: column;">
    <h4 class="spectrum-Heading--subtitle1">Default</h4>
    <sp-checkbox>Web component</sp-checkbox>
    <sp-checkbox checked>Web component</sp-checkbox>
    <sp-checkbox indeterminate>Web component</sp-checkbox>
  </div>

  <div style="display: flex; flex-direction: column;">
    <h4 class="spectrum-Heading--subtitle1">Invalid</h4>
    <sp-field-group vertical label="Select an option" invalid>
      <sp-checkbox invalid>Web component</sp-checkbox>
      <sp-checkbox checked invalid>Web component</sp-checkbox>
      <sp-checkbox indeterminate invalid>Web component</sp-checkbox>
      <sp-help-text slot="negative-help-text" icon>
        This selection is invalid.
      </sp-help-text>
    </sp-field-group>
  </div>

  <div style="display: flex; flex-direction: column;">
    <h4 class="spectrum-Heading--subtitle1">Disabled</h4>
    <sp-checkbox disabled>Web component</sp-checkbox>
    <sp-checkbox checked disabled>Web component</sp-checkbox>
    <sp-checkbox indeterminate disabled>Web component</sp-checkbox>
  </div>
</div>Emphasized Checkboxes
Emphasized checkboxes are a secondary style for checkboxes. The blue color provides a visual prominence that is optimal for forms, settings, lists or grids of assets, etc. where the checkboxes need to be noticed.

<div style="display: flex; justify-content: space-between;">
  <div style="display: flex; flex-direction: column;">
    <h4 class="spectrum-Heading--subtitle1">Default</h4>
    <sp-checkbox emphasized>Web component</sp-checkbox>
    <sp-checkbox emphasized checked>Web component</sp-checkbox>
    <sp-checkbox emphasized indeterminate>Web component</sp-checkbox>
  </div>

  <div style="display: flex; flex-direction: column;">
    <h4 class="spectrum-Heading--subtitle1">Invalid</h4>
    <sp-field-group vertical label="Select an option" invalid>
      <sp-checkbox emphasized invalid>Web component</sp-checkbox>
      <sp-checkbox emphasized checked invalid>Web component</sp-checkbox>
      <sp-checkbox emphasized indeterminate invalid>Web component</sp-checkbox>
      <sp-help-text slot="negative-help-text" icon>
        This selection is invalid.
      </sp-help-text>
    </sp-field-group>
  </div>

  <div style="display: flex; flex-direction: column;">
    <h4 class="spectrum-Heading--subtitle1">Disabled</h4>
    <sp-checkbox emphasized disabled>Web component</sp-checkbox>
    <sp-checkbox emphasized checked disabled>Web component</sp-checkbox>
    <sp-checkbox emphasized indeterminate disabled>Web component</sp-checkbox>
  </div>
</div>
The `invalid` attribute indicates that the checkbox's value is invalid. When set, appropriate ARIA attributes will be automatically applied.

When a checkbox is in an invalid state, provide help text to explain the error and guide the user toward a solution. Wrap the checkbox in an `<sp-field-group>` to associate the help text with the checkbox. (See help text for more information.)

**Important:** Both the `<sp-field-group>` and its child `<sp-checkbox>` elements must be marked as `invalid` for the complete invalid state to display correctly:

*   The `invalid` attribute on `<sp-field-group>` controls help text visibility (showing the `negative-help-text` slot).
*   The `invalid` attribute on each `<sp-checkbox>` controls the visual invalid styling on the checkbox itself.

Setting only one creates a sync hazard where either the help text won't display or the checkboxes won't show invalid styling.

<sp-field-group vertical label="Terms and conditions" invalid>
  <sp-checkbox invalid>I accept the terms and conditions</sp-checkbox>
  <sp-help-text slot="negative-help-text" icon>
    You must accept the terms to continue.
  </sp-help-text>
</sp-field-group>
The `disabled` attribute prevents the checkbox from receiving focus or events. The checkbox will appear faded.

<sp-checkbox disabled>Disabled</sp-checkbox>
The `indeterminate` attribute sets the checkbox to an indeterminate state, visually distinct from both checked and unchecked states.

<sp-checkbox indeterminate>Indeterminate</sp-checkbox>
Checkboxes have a `readonly` attribute for when they’re in the disabled state but still need their labels to be shown. This allows for content to be copied, but not interacted with or changed.

<sp-checkbox readonly>Read-only</sp-checkbox>
Help text can be accessibly associated with checkboxes by using the `help-text` or `negative-help-text` slots on an `<sp-field-group>` element. When using the `negative-help-text` slot, `<sp-field-group>` will self manage the presence of this content based on the value of the `invalid` property on your `<sp-field-group>` element. Content within the `help-text` slot will be shown by default. When your `<sp-field-group>` should receive help text based on state outside of the complexity of `invalid` or not, manage the content addressed to the `help-text` from above to ensure that it displays the right messaging and possesses the right `variant`.

Read more about using help text.

Self managed<sp-field-group vertical id="self" label="Notification preferences" onchange=" const checkboxes = this.querySelectorAll('sp-checkbox'); const noneChecked = ![...checkboxes].some(cb => cb.checked); this.invalid = noneChecked; ">
  <sp-checkbox value="email">Email notifications</sp-checkbox>
  <sp-checkbox value="sms">SMS notifications</sp-checkbox>
  <sp-checkbox value="push" checked>Push notifications</sp-checkbox>
  <sp-help-text slot="help-text">
    Choose how you'd like to be notified.
  </sp-help-text>
  <sp-help-text slot="negative-help-text" icon>
    Select at least one notification method.
  </sp-help-text>
</sp-field-group>Managed from above<sp-field-label for="above">Notification preferences</sp-field-label>
<sp-field-group vertical id="above" onchange=" const checkboxes = this.querySelectorAll('sp-checkbox'); const noneChecked = ![...checkboxes].some(cb => cb.checked); const helpText = this.querySelector(`[slot='help-text']`); helpText.icon = noneChecked; helpText.textContent = noneChecked ? 'Select at least one notification method.' : 'Choose how you\'d like to be notified.'; helpText.variant = noneChecked ? 'negative' : 'neutral'; ">
  <sp-checkbox value="email">Email notifications</sp-checkbox>
  <sp-checkbox value="sms">SMS notifications</sp-checkbox>
  <sp-checkbox value="push" checked>Push notifications</sp-checkbox>
  <sp-help-text slot="help-text">
    Choose how you'd like to be notified.
  </sp-help-text>
</sp-field-group>Single checkbox
When a single checkbox requires validation, wrap it in an `<sp-field-group>` to associate help text:

<sp-field-group vertical label="Agreement" invalid>
  <sp-checkbox invalid>I have read and accept the terms of service</sp-checkbox>
  <sp-help-text slot="negative-help-text" icon>
    You must accept the terms of service to continue.
  </sp-help-text>
</sp-field-group>
Event handlers for clicks and other user actions can be registered on an `<sp-checkbox>` as they would a standard `<input type="checkbox">` element.

<sp-checkbox id="checkbox-example" onclick="spAlert(this, '<sp-checkbox> clicked!')">
  Check this box to see an onclick alert.
</sp-checkbox>
Checkboxes are accessible by default, rendered in HTML using the `<input type="checkbox">` element. When the checkbox is set as `indeterminate` or `invalid`, the appropriate ARIA state attribute will automatically be applied.

Every checkbox must have a label that clearly describes its purpose. The label can be provided as content within the `<sp-checkbox>` element.

<sp-checkbox>Send me text messages.</sp-checkbox>
Sets of checkboxes should always have a clear label that describes what the list of options represents and guides users what to do. This is important for accessibility, since a screen reader will read the label before each option. (See field group's label documentation for more information.)

<sp-field-group label="Select your toppings">
  <sp-checkbox>Ketchup</sp-checkbox>
  <sp-checkbox>Mustard</sp-checkbox>
  <sp-checkbox>Pickles</sp-checkbox>
</sp-field-group>
Checkbox groups should use help text for error messaging and descriptions. Descriptions are valuable for giving context about a selection or for clarifying the options.

It is not currently possible to provide accessible ARIA references between elements in different shadow roots. To ensure proper association between elements, help text must be included via the `slot="help-text"` or `slot="negative-help-text"` on the parent `<sp-field-group>`.

See help text for more information.

Checkboxes can be toggled using the Space key when focused. They follow the standard tab order of the page.

Screen readers interpret checkboxes by announcing their role, label, current state, and role to the user. This allows users relying on assistive technology to understand and interact with the checkbox effectively.

When focused, a screen reader will announce:

*   The label (text provided inside the or associated with it)
*   The state: "checked", "not checked", or "partially checked" (when indeterminate is set)
*   The role: "checkbox"
*   If the checkbox is marked as invalid, it may also announce "invalid entry" depending on the screen reader.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1

*   Updated dependencies [`f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5228`a4de4c7` Thanks @renovate! - 📝 #3617 Thanks @marissahuysentruyt!

Adds a `::before` pseudo element to properly target the checkbox checked input + box element. The selector update, specifically in the invalid + checked + hover state should now get the proper error background color, as opposed to the default background color.

*   Updated dependencies []:

    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   #5176`468314f` Thanks @TarunAdobe!

    1.   chore(checkbox): updated to latest css v10.1.1 for s2 fast follow
    2.   chore(dialog): The error property was not properly deprecated with a full migration plan in place. This has caused confusion and false sense of urgency for consumers to migrate. We are removing it to eliminate those pain points for consumers while we take a deep look at our dialogs and patterns.
    3.   chore(menu): updated to latest css v9.1.1 for s2 fast follow
    4.   fix(overlay): sp-overlay with type="manual" should close on pressing ESC key. When the last item is on overlay stack we are triggering the close method on esc key event.

*   Updated dependencies []:

    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   **base:** move lit imports to base (#4416) (b7cb07e)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   **checkbox:** add missing readonly prop (#3859) (35b5649)

*   **checkbox:** refactor architecture for more rendering perf and DOM element count (7c2277f)

*   **textfield:** added name attribute to textfield (#3752) (593005a)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   #353 with a temporary override (e6b4e37)
*   add support for "readonly" attribute (4bce3b7)
*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   **checkbox:** allow events to be cancelled on checkboxbase (aab568c)
*   **checkbox:** work around specificity changes when processing Spectrum CSS and cover with tests (d53a871)
*   complete deprecation of "quiet" attribute in checkbox and radio (29d8452)
*   correct @element jsDoc listing across library (c97a632)
*   ensure [disabled] styling (4c067eb)
*   ensure aria attributes based on state (6369ff3)
*   ensure aria attributes based on state (6ee43de)
*   ensure browser understandable extensions (f4e59f7)
*   focusable style (48ea3e7)
*   implement "emphasized" styles (750bbe7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   move hover/focus hoisting into conditioning (15ac2f7)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   reduce cycles (66a4efb)
*   **shared:** prevent focusable returning focus to host (745f7b0)
*   stop merging selectors in a way that alters the cascade (369388f)
*   support a wider number of sizes (ee44978)
*   **textfield:** remove use of sp-icons-* (9a5c213)
*   update configuration for Spectrum CSS processing for specificity (5c2e21e)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** add action-group pattern (d2de766)
*   add and use icons-ui package (d9c3ab2)
*   add t-shirt sizing with visual regressions to checkbox and picker elements (ce47ec8)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)
*   **checkbox:** update spectrum css input (e894cb4)
*   conditionally load focus-visible polyfill (6b5e5cf)
*   **field-group:** add field-group pattern (f8d265c)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use 3.0.0-beta.* release for styles (877b485)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   move hover/focus hoisting into conditioning (15ac2f7)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   **checkbox:** allow events to be cancelled on checkboxbase (aab568c)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   conditionally load focus-visible polyfill (6b5e5cf)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)

*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   add support for "readonly" attribute (4bce3b7)
*   reduce cycles (66a4efb)

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   support a wider number of sizes (ee44978)

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   add t-shirt sizing with visual regressions to checkbox and picker elements (ce47ec8)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   complete deprecation of "quiet" attribute in checkbox and radio (29d8452)
*   ensure [disabled] styling (4c067eb)
*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update configuration for Spectrum CSS processing for specificity (5c2e21e)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **checkbox:** update spectrum css input (e894cb4)
*   **field-group:** add field-group pattern (f8d265c)

*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **checkbox:** update spectrum css input (e894cb4)
*   **field-group:** add field-group pattern (f8d265c)

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   **checkbox:** work around specificity changes when processing Spectrum CSS and cover with tests (d53a871)
*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   **action-group:** add action-group pattern (d2de766)
*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)
*   use 3.0.0-beta.* release for styles (877b485)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   ensure browser understandable extensions (f4e59f7)

*   **shared:** prevent focusable returning focus to host (745f7b0)

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   ensure aria attributes based on state (6369ff3)
*   ensure aria attributes based on state (6ee43de)

*   **textfield:** remove use of sp-icons-* (9a5c213)

*   add and use icons-ui package (d9c3ab2)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   #353 with a temporary override (e6b4e37)

*   focusable style (48ea3e7)

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

**Note:** Version bump only for package @spectrum-web-components/checkbox

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/checkbox

Property  Attribute  Type  Default  Description `checked``checked``boolean``false``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `emphasized``emphasized``boolean``false``indeterminate``indeterminate``boolean``false``invalid``invalid``boolean``false``name``name``string | undefined``readonly``readonly``boolean``false``tabIndex``tabindex``number``0`

Name  Description `default slot` content to display as the label for the Checkbox

Name  Type  Description `change``Event``Announces a change in the `checked` property of a Checkbox`
