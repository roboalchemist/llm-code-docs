# Source: https://opensource.adobe.com/spectrum-web-components/components/menu/

Title: Menu: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/menu/

Markdown Content:
An `<sp-menu>` is used for creating a menu list. The various elements inside a menu are given as `<sp-menu-group>`, `<sp-menu-item>`, or `<sp-menu-divider>`. Often a `<sp-menu>` element will appear in a `<sp-popover>` element so that it displays as a toggling menu.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/menu?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/menu?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/menu

Import the side effectful registration of `<sp-menu>`, `<sp-menu-group>`, `<sp-menu-item>`, or `<sp-menu-divider>` individually as follows:

import '@spectrum-web-components/menu/sp-menu.js';
import '@spectrum-web-components/menu/sp-menu-group.js';
import '@spectrum-web-components/menu/sp-menu-item.js';
import '@spectrum-web-components/menu/sp-menu-divider.js';

When looking to leverage the `Menu`, `MenuGroup`, `MenuItem`, or `MenuDivider` base classes as a type and/or for extension purposes, do so via:

import {
    Menu,
    MenuGroup,
    MenuItem,
    MenuDivider
} from '@spectrum-web-components/menu';
<sp-menu label="Selection type">
    <sp-menu-item>
        Deselect
    </sp-menu-item>
    <sp-menu-item>
        Select inverse
    </sp-menu-item>
    <sp-menu-item>
        Feather...
    </sp-menu-item>
    <sp-menu-item>
        Select and mask...
    </sp-menu-item>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-menu>
Often an `<sp-menu>` element will be delivered inside of an `<sp-popover>` element when displaying it above other content.

<sp-popover open style="position: relative" label="Selection type">
  <sp-menu>
    <sp-menu-item value="item-1">Deselect</sp-menu-item>
    <sp-menu-item value="item-2">Select inverse</sp-menu-item>
    <sp-menu-item value="item-3">Feather...</sp-menu-item>
    <sp-menu-item value="item-4">Select and mask...</sp-menu-item>
    <sp-menu-item value="item-5">Save selection</sp-menu-item>
    <sp-menu-item value="item-6" disabled>Make work path</sp-menu-item>
  </sp-menu>
</sp-popover>
To render accessibly, an `<sp-menu>` element or its parent `<sp-popover>` must have a label. For an accessible label that is visibly hidden, but can still be read by assistive technology, use the `label` attribute.

Menu with label<sp-menu id="menu-label-attribute" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-menu>Popover with label<sp-popover open style="position: relative" label="Selection type:">
  <sp-menu id="popover-label-attribute">
    <sp-menu-item>Deselect</sp-menu-item>
    <sp-menu-item>Select inverse</sp-menu-item>
    <sp-menu-item>Feather...</sp-menu-item>
    <sp-menu-item>Select and mask...</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Save selection</sp-menu-item>
    <sp-menu-item disabled>Make work path</sp-menu-item>
  </sp-menu>
</sp-popover>Small<sp-menu id="menu-s" size="s" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-menu>
<sp-popover open style="position: relative" label="Selection type:">
  <sp-menu id="menu-s-popover" size="s">
    <sp-menu-item>Deselect</sp-menu-item>
    <sp-menu-item>Select inverse</sp-menu-item>
    <sp-menu-item>Feather...</sp-menu-item>
    <sp-menu-item>Select and mask...</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Save selection</sp-menu-item>
    <sp-menu-item disabled>Make work path</sp-menu-item>
  </sp-menu>
</sp-popover>Medium<sp-menu id="menu-m" size="m" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-menu>
<sp-popover open style="position: relative" label="Selection type:">
  <sp-menu id="menu-m-popover" size="m">
    <sp-menu-item>Deselect</sp-menu-item>
    <sp-menu-item>Select inverse</sp-menu-item>
    <sp-menu-item>Feather...</sp-menu-item>
    <sp-menu-item>Select and mask...</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Save selection</sp-menu-item>
    <sp-menu-item disabled>Make work path</sp-menu-item>
  </sp-menu>
</sp-popover>Large<sp-menu id="menu-l" size="l" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-menu>
<sp-popover open style="position: relative" label="Selection type:">
  <sp-menu id="menu-l-popover" size="l">
    <sp-menu-item>Deselect</sp-menu-item>
    <sp-menu-item>Select inverse</sp-menu-item>
    <sp-menu-item>Feather...</sp-menu-item>
    <sp-menu-item>Select and mask...</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Save selection</sp-menu-item>
    <sp-menu-item disabled>Make work path</sp-menu-item>
  </sp-menu>
