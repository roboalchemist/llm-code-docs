# Source: https://opensource.adobe.com/spectrum-web-components/components/swatch/

Title: Swatch: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/swatch/

Markdown Content:
An `<sp-swatch>` shows a small sample of a fill — such as a color, gradient, texture, or material — that is intended to be applied to an object.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/swatch?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/swatch?style=for-the-badge)

yarn add @spectrum-web-components/swatch
Import the side effectful registration of `<sp-swatch>` via:

import '@spectrum-web-components/swatch/sp-swatch.js';
When looking to leverage the `Swatch` base class as a type and/or for extension purposes, do so via:

import { Swatch } from '@spectrum-web-components/swatch';Extra Small<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)" size="xs"></sp-swatch>
  <sp-swatch rounding="none" color="rgb(255 0 0 / 0.7)" size="xs"></sp-swatch>
  <sp-swatch rounding="full" color="rgb(255 0 0 / 0.7)" size="xs"></sp-swatch>
  <sp-swatch border="light" color="rgb(255 0 0 / 0.7)" size="xs"></sp-swatch>
  <sp-swatch border="none" color="rgb(255 0 0 / 0.7)" size="xs"></sp-swatch>
  <sp-swatch nothing size="xs"></sp-swatch>
  <sp-swatch shape="rectangle" color="rgb(255 0 0 / 0.7)" size="xs"></sp-swatch>
  <sp-swatch shape="rectangle" disabled color="rgb(255 0 0 / 0.7)" size="xs" ></sp-swatch>
  <sp-swatch rounding="full" shape="rectangle" mixed-value size="xs" ></sp-swatch>
</sp-swatch-group>Small<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)" size="s"></sp-swatch>
  <sp-swatch rounding="none" color="rgb(255 0 0 / 0.7)" size="s"></sp-swatch>
  <sp-swatch rounding="full" color="rgb(255 0 0 / 0.7)" size="s"></sp-swatch>
  <sp-swatch border="light" color="rgb(255 0 0 / 0.7)" size="s"></sp-swatch>
  <sp-swatch border="none" color="rgb(255 0 0 / 0.7)" size="s"></sp-swatch>
  <sp-swatch nothing size="s"></sp-swatch>
  <sp-swatch shape="rectangle" color="rgb(255 0 0 / 0.7)" size="s"></sp-swatch>
  <sp-swatch shape="rectangle" disabled color="rgb(255 0 0 / 0.7)" size="s" ></sp-swatch>
  <sp-swatch rounding="full" shape="rectangle" mixed-value size="s"></sp-swatch>
</sp-swatch-group>Medium<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)" size="m"></sp-swatch>
  <sp-swatch rounding="none" color="rgb(255 0 0 / 0.7)" size="m"></sp-swatch>
  <sp-swatch rounding="full" color="rgb(255 0 0 / 0.7)" size="m"></sp-swatch>
  <sp-swatch border="light" color="rgb(255 0 0 / 0.7)" size="m"></sp-swatch>
  <sp-swatch border="none" color="rgb(255 0 0 / 0.7)" size="m"></sp-swatch>
  <sp-swatch nothing size="m"></sp-swatch>
  <sp-swatch shape="rectangle" color="rgb(255 0 0 / 0.7)" size="m"></sp-swatch>
  <sp-swatch shape="rectangle" disabled color="rgb(255 0 0 / 0.7)" size="m" ></sp-swatch>
  <sp-swatch rounding="full" shape="rectangle" mixed-value size="m"></sp-swatch>
</sp-swatch-group>Large<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)" size="l"></sp-swatch>
  <sp-swatch rounding="none" color="rgb(255 0 0 / 0.7)" size="l"></sp-swatch>
  <sp-swatch rounding="full" color="rgb(255 0 0 / 0.7)" size="l"></sp-swatch>
  <sp-swatch border="light" color="rgb(255 0 0 / 0.7)" size="l"></sp-swatch>
  <sp-swatch border="none" color="rgb(255 0 0 / 0.7)" size="l"></sp-swatch>
  <sp-swatch nothing size="l"></sp-swatch>
  <sp-swatch shape="rectangle" color="rgb(255 0 0 / 0.7)" size="l"></sp-swatch>
  <sp-swatch shape="rectangle" disabled color="rgb(255 0 0 / 0.7)" size="l" ></sp-swatch>
  <sp-swatch rounding="full" shape="rectangle" mixed-value size="l"></sp-swatch>
</sp-swatch-group>
An `<sp-swatch>` element can be modified by the following attributes/properties to customize its delivery as desired for your use case: `border`, `color`, `disabled`, `mixedValue` (accepted as the `mixed-value` attribute), `nothing`, `rounding`, and `shape`. Use these in concert with each other for a variety of final visual deliveries.

Border
The `border` attribute/property is not required and when applied accepts the values of `none` or `light`.

<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)"></sp-swatch>
  <sp-swatch color="rgb(255 0 0 / 0.7)" border="light"></sp-swatch>
  <sp-swatch color="rgb(255 0 0 / 0.7)" border="none"></sp-swatch>
</sp-swatch-group>Color
The `color` attribute/property determines the color value that the `<sp-swatch>` element will deliver.

<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)"></sp-swatch>
  <sp-swatch color="orange"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>Mixed Value
