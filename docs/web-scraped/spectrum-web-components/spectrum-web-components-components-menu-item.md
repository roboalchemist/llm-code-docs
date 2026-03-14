# Source: https://opensource.adobe.com/spectrum-web-components/components/menu-item/

Title: Menu Item: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/menu-item/

Markdown Content:
For use within an `<sp-menu>` element, an `<sp-menu-item>` represents a single item in a menu.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/menu?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/menu?style=for-the-badge)

yarn add @spectrum-web-components/menu

Import the side effectful registration of `<sp-menu-item>` as follows:

import '@spectrum-web-components/menu/sp-menu-item.js';

When looking to leverage the `MenuItem` base class as a type and/or for extension purposes, do so via:

import { MenuItem } from '@spectrum-web-components/menu';

Menus are a collection of `<sp-menu-item>`s that can be modified via a `disabled` or `selected` attribute to represent an item in that state.

<sp-menu selectable>
  <sp-menu-item>Active Menu Item</sp-menu-item>
  <sp-menu-item disabled>Disabled Menu Item</sp-menu-item>
  <sp-menu-item selected>Selected Menu Item</sp-menu-item>
</sp-menu>
Content assigned to the `icon` slot will be placed at the beginning of the `<sp-menu-item>`.

<sp-menu style="width: 200px;">
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
</sp-menu>
When you use `<sp-menu-item>` elements without text content, you will need to be sure to use the `value` attribute so that the `<sp-picker>` or `<sp-menu>` element can differentiate between the available options. Further, it is important that you apply accessible labeling to the `[slot="icon"]` content as follows:

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
Content assigned to the `description` slot will be placed below the `<sp-menu-item>`, like help text for users to understand the context of corresponding `<sp-menu-item>`.

<sp-menu style="width: 200px;">
  <sp-menu-item>
    Quick export
    <span slot="description">Share a snapshot</span>
  </sp-menu-item>
  <sp-menu-item>
    Open a copy
    <span slot="description">Illustrator for iPad</span>
  </sp-menu-item>
  <sp-menu-item>
    Share link
    <span slot="description">Enable comments and download</span>
  </sp-menu-item>
</sp-menu>
Content assigned to the `value` slot will be placed at the end of the `<sp-menu-item>`, like values, keyboard shortcuts, etc., based on the current text direction.

<sp-menu style="width: 200px;">
  <sp-menu-item>
    Save
    <kbd slot="value">⌘S</kbd>
  </sp-menu-item>
  <sp-menu-item>
    Completed
    <span slot="value">47%</span>
  </sp-menu-item>
  <sp-menu-item>
    Activity
    <sp-link slot="value" href="#">More&nbsp;info</sp-link>
  </sp-menu-item>
</sp-menu>
When displayed as a descendent of an element that manages selection (e.g. `<sp-action-menu>`, `<sp-picker>`, `<sp-split-button>`, etc.), an `<sp-menu-item>` will represent the "selected" value of that ancestor when its `value` attribute or the trimmed `textContent` (represeted by `el.itemText`) matches the `value` of the ancestor element.

In the following example, the selected `<sp-menu-item>` represents a `value` of `"Text that is really long and useful to a visitor, but not exactly good to use in your application or component state."` for the ancestor element.

Picker<sp-field-label for="picker-content">Value attribute usage:</sp-field-label>
<sp-picker id="picker-content" label="Menu items examples" value="Text that is really long and useful to a visitor, but not exactly good to use in your application or component state.">
  <sp-menu-item>
    Text that is really long and useful to a visitor, but not exactly good to
    use in your application or component state.
  </sp-menu-item>
  <sp-menu-item>Not selected</sp-menu-item>
</sp-picker>Action menu<sp-action-menu value="Text that is really long and useful to a visitor, but not exactly good to use in your application or component state.">
  <span slot="label">Menu items examples</span>
  <sp-menu-item>
    Text that is really long and useful to a visitor, but not exactly good to
    use in your application or component state.
  </sp-menu-item>
  <sp-menu-item>Not selected</sp-menu-item>
</sp-action-menu>
When the `value` attribute is leveraged, the selected `<sp-menu-item>` represents a `value` of `"short-key"` for the `<sp-action-menu>` element.

Picker<sp-field-label for="picker-value">Value attribute usage:</sp-field-label>
<sp-picker id="picker-value" value="short-key">
  <span slot="label">Menu items examples</span>
  <sp-menu-item value="not-selected">Not selected</sp-menu-item>
  <sp-menu-item value="short-key">
    Text that is really long and useful to a visitor, but not exactly good to
    use in your application or component state.
  </sp-menu-item>
</sp-picker>Action menu<sp-action-menu value="short-key">
  <span slot="label">Menu items examples</span>
  <sp-menu-item value="not-selected">Not selected</sp-menu-item>
  <sp-menu-item value="short-key">
    Text that is really long and useful to a visitor, but not exactly good to
    use in your application or component state.
  </sp-menu-item>
</sp-action-menu>
An `<sp-menu-item>` can also accept content addressed to its `"submenu"` slot. An `<sp-menu>` element with this slot name surfaces the options in an adjacent popover, which can be activated by hovering over the parent menu item with your pointer or focusing the menu item and pressing the appropriate `ArrowRight` or `ArrowLeft` key based on text direction to move into the submenu.

