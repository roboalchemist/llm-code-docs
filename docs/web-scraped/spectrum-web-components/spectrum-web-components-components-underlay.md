# Source: https://opensource.adobe.com/spectrum-web-components/components/underlay/

Title: Underlay: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/underlay/

Markdown Content:
An `<sp-underlay>` provides a visual layer between overlay content and the rest of your application. It is commonly used with modal dialogs and other overlay elements to create a visual separation and prevent interaction with the background content while the overlay is active.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/underlay?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/underlay?style=for-the-badge)

yarn add @spectrum-web-components/underlay

Import the side effectful registration of `<sp-underlay>` via:

import '@spectrum-web-components/underlay/sp-underlay.js';

When looking to leverage the `Underlay` base class as a type and/or for extension purposes, do so via:

import { Underlay } from '@spectrum-web-components/underlay';

When using an `<sp-underlay>` with overlay content, place it as a sibling element before your overlay content.

<style> sp-underlay:not([open]) + sp-dialog { display: none; } sp-underlay + sp-dialog { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1; background: var(--spectrum-gray-100); }</style>

<sp-button onclick=" console.log(this.nextElementSibling); this.nextElementSibling.open = true; ">
  Open dialog with underlay element
</sp-button>

<sp-underlay></sp-underlay>
<sp-dialog size="s">
  <h1 slot="heading">Hello, I'm an overlay!</h1>
  <p>Enjoy your day...</p>
  <sp-button slot="button" onclick=" this.parentElement.previousElementSibling.open = false; " >
    Close
  </sp-button>
</sp-dialog>
To ensure proper layering of your overlay content with the underlay, use appropriate CSS:

<style> sp-underlay:not([open]) + sp-dialog { display: none; } sp-underlay + sp-dialog { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1; }</style>
The `<sp-underlay>` element helps create an accessible modal experience by:

1.   Providing visual separation between modal content and the rest of the page
2.   Supporting proper focus management when used with modal dialogs
3.   Helping communicate the modal state to assistive technologies

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   **tray:** only allow "click" events when they "pointerdown"ed on the Underlay (#4020) (4f9aa4a)

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   **underlay:** use core tokens (9c555ab)

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   add dialog, dialog-wrapped, and underlay elements (3df9050)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **underlay:** update spectrum css input (edf1a4b)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

**Note:** Version bump only for package @spectrum-web-components/underlay

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **underlay:** update spectrum css input (edf1a4b)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **underlay:** update spectrum css input (edf1a4b)

**Note:** Version bump only for package @spectrum-web-components/underlay

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/underlay

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/underlay

*   add dialog, dialog-wrapped, and underlay elements (3df9050)

Property  Attribute  Type  Default  Description `open``open``boolean``false`

Name  Type  Description `close``Event``When the underlay is "clicked" and the consuming pattern should chose whether to close based on that interaction`
