# Source: https://opensource.adobe.com/spectrum-web-components/components/field-group/

Title: Field Group: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/field-group/

Markdown Content:
An `<sp-field-group>` element is used to layout a group of fields, usually `<sp-checkbox>` elements. It can be leveraged for `vertical` or `horizontal` organization of the fields that are supplied as its children.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/field-group?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/field-group?style=for-the-badge)

yarn add @spectrum-web-components/field-group
Import the side effectful registration of `<sp-field-group>` via:

import '@spectrum-web-components/field-group/sp-field-group.js';
When looking to leverage the `FieldGroup` base class as a type and/or for extension purposes, do so via:

import { FieldGroup } from '@spectrum-web-components/field-group';<sp-field-group horizontal label="Choose from horizontally placed options">
  <sp-checkbox>Checkbox 1</sp-checkbox>
  <sp-checkbox>Checkbox 2</sp-checkbox>
  <sp-checkbox checked>Checkbox 3</sp-checkbox>
  <sp-checkbox>Checkbox 4</sp-checkbox>
  <sp-checkbox>Checkbox 5</sp-checkbox>
</sp-field-group>
A field group must have a label in order to be accessible. A label can be provided either via the `label` attribute, like the previous example or with an `<sp-field-label>` element.

<sp-field-label for="horizontal">
  Choose from horizontally placed options
</sp-field-label>
<sp-field-group horizontal id="horizontal">
  <sp-checkbox>Checkbox 1</sp-checkbox>
  <sp-checkbox>Checkbox 2</sp-checkbox>
  <sp-checkbox checked>Checkbox 3</sp-checkbox>
  <sp-checkbox>Checkbox 4</sp-checkbox>
  <sp-checkbox>Checkbox 5</sp-checkbox>
</sp-field-group>
Help text can be accessibly associated with an `<sp-field-group>` element by using the `help-text` or `negative-help-text` slots. When using the `negative-help-text` slot, `<sp-field-group>` will self manage the presence of this content based on the value of the `invalid` property on your `<sp-field-group>` element. Content within the `help-text` slot will be show by default. When your `<sp-field-group>` should receive help text based on state outside of the complexity of `invalid` or not, manage the content addressed to the `help-text` from above to ensure that it displays the right messaging and possesses the right `variant`.

Self managed<sp-field-group horizontal id="self" label="What are your favorite fruits?">
  <sp-checkbox value="apple">Apple</sp-checkbox>
  <sp-checkbox value="not-a-fruit" onchange="javascript:this.parentElement.invalid = this.checked" >
    Lettuce
  </sp-checkbox>
  <sp-checkbox value="strawberry" checked>Strawberry</sp-checkbox>
  <sp-help-text slot="help-text">One of these is not a fruit.</sp-help-text>
  <sp-help-text slot="negative-help-text" icon>
    Choose actual fruit(s).
  </sp-help-text>
</sp-field-group>Managed from above<sp-field-label for="above">What are your favorite fruits?</sp-field-label>
<sp-field-group horizontal id="above">
  <sp-checkbox value="apple">Apple</sp-checkbox>
  <sp-checkbox value="not-a-fruit" onchange=" const helpText = this.parentElement.querySelector(`[slot='help-text']`); helpText.icon = this.checked; helpText.textContent = this.checked ? 'Choose actual fruit(s).' : 'One of these is not a fruit.'; helpText.variant = this.checked ? 'negative' : 'neutral'; " >
    Lettuce
  </sp-checkbox>
  <sp-checkbox value="strawberry" checked>Strawberry</sp-checkbox>
  <sp-help-text slot="help-text">One of these is not a fruit.</sp-help-text>
</sp-field-group><sp-field-label for="vertical">
  Choose from vertically placed options
</sp-field-label>
<sp-field-group vertical id="vertical">
  <sp-checkbox>Checkbox 1</sp-checkbox>
  <sp-checkbox>Checkbox 2</sp-checkbox>
  <sp-checkbox>Checkbox 3</sp-checkbox>
  <sp-checkbox>Checkbox 4</sp-checkbox>
  <sp-checkbox checked>Checkbox 5</sp-checkbox>
