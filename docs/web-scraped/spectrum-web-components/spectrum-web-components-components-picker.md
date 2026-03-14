# Source: https://opensource.adobe.com/spectrum-web-components/components/picker/

Title: Picker: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/picker/

Markdown Content:
Overview API Changelog
An `<sp-picker>` is an alternative to HTML's `<select>` element. Use `<sp-menu-item>` elements to outline the options that will be made available to the user when interacting with the `<sp-picker>` element.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/picker?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/picker?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/picker
Import the side effectful registration of `<sp-picker>` via:

import '@spectrum-web-components/picker/sp-picker.js';
The default of `<sp-picker>` will load dependencies in `@spectrum-web-components/overlay` asynchronously via a dynamic import. In the case that you would like to import those tranverse dependencies statically, import the side effectful registration of `<sp-picker>` as follows:

import '@spectrum-web-components/picker/sync/sp-picker.js';
When looking to leverage the `Picker` base class as a type and/or for extension purposes, do so via:

import { Picker } from '@spectrum-web-components/picker';
A picker includes a label and a menu.

To render accessibly, an `<sp-picker>` element should be paired with an `<sp-field-label>` element that has the `for` attribute referencing the `id` of the `<sp-picker>` element.

For an accessible label that renders within the bounds of the picker itself, but still fulfills the accessibility contract, use the `label` attribute or a `<span slot="label">` as a child element of `<sp-picker>`.

Uses <sp-field-label><sp-field-label for="uses-sp-field-label">Selection type:</sp-field-label>
<sp-picker id="uses-sp-field-label">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Uses label attribute<sp-picker label="Selection type" id="uses-label-attribute">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Uses label slot<sp-picker id="uses-label-slot">
  <span slot="label">Selection type:</span>
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>
The picker menu is a menu element that is used to display the options for the picker. A picker menu can include menu items, menu dividers, and menu groups. A picker menu should never contain submenus, as doing so would render it inaccessible.

If you require a submenu, use and action menu instead of a picker.

<sp-picker>
    <span slot="label">Select a free food item:</span>
    <sp-menu-group>
        <span slot="header">Fruits</span>
        <sp-menu-item>Apple</sp-menu-item>
        <sp-menu-item>Banana</sp-menu-item>
        <sp-menu-item>Pear</sp-menu-item>
    </sp-menu-group>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-group>
        <span slot="header">Vegetables</span>
        <sp-menu-item>Artichoke</sp-menu-item>
        <sp-menu-item>Carrot</sp-menu-item>
        <sp-menu-item>Potato</sp-menu-item>
    </sp-menu-group>
    <sp-menu-group>
</sp-picker>
`<sp-menu-item>`s in an `<sp-picker>` that are provided content addressed to their `icon` slot will be passed to the `<sp-picker>` element when that item is chosen.

<sp-field-label for="picker-icons">Choose an action...</sp-field-label>
<sp-picker label="What would you like to do?" value="item-2" id="picker-icons">
  <sp-menu-item>
    <sp-icon-save-floppy slot="icon"></sp-icon-save-floppy>
    Save
  </sp-menu-item>
  <sp-menu-item>
    <sp-icon-stopwatch slot="icon"></sp-icon-stopwatch>
    Finish
  </sp-menu-item>
  <sp-menu-item>
    <sp-icon-user-activity slot="icon"></sp-icon-user-activity>
    Review
  </sp-menu-item>
</sp-picker>
When using `<sp-menu-item>` elements without text content, be sure to use the `value` attribute so that the `<sp-picker>` element can differentiate between the available options. Furthermore, it is important to apply accessible labeling to the `[slot="icon"]` content as follows:

<sp-field-label for="picker-icons-only">Choose an action...</sp-field-label>
<sp-picker label="What would you like to do?" value="item-2" id="picker-icons-only">
  <sp-menu-item value="item-1">
    <sp-icon-save-floppy slot="icon" label="Save"></sp-icon-save-floppy>
  </sp-menu-item>
  <sp-menu-item value="item-2">
    <sp-icon-stopwatch slot="icon" label="Finish"></sp-icon-stopwatch>
  </sp-menu-item>
  <sp-menu-item value="item-3">
    <sp-icon-user-activity slot="icon" label="Review"></sp-icon-user-activity>
  </sp-menu-item>
</sp-picker>
The `icons` attribute manages how the selected item will appear. Set `icons="only"` to display only the selected item's icon in the `<sp-picker>` element, or `icons="none"` to display the selected item text without the icon `<sp-picker>`.

