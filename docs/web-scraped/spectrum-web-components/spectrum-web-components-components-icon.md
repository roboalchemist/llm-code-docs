# Source: https://opensource.adobe.com/spectrum-web-components/components/icon/

Title: Icon: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/icon/

Published Time: Thu, 12 Mar 2026 20:57:05 GMT

Markdown Content:
Icon: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-icon
=======

NPM 1.11.2

View Storybook

Overview API Changelog

Overview
--------

#Section titled Overview

`<sp-icon>` renders an icon to the page. By default the `name` attribute will pair with separately registered icon sets to deliver the icons. When not present, `<sp-icon>` will subsequently check for its `src` attribute which could populate the icon via an image, and then fallback to any slotted content for an element based icon.

### Usage

#Section titled Usage

![Image 3: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/icon?style=for-the-badge)![Image 4: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/icon?style=for-the-badge)

yarn add @spectrum-web-components/icon

Import the side effectful registration of `<sp-icon>` via:

import '@spectrum-web-components/icon/sp-icon.js';

When looking to leverage the `Icon` base class as a type and/or for extension purposes, do so via:

import { Icon } from '@spectrum-web-components/icon';

### Example

#Section titled Example

Names of the icons on this page are provided by the `<sp-icons-medium>` icon set. Learn how to create your own via `sp-iconset`.

<sp-icons-medium></sp-icons-medium>
<sp-icon name="ui:Arrow100"></sp-icon>

### Options

#Section titled Options

#### Sizes

#Section titled Sizes

Icons are available in various sizes in Spectrum ranging from `s` to `xxl`. By default an `sp-icon` without a `size` attribute will appear as if it were `size="m"`. We can specify the size via `size` attribute.

<sp-icon size="s" name="ui:Arrow100"></sp-icon>
<sp-icon size="m" name="ui:Arrow100"></sp-icon>
<sp-icon size="l" name="ui:Arrow100"></sp-icon>
<sp-icon size="xl" name="ui:Arrow100"></sp-icon>
<sp-icon size="xxl" name="ui:Arrow100"></sp-icon>

#### Icon colors

#Section titled Icon colors

Icons apply their color as `currentColor`, so change the `color` property of the element for customization.

<sp-icon name="ui:Arrow100" style="color: red;"></sp-icon>

#### Image icon

#Section titled Image icon

An image icon can be supplied via the `src` attribute. Remember that you cannot style the contents of an image via CSS, so use graphics that are appropriate for your application's design requirements.

<sp-icon label="Previous" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0yOTU3Ljk5NSAtNTUzMC4wMzIgNiAxMCI+PGRlZnM+PHN0eWxlPi5he2ZpbGw6bm9uZTtzdHJva2U6IzE0NzNlNjtzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtbGluZWpvaW46cm91bmQ7c3Ryb2tlLW1pdGVybGltaXQ6MTA7c3Ryb2tlLXdpZHRoOjJweDt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImEiIGQ9Ik0yNTEuMywzMzNsNC00LTQtNCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTI3MDEuNjk1IC01MTk2LjAzMikgcm90YXRlKDE4MCkiLz48L3N2Zz4="></sp-icon>

#### HTML/SVG Element icon

#Section titled HTML/SVG Element icon

Icons can also be supplied via HTML elements and are applied via the default `<slot>`.

<sp-icon>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 22 22" role="img" fill="currentColor" height="18" width="18" aria-hidden="true" >
    <path d="M19.75,10.04h-15l5.97-5.97a.483.483,0,0,0,0-.7l-.35-.36a.513.513,0,0,0-.71,0L2.24,10.44a.513.513,0,0,0,0,.71l7.39,7.84a.513.513,0,0,0,.71,0l.35-.35a.513.513,0,0,0,0-.71L4.76,11.5H19.75a.25.25,0,0,0,.25-.25v-.96A.25.25,0,0,0,19.75,10.04Z" ></path>
  </svg>
</sp-icon>

### Accessibility

#Section titled Accessibility

If no meaning is lost by visually hiding an icon, it is considered decorative. Decorative icons should not have a label and should be hidden from assistive technology. `aria-hidden` is set to true by default for icons.

