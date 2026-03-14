# Source: https://opensource.adobe.com/spectrum-web-components/components/iconset/

Title: Iconset: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/iconset/

Markdown Content:
Extend either the `Iconset` or `IconsetSVG` exports of this package to supply your application with a custom icon set to power the use of `<sp-icon>` elements throughout. Give your new icon set a custom name, and you'll be ready to supply them as `<sp-icon name="custom-icons:icon">` across your application.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/iconset?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/iconset?style=for-the-badge)

yarn add @spectrum-web-components/iconset
import { TemplateResult } from 'lit-element';
import { IconsetSVG } from '@spectrum-web-components/iconset/src/iconset-svg.js';

import { CustomIconSet } from 'your-icon-set.js';

export class IconsLarge extends IconsetSVG {
  public constructor() {
    super();
    this.name = 'custom-icons'; 
  }

  protected renderDefaultContent(): TemplateResult {
    return CustomIconSet;
  }
}
Iconsets have been deprecated and will be removed from the project in an upcoming version. Using a technique that ensures only the icons actually leveraged in your application are present in your build, like UI Icons (../icons-ui/) or Workflow Icons (../icons-workflow/), will ensure smaller bundles and higher performance for you visitor. For non-Spectrum icons, you can still slot SVG and image content into an `sp-icon` element or sanitize the SVG to a template literal so that it can be returned from the `render()` method in an extension of `IconBase` to create your own named icon element.

Review the accessibility guidelines for the icon.

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

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

*   **icon:** remove size300 suffix from chevron and checkmark icons in Spectrum 2 (#4904) (a22f42b)

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)
*   apply "HelpTextMixin" to form elements (a952447)
*   ensure browser understandable extensions (f4e59f7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   lint away debugger statements (34a498e)
*   manage updated node types (0517fc1)
*   normalize "event" and "error" argument names (8d382cd)
*   remove ":" based namespacing of events (d77a843)
*   remove "type: "module"" in package.json for node 12 (c9f76e2)
*   use icons without "size" values (3fc7c91)

*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **iconset:** update spectrum css input (914150a)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   update lit-* dependencies, wip (377f3c8)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

*   manage updated node types (0517fc1)

**Note:** Version bump only for package @spectrum-web-components/iconset

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

*   apply "HelpTextMixin" to form elements (a952447)

*   update lit-* dependencies, wip (377f3c8)

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)

**Note:** Version bump only for package @spectrum-web-components/iconset

*   lint away debugger statements (34a498e)

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

*   include the "types" entry in package.json files (b432f59)
*   use icons without "size" values (3fc7c91)

*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **iconset:** update spectrum css input (914150a)

*   include the "types" entry in package.json files (b432f59)
*   use icons without "size" values (3fc7c91)

*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **iconset:** update spectrum css input (914150a)

**Note:** Version bump only for package @spectrum-web-components/iconset

*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/iconset

**Note:** Version bump only for package @spectrum-web-components/iconset

*   ensure browser understandable extensions (f4e59f7)

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/iconset

*   remove "type: "module"" in package.json for node 12 (c9f76e2)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/iconset

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   remove ":" based namespacing of events (d77a843)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/iconset
