# Source: https://opensource.adobe.com/spectrum-web-components/components/color-area/

Title: Color Area: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/color-area/

Markdown Content:
An `<sp-color-area>` allows users to visually select two properties of a color simultaneously. It's commonly used together with a color slider or color wheel to create comprehensive color selection interfaces.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/color-area?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/color-area?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/color-area
Import the side effectful registration of `<sp-color-area>` via:

import '@spectrum-web-components/color-area/sp-color-area.js';
When looking to leverage the `ColorArea` base class as a type and/or for extension purposes, do so via:

import { ColorArea } from '@spectrum-web-components/color-area';
The color area consists of several key parts:

*   A two-dimensional color selection area with visual gradients
*   A draggable handle that indicates the current color position
*   Accessible labels for the X and Y axes
*   Optional custom gradient slot for advanced styling

<sp-color-area></sp-color-area>
You can provide a custom gradient to replace the default color area appearance using the `gradient` slot:

<sp-color-area>
  <div slot="gradient" class="textured-gradient"></div>
</sp-color-area>

<style> .textured-gradient { width: 100%; height: 100%; background: radial-gradient( circle at 20% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 90% ), radial-gradient( circle at 80% 20%, rgba(0, 0, 0, 0.1) 0%, transparent 50% ), linear-gradient(to bottom, transparent 0%, black 100%), linear-gradient(to right, white 0%, transparent 100%), hsl(180, 100%, 50%); }</style>
The color area supports several properties for configuration:

Control the base hue of the color area (0-360 degrees):

<sp-color-area hue="240"></sp-color-area>
The color area supports a wide variety of color formats for setting and getting color values:

<sp-color-area color="#f00"></sp-color-area>
<sp-color-area color="#f00f"></sp-color-area>
<sp-color-area color="#ff0000"></sp-color-area>
<sp-color-area color="#ff0000ff"></sp-color-area>

<sp-color-area color="rgb(255, 0, 0)"></sp-color-area>
<sp-color-area color="rgba(255, 0, 0, 0.5)"></sp-color-area>
<sp-color-area color="rgb(100%, 0%, 0%)"></sp-color-area>
<sp-color-area color="rgb 255 0 0"></sp-color-area>

<sp-color-area color="hsl(0, 100%, 50%)"></sp-color-area>
<sp-color-area color="hsla(0, 100%, 50%, 0.5)"></sp-color-area>
<sp-color-area color="hsl 0 100% 50%"></sp-color-area>

<sp-color-area color="hsv(0, 100%, 100%)"></sp-color-area>
<sp-color-area color="hsva(0, 100%, 100%, 0.5)"></sp-color-area>
<sp-color-area color="hsv 0 100% 100%"></sp-color-area>

<sp-color-area color="red"></sp-color-area>
<sp-color-area color="rebeccapurple"></sp-color-area>
When using the color elements, the `color` property will maintain the format you provided. For example, if you supply a color in `rgb()` format, `el.color` will return the color in `rgb()` format as well.

The `step` attribute controls the granularity of color selection when using keyboard navigation. It defines the increment size (between 0 and 1) for each movement when using arrow keys or other keyboard controls.

<sp-color-area></sp-color-area>

<sp-color-area step="0.05"></sp-color-area>

<sp-color-area step="0.005"></sp-color-area>
The step size affects:

*   Regular arrow key movements (moves by 1× step)
*   Shift+arrow key combinations (moves by 5× step)
*   Page Up/Page Down keys (moves by 10× step vertically)
*   Home/End keys (moves by 10× step horizontally)

A smaller step value provides more precise control but requires more key presses to move across the color area, while a larger step value allows for faster movement at the cost of precision. Choose a step size appropriate for your use case:

*   **Fine-tuning**: Use smaller values (0.001-0.01) for detailed color work
*   **General use**: The default (0.01) works well for most scenarios
*   **Quick selection**: Larger values (0.05-0.1) for faster navigation

The color area supports both left-to-right and right-to-left layouts:

<sp-color-area dir="rtl"></sp-color-area>
An `<sp-color-area>`'s height and width can be customized appropriately for its context.

