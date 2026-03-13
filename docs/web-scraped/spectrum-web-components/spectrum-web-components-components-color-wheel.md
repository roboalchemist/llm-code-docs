# Source: https://opensource.adobe.com/spectrum-web-components/components/color-wheel/

Title: Color Wheel: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/color-wheel/

Markdown Content:
An `<sp-color-wheel>` allows users to visually select the hue of a color on a circular track. It's commonly used together with other color components to create comprehensive color selection interfaces.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/color-wheel?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/color-wheel?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/color-wheel
Import the side effectful registration of `<sp-color-wheel>` via:

import '@spectrum-web-components/color-wheel/sp-color-wheel.js';
When looking to leverage the `ColorWheel` base class as a type and/or for extension purposes, do so via:

import { ColorWheel } from '@spectrum-web-components/color-wheel';
The color wheel consists of several key parts:

*   A circular track displaying the full spectrum of hues
*   A draggable handle that indicates the current hue selection
*   Accessible labels for screen readers
*   Optional custom gradient slot for advanced styling

<sp-color-wheel></sp-color-wheel>
**⚠️ Deprecated Feature**

The custom gradient functionality has been deprecated and is no longer supported. While the `gradient` slot may still be present in the component's code, it is broken and will not work as intended.

If you previously relied on custom gradients for the color wheel, you should:

*   Use the default color wheel appearance
*   Consider alternative approaches for custom styling
*   Remove any existing custom gradient implementations

**Note**: Even if you find the `gradient` slot in the component's source code, this feature is non-functional and should not be used in new implementations.

The color wheel supports several properties for configuration:

The `value` property controls the hue angle of the color wheel (0-360 degrees). This represents the position of the handle on the circular track and determines the hue component of the displayed color.

<sp-color-wheel value="180"></sp-color-wheel>
The color wheel supports a wide variety of color formats for setting and getting color values:

<div style="display: flex; gap: 16px;">
  <sp-color-wheel color="#7277b5"></sp-color-wheel>
  <sp-color-wheel color="hsl(96, 84.00%, 49.00%)"></sp-color-wheel>
  <sp-color-wheel color="red"></sp-color-wheel>
</div>Format Example Values Description Hex3`#f00`, `#0a5`3-digit hexadecimal Hex4`#f00f`, `#0a58`3-digit hexadecimal + alpha Hex6`#ff0000`, `#00aa55`6-digit hexadecimal Hex8`#ff0000ff`, `#00aa5580`6-digit hexadecimal + alpha RGB`rgb(255, 0, 0)`, `rgb(0, 170, 85)`Red, Green, Blue values (0-255)RGBA`rgba(255, 0, 0, 1)`, `rgba(0, 170, 85, 0.5)`RGB + Alpha channel (0-1)HSL`hsl(0, 100%, 50%)`, `hsl(150, 100%, 33%)`Hue (0-360°), Saturation, Lightness HSLA`hsla(0, 100%, 50%, 1)`, `hsla(150, 100%, 33%, 0.5)`HSL + Alpha channel (0-1)HSV`hsv(0, 100%, 100%)`, `hsv(150, 100%, 67%)`Hue (0-360°), Saturation, Value HSVA`hsva(0, 100%, 100%, 1)`, `hsva(150, 100%, 67%, 0.5)`HSV + Alpha channel (0-1)Named Colors`red`, `rebeccapurple`, `darkseagreen`CSS color keywords (full list)
The `step` attribute controls the increment of hue adjustment when using keyboard navigation. It defines how many degrees the hue changes with each arrow key press:

<div style="display: flex; gap: 16px;">
  <sp-color-wheel step="1" label="Fine Control (1° per key)"></sp-color-wheel>
  <sp-color-wheel step="10" label="Medium Control (10° per key)" ></sp-color-wheel>
  <sp-color-wheel step="45" label="Coarse Control (45° per key)" ></sp-color-wheel>
</div>
The step size affects keyboard navigation:

*   Regular arrow keys move by the step value
*   Shift + arrow keys move by 10× the step value
*   Choose your step size based on your use case: 
    *   **step="1"**: Precise color selection, best for professional design tools
    *   **step="10"**: Balanced control, good for general use
    *   **step="45"**: Quick selection between major hues, ideal for simple color pickers

Provide a custom aria-label for accessibility:

<sp-color-wheel label="Select color hue"></sp-color-wheel>
The color wheel supports both left-to-right and right-to-left layouts:

<sp-color-wheel dir="rtl"></sp-color-wheel>
The `tabIndex` property controls the tab order of the color wheel within the page. This follows the standard HTML `tabindex` attribute behavior:

<div style="display: flex; gap: 16px;">
  <div style="text-align: center;">
    <div style="font-weight: bold; margin-bottom: 8px;">Default Tab Order</div>
    <sp-color-wheel></sp-color-wheel>
  </div>
  <div style="text-align: center;">
    <div style="font-weight: bold; margin-bottom: 8px;">Skip in Tab Order</div>
    <sp-color-wheel tabindex="-1"></sp-color-wheel>
  </div>
  <div style="text-align: center;">
    <div style="font-weight: bold; margin-bottom: 8px;">Custom Tab Order</div>
    <sp-color-wheel tabindex="5"></sp-color-wheel>
  </div>
</div>
**Note**: See the general documentation about the HTML tabindex property for detailed information about tab order behavior.

An `<sp-color-wheel>`'s size can be customized appropriately for its context. By default, the size is 192 px.

You can set custom dimensions using inline styles. For a perfect circle, ensure width and height are the same:

<sp-color-wheel style="width: 300px; height: 300px;"></sp-color-wheel>
The component exposes CSS custom properties for consistent theming. Both `--mod-colorwheel-width` and `--mod-colorwheel-height` should be set to the same value to maintain a perfect circle:

