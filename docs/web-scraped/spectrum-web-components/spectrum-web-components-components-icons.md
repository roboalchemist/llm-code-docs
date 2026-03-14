# Source: https://opensource.adobe.com/spectrum-web-components/components/icons/

Title: Icons: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/icons/

Markdown Content:
The `<sp-icons-medium>` and `<sp-icons-large>` elements included in this package supply your application with the Spectrum CSS medium and large icons for use in the `<sp-icon>` element. Include at least one of these elements in a project that makes use of icons in these sets. You can also include these sets in the scope of any element that leverages them, as they will be deduplicated to ensure all of your components can deliver the icons included therein.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/icons?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/icons?style=for-the-badge)

yarn add @spectrum-web-components/icons

Import the side effectful registration of `<sp-icons-medium>` or `<sp-icons-large>` via:

import '@spectrum-web-components/icons/sp-icons-medium.js';
import '@spectrum-web-components/icons/sp-icons-large.js';

When looking to leverage the `IconsMedium` or `IconsLarge` base classes as a type and/or for extension purposes, do so via:

import { IconsMedium, IconsLarge } from '@spectrum-web-components/icons';

The `Icons` package has been deprecated as part of the removal of the `Iconset` package from the library and will be removed in an upcoming release. To optimize your build and ensure smaller bundles and higher performance for your users, consider using techniques that include only the icons actually used in your application. For Spectrum icons, you can use UI Icons or Workflow Icons.

For non-Spectrum icons, you can still:

1.   Slot SVG or image content into an `sp-icon` element, or
2.   Sanitize the SVG and convert it to a template literal to use within the `render()` method of an extension of `IconBase` to create your own custom named icon element.```

Review the accessibility guidelines for the icon.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/iconset@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/iconset@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/iconset@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/iconset@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/iconset@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

*   correct @element jsDoc listing across library (c97a632)
*   ensure browser understandable extensions (f4e59f7)
*   **icons:** process icons for use as UIIcons (47a43d7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   remove ":" based namespacing of events (d77a843)
*   update side effect listings (8160d3a)

*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** add workflow icons package (6b09287)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **icons:** update spectrum css input (296738e)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

*   include the "types" entry in package.json files (b432f59)

*   **action-button:** add action button pattern (03ac00a)
*   **icons:** update spectrum css input (296738e)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

*   include the "types" entry in package.json files (b432f59)

*   **action-button:** add action button pattern (03ac00a)
*   **icons:** update spectrum css input (296738e)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

**Note:** Version bump only for package @spectrum-web-components/icons

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/icons

*   ensure browser understandable extensions (f4e59f7)

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

*   use "sideEffects" listing in package.json (7271614)

*   **icons-workflow:** add workflow icons package (6b09287)

**Note:** Version bump only for package @spectrum-web-components/icons

**Note:** Version bump only for package @spectrum-web-components/icons

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use @adobe/spectrum-css@2.15.1 (3918888)

*   remove ":" based namespacing of events (d77a843)

*   **icons:** process icons for use as UIIcons (47a43d7)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/icons
