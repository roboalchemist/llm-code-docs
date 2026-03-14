# Source: https://opensource.adobe.com/spectrum-web-components/components/status-light/

Title: Status Light: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/status-light/

Published Time: Thu, 12 Mar 2026 20:57:05 GMT

Markdown Content:
Status Light: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-status-light
===============

NPM 1.11.2

View Storybook

Try it on Stackblitz

Overview API Changelog

Overview
--------

#Section titled Overview

An `<sp-status-light>` is a great way to convey semantic meaning, such as statuses and categories. It provides visual indicators through colored dots accompanied by descriptive text.

### Usage

#Section titled Usage

![Image 4: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/status-light?style=for-the-badge)![Image 5: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/status-light?style=for-the-badge)![Image 6: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/status-light

Import the side effectful registration of `<sp-status-light>` via:

import '@spectrum-web-components/status-light/sp-status-light.js';

When looking to leverage the `StatusLight` base class as a type and/or for extension purposes, do so via:

import { StatusLight } from '@spectrum-web-components/status-light';

### Anatomy

#Section titled Anatomy

A status light consists of a colored dot indicator and a required text label. The dot's color represents the status or category, while the text provides additional context.

<sp-status-light variant="positive">approved</sp-status-light>

### Options

#Section titled Options

#### Sizes

#Section titled Sizes

Small<sp-status-light size="s" variant="positive">approved</sp-status-light>Medium<sp-status-light size="m" variant="positive">approved</sp-status-light>Large<sp-status-light size="l" variant="positive">approved</sp-status-light>Extra Large<sp-status-light size="xl" variant="positive">approved</sp-status-light>

#### Variants

#Section titled Variants

Status lights come in various semantic and non-semantic variants to convey different meanings. The `variant` attribute controls the main variant of the status light, with `neutral` being the default.

Semantic<sp-status-light variant="neutral">use for default state</sp-status-light>
<sp-status-light variant="positive">
  use for success or approval
</sp-status-light>
<sp-status-light variant="negative">use for error or rejection</sp-status-light>
<sp-status-light variant="notice">
  use for warning or attention needed
</sp-status-light>
<sp-status-light variant="info">
  use for information or neutral state
</sp-status-light>Non-semantic<sp-status-light variant="yellow">yellow status</sp-status-light>
<sp-status-light variant="fuchsia">fuchsia status</sp-status-light>
<sp-status-light variant="indigo">indigo status</sp-status-light>
<sp-status-light variant="seafoam">seafoam status</sp-status-light>
<sp-status-light variant="chartreuse">chartreuse status</sp-status-light>
<sp-status-light variant="magenta">magenta status</sp-status-light>
<sp-status-light variant="celery">celery status</sp-status-light>
<sp-status-light variant="purple">purple status</sp-status-light>
<sp-status-light variant="cyan">cyan status</sp-status-light>

### States

#Section titled States

#### Disabled

#Section titled Disabled

A status light in a disabled state shows that a status exists, but is not available in that circumstance. This can be used to maintain layout continuity and communicate that a status may become available later.

<sp-status-light variant="positive" disabled>disabled</sp-status-light>

### Accessibility

#Section titled Accessibility

The status light component implements several accessibility features:

*   **ARIA Support**: When disabled, the component automatically sets `aria-disabled="true"`.
*   **Color Meaning**: Colors are used in combination with text labels to ensure that status information is not conveyed through color alone.

#### Best Practices

#Section titled Best Practices

*   Use semantic variants (`positive`, `negative`, `notice`, `info`, `neutral`) when the status has specific meaning
*   Include a clear, descriptive text label that explains the status
*   Consider the disabled state for statuses that exist but are temporarily unavailable
*   Ensure sufficient color contrast between the status light and its background

Changelog
---------

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`6f5419a`]: 
    *   @spectrum-web-components/core@0.0.4
    *   @spectrum-web-components/base@1.11.2

1.11.1
------

#Section titled 1.11.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/core@0.0.3
    *   @spectrum-web-components/base@1.11.1

1.11.0
------

#Section titled 1.11.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`283f0fe`, `1d76b70`, `9cb816b`]: 
    *   @spectrum-web-components/core@0.0.2
    *   @spectrum-web-components/base@1.11.0

1.10.0
------

#Section titled 1.10.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0

1.9.1
-----

#Section titled 1.9.1

### Patch Changes

#Section titled Patch Changes

*   #5813`2811b9e` Thanks @marissahuysentruyt! - **Fixed**: Added missing `accent` and `cyan` variant to status light.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.9.1

1.9.0
-----

#Section titled 1.9.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0

1.8.0
-----

#Section titled 1.8.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0

1.7.0
-----

#Section titled 1.7.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0

1.6.0
-----

#Section titled 1.6.0

### Patch Changes

#Section titled Patch Changes

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.6.0

1.5.0
-----

#Section titled 1.5.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0

1.4.0
-----

