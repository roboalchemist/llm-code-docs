# Source: https://opensource.adobe.com/spectrum-web-components/components/color-loupe/

Title: Color Loupe: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/color-loupe/

Published Time: Thu, 12 Mar 2026 20:57:05 GMT

Markdown Content:
Color Loupe: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-color-loupe
==============

NPM 1.11.2

View Storybook

Overview API Changelog

Overview
--------

#Section titled Overview

An `<sp-color-loupe>` shows the output color that would otherwise be covered by a cursor, stylus, or finger during color selection.

### Usage

#Section titled Usage

![Image 3: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/color-loupe?style=for-the-badge)![Image 4: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/color-loupe?style=for-the-badge)

yarn add @spectrum-web-components/color-loupe
Import the side effectful registration of `<sp-color-loupe>` via:

import '@spectrum-web-components/color-loupe/sp-color-loupe.js';
When looking to leverage the `ColorLoupe` base class as a type and/or for extension purposes, do so via:

import { ColorLoupe } from '@spectrum-web-components/color-loupe';

### Anatomy

#Section titled Anatomy

The color loupe consists of:

*   A floating loupe element positioned above the interaction point
*   A color preview that reflects the color currently sampled by its parent color component

<div style="padding: 100px 0 0;">
  <div style="position:relative">
    <sp-color-loupe open="" dir="ltr"></sp-color-loupe>
  </div>
</div>

### Options

#Section titled Options

#### Color

#Section titled Color

The color property sets the visual color displayed within the loupe. This accepts any valid CSS color format.

For a complete list of supported color formats, see the ColorController documentation.

Transparency Support: When using transparent colors, the handle displays an opacity checkerboard pattern background to clearly show the transparency level.

<div style="display: flex; flex-direction: row; justify-content: space-between; align-items: flex-start; width: 100%;;">
  <!-- Yellow color loupe -->
  <div style="padding: 100px 0 0; position: relative; min-width: 120px;">
    <div style="position: relative;">
      <sp-color-loupe color="yellow" open dir="ltr"></sp-color-loupe>
    </div>
  </div>

  <!-- Red color loupe -->
  <div style="padding: 100px 0 0; position: relative; min-width: 120px;">
    <div style="position: relative;">
      <sp-color-loupe color="#ff0000" open dir="ltr"></sp-color-loupe>
    </div>
  </div>

  <!-- Blue color loupe -->
  <div style="padding: 100px 0 0; position: relative; min-width: 120px;">
    <div style="position: relative;">
      <sp-color-loupe color="rgba(44, 62, 224, 0.81)" open dir="ltr" ></sp-color-loupe>
    </div>
  </div>

  <!-- Green color loupe -->
  <div style="padding: 100px 0 0; position: relative; min-width: 120px;">
    <div style="position: relative;">
      <sp-color-loupe color="hsl(111, 82%, 56%)" open dir="ltr" ></sp-color-loupe>
    </div>
  </div>
</div>

### States

#Section titled States

#### Open

#Section titled Open

The `open` attribute controls whether the loupe is visible. When `open` is present, the loupe displays the color preview.

<div style="display: flex; flex-direction: row; gap: 20px;">
  <!-- Loupe is visible -->
  <div style="padding: 100px 0 0; margin-left:20%">
    <div style="position:relative">
      <sp-color-loupe open="" dir="ltr"></sp-color-loupe>
      <p id="color-context" style="margin-top: 40px">
        This loupe above this text is visible.
      </p>
    </div>
  </div>

  <!-- Loupe is hidden -->
  <div style="padding: 100px 0 0;">
    <div style="position:relative">
      <sp-color-loupe dir="ltr"></sp-color-loupe>
      <p id="color-context" style="margin-top: 40px">
        This loupe above this text is not visible.
      </p>
    </div>
  </div>
</div>

### Behaviors

#Section titled Behaviors

The color loupe is typically managed by its parent color component (such as `<sp-color-area>`, `<sp-color-slider>`, or `<sp-color-wheel>`). The loupe automatically appears when the user interacts with the parent component and disappears when the interaction ends.

#### Automatic behavior

#Section titled Automatic behavior

*   **Touch input**: The loupe automatically appears during touch interactions with any color component (`<sp-color-area>`, `<sp-color-slider>`, or `<sp-color-wheel>`) to prevent the finger from obscuring the selected color
*   **Mouse/Stylus input**: The loupe remains hidden by default for precision pointing devices
*   **Parent control**: The loupe's visibility is managed by the parent color component
*   **Accessibility**: The loupe ensures that users can see the selected color even when their finger covers the interaction point

### Accessibility

#Section titled Accessibility

The `<sp-color-loupe>` is designed to work as part of accessible color selection components. The loupe automatically appears during touch interactions with any of these components to ensure the selected color remains visible:

Color-Area<div style="display: flex; flex-direction: row; justify-content: space-between; width: 100%;">
  <sp-color-area aria-label="Saturation and brightness selector - adjust color intensity and lightness" aria-describedby="color-context" ></sp-color-area>
</div>Color-Slider<div style="display: flex; flex-direction: row; justify-content: space-between; width: 100%;">
  <sp-color-slider aria-label="Hue slider - adjust the base color" aria-describedby="color-context" ></sp-color-slider>
