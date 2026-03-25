# Source: https://opensource.adobe.com/spectrum-web-components/tools/base/

Title: Base: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/tools/base/

Published Time: Thu, 12 Mar 2026 20:57:05 GMT

Markdown Content:
Base: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

base
====

NPM 1.11.2

Overview Changelog

Description
-----------

#Section titled Description

The `SpectrumElement` base class as created by mixing `SpectrumMixin` onto `LitElement` provides text direction support via the CSS `:dir()` pseudo-class, which automatically inherits directionality from the DOM hierarchy. In a TypeScript context, it also enforces the presence of `this.shadowRoot` on extending components.

### Usage

#Section titled Usage

![Image 3: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/base?style=for-the-badge)![Image 4: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/base?style=for-the-badge)

yarn add @spectrum-web-components/base

When looking to leverage the `SpectrumElement` base class as a type and/or for extension purposes, do so via:

import { SpectrumElement } from '@spectrum-web-components/base';

export MyElement extends SpectrumElement {}

Similarly the `SpectrumMixin` class factory mixin is available via:

import { SpectrumMixin } from '@spectrum-web-components/base';

export MyElement extends SpectrumMixin(HTMLElement) {}

### Features

#Section titled Features

#### `dir` management

#Section titled dir

Elements built from `SpectrumMixin` leverage the CSS `:dir()` pseudo-class to handle text direction. This modern approach automatically inherits directionality from the DOM hierarchy without requiring explicit `dir` attributes on individual components. The `:dir()` pseudo-class is well-supported across modern browsers and provides a performant, declarative way to manage both "left to right" (LTR) and "right to left" (RTL) content.

To manage content direction in your application, set the `dir` attribute on `document.documentElement` or on an `sp-theme` element. Components will automatically inherit the direction and apply appropriate RTL/LTR styles using CSS selectors like `:host(:dir(rtl))` and `:dir(rtl)`. This allows you to manage content direction in a single place while also enabling multiple content directions on the same page by scoping those content sections with `sp-theme` elements.

When JavaScript access to the direction value is needed, components can use the `dir` getter which returns `getComputedStyle(this).direction` (defaulting to `'ltr'` if not set).

#### public shadowRoot!: ShadowRoot;

#Section titled public shadowRoot!: ShadowRoot;

Elements built from `SpectrumMixin` assume that you will be using shadow DOM in the resulting custom element. To simplify TypeScript usage the presence of `this.shadowRoot` is asserted as non-null so that you have direct access to it without extended type checking.

Changelog
---------

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`6f5419a`]: 
    *   @spectrum-web-components/core@0.0.4

1.11.1
------

#Section titled 1.11.1

### Patch Changes

#Section titled Patch Changes

*   #5993`95e1c25` Thanks @rubencarvalho! - - **Fixed**: Replaced wildcard exports from `@spectrum-web-components/core` with explicit named exports for better bundler compatibility 
    *   **Fixed**: Changed build target from ES2022 to ES2018 to support Vitest and other consumer environments
    *   **Fixed**: Added `@spectrum-web-components/core` as direct dependency to `@spectrum-web-components/shared` to resolve module resolution issues in strict dependency environments
    *   **Fixed**: Added `@lit-labs/observers` as dependency and externalized it in Vite build config

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/core@0.0.3

1.11.0
------

#Section titled 1.11.0

### Patch Changes

#Section titled Patch Changes

*   #5866`9cb816b` Thanks @rubencarvalho! - - **Fixed**: Added `typesVersions` to `@spectrum-web-components/core` to improve TypeScript module resolution for users with `moduleResolution: "node"`. This provides a fallback mechanism when the `exports` field resolution encounters issues, ensuring type declarations are properly resolved across different TypeScript configurations.

*   Updated dependencies [`283f0fe`, `1d76b70`, `9cb816b`]:

    *   @spectrum-web-components/core@0.0.2

1.10.0
------

#Section titled 1.10.0

### Minor Changes

#Section titled Minor Changes

*   No customer-facing changes.

Introduced architectural changes to support side-by-side development of 1st-gen and 2nd-gen components.

1.9.1
-----

#Section titled 1.9.1

1.9.0
-----

#Section titled 1.9.0

1.8.0
-----

#Section titled 1.8.0

1.7.0
-----

#Section titled 1.7.0

1.6.0
-----

#Section titled 1.6.0

1.5.0
-----

#Section titled 1.5.0

1.4.0
-----

#Section titled 1.4.0

1.3.0
-----

#Section titled 1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