</sp-popover>Extra Large<sp-menu id="menu-xl" size="xl" label="Selection type">
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save selection</sp-menu-item>
  <sp-menu-item disabled>Make work path</sp-menu-item>
</sp-menu>
<sp-popover open style="position: relative" label="Selection type:">
  <sp-menu id="menu-xl-popover" size="xl">
    <sp-menu-item>Deselect</sp-menu-item>
    <sp-menu-item>Select inverse</sp-menu-item>
    <sp-menu-item>Feather...</sp-menu-item>
    <sp-menu-item>Select and mask...</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Save selection</sp-menu-item>
    <sp-menu-item disabled>Make work path</sp-menu-item>
  </sp-menu>
</sp-popover>
The `<sp-menu>` element can be instructed to maintain a selection via the `selects` attribute. Depending on the chosen algorithm, the `<sp-menu>` element will hold a `value` property and manage the `selected` state of its `<sp-menu-item>` descendants.

*   When `selects="single"`, the `<sp-menu>` element will maintain one selected item after an initial selection is made.
*   When `selects` is set to `multiple`, the `<sp-menu>` element will maintain zero or more selected items.
*   When `selects` is set to `inherit`, the `<sp-menu>` element will allow its `<sp-menu-item>` children to participate in the selection of its nearest `<sp-menu>` ancestor.

Single<p>
  The value of the `&lt;sp-menu&gt;` element is:
  <span id="single-value"></span>
</p>
<sp-menu label="Choose a shape" selects="single" onchange="this.previousElementSibling.querySelector('#single-value').textContent=this.value">
  <sp-menu-item value="item-1">Square</sp-menu-item>
  <sp-menu-item value="item-2" selected>Triangle</sp-menu-item>
  <sp-menu-item value="item-3">Parallelogram</sp-menu-item>
  <sp-menu-item value="item-4">Star</sp-menu-item>
  <sp-menu-item value="item-5">Hexagon</sp-menu-item>
  <sp-menu-item value="item-6" disabled>Circle</sp-menu-item>
</sp-menu>Multiple<p>
  The value of the `&lt;sp-menu&gt;` element is:
  <span id="multiple-value">item-3,item-4</span>
</p>
<sp-menu label="Choose some fruit" selects="multiple" onchange="this.previousElementSibling.querySelector('#multiple-value').textContent=this.value">
  <sp-menu-item value="item-1">Apple</sp-menu-item>
  <sp-menu-item value="item-2">Banana</sp-menu-item>
  <sp-menu-item value="item-3" selected>Goji berry</sp-menu-item>
  <sp-menu-item value="item-4" selected>Grapes</sp-menu-item>
  <sp-menu-item value="item-5" disabled>Kumquat</sp-menu-item>
  <sp-menu-item value="item-6">Orange</sp-menu-item>
</sp-menu>Inherit<p>
  The value of the `&lt;sp-menu&gt;` element is:
  <span id="inherit-value">item-3 || item-4 || item-8 || item-11</span>
</p>
<sp-menu label="Choose some groceries" selects="multiple" value-separator=" || " onchange="this.previousElementSibling.querySelector('#inherit-value').textContent=this.value">
  <sp-menu label="Fruit" selects="inherit">
    <sp-menu-item value="item-1">Apple</sp-menu-item>
    <sp-menu-item value="item-2">Banana</sp-menu-item>
    <sp-menu-item value="item-3" selected>Goji berry</sp-menu-item>
    <sp-menu-item value="item-4" selected>Grapes</sp-menu-item>
    <sp-menu-item value="item-5" disabled>Kumquat</sp-menu-item>
    <sp-menu-item value="item-6">Orange</sp-menu-item>
  </sp-menu>
  <sp-menu label="Vegetables" selects="inherit">
    <sp-menu-item value="item-7">Carrot</sp-menu-item>
    <sp-menu-item value="item-8" selected>Garlic</sp-menu-item>
    <sp-menu-item value="item-9" disabled>Lettuce</sp-menu-item>
    <sp-menu-item value="item-10">Onion</sp-menu-item>
    <sp-menu-item value="item-11" selected>Potato</sp-menu-item>
    <sp-menu-item value="item-12">Tomato</sp-menu-item>
  </sp-menu>
