# Source: https://opensource.adobe.com/spectrum-web-components/components/popover/

Title: Popover: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/popover/

Markdown Content:
An `<sp-popover>` is used to display transient content (menus, options, additional actions etc.) and appears when clicking/tapping on a source (tools, buttons, etc.) It stands out via its visual style (stroke and drop shadow) and floats on top of the rest of the interface. This component does not implement the actual overlay behavior and interactions. This is handled by the `Overlay` system.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/popover?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/popover?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/popover

Import the side effectful registration of `<sp-popover>` via:

import '@spectrum-web-components/popover/sp-popover.js';

When looking to leverage the `Popover` base class as a type and/or for extension purposes, do so via:

import { Popover } from '@spectrum-web-components/popover';
<div style=" position: relative; height: 100px; ">
  <sp-popover open>
    Cupcake ipsum dolor sit amet jelly beans. Chocolate jelly caramels.
  </sp-popover>
</div>
Default popover with no tip and no placement. Popovers will fill up the space of their containing element by default. The default popover has no padding.

<div style=" position: relative; height: 180px; max-width: 320px; ">
  <sp-popover variant="default" open>
    <h2>Popover title</h2>
    <p>
      Cupcake ipsum dolor sit amet jelly beans. Chocolate jelly caramels. Icing
      soufflé chupa chups donut cheesecake. Jelly-o chocolate cake sweet roll
      cake danish candy biscuit halvah
    </p>
  </sp-popover>
</div>
To apply a managed amount of padding within your `<sp-popover>`, you may choose to wrap your slotted content in an `<sp-dialog>` element, as seen below:

<div style=" position: relative; height: 250px; max-width: 320px; ">
  <sp-popover open>
    <sp-dialog>
      <h3 slot="heading">Popover title</h3>
      Cupcake ipsum dolor sit amet jelly beans. Chocolate jelly caramels. Icing
      soufflé chupa chups donut cheesecake. Jelly-o chocolate cake sweet roll
      cake danish candy biscuit halvah
    </sp-dialog>
  </sp-popover>
</div>
The `placement` attribute can be used to customize how the `<sp-popover>` points to its related content. `placement="top"` will point down to the related content from the top, etc.

Top<div style=" position: relative; height: 250px; max-width: 320px; ">
  <sp-popover placement="top" tip open>
    <sp-dialog>
      <h3 slot="heading">Popover title</h3>
      Cupcake ipsum dolor sit amet jelly beans. Chocolate jelly caramels. Icing
      soufflé chupa chups donut cheesecake. Jelly-o chocolate cake sweet roll
      cake danish candy biscuit halvah
    </sp-dialog>
  </sp-popover>
</div>Right<div style=" position: relative; height: 200px; max-width: 320px; ">
  <sp-popover placement="right" tip open>
    <sp-dialog>
      <h3 slot="heading">Popover title</h3>
      Cupcake ipsum dolor sit amet jelly beans. Chocolate jelly caramels. Icing
      soufflé chupa chups donut cheesecake. Jelly-o chocolate cake sweet roll
      cake danish candy biscuit halvah
    </sp-dialog>
  </sp-popover>
</div>Bottom<div style=" position: relative; height: 200px; max-width: 320px; ">
  <sp-popover placement="bottom" tip open>
    <sp-dialog>
      <h3 slot="heading">Popover title</h3>
      Cupcake ipsum dolor sit amet jelly beans. Chocolate jelly caramels. Icing
      soufflé chupa chups donut cheesecake. Jelly-o chocolate cake sweet roll
      cake danish candy biscuit halvah
    </sp-dialog>
  </sp-popover>
</div>Left<div style=" position: relative; height: 200px; max-width: 320px; ">
  <sp-popover placement="left" tip open>
    <sp-dialog>
      <h3 slot="heading">Popover title</h3>
      Cupcake ipsum dolor sit amet jelly beans. Chocolate jelly caramels. Icing
      soufflé chupa chups donut cheesecake. Jelly-o chocolate cake sweet roll
      cake danish candy biscuit halvah
    </sp-dialog>
  </sp-popover>