</div>Color-Wheel<div style="display: flex; flex-direction: row; justify-content: space-between; width: 100%;">
  <sp-color-wheel aria-label="Color wheel - select from the full color spectrum" aria-describedby="color-context" ></sp-color-wheel>
</div>

#### Screen reader support

#Section titled Screen reader support

The color loupe is rendered as a visual indicator and does not directly interface with screen readers. Accessibility is provided through the parent color component's ARIA implementation.

#### Focus management

#Section titled Focus management

Focus is managed by the parent color component, with the loupe reflecting the focused state visually when its parent component has keyboard focus.

#### Touch accessibility

#Section titled Touch accessibility

*   **Automatic loupe display**: During touch interactions with any color component, the loupe automatically appears to ensure the selected color remains visible
*   **Finger coverage prevention**: The loupe prevents the user's finger from obscuring the color they're selecting
*   **Touch interaction support**: Color components support touch interactions with proper pointer event handling
*   **Visual feedback**: The loupe provides immediate visual feedback during touch interactions

#### Best practices

#Section titled Best practices

*   Ensure the parent color component (for example, `sp-color-area`, `sp-color-slider`, or `sp-color-wheel`) provides appropriate labeling via visible text or ARIA
*   Avoid conveying meaning through color alone; pair color with text, labels, or other indicators as appropriate
*   The loupe is visual-only and should not receive focus. Manage focus on the interactive parent control
*   Test touch interactions on mobile devices to ensure the loupe appears correctly and provides adequate visual feedback

#### Accessible example

#Section titled Accessible example

Provide clear context for what the loupe displays. The loupe itself is presentational and is typically managed by its parent color component. During touch interactions, the loupe automatically appears to ensure the selected color remains visible. The loupe is a visual-only element and doesn't require ARIA attributes since it doesn't provide interactive functionality.

<div role="region" aria-label="Color selection interface" style="padding: 100px 0 0;">
  <div style="position: relative; display: flex; flex-direction: column; align-items: center;" >
    <sp-color-loupe open dir="ltr"></sp-color-loupe>
  </div>
  <p id="color-context" style="margin-top: 8px; text-align: center;">
    The loupe above shows the color currently selected. During touch
    interactions, it automatically appears to prevent your finger from covering
    the selected color.
  </p>
</div>
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

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

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

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 1.1.1 (2025-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

1.1.0 (2025-01-29)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

### 1.0.1 (2024-11-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

1.0.0 (2024-10-31)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.49.0 (2024-10-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.48.0 (2024-09-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.47.1 (2024-08-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.42.4 (2024-05-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.42.0 (2024-03-19)
-------------------

#Section titled 

### Features

#Section titled Features

*   **asset:** use core tokens (99e76f4)

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.41.0 (2024-02-13)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.40.1 (2023-12-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.40.0 (2023-11-16)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.39.4 (2023-11-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.39.2 (2023-10-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.39.1 (2023-10-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.39.0 (2023-09-25)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **color-handle,color-loupe,swatch,thumbnail:** use the Opacity Checkerboard package (47e1fc4)
*   opacity checkerboard inclusion order (#3651) (4f417dc)

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.37.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.35.0 (2023-07-31)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.34.0 (2023-07-11)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **color-loupe:** hide svg from screen readers (#3318) (01e75b7)

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.32.0 (2023-06-01)
-------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **color-handle,color-loupe:** accept updated CSS token names (8c28f6d)

0.31.0 (2023-05-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Bug Fixes

#Section titled Bug Fixes

*   address westbrooks comments (634af60)

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **color-loupe:** add color-loupe pattern (e2f0d15)
*   **color-loupe:** use core tokens (149165c)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)

0.5.0 (2023-04-24)
------------------

#Section titled 

### Features

#Section titled Features

*   **color-loupe:** use core tokens (149165c)

### 0.4.8 (2023-04-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.4.7 (2023-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.4.6 (2023-02-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.4.5 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.4.4 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.4.3 (2022-12-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.4.2 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.4.1 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.4.0 (2022-08-09)
------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

### 0.3.11 (2022-08-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.10 (2022-07-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.9 (2022-06-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.8 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.7 (2022-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.6 (2022-04-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.5 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.4 (2022-03-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.3 (2022-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.2 (2022-01-26)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.3.1 (2021-12-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.3.0 (2021-11-08)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.2.1 (2021-11-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.2.0 (2021-11-02)
------------------

#Section titled 

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)

### 0.1.7 (2021-09-20)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.1.6 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.1.5 (2021-06-16)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.1.4 (2021-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.1.3 (2021-04-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.1.2 (2021-03-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

### 0.1.1 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/color-loupe

0.1.0 (2021-03-05)
------------------

#Section titled 0.1.0 (2021-03-05)

### Bug Fixes

#Section titled Bug Fixes

*   address westbrooks comments (634af60)

### Features

#Section titled Features

*   **color-loupe:** add color-loupe pattern (e2f0d15)

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `color``color``string``'rgba(255, 0, 0, 0.5)'``open``open``boolean``false`

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
