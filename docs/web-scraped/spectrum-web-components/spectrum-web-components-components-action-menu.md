# Source: https://opensource.adobe.com/spectrum-web-components/components/action-menu/

Title: Action Menu: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/action-menu/

Markdown Content:
An `<sp-action-menu>` is an action button that triggers an overlay with `<sp-menu-items>` for activation. Use an `<sp-menu>` element to outline the items that will be made available to the user when interacting with the `<sp-action-menu>` element. By default, `<sp-action-menu>` does not manage a selection. If you'd like for a selection to be managed, use `selects="single"` on the `<sp-menu>` to activate this functionality.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/action-menu?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/action-menu?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/action-menu

Import the side effectful registration of `<sp-action-menu>` via:

import '@spectrum-web-components/action-menu/sp-action-menu.js';

The default of `<sp-action-menu>` will load dependencies in `@spectrum-web-components/overlay` asynchronously via a dynamic import. In the case that you would like to import those tranverse dependencies statically, import the side effectful registration of `<sp-action-menu>` as follows:

import '@spectrum-web-components/action-menu/sync/sp-action-menu.js';

When looking to leverage the `ActionMenu` base class as a type and/or for extension purposes, do so via:

import { ActionMenu } from '@spectrum-web-components/action-menu';
Small<sp-action-menu size="s">
    <span slot="label">More Actions</span>
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
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-action-menu>Medium<sp-action-menu size="m">
    <span slot="label">More Actions</span>
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
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-action-menu>Large<sp-action-menu size="l">
    <span slot="label">More Actions</span>
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
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-action-menu>Extra Large<sp-action-menu size="xl">
    <span slot="label">More Actions</span>
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
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-action-menu>
In order to deliver an `<sp-action-menu>` without an icon, use the `label-only` slot. This will supress any icon from being displayed, both the default ellipsis icon or any icon the user might provide to the element.

<sp-action-menu>
    <span slot="label-only">More Actions</span>
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
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-action-menu>
The visible label that is be provided via the default `<slot>` interface can be omitted in preference of an icon only interface. In this context be sure that the `<sp-action-menu>` continued to be accessible to screen readers by applying the `label` attribute. This will apply an `aria-label` attribute of the same value to the `<button>` element that toggles the menu list.

<sp-action-menu label="More Actions">
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
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-action-menu>
A custom icon can be supplied via the `icon` slot in order to replace the default meatballs icon.

<sp-action-menu>
    <sp-icon-settings slot="icon"></sp-icon-settings>
    <span slot="label">Actions under the gear</span>
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
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>
        Save selection
    </sp-menu-item>
    <sp-menu-item disabled>
        Make work path
    </sp-menu-item>
</sp-action-menu>
When `selects` is set to `single`, the `<sp-action-menu>` element will maintain one selected item after an initial selection is made.

<p>
  The value of the `&lt;sp-action-menu&gt;` element is:
  <span id="single-value"></span>
</p>
<sp-action-menu selects="single" onchange="this.previousElementSibling.querySelector('#single-value').textContent=this.value">
  <span slot="label">Available shapes</span>
  <sp-menu-item value="shape-1-square">Square</sp-menu-item>
  <sp-menu-item value="shape-2-triangle">Triangle</sp-menu-item>
  <sp-menu-item value="shape-3-parallelogram">Parallelogram</sp-menu-item>
  <sp-menu-item value="shape-4-star">Star</sp-menu-item>
  <sp-menu-item value="shape-5-hexagon">Hexagon</sp-menu-item>
  <sp-menu-item value="shape-6-circle" disabled>Circle</sp-menu-item>
</sp-action-menu>
On mobile, the menu can be exposed in either a `sp-popover` or `sp-tray`. By default, `sp-action-menu` will render an `sp-tray`. If you would like to render `sp-popover` on mobile, add the attribute `force-popover` to the `sp-action-menu`.

Usage Guidance:

*   Use a tray when a menu’s proximity to its trigger is considered to be less important to the experience, or for showing a volume of content that is too overwhelming for a popover.
*   Use a popover when a menu’s proximity to its trigger is considered to be important to the experience, or for showing a volume of content that is manageable for a popover.

To see this functionality in action, load this page from your mobile device or use Chrome DevTools (or equivalent) and select a mobile device once the Device Toolbar (the phone/tablet icon) is active.

