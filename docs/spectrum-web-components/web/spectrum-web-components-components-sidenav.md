# Source: https://opensource.adobe.com/spectrum-web-components/components/sidenav/

Title: Sidenav: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/sidenav/

Markdown Content:
Side navigation allows users to locate information and features within the UI. It can be used for either hierarchical or flat navigation, and gives the ability to group navigable items categorically. Side navigation is an opportunity to prioritize content or features based on your users’ needs in a way that maintains clear, persistent visibility. Use side navigation within the context of larger elements and mechanisms within the app frame.

`<sp-sidenav>` elements accept both `<sp-sidenav-item>` and `<sp-sidenav-heading>` elements as children in order to construct a hierarchy of navigation elements. `<sp-sidenav-item>` elements will place themselves as a togglable child of their `<sp-sidenav>` element parent. `<sp-sidenav-heading>` elements will create visible structure by grouping their `<sp-sidenav-item>` children under a non-interactive heading.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/sidenav?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/sidenav?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/sidenav
Import the side effectful registration of `<sp-sidenav>`, `<sp-sidenav-heading>`, or `<sp-sidenav-item>` via:

import '@spectrum-web-components/sidenav/sp-sidenav.js';
import '@spectrum-web-components/sidenav/sp-sidenav-heading.js';
import '@spectrum-web-components/sidenav/sp-sidenav-item.js';
When looking to leverage the `Sidenav`, `SidenavHeading`, or `SidenavItem` base classes as a type and/or for extension purposes, do so via:

import {
  Sidenav,
  SidenavHeading,
  SidenavItem,
} from '@spectrum-web-components/sidenav';
The side navigation consists of several key parts:

*   A container element that manages the side navigation behavior
*   Individual side navigation items that may or may not be expandable
*   Children side navigation items that are revealed when a parent item is expanded
*   Optional heading with a label

<sp-sidenav>
  <sp-sidenav-heading label="Piano"></sp-sidenav-heading>
  <sp-sidenav-item label="Treble"></sp-sidenav-item>
  <sp-sidenav-item label="Bass"></sp-sidenav-item>
  <sp-sidenav-item disabled label="Grand staff"></sp-sidenav-item>
</sp-sidenav>Default (single-level)
Make sure to use the right option for the context and user needs. Don’t mix behavior, styles, or variations together in a single navigation menu. Follow these guidelines:

*   When navigation is simple, use the single level side navigation.
*   When navigation is simple but categorical, use the single level side navigation with headers.
*   When navigation is expansive, hierarchical, and/or you need progressive disclosure in the menu behavior, use the multi-level side navigation. Up to three levels of navigation are supported.

<sp-sidenav defaultValue="Docs">
  <sp-sidenav-item value="Docs" href="/components/SideNav" label="Docs" selected ></sp-sidenav-item>
  <sp-sidenav-item value="Guides" href="/guides" label="Guides" ></sp-sidenav-item>
  <sp-sidenav-item value="Community" href="/community" label="Community" ></sp-sidenav-item>
  <sp-sidenav-item value="Storybook" href="/storybook" target="_blank" label="Storybook" ></sp-sidenav-item>
  <sp-sidenav-item value="Releases" href="/releases" target="_blank" label="Releases" disabled ></sp-sidenav-item>
  <sp-sidenav-item value="GitHub" href="/github" target="_blank" label="Github" ></sp-sidenav-item>
</sp-sidenav>Single-level with icons
In single-level side navigation, do not mix icon usage between side nav items. Either all side nav items have icons, or no items have icons. In cases where the navigation content might be user-generated, stick to text-only navigation items.

<sp-sidenav>
  <sp-sidenav-item value="Section Title 1" label="Section Title 1">
    <sp-icon-star slot="icon"></sp-icon-star>
  </sp-sidenav-item>
  <sp-sidenav-item value="Section Title 2" label="Section Title 2" expanded>
    <sp-icon-star slot="icon"></sp-icon-star>
  </sp-sidenav-item>
  <sp-sidenav-item value="Section Title 3" label="Section Title 3" expanded>
    <sp-icon-star slot="icon"></sp-icon-star>
  </sp-sidenav-item>
</sp-sidenav>With headings
Use headings in single level side navigation when it's beneficial to group navigation items into categories. The headings are not interactive. If items don’t fall into a category, place them at the top. When using the heading variation, an entire category should either all have icons or all be text-only.

Although headings can be used in multi-level side navigation, they can only be used as first-level items, and are not to be nested.

