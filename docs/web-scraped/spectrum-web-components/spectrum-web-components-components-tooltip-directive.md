# Source: https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/

Title: Tooltip Directive: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/

Markdown Content:
Tooltip Directive: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

tooltip-directive
=================

NPM 1.11.2

View Storybook

Try it on Stackblitz

Overview

Overview
--------

#Section titled Overview

While `<sp-tooltip>` elements are generally fairly innocuous amounts of DOM, it is possible impact performance with too many Tooltips. To support consumers that use `lit-html`, Spectrum Web Components also proives a directive to improve performance when using many `<sp-tooltip>` elements.

### Usage

#Section titled Usage

yarn add @spectrum-web-components/tooltip

Import the tooltip directive as follows:

import { tooltip } from '@spectrum-web-components/tooltip/src/tooltip-directive.js';

### Anatomy

#Section titled Anatomy

The tooltip directive consists of two main parts:

1.   A method returning the `TemplateResult` defining the content of the open overlay:

() => TemplateResult;
1.   An optional options object for configuring the tooltip behavior:

{
    open?: boolean; // Whether the Overlay in question should be rendered open.
    triggerInteraction: TriggerInteraction; // 'click' | 'longpress' | 'hover'
    overlayOptions: OverlayOptions;
    insertionOptions?: InsertionOptions;
    variant: 'info' | 'positive' | 'negative';
}

### Options

#Section titled Options

#### Overlay Options

#Section titled Overlay Options

The `overlayOptions` are leveraged in the same way as outlined here.

#### Insertion Options

#Section titled Insertion Options

The `insertionOptions` define where in the DOM the Overlay should be inserted:

type InsertionOptions = {
  el: HTMLElement | (() => HTMLElement); // returning a reference to the element the Overlay should be inserted adjacent to
  where: InsertPosition; // 'afterbegin' | 'afterend' | 'beforebegin' | 'beforeend'
};

### Behaviors

#Section titled Behaviors

#### Consumption via `lit-html`

#Section titled Consumption via 

The `tooltip()` directive will automatically wrap whatever content you provide in an `<sp-tooltip>` element. Pass a `TemplateResult` into the `tooltip()` directive to have it rendered to the DOM when the associated Tooltip is about to open and then removed after the Tooltip has closed.

<div id="root"></div>

<script type="module"> import { tooltip } from '@spectrum-web-components/tooltip/src/tooltip-directive.js'; import { html, render } from 'lit-html'; const renderOverlayContent = () => html` <p>Tooltip content</p> `; const template = html` <sp-button ${tooltip(renderOverlayContent, { variant: 'negative' })}>Trigger</sp-button> `; customElements.whenDefined('code-example').then(() => { Promise.all([...document.querySelectorAll('code-example')].map(example => example.updateComplete)).then(() => { const appRoot = document.querySelector('#root'); appRoot.innerHTML = ''; render(template, appRoot); }); });</script>

### Accessibility

#Section titled Accessibility

The tooltip directive automatically manages accessibility features:

*   Tooltips are associated with their trigger elements via `aria-describedby`
*   Content is only rendered when needed, reducing DOM complexity
*   Hover and focus interactions are handled automatically
*   Keyboard navigation support is built-in

For more information on accessibility, see the Accessibility section of the tooltip component.

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