</sp-menu>
Regardless of whether or not `<sp-menu>` carries a selection, when one of the `<sp-menu-item>` children that it manages is activated, the `<sp-menu>` element will dispatch a `change` event. At dispatch time, even when a selection is not held due to the absence of the `selects` attribute, the `value` of the `<sp-menu>` will correspond to the `<sp-menu-item>` that was activated. When the `selects` attribute is present, this `value` will persist beyond the lifecycle of the `change` event. When `selects="multiple"`, the values of multiple items will be comma separated, unless otherwise set via the `value-separator` attribute.

Note: The `change` event is only dispatched on a left mouse click or Enter/Space keypress. Right/Middle mouse clicks will not dispatch the `change` event.

Review the accessibility guidelines for the menu-item and menu-group descendants.

A menu is required to have an accessible label.

*   Updated dependencies []: 
    *   @spectrum-web-components/divider@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/action-button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/overlay@1.11.2
    *   @spectrum-web-components/popover@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/divider@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/overlay@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/popover@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5867`eac97a2` Thanks @shipg22! - **Fixed**: Improved touch interaction handling for submenus to prevent unintended submenu closures.

*   #5965`b95e254` Thanks @rubencarvalho! - **Fixed**: `sp-menu` now stops propagation of arrow key events when navigating between menu items. This prevents unintended side effects in layouts or applications that also listen for arrow key events.

*   Updated dependencies [`b95e254`, `02b2d7d`, `f07344f`, `1d76b70`, `f8bdeec`, `cadc39e`, `4cb0b7b`, `9cb816b`]:

    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/popover@1.11.0
    *   @spectrum-web-components/divider@1.11.0
    *   @spectrum-web-components/action-button@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/divider@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/overlay@1.10.0
    *   @spectrum-web-components/popover@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies [`a19cbe3`]: 
    *   @spectrum-web-components/overlay@1.9.1
    *   @spectrum-web-components/popover@1.9.1
    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/divider@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5732`4880da4` Thanks @Rajdeepc! - - **Fixed**: MenuItem focus stealing from input elements on mouseover by enhancing MenuItem's `handleMouseover` method to detect when an input element currently has focus and prevent stealing focus in those cases.

*   Updated dependencies [`7d23140`]:

    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/overlay@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/popover@1.9.0
    *   @spectrum-web-components/divider@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   #5616`f27ab09` Thanks @Rajdeepc! - **Fixed** : Fix iPad scrolling issue in picker dropdown where scrolling through menu items would accidentally select the first touched item and close the picker.

The fix implements touch gesture detection to distinguish between scrolling and selection. Added `isScrolling` getter for public API access. Test on iPad devices with long menus to validate scrolling behavior and selection accuracy.

*   Updated dependencies [`14486d6`, `ee1bae6`, `14486d6`, `826a2d5`]: 
    *   @spectrum-web-components/overlay@1.8.0
    *   @spectrum-web-components/divider@1.8.0
    *   @spectrum-web-components/popover@1.8.0
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   #5402`3aeafdd` Thanks @Rajdeepc! - **Fixes**: Icons in menu stories weren't properly responding to theme changes when used in functional story components. Switching to class-based LitElement components ensures proper component lifecycle hooks and shadow DOM context for icon initialization and theme integration.
*   Updated dependencies [`a646ae8`, `c1669d2`]: 
    *   @spectrum-web-components/overlay@1.7.0
    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/popover@1.7.0
    *   @spectrum-web-components/divider@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`03a4439`, `53f3769`]:

    *   @spectrum-web-components/popover@1.6.0
    *   @spectrum-web-components/overlay@1.6.0
    *   @spectrum-web-components/action-button@1.6.0
    *   @spectrum-web-components/divider@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5350`86bcd12` Thanks @Rajdeepc! - change display property from inline-flex to flex to eliminate unwanted spacing between menu items

*   #5313`4c2f908` Thanks @TarunAdobe! - Tapping on an `sp-menu-item` was causing the tap event to propagate to an `sp-checkbox` underneath it, resulting in the checkbox being checked unintentionally. The fix involves capturing the `touchend` event on the `sp-menu` to prevent this propagation.