If an icon does add meaning, a label is required. Use the `label` attribute to set the label's text as the `aria-label` of the icon and remove the `aria-hidden` attribute.

<sp-icon name="ui:Arrow100" label="Arrow pointing to the right"></sp-icon>
Changelog
---------

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/iconset@1.11.2

1.11.1
------

#Section titled 1.11.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/iconset@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

1.11.0
------

#Section titled 1.11.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`b95e254`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/iconset@1.11.0

1.10.0
------

#Section titled 1.10.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/iconset@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

1.9.1
-----

#Section titled 1.9.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1

1.9.0
-----

#Section titled 1.9.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/iconset@1.9.0
    *   @spectrum-web-components/base@1.9.0

1.8.0
-----

#Section titled 1.8.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0

1.7.0
-----

#Section titled 1.7.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.7.0
    *   @spectrum-web-components/base@1.7.0

1.6.0
-----

#Section titled 1.6.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.6.0
    *   @spectrum-web-components/base@1.6.0

1.5.0
-----

#Section titled 1.5.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.5.0
    *   @spectrum-web-components/base@1.5.0

1.4.0
-----

#Section titled 1.4.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.4.0
    *   @spectrum-web-components/base@1.4.0

1.3.0
-----

#Section titled 1.3.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

1.2.0 (2025-02-27)
------------------

#Section titled 

### Features

