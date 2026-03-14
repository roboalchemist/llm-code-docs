# Source: https://opensource.adobe.com/spectrum-web-components/components/icons-ui/

Title: Icons UI: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/icons-ui/

Markdown Content:
Deliver Spectrum UI Icons as either:

*   Registered custom elements (`<sp-icon-arrow75>`)
*   Unregistered class definitions (`IconArrow75`)
*   Functions with customizable template tags to be used across various frameworks (`Arrow75Icon()`)

Search a full list of icons to find an icon for your project or find technical information about extended use cases, like consuming this package in various UI frameworks below.

Remember to consult Spectrum's Iconography Guidelines when planning how to leverage these icons in the visual delivery of your application.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/icons-ui?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/icons-ui?style=for-the-badge)

yarn add @spectrum-web-components/icons-ui

Import the side effectful registration of a single element (e.g. `<sp-icon-arrow75>`) via:

import '@spectrum-web-components/icons-ui/icons/sp-icon-arrow75.js';

Leverage a single icon base class (e.g. `IconArrow75`) as a type, or for extension purposes, do so, via:

import { IconArrow75 } from '@spectrum-web-components/icons-ui/src/elements/IconArrow75.js';

Search the available Spectrum Workflow icons below.

You can import raw icons (e.g. `Arrow75Icon()`) via:

import { Arrow75Icon } from '@spectrum-web-components/icons-ui/src/icons/Arrow75.js';
`@spectrum-web-components/icons-ui` exports _all_ icons. If your build process tree-shakes dependencies, you can import from it directly:

import { Arrow75Icon } from '@spectrum-web-components/icons-ui';
These icon literals are prepared with the `html` template tag from `lit-html`, the default value of an icon export will be as follows:

import { LitElement, html } from 'lit-element';
import '@spectrum-web-components/icon';
import { Arrow75Icon } from '@spectrum-web-components/icons-ui';

class ElementWithIcon extends LitElement {
    protected override render(): TemplateResult {
        return html` <sp-icon> ${Arrow75Icon()} </sp-icon> `
    }
}

customElements.define('element-with-icon', ElementWithIcon);
Every icons can be customized via the following options:

{
    width: 24, 
    height: 24, 
    hidden: false, 
    title: 'Icon title', 
}
The default exports of this package are pre-wrapped via `setCustomTemplateLiteralTag` in the `html` template tag from `lit-html`, and work like the following::

import { Arrow75Icon } from '@spectrum-web-components/icons-ui';

console.log(Arrow75Icon());

When working in the context of other frameworks, it is possible to import the icons with a generic template tag as follows:

import { Arrow75Icon } from '@spectrum-web-components/icons-ui/src/icons.js';

console.log(Arrow75Icon());

What's more, if you're already working with a specific parser in your project, you can assign it as the one to use when delivering the icons in order to be sure that the SVG content is delivered as parsed content to your final template. The means if you were working with Preact via the `htm` tag as bound to the provided hyperscript function:

import {
  Arrow75Icon,
  setCustomTemplateLiteralTag,
} from '@spectrum-web-components/icons-ui/src/icons.js';
import htm from 'htm';
import { h } from 'preact';

const hPreact = htm.bind(h);

setCustomTemplateLiteralTag(hPreact);

console.log(Arrow75Icon());

In this way, the icons exported by `@spectrum-web-components/icons-ui` can be leveraged in projects powered by the likes of hyperHTML, lighterhtml, lit-html, Preact, React, Vanilla JS, Vue.js, and more!

Review the accessibility guidelines for the icon.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/iconset@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/iconset@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/iconset@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/iconset@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/iconset@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/iconset@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/iconset@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/iconset@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/iconset@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/iconset@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/iconset@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/iconset@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   **icon:** remove size300 suffix from chevron and checkmark icons in Spectrum 2 (#4904) (a22f42b)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   **infield-button:** add infield-button package (057b885)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   correct @element jsDoc listing across library (c97a632)
*   **icon:** clean up docs and types for available size values (c38850d)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   remove "type: "module"" in package.json for node 12 (c9f76e2)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   add and use icons-ui package (d9c3ab2)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **icons-ui:** update spectrum css input (4cb87ff)
*   **icons-ui:** vend fully registered icon components (915a7b5)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   **icon:** clean up docs and types for available size values (c38850d)
*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **icons-ui:** update spectrum css input (4cb87ff)
*   **icons-ui:** vend fully registered icon components (915a7b5)

*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **icons-ui:** update spectrum css input (4cb87ff)
*   **icons-ui:** vend fully registered icon components (915a7b5)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/icons-ui

*   remove "type: "module"" in package.json for node 12 (c9f76e2)

*   add and use icons-ui package (d9c3ab2)

Property  Attribute  Type  Default  Description `label``label``string``''``size``size``'xxs' | 'xs' | 's' | 'm' | 'l' | 'xl' | 'xxl' | undefined`