<sp-action-menu force-popover>
  <span slot="label">Action Menu</span>
  <sp-menu-item>Deselect</sp-menu-item>
  <sp-menu-item>Select Inverse</sp-menu-item>
  <sp-menu-item>Feather...</sp-menu-item>
  <sp-menu-item>Select and Mask...</sp-menu-item>
  <sp-menu-divider></sp-menu-divider>
  <sp-menu-item>Save Selection</sp-menu-item>
  <sp-menu-item disabled>Make Work Path</sp-menu-item>
</sp-action-menu>
Tooltip in action menu can be attached via adding `<sp-tooltip>` and can be customized by using various parameters (e.g. placement, content, etc) as needed.

<sp-action-menu>
  <sp-tooltip slot="tooltip" self-managed placement="bottom">
    Content
  </sp-tooltip>
  <span slot="label">Available shapes</span>
  <sp-menu-item value="shape-1-square">Square</sp-menu-item>
  <sp-menu-item value="shape-2-triangle">Triangle</sp-menu-item>
  <sp-menu-item value="shape-3-parallelogram">Parallelogram</sp-menu-item>
</sp-action-menu>
An `<sp-action-menu>` parent will ensure that the internal `<sp-menu>` features a role of `listbox` and contains children with the role `option`. Upon focusing the `<sp-action-menu>` using `ArrowDown` will also open the menu while throwing focus into first selected (or unselected when none are selected) menu item to assist in selecting of a new value.

*   Updated dependencies [`3783d87`]: 
    *   @spectrum-web-components/picker@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/action-button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2
    *   @spectrum-web-components/overlay@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/overlay@1.11.1
    *   @spectrum-web-components/picker@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   #5900`283f0fe` Thanks @TarunAdobe! - Added missing dependencies to the package.json files of several components to align with their usage in source code.

*   #5983`2732aad` Thanks @rubencarvalho! - **Fixed**: Safari + VoiceOver crash when opening Picker and ActionMenu. The issue was caused by an imperative `render()` call that mutated the DOM during the render cycle, causing Safari to crash while VoiceOver scanned the accessibility tree.

*   Updated dependencies [`ae61361`, `02b2d7d`, `b95e254`, `f07344f`, `2732aad`, `1d76b70`, `f8bdeec`, `cadc39e`, `4cb0b7b`, `9cb816b`]:

    *   @spectrum-web-components/picker@1.11.0
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/action-button@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/picker@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/picker@1.9.1
    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`bdf54c1`, `dbba861`, `7d23140`]: 
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/picker@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies [`6c2acaf`]: 
    *   @spectrum-web-components/picker@1.8.0
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies [`c1669d2`]: 
    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/picker@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`f6cebbd`, `3c3bc2b`]: 
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/picker@1.6.0
    *   @spectrum-web-components/action-button@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`6c58f50`]: 
    *   @spectrum-web-components/action-button@1.5.0
    *   @spectrum-web-components/picker@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   #5213`82212f4` Thanks @Rajdeepc! - Updated the attribute name from `forcePopover` to `force-popover` in the Picker and Action menu documentation

