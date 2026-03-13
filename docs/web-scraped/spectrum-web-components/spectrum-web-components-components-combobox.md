# Source: https://opensource.adobe.com/spectrum-web-components/components/combobox/

Title: Combobox: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/combobox/

Markdown Content:
An `<sp-combobox>` allows users to filter lists to only the options matching a query. It's composed of a textfield, a picker button, and child menu items.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/combobox?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/combobox?style=for-the-badge)

yarn add @spectrum-web-components/combobox

Import the side effectful registration of `<sp-combobox>` via:

import '@spectrum-web-components/combobox/sp-combobox.js';

When looking to leverage the `Combobox` base class as a type and/or for extension purposes, do so via:

import { Combobox } from '@spectrum-web-components/combobox';

Combobox options are presented as a popup menu. Menu items can be provided via markup as `<sp-menu-item>` children, or by assigning an array to the `options` property of an `<sp-combobox>`.

Instead of providing `<sp-menu-item>` children, you can assign an array of `ComboboxOptions` to the `options` property, and `<sp-combobox>` will create matching menu items:

<sp-combobox id="color" label="Color"></sp-combobox>

<script> document.getElementById('color').options = [ { value: "red", itemText: "Red" }, { value: "green", itemText: "Green" }, { value: "blue", itemText: "Blue" } ];</script>
When you replace the `options` Array, or add/remove `<sp-menu-item>` children, the `<sp-combobox>` will detect that change and update its popup menu contents. For example, using Lit:

render() {
    return html`<sp-combobox label="Color" .options=${this.colorOptions}></sp-combobox>`;
}

mutate() {
    this.colorOptions = [
        ...this.colorOptions,
        { value: 'purple', itemText: 'Purple' }
    ];
}Small<sp-combobox size="s" label="Color">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>Medium<sp-combobox size="m" label="Color">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>Large<sp-combobox size="l" label="Color">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>Extra Large<sp-combobox size="xl" label="Color">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox><sp-field-label for="color">Color</sp-field-label>
<sp-combobox id="color" quiet>
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>
The text in an `<sp-combobox>` is editable, and the string the user has typed in will become the `value` of the combobox unless the user selects a different value in the popup menu.

`autocomplete="none"`

The suggested popup menu items will remain the same regardless of the currently-input value. Whenever the currently-typed input exactly matches the `value` of a popup menu item, that item is automatically selected.

<sp-field-label for="color-none" autocomplete="none">Color</sp-field-label>
<sp-combobox id="color-none">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>
`autocomplete="list"`

The popup menu items are filtered to only those completing the currently-input value.

<sp-field-label for="color-list" autocomplete="list">Color</sp-field-label>
<sp-combobox id="color-list">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>Disabled<sp-field-label for="color-disabled">Color</sp-field-label>
<sp-combobox id="color-disabled" disabled>
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>
<br />
<sp-field-label for="color-disabled-item">Color</sp-field-label>
<sp-combobox id="color">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue" disabled>Blue</sp-menu-item>
</sp-combobox>Invalid<sp-field-label for="color-invalid">Color</sp-field-label>
<sp-combobox id="color-invalid" invalid>
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
  <sp-help-text slot="negative-help-text">
    Choose or add at least one color.
  </sp-help-text>
</sp-combobox>Pending<sp-field-label for="color">Color</sp-field-label>
<sp-combobox id="color" pending>
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>
A combobox must be labeled. Typically, you should render a visible label via `<sp-field-label>`. For exceptional cases, provide an accessible label via the `label` attribute.

<sp-field-label for="color">Color</sp-field-label>
<sp-combobox id="color">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>
It is not currently possible to provide accessible ARIA references between elements in different shadow roots. To ensure proper association between elements, help text must be included via the `slot="help-text"` or `slot="negative-help-text"` and tooltips must be included via the `slot="tooltip"`.

See help text and tooltip for more information.

Help text<sp-field-label for="color1">Color</sp-field-label>
<sp-combobox id="color1">
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
  <sp-help-text slot="help-text">Enter the name of a color.</sp-help-text>
</sp-combobox>Negative help text<sp-field-label for="color2">Color</sp-field-label>
<sp-combobox id="color2" required>
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
  <sp-help-text slot="help-text">Enter the name of a color.</sp-help-text>
  <sp-help-text slot="negative-help-text">A color is required.</sp-help-text>
</sp-combobox>Tooltip<sp-field-label for="color3">Color</sp-field-label>
<sp-combobox id="color3">
  <sp-tooltip slot="tooltip">
    Color options, such as red, green, or blue.
  </sp-tooltip>
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
</sp-combobox>
The combobox supports both mouse and keyboard navigation. Mobile behavior is currently unspecified.

When an `<sp-combobox>` is focused, pressing the down arrow moves focus to the first menu item in the popup menu. The up and down arrows then move between available menu items.

The escape key dismisses the popup menu if open. Otherwise, it clears the combobox's textfield.

