# Source: https://opensource.adobe.com/spectrum-web-components/components/asset/

Title: Asset: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/asset/

Markdown Content:
Use an `<sp-asset>` element to visually represent a file, folder or image in your application. File and folder representations will center themselves horizontally and vertically in the space provided to the element. Images will be contained to the element, growing to the element's full height while centering itself within the width provided.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/asset?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/asset?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/asset

Import the side effectful registration of `<sp-asset>` via:

import '@spectrum-web-components/asset/sp-asset.js';

When looking to leverage the `Asset` base class as a type and/or for extension purposes, do so via:

import { Asset } from '@spectrum-web-components/asset';
<sp-asset style="height: 128px">
  <img src="https://picsum.photos/500/500" alt="Demo Image" />
</sp-asset><div class="flex">
  <sp-asset variant="file"></sp-asset>
  <sp-asset variant="file" label="Named File Asset"></sp-asset>
</div><div class="flex">
  <sp-asset variant="folder"></sp-asset>
  <sp-asset variant="folder" label="Named Folder Asset"></sp-asset>
</div>

*   Updated dependencies [`6f5419a`]: 
    *   @spectrum-web-components/core@0.0.4
    *   @spectrum-web-components/base@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/core@0.0.3
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`283f0fe`, `1d76b70`, `9cb816b`]: 
    *   @spectrum-web-components/core@0.0.2
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

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

*   **asset:** include alternative text for the file/folder versions (92a091c)
*   **asset:** surface label attribute for folder/file "assets" (861696b)
*   ensure browser understandable extensions (f4e59f7)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **asset:** add the asset pattern (a7c00bb)
*   **asset:** update spectrum css input (b3f0d70)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

*   **asset:** surface label attribute for folder/file "assets" (861696b)

**Note:** Version bump only for package @spectrum-web-components/asset

**Note:** Version bump only for package @spectrum-web-components/asset

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   update file path access (8898bf7)
*   **asset:** include alternative text for the file/folder versions (92a091c)
*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **asset:** update spectrum css input (b3f0d70)

*   update file path access (8898bf7)
*   **asset:** include alternative text for the file/folder versions (92a091c)
*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **asset:** update spectrum css input (b3f0d70)

**Note:** Version bump only for package @spectrum-web-components/asset

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/asset

*   ensure browser understandable extensions (f4e59f7)

*   **asset:** add the asset pattern (a7c00bb)

Property  Attribute  Type  Default  Description `label``label``string``''` Accessible label for the asset’s file or folder variant. `variant``variant``AssetVariant | undefined` The variant of the asset. When not provided, slot content is rendered (e.g., an image).

Name  Description `default slot` content to be displayed in the asset when an acceptable value for `file` is not present