<sp-color-area style=" width: 72px; height: 72px"></sp-color-area>
An `<sp-color-area>` in a disabled state shows that an input exists, but is not available in that circumstance. This can be used to maintain layout continuity and communicate that the area may become available later.

<sp-color-area disabled></sp-color-area>
The color area manages its focused state automatically, but you can also check the focused state programmatically:

const colorArea = document.querySelector('sp-color-area');
console.log(colorArea.focused); 
When using the color elements, use `el.color` to access the `color` property, which should manage itself in the colour format supplied. For example, If you supply a color in `rgb()` format, `el.color` should return the color in `rgb()` format, as well. In ColorArea, colours are formatted as hex values.

The current color formats supported are as follows:

*   Hex3, Hex4, Hex6, Hex8
*   HSV, HSVA
*   HSL, HSLA
*   RGB, RGBA
*   Named color strings (see full list)

The color area supports both mouse and touch interactions:

*   **Click**: Jump to a specific color position
*   **Drag**: Continuously adjust color while dragging
*   **Touch**: Full touch support for mobile devices

<sp-color-area @pointerdown="${(event)" =""></sp-color-area>
The color area automatically manages focus between its internal X and Y axis controls:

The `<sp-color-area>` is rendered with appropriate ARIA attributes to ensure accessibility for screen readers and keyboard navigation.

An `<sp-color-area>` renders accessible labels for each axis: _"saturation"_ and _"luminosity"_. Specify `label-x` and `label-y` attributes to override these defaults.

<sp-color-area label-x="Color intensity" label-y="Color brightness"></sp-color-area>
The color area supports comprehensive keyboard interaction for precise color selection:

Key Action Arrow Keys Move the color selection by one step Shift + Arrow Keys Move the color selection by a larger step (5x)Page Up/Page Down Move vertically by a large step (10x)Home/End Move horizontally by a large step (10x)
The component provides comprehensive ARIA support with different behavior for mobile and desktop:

*   **Role**: Uses native `input[type="range"]` elements with implicit "slider" roles for 2D color selection
*   **Role Description**: Announces as "2d slider" on desktop devices (omitted on mobile for better touch screen reader experience)
*   **Labels**: 
    *   Mobile: Simple axis labels (e.g., "saturation", "luminosity")
    *   Desktop: Combined labels (e.g., "saturation Color Picker", "luminosity Color Picker")

*   **Orientation**: Explicitly set as "horizontal" for X-axis and "vertical" for Y-axis
*   **Value Text**: Internationalized percentage values 
    *   Mobile: Single axis value (e.g., "45%")
    *   Desktop: Comprehensive context including both axes (e.g., "45%, saturation, 78%, luminosity")

*   **Fieldset**: Contains both sliders with appropriate labeling for mobile screen readers
*   **Presentation**: Wrapper divs marked with `role="presentation"` to avoid navigation confusion

The component provides comprehensive screen reader support through:

*   **Internationalized Values**: Percentage values are formatted according to the user's locale using `Intl.NumberFormat`
*   **Context-Aware Announcements**: Different announcement patterns for focus changes vs. value changes
*   **Focused State Management**: Special handling to prevent focus traps and ensure proper screen reader navigation
*   **Shadow DOM Optimization**: Dynamically creates shadow roots when focused to prevent duplicate tab stops in certain browsers
*   **Keyboard Focus Tracking**: Maintains the active axis (X or Y) to ensure consistent focus when navigating with a screen reader
*   **Value Change Context**: When values change, announces only the changed value; when focused, announces both axes for context

The component implements specific optimizations for mobile devices (Android and iOS):