When using `icons="only"` on `<sp-menu-item>` elements that have text content, that text will be applied to `<sp-picker>` element in a non-visible way.

Only<sp-field-label for="picker-icons-value">Choose an action...</sp-field-label>
<sp-picker label="What would you like to do?" value="save" id="picker-icons-value" icons="only">
  <sp-menu-item value="save">
    <sp-icon-save-floppy slot="icon"></sp-icon-save-floppy>
    Save
  </sp-menu-item>
  <sp-menu-item value="finish">
    <sp-icon-stopwatch slot="icon"></sp-icon-stopwatch>
    Finish
  </sp-menu-item>
  <sp-menu-item value="review">
    <sp-icon-user-activity slot="icon"></sp-icon-user-activity>
    Review
  </sp-menu-item>
</sp-picker>None<sp-field-label for="picker-icons-none">Choose an action...</sp-field-label>
<sp-picker label="What would you like to do?" value="save" id="picker-icons-none" icons="none">
  <sp-menu-item value="save">
    <sp-icon-save-floppy slot="icon"></sp-icon-save-floppy>
    Save
  </sp-menu-item>
  <sp-menu-item value="finish">
    <sp-icon-stopwatch slot="icon"></sp-icon-stopwatch>
    Finish
  </sp-menu-item>
  <sp-menu-item value="review">
    <sp-icon-user-activity slot="icon"></sp-icon-user-activity>
    Review
  </sp-menu-item>
</sp-picker>
When the `value` of an `<sp-picker>` matches either the `value` attribute or the trimmed `textContent` (or `itemText`) of a descendent `<sp-menu-item>`, it will mark that element as `selected`.

Matching value<sp-field-label for="picker-value">Selection type:</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" value="item-2" id="picker-value">
  <sp-menu-item value="item-1">Deselect</sp-menu-item>
  <sp-menu-item value="item-2">Select inverse</sp-menu-item>
  <sp-menu-item value="item-3">Feather...</sp-menu-item>
  <sp-menu-item value="item-4">Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item value="item-5">Save selection</sp-menu-item>
  <sp-menu-item disabled value="item-6">Make work path</sp-menu-item>
</sp-picker>Matching itemText<sp-field-label for="picker-item-text">Selection type:</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" value="Feather..." id="picker-item-text">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item>Make work path</sp-menu-item>
</sp-picker>Small<sp-field-label for="picker-s" size="s">Selection type:</sp-field-label>
<sp-picker id="picker-s" size="s" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>
<br />
<br />
<sp-field-label for="picker-s-quiet" size="s">Selection type:</sp-field-label>
<sp-picker id="picker-s-quiet" quiet size="s" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Medium<sp-field-label for="picker-m" size="m">Selection type:</sp-field-label>
<sp-picker id="picker-m" size="m" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>
<br />
<br />
<sp-field-label for="picker-m-quiet" size="m">Selection type:</sp-field-label>
<sp-picker id="picker-m-quiet" quiet size="m" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Large<sp-picker id="picker-l" size="l" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>
<br />
<br />
<sp-field-label for="picker-l-quiet" size="l">Selection type:</sp-field-label>
<sp-picker id="picker-l-quiet" quiet size="l" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Extra Large<sp-field-label for="picker-xl" size="xl">Selection type:</sp-field-label>
<sp-picker id="picker-xl" size="xl" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>
<br />
<br />
<sp-field-label for="picker-xl-quiet" size="xl">Selection type:</sp-field-label>
<sp-picker id="picker-xl-quiet" quiet size="xl" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Side label, standard<sp-field-label side-aligned="start" for="picker-sideLabel">
  Standard:
</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" id="picker-sideLabel">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Side label, quiet<sp-field-label side-aligned="start" for="picker-sideLabel-quiet">
  Quiet:
</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" quiet id="picker-sideLabel-quiet">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Invalid, standard<sp-field-label for="picker-invalid">Standard:</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" invalid id="picker-invalid">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Invalid, quiet<sp-field-label for="picker-invalid-quiet">Quiet:</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" invalid quiet id="picker-invalid-quiet">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Disabled, standard<sp-field-label for="picker-disabled">Standard:</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" disabled id="picker-disabled">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>Disabled, quiet<sp-field-label for="picker-disabled-quiet">Quiet:</sp-field-label>
<sp-picker label="Select a Country with a very long label, too long in fact" disabled quiet id="picker-disabled-quiet">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-picker>
While in pending state, `<sp-picker>` elements will not respond to click events and will be delivered with `<sp-progress-circle>` to visually denote that it is pending. It will not toggle open or display its `<sp-menu-item>` descendants until the attribute is removed. Use the `pending-label` attribute to customize the pending text for assoistive technology, which is set to `Pending` by default.