*   Updated dependencies [`2a0422e`, `72dbe62`, `1fc141c`, `82212f4`]:

    *   @spectrum-web-components/picker@1.4.0
    *   @spectrum-web-components/action-button@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   #5031`ea38ef0` Thanks @nikkimk! - Used WAI ARIA Authoring Practices Guide (APG) to make accessibility improvements for `<sp-action-menu>`, `<sp-menu>`, and `<sp-picker>`, including:

    *   Numpad keys now work with `<sp-picker>` and `<sp-action-menu>` -`<sp-action-menu>`'s `<sp-menu-item>` elements can now be read by a screen reader (#4556)
    *   `<sp-menu-item>` href can now be clicked by a screen reader (#4997)
    *   Opening a `<sp-action-menu>`, `<sp-menu>`, and `<sp-picker>` with a keyboard now sets focus on an item within the menu. (#4557)

See the following APG examples for more information:

    *   Navigation Menu Example
    *   Editor Menubar Example

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/picker@1.3.0
    *   @spectrum-web-components/action-button@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **action menu:** keyboard accessibility omnibus (#5031) (ea38ef0), closes #4623

*   **overlay:** derive popover placement from host in interaction controller (#5078) (635cf53)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)
*   **overlay:** make :focus-visible consistent when using overlay type modal (#4912) (7a5f786), closes #5021

*   add an optional chromatic vrt action (7d2f840)
*   **picker:** add forcePopover property (#5041) (3651e57)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   remove deprecated 'static' references (#4818)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **action-menu:** dispatch scroll event (#4715) (c76f3f5)
*   **picker:** added a custom class to make `:focus-visible` styles consistent across all browsers (#4724) (d667d08)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **action-menu** clicking a menu item in an ActionMenu tray doesn't register a click behind it ([4461] (https://github.com/adobe/spectrum-web-components/issues/4461)) ([56366ce] (https://github.com/adobe/spectrum-web-components/commit/56366ce2750bb4bb5c6e3fa5fe7d809434497adb))

*   **action-menu** ActionMenu tray in mobile device doesn't dispatch multiple events ([4459] (https://github.com/adobe/spectrum-web-components/issues/4459)) ([56366ce] (https://github.com/adobe/spectrum-web-components/commit/56366ce2750bb4bb5c6e3fa5fe7d809434497adb))

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **action-menu:** allow menu groups to handle their own selections (#4397) (5a19051)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **overlay:** clean position data on close (edac590)
*   **picker,action-menu,split-button:** update interaction model (#3935) (bae7d52)

*   **overlay:** move closed overlays to "display: none" (fc0278b)
*   **picker:** force close slotted Tooltip elements with disabled when Menu openes (82c8f12)

*   **menu:** support navigating to and selecting Menu Items in Menu Groups (8469ab2)

*   **action-menu:** allow tray to display full width (31415e4)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **menu:** allow `change` events to be direct (#3689) (b2cd3da)

*   **action-menu:** stack a "label-only" slot on top of the others to allow no icon menu buttons (6b5817d)
*   **menu:** allow Menu elements to be controlled (74ed7fb)
*   **picker,split-button:** include "tooltip" slot in the main button (699b8af)

*   **action-menu,split-button:** ensure toggling the Menu closed completes (2dd0f98)
*   **action-menu:** added static attribute support (#3573) (25889a8)

*   **picker,action-group,split-button:** leverage Overlay v2 (170a223)

*   make lots of things lazy (b8fa3ad)

*   **action-menu:** add a slot for Tooltip content (#3488) (23cef3a)

*   **menu:** convert to core tokens (#3254) (da43540)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **action-button,action-menu,picker,split-button:** expand and update application of aria-* attributes (52c0156)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   **action-menu:** apply slot text observer pattern (bbe6bb5)
*   **action-menu:** call super.firstUpdated for focus control (88bad85)
*   **action-menu:** fix 2510, unable to control top-level action-menu selection (c9198c2)
*   **action-menu:** never set item selected values when selects is undefined (5237fdb)
*   **action-menu:** provide action menu size to action button (b963f57)
*   **action-menu:** spectrum adherence update (6eb1860)
*   **action-menu:** stop stripping selected state from submenu items (968d1f2)
*   analyze type errors, and add deprecated syntax tests (b7e67a1)
*   code review feedback (23b84fc)
*   css fixes for action-menu (8c804c8)
*   ensure Action Menu Item with [href] close the menu (6b3d87f)
*   expand sync offering for elements with overlay content (0195843)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   **menu:** ensure that Groups in Action Menus are rendered with the correct width (a996a10)
*   missed ActionMenu for type changes (fa66d56)
*   normalize "event" and "error" argument names (8d382cd)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   remove unused dependencies and imports (fad4c9b)
*   **shared:** fixes focus-visible types in test (0dc7d68)
*   **shared:** further tweaks for test types (ee45173)
*   slot documentation (0ebd260)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-menu:** allow icon customization (cffd49a)
*   **action-menu:** remove menu selection by default (54d636f)
*   **action-menu:** update spectrum css input (62a5065)
*   **button:** use synthetic button instead of native (49e94bc)
*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)
*   **dropdown:** open menu UI with overlay system (9811eeb)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   sets action-menu quiet to false by default, fixes #3040 (8414cab)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   support Spectrum Token consumption and update Action Button to use them (743ab16)
*   **tabs:** add sp-tab-panel element (b17d276)
*   track the associated Spectrum CSS package (86b1be5)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   sets action-menu quiet to false by default, fixes #3040 (8414cab)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   ensure Action Menu Item with [href] close the menu (6b3d87f)

*   **menu:** ensure that Groups in Action Menus are rendered with the correct width (a996a10)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **action-menu:** fix 2510, unable to control top-level action-menu selection (c9198c2)
*   **action-menu:** never set item selected values when selects is undefined (5237fdb)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   include all Dev Mode files in side effects (f70817c)

*   **action-menu:** stop stripping selected state from submenu items (968d1f2)

*   support Spectrum Token consumption and update Action Button to use them (743ab16)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   remove unused dependencies and imports (fad4c9b)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)

*   track the associated Spectrum CSS package (86b1be5)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   expand sync offering for elements with overlay content (0195843)

*   **action-menu:** remove menu selection by default (54d636f)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **tabs:** add sp-tab-panel element (b17d276)

*   **action-menu:** provide action menu size to action button (b963f57)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   analyze type errors, and add deprecated syntax tests (b7e67a1)
*   missed ActionMenu for type changes (fa66d56)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   slot documentation (0ebd260)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   include the "types" entry in package.json files (b432f59)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-menu:** update spectrum css input (62a5065)
*   **button:** use synthetic button instead of native (49e94bc)

*   include the "types" entry in package.json files (b432f59)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-menu:** update spectrum css input (62a5065)
*   **button:** use synthetic button instead of native (49e94bc)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   code review feedback (23b84fc)
*   css fixes for action-menu (8c804c8)

*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **dropdown:** open menu UI with overlay system (9811eeb)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **action-menu:** spectrum adherence update (6eb1860)

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   **shared:** fixes focus-visible types in test (0dc7d68)
*   **shared:** further tweaks for test types (ee45173)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)

*   **action-menu:** apply slot text observer pattern (bbe6bb5)

**Note:** Version bump only for package @spectrum-web-components/action-menu

*   **action-menu:** call super.firstUpdated for focus control (88bad85)

*   **action-menu:** allow icon customization (cffd49a)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/action-menu

Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false` Whether the component is disabled. When disabled, the component cannot be interacted with. `focused``focused``boolean``false` Whether the component currently has visible focus. `forcePopover``force-popover``boolean``false` Forces the component to render as a popover on mobile instead of a tray. `icons``icons``'only' | 'none' | undefined` Controls how icons are displayed in the picker button. - `'only'`: Shows only the icon, hiding the label visually. - `'none'`: Hides the icon entirely. `invalid``invalid``boolean``false` Whether the picker is in an invalid state. Displays a validation icon when true. `label``label``string | undefined` The placeholder label displayed when no item is selected. `open``open``boolean``false` Whether the component's menu overlay is currently open. `pending``pending``boolean``false` Whether the items are currently loading. `pendingLabel``pending-label``string``'Pending'` Defines a string value that labels the Picker while it is in pending state. `placement``placement``"top" | "top-start" | "top-end" | "right" | "right-start" | "right-end" | "bottom" | "bottom-start" | "bottom-end" | "left" | "left-start" | "left-end"``'bottom-start'` The preferred placement of the component's overlay relative to the trigger button. `quiet``quiet``boolean``false` Whether to render the picker in quiet mode with minimal visual styling. `readonly``readonly``boolean``false` Whether the component is read-only. When read-only, the component displays its value but cannot be changed. `selects``selects``undefined | 'single'``undefined` The selection mode for the action menu. Unlike Picker, defaults to `undefined` (no selection management). Set to `'single'` to maintain a selected item. `staticColor``static-color``'white' | 'black' | undefined` Applies static color styling for use on colored backgrounds. - `'white'`: Use on dark backgrounds - `'black'`: Use on light backgrounds `value``value``string``''` The current value of the picker, corresponding to the selected menu item's value.

Name  Description `default slot` menu items to be listed in the Action Menu `icon` The icon to use for the Action Menu `label` The label to use for the Action Menu `label-only` The label to use for the Action Menu (no icon space reserved) `tooltip` Tooltip to be applied to the Action Button

Name  Type  Description `change``Event``scroll``Event``sp-closed``Event``Announces that the overlay has been closed``sp-opened``Event``Announces that the overlay has been opened`