*   **Platform Detection**: Uses `isAndroid()` and `isIOS()` to apply platform-specific behaviors
*   **Simplified ARIA**: Provides more concise labels and values on mobile to improve screen reader experience
*   **Touch Pointer Events**: Special handling for touch interactions vs. mouse interactions
*   **Mobile Focus States**: Different focus handling for touch vs. mouse input
*   **Fieldset Labeling**: Adds an explicit `aria-label="Color Picker"` to the fieldset only on mobile
*   **Omitted Role Description**: Removes the "2d slider" role description on mobile for better compatibility with mobile screen readers
*   **Simplified Value Text**: Announces only the current axis value without additional context to reduce verbosity on mobile

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

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   **color-area:** providing x and y attributes renders color handle correctly (#4240) (9eb5056)

*   **color-area:** providing x and y attributes renders color handle correctly (#4240) (9eb5056)

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   update deps graph, update link docs (#3709) (2deb284)

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   **color-area,color-slider:** color-area labeling, RTL support, vertical slider orientation(#3315) (ca2acda), closes #3313

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)
*   address westbrooks comments (634af60)
*   **color-area:** fix hue value for hsv and hsl (a66e111)
*   **color-area:** up and down arrows now work properly (44b9f74)
*   ensure streamingListener ends even if pointercancel not fired (74105f2)
*   expand support for maintaining hue and saturation across customization (fe18944)
*   flappy Slider/Color Area tests (c769c87)
*   include touch-action rule for draggable content (3f507e6)
*   key interaction handling no longer prevents "tab" presses (b542ce8)
*   leverage Color Controller to unify color interface across packages (fb71690)
*   lint away debugger statements (34a498e)
*   manage "focused" across more contexts (9273c15)
*   normalize focus passing during and after pointer events (357931b)
*   **overlay:** allow overlay-trigger to declaratively open overlay content (194a44e)
*   remove right click value setting (a44968d)
*   update package.json (455b626)
*   use hue normalized color in handle and allow focus (f9e1fa2)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **color-area:** add color-area pattern (dc15e1c)
*   **color-area:** separate X and Y aria labels to improve accessibility (e8d9768)
*   **color-area:** use core tokens (51a89de)
*   debug colour elements for a11y (7008f7c)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)

*   ensure streamingListener ends even if pointercancel not fired (74105f2)

**Note:** Version bump only for package @spectrum-web-components/color-area

*   **color-area:** use core tokens (51a89de)

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   leverage Color Controller to unify color interface across packages (fb71690)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   update lit-* dependencies, wip (377f3c8)

*   abstract "hasVisibleFocusInTree" functionality and return trigger focus after close (4f39f2c)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/color-area

*   **color-area:** separate X and Y aria labels to improve accessibility (e8d9768)

*   flappy Slider/Color Area tests (c769c87)
*   manage "focused" across more contexts (9273c15)

**Note:** Version bump only for package @spectrum-web-components/color-area

*   key interaction handling no longer prevents "tab" presses (b542ce8)

**Note:** Version bump only for package @spectrum-web-components/color-area

**Note:** Version bump only for package @spectrum-web-components/color-area

*   expand support for maintaining hue and saturation across customization (fe18944)
*   normalize focus passing during and after pointer events (357931b)

**Note:** Version bump only for package @spectrum-web-components/color-area

*   lint away debugger statements (34a498e)
*   **color-area:** fix hue value for hsv and hsl (a66e111)

*   include touch-action rule for draggable content (3f507e6)

*   use hue normalized color in handle and allow focus (f9e1fa2)

*   **color-area:** up and down arrows now work properly (44b9f74)

*   **overlay:** allow overlay-trigger to declaratively open overlay content (194a44e)
*   remove right click value setting (a44968d)

*   address westbrooks comments (634af60)
*   update package.json (455b626)

*   debug colour elements for a11y (7008f7c)
*   **color-area:** add color-area pattern (dc15e1c)

Property  Attribute  Type  Default  Description `color``color``ColorTypes``disabled``disabled``boolean``false``focused``focused``boolean``false``hue``hue``number``labelX``label-x``string``'saturation'``labelY``label-y``string``'luminosity'``step``step``number``0.01``value``value``ColorTypes``x``x``number``y``y``number`

Name  Description `gradient` a custom gradient visually outlining the available color values

Name  Type  Description `change``Event``An alteration to the value of the Color Area has been committed by the user.``input``Event``The value of the Color Area has changed.`
