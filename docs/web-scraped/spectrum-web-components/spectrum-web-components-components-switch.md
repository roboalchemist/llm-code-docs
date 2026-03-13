# Source: https://opensource.adobe.com/spectrum-web-components/components/switch/

Title: Switch: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/switch/

Published Time: Thu, 12 Mar 2026 20:57:05 GMT

Markdown Content:
Switch: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-switch
=========

NPM 1.11.2

View Storybook

Try it on Stackblitz

Overview API Changelog

Overview
--------

#Section titled Overview

An `<sp-switch>` is used to turn an option on or off. Switches allow users to select the state of a single option at a time. Use a switch rather than a checkbox when activating (or deactivating) an option, instead of selecting.

### Usage

#Section titled Usage

![Image 4: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/switch?style=for-the-badge)![Image 5: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/switch?style=for-the-badge)![Image 6: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/switch

Import the side effectful registration of `<sp-switch>` via:

import '@spectrum-web-components/switch/sp-switch.js';

When looking to leverage the `Switch` base class as a type and/or for extension purposes, do so via:

import { Switch } from '@spectrum-web-components/switch';

### Anatomy

#Section titled Anatomy

A switch consists of a switch input and slotted label.

<sp-switch>Email notifications</sp-switch>

#### Checked

#Section titled Checked

A switch can be checked by setting the `checked` property/attribute.

<sp-field-group vertical>
  <sp-switch>Not checked</sp-switch>
  <sp-switch checked>Checked</sp-switch>
</sp-field-group>

### Options

#Section titled Options

#### Sizes

#Section titled Sizes

Small<sp-switch size="s">Small</sp-switch>Medium<sp-switch size="m">Medium</sp-switch>Large<sp-switch size="l">Large</sp-switch>Extra Large<sp-switch size="xl">Extra Large</sp-switch>

#### Emphasized

#Section titled Emphasized

Emphasized switches, which use the `empahasized` attribute/property are a secondary style for switches. The blue color provides a visual prominence that is optimal for forms, settings, etc. where the switches need to be noticed.

<sp-field-group vertical>
  <sp-switch emphasized>Emphasized</sp-switch>
  <sp-switch emphasized checked>Emphasized and checked</sp-switch>
</sp-field-group>

### States

#Section titled States

A switch can be disabled using the `disabled` property/attribute.

<sp-field-group vertical>
  <sp-switch disabled>Disabled</sp-switch>
  <sp-switch disabled checked>Disabled and checked</sp-switch>
</sp-field-group>

### Behaviors

#Section titled Behaviors

#### Handling events

#Section titled Handling events

Event handlers for clicks and other user actions can be registered on an `<sp-switch>` similar to a standard `<input type="checkbox">` element.

<sp-switch id="switch-example" onclick="spAlert(this, '<sp-switch> clicked!')">
  Web component
</sp-switch>

### Accessibility

#Section titled Accessibility

Switch are rendered in HTML using the `<input type="checkbox">` element with the appropriate accessibility role, `switch`. When the Switch is `checked`, the appropriate ARIA state attribute will automatically be applied.

#### Include a label

#Section titled Include a label

A switch is required to have either a visible text label nested inside `<sp-switch>` itself.

<sp-switch>Email notifications</sp-switch>
Standalone switches should be used in situations where the context is clear without an associated text label. For example, a switch located at the top of a panel next to the panel's title makes it clear that the switch will enable/disable the panel options.

In those cases, you can use CSS to visually hide the text label.

<div id="settings">
  <sp-field-label for="notifications-settings">Notifications</sp-field-label>
  <sp-switch id="notify">
    <span class="visually-hidden">Notifications</span>
  </sp-switch>
  <sp-field-group id="notifications-settings" vertical>
    <sp-switch disabled>Email</sp-switch>
    <sp-switch disabled>Telephone</sp-switch>
    <sp-switch disabled>Text</sp-switch>
  </sp-field-group>
</div>

<style> .visually-hidden { clip-path: inset(50%); height: 1px; overflow: hidden; position: absolute; white-space: nowrap; width: 1px; } #settings { display: grid; grid-gap: 10px; grid-template-columns: calc(100% - 50px) 50px; } #notifications-settings { grid-column: 1 / 3; grid-row: 2; }</style>
Changelog
---------

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/checkbox@1.11.2

1.11.1
------

#Section titled 1.11.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/checkbox@1.11.1

1.11.0
------

#Section titled 1.11.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/checkbox@1.11.0

1.10.0
------

#Section titled 1.10.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/checkbox@1.10.0

1.9.1
-----

#Section titled 1.9.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.9.1
    *   @spectrum-web-components/base@1.9.1

1.9.0
-----

#Section titled 1.9.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.9.0
    *   @spectrum-web-components/base@1.9.0

1.8.0
-----

#Section titled 1.8.0

### Patch Changes

#Section titled Patch Changes

*   #5524`dcd2cd3` Thanks @marissahuysentruyt! - ### Fix down state colors for switch

Because the `postcss-hover-media-feature` plugin converts hover styles into a media query for devices that support hover, the hover styles were overriding any active/down state styles. We needed to target the active/down states of the switch with additional active state selectors, in order to ensure that the active state takes precedence over the hover state, maintaining the correct visual behavior of the switch component across different interaction states.

This fix should address hover + active state discrepancies in S1 and S2 foundations.

*   Updated dependencies []:

    *   @spectrum-web-components/checkbox@1.8.0
    *   @spectrum-web-components/base@1.8.0

1.7.0
-----

#Section titled 1.7.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.7.0
    *   @spectrum-web-components/base@1.7.0

1.6.0
-----

#Section titled 1.6.0

### Patch Changes

#Section titled Patch Changes

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/checkbox@1.6.0
    *   @spectrum-web-components/base@1.6.0

1.5.0
-----

#Section titled 1.5.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`a4de4c7`]: 
    *   @spectrum-web-components/checkbox@1.5.0
    *   @spectrum-web-components/base@1.5.0

1.4.0
-----

#Section titled 1.4.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/checkbox@1.4.0
    *   @spectrum-web-components/base@1.4.0

1.3.0
-----

#Section titled 1.3.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`468314f`]: 
    *   @spectrum-web-components/checkbox@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

1.2.0 (2025-02-27)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 1.1.1 (2025-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

1.1.0 (2025-01-29)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

### 1.0.3 (2024-12-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 1.0.1 (2024-11-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

1.0.0 (2024-10-31)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.49.0 (2024-10-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.48.0 (2024-09-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.47.1 (2024-08-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.42.4 (2024-05-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.42.0 (2024-03-19)
-------------------

#Section titled 

### Features

#Section titled Features

*   **asset:** use core tokens (99e76f4)

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.41.0 (2024-02-13)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.40.1 (2023-12-05)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   **checkbox:** refactor architecture for more rendering perf and DOM element count (7c2277f)

0.40.0 (2023-11-16)
-------------------

#Section titled 

### Features

#Section titled Features

*   **textfield:** added name attribute to textfield (#3752) (593005a)

### 0.39.4 (2023-11-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.39.2 (2023-10-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.39.1 (2023-10-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.39.0 (2023-09-25)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.37.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.35.0 (2023-07-31)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.34.0 (2023-07-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.32.0 (2023-06-01)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.31.0 (2023-05-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Bug Fixes

#Section titled Bug Fixes

*   add support for "readonly" attribute (4bce3b7)
*   correct @element jsDoc listing across library (c97a632)
*   ensure [disabled] styling (4c067eb)
*   ensure aria attributes based on state (6ee43de)
*   focusable style (48ea3e7)
*   implement "emphasized" styles (750bbe7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   move hover/focus hoisting into conditioning (15ac2f7)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **switch:** process CSS correction (292fff1)
*   **switch:** track aria-checked (1980046)
*   update configuration for Spectrum CSS processing for specificity (5c2e21e)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   workaround bug in Edge with switches (7014a2c)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** add action-group pattern (d2de766)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **switch:** update spectrum css input (1d2ce17)
*   **switch:** use core tokens (8011ead)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

### Reverts

#Section titled Reverts

*   Revert "chore: release new versions" (a6d655d)

### 0.11.13 (2023-04-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.12 (2023-04-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.11 (2023-03-22)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   move hover/focus hoisting into conditioning (15ac2f7)

### 0.11.10 (2023-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.9 (2023-02-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.8 (2023-02-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.7 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.6 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.5 (2022-12-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.4 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.3 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.2 (2022-10-28)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.11.1 (2022-10-17)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.11.0 (2022-10-10)
-------------------

#Section titled 

### Features

#Section titled Features

*   **switch:** use core tokens (8011ead)

0.10.0 (2022-08-09)
-------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

### 0.9.14 (2022-08-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.13 (2022-07-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.12 (2022-06-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.11 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.10 (2022-05-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.9 (2022-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.8 (2022-04-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.7 (2022-03-30)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.6 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.5 (2022-03-04)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.4 (2022-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.3 (2022-01-26)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.2 (2022-01-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.9.1 (2021-12-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.9.0 (2021-11-08)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.8.1 (2021-11-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.8.0 (2021-11-02)
------------------

#Section titled 

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)

### 0.7.16 (2021-10-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.15 (2021-09-20)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.14 (2021-09-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.13 (2021-08-24)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   correct @element jsDoc listing across library (c97a632)

### 0.7.12 (2021-08-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.11 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.10 (2021-07-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.9 (2021-06-16)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.8 (2021-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.7 (2021-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.6 (2021-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.5 (2021-04-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.4 (2021-03-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.3 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.7.2 (2021-03-22)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add support for "readonly" attribute (4bce3b7)

### 0.7.1 (2021-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.7.0 (2021-03-04)
------------------

#Section titled 

### Features

#Section titled Features

*   use latest exports specification (a7ecf4b)

### 0.6.3 (2021-02-11)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update to latest spectrum-css packages (a5ca19f)

### 0.6.2 (2021-02-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.6.1 (2021-01-28)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.6.0 (2021-01-21)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   ensure [disabled] styling (4c067eb)
*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update configuration for Spectrum CSS processing for specificity (5c2e21e)
*   update latest Spectrum CSS beta releases (d8d3acc)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   **switch:** update spectrum css input (1d2ce17)

0.5.0 (2021-01-13)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)

### Features

#Section titled Features

*   **action-button:** add action button pattern (03ac00a)
*   **switch:** update spectrum css input (1d2ce17)

### 0.4.4 (2020-10-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.4.3 (2020-10-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include default export in the "exports" fields (f32407d)

### 0.4.2 (2020-09-25)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update side effect listings (8160d3a)

### 0.4.1 (2020-09-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.4.0 (2020-08-31)
------------------

#Section titled 

### Features

#Section titled Features

*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   **action-group:** add action-group pattern (d2de766)

### 0.3.4 (2020-08-19)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.3.3 (2020-07-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.3.2 (2020-07-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.3.1 (2020-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

0.3.0 (2020-07-17)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **switch:** track aria-checked (1980046)

### Features

#Section titled Features

*   leverage "exports" field in package.json (321abd7)

### 0.2.16 (2020-06-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.15 (2020-05-08)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **switch:** process CSS correction (292fff1)
*   ensure aria attributes based on state (6ee43de)

### 0.2.14 (2020-04-21)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   workaround bug in Edge with switches (7014a2c)

### 0.2.13 (2020-04-16)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)

### 0.2.12 (2020-04-10)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.11 (2020-04-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.10 (2020-03-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.9 (2020-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.8 (2020-02-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.7 (2020-01-30)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.6 (2020-01-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.5 (2019-12-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.4 (2019-12-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.2.3 (2019-12-03)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   focusable style (48ea3e7)

### 0.2.2 (2019-12-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

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

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

### 0.1.5 (2019-11-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/switch

### 0.1.4 (2019-10-14)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

0.1.3 (2019-10-03)
------------------

#Section titled 0.1.3 (2019-10-03)

**Note:** Version bump only for package @spectrum-web-components/switch

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `checked``checked``boolean``false``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `emphasized``emphasized``boolean``false``name``name``string | undefined``readonly``readonly``boolean``false``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property 

### Slots

#Section titled Slots

 Name  Description `default slot` text label of the Switch 

### Events

#Section titled Events

 Name  Type  Description `change``Event``Announces a change in the `checked` property of a Switch`

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/switch/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/switch/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
