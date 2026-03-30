# Source: https://opensource.adobe.com/spectrum-web-components/components/tags/

Title: Tags: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/tags/

Markdown Content:
`<sp-tags>` elements contain a collection of `<sp-tag>` elements and allow users to categorize content. They can represent keywords or people, and are grouped to describe an item or a search request.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/tags?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/tags?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/tags
Import the side effectful registration of `<sp-tags>` or `<sp-tag>` via:

import '@spectrum-web-components/tags/sp-tags.js';
import '@spectrum-web-components/tags/sp-tag.js';
When looking to leverage the `Tags` or `Tag` base classes as a type and/or for extension purposes, do so via:

import { Tags, Tag } from '@spectrum-web-components/tags';
Tags are created from the following parts:

*   **Tags**: The container component (`<sp-tags>`) that manages a collection of `<sp-tag>` elements.
*   **Tag**: The individual tag element (`<sp-tag>`) represents a single tag. Read more about the `Tag` component.

Basic Tags<sp-tags>
  <sp-tag>Tag 1</sp-tag>
  <sp-tag invalid>Tag 2</sp-tag>
  <sp-tag disabled>Tag 3</sp-tag>
</sp-tags>With Avatars<sp-tags>
    <sp-tag>
        Tag 1
        <sp-avatar slot="avatar" label="Tag 1" src=https://picsum.photos/500/500 ></sp-avatar>
    </sp-tag>
    <sp-tag invalid>
        Tag 2
        <sp-avatar slot="avatar" label="Tag 1" src=https://picsum.photos/500/500 ></sp-avatar>
    </sp-tag>
    <sp-tag disabled>
        Tag 3
        <sp-avatar slot="avatar" label="Tag 1" src=https://picsum.photos/500/500 ></sp-avatar>
    </sp-tag>
</sp-tags>With Icons<sp-tags>
  <sp-tag>
    Tag 1
    <sp-icon-magnify slot="icon" size="s"></sp-icon-magnify>
  </sp-tag>
  <sp-tag invalid>
    Tag 2
    <sp-icon-magnify slot="icon" size="s"></sp-icon-magnify>
  </sp-tag>
  <sp-tag disabled>
    Tag 3
    <sp-icon-magnify slot="icon" size="s"></sp-icon-magnify>
  </sp-tag>
</sp-tags>
`<sp-tags>` is a `role="list"` container that manages a collection of `<sp-tag>` elements. It has an `aria-label` attribute that defaults to `Tags`.

`<sp-tags>` uses the roving tabindex pattern for efficient keyboard navigation. `Tab` enters the collection, arrow keys navigate between tags, and only deletable tags are focusable. The container provides `role="list"` semantics with each tag as a `role="listitem"` for proper screen reader support.

**Mouse**

*   Read-only tags: Do not get mouse functionality besides a mouse cursor on hover and do not have interactive functionality.

**Keyboard**

*   Read-only tags: Cannot be operated by a keyboard and have no interactive functionality.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`, `7d23140`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`00eb0a8`]: 
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`4e06533`]:

    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   **icon:** use core tokens (a11ef6b)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   **tags:** make the 'delete' event cancelable (#3778) (d9afd41)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   **grid:** grid focusgroup fix on mutationObserver (#3684) (5d47db5)

**Note:** Version bump only for package @spectrum-web-components/tags

*   **tags:** add mod for clear button width (bea891f)

**Note:** Version bump only for package @spectrum-web-components/tags

*   added default focus in focus group (1abe7e7)
*   added default focus in focus group (cd59f18)
*   added Mutation Observer in the tags workflow (3af1861)
*   parentNode declaration (c45fdc3)
*   removed mutation controller from tags and added to focusgroup (aaa1bc0)
*   **tags:** delete functionality working (60e6c2e)
*   **tags:** performed the suggested changes (6e3ef36)
*   **tags:** removed extra white spaces (196bdae)
*   **tags:** some minor chnages (36886fc)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   **shared:** allow "disabled" first to return to "tabindex=0" in "focusable" (160bc59)

*   add support for "readonly" attribute (4bce3b7)
*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   correct @element jsDoc listing across library (c97a632)
*   ensure browser understandable extensions (f4e59f7)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   remove errant readme content, correct icon selector (3dd1fb1)
*   stop merging selectors in a way that alters the cascade (369388f)
*   support matching keydown to [dir] (70b40a9)
*   **tags:** correct render types (ecfb6ab)
*   **tags:** gate focus with deletable attribute (d5e79f6)
*   **tags:** support distant sibling selectors (a8dcf7f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** add action-group pattern (d2de766)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tags:** add tags pattern (ae91865)
*   **tags:** manage aria-disabled from disabled attribute (657eba8)
*   **tags:** update spectrum css input (f8a59ed)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use core tokens (d569672)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   use core tokens (d569672)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/tags

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   **tags:** gate focus with deletable attribute (d5e79f6)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   add support for "readonly" attribute (4bce3b7)

**Note:** Version bump only for package @spectrum-web-components/tags

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **action-button:** add action button pattern (03ac00a)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **tags:** update spectrum css input (f8a59ed)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **tags:** update spectrum css input (f8a59ed)

**Note:** Version bump only for package @spectrum-web-components/tags

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/tags

*   support matching keydown to dir
*   **tags:** correct render types (ecfb6ab)
*   **tags:** support distant sibling selectors (a8dcf7f)

*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   **action-group:** add action-group pattern (d2de766)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   ensure browser understandable extensions (f4e59f7)

**Note:** Version bump only for package @spectrum-web-components/tags

*   **tags:** manage aria-disabled from disabled attribute (657eba8)
*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/tags

**Note:** Version bump only for package @spectrum-web-components/tags

*   remove errant readme content, correct icon selector (3dd1fb1)

*   **tags:** add tags pattern (ae91865)

Name  Description `default slot` Tag elements to manage as a group
