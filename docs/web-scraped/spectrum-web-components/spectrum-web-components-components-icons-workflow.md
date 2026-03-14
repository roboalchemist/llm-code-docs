# Source: https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/

Title: Icons Workflow: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/

Markdown Content:
Deliver Spectrum Workflow Icons as either:

*   Registered custom elements (`<sp-icon-abc>`)
*   Unregistered class definitions (`IconAbc`)
*   Functions with customizable template tags to be used across various frameworks (`AbcIcon()`)

Search a full list of icons to find an icon for your project or find technical information about extended use cases, like consuming this package in various UI frameworks below.

When planning how to leverage these icons in the visual delivery of your application, remember to consult Spectrum's Iconography Guidelines.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/icons-workflow?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/icons-workflow?style=for-the-badge)

yarn add @spectrum-web-components/icons-workflow

Import the side effectful registration of a single element (e.g. `<sp-icon-abc>`) via:

import '@spectrum-web-components/icons-workflow/icons/sp-icon-abc.js';

Leverage a single icon base class (e.g. `IconAbc`) as a type, or for extension purposes, do so, via:

import { IconAbc } from '@spectrum-web-components/icons-workflow/src/elements/IconAbc.js';

Search the available Spectrum Workflow icons below.

You can import raw icons (e.g. `AbcIcon()`) via:

import { AbcIcon } from '@spectrum-web-components/icons-workflow/src/icons/ABC.js';
`@spectrum-web-components/icons-workflow` exports _all_ icons. If your build process tree-shakes dependencies, you can import from it directly:

import { AbcIcon } from '@spectrum-web-components/icons-workflow';
These icon literals are prepared with the `html` template tag from `lit-html`, the default value of an icon export will be as follows:

import { LitElement, html } from 'lit-element';
import '@spectrum-web-components/icon';
import { AbcIcon } from '@spectrum-web-components/icons-workflow';

class ElementWithIcon extends LitElement {
    protected override render(): TemplateResult {
        return html` <sp-icon> ${AbcIcon()} </sp-icon> `
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

import { AbcIcon } from '@spectrum-web-components/icons-workflow';

console.log(AbcIcon());

When working in the context of other frameworks, it is possible to import the icons with a generic template tag as follows:

import { AbcIcon } from '@spectrum-web-components/icons-workflow/src/icons.js';

console.log(AbcIcon());

What's more, if you're already working with a specific parser in your project, you can assign it as the one to use when delivering the icons in order to be sure that the SVG content is delivered as parsed content to your final template. The means if you were working with Preact via the `htm` tag as bound to the provided hyperscript function:

import {
  AbcIcon,
  setCustomTemplateLiteralTag,
} from '@spectrum-web-components/icons-workflow/src/icons.js';
import htm from 'htm';
import { h } from 'preact';

const hPreact = htm.bind(h);

setCustomTemplateLiteralTag(hPreact);

console.log(AbcIcon());

In this way the icons exported by `@spectrum-web-components/icons-workflow` can be leveraged in projects powered by the the likes of hyperHTML, lighterhtml, lit-html, Preact, React, Vanilla JS, Vue.js, and more!

Review the accessibility guidelines for the icon.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/icon@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/icon@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/icon@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   #5735`bdf54c1` Thanks @rubencarvalho! - - Upgraded to `@adobe/spectrum-css-workflow-icons@5.0.0`. - Includes changes from previous a4u upstream releases: - Added `S2_Icon_HeartFilled_20_N.svg`, updated `S2_Icon_SpeedFast_20_N.svg`. - Replaced all 22×20px Cloud State icons with 20px variants. - Removed deprecated multi-colored error icon. Added new Cloud State icons (`Disconnected`, `Error`, `InProgress`, `Online`, `Paused`, `Pending`, `SlowConnection`). - Updated several other icons (`CloseCaptions`, `CommentHide`, `Community`, etc.). 
    *   For the full changelog, see: https://github.com/adobe/spectrum-css-workflow-icons/pull/50

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   #5367`f6cebbd` Thanks @Rajdeepc! - Added missing S2 icons

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   **icon:** remove size300 suffix from chevron and checkmark icons in Spectrum 2 (#4904) (a22f42b)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   **icon:** use core tokens (a11ef6b)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   **infield-button:** add infield-button package (057b885)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   **alert-dialog:** add Alert Dialog package (#3501) (1062847)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   correct @element jsDoc listing across library (c97a632)
*   **icon:** clean up docs and types for available size values (c38850d)
*   **icons-workflow:** rename icons/files to avoid ad blocking (842b081)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   remove "type: "module"" in package.json for node 12 (c9f76e2)

*   add and use icons-ui package (d9c3ab2)
*   **icons-workflow:** add workflow icons package (6b09287)
*   **icons-workflow:** update spectrum css input (549b4b6)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   track the associated Spectrum CSS package (86b1be5)
*   update lit-* dependencies, wip (377f3c8)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   track the associated Spectrum CSS package (86b1be5)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   **icons-workflow:** rename icons/files to avoid ad blocking (842b081)

*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   **icon:** clean up docs and types for available size values (c38850d)
*   include the "types" entry in package.json files (b432f59)

*   **icons-workflow:** update spectrum css input (549b4b6)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

*   include the "types" entry in package.json files (b432f59)

*   **icons-workflow:** update spectrum css input (549b4b6)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/icons-workflow

*   remove "type: "module"" in package.json for node 12 (c9f76e2)

*   add and use icons-ui package (d9c3ab2)

*   use "sideEffects" listing in package.json (7271614)

*   **icons-workflow:** add workflow icons package (6b09287)

Property  Attribute  Type  Default  Description `label``label``string``''``size``size``'xxs' | 'xs' | 's' | 'm' | 'l' | 'xl' | 'xxl' | undefined`
