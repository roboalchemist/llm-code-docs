# Source: https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/

Title: Breadcrumb Item: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/

Markdown Content:
Breadcrumb Item: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-breadcrumb-item
==================

compact true false

label

max-visible-items

NPM 1.11.2

View Storybook

Overview API

Overview
--------

#Section titled Overview

For use within an `<sp-breadcrumbs>` element, an `<sp-breadcrumb-item>` represents a single item in a breadcrumbs list. The default slot contains the main content of the breadcrumb item.

### Usage

#Section titled Usage

![Image 3: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/breadcrumbs?style=for-the-badge)![Image 4: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/breadcrumbs?style=for-the-badge)

yarn add @spectrum-web-components/breadcrumbs
Import the side effectful registration of `<sp-breadcrumb-item>` as follows:

import '@spectrum-web-components/breadcrumbs/sp-breadcrumb-item.js';
When looking to leverage the `BreadcrumbItem` base class as a type and/or for extension purposes, do so via:

import { BreadcrumbItem } from '@spectrum-web-components/breadcrumbs';

### Anatomy

#Section titled Anatomy

The breadcrumb item consists of the following:

*   A clickable anchor (`<a>`) that contains the breadcrumb text and handles navigation
*   Text content as the main label displayed in the default slot, which becomes the clickable link text
*   A separator consisting of a chevron UI icon component (`<sp-icon-chevron100>`) that visually separates breadcrumb items
*   An optional action menu for displaying overflowed breadcrumb items

### Options

#Section titled Options

#### Value or href attributes

#Section titled Value or href attributes

When using the `href` attribute instead of the `value` attribute, the breadcrumb item behaves as a regular anchor link.

Value<sp-breadcrumbs>
  <sp-breadcrumb-item value="home">Home</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">March 2019 Assets</sp-breadcrumb-item>
</sp-breadcrumbs>Link<sp-breadcrumbs>
  <sp-breadcrumb-item href="/home">Home</sp-breadcrumb-item>
  <sp-breadcrumb-item href="/trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item href="/assets">March 2019 Assets</sp-breadcrumb-item>
</sp-breadcrumbs>

#### With menu content

#Section titled With menu content

When breadcrumbs overflow, `<sp-breadcrumbs>` will create an `<sp-breadcrumb-item>` with an `<sp-action-menu>` that contains the full list of breadcrumb items in reading order.

<sp-breadcrumbs max-visible-items="2">
  <sp-breadcrumb-item slot="root" value="your_stuff">
    Your stuff
  </sp-breadcrumb-item>
  <sp-breadcrumb-item value="team">Files</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="winter">Winter</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">Assets</sp-breadcrumb-item>
  <sp-breadcrumb-item value="18x24">18x24</sp-breadcrumb-item>
</sp-breadcrumbs>

### States

#Section titled States

#### Disabled

#Section titled Disabled

An `sp-breadcrumb-item` can have a `disabled` state which disables the events from that item.

<sp-breadcrumbs>
  <sp-breadcrumb-item disabled value="home">Home</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">March 2019 Assets</sp-breadcrumb-item>
</sp-breadcrumbs>

### Accessibility

#Section titled Accessibility

The `<sp-breadcrumb-item>` component provides the following accessibility features:

*   Automatically applies `role="listitem"` to ensure proper semantic meaning for assistive technologies
*   The last breadcrumb item automatically receives `aria-current="page"` to indicate the current location
*   Applies `aria-disabled="true"` when the `disabled` property is set
*   Each breadcrumb item is keyboard accessible with `tabindex="0"`
*   Supports `Enter` key activation for navigation

#### Best practices

#Section titled Best practices

*   **Provide meaningful text content**: Ensure each breadcrumb item has descriptive and meaningful labels
*   **Use proper hierarchy**: Place breadcrumb items in the correct order from root to current page
*   **Handle navigation events**: Listen for the `breadcrumb-select` event when using `value` instead of `href`
*   **Keep labels concise**: Use short, descriptive labels that clearly identify each level

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `value``value``string | undefined``undefined`

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