#Section titled 1.4.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

1.3.0
-----

#Section titled 1.3.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

1.2.0 (2025-02-27)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 1.1.1 (2025-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

1.1.0 (2025-01-29)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

### 1.0.1 (2024-11-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

1.0.0 (2024-10-31)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.49.0 (2024-10-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.48.0 (2024-09-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.47.1 (2024-08-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.42.4 (2024-05-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.42.0 (2024-03-19)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

### Features

#Section titled Features

*   **asset:** use core tokens (99e76f4)

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.41.0 (2024-02-13)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.40.1 (2023-12-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.40.0 (2023-11-16)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.39.4 (2023-11-02)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **overlay:** place longpress helper content in a more accessible, less layout affecting location (dd12c23)

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.39.2 (2023-10-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.39.1 (2023-10-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.39.0 (2023-09-25)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.37.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.35.0 (2023-07-31)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.34.0 (2023-07-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.32.0 (2023-06-01)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.31.0 (2023-05-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Bug Fixes

#Section titled Bug Fixes

*   correct @element jsDoc listing across library (c97a632)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   **shared:** make Focusable pass disabled always (a339d6f)
*   **status-light:** extend docs and styling for [disabled] (3d9fd16)
*   **status-light:** manage aria-disabled from disabled attribute (8bc9be7)
*   **status-light:** review comments for status-light (80caa08)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **status-light:** add status-light component (e3a5b3d)
*   **status-light:** update spectrum css input (e10fd45)
*   **tabs:** add sp-tab-panel element (b17d276)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)
*   use SixedMixin to manage "size" property (8819821)

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)

### Reverts

#Section titled Reverts

*   Revert "chore: release new versions" (a6d655d)

### 0.11.11 (2023-04-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.10 (2023-04-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.9 (2023-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.8 (2023-02-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.7 (2023-02-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.6 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.5 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.4 (2022-12-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.3 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.2 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.11.1 (2022-10-10)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.11.0 (2022-08-09)
-------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

### 0.10.12 (2022-08-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.11 (2022-07-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.10 (2022-06-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.9 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.8 (2022-05-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.7 (2022-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.6 (2022-04-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.5 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.4 (2022-03-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.3 (2022-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.2 (2022-01-26)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.10.1 (2021-12-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.10.0 (2021-11-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.9.1 (2021-11-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.9.0 (2021-11-02)
------------------

#Section titled 

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)

### 0.8.3 (2021-09-20)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.8.2 (2021-08-24)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   correct @element jsDoc listing across library (c97a632)

### 0.8.1 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.8.0 (2021-06-16)
------------------

#Section titled 

### Features

#Section titled Features

*   **tabs:** add sp-tab-panel element (b17d276)

### 0.7.5 (2021-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.7.4 (2021-04-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.7.3 (2021-03-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.7.2 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.7.1 (2021-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.7.0 (2021-03-04)
------------------

#Section titled 

### Features

#Section titled Features

*   use latest exports specification (a7ecf4b)

### 0.6.1 (2021-02-11)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update to latest spectrum-css packages (a5ca19f)

0.6.0 (2021-01-21)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **status-light:** update spectrum css input (e10fd45)

0.5.0 (2021-01-13)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **status-light:** update spectrum css input (e10fd45)

### 0.4.3 (2020-10-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.4.2 (2020-10-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include default export in the "exports" fields (f32407d)

### 0.4.1 (2020-09-25)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update side effect listings (8160d3a)

0.4.0 (2020-08-31)
------------------

#Section titled 

### Features

#Section titled Features

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

### 0.3.1 (2020-08-19)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

0.3.0 (2020-07-17)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **status-light:** manage aria-disabled from disabled attribute (8bc9be7)

### Features

#Section titled Features

*   leverage "exports" field in package.json (321abd7)

### 0.2.6 (2020-06-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.2.5 (2020-04-16)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)

### 0.2.4 (2020-04-07)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **status-light:** extend docs and styling for disabled

### 0.2.3 (2020-03-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.2.2 (2020-01-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/status-light

### 0.2.1 (2019-11-27)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include "type" in package.json, generate custom-elements.json (1a8d716)

0.2.0 (2019-11-19)
------------------

#Section titled 

### Features

#Section titled Features

*   use @adobe/spectrum-css@2.15.1 (3918888)

### 0.1.1 (2019-11-01)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **shared:** make Focusable pass disabled always (a339d6f)

0.1.0 (2019-10-23)
------------------

#Section titled 0.1.0 (2019-10-23)

### Bug Fixes

#Section titled Bug Fixes

*   **status-light:** review comments for status-light (80caa08)

### Features

#Section titled Features

*   **status-light:** add status-light component (e3a5b3d)

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false``variant``variant``StatusLightVariantS1``'info'` The variant of the status light. 

### Slots

#Section titled Slots

 Name  Description `default slot` text label of the Status Light 

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/status-light/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/status-light/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