Pending, standard<sp-field-label for="picker-loading">Standard:</sp-field-label>
<sp-picker id="picker-loading" label="Loading blending modes..." pending pending-label="loading options">
  <sp-menu-item>Pass through</sp-menu-item>
  <sp-menu-item>Normal</sp-menu-item>
  <sp-menu-item>Multiply</sp-menu-item>
  <sp-menu-item>Screen</sp-menu-item>
</sp-picker>Pending, quiet<sp-field-label for="picker-loading-quiet">Quiet:</sp-field-label>
<sp-picker id="picker-loading-quiet" label="Loading blending modes..." pending quiet>
  <sp-menu-item>Pass through</sp-menu-item>
  <sp-menu-item>Normal</sp-menu-item>
  <sp-menu-item>Multiply</sp-menu-item>
  <sp-menu-item>Screen</sp-menu-item>
</sp-picker>
On mobile, the menu can be exposed in either a `sp-popover` or `sp-tray`. By default, `sp-picker` will render an `sp-tray`. If you would like to render `sp-popover` on mobile, add the attribute `force-popover` to the `sp-picker`.

Usage Guidance:

*   Use a tray when a menu’s proximity to its trigger is considered to be less important to the experience, or for showing a volume of content that is too overwhelming for a popover.
*   Use a popover when a menu’s proximity to its trigger is considered to be important to the experience, or for showing a volume of content that is manageable for a popover.

To see this functionality in action, load this page from your mobile device or use Chrome DevTools (or equivalent) and select a mobile device once the Device Toolbar (the phone/tablet icon) is active.

<sp-field-label for="picker-tray">
  Do you want to see a tray menu?
</sp-field-label>
<sp-picker id="picker-tray" label="Select an option">
  <sp-menu-item value="option-1">Yes</sp-menu-item>
  <sp-menu-item value="option-2">No</sp-menu-item>
</sp-picker>
<br />
<sp-field-label for="picker-popover">
  Do you want to see a popover menu?
</sp-field-label>
<sp-picker id="picker-popover" label="Select an option" force-popover>
  <sp-menu-item value="option-1">Yes</sp-menu-item>
  <sp-menu-item value="option-2">No</sp-menu-item>
</sp-picker>
Every picker should have a label. A picker without a label is ambiguous and not accessible.

A picker’s description in the help text can communicate what to select or how to select an option. This includes information such as:

*   An overall description of the picker options
*   Hints for what kind of information to choose
*   More context for why a user needs to make a selection

The help text’s message should not simply restate the same information in the label in order to prompt someone to interact with a picker. Don’t add help text to maintain layout continuity with other inputs that require help text if it isn’t actually relevant or meaningful to a user.

The help text area also displays an error message. When a picker already includes help text and an error is triggered, the help text is replaced with error text. Once the error is resolved, the help text description reappears below the picker.

Since one gets replaced by the other, the language of the help text and error text need to work together to convey the same messaging. Help text explains the requirement or adds supplementary context for how to complete the interaction. Error text tells a user how to fix the error by re-stating the selection requirements or describing the necessary interaction. Make sure that the help text and the error text include the same essential information so that it isn’t lost if one replaces the other (e.g., minimum requirements).

Use `<sp-help-text>` to add help text and error text:

Help text<sp-field-label for="text">Preferred contact method:</sp-field-label>
<sp-picker id="text" label="Select contact method" aria-describedby="help-text">
  <sp-menu-item>Phone</sp-menu-item>
  <sp-menu-item>Text</sp-menu-item>
  <sp-menu-item>Email</sp-menu-item>
</sp-picker>
<sp-help-text id="help-text">
  Choose the best way to contact you in case there's an issue with your account.
</sp-help-text>Error text<sp-field-label for="error-text" required invalid>
  Preferred contact method:
</sp-field-label>
<sp-picker id="error-text" invalid label="Select contact method" required aria-describedby="error-help-text">
  <sp-menu-item>Phone</sp-menu-item>
  <sp-menu-item>Text</sp-menu-item>
  <sp-menu-item>Email</sp-menu-item>
</sp-picker>
<sp-help-text id="error-help-text" variant="negative">
  Select a contact method.
</sp-help-text>
A picker menu should never contain submenus, as doing so would render it inaccessible. A picker's menu role is a listbox, and its menu items are listbox options, which are not allowed to have submenus.