The enter key sets the `value` of the focused `<sp-combobox>`. If the popup menu is open, the value is set to the `value` of the selected menu item, returning focus back to the combobox's textfield.

For comprehensive information on combobox accessibility, see WAI ARIA Authoring Practice Guide's Menu Button Pattern.

*   Updated dependencies []: 
    *   @spectrum-web-components/progress-circle@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/menu@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/action-button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/overlay@1.11.2
    *   @spectrum-web-components/picker-button@1.11.2
    *   @spectrum-web-components/popover@1.11.2
    *   @spectrum-web-components/textfield@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/progress-circle@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/menu@1.11.1
    *   @spectrum-web-components/overlay@1.11.1
    *   @spectrum-web-components/picker-button@1.11.1
    *   @spectrum-web-components/textfield@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/popover@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`eac97a2`, `b95e254`, `02b2d7d`, `f07344f`, `1d76b70`, `b95e254`, `cadc39e`, `4cb0b7b`, `9cb816b`]: 
    *   @spectrum-web-components/menu@1.11.0
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/textfield@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/popover@1.11.0
    *   @spectrum-web-components/progress-circle@1.11.0
    *   @spectrum-web-components/action-button@1.11.0
    *   @spectrum-web-components/picker-button@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/menu@1.10.0
    *   @spectrum-web-components/overlay@1.10.0
    *   @spectrum-web-components/picker-button@1.10.0
    *   @spectrum-web-components/popover@1.10.0
    *   @spectrum-web-components/progress-circle@1.10.0
    *   @spectrum-web-components/textfield@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies [`a19cbe3`]: 
    *   @spectrum-web-components/overlay@1.9.1
    *   @spectrum-web-components/menu@1.9.1
    *   @spectrum-web-components/popover@1.9.1
    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/picker-button@1.9.1
    *   @spectrum-web-components/progress-circle@1.9.1
    *   @spectrum-web-components/textfield@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1

*   #5730`7d23140` Thanks @caseyisonit! - - **Fixed**: Pending state handling and accessibility in `<sp-combobox>` component.

    *   **Changed**: Removed dependency on `PendingStateController` and implemented inline pending state handling
    *   **Fixed**: Updated aria-labelledby attribute ordering to improve screen reader experience (`label applied-label pending-label`)
    *   **Fixed**: Updated progress circle implementation to use `role="presentation"` instead of `aria-valuetext`
    *   **Added**: Direct pending state visual rendering with improved accessibility

These changes improve accessibility for pending states while reducing unnecessary component dependencies.

*   Updated dependencies [`4880da4`, `72d807c`, `14ebeb9`, `7d23140`, `7d23140`]:

    *   @spectrum-web-components/menu@1.9.0
    *   @spectrum-web-components/textfield@1.9.0
    *   @spectrum-web-components/progress-circle@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/picker-button@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/overlay@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/popover@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   #5538`cc6e91e` Thanks @tjgupta! - Replace the use of offsetWidth with a resizeObserver to avoid unecessary, performance-impacting layout reflows.

*   Updated dependencies [`14486d6`, `f27ab09`, `ee1bae6`, `14486d6`]:

    *   @spectrum-web-components/overlay@1.8.0
    *   @spectrum-web-components/menu@1.8.0
    *   @spectrum-web-components/popover@1.8.0
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/picker-button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/progress-circle@1.8.0
    *   @spectrum-web-components/textfield@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0

*   Updated dependencies [`3aeafdd`, `a646ae8`, `c1669d2`, `cde976d`]: 
    *   @spectrum-web-components/menu@1.7.0
    *   @spectrum-web-components/overlay@1.7.0
    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/textfield@1.7.0
    *   @spectrum-web-components/popover@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/picker-button@1.7.0
    *   @spectrum-web-components/progress-circle@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies [`03a4439`, `9e15a66`, `a9727d2`, `53f3769`]: 
    *   @spectrum-web-components/popover@1.6.0
    *   @spectrum-web-components/textfield@1.6.0
    *   @spectrum-web-components/menu@1.6.0
    *   @spectrum-web-components/overlay@1.6.0
    *   @spectrum-web-components/action-button@1.6.0
    *   @spectrum-web-components/picker-button@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/progress-circle@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   #5202`fa4be70` Thanks @Rajdeepc! - Updates the combobox component from version 4.0.0-s2-foundations.21 to 4.1.2. This work also addresses the design feedback for combobox in S2 foundations: 
    *   corrects the border colors for several combobox states including focus, keyboardFocus, focus+hover, disabled, read-only for all themes
    *   increases the specificity of the `#textfield:hover .input` selector to `#textfield:hover .input:focus` in order to properly render the focus+hover border color styles (within the `combobox.css` file)
    *   adds an additional selector for disabled comboboxes that correctly renders the border colors based on theme context