<sp-color-wheel style="--mod-colorwheel-width: 250px; --mod-colorwheel-height: 250px;"></sp-color-wheel>
**Note**: The CSS internally reuses the width value for both dimensions, but both mod tokens are exposed for flexibility in custom implementations.

A color wheel in a disabled state shows that an input exists, but is not available in that circumstance. This can be used to maintain layout continuity and communicate that the wheel may become available later.

<sp-color-wheel disabled></sp-color-wheel>
The color wheel manages its focused state automatically, providing visual feedback during keyboard navigation:

<sp-color-wheel focused></sp-color-wheel>
When using the color elements, use `el.color` to access the `color` property, which should manage itself in the color format supplied. If you supply a color in `rgb()` format, `el.color` should return the color in `rgb()` format, as well.

**Please note for the following formats: HSV, HSVA, HSL, HSLA** When using the HSL or HSV formats, and a color's value (in HSV) is set to 0, or its luminosity (in HSL) is set to 0 or 1, the hue and saturation values may not be preserved by the element's `color` property. This is detailed in the colorjs documentation. Separately, the element's `value` property is directly managed by the hue as represented in the interface.

The color wheel supports both mouse and touch interactions:

*   **Click**: Jump to a specific hue on the wheel
*   **Drag**: Continuously adjust hue while dragging around the wheel
*   **Touch**: Full touch support for mobile devices

The color wheel automatically manages focus for keyboard accessibility, ensuring proper focus indication and keyboard operability.

The `<sp-color-wheel>` is rendered with appropriate ARIA attributes to ensure accessibility for screen readers and keyboard navigation.

The color wheel supports comprehensive keyboard interaction:

Key Action Arrow Left/Arrow Right Decrease/Increase hue by step value (respects RTL)Arrow Up/Arrow Down Increase/Decrease hue by step value Shift + Arrow Keys Adjust hue by larger increments (10× step)
The component provides comprehensive ARIA support:

*   **Role**: Uses native `input[type="range"]` with implicit "slider" role
*   **Label**: Customizable via the `label` property (defaults to "hue")
*   **Value Text**: Announces the current hue value in degrees with proper internationalization
*   **Orientation**: Implicitly circular, supporting both LTR and RTL layouts

The component provides meaningful announcements for assistive technologies:

*   Current hue value announced in degrees (e.g., "180 degrees")
*   Internationalized number formatting based on user's locale
*   Clear indication of the control's purpose through proper labeling

The color wheel is fully accessible on mobile devices with:

*   Touch-friendly interaction areas
*   Proper focus management for mobile screen readers

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/color-handle@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/color-handle@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/color-handle@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/color-handle@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/color-handle@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   #5641`c3d5558` Thanks @blunteshwar! - Fixed `<sp-color-wheel>` step attribute functionality for keyboard navigation. The step attribute now properly controls the increment size when using arrow keys to navigate the color wheel.

*   Updated dependencies []:

    *   @spectrum-web-components/color-handle@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`165a904`]:

    *   @spectrum-web-components/color-handle@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/color-handle@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   **color-wheel:** reorient reactively to "dir" changes (#3319) (6a9dcec)

*   **color-area,color-slider:** color-area labeling, RTL support, vertical slider orientation(#3315) (ca2acda), closes #3313
*   **color-slider,color-wheel:** fix focused state #3278 (96b83f7)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   address westbrooks comments (634af60)
*   **color-wheel:** use correct focus events in test (f6f35ec)
*   ensure color wheel in not opinionated about saturation and lightness (8e0fd9c)
*   ensure streamingListener ends even if pointercancel not fired (74105f2)
*   expand support for maintaining hue and saturation across customization (fe18944)
*   include touch-action rule for draggable content (3f507e6)
*   key interaction handling no longer prevents "tab" presses (b542ce8)
*   leverage Color Controller to unify color interface across packages (fb71690)
*   manage "focused" across more contexts (9273c15)
*   normalize focus passing during and after pointer events (357931b)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   remove right click value setting (a44968d)
*   update colour slider (9acda67)
*   use hue normalized color in handle and allow focus (f9e1fa2)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **color-wheel:** add color-wheel pattern (8b2a56d)
*   **color-wheel:** use core tokens (57159a2)
*   debug colour elements for a11y (7008f7c)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)

*   ensure streamingListener ends even if pointercancel not fired (74105f2)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   **color-wheel:** use core tokens (57159a2)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   leverage Color Controller to unify color interface across packages (fb71690)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   update lit-* dependencies, wip (377f3c8)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

*   **color-wheel:** use correct focus events in test (f6f35ec)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   manage "focused" across more contexts (9273c15)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   key interaction handling no longer prevents "tab" presses (b542ce8)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   expand support for maintaining hue and saturation across customization (fe18944)
*   normalize focus passing during and after pointer events (357931b)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)

*   include touch-action rule for draggable content (3f507e6)

*   ensure color wheel in not opinionated about saturation and lightness (8e0fd9c)
*   use hue normalized color in handle and allow focus (f9e1fa2)

**Note:** Version bump only for package @spectrum-web-components/color-wheel

*   remove right click value setting (a44968d)

*   address westbrooks comments (634af60)
*   update colour slider (9acda67)

*   debug colour elements for a11y (7008f7c)
*   **color-wheel:** add color-wheel pattern (8b2a56d)

Property  Attribute  Type  Default  Description `color``color``ColorTypes``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `focused``focused``boolean``false``label``label``string``'hue'``step``step``number``1``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `value``value``number`

Name  Description `gradient` a custom gradient visually outlining the available color values

Name  Type  Description `change``Event``An alteration to the value of the Color Wheel has been committed by the user.``input``Event``The value of the Color Wheel has changed.`