*   #5972`3783d87` Thanks @rubencarvalho! - **Fixed** issue where Picker component doesn't show label when value is set before menu-items are rendered. When menu-items are added later (e.g., conditionally rendered with Lit's `when()` directive or lazy loaded), the Picker now preserves the value and correctly displays the label once menu-items become available.

This fix ensures the value is preserved when `manageSelection()` runs before menu-items exist or when items exist but don't have values yet (e.g., during async custom element upgrade). The value is only cleared when menu-items with meaningful values exist but none match the picker's value.

*   Updated dependencies []:

    *   @spectrum-web-components/progress-circle@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/menu@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/field-label@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2
    *   @spectrum-web-components/overlay@1.11.2
    *   @spectrum-web-components/popover@1.11.2
    *   @spectrum-web-components/tooltip@1.11.2
    *   @spectrum-web-components/tray@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/progress-circle@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/field-label@1.11.1
    *   @spectrum-web-components/menu@1.11.1
    *   @spectrum-web-components/overlay@1.11.1
    *   @spectrum-web-components/tooltip@1.11.1
    *   @spectrum-web-components/tray@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1
    *   @spectrum-web-components/popover@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5901`ae61361` Thanks @iuliauta! - **Fixed**: click events are now dispatched from menu-items on touch devices

    *   All touch devices (including iPads with screen widths >743px) now correctly use click events instead of drag-and-select behavior

*   #5965`b95e254` Thanks @rubencarvalho! - **Fixed**: Arrow key events now stop propagation when handled by the picker, preventing them from bubbling up to parent elements.

Previously, arrow key events (`ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`) would propagate to ancestor containers even when the picker was actively handling them. This could cause unintended side effects in layouts or applications that also listen for arrow key events.

*   #5868`f07344f` Thanks @Rajdeepc! - **Fixed** issue where picker menus inside overlays could not scroll to the bottom after selecting an item and reopening. The problem was caused by the overlay's placement calculation happening before the menu fully rendered, resulting in incorrect height measurements.

This fix ensures picker menus maintain proper scrollable height when reopened, regardless of the selected item's position.

*   #5983`2732aad` Thanks @rubencarvalho! - **Fixed**: Safari + VoiceOver crash when opening Picker and ActionMenu. The issue was caused by an imperative `render()` call that mutated the DOM during the render cycle, causing Safari to crash while VoiceOver scanned the accessibility tree.

*   Updated dependencies [`7af5e8f`, `eac97a2`, `b95e254`, `02b2d7d`, `6b887f2`, `f07344f`, `1d76b70`, `f8bdeec`, `b95e254`, `cadc39e`, `e780f82`, `4cb0b7b`, `9cb816b`]:

    *   @spectrum-web-components/field-label@1.11.0
    *   @spectrum-web-components/menu@1.11.0
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/tray@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/tooltip@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/popover@1.11.0
    *   @spectrum-web-components/progress-circle@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/field-label@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/menu@1.10.0
    *   @spectrum-web-components/overlay@1.10.0
    *   @spectrum-web-components/popover@1.10.0
    *   @spectrum-web-components/progress-circle@1.10.0
    *   @spectrum-web-components/tooltip@1.10.0
    *   @spectrum-web-components/tray@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies [`a19cbe3`]: 
    *   @spectrum-web-components/overlay@1.9.1
    *   @spectrum-web-components/menu@1.9.1
    *   @spectrum-web-components/popover@1.9.1
    *   @spectrum-web-components/tooltip@1.9.1
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/field-label@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/progress-circle@1.9.1
    *   @spectrum-web-components/tray@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5733`dbba861` Thanks @iuliauta! - - **Fixed**: Picker border color should be hidden in S2 theme

*   #5730`7d23140` Thanks @caseyisonit! - - **Fixed**: Pending state handling and accessibility in `<sp-picker>` component.

    *   **Changed**: Removed dependency on `PendingStateController` and implemented inline pending state handling
    *   **Fixed**: Updated aria-labelledby attribute ordering to improve screen reader experience (`icon label applied-label pending-label`)
    *   **Fixed**: Updated progress circle implementation to use `role="presentation"` instead of `aria-valuetext`
    *   **Added**: Direct pending state visual rendering with improved accessibility

These changes improve accessibility for pending states while reducing unnecessary component dependencies.

