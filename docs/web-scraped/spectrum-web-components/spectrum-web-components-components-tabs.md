# Source: https://opensource.adobe.com/spectrum-web-components/components/tabs/

Title: Tabs: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/tabs/

Markdown Content:
The `<sp-tabs>` displays a list of `<sp-tab>` element children as `role="tablist"`. An `<sp-tab>` element is associated with a sibling `<sp-tab-panel>` element via their `value` attribute. When an `<sp-tab>` element is `selected`, the associated `<sp-tab-panel>` will also be selected, showing that panel and hiding the others.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/tabs?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/tabs?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/tabs
Import the side effectful registration of `<sp-tabs>`, `<sp-tab>` or `<sp-tab-panel>` via:

import '@spectrum-web-components/tabs/sp-tabs.js';
import '@spectrum-web-components/tabs/sp-tab.js';
import '@spectrum-web-components/tabs/sp-tab-panel.js';
When looking to leverage the `Tabs`, `Tab`, or `TabPanel` base class as a type and/or for extension purposes, do so via:

import { Tabs, Tab, TabPanel } from '@spectrum-web-components/tabs';
Tabs are created from the following parts:

*   **Tabs:** The container component (`<sp-tabs>`) that manages the tab list and handles selection logic.
*   **Tab item:** An individual tab (`<sp-tab>`) that users can select to view different content panels.
*   **Tab view:** The content panel (`<sp-tab-panel>`) associated with a tab, shown when its corresponding tab is selected.
*   **Divider:** A visual separator between tab items, used in some variants for clarity.
*   **Selection indicator:** A visual highlight (such as an underline or bar) that shows which tab is currently selected.

<sp-tabs selected="1" size="m">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Small<sp-tabs selected="1" size="s">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Medium<sp-tabs selected="1" size="m">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Large<sp-tabs selected="1" size="l">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Extra Large<sp-tabs selected="1" size="xl">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>
An `<sp-tabs>` element will display horizontally by default. It can be modified with attributes like `compact`, and `quiet`, or with content like icons, etc.

Compact
Compact tabs should never be used without the quiet variation. Please use Quiet + Compact Tabs instead.

<sp-tabs selected="1" compact>
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Icons<sp-tabs selected="1">
  <sp-tab label="Tab 1" value="1">
    <sp-icon-checkmark slot="icon"></sp-icon-checkmark>
  </sp-tab>
  <sp-tab label="Tab 2" value="2">
    <sp-icon-close slot="icon"></sp-icon-close>
  </sp-tab>
  <sp-tab label="Tab 3" value="3">
    <sp-icon-chevron-down slot="icon"></sp-icon-chevron-down>
  </sp-tab>
  <sp-tab label="Tab 4" value="4">
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Quiet<sp-tabs selected="1" quiet>
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Quiet + Compact<sp-tabs selected="1" quiet compact>
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>
An `<sp-tabs>` element will display horizontally by default. It can be modified with states like `compact`, `disabled`, and `quiet`, or with content like icons, etc. Vertical tabs should be used when horizontal space is more generous and when the list of sections is greater than can be presented to the user in a horizontal format. Vertical tabs are enabled by setting the `direction` attribute to `vertical` on `sp-tabs`.

Compact
Compact tabs should never be used without the quiet variation. Please use Quiet + Compact Tabs instead.

<sp-tabs selected="1" compact direction="vertical">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Icons<sp-tabs selected="1" direction="vertical">
  <sp-tab label="Tab 1" value="1">
    <sp-icon-checkmark slot="icon"></sp-icon-checkmark>
  </sp-tab>
  <sp-tab label="Tab 2" value="2">
    <sp-icon-close slot="icon"></sp-icon-close>
  </sp-tab>
  <sp-tab label="Tab 3" value="3">
    <sp-icon-chevron-down slot="icon"></sp-icon-chevron-down>
  </sp-tab>
  <sp-tab label="Tab 4" value="4">
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Quiet<sp-tabs selected="1" quiet direction="vertical">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>Quiet + Compact<sp-tabs selected="1" quiet compact direction="vertical">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4</sp-tab-panel>
</sp-tabs>
When an `<sp-tabs>` element is given the `disabled` attribute, its `<sp-tab>` children will be disabled as well, preventing a visitor from changing the selected tab. By default, `<sp-tab-panel>` children will not be addressed and the available content of the currently selected tab will be fully visible.

<sp-tabs selected="2" disabled>
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3"></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1 is not selectable</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2 is selected</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3 is not selectable</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4 is not selectable</sp-tab-panel>
</sp-tabs>
When an `<sp-tabs>` has a `selected` value, the `<sp-tab>` child of that `value` will be given `[tabindex="0"]` and will receive initial focus when tabbing into the `<sp-tabs>` element. When no `selected` value is present, the first `<sp-tab>` child will be treated in this way. When focus is currently within the `<sp-tabs>` element, the left and right arrows will move that focus back and forth through the available `<sp-tab>` children.