<p>
  Your favorite park in New York is:
  <span id="group-1-value"></span>
  <br />
  <br />
  Your favorite park in San Francisco is:
  <span id="group-2-value"></span>
</p>
<sp-menu style="width: 200px;" onchange="this.parentElement .previousElementSibling .querySelector(`#${arguments[0].target.id}-value`) .textContent = arguments[0].target.value">
  <sp-menu-item>
    New York
    <sp-menu slot="submenu" selects="single">
      <sp-menu-item>Central Park</sp-menu-item>
      <sp-menu-item>Flushing Meadows Corona Park</sp-menu-item>
      <sp-menu-item>Prospect Park</sp-menu-item>
    </sp-menu>
  </sp-menu-item>
  <sp-menu-item>
    San Francisco
    <sp-menu slot="submenu" selects="single">
      <sp-menu-item>Golden Gate Park</sp-menu-item>
      <sp-menu-item>John McLaren Park</sp-menu-item>
      <sp-menu-item>Lake Merced Park</sp-menu-item>
    </sp-menu>
  </sp-menu-item>
</sp-menu>
Note: While `sp-menu-item` can accommodate any custom content in the `submenu` slot, it will not handle selection or keyboard navigation for such content. To ensure proper management of selection and keyboard navigation, it is recommended to use `sp-menu` within the `submenu` slot```

<sp-menu style="width: 200px;">
  <sp-menu-item>
    Item with arbitrary content in submenu
    <div role="menuitem" slot="submenu" style="padding: 12px">
      <img src="https://placekitten.com/200/200" alt="Kitten" style="width: 100%; height: auto; border-radius: 4px" />
      <p>I am an arbitrary content in submenu</p>
    </div>
  </sp-menu-item>
</sp-menu>
When displayed as a descendent of an element that manages selection (e.g. `<sp-action-menu>`, `<sp-picker>`, etc.), an `<sp-menu-item>` will represent the "selected" value of that ancestor when its `value` attribute or the trimmed `textContent` (represeted by `el.itemText`) matches the `value` of the ancestor element.

In the following example, the selected `<sp-menu-item>` represents a `value` of `Text that is really long and useful to a visitor, but not exactly good to use in your application or component state.` for the ancestor element.

<sp-menu style="width: 200px;">
  <sp-menu-item>
    Item with arbitrary content in submenu
    <div role="menuitem" slot="submenu" style="padding: 12px">
      <img src="https://placekitten.com/200/200" alt="Kitten" style="width: 100%; height: auto; border-radius: 4px" />
      <p>I am an arbitrary content in submenu</p>
    </div>
  </sp-menu-item>
</sp-menu>
Note: While `sp-menu-item` can accommodate any custom content in the `submenu` slot, it will not handle selection or keyboard navigation for such content. To ensure proper management of selection and keyboard navigation, it is recommended to use `sp-menu` within the `submenu` slot```

<sp-menu style="width: 200px;">
  <sp-menu-item>
    Item with arbitrary content in submenu
    <div role="menuitem" slot="submenu" style="padding: 12px">
      <img src="https://placekitten.com/200/200" alt="Kitten" style="width: 100%; height: auto; border-radius: 4px" />
      <p>I am an arbitrary content in submenu</p>
    </div>
  </sp-menu-item>
</sp-menu>
Review the accessibility guidelines for the parent menu and menu-group.

Either place visible text in the component's slot or use `label` attribute to ensure menu items can be read by assistive technology.

Using slotted text<sp-field-label for="picker-icons-only">Choose an action...</sp-field-label>
<sp-picker label="What would you like to do?" value="item-2" id="picker-icons-only">
  <sp-menu-item value="item-1">
    <sp-icon-save-floppy slot="icon"></sp-icon-save-floppy>
    Save
  </sp-menu-item>
  <sp-menu-item value="item-2">
    <sp-icon-stopwatch slot="icon"></sp-icon-stopwatch>
    Finish
  </sp-menu-item>
  <sp-menu-item value="item-3">
    <sp-icon-user-activity slot="icon"></sp-icon-user-activity>
    Review
  </sp-menu-item>
</sp-picker>Using label attribute<sp-field-label for="picker-icons-only">Choose an action...</sp-field-label>
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

Property  Attribute  Type  Default  Description `active``active``boolean``false` whether the menu item is active or has an active descendant `disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `focused``focused``boolean``false` whether the menu item has keyboard focus `hasSubmenu``has-submenu``boolean``false` whether the menu item has a submenu `href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `noWrap``no-wrap``boolean``false` whether menu item text content should not wrap `open``open``boolean``false` whether submenu is open `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `selected``selected``boolean``false` whether the menu item is selected `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `value``value``string` value of the menu item which is used for selection

Name  Description `default slot` text content to display within the Menu Item `description` description to be placed below the label of the Menu Item `icon` icon element to be placed at the start of the Menu Item `value` content placed at the end of the Menu Item like values, keyboard shortcuts, etc.

Name  Type  Description `blur``FocusEvent``focus``FocusEvent``undefined``MenuItemAddedOrUpdatedEvent`