*   Updated dependencies [`7d23140`, `4880da4`, `bdf54c1`, `7d23140`, `7d23140`, `72d807c`]:

    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/menu@1.9.0
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/progress-circle@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/field-label@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/overlay@1.9.0
    *   @spectrum-web-components/tooltip@1.9.0
    *   @spectrum-web-components/tray@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/popover@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   #5672`6c2acaf` Thanks @Rajdeepc! - **Fixed** escape key behavior in modal overlays containing picker components. Previously, pressing the Escape key when a picker was open inside a modal overlay would not properly close the modal, instead moving focus to the picker. Now, the escape key correctly closes the picker first (if open), then closes the modal overlay on subsequent escape key presses.

This fix adds a check for `this.open` in the picker's `handleEscape` method to ensure proper modal overlay closure behavior.

*   Updated dependencies [`14486d6`, `f27ab09`, `ee1bae6`, `15be17d`, `14486d6`]: 
    *   @spectrum-web-components/overlay@1.8.0
    *   @spectrum-web-components/menu@1.8.0
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/popover@1.8.0
    *   @spectrum-web-components/tooltip@1.8.0
    *   @spectrum-web-components/field-label@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/progress-circle@1.8.0
    *   @spectrum-web-components/tray@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies [`3aeafdd`, `a646ae8`, `cde976d`]: 
    *   @spectrum-web-components/menu@1.7.0
    *   @spectrum-web-components/overlay@1.7.0
    *   @spectrum-web-components/tooltip@1.7.0
    *   @spectrum-web-components/popover@1.7.0
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/field-label@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/progress-circle@1.7.0
    *   @spectrum-web-components/tray@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5358`3c3bc2b` Thanks @nikkimk! - `PickerBase`(used in `<sp-picker>` and `sp-action-menu>`):

Fixes focus so that it is not set on `<sp-menu-item>` elements when opened via mouse.

A keyboard interaction is the only interaction that should set focus on an `<sp-menu-item>` when the menu is opened. A user with a mouse would expect the focus to stay where the mouse is.

Fixes: #2950