1.2.0 (2025-02-27)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 1.1.1 (2025-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

1.1.0 (2025-01-29)
------------------

#Section titled 

### Features

#Section titled Features

*   **sp-button-group:** sp-button-group react to size updates (#5037) (63bc618)

### 1.0.1 (2024-11-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

1.0.0 (2024-10-31)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.49.0 (2024-10-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.48.0 (2024-09-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.47.1 (2024-08-27)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **breadcrumbs:** adjust ref directives imports (#4681) (6e7ba13)

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.42.4 (2024-05-14)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **base:** move lit imports to base (#4416) (b7cb07e)
*   **styles,theme:** add S2 tokens and theme (#4241) (a29e4a2), closes #4232#4228

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.42.0 (2024-03-19)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.41.0 (2024-02-13)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.40.1 (2023-12-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.40.0 (2023-11-16)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.39.4 (2023-11-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.39.2 (2023-10-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.39.1 (2023-10-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.39.0 (2023-09-25)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **base:** add re-export of lit/directive.js (#3616) (d2e237f)
*   **base:** introduce static version property for component class (#3582) (e7e2b76)

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.37.0 (2023-08-18)
-------------------

#Section titled 

### Features

#Section titled Features

*   **overlay:** ship Overlay API v2 (67b5d1b)

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.35.0 (2023-07-31)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.34.0 (2023-07-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.32.0 (2023-06-01)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **base:** ensure streaming listener "streams" on the animation frame (1478db1)

0.31.0 (2023-05-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Features

#Section titled Features

*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)

### Performance Improvements

#Section titled Performance Improvements

*   reduce render cycles when managing "dir" attribute (7b28309)

### 0.7.5 (2023-04-05)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   reduce render cycles when managing "dir" attribute (7b28309)

### 0.7.4 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.7.3 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.7.2 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.7.1 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.7.0 (2022-08-09)
------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

0.6.0 (2022-08-04)
------------------

#Section titled 

### Features

#Section titled Features

*   delivery dev mode messages in various packages (62370a1)

### 0.5.8 (2022-06-29)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add when directive (18b7405)

### 0.5.7 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.5.6 (2022-05-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   move property management into update or willUpdate (f66069f)

### 0.5.5 (2022-04-21)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   allow dir to be managed across multiple connections and disconnections (6d93170)

### 0.5.4 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.5.3 (2022-03-04)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add Grid pattern (341f493)

### 0.5.2 (2022-02-22)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **dialog:** updates for delivering dialog content accessibly (f0ed33c)

### 0.5.1 (2021-12-13)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)

0.5.0 (2021-11-08)
------------------

#Section titled 

### Features

#Section titled Features

*   update lit-* dependencies, wip (377f3c8)

### 0.4.6 (2021-11-08)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)

### 0.4.5 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.4.4 (2021-06-16)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.4.3 (2021-04-09)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   allow for late loading theme scopes (4c7a124)

### 0.4.2 (2021-03-22)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   remove right click value setting (a44968d)

### 0.4.1 (2021-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.4.0 (2021-03-04)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   support a wider number of sizes (ee44978)

### Features

#Section titled Features

*   use latest exports specification (a7ecf4b)

### 0.3.3 (2021-02-11)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   expand sized functionality to support no default and returning to default values (acf3cfb)
*   reduce cycles (8917a5e)

### 0.3.2 (2021-02-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

### 0.3.1 (2021-01-28)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/base

0.3.0 (2021-01-21)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **textfield:** reimplement min/maxlength (23a4c2e)
*   include the "types" entry in package.json files (b432f59)

### Features

#Section titled Features

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **story-decorator:** add story decorator to replace knobs for theme application (7c0c6be)

0.2.0 (2021-01-13)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include the "types" entry in package.json files (b432f59)

### Features

#Section titled Features

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **story-decorator:** add story decorator to replace knobs for theme application (7c0c6be)

### 0.1.3 (2020-10-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **base:** use full file extension (6ea4d9d)

### 0.1.2 (2020-10-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include default export in the "exports" fields (f32407d)

### 0.1.1 (2020-09-25)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   dir should never fall back to null (6b16c6d)

0.1.0 (2020-08-31)
------------------

#Section titled 0.1.0 (2020-08-31)

### Features

#Section titled Features

*   allow dir management by sp-theme elements (2d10158)
*   observe document.documentElement for dir value (da84a9a)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)
*   use 3.0.0-beta.* release for styles (877b485)
*   **base:** insert Spectrum base class/mixin (37c2ee9)

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/tools/base/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/tools/base/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