*   #5270`a69accb` Thanks @nikkimk! - correctly applies menuitem hover styling with pointerenter actions and only applies menuitem focus styling with keyboard/click action #5269

*   Updated dependencies [`165a904`, `8f8735c`, `6c58f50`]:

    *   @spectrum-web-components/divider@1.5.0
    *   @spectrum-web-components/overlay@1.5.0
    *   @spectrum-web-components/action-button@1.5.0
    *   @spectrum-web-components/popover@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   #5187`2a0422e` Thanks @TarunAdobe! - Disabled drag and select functionality of picker in mobile devices. This is done to prevent click event being captured behind the menu-tray combination because the menu was closing immediately on pointerup. 
    *   Fixed a bug where the picker in a dialog was not closing when clicking outside the dialog. (#5111)
    *   Fixed another bug where the elements behind the menu were receiving click events. (#5060)

*   #5197`6618422` Thanks @nikkimk! - `<sp-menu>` - fixes `<sp-menu-item>` focus on hover (#5180)

*   Updated dependencies [`72dbe62`, `46cd782`, `70f5f6f`]:

    *   @spectrum-web-components/action-button@1.4.0
    *   @spectrum-web-components/overlay@1.4.0
    *   @spectrum-web-components/popover@1.4.0
    *   @spectrum-web-components/divider@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
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

*   #5176`468314f` Thanks @TarunAdobe! - 1. chore(checkbox): updated to latest css v10.1.1 for s2 fast follow 2. chore(dialog): The error property was not properly deprecated with a full migration plan in place. This has caused confusion and false sense of urgency for consumers to migrate. We are removing it to eliminate those pain points for consumers while we take a deep look at our dialogs and patterns. 3. chore(menu): updated to latest css v9.1.1 for s2 fast follow 4. fix(overlay): sp-overlay with type="manual" should close on pressing ESC key. When the last item is on overlay stack we are triggering the close method on esc key event.

*   Updated dependencies [`ea38ef0`, `468314f`]:

    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/overlay@1.3.0
    *   @spectrum-web-components/popover@1.3.0
    *   @spectrum-web-components/action-button@1.3.0
    *   @spectrum-web-components/divider@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **action menu:** keyboard accessibility omnibus (#5031) (ea38ef0), closes #4623
*   **menu:** make submenu scrollable (#5082) (a13dac2)
*   **picker:** update picker when menu item icons change (#5088) (63ef1ad)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   add an optional chromatic vrt action (7d2f840)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** prevent sp-menu-item text-align cascading (#4868) (6663820)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** allow menu-item to support arbitrary element as the submenu root (#4720) (4c6a0dc)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

*   **menu:** should not make a selection on right click (#4642) (d269629)

*   upgrade menu and dialog grid css (#4638) (ab9d468)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **action-bar:** support for action-menus (#3780) (4aff599)

*   **menu:** enable numpad arrow and Enter keys (#4492) (012c411)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **action-menu:** allow menu groups to handle their own selections (#4397) (5a19051)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** release synthetic "click" promise to unblock keyboard interactions (f8aecf3)

*   **asset:** use core tokens (99e76f4)

*   **menu:** fix css for `disabled` "value" slots in menu items (#4113) (3c5855d)

*   **menu:** correct disabled menu item's chevron to appropriate colour (#4052) (30f5bb5)

*   support generating random IDs outside of secure contexts (485a67c)

*   **menu:** process ":active" styles (7917583)

*   **picker,action-menu,split-button:** update interaction model (#3935) (bae7d52)

*   **overlay:** move closed overlays to "display: none" (fc0278b)

*   **menu:** support navigating to and selecting Menu Items in Menu Groups (8469ab2)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   update deps graph, fix imports (f633005)

*   **menu:** conditionally access slots for their assigned content (#3717) (c045822)

*   **menu:** allow `change` events to be direct (#3689) (b2cd3da)

*   **menu:** allow Menu elements to be controlled (74ed7fb)
*   **menu:** manage deeply slotted menu items and initial focus (7f9ad69)

*   **menu:** added support for menu item description (#3559) (ce99528)
*   **menu:** correct types import for .d.ts file creation (a11d264)

*   ensure submenus stay open when root it clicked again (83ced1c)

*   **menu:** prepare for Overlay v2 and less connnected/disconnected responsibilities (5dfb71e)

*   make lots of things lazy (b8fa3ad)
*   make submenus lazier (a2d661c)
*   make submenus lazy (93531b9)

*   **menu:** convert to core tokens (#3254) (da43540)

*   menu item missing aria labels (#3417) (0d04869)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:**#3164 plug memory leak with gobal events (ff589d4)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   add "value" slot to sp-menu-item (e1bd264)
*   add icon present and icon-only support to Picker (f6887a3)
*   add value/selection checks to the tests and fix up the value logic (933106f)
*   address a11y issues raised by updating our dependencies (4f06477)
*   correct @element jsDoc listing across library (c97a632)
*   correctly delivery visuals and mouse interactions for litAnchor and extensions (0ae889a)
*   **dropdown:** improve accessibility (389d9d9)
*   ensure Action Menu Item with [href] close the menu (6b3d87f)
*   ensure browser understandable extensions (f4e59f7)
*   ensure that an overlay can be released even if it does not complete its fade in animation (4cbb36f)
*   ensure that entering an ancestor Menu Item without a submen closes related submenus (efe5fa1)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   match "pointerup" listeners with "pointercancel" for full coverage (7f2ce92)
*   **menu:** add support for submenu interactions (68399af)
*   **menu:** allow for settign "selected" async from above (9d7f622)
*   **menu:** cache item parent element to correct disconnecting event dispatch (f375510)
*   **menu:** clarify menu internal focus management via preventScroll option (9ae092c)
*   **menu:** disabled menu-item should not open submenu (33848bc)
*   **menu:** ensure active descendant is in view when activated (6edc351)
*   **menu:** ensure that Groups in Action Menus are rendered with the correct width (a996a10)
*   **menu:** include all direct dependencies (aa7327f)
*   **menu:** manage tabindex and focus entry correctly (3b1a250)
*   **menu:** only scrollIntoView when keyboard navigating (f4e9278)
*   **menu:** pass current focus visibility to menu items (2d3bf80)
*   **menu:** patch undefined lastFocusedItem (772a7ea)
*   **menu:** prevent infinite loop when focus() (e4e98a3)
*   **menu:** support menu item list change in deep decendents (b2b47f3)
*   normalize "event" and "error" argument names (8d382cd)
*   **picker:** allow menu items to be added, updated, and removed (73511ba)
*   prepare for querying child items while disconnected (f4152a5)
*   prevent infinite loops when all children are [disabled] (2deac3d)
*   prevent leaving multiple submenus open at a time (d2bfbb2)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   simplify focus application in Menu (6140169)
*   **split-button:** hide "selected" item from menu (322a966)
*   stop merging selectors in a way that alters the cascade (369388f)
*   style clean up (49e1537)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update Picker label via MutationObserver instead of "slotchange" (196998e)
*   update role application logic to not overwrite menu* roles (94b6aec)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   add screenshot regression testing to CI (8205dfe)
*   add selects attribute to menu (bdf2578)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   allow dir management by sp-theme elements (2d10158)
*   conditionally load focus-visible polyfill (6b5e5cf)
*   delivery dev mode messages in various packages (62370a1)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   **menu:** update spectrum css input (8c7e18a)
*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   **picker:** process field-label content for more accurate a11y tree (dc9df54)
*   **picker:** support responsive delivery of menu (20031d1)
*   reparentChildren - refactored arguments - breaking change (dea2bc5)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **split-button:** add split-button pattern (4833a59)
*   update lit-* dependencies, wip (377f3c8)
*   update Menu Divider for new Spectrum CSS output (aca7e2d)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   reorganize inheritance and composition in Menu Items (d96ccb6)
*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** patch undefined lastFocusedItem (772a7ea)
*   prepare for querying child items while disconnected (f4152a5)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   ensure that an overlay can be released even if it does not complete its fade in animation (4cbb36f)

**Note:** Version bump only for package @spectrum-web-components/menu

*   ensure Action Menu Item with [href] close the menu (6b3d87f)

*   **menu:** ensure that Groups in Action Menus are rendered with the correct width (a996a10)

*   match "pointerup" listeners with "pointercancel" for full coverage (7f2ce92)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   include all Dev Mode files in side effects (f70817c)

*   delivery dev mode messages in various packages (62370a1)

**Note:** Version bump only for package @spectrum-web-components/menu

*   ensure that entering an ancestor Menu Item without a submen closes related submenus (efe5fa1)
*   update Picker label via MutationObserver instead of "slotchange" (196998e)

*   prevent leaving multiple submenus open at a time (d2bfbb2)
*   **menu:** disabled menu-item should not open submenu (33848bc)

*   update consumption of Spectrum CSS for latest version (ed2305b)

*   update Menu Divider for new Spectrum CSS output (aca7e2d)

*   conditionally load focus-visible polyfill (6b5e5cf)
*   reparentChildren - refactored arguments - breaking change (dea2bc5)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** add support for submenu interactions (68399af)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **picker:** support responsive delivery of menu (20031d1)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   **picker:** allow menu items to be added, updated, and removed (73511ba)

*   update lit-* dependencies, wip (377f3c8)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** cache item parent element to correct disconnecting event dispatch (f375510)

**Note:** Version bump only for package @spectrum-web-components/menu

*   simplify focus application in Menu (6140169)

*   correct @element jsDoc listing across library (c97a632)

*   reorganize inheritance and composition in Menu Items (d96ccb6)

*   add value/selection checks to the tests and fix up the value logic (933106f)
*   **split-button:** hide "selected" item from menu (322a966)

*   add selects attribute to menu (bdf2578)

*   style clean up (49e1537)

*   add "value" slot to sp-menu-item (e1bd264)
*   add icon present and icon-only support to Picker (f6887a3)

*   update role application logic to not overwrite menu* roles (94b6aec)

*   **menu:** clarify menu internal focus management via preventScroll option (9ae092c)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** pass current focus visibility to menu items (2d3bf80)

*   **menu:** manage tabindex and focus entry correctly (3b1a250)
*   **menu:** only scrollIntoView when keyboard navigating (f4e9278)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   correctly delivery visuals and mouse interactions for litAnchor and extensions (0ae889a)
*   remove `<sp-menu>` usage where deprecated (387db3b)

*   **picker:** process field-label content for more accurate a11y tree (dc9df54)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** ensure active descendant is in view when activated (6edc351)

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   address a11y issues raised by updating our dependencies (4f06477)
*   include the "types" entry in package.json files (b432f59)
*   prevent infinite loops when all children are [disabled] (2deac3d)
*   stop merging selectors in a way that alters the cascade (369388f)
*   use icons without "size" values (3fc7c91)
*   **menu:** prevent infinite loop when focus() (e4e98a3)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **menu:** update spectrum css input (8c7e18a)

*   include the "types" entry in package.json files (b432f59)
*   prevent infinite loops when all children are disabled
*   stop merging selectors in a way that alters the cascade (369388f)
*   use icons without "size" values (3fc7c91)
*   **menu:** prevent infinite loop when focus() (e4e98a3)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **menu:** update spectrum css input (8c7e18a)

**Note:** Version bump only for package @spectrum-web-components/menu

*   include default export in the "exports" fields (f32407d)
*   **dropdown:** improve accessibility (389d9d9)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/menu

*   allow dir management by sp-theme elements (2d10158)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   **split-button:** add split-button pattern (4833a59)

**Note:** Version bump only for package @spectrum-web-components/menu

*   **menu:** include all direct dependencies (aa7327f)
*   ensure browser understandable extensions (f4e59f7)

*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   leverage "exports" field in package.json (321abd7)

*   **menu:** support menu item list change in deep decendents (b2b47f3)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

**Note:** Version bump only for package @spectrum-web-components/menu

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   **menu:** allow for settign "selected" async from above (9d7f622)

*   add screenshot regression testing to CI (8205dfe)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/menu

Property  Attribute  Type  Default  Description `ignore``ignore``boolean``false` whether menu should be ignored by roving tabindex controller `label``label``string``''` label of the menu `selects``selects``undefined | 'inherit' | 'single' | 'multiple'` how the menu allows selection of its items: - `undefined` (default): no selection is allowed - `"inherit"`: the selection behavior is managed from an ancestor - `"single"`: only one item can be selected at a time - `"multiple"`: multiple items can be selected `value``value``string``''` value of the selected item(s) `valueSeparator``value-separator``string``','`

Name  Description `default slot` menu items to be listed in the menu

Name  Type  Description `change``Event``Announces that the `value` of the element has changed``close``Event`