*   Updated dependencies [`03a4439`, `f6cebbd`, `00eb0a8`, `700489f`, `a9727d2`, `53f3769`]:

    *   @spectrum-web-components/popover@1.6.0
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/tooltip@1.6.0
    *   @spectrum-web-components/menu@1.6.0
    *   @spectrum-web-components/overlay@1.6.0
    *   @spectrum-web-components/field-label@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/progress-circle@1.6.0
    *   @spectrum-web-components/tray@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`86bcd12`, `165a904`, `4e06533`, `8f8735c`, `4c2f908`, `a69accb`]: 
    *   @spectrum-web-components/menu@1.5.0
    *   @spectrum-web-components/field-label@1.5.0
    *   @spectrum-web-components/tray@1.5.0
    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/overlay@1.5.0
    *   @spectrum-web-components/popover@1.5.0
    *   @spectrum-web-components/tooltip@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/progress-circle@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   #5187`2a0422e` Thanks @TarunAdobe! - Disabled drag and select functionality of picker in mobile devices. This is done to prevent click event being captured behind the menu-tray combination because the menu was closing immediately on pointerup.

    *   Fixed a bug where the picker in a dialog was not closing when clicking outside the dialog. (#5111)
    *   Fixed another bug where the elements behind the menu were receiving click events. (#5060)

*   #5247`1fc141c` Thanks @rubencarvalho! - fix: moved tooltip outside of the trigger button content which prevents event propagation issues and fixes CSS hover state problems by properly separating the tooltip from the button's content (it no longer is a direct child in the DOM).

*   #5213`82212f4` Thanks @Rajdeepc! - Updated the attribute name from `forcePopover` to `force-popover` in the Picker and Action menu documentation

*   Updated dependencies [`2a0422e`, `46cd782`, `6618422`, `70f5f6f`]:

    *   @spectrum-web-components/menu@1.4.0
    *   @spectrum-web-components/overlay@1.4.0
    *   @spectrum-web-components/popover@1.4.0
    *   @spectrum-web-components/tooltip@1.4.0
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/field-label@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/progress-circle@1.4.0
    *   @spectrum-web-components/tray@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   #5031`ea38ef0` Thanks @nikkimk! - Used WAI ARIA Authoring Practices Guide (APG) to make accessibility improvements for `<sp-action-menu>`, `<sp-menu>`, and `<sp-picker>`, including:

    *   Numpad keys now work with `<sp-picker>` and `<sp-action-menu>` -`<sp-action-menu>`'s `<sp-menu-item>` elements can now be read by a screen reader (#4556)
    *   `<sp-menu-item>` href can now be clicked by a screen reader (#4997)
    *   Opening a `<sp-action-menu>`, `<sp-menu>`, and `<sp-picker>` with a keyboard now sets focus on an item within the menu. (#4557)

See the following APG examples for more information:

    *   Navigation Menu Example
    *   Editor Menubar Example

*   Updated dependencies [`ea38ef0`, `468314f`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/menu@1.3.0
    *   @spectrum-web-components/overlay@1.3.0
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/field-label@1.3.0
    *   @spectrum-web-components/tooltip@1.3.0
    *   @spectrum-web-components/tray@1.3.0
    *   @spectrum-web-components/popover@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/progress-circle@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **action menu:** keyboard accessibility omnibus (#5031) (ea38ef0), closes #4623
*   **picker:** update picker when menu item icons change (#5088) (63ef1ad)

*   **overlay:** derive popover placement from host in interaction controller (#5078) (635cf53)
*   **picker:** stop the click events from reaching the elements below picker-tray (#5060) (7e4fdbf)

*   **overlay:** make :focus-visible consistent when using overlay type modal (#4912) (7a5f786), closes #5021

*   **picker:** add forcePopover property (#5041) (3651e57)

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)
*   **overlay:** make :focus-visible consistent when using overlay type modal (#4912) (7a5f786), closes #5021

*   add an optional chromatic vrt action (7d2f840)
*   **picker:** add forcePopover property (#5041) (3651e57)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** don't handle pointerdown for touch devices (#4850) (3a62d13)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **action-menu:** dispatch scroll event (#4715) (c76f3f5)
*   **picker:** added a custom class to make `:focus-visible` styles consistent across all browsers (#4724) (d667d08)

*   **reactive-controller:** new pending state controller (#4605) (68baf94)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** updated type for mobile and desktop (#4666) (d11da1f)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker** pointerup in mobile does not automatically make a selection. (4227) ([56366ce] (https://github.com/adobe/spectrum-web-components/commit/56366ce2750bb4bb5c6e3fa5fe7d809434497adb))

**Note:** Version bump only for package @spectrum-web-components/picker

*   **action-bar:** support for action-menus (#3780) (4aff599)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **action-menu:** allow menu groups to handle their own selections (#4397) (5a19051)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** add loading state to the picker (#3110) (d91e2c9)
*   **picker:** allow open/close in tablet (dcfc96e)
*   **picker:** correctly process the CSS for the quiet hover effect (#4167) (eb282fa)

*   **asset:** use core tokens (99e76f4)

*   **overlay:** leverage "transition-behavior" to persist top-layer content while closing (#4050) (e3dea14)
*   **picker:** support inline labeling of quiet Picker (#3704) (3372286)

*   **picker:** correct implementation of "disabled", expand stories and documentation (#4040) (84c2fef)

*   **icon:** use core tokens (a11ef6b)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker,action-menu,split-button:** update interaction model (#3935) (bae7d52)

*   **picker:** force close slotted Tooltip elements with disabled when Menu openes (82c8f12)
*   **picker:** prevent the Menu opening until required dependencies are loaded (55e6174)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** ensure menu placement in mobile (#3835) (4aba1c6)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **overlay:** calculate more transforms (6538a45)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker,split-button:** include "tooltip" slot in the main button (699b8af)

*   **action-menu,split-button:** ensure toggling the Menu closed completes (2dd0f98)
*   **picker:** ensure the Menu opens in a Tray on mobile (6be2bed)

*   allow non-selection carying Picker derivatives to report value (02c0134)

*   **picker,action-group,split-button:** leverage Overlay v2 (170a223)

*   make lots of things lazy (b8fa3ad)
*   make submenus lazier (a2d661c)

*   **menu:** convert to core tokens (#3254) (da43540)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **action-button,action-menu,picker,split-button:** expand and update application of aria-* attributes (52c0156)
*   **picker:** correct label application for screen readers (8ce0cb0)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** correct attribute spelling of "aria-label" in dismiss button (5fc9b30)

*   generate react/picker and pass react TS checks (101b88c)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   **action-menu:** fix 2510, unable to control top-level action-menu selection (c9198c2)
*   **action-menu:** never set item selected values when selects is undefined (5237fdb)
*   **action-menu:** stop stripping selected state from submenu items (968d1f2)
*   add icon present and icon-only support to Picker (f6887a3)
*   add support for "readonly" attribute (4bce3b7)
*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)
*   allow Picker to be reparented (39e7309)
*   analyze errors, properly this time (df685a2)
*   analyze type errors, and add deprecated syntax tests (b7e67a1)
*   bad merge conflict resolution (e408d61)
*   correct custom property hoisting (a1d98dc)
*   correct max size calculation for overlays (0585f7f)
*   ensure Action Menu Item with [href] close the menu (6b3d87f)
*   ensure correct Menu Items are "selected" when passed into the overlay (46a25db)
*   ensure focus is managed when tabbing out of a menu (9bfa81d)
*   expand sync offering for elements with overlay content (0195843)
*   give Picker a focus helper to enable tab navigation in Safari (e796525)
*   hopefully fix CI (ea87245)
*   include late added items in the item list for the Picker (9232eb1)
*   issues with optionsMenu & menuItems (01a7e35)
*   **menu:** add support for submenu interactions (68399af)
*   **menu:** clarify menu internal focus management via preventScroll option (9ae092c)
*   **menu:** ensure active descendant is in view when activated (6edc351)
*   **menu:** only scrollIntoView when keyboard navigating (f4e9278)
*   **overlay:** move "escape" listener to "keydown" (813b341)
*   **picker:** accept new "value" and new option post first render (8f8c93f)
*   **picker:** add "quick select" action to right/left arrow keys (21895ee)
*   **picker:** allow menu items to be added, updated, and removed (73511ba)
*   **picker:** ensure focus visibility application (2679081)
*   **picker:** ensure that width is customizable from the outside (702b052)
*   **picker:** make "change" event bubbling and composed (1fdd33d)
*   **picker:** query less strictly to support automatically selecting values (969f966)
*   **picker:** use "modal" as the menu overlay interaction (c8fbbe2)
*   prevent console.log in source and test files (3ee082c)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   simplify focus application in Menu (6140169)
*   simplify optionsMenu usage and fix tests (91241b7)
*   slot documentation (0ebd260)
*   split-button tests & lots of cleanup based on review feedback (10b4a04), closes #1189
*   style icons in Picker correctly (0bbdf84)
*   support a wider number of sizes (ee44978)
*   update Picker label via MutationObserver instead of "slotchange" (196998e)
*   update screen reader interface with menu items list (16756b5)
*   update to latest spectrum-css packages (a5ca19f)

*   add selects attribute to menu (bdf2578)
*   add t-shirt sizing with visual regressions to checkbox and picker elements (ce47ec8)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   conditionally load focus-visible polyfill (6b5e5cf)
*   delivery dev mode messages in various packages (62370a1)
*   deprecate sp-menu in PickerBase derived classes (bbb773c)
*   include all Dev Mode files in side effects (f70817c)
*   **picker:** process field-label content for more accurate a11y tree (dc9df54)
*   **picker:** replace dropdown with picker component (30b8bc7)
*   **picker:** support responsive delivery of menu (20031d1)
*   **picker:** update "icons-only" to "icons=only" to support more variations (de16a62)
*   **picker:** use new tokens (7d65b69)
*   reparentChildren - refactored arguments - breaking change (dea2bc5)
*   sets action-menu quiet to false by default, fixes #3040 (8414cab)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   update lit-* dependencies, wip (377f3c8)
*   use latest exports specification (a7ecf4b)

*   reorganize inheritance and composition in Menu Items (d96ccb6)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   sets action-menu quiet to false by default, fixes #3040 (8414cab)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** use new tokens (7d65b69)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   ensure Action Menu Item with [href] close the menu (6b3d87f)

*   style icons in Picker correctly (0bbdf84)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **action-menu:** fix 2510, unable to control top-level action-menu selection (c9198c2)
*   **action-menu:** never set item selected values when selects is undefined (5237fdb)

*   **overlay:** move "escape" listener to "keydown" (813b341)

**Note:** Version bump only for package @spectrum-web-components/picker

*   include all Dev Mode files in side effects (f70817c)

*   **action-menu:** stop stripping selected state from submenu items (968d1f2)
*   **picker:** query less strictly to support automatically selecting values (969f966)

*   delivery dev mode messages in various packages (62370a1)

**Note:** Version bump only for package @spectrum-web-components/picker

*   update Picker label via MutationObserver instead of "slotchange" (196998e)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   allow Picker to be reparented (39e7309)
*   correct custom property hoisting (a1d98dc)
*   ensure correct Menu Items are "selected" when passed into the overlay (46a25db)

*   conditionally load focus-visible polyfill (6b5e5cf)
*   reparentChildren - refactored arguments - breaking change (dea2bc5)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **menu:** add support for submenu interactions (68399af)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** support responsive delivery of menu (20031d1)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** make "change" event bubbling and composed (1fdd33d)

**Note:** Version bump only for package @spectrum-web-components/picker

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   **picker:** allow menu items to be added, updated, and removed (73511ba)

*   update lit-* dependencies, wip (377f3c8)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)

*   update screen reader interface with menu items list (16756b5)
*   **picker:** use "modal" as the menu overlay interaction (c8fbbe2)
*   include late added items in the item list for the Picker (9232eb1)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

**Note:** Version bump only for package @spectrum-web-components/picker

*   give Picker a focus helper to enable tab navigation in Safari (e796525)
*   simplify focus application in Menu (6140169)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **picker:** update "icons-only" to "icons=only" to support more variations (de16a62)

*   reorganize inheritance and composition in Menu Items (d96ccb6)

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)
*   expand sync offering for elements with overlay content (0195843)

*   add selects attribute to menu (bdf2578)

**Note:** Version bump only for package @spectrum-web-components/picker

*   add icon present and icon-only support to Picker (f6887a3)

*   prevent console.log in source and test files (3ee082c)

*   **menu:** clarify menu internal focus management via preventScroll option (9ae092c)
*   ensure focus is managed when tabbing out of a menu (9bfa81d)

*   **tabs:** add sp-tab-panel element (b17d276)

*   **picker:** ensure focus visibility application (2679081)

*   **menu:** only scrollIntoView when keyboard navigating (f4e9278)

*   **picker:** accept new "value" and new option post first render (8f8c93f)

*   correct max size calculation for overlays (0585f7f)

**Note:** Version bump only for package @spectrum-web-components/picker

*   add support for "readonly" attribute (4bce3b7)
*   analyze errors, properly this time (df685a2)
*   analyze type errors, and add deprecated syntax tests (b7e67a1)
*   bad merge conflict resolution (e408d61)
*   hopefully fix CI (ea87245)
*   issues with optionsMenu & menuItems (01a7e35)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   simplify optionsMenu usage and fix tests (91241b7)
*   slot documentation (0ebd260)
*   split-button tests & lots of cleanup based on review feedback (10b4a04), closes #1189

*   **picker:** process field-label content for more accurate a11y tree (dc9df54)
*   deprecate sp-menu in PickerBase derived classes (bbb773c)

**Note:** Version bump only for package @spectrum-web-components/picker

*   **menu:** ensure active descendant is in view when activated (6edc351)
*   **picker:** add "quick select" action to right/left arrow keys (21895ee)
*   **picker:** ensure that width is customizable from the outside (702b052)
*   support a wider number of sizes (ee44978)

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   add t-shirt sizing with visual regressions to checkbox and picker elements (ce47ec8)

*   **picker:** replace dropdown with picker component (30b8bc7)

Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false` Whether the component is disabled. When disabled, the component cannot be interacted with. `focused``focused``boolean``false` Whether the component currently has visible focus. `forcePopover``force-popover``boolean``false` Forces the component to render as a popover on mobile instead of a tray. `icons``icons``'only' | 'none' | undefined` Controls how icons are displayed in the picker button. - `'only'`: Shows only the icon, hiding the label visually. - `'none'`: Hides the icon entirely. `invalid``invalid``boolean``false` Whether the picker is in an invalid state. Displays a validation icon when true. `label``label``string | undefined` The placeholder label displayed when no item is selected. `open``open``boolean``false` Whether the component's menu overlay is currently open. `pending``pending``boolean``false` Whether the items are currently loading. `pendingLabel``pending-label``string``'Pending'` Defines a string value that labels the Picker while it is in pending state. `placement``placement``"top" | "top-start" | "top-end" | "right" | "right-start" | "right-end" | "bottom" | "bottom-start" | "bottom-end" | "left" | "left-start" | "left-end"``'bottom-start'` The preferred placement of the component's overlay relative to the trigger button. `quiet``quiet``boolean``false` Whether to render the picker in quiet mode with minimal visual styling. `readonly``readonly``boolean``false` Whether the component is read-only. When read-only, the component displays its value but cannot be changed. `value``value``string``''` The current value of the picker, corresponding to the selected menu item's value.

Name  Description `description` The description content for the Picker `label` The placeholder content for the Picker `tooltip` Tooltip to to be applied to the the Picker Button `default slot` menu items to be listed in the Picker

Name  Type  Description `change``Event``Announces that the `value` of the element has changed``scroll``Event``sp-closed``Event``Announces that the overlay has been closed``sp-opened``Event``Announces that the overlay has been opened`