<sp-sidenav>
  <sp-sidenav-item value="Section 1" label="Section 1"></sp-sidenav-item>
  <sp-sidenav-item value="Section 2" label="Section 2"></sp-sidenav-item>
  <sp-sidenav-heading label="Category 1">
    <sp-sidenav-item value="Section 3" label="Section 3"></sp-sidenav-item>
    <sp-sidenav-item value="Section 4" label="Section 4"></sp-sidenav-item>
  </sp-sidenav-heading>
  <sp-sidenav-heading label="Category 2">
    <sp-sidenav-item value="Section 5" label="Section 5"></sp-sidenav-item>
    <sp-sidenav-item value="Section 6" label="Section 6"></sp-sidenav-item>
  </sp-sidenav-heading>
</sp-sidenav>Multi-level
Use `variant="multilevel"` when you have multiple layers of hierarchical navigation. In the instances where a top-level navigation item has no children, clicking will send the user to the location of the item. Additionally, headings can be used in multi-level side navigation, but they can only be used as first-level items, and are not to be nested.

Up to three levels of navigation are supported.

<sp-sidenav variant="multilevel" defaultValue="Layout">
  <sp-sidenav-item value="Guidelines" label="Guidelines"></sp-sidenav-item>
  <sp-sidenav-heading value="Styles" label="Styles">
    <sp-sidenav-item value="Color" label="Color"></sp-sidenav-item>
    <sp-sidenav-item value="Grid" label="Grid" expanded>
      <sp-sidenav-item value="Layout" label="Layout"></sp-sidenav-item>
      <sp-sidenav-item value="Responsive" label="Responsive"></sp-sidenav-item>
    </sp-sidenav-item>
    <sp-sidenav-item value="Typography" label="Typography"></sp-sidenav-item>
  </sp-sidenav-heading>
  <sp-sidenav-item value="Elements" label="Elements"></sp-sidenav-item>
  <sp-sidenav-item value="Patterns" label="Patterns"></sp-sidenav-item>
</sp-sidenav>Multi-level with icons
In multi-level side navigation, icon and text-only navigation items can be used in combination, but only the first-level items can have icons to maintain visual clarity and hierarchy. Icons only appear on first-level items, and sublevels (second and third) should not include icons. In cases where the navigation content might be user-generated, stick to text-only navigation items.

*   All icons: all items have icons
*   No icons: no items have icons
*   Mixed icons: only first-level items have icons; second and third-level items do not

<sp-sidenav>
  <sp-sidenav-item value="Section Title 1" label="Section Title 1">
    <sp-icon-star slot="icon"></sp-icon-star>
    <sp-sidenav-item value="Typography" label="Typography"></sp-sidenav-item>
  </sp-sidenav-item>
  <sp-sidenav-item value="Section Title 2" label="Section Title 2" expanded>
    <sp-icon-star slot="icon"></sp-icon-star>
    <sp-sidenav-item value="Iconography" label="Iconography"></sp-sidenav-item>
  </sp-sidenav-item>
  <sp-sidenav-item value="Section Title 3" label="Section Title 3" expanded>
    <sp-icon-star slot="icon"></sp-icon-star>
    <sp-sidenav-item value="Patterns" label="Patterns" expanded>
      <sp-sidenav-item value="Forms" label="Forms"></sp-sidenav-item>
      <sp-sidenav-item value="Cards" label="Cards"></sp-sidenav-item>
    </sp-sidenav-item>
  </sp-sidenav-item>
</sp-sidenav>
When an side navigation item is programmatically selected in `variant="multilevel"`, all of its parent items automatically expand to reveal the selection path.

When the `manage-tab-index` attribute is set on an `<sp-sidenav>` element, it will present its `<sp-sidenav-item>` children with a single tab-stop. This will leave items beyond the selected item (or when there is no focusable selected item), accessible via the up and down arrow keys. Items with expanded children that aren't selected lose focus when `manage-tab-index` is active.

*   `<sp-sidenav>` renders a `<nav>` tag and implicitly sets `role="navigation"`
*   Optional `aria-label` is available for further identification
*   Individual items use `role="listitem"` automatically
*   Nested list containers (i.e. `<div>` tags) use `role="list"`
*   Nested item containers use `aria-labelledby` referencing their parent item's `id`
*   `aria-expanded="true/false"` indicates expand/collapse state for parent items
*   `aria-controls` on parent items is set to the `id` of their child `role="list"` containers when expanded
*   `aria-current="page"` indicates the currently selected item when it has an `href`
*   When the `<sp-sidenav>` includes the `disabled` property, the entire component receives `tabindex="-1"`
*   `aria-hidden="true"` is applied to all decorative icons