</sp-field-group>
When a group of checkboxes fails validation, use the `invalid` attribute on the field group along with `negative-help-text` to explain the error. Set the `invalid` attribute on individual checkboxes as well to apply the appropriate visual styling.

**Important:** Both the `<sp-field-group>` and its child elements must be marked as `invalid` for the complete invalid state to display correctly:

*   The `invalid` attribute on `<sp-field-group>` controls help text visibility (showing the `negative-help-text` slot).
*   The `invalid` attribute on each child element (e.g., `<sp-checkbox>`) controls the visual invalid styling on that element.

Setting only one creates a sync hazard where either the help text won't display or the child elements won't show invalid styling.

<sp-field-group vertical label="Required selections" invalid>
  <sp-checkbox invalid>Option A</sp-checkbox>
  <sp-checkbox invalid>Option B</sp-checkbox>
  <sp-checkbox invalid>Option C</sp-checkbox>
  <sp-help-text slot="negative-help-text" icon>
    Select at least one option to continue.
  </sp-help-text>
</sp-field-group>
Every field group should have a label. A field without a label is ambiguous and not accessible.

The description in the help text is flexible and encompasses a range of guidance. Sometimes this guidance is about what to input, and sometime it’s about how to input. This includes information such as:

*   An overall description of the input field
*   Hints for what kind of information needs to be input
*   Specific formatting examples or requirements

Learn more about using help text.

Write error messaging in a human-centered way by guiding a user and showing them a solution — don’t simply state what’s wrong and then leave them guessing as to how to resolve it. Ambiguous error messages can be frustrating and even shame-inducing for users. Also, keep in mind that something that a system may deem an error may not actually be perceived as an error to a user.

Learn more about writing error messages.

Putting instructions for how to complete an input, requirements, or any other essential information into placeholder text is not accessible. Once a value is entered, placeholder text is no longer viewable; if someone is using an automatic form filler, they will never get the information in the placeholder text.

Instead, use the help text description to convey requirements or to show any formatting examples that would help user comprehension. If there's placeholder text and help text at the same time, it becomes redundant and distracting, especially if they're communicating the same thing.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/help-text@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/help-text@1.11.1

*   Updated dependencies [`7af5e8f`, `9cb816b`]: 
    *   @spectrum-web-components/help-text@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/help-text@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies [`72d807c`]: 
    *   @spectrum-web-components/help-text@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies [`165a904`]: 
    *   @spectrum-web-components/help-text@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   **field-group:** apply role when none present (3616199)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   apply "HelpTextMixin" to form elements (a952447)
*   include the "types" entry in package.json files (b432f59)
*   reduce cycles (66a4efb)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update to latest spectrum-css packages (a5ca19f)

*   **action-button:** add action button pattern (03ac00a)
*   add t-shirt sizing to the Radio pattern (fc49343)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **field-group:** add field-group pattern (f8d265c)
*   **field-group:** update spectrum css input (b2160a9)
*   **field-group:** use core tokens (7433e59)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   **field-group:** use core tokens (7433e59)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   add t-shirt sizing to the Radio pattern (fc49343)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   apply "HelpTextMixin" to form elements (a952447)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   reduce cycles (66a4efb)

**Note:** Version bump only for package @spectrum-web-components/field-group

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/field-group

**Note:** Version bump only for package @spectrum-web-components/field-group

*   include the "types" entry in package.json files (b432f59)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)

*   **action-button:** add action button pattern (03ac00a)
*   **field-group:** add field-group pattern (f8d265c)
*   **field-group:** update spectrum css input (b2160a9)

*   include the "types" entry in package.json files (b432f59)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)

*   **action-button:** add action button pattern (03ac00a)
*   **field-group:** add field-group pattern (f8d265c)
*   **field-group:** update spectrum css input (b2160a9)

Property  Attribute  Type  Default  Description `horizontal``horizontal``boolean``false``invalid``invalid``boolean``false``label``label``string``''``vertical``vertical``boolean``false`

Name  Description `default slot` the form controls that make up the group `help-text` default or non-negative help text to associate to your form element `negative-help-text` negative help text to associate to your form element when `invalid`
