# Source: https://opensource.adobe.com/spectrum-web-components/components/color-slider/

Title: Color Slider: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/color-slider/

Markdown Content:
An `<sp-color-slider>` lets users visually change an individual channel of a color. The background of the `<sp-color-slider>` is a visual representation of the range of values a user can select from. This can represent color properties such as hues, color channel values (such as RGB or CMYK levels), or opacity. Currently, the slider only supports leveraging the `hue` property.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/color-slider?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/color-slider?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/color-slider
Import the side effectful registration of `<sp-color-slider>` via:

import '@spectrum-web-components/color-slider/sp-color-slider.js';
When looking to leverage the `ColorSlider` base class as a type and/or for extension purposes, do so via:

import { ColorSlider } from '@spectrum-web-components/color-slider';
The color slider consists of several key parts:

*   A gradient track showing the range of color values
*   A draggable handle that indicates the current color position
*   An accessible label for screen readers

<sp-color-slider></sp-color-slider>
By default, the color slider is displayed horizontally. You can change the orientation to vertical using the `vertical` attribute:

<sp-color-slider vertical></sp-color-slider>
The standard color slider allows users to select hue values from 0 to 360 degrees:

<sp-color-slider></sp-color-slider>
A color slider in a disabled state shows that an input exists, but is not available in that circumstance. This can be used to maintain layout continuity and communicate that the slider may become available later.

<sp-color-slider disabled></sp-color-slider>
When using the color elements, use `el.color` to access the `color` property, which should manage itself in the colour format supplied. If you supply a color in `rgb()` format, `el.color` should return the color in `rgb()` format, as well.

The current color formats supported are as follows:

*   Hex3, Hex4, Hex6, Hex8
*   HSV, HSVA
*   HSL, HSLA
*   RGB, RGBA
*   Strings (eg "red", "blue")

For a complete list of supported color formats, see the ColorController documentation.

**Please note for the following formats: HSV, HSVA, HSL, HSLA**

When using the HSL or HSV formats, and a color's value (in HSV) is set to 0, or its luminosity (in HSL) is set to 0 or 1, the hue and saturation values may not be preserved by the element's `color` property. This is detailed in the colorjs documentation. Seperately, the element's `value` property is directly managed by the hue as represented in the interface.

The `<sp-color-slider>` is rendered with appropriate ARIA attributes to ensure accessibility:

*   Uses native `input[type="range"]` element with implicit "slider" role
*   Provides value text announcements for screen readers
*   Supports full keyboard navigation

The color slider includes an accessible label that describes what the slider controls. By default, the label is set to "hue", but you can customize it using the `label` attribute:

<sp-color-slider></sp-color-slider>

<sp-color-slider label="Color hue"></sp-color-slider>
<sp-color-slider label="Saturation level"></sp-color-slider>
The label serves several important accessibility purposes:

*   **Screen Reader Announcements**: Screen readers announce the label when the slider receives focus, helping users understand what they're adjusting
*   **ARIA Labeling**: The label is used as the `aria-label` attribute on the internal range input
*   **Context for Value Changes**: When the slider value changes, screen readers announce both the current value and the label for context

For example, when a user focuses on a color slider with `label="Color hue"`, screen readers will announce something like "Color hue slider, 180 degrees" to provide clear context about what the control does and its current value.

