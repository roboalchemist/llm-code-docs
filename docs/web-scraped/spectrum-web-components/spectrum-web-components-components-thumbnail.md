# Source: https://opensource.adobe.com/spectrum-web-components/components/thumbnail/

Title: Thumbnail: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/thumbnail/

Published Time: Thu, 12 Mar 2026 20:57:05 GMT

Markdown Content:
Thumbnail: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-thumbnail
============

NPM 1.11.2

View Storybook

Try it on Stackblitz

Overview API Changelog

Overview
--------

#Section titled Overview

An `sp-thumbnail` can be used in a variety of locations as a way to display a preview of an image, layer, or effect.

### Usage

#Section titled Usage

![Image 4: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/thumbnail?style=for-the-badge)![Image 5: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/thumbnail?style=for-the-badge)![Image 6: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/thumbnail
Import the side effectful registration of `<sp-thumbnail>` via:

import '@spectrum-web-components/thumbnail/sp-thumbnail.js';
When looking to leverage the `Thumbnail` base class as a type and/or for extension purposes, do so via:

import { Thumbnail } from '@spectrum-web-components/thumbnail';

### Options

#Section titled Options

#### Sizes

#Section titled Sizes

50<sp-thumbnail size="50">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>75<sp-thumbnail size="75">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>100<sp-thumbnail size="100">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>200<sp-thumbnail size="200">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>300<sp-thumbnail size="300">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>400<sp-thumbnail size="400">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>500<sp-thumbnail size="500">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>600<sp-thumbnail size="600">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>700<sp-thumbnail size="700">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>800<sp-thumbnail size="800">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>900<sp-thumbnail size="900">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>1000<sp-thumbnail size="1000">
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>

#### Representing non-square content

#Section titled Representing non-square content

By default, an `sp-thumbnail` will ensure that the entirety of the content that it respresents is visible by letterboxing that content with a checkerboard background when its aspect ratio is not square.

<div style="display: flex; gap: var(--spectrum-spacing-100);">
  <sp-thumbnail>
    <img src="https://picsum.photos/300/400" alt="Demo Image" />
  </sp-thumbnail>

  <sp-thumbnail>
    <img src="https://picsum.photos/500/100" alt="Demo Image" />
  </sp-thumbnail>
</div>
The `background` attribute takes a string value of the CSS "background" property in order to customize the letterboxing.

<div style="display: flex; gap: var(--spectrum-spacing-100);">
  <sp-thumbnail background="red">
    <img src="https://picsum.photos/300/400" alt="Demo Image" />
  </sp-thumbnail>

  <sp-thumbnail background="#00ff00">
    <img src="https://picsum.photos/500/100" alt="Demo Image" />
  </sp-thumbnail>
</div>
The `cover` attribute will cause the content to fill the space provided by the `sp-thumbnail` element:

<div style="display: flex; gap: var(--spectrum-spacing-100);">
  <sp-thumbnail cover>
    <img src="https://picsum.photos/300/400" alt="Demo Image" />
  </sp-thumbnail>

  <sp-thumbnail cover>
    <img src="https://picsum.photos/500/100" alt="Demo Image" />
  </sp-thumbnail>
</div>

#### Layer and Layer Selected

#Section titled Layer and Layer Selected

For when `sp-thumbail` is used in layer management (such as the Compact or Detail Layers panels). The thumbnail is given a thick blue border to indicate its selection when used in layer management.

<div style="display: flex; gap: var(--spectrum-spacing-100);">
  <sp-thumbnail layer>
    <img src="https://picsum.photos/400/400" alt="Demo Image" />
  </sp-thumbnail>

  <sp-thumbnail layer selected>
    <img src="https://picsum.photos/500/100" alt="Demo Image" />
  </sp-thumbnail>
</div>

### States

#Section titled States

#### Focused

#Section titled Focused

When `focused` the `sp-thumbnail` element will be displayed as follows:

<sp-thumbnail focused>
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>

#### Disabled

#Section titled Disabled

Thumbnail should only be displayed as disabled if the entire component is also disabled. When `disabled` the `sp-thumbnail` element will be displayed as follows:

<sp-thumbnail disabled>
  <img src="https://picsum.photos/100/100" alt="Demo Image" />
</sp-thumbnail>

### Accessibility

#Section titled Accessibility

`alt` attributes must be set on the `img` element inside of the `sp-thumbnail` element.

Changelog
---------

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/opacity-checkerboard@1.11.2

1.11.1
------

#Section titled 1.11.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/opacity-checkerboard@1.11.1

1.11.0
------

#Section titled 1.11.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/opacity-checkerboard@1.11.0

1.10.0
------

#Section titled 1.10.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/opacity-checkerboard@1.10.0

1.9.1
-----

#Section titled 1.9.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/opacity-checkerboard@1.9.1

1.9.0
-----

#Section titled 1.9.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/opacity-checkerboard@1.9.0

1.8.0
-----

#Section titled 1.8.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/opacity-checkerboard@1.8.0

1.7.0
-----

#Section titled 1.7.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/opacity-checkerboard@1.7.0

1.6.0
-----

#Section titled 1.6.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/opacity-checkerboard@1.6.0

1.5.0
-----

#Section titled 1.5.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/opacity-checkerboard@1.5.0

1.4.0
-----

#Section titled 1.4.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/opacity-checkerboard@1.4.0

1.3.0
-----

#Section titled 1.3.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/opacity-checkerboard@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

1.2.0 (2025-02-27)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 1.1.1 (2025-01-29)

#Section titled 

### Features

#Section titled Features

*   **thumbnail:** bump thumbnail to use foundations release (7490324)

1.1.0 (2025-01-29)
------------------

#Section titled 

### Features

#Section titled Features

*   **thumbnail:** bump thumbnail to use foundations release (7490324)

### 1.0.1 (2024-11-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

1.0.0 (2024-10-31)
------------------

#Section titled 

### BREAKING CHANGES

#Section titled BREAKING CHANGES

*   remove thumbnail deprecated sizes (#4760)

0.49.0 (2024-10-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.48.0 (2024-09-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.47.1 (2024-08-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.42.4 (2024-05-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.42.0 (2024-03-19)
-------------------

#Section titled 

### Features

#Section titled Features

*   **asset:** use core tokens (99e76f4)

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.41.0 (2024-02-13)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.40.1 (2023-12-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.40.0 (2023-11-16)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.39.4 (2023-11-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.39.2 (2023-10-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.39.1 (2023-10-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.39.0 (2023-09-25)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **color-handle,color-loupe,swatch,thumbnail:** use the Opacity Checkerboard package (47e1fc4)

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.37.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.35.0 (2023-07-31)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.34.0 (2023-07-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.32.0 (2023-06-01)
-------------------

#Section titled 

### Features

#Section titled Features

*   **thumbnail:** use core tokens (e298035)

0.31.0 (2023-05-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Bug Fixes

#Section titled Bug Fixes

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   use latest @spectrum-css/thumbnail with built in "cover" support (d152b4e)

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   leverage latest Spectrum button API (9faeade)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   **thumbnail:** add the thumbnail package (56935d5)

### 0.6.9 (2023-04-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.8 (2023-04-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.7 (2023-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.6 (2023-02-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.5 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.4 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.3 (2022-12-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.2 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.6.1 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.6.0 (2022-08-09)
------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

### 0.5.7 (2022-08-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.5.6 (2022-07-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.5.5 (2022-06-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.5.4 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.5.3 (2022-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.5.2 (2022-04-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.5.1 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.5.0 (2022-03-04)
------------------

#Section titled 

### Features

#Section titled Features

*   leverage latest Spectrum button API (9faeade)

### 0.4.4 (2022-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.4.3 (2022-01-26)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.4.2 (2022-01-07)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   use latest @spectrum-css/thumbnail with built in "cover" support (d152b4e)

### 0.4.1 (2021-12-13)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)

0.4.0 (2021-11-08)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.3.1 (2021-11-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.3.0 (2021-11-02)
------------------

#Section titled 

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)

### 0.2.5 (2021-10-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.2.4 (2021-09-20)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.2.3 (2021-08-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.2.2 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.2.1 (2021-06-16)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.2.0 (2021-06-07)
------------------

#Section titled 

### Features

#Section titled Features

*   **tabs:** add sp-tab-panel element (b17d276)

### 0.1.5 (2021-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.1.4 (2021-04-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.1.3 (2021-03-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.1.2 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

### 0.1.1 (2021-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/thumbnail

0.1.0 (2021-03-04)
------------------

#Section titled 0.1.0 (2021-03-04)

### Features

#Section titled Features

*   **thumbnail:** add the thumbnail package (56935d5)

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `background``background``string | undefined``cover``cover``boolean``false``layer``layer``boolean``false``size``size``ThumbnailSize`

### Slots

#Section titled Slots

 Name  Description `image` image element to present in the Thumbnail 

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