Tab items should have a label for accessibility. If a label isn’t present, it must include an icon and becomes an icon-only tab item.

Icons should only be used in a tab item when absolutely necessary: when adding essential value and having a strong association with the label. If the tab item does not have a visible label, it must still have a tooltip to disclose the label.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/action-button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/action-button@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   #5429`8da375b` Thanks @Rajdeepc! - Added `@spectrum-web-components/action-button` as a dependency for Tabs as its used in the direction button.

*   Updated dependencies [`c1669d2`]:

    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5323`c7efe31` Thanks @mizgaionutalexandru! - Fixed a bug where removing the `disabled` attribute (or setting it to `false`) on an `sp-tabs` element would not correctly enable the selected `sp-tab`. The fix updates the `focusInIndex` method in the component's `RovingTabindexController` to properly identify the selected tab that should become focusable when the parent tabs component is enabled.

*   Updated dependencies []:

    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **action menu:** keyboard accessibility omnibus (#5031) (ea38ef0), closes #4623

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** scroll exceeding tabs limit (#4722) (fc9a448)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** prevent vertical auto scroll (#4613) (e1ef097)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)
*   **tab-overflow:** improve tab navigation experience and support custom aria labels (#4165) (9c9bf95)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** bring selected tab into view (#4032) (a187057)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** account for the indicator bar in the overflow decorator (f4a8744)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** prevent vertical scrolling in overflow tabs (eb0592f)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** allow bi-directional arrow key navigation in both orientations (#3410) (ea10049)

*   **tabs,top-nav:** use Core Tokens (c6ba355)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)
*   allow Tab elements to accept slotted DOM content (29c9517)
*   check if current selected value exists before setting selected attr (1878ca3)
*   correct @element jsDoc listing across library (c97a632)
*   ensure browser understandable extensions (f4e59f7)
*   ensure that updates to Tab element content update the Selection Indicator (94891eb)
*   extract and share tshirt size styles (3acfc30)
*   extract and share tshirt size styles (b1440f7)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   keep compact property (904df71)
*   keep compact property (b5af15f)
*   manually support WHCM in tabs (11884f1)
*   move hover/focus hoisting into conditioning (15ac2f7)
*   proper overflow rtl support (9b1c9d4)
*   remove attribute binding logic (1f6833f)
*   remove attribute binding logic (7bce0ae)
*   stop merging selectors in a way that alters the cascade (369388f)
*   support matching keydown to [dir] (70b40a9)
*   tab indicator positioning (8c20769)
*   **tabs:** add "emphasized" and correct WHCM delivery (27940bd)
*   **tabs:** add "quiet", "compact", and "emphasized" "direction=vertical" (26fff53)
*   **tabs:** add "tablist" part to manage list styles (bbf8074)
*   **tabs:** added test (7d5f41f)
*   **tabs:** bind tabindicator update to dir value (09598b5)
*   **tabs:** bind tabs overflow state with sp-tabs (a07c45b)
*   **tabs:** bind tabs overflow state with sp-tabs (570a2cd)
*   **tabs:** correct entry focus element (64407d3)
*   **tabs:** correct indicator size by scaling from 100px (a3fb68b)
*   **tabs:** ensure only one active tab stop in the tabs (68b2523)
*   **tabs:** ensure tabs has layout (7aba515)
*   **tabs:** ensure that "auto" attribute is respected (d200775)
*   **tabs:** error on click - undefined tab target (9742227)
*   **tabs:** include sp-tab-panel.js in the export map (1619ae8)
*   **tabs:** manage disabled state on tabs and tab elements (58def1f)
*   **tabs:** update css workarounds (c2a17e0)
*   **top-nav:** prototype top-nav pattern (9708f6f)
*   update indicator animation for loading and content direction (f607f8b)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use CSS position relative and revert Tabs.ts changes (a682bcf)
*   use latest @spectrum-css/* versions (c35eb86)
*   use ObserveSlotText mixin to prevent white space from overriding label attribute (610fb4b)
*   use typescript@^4.5 for "native" document.fonts typings (a3e4aea)

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs-overflow:** address comments (b0e3398)
*   **tabs-overflow:** first round implementation of sp-tabs-overflow (c5b589a)
*   **tabs:** add sp-tab-panel element (b17d276)
*   **tabs:** add test coverage, remove unused property from component class (9933ad8)
*   **tabs:** add test coverage, update import paths (d104b52)
*   **tabs:** moving tabs overflow under tabs package (a18c692)
*   **tabs:** update bundle setup and readme (0249b94)
*   **tabs:** update imports to get correct coverage (2e421cd)
*   **tabs:** update spectrum css input (d875a0c)
*   update card and tabs to latest spectrum-css (55b8d67)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use latest exports specification (a7ecf4b)
*   use SixedMixin to manage "size" property (8819821)

*   reduce render cycles when managing "dir" attribute (7b28309)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   reduce render cycles when managing "dir" attribute (7b28309)

*   extract and share tshirt size styles (3acfc30)
*   extract and share tshirt size styles (b1440f7)
*   keep compact property (904df71)
*   keep compact property (b5af15f)
*   move hover/focus hoisting into conditioning (15ac2f7)
*   proper overflow rtl support (9b1c9d4)
*   remove attribute binding logic (1f6833f)
*   remove attribute binding logic (7bce0ae)
*   **tabs:** bind tabs overflow state with sp-tabs (a07c45b)
*   **tabs:** bind tabs overflow state with sp-tabs (570a2cd)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs-overflow:** address comments (b0e3398)
*   **tabs-overflow:** first round implementation of sp-tabs-overflow (c5b589a)
*   **tabs:** add test coverage, remove unused property from component class (9933ad8)
*   **tabs:** add test coverage, update import paths (d104b52)
*   **tabs:** moving tabs overflow under tabs package (a18c692)
*   **tabs:** update bundle setup and readme (0249b94)
*   **tabs:** update imports to get correct coverage (2e421cd)

*   **tabs:** correct indicator size by scaling from 100px (a3fb68b)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   tab indicator positioning (8c20769)
*   use CSS position relative and revert Tabs.ts changes (a682bcf)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** update css workarounds (c2a17e0)

*   update card and tabs to latest spectrum-css (55b8d67)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** add "quiet", "compact", and "emphasized" "direction=vertical" (26fff53)

*   include all Dev Mode files in side effects (f70817c)

*   **tabs:** add "tablist" part to manage list styles (bbf8074)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** add "emphasized" and correct WHCM delivery (27940bd)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   manually support WHCM in tabs (11884f1)

*   **tabs:** ensure that "auto" attribute is respected (d200775)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   **tabs:** added test (7d5f41f)
*   **tabs:** error on click - undefined tab target (9742227)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   allow Tab elements to accept slotted DOM content (29c9517)
*   ensure that updates to Tab element content update the Selection Indicator (94891eb)
*   use typescript@^4.5 for "native" document.fonts typings (a3e4aea)

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   correct @element jsDoc listing across library (c97a632)

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)

*   **tabs:** ensure tabs has layout (7aba515)
*   **tabs:** manage disabled state on tabs and tab elements (58def1f)

*   update indicator animation for loading and content direction (f607f8b)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   use ObserveSlotText mixin to prevent white space from overriding label attribute (610fb4b)

*   **tabs:** include sp-tab-panel.js in the export map (1619ae8)

*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/tabs

**Note:** Version bump only for package @spectrum-web-components/tabs

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **tabs:** update spectrum css input (d875a0c)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **tabs:** update spectrum css input (d875a0c)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   include default export in the "exports" fields (f32407d)

*   check if current selected value exists before setting selected attr (1878ca3)
*   update side effect listings (8160d3a)

*   **top-nav:** prototype top-nav pattern (9708f6f)

*   **tabs:** bind tabindicator update to dir value (09598b5)
*   support matching keydown to dir

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/tabs

*   ensure browser understandable extensions (f4e59f7)

*   **tabs:** correct entry focus element (64407d3)

*   **tabs:** ensure only one active tab stop in the tabs (68b2523)

*   leverage "exports" field in package.json (321abd7)

 Property  Attribute  Type  Default  Description `auto``auto``boolean``false` Whether to activate a tab on keyboard focus or not. 
By default a tab is activated via a "click" interaction. This is specifically intended for when tab content cannot be displayed instantly, e.g. not all of the DOM content is available, etc. To learn more about "Deciding When to Make Selection Automatically Follow Focus", visit: https://w3c.github.io/aria-practices/#kbd_selection_follows_focus

`compact``compact``boolean``false` The tab items are displayed closer together. `direction``direction``'vertical' | 'vertical-right' | 'horizontal'``'horizontal'``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `emphasized``emphasized``boolean``false``enableTabsScroll``enableTabsScroll``boolean``false``label``label``string``''``quiet``quiet``boolean``false` The tab list is displayed without a border. `selected``selected``string``''``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property 

Name  Description `default slot` Tab elements to manage as a group `tab-panel` Tab Panel elements related to the listed Tab elements

Name  Type  Description `change``Event``The selected Tab child has changed.`