*   Updated dependencies [`86bcd12`, `fa4be70`, `8f8735c`, `6c58f50`, `4c2f908`, `a69accb`]: 
    *   @spectrum-web-components/menu@1.5.0
    *   @spectrum-web-components/picker-button@1.5.0
    *   @spectrum-web-components/overlay@1.5.0
    *   @spectrum-web-components/action-button@1.5.0
    *   @spectrum-web-components/textfield@1.5.0
    *   @spectrum-web-components/popover@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/progress-circle@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies [`2a0422e`, `72dbe62`, `46cd782`, `6618422`, `70f5f6f`]: 
    *   @spectrum-web-components/menu@1.4.0
    *   @spectrum-web-components/action-button@1.4.0
    *   @spectrum-web-components/overlay@1.4.0
    *   @spectrum-web-components/popover@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/picker-button@1.4.0
    *   @spectrum-web-components/progress-circle@1.4.0
    *   @spectrum-web-components/textfield@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies [`ea38ef0`, `468314f`]: 
    *   @spectrum-web-components/menu@1.3.0
    *   @spectrum-web-components/overlay@1.3.0
    *   @spectrum-web-components/popover@1.3.0
    *   @spectrum-web-components/action-button@1.3.0
    *   @spectrum-web-components/picker-button@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/progress-circle@1.3.0
    *   @spectrum-web-components/textfield@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **action menu:** keyboard accessibility omnibus (#5031) (ea38ef0), closes #4623

*   **combobox:** allow support for disabled items (#5104) (b78d412)

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   add an optional chromatic vrt action (7d2f840)

*   **overlay:** overlay scroll in safari and firefox (#4969) (05d24ff)

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

*   **combobox:** update selected item state in menu (#4730) (c4cfd2a)

*   **reactive-controller:** new pending state controller (#4605) (68baf94)

**Note:** Version bump only for package @spectrum-web-components/combobox

*   **reactive-controllers:** update focusable element's tab-index to 0 on accepting focus (#4630) (d359e84)

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

*   **combobox:** add `pending` state (#4462) (2d0c388)

**Note:** Version bump only for package @spectrum-web-components/combobox

*   **combobox:** allow numeric values and trigger change event on keybo… (#4405) (235ae7c)
*   **combobox:** correct package.json listings (35a69a2)
*   **combobox:** process styles for invalid state (#4344) (c2b952e)

*   **combobox:** correct package.json listings (35a69a2)

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/combobox

**Note:** Version bump only for package @spectrum-web-components/combobox

*   **icon:** use core tokens (a11ef6b)

*   **combobox:** prevent initial list render and update tests to prove that reduces render time (3dc5b1f)

*   **combobox:** add combobox pattern (#3894) (47d7d71), closes #3887

 Property  Attribute  Type  Default  Description `allowedKeys``allowed-keys``string``''` A regular expression outlining the keys that will be allowed to update the value of the form control. `autocomplete``autocomplete``| 'list' | 'none' | HTMLInputElement['autocomplete'] | HTMLTextAreaElement['autocomplete'] | undefined``'none'` What form of assistance should be provided when attempting to supply a value to the form control 
Note: combobox overrides `autocomplete` intentionally with `aria-autocomplete` values, which is why those values (although invalid for native `autocomplete`) are included here to support the combobox accessibility pattern.

`disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `grows``grows``boolean``false` Whether a form control delivered with the `multiline` attribute will change size vertically to accomodate longer input `invalid``invalid``boolean``false` Whether the `value` held by the form control is invalid. `label``label``string``''` A string applied via `aria-label` to the form control when a user visible label is not provided. `maxlength``maxlength``number``-1` Defines the maximum string length that the user can enter `minlength``minlength``number``-1` Defines the minimum string length that the user can enter `multiline``multiline``boolean``false` Whether the form control should accept a value longer than one line `name``name``string | undefined` Name of the form control. `open``open``boolean``false` Whether the listbox is visible. `options``options``(ComboboxOption | MenuItem)[] | undefined` An array of options to present in the Menu provided while typing into the input `pattern``pattern``string | undefined` Pattern the `value` must match to be valid `pending``pending``boolean``false` Whether the items are currently loading. `pendingLabel``pending-label``string``'Pending'` Defines a string value that labels the Combobox while it is in pending state. `placeholder``placeholder``string``''` Text that appears in the form control when it has no value set `quiet``quiet``boolean``false` Whether to display the form control with no visible background `readonly``readonly``boolean``false` Whether a user can interact with the value of the form control `required``required``boolean``false` Whether the form control will be found to be invalid when it holds no `value` `rows``rows``number``-1` The specific number of rows the form control should provide in the user interface `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `valid``valid``boolean``false` Whether the `value` held by the form control is valid. `value``value``string | number` The value held by the form control 

Name  Description `default slot` Supply Menu Item elements to the default slot in order to populate the available options `help-text` default or non-negative help text to associate to your form element `negative-help-text` negative help text to associate to your form element when `invalid` `tooltip` Tooltip to to be applied to the the Picker Button

Name  Type  Description `change``Event``An alteration to the value of the element has been committed by the user.``input``Event``The value of the element has changed.`
