# Source: https://opensource.adobe.com/spectrum-web-components/components/color-handle/

Title: Color Handle: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/color-handle/

Markdown Content:
The `<sp-color-handle>` is used to select a color on an `<sp-color-area>`, `<sp-color-slider>`, or `<sp-color-wheel>`. It provides a draggable control point for precise color selection within color components.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/color-handle?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/color-handle?style=for-the-badge)

**Note**: `<sp-color-handle>` is a primitive component designed to be used within other color selection components. It's not typically used directly in applications, but rather as part of higher-level color components like `<sp-color-area>`, `<sp-color-slider>`, or `<sp-color-wheel>`.

yarn add @spectrum-web-components/color-handle
Import the side effectful registration of `<sp-color-handle>` via:

import '@spectrum-web-components/color-handle/sp-color-handle.js';
When looking to leverage the `ColorHandle` base class as a type and/or for extension purposes, do so via:

import { ColorHandle } from '@spectrum-web-components/color-handle';
The color handle consists of several key parts:

*   A visual handle element that indicates the current position
*   Touch-responsive interaction areas
*   Color display showing the current selected color
*   Opacity checkerboard pattern for transparent colors
*   An optional `sp-color-loupe` that appears above the handle when the properties `open = true` and `disabled = false`

<sp-color-handle></sp-color-handle>
The `color` property sets the visual color displayed within the handle. This accepts any valid CSS color format. The default color is `rgba(255, 0, 0, 0.5)` (semi-transparent red).

For a complete list of supported color formats, see the ColorController documentation.

**Transparency Support**: When using transparent colors, the handle displays an opacity checkerboard pattern background to clearly show the transparency level.

<div style="display: flex; gap: 16px; align-items: center; margin: 16px 0;">
  
  <div style="position: relative; height: 20px; margin: 20px;">
    <sp-color-handle color="#ff0000"></sp-color-handle>
  </div>

  
  <div style="position: relative; height: 20px; margin: 20px;">
    <sp-color-handle color="rgb(255, 0, 0)"></sp-color-handle>
  </div>

  
  <div style="position: relative; height: 20px; margin: 20px;">
    <sp-color-handle color="rgba(255, 0, 0, 0.5)"></sp-color-handle>
  </div>

  
  <div style="position: relative; height: 20px; margin: 20px;">
    <sp-color-handle color="hsl(0, 100%, 50%)"></sp-color-handle>
  </div>

  
  <div style="position: relative; height: 20px; margin: 20px;">
    <sp-color-handle color="red"></sp-color-handle>
  </div>
</div>
The default state of the color handle, ready for interaction:

<sp-color-handle></sp-color-handle>
A disabled color handle shows that the control exists but is not available for interaction. This maintains layout continuity and communicates that the handle may become available later:

<sp-color-handle disabled></sp-color-handle>
When the `open` property is set, the `<sp-color-loupe>` component appears above the handle to show the selected color that would otherwise be covered by a mouse, stylus, or finger on the down/touch state. The loupe automatically appears for touch input (`pointerType === 'touch'`).

<div style="height: 72px"></div>
<sp-color-handle open></sp-color-handle>
**Automatic Behavior**: The loupe automatically opens when touched and closes when the touch interaction ends. For mouse and stylus input, the loupe remains hidden by default unless explicitly set to `open="true"`.

The color handle can receive keyboard focus when used within interactive color components. The focused state is managed automatically by the parent component and is indicated visually:

<sp-color-handle focused></sp-color-handle>
The color handle automatically manages pointer events to provide the optimal user experience:

*   **Touch Input**: When touched (`pointerType === 'touch'`), the color loupe automatically appears to prevent the finger from obscuring the selected color
*   **Mouse/Stylus Input**: The loupe remains hidden by default for precision pointing devices
*   **Pointer Capture**: The handle captures pointer events during interaction to ensure smooth dragging even when the pointer moves outside the handle area
*   **Event Handling**: The component listens for `pointerdown`, `pointerup`, and `pointercancel` events to manage the interaction lifecycle

The handle displays the current color with proper support for transparency:

*   Transparent colors are shown with an opacity checkerboard pattern background
*   The color updates in real-time as the user interacts with the parent color component
*   Supports all standard CSS color formats

For a complete list of supported color formats, see the ColorController documentation.

The `<sp-color-handle>` is designed to work as part of accessible color selection components:

While the color handle itself is not directly keyboard accessible, it works in conjunction with its parent components (`<sp-color-area>`, `<sp-color-slider>`, `<sp-color-wheel>`) which provide comprehensive keyboard navigation. Example: Keyboard accessibility with `sp-color-area` as parent component

<sp-color-area></sp-color-area>
The color handle is rendered as a visual indicator and does not directly interface with screen readers. Accessibility is provided through the parent color component's ARIA implementation.

*   **Color Loupe**: Automatically appears for touch input to ensure the selected color remains visible
*   **Large Touch Target**: The handle provides an appropriately sized touch target for mobile interaction
*   **Pointer Capture**: Ensures reliable dragging behavior across different touch devices

Focus is managed by the parent color component, with the handle reflecting the focused state visually when its parent component has keyboard focus.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/color-loupe@1.11.2
    *   @spectrum-web-components/opacity-checkerboard@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/color-loupe@1.11.1
    *   @spectrum-web-components/opacity-checkerboard@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/color-loupe@1.11.0
    *   @spectrum-web-components/opacity-checkerboard@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/color-loupe@1.10.0
    *   @spectrum-web-components/opacity-checkerboard@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-loupe@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/opacity-checkerboard@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/color-loupe@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/opacity-checkerboard@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-loupe@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/opacity-checkerboard@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-loupe@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/opacity-checkerboard@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-loupe@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/opacity-checkerboard@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`165a904`]:

    *   @spectrum-web-components/color-loupe@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/opacity-checkerboard@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-loupe@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/opacity-checkerboard@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-loupe@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/opacity-checkerboard@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   update deps graph, update link docs (#3709) (2deb284)

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   **color-handle,color-loupe,swatch,thumbnail:** use the Opacity Checkerboard package (47e1fc4)

*   **color-slider:** migrate to core tokens (#3507) (96d0d40)

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   **color-handle,color-loupe:** accept updated CSS token names (8c28f6d)

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   address westbrooks comments (634af60)
*   expand support for maintaining hue and saturation across customization (fe18944)
*   include touch-action rule for draggable content (3f507e6)
*   leverage Color Controller to unify color interface across packages (fb71690)
*   manage "focused" across more contexts (9273c15)
*   prevent focus outline (af2b077)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **color-handle:** add color-handle pattern (e3856d8)
*   **color-handle:** use core tokens (e0c1468)
*   **color-loupe:** use core tokens (149165c)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)

*   **color-handle:** use core tokens (e0c1468)
*   **color-loupe:** use core tokens (149165c)

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   leverage Color Controller to unify color interface across packages (fb71690)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   manage "focused" across more contexts (9273c15)
*   prevent focus outline (af2b077)

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   expand support for maintaining hue and saturation across customization (fe18944)

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   include touch-action rule for draggable content (3f507e6)

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

**Note:** Version bump only for package @spectrum-web-components/color-handle

*   address westbrooks comments (634af60)

*   **color-handle:** add color-handle pattern (e3856d8)

Property  Attribute  Type  Default  Description `color``color``string``'rgba(255, 0, 0, 0.5)'``disabled``disabled``boolean``false``focused``focused``boolean``false``open``open``boolean``false`