Key Action Arrow Left/Arrow Down Decreases the hue value Arrow Right/Arrow Up Increases the hue value Shift + Arrow Left/Shift + Arrow Down Decreases the hue value by a larger step (10x)Shift + Arrow Right/Shift + Arrow Up Increases the hue value by a larger step (10x)Page Down Decreases the hue value by a larger step(10% of total value)Page Up Increases the hue value by a larger step(10% of total value)Home Sets the hue to minimum value (0)End Sets the hue to maximum value (360)

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/color-handle@1.11.2
    *   @spectrum-web-components/opacity-checkerboard@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/color-handle@1.11.1
    *   @spectrum-web-components/opacity-checkerboard@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/color-handle@1.11.0
    *   @spectrum-web-components/opacity-checkerboard@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/color-handle@1.10.0
    *   @spectrum-web-components/opacity-checkerboard@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/opacity-checkerboard@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/color-handle@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/opacity-checkerboard@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/opacity-checkerboard@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/opacity-checkerboard@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/opacity-checkerboard@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`165a904`]:

    *   @spectrum-web-components/color-handle@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/opacity-checkerboard@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/opacity-checkerboard@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/color-handle@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/opacity-checkerboard@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   update deps graph, update link docs (#3709) (2deb284)

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   **color-slider:** migrate to core tokens (#3507) (96d0d40)

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   **color-area,color-slider:** color-area labeling, RTL support, vertical slider orientation(#3315) (ca2acda), closes #3313
*   **color-slider,color-wheel:** fix focused state #3278 (96b83f7)
*   **color-slider:** announce new value on change after keydown (#3304) (d70d0ae), closes #3303

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   **color-slider:** use inset-block-_ and inset-inline-_ and fix RTL orientation and behavior #3301 (52aa328)

*   **color-slider:** vertical variant orientation is upside down #3291 (67c7e0a)

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   address westbrooks comments (634af60)
*   **color-slider:** use correct focus events in test (b974c12)
*   ensure color wheel in not opinionated about saturation and lightness (8e0fd9c)
*   ensure streamingListener ends even if pointercancel not fired (74105f2)
*   expand support for maintaining hue and saturation across customization (fe18944)
*   include touch-action rule for draggable content (53221da)
*   include touch-action rule for draggable content (3f507e6)
*   key interaction handling no longer prevents "tab" presses (b542ce8)
*   leverage Color Controller to unify color interface across packages (fb71690)
*   manage "focused" across more contexts (9273c15)
*   normalize focus passing during and after pointer events (357931b)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   remove right click value setting (a44968d)
*   simplify touch-action application (d23f735)
*   update colour slider (9acda67)
*   use hue normalized color in handle and allow focus (f9e1fa2)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **color-handle:** use core tokens (e0c1468)
*   **color-slider:** add color-slider pattern (625f6fe)
*   debug colour elements for a11y (7008f7c)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)

*   ensure streamingListener ends even if pointercancel not fired (74105f2)

*   **color-handle:** use core tokens (e0c1468)

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   leverage Color Controller to unify color interface across packages (fb71690)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   simplify touch-action application (d23f735)

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   update lit-* dependencies, wip (377f3c8)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

*   **color-slider:** use correct focus events in test (b974c12)

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   manage "focused" across more contexts (9273c15)

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   key interaction handling no longer prevents "tab" presses (b542ce8)

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   expand support for maintaining hue and saturation across customization (fe18944)
*   normalize focus passing during and after pointer events (357931b)

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)

*   include touch-action rule for draggable content (53221da)
*   include touch-action rule for draggable content (3f507e6)

*   ensure color wheel in not opinionated about saturation and lightness (8e0fd9c)
*   use hue normalized color in handle and allow focus (f9e1fa2)

**Note:** Version bump only for package @spectrum-web-components/color-slider

*   remove right click value setting (a44968d)

*   address westbrooks comments (634af60)
*   update colour slider (9acda67)

*   debug colour elements for a11y (7008f7c)
*   **color-slider:** add color-slider pattern (625f6fe)

Property  Attribute  Type  Default  Description `color``color``ColorTypes``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `focused``focused``boolean``false``label``label``string``'hue'``step``step``number``1``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `value``value``number``vertical``vertical``boolean``false`

Name  Description `gradient` a custom gradient visually outlining the available color values

Name  Type  Description `change``Event``An alteration to the value of the Color Slider has been committed by the user.``input``Event``The value of the Color Slider has changed.`