*   `Tab` and `Shift + Tab` moves focus into or out of the side nav
*   If `manage-tab-index` is enabled, the up and down arrow keys will shift focus between all visible sidenav items
*   `Enter` selects a side nav item or toggles expansion for parent items

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   #5504`cde976d` Thanks @castastrophe! - Replace deprecated `word-break: break-word` with `overflow-wrap: break-word` to align with modern CSS standards and improve cross-browser compatibility. This property was deprecated in Chrome 44 (July 2015) in favor of the standardized `overflow-wrap` property.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   **reactive-controllers:** update focusable element's tab-index to 0 on accepting focus (#4630) (d359e84)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   update deps graph, fix imports (f633005)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   **sidenav:** reintroduce support for slotted label content (26c7e6e)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   **sidenav:** migrate to core tokens (1846aa3)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   **sidenav:** express hierarchy using list and listitem (f9019d7), closes #3348#3348

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   generate react/picker and pass react TS checks (101b88c)

*   #2933 by adding optional variant property to SideNav (9c45c33)
*   correct @element jsDoc listing across library (c97a632)
*   correct a11y tree (f7e54e5)
*   correctly track "activeElement" across shadow boundaries (8b9f93a)
*   ensure browser understandable extensions (f4e59f7)
*   ensure item exists when attempting to acquire next item to focus (fb52cea)
*   fix expanding sidenav item that has no value (b28cdac)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   normalize "event" and "error" argument names (8d382cd)
*   prevent infinite loops when all children are [disabled] (2deac3d)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   **sidenav:** add aria-current when using href with sidenav-item (9172639)
*   **sidenav:** add support for icons and document icons/headlines (9ddb363)
*   **sidenav:** manage tabindex when interacting with keyboard (ea977cf)
*   **sidenav:** prevent items with hrefs from toggling expanded or selection (7ff4920)
*   **sidenav:** tighten Spectrum adherence and sharpen docs delivery (d4c70cd)
*   stop merging selectors in a way that alters the cascade (369388f)
*   style clean up (49e1537)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update slotting in "sp-sidenav-item" to allow for labelling in HTML (928c476)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   implement #2964 for sidenav component (99afac9)
*   implement #2964 for sidenav component (5bf36e5)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **sidenav:** add a "change" event to track the "value" property (8d3a0bd)
*   **sidenav:** add keyboard accessibility (6ff622b)
*   **sidenav:** update spectrum css input (bd43201)
*   support rel attribute for sidenav item (90522e7)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   implement #2964 for sidenav component (99afac9)
*   implement #2964 for sidenav component (5bf36e5)

*   #2933 by adding optional variant property to SideNav (9c45c33)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   **sidenav:** prevent items with hrefs from toggling expanded or selection (7ff4920)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   update consumption of Spectrum CSS for latest version (ed2305b)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   correct @element jsDoc listing across library (c97a632)

*   update slotting in "sp-sidenav-item" to allow for labelling in HTML (928c476)

*   style clean up (49e1537)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)

*   ensure item exists when attempting to acquire next item to focus (fb52cea)

*   **sidenav:** add a "change" event to track the "value" property (8d3a0bd)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   include the "types" entry in package.json files (b432f59)
*   prevent infinite loops when all children are [disabled] (2deac3d)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **sidenav:** update spectrum css input (bd43201)

*   include the "types" entry in package.json files (b432f59)
*   prevent infinite loops when all children are disabled
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **sidenav:** update spectrum css input (bd43201)

*   support rel attribute for sidenav item (90522e7)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   ensure browser understandable extensions (f4e59f7)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   **sidenav:** add aria-current when using href with sidenav-item (9172639)
*   **sidenav:** manage tabindex when interacting with keyboard (ea977cf)

*   leverage "exports" field in package.json (321abd7)

*   **sidenav:** add support for icons and document icons/headlines (9ddb363)
*   **sidenav:** tighten Spectrum adherence and sharpen docs delivery (d4c70cd)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/sidenav

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   correct a11y tree (f7e54e5)

*   correctly track "activeElement" across shadow boundaries (8b9f93a)

**Note:** Version bump only for package @spectrum-web-components/sidenav

*   fix expanding sidenav item that has no value (b28cdac)

*   **sidenav:** add keyboard accessibility (6ff622b)

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/sidenav

Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `label``label``string | undefined | undefined``undefined` An accessible label that describes the component, so that the side navigation can be distinguished from other navigation by screen reader users. It will be applied to aria-label, but not visually rendered. `manageTabIndex``manage-tab-index``boolean``false``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `value``value``string | undefined``undefined``variant``variant``'multilevel' | undefined``undefined` The multilevel variant will have multiple layers of hierarchical navigation items.

Name  Description `default slot` the Sidenav Items to display

Name  Type  Description `change``Event``Announces a change in the `value` property of the navigation element. This change can be "canceled" via `event.preventDefault()`.`