</div>
For components used with a popover, see the accessibility guidelines of the particular component.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/overlay@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/overlay@1.11.1

*   Updated dependencies [`02b2d7d`, `f07344f`, `1d76b70`, `cadc39e`, `4cb0b7b`, `9cb816b`]: 
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/overlay@1.10.0

*   Updated dependencies [`a19cbe3`]: 
    *   @spectrum-web-components/overlay@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/overlay@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies [`14486d6`, `ee1bae6`, `14486d6`]: 
    *   @spectrum-web-components/overlay@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies [`a646ae8`]: 
    *   @spectrum-web-components/overlay@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   #5341`03a4439` Thanks @renovate! - 📝 #​3566 Thanks @​aramos-adobe!

Popover overflow bug on Safari

    *   `translateZ` has been added to the open popover to prevent clipping of the `filter: drop-shadow` when overflow is applied. `translateZ` or `translate3d` on the open state accelerates the component to the GPU layer maintaining any transformations and animations.
    *   `overflow: visible` applied to CSS `*--withTip` so the tip is still visible if overflow is applied to the component.

*   Updated dependencies [`53f3769`]:

    *   @spectrum-web-components/overlay@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies [`8f8735c`]: 
    *   @spectrum-web-components/overlay@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies [`46cd782`, `70f5f6f`]: 
    *   @spectrum-web-components/overlay@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies [`468314f`]: 
    *   @spectrum-web-components/overlay@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   remove popover's dialog property (#4751)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   **popover:** correct tip delivery size (#4018) (4ff403e)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   **popover:** leverage Overlay v2 (cde0a16)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   **popover:** use core tokens (68328cc)

**Note:** Version bump only for package @spectrum-web-components/popover

*   add content flow fallbacks to the position manager (c008957)
*   allow ActiveOverlay to manage open state (a7c4cff)
*   constrain overlay to available window size (9729b55)
*   correct @element jsDoc listing across library (c97a632)
*   correct max size calculation for overlays (0585f7f)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   **menu:** add support for submenu interactions (68399af)
*   position tip shapes for bi-directional delivery (35654de)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **tooltip:** correct arrow orientation, remove popper-arrow-rotate (fcd6ea2)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update screen reader interface with menu items list (16756b5)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)
*   use less restrictive overlay sizing (f6917aa)

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   allow activation of longpress content (55e71fd)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   **popover:** update spectrum css input (0f7a00e)
*   rework overlays to use popper (e17d1bb)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   add content flow fallbacks to the position manager (c008957)

**Note:** Version bump only for package @spectrum-web-components/popover

*   use less restrictive overlay sizing (f6917aa)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   **menu:** add support for submenu interactions (68399af)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   update screen reader interface with menu items list (16756b5)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   correct max size calculation for overlays (0585f7f)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   allow activation of longpress content (55e71fd)

*   position tip shapes for bi-directional delivery (35654de)
*   **tooltip:** correct arrow orientation, remove popper-arrow-rotate (fcd6ea2)
*   allow ActiveOverlay to manage open state (a7c4cff)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **popover:** update spectrum css input (0f7a00e)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **popover:** update spectrum css input (0f7a00e)

**Note:** Version bump only for package @spectrum-web-components/popover

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/popover

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   constrain overlay to available window size (9729b55)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

**Note:** Version bump only for package @spectrum-web-components/popover

*   rework overlays to use popper (e17d1bb)

**Note:** Version bump only for package @spectrum-web-components/popover

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use @adobe/spectrum-css@2.15.1 (3918888)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/popover

Property  Attribute  Type  Default  Description `open``open``boolean``false` Whether the popover is visible or not. `placement``placement``"top" | "top-start" | "top-end" | "right" | "right-start" | "right-end" | "bottom" | "bottom-start" | "bottom-end" | "left" | "left-start" | "left-end"``tip``tip``boolean``false`

Name  Description `default slot` content to display within the Popover
