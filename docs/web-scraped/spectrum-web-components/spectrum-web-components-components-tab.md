# Source: https://opensource.adobe.com/spectrum-web-components/components/tab/

Title: Tab: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/tab/

Markdown Content:
Tab: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-tab
======

NPM 1.11.2

View Storybook

Try it on Stackblitz

Overview API

Overview
--------

#Section titled Overview

An `<sp-tab>` element surfaces a `label` attribute to serve as its default text content when none is available in the DOM. An icon may be assigned to the element via the `icon` slot; e.g. `<sp-tab><svg slot="icon" label="Tab with icon">...</svg></sp-tab>`. Associate an `<sp-tab>` element with the `<sp-tab-panel>` that represents its content with the `value` attribute.

### Usage

#Section titled Usage

![Image 3: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/tabs?style=for-the-badge)![Image 4: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/tabs?style=for-the-badge)

yarn add @spectrum-web-components/tabs
Import the side effectful registration of `<sp-tab>` via:

import '@spectrum-web-components/tabs/sp-tab.js';
When looking to leverage the `Tab` base class as a type and/or for extension purposes, do so via:

import { Tab } from '@spectrum-web-components/tabs';

### Anatomy

#Section titled Anatomy

The `<sp-tab>` element consists of the following:

*   a label, so that users know which tab panels content will be shown
*   an optional icon
*   a value that programmatically associates the tab with its corresponding tab panel

<sp-tabs>
    <sp-tab label="Tab cola" value="tab-cola">
        <sp-icon-checkmark slot="icon"></sp-icon-checkmark>
    </sp-tab>
    <sp-tab-panel value="tab-cola">
        Tab (or TaB) was a diet cola soft drink from The Coca-Cola Company, introduced in 1963. It is no longer produced.
    </sp-tab-panel>
</sp-tab>

### Options

#Section titled Options

#### Icon only

#Section titled Icon only

For tabs that have an icon and no visible label, the icon should have a `label` attribute in order to set the `aria-label` of the icon. Icons should not be used just as decoration.

<sp-tabs>
  <sp-tab value="complete">
    <sp-icon-checkmark slot="icon" label="Checking your work" ></sp-icon-checkmark>
  </sp-tab>
  <sp-tab-panel value="complete">
    A screenreader will read this tab as "Checking your work"
  </sp-tab-panel>
</sp-tabs>

#### Label only

#Section titled Label only

The label can be provided via the `label` attribute or the default slot:

<sp-tabs>
    <sp-tab label="Tab using an attribute" value="attribute">
    </sp-tab>
    <sp-tab-panel value="attribute">
        This tab uses the `label` attribute to label the tab.
    </sp-tab-panel>
    <sp-tab value="slot">
        Tab using slot
    </sp-tab>
    <sp-tab-panel value="slot">
        This tab uses the default slot to label the tab.
    </sp-tab-panel>
</sp-tab>
The `label` attribute provides the visible text content and accessible name for screen readers. The `value` attribute links the tab to its corresponding `sp-tab-panel` via matching values.

### States

#Section titled States

In order to activate the `<sp-tab>` element's interactive states, it must be used within an `<sp-tabs>` element.

#### Selected state

#Section titled Selected state

The tab is currently active and its associated panel is visible.

<sp-tabs>
  <sp-tab selected="label" label="Label" value="1"></sp-tab>
  <sp-tab-panel value="1">This tab is selected.</sp-tab-panel>
</sp-tabs>

#### Focused state

#Section titled Focused state

The tab has keyboard focus. All tabs can receive focus through keyboard navigation, except when the tab is `disabled`.

#### Disabled state

#Section titled Disabled state

When an `<sp-tab>` element is given the `disabled` attribute, it will prevent visitors from selecting that tab and its contents. The ability to select other tabs and their content will remain unrestricted.

<sp-tabs selected="2">
  <sp-tab label="Tab 1" value="1"></sp-tab>
  <sp-tab label="Tab 2" value="2"></sp-tab>
  <sp-tab label="Tab 3" value="3" disabled></sp-tab>
  <sp-tab label="Tab 4" value="4"></sp-tab>
  <sp-tab-panel value="1">Content for Tab 1 is selectable</sp-tab-panel>
  <sp-tab-panel value="2">Content for Tab 2 is selected</sp-tab-panel>
  <sp-tab-panel value="3">Content for Tab 3 is not selectable</sp-tab-panel>
  <sp-tab-panel value="4">Content for Tab 4 is selectable</sp-tab-panel>
</sp-tabs>

### Behaviors

#Section titled Behaviors

#### Selection

#Section titled Selection

*   Clicking a tab selects it and shows its associated panel
*   Only one tab can be selected at a time within a tab group
*   Disabled tabs cannot be selected

#### Events

#Section titled Events

*   `click`: Fired when the tab is clicked
*   `keydown`: Fired when a key is pressed while the tab has focus

### Accessibility

#Section titled Accessibility

#### Best practices

#Section titled Best practices

*   Always provide meaningful text content via `label` attribute or slot content. In rare cases where an icon alone provides enough meaning, use the icon's `label` attribute.
*   Use descriptive `value` attributes that clearly identify the tab's purpose.
*   Ensure tab labels are concise but descriptive.
*   When using icons, provide an appropriate `label` attribute on the icon.

#### Keyboard navigation

#Section titled Keyboard navigation

*   `Tab`: Move focus to the next focusable element
*   `Arrow keys`: Navigate between tabs in the group and move the focus indicator
*   `Enter` or `Space`: Select the focused tab

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false``label``label``string``''``selected``selected``boolean``false``value``value``string``''``vertical``vertical``boolean``false`

### Slots

#Section titled Slots

 Name  Description `default slot` text label of the Tab `icon` The icon that appears on the left of the label 

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/tab/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/tab/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