The `mixed-value` attribute and `mixedValue` property outline when an `<sp-swatch>` element represents more than one color.

<sp-swatch-group selects="multiple">
  <sp-swatch mixed-value></sp-swatch>
  <sp-swatch mixed-value rounding="full"></sp-swatch>
  <sp-swatch mixed-value shape="rectangle"></sp-swatch>
</sp-swatch-group>
Please note that the `aria-checked="mixed"` value only applies when the swatch is in a group with `selects="multiple"`

Nothing
The `nothing` attribute/property outlines that the `<sp-swatch>` represents no color or that it represents "transparent".

<sp-swatch-group selects="multiple">
  <sp-swatch nothing></sp-swatch>
  <sp-swatch nothing rounding="full"></sp-swatch>
  <sp-swatch nothing shape="rectangle"></sp-swatch>
</sp-swatch-group>Rounding
The `rounding` attribute/property is not required and when applied accepts the values of `none` or `full`.

<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)"></sp-swatch>
  <sp-swatch color="rgb(255 0 0 / 0.7)" rounding="none"></sp-swatch>
  <sp-swatch color="rgb(255 0 0 / 0.7)" rounding="full"></sp-swatch>
</sp-swatch-group>Shape
The `shape` attribute/property is not required and when applied accepts the values of `rectangle`.

<sp-swatch-group selects="multiple">
  <sp-swatch color="rgb(255 0 0 / 0.7)"></sp-swatch>
  <sp-swatch color="rgb(255 0 0 / 0.7)" shape="rectangle"></sp-swatch>
</sp-swatch-group>
The `disabled` attribute/property determines prevents interaction on the `<sp-swatch>` element.

<sp-swatch-group selects="multiple">
  <sp-swatch disabled color="rgb(255 0 0 / 0.7)"></sp-swatch>
  <sp-swatch disabled color="orange"></sp-swatch>
  <sp-swatch disabled color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>
When swatches are intended to be selectable, set the `selects` property on `<sp-swatch-group>` to enable proper ARIA semantics:

*   `selects="single"`: Swatches have `role="radio"` and announce as radio buttons
*   `selects="multiple"`: Swatches have `role="checkbox"` and announce as checkboxes with checked/unchecked states

Without the `selects` property, swatches default to `role="button"` and the swatch-group stops propagation of change events, so `selected` and `aria-pressed` states won't update when clicked. This prevents screen readers from announcing selection state changes.

<sp-swatch-group selects="multiple" aria-label="Select colors">
  <sp-swatch color="red" label="Red"></sp-swatch>
  <sp-swatch color="blue" label="Blue"></sp-swatch>
</sp-swatch-group>
*   Ensure swatches have sufficient color contrast for visibility.
*   Verify that swatches are appropriately labeled for screen readers.
*   Use the `selects` property when swatches represent a selection interface.

*   `Tab`: Move focus to the next focusable element
*   `Arrow keys`: Navigate between swatches in the group and move the focus indicator
*   `Enter` or `Space`: Select the focused swatch

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/opacity-checkerboard@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/opacity-checkerboard@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0
    *   @spectrum-web-components/opacity-checkerboard@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/opacity-checkerboard@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/opacity-checkerboard@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/opacity-checkerboard@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/opacity-checkerboard@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/opacity-checkerboard@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/opacity-checkerboard@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/opacity-checkerboard@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/opacity-checkerboard@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/opacity-checkerboard@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   **swatch:** sync aria-label with changes in label, color, and mixed state (#4519) (50aef31)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)
*   **swatch:** allow Swatch Group to manage selection through multiple slots (f333379)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   **alert-dialog:** add Alert Dialog package (#3501) (1062847)
*   **color-handle,color-loupe,swatch,thumbnail:** use the Opacity Checkerboard package (47e1fc4)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   **swatch:** clear previously selected children when updating `selected` (ce1bd36)
*   **swatch:** warn when mixed-value used with selects !== 'multiple' (#3460) (89c288e)

*   **swatch:** mixed-value state must be conveyed to screen readers using ARIA (#3330) (7711264)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   **shared:** allow "disabled" first to return to "tabindex=0" in "focusable" (160bc59)

*   include all dependencies (c80d244)
*   support non-flat "color" application (efc0159)
*   **swatch:** normalize repeat selection of same item in "selects=single" (ee0fb0c)

*   add swatch pattern (0cdc04b)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **swatch:** use core tokens (821aebe)

*   support non-flat "color" application (efc0159)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   **swatch:** normalize repeat selection of same item in "selects=single" (ee0fb0c)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   **swatch:** use core tokens (821aebe)

**Note:** Version bump only for package @spectrum-web-components/swatch

**Note:** Version bump only for package @spectrum-web-components/swatch

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/swatch

*   include all dependencies (c80d244)

**Note:** Version bump only for package @spectrum-web-components/swatch

*   add swatch pattern (0cdc04b)

Property  Attribute  Type  Default  Description `border``border``SwatchBorder``color``color``string``''``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `label``label``string``''``mixedValue``mixed-value``boolean``false``nothing``nothing``boolean``false``role``role``string``'button'``rounding``rounding``SwatchRounding``selected``selected``boolean``false``shape``shape``SwatchShape``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `value``value``string`

Name  Type  Description `change``Event`