#Section titled Features

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 1.1.1 (2025-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

1.1.0 (2025-01-29)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

### Features

#Section titled Features

*   add an optional chromatic vrt action (7d2f840)

### 1.0.3 (2024-12-09)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **toast:** adds iconLabel to address accessibility (#4944) (8121057)

### 1.0.1 (2024-11-11)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **icon:** remove size300 suffix from chevron and checkmark icons in Spectrum 2 (#4904) (a22f42b)

1.0.0 (2024-10-31)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.49.0 (2024-10-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.48.0 (2024-09-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.47.1 (2024-08-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.42.4 (2024-05-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.42.0 (2024-03-19)
-------------------

#Section titled 

### Features

#Section titled Features

*   **asset:** use core tokens (99e76f4)

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.41.0 (2024-02-13)
-------------------

#Section titled 

### Features

#Section titled Features

*   **icon:** use core tokens (a11ef6b)

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.40.1 (2023-12-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.40.0 (2023-11-16)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.39.4 (2023-11-02)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **infield-button:** add infield-button package (057b885)

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.39.2 (2023-10-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.39.1 (2023-10-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.39.0 (2023-09-25)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **alert-dialog:** add Alert Dialog package (#3501) (1062847)

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.37.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.35.0 (2023-07-31)
-------------------

#Section titled 

### Features

#Section titled Features

*   **action-bar:** use core tokens (4e21edf)

0.34.0 (2023-07-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.32.0 (2023-06-01)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.31.0 (2023-05-17)
-------------------

#Section titled 

### Features

#Section titled Features

*   **icon:** image src invalid error api (19e06f9)
*   **icon:** review comment changes (ba75d94)
*   **icon:** review comment changes (4597713)
*   **icon:** review comment changes (19287fb)
*   **icon:** review comment changes (dee1929)
*   **icon:** review comment changes (cb41b33)
*   **icon:** skipping test case for webkit (fa4b903)

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Bug Fixes

#Section titled Bug Fixes

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)
*   correct @element jsDoc listing across library (c97a632)
*   ensure browser understandable extensions (f4e59f7)
*   **icon:** clean up docs and types for available size values (c38850d)
*   **icon:** prevent async race resulting in multiple inner SVG elements (b05e2d5)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   manage updated node types (0517fc1)
*   normalize "event" and "error" argument names (8d382cd)
*   remove ":" based namespacing of events (d77a843)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **icon:** add UIIcon styles (6f03b1a)
*   **icon:** allow `<sp-icon>` to accept a slotted icon (cbf7a07)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **icon:** update spectrum css input (42f17db)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

### Reverts

#Section titled Reverts

*   Revert "chore: release new versions" (a6d655d)

### 0.12.11 (2023-04-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.10 (2023-04-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.9 (2023-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.8 (2023-02-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.7 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.6 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.5 (2022-12-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.4 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.3 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.12.2 (2022-10-28)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   manage updated node types (0517fc1)

### 0.12.1 (2022-10-10)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.12.0 (2022-08-09)
-------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

### 0.11.12 (2022-08-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.11 (2022-07-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.10 (2022-06-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.9 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.8 (2022-05-27)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update consumption of Spectrum CSS for latest version (ed2305b)

### 0.11.7 (2022-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.6 (2022-04-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.5 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.4 (2022-03-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.3 (2022-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.2 (2022-01-26)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.11.1 (2021-12-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.11.0 (2021-11-08)
-------------------

#Section titled 

### Features

#Section titled Features

*   update lit-* dependencies, wip (377f3c8)

### 0.10.1 (2021-11-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.10.0 (2021-11-02)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **icon:** prevent async race resulting in multiple inner SVG elements (b05e2d5)

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)

### 0.9.11 (2021-09-20)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.10 (2021-08-24)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   correct @element jsDoc listing across library (c97a632)

### 0.9.9 (2021-08-03)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)

### 0.9.8 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.7 (2021-06-16)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.6 (2021-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.5 (2021-04-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.4 (2021-03-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.3 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.2 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.9.1 (2021-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.9.0 (2021-03-04)
------------------

#Section titled 

### Features

#Section titled Features

*   use latest exports specification (a7ecf4b)

### 0.8.3 (2021-02-11)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update to latest spectrum-css packages (a5ca19f)

### 0.8.2 (2021-02-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.8.1 (2021-01-28)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

0.8.0 (2021-01-21)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **icon:** clean up docs and types for available size values (c38850d)
*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   **icon:** update spectrum css input (42f17db)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

0.7.0 (2021-01-13)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   **icon:** update spectrum css input (42f17db)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

### 0.6.3 (2020-10-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.6.2 (2020-10-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include default export in the "exports" fields (f32407d)

### 0.6.1 (2020-09-25)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update side effect listings (8160d3a)

0.6.0 (2020-08-31)
------------------

#Section titled 

### Features

#Section titled Features

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

### 0.5.2 (2020-08-19)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.5.1 (2020-07-24)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   ensure browser understandable extensions (f4e59f7)

0.5.0 (2020-07-17)
------------------

#Section titled 

### Features

#Section titled Features

*   **overlay:** manage focus throwing and tab trapping (27a0b53)
*   leverage "exports" field in package.json (321abd7)

### 0.4.8 (2020-06-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.4.7 (2020-05-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.4.6 (2020-04-16)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)

### 0.4.5 (2020-04-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.4.4 (2020-03-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.4.3 (2020-01-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/icon

### 0.4.2 (2019-12-02)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   normalize "event" and "error" argument names (8d382cd)

### 0.4.1 (2019-11-27)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include "type" in package.json, generate custom-elements.json (1a8d716)

0.4.0 (2019-11-19)
------------------

#Section titled 

### Features

#Section titled Features

*   use @adobe/spectrum-css@2.15.1 (3918888)

0.3.0 (2019-11-01)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   remove ":" based namespacing of events (d77a843)

### Features

#Section titled Features

*   **icon:** allow `<sp-icon>` to accept a slotted icon (cbf7a07)

0.2.0 (2019-10-14)
------------------

#Section titled 

### Features

#Section titled Features

*   **icon:** add UIIcon styles (6f03b1a)

### Performance Improvements

#Section titled Performance Improvements

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

0.1.3 (2019-10-03)
------------------

#Section titled 0.1.3 (2019-10-03)

**Note:** Version bump only for package @spectrum-web-components/icon

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `label``label``string``''``name``name``string | undefined``size``size``'xxs' | 'xs' | 's' | 'm' | 'l' | 'xl' | 'xxl' | undefined``src``src``string | undefined`

### Events

#Section titled Events

 Name  Type  Description `error``Event`

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/icon/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/icon/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
