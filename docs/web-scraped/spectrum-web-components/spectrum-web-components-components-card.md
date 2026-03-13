# Source: https://opensource.adobe.com/spectrum-web-components/components/card/

Title: Card: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/card/

Published Time: Thu, 12 Mar 2026 20:57:05 GMT

Markdown Content:
Card: Spectrum Web Components
===============
[Spectrum Web Components ==========================](https://opensource.adobe.com/spectrum-web-components/index.html)

sp-card
=======

NPM 1.11.2

View Storybook

Try it on Stackblitz

Overview API Changelog

Overview
--------

#Section titled Overview

An `<sp-card>` represents a rectangular card that contains a variety of text and image layouts. Cards are typically used to encapsulate units of a data set, such as a gallery of image/caption pairs.

### Usage

#Section titled Usage

![Image 4: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/card?style=for-the-badge)![Image 5: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/card?style=for-the-badge)![Image 6: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/card

Import the side effectful registration of `<sp-card>` via:

import '@spectrum-web-components/card/sp-card.js';

When looking to leverage the `Card` base class as a type and/or for extension purposes, do so via:

import { Card } from '@spectrum-web-components/card';

### Anatomy

#Section titled Anatomy

Normal cards can contain a heading, a subheading, a cover photo, and a footer.

<sp-card heading="Card Heading">
  <img alt="" slot="cover-photo" src="https://picsum.photos/250/300" />
  <span slot="subheading">JPG photo</span>
  <div slot="footer">Footer</div>
</sp-card>

#### Heading

#Section titled Heading

By default, the heading for an `<sp-card>` is applied via the `heading` attribute, which is restricted to string content only. For HTML content, use the `heading` slot instead.

attribute<sp-card heading="Card Heading" subheading="JPG Photo" style="--spectrum-card-body-header-height: auto;">
  <img alt="" slot="cover-photo" src="https://picsum.photos/250/300" />
  <div slot="footer">Footer</div>
</sp-card>slot<sp-card subheading="JPG Photo" style="--spectrum-card-body-header-height: auto;">
  <h1 slot="heading">Card Heading</h1>
  <img alt="" slot="cover-photo" src="https://picsum.photos/250/300" />
  <div slot="footer">Footer</div>
</sp-card>

#### Linking

#Section titled Linking

An `<sp-card>` can be provided with an `href` attribute in order for it to act as one large anchor element. When leveraging the `href` attribute, the `download`, `target` and `rel` attributes customize the card's linking behavior. Use them as follows:

<sp-card heading="Card Title" subheading="JPG" href="https://opensource.adobe.com/spectrum-web-components" target="_blank">
  <img slot="cover-photo" src="https://picsum.photos/200/300" alt="Demo Image" />
</sp-card>

#### Cover Photo

#Section titled Cover Photo

Use `slot="cover-photo"` on an image to set it as the card's cover photo.

<sp-card heading="Card Heading" subheading="JPG Photo">
  <img slot="cover-photo" src="https://picsum.photos/200/300" alt="Demo Image" />
  <div slot="footer">Footer</div>
</sp-card>

#### Preview Image

#Section titled Preview Image

Use `slot="preview"` on an image to set it as the card's preview image.

<sp-card heading="Card Title" subheading="JPG">
  <img slot="preview" src="https://picsum.photos/200/300" alt="Demo Image" />
  <div slot="footer">Footer</div>
</sp-card>

#### No Preview Image

#Section titled No Preview Image

Cards with no preview image can contain a heading, a subheading, and a footer.

<sp-card heading="Card Title" subheading="No Preview Image">
  <div slot="footer">Footer</div>
</sp-card>

#### Actions

#Section titled Actions

Cards can be supplied an `actions` via a names slot.

<sp-card heading="Card Heading" subheading="JPG Photo">
  <img slot="cover-photo" src="https://picsum.photos/200/300" alt="Demo Image" />
  <div slot="footer">Footer</div>
  <sp-action-menu label="More Actions" slot="actions" placement="bottom-end" quiet >
    <sp-menu-item>Deselect</sp-menu-item>
    <sp-menu-item>Select Inverse</sp-menu-item>
    <sp-menu-item>Feather...</sp-menu-item>
    <sp-menu-item>Select and Mask...</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Save Selection</sp-menu-item>
    <sp-menu-item disabled>Make Work Path</sp-menu-item>
  </sp-action-menu>
</sp-card>

### Options

#Section titled Options

#### Horizontal

#Section titled Horizontal

Cards with a `horizontal` attribute can contain a heading, a subheading, a cover photo, and a description.

<sp-card horizontal heading="Card Heading" subheading="JPG Photo">
  <img alt="" slot="cover-photo" src="https://picsum.photos/200/250" />
  <div slot="description">10/15/18</div>
</sp-card>

#### Variant

#Section titled Variant

There are multiple card variants to choose from in Spectrum. The `variant` attribute controls the main variant of the card.

Cards with `variant="quiet"` can contain a heading, a subheading, a cover photo, a description, and a footer. Quiet cards will also accept `actions` via a named slot.

<sp-card variant="quiet" heading="Card Heading" subheading="JPG Photo">
  <img alt="" slot="preview" src="https://picsum.photos/200/350" />
  <div slot="description">10/15/18</div>
  <sp-action-menu label="More Actions" slot="actions" placement="bottom-end" quiet >
    <sp-menu-item>Deselect</sp-menu-item>
    <sp-menu-item>Select Inverse</sp-menu-item>
    <sp-menu-item>Feather...</sp-menu-item>
    <sp-menu-item>Select and Mask...</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Save Selection</sp-menu-item>
    <sp-menu-item disabled>Make Work Path</sp-menu-item>
  </sp-action-menu>
</sp-card>
Cards with `variant="gallery"` can contain a heading, a subheading, an image preview, a description, and a footer.

<sp-card variant="gallery" heading="Card Heading" subheading="JPG Photo">
  <img alt="" slot="preview" src="https://picsum.photos/532/192" />
  <div slot="description">10/15/18</div>
  <div slot="footer">Footer</div>
</sp-card>

#### Asset

#Section titled Asset

When leveraging the `asset` attribute, a card can be declared as representing a `file` or a `folder`:

<sp-card heading="Card Heading" subheading="JPG Photo" asset="file">
  <div slot="heading">File Name</div>
  <div slot="description">10/15/18</div>
  <div slot="footer">Footer</div>
</sp-card>
<sp-card subheading="JPG Photo" asset="folder">
  <div slot="heading">Folder Name</div>
  <div slot="description">10/15/18</div>
  <div slot="footer">Footer</div>
</sp-card>

#### Toggles

#Section titled Toggles

When the `toggles` boolean attribute set to `true`, the card can be toggled between selected and unselected states. A checkbox will be rendered on hover, focus within, and when the card is selected.

<sp-card toggles variant="quiet" heading="Card Heading" subheading="JPG Photo">
  <img alt="" slot="preview" src="https://picsum.photos/200/350" />
  <div slot="description">10/15/18</div>
</sp-card>

### Accessibility

#Section titled Accessibility

#### Be concise

#Section titled Be concise

Heading text should be no more than 5-7 words. If the card has an `href`, the heading is used as a link and should ideally be no more than 3 words. For buttons, 1-2 words.

#### Use descriptive heading, link, and button text

#Section titled Use descriptive heading, link, and button text

Be descriptive. Set expectations on what someone will find and where they will go once they interact with a card. Avoid using the same text on more than one interactive element, unless both elements go to the same place.

#### Make the first word in a heading meaningful

#Section titled Make the first word in a heading meaningful

Consider making the first word of links, buttons and headings something an assistive technology user might search for when headings and links are listed alphabetically.

Changelog
---------

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/asset@1.11.2
    *   @spectrum-web-components/divider@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/checkbox@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2
    *   @spectrum-web-components/popover@1.11.2
    *   @spectrum-web-components/styles@1.11.2

1.11.1
------

#Section titled 1.11.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/asset@1.11.1
    *   @spectrum-web-components/divider@1.11.1
    *   @spectrum-web-components/checkbox@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1
    *   @spectrum-web-components/popover@1.11.1
    *   @spectrum-web-components/styles@1.11.1

1.11.0
------

#Section titled 1.11.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`f8bdeec`, `9cb816b`, `7c26e3a`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/styles@1.11.0
    *   @spectrum-web-components/popover@1.11.0
    *   @spectrum-web-components/asset@1.11.0
    *   @spectrum-web-components/divider@1.11.0
    *   @spectrum-web-components/checkbox@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

1.10.0
------

#Section titled 1.10.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/asset@1.10.0
    *   @spectrum-web-components/checkbox@1.10.0
    *   @spectrum-web-components/divider@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/popover@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/styles@1.10.0

1.9.1
-----

#Section titled 1.9.1

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies []: 
    *   @spectrum-web-components/popover@1.9.1
    *   @spectrum-web-components/asset@1.9.1
    *   @spectrum-web-components/checkbox@1.9.1
    *   @spectrum-web-components/divider@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1
    *   @spectrum-web-components/styles@1.9.1

1.9.0
-----

#Section titled 1.9.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`bdf54c1`]: 
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/checkbox@1.9.0
    *   @spectrum-web-components/popover@1.9.0
    *   @spectrum-web-components/asset@1.9.0
    *   @spectrum-web-components/divider@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0
    *   @spectrum-web-components/styles@1.9.0

1.8.0
-----

#Section titled 1.8.0

### Minor Changes

#Section titled Minor Changes

*   #5638`f8da034` Thanks @Rajdeepc! - **Fixed** the card component's CSS by moving `block-size: 100%` from the base `:host` selector to only apply to `gallery` and `quiet` variants

*   #5171`eae4332` Thanks @majornista! - Enhanced the Card component's checkbox functionality with improved screen reader support and keyboard navigation.

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`77bdef6`, `15be17d`, `826a2d5`]: 
    *   @spectrum-web-components/styles@1.8.0
    *   @spectrum-web-components/divider@1.8.0
    *   @spectrum-web-components/popover@1.8.0
    *   @spectrum-web-components/asset@1.8.0
    *   @spectrum-web-components/checkbox@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

1.7.0
-----

#Section titled 1.7.0

### Minor Changes

#Section titled Minor Changes

*   #5521`56f2ff4` Thanks @Rajdeepc! - **Fixed**: On mobile Chrome (both Android and iOS), scrolling on `sp-card` components would inadvertently trigger click events. This was caused by the timing-based click detection (200ms threshold) in the pointer event handling, which could misinterpret quick scrolls as clicks. This issue did not affect Safari on mobile devices.

### Patch Changes

#Section titled Patch Changes

*   #5449`ae9dcf8` Thanks @Rajdeepc! - - **Fixed**: `sp-card` component relies on `sp-popover` for certain toggle interactive behaviors, but this dependency was missing from its dependency tree.

*   Updated dependencies [`1126cf2`]:

    *   @spectrum-web-components/styles@1.7.0
    *   @spectrum-web-components/popover@1.7.0
    *   @spectrum-web-components/asset@1.7.0
    *   @spectrum-web-components/checkbox@1.7.0
    *   @spectrum-web-components/divider@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

1.6.0
-----

#Section titled 1.6.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`f6cebbd`, `9e15a66`, `a9727d2`]: 
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/styles@1.6.0
    *   @spectrum-web-components/asset@1.6.0
    *   @spectrum-web-components/checkbox@1.6.0
    *   @spectrum-web-components/divider@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

1.5.0
-----

#Section titled 1.5.0

### Patch Changes

#Section titled Patch Changes

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`165a904`, `a4de4c7`, `4e06533`, `fa4be70`, `daeb11f`, `6c58f50`, `fa4be70`]:

    *   @spectrum-web-components/asset@1.5.0
    *   @spectrum-web-components/divider@1.5.0
    *   @spectrum-web-components/styles@1.5.0
    *   @spectrum-web-components/checkbox@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

1.4.0
-----

#Section titled 1.4.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`3cca7ea`]: 
    *   @spectrum-web-components/styles@1.4.0
    *   @spectrum-web-components/asset@1.4.0
    *   @spectrum-web-components/checkbox@1.4.0
    *   @spectrum-web-components/divider@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

1.3.0
-----

#Section titled 1.3.0

### Patch Changes

#Section titled Patch Changes

*   Updated dependencies [`468314f`]: 
    *   @spectrum-web-components/checkbox@1.3.0
    *   @spectrum-web-components/asset@1.3.0
    *   @spectrum-web-components/divider@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0
    *   @spectrum-web-components/styles@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

1.2.0 (2025-02-27)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 1.1.2 (2025-02-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 1.1.1 (2025-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

1.1.0 (2025-01-29)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

### 1.0.3 (2024-12-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 1.0.1 (2024-11-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

1.0.0 (2024-10-31)
------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.49.0 (2024-10-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.48.1 (2024-10-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.48.0 (2024-09-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.47.2 (2024-09-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.47.1 (2024-08-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.47.0 (2024-08-20)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.46.0 (2024-08-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.45.0 (2024-07-30)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.44.0 (2024-07-15)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.43.0 (2024-06-11)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.42.5 (2024-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.42.4 (2024-05-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.42.3 (2024-05-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.42.2 (2024-04-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.42.1 (2024-04-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.42.0 (2024-03-19)
-------------------

#Section titled 

### Features

#Section titled Features

*   **asset:** use core tokens (99e76f4)

### 0.41.2 (2024-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.41.1 (2024-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.41.0 (2024-02-13)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.40.5 (2024-02-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.40.4 (2024-01-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.40.3 (2024-01-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.40.2 (2023-12-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.40.1 (2023-12-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.40.0 (2023-11-16)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.39.4 (2023-11-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.39.3 (2023-10-18)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.39.2 (2023-10-13)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update deps graph, update link docs (#3709) (2deb284)

### 0.39.1 (2023-10-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.39.0 (2023-09-25)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.38.0 (2023-09-05)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.37.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.36.0 (2023-08-18)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.35.0 (2023-07-31)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.34.0 (2023-07-11)
-------------------

#Section titled 

### Features

#Section titled Features

*   **card:** use core tokens (9cccd26)

### 0.33.2 (2023-06-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.33.0 (2023-06-08)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.32.0 (2023-06-01)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.31.0 (2023-05-17)
-------------------

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.30.0 (2023-05-03)
-------------------

#Section titled 0.30.0 (2023-05-03)

### Bug Fixes

#Section titled Bug Fixes

*   add Grid pattern (341f493)
*   add likeAnchor API to Card element (5c338fb)
*   **card:** allow for preview or cover-photo (2d2f42b)
*   **card:** correctly apply :focus-visible styling to variants (d7c7539)
*   **card:** create no preview image variant of card instead of no imageless variant at all (7b102b9)
*   **card:** do not transform subheadling text to uppercase (4244390)
*   **card:** include dependencies (18beaf6)
*   **card:** normalize sizing technique to align with future t-shirt size usage (6f05b3b)
*   **card:** removed empty card from documentation/stories (8322894)
*   **card:** stop event propogation on handleselectedchange (0ef95e5)
*   **dialog:** normalize sizing technique to align with future t-shirt size usage (da33797)
*   ensure that all paths to user change of selected trigger a change event (2eee81e)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   match "pointerup" listeners with "pointercancel" for full coverage (7f2ce92)
*   override and clear text-transform: uppercase (dddce4b)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   remove standard variant from image getter (97e4713)
*   stop merging selectors in a way that alters the cascade (369388f)
*   switch to heading/subheading instead of title (d182a0f)
*   tests weren't fully updated (22bf3b1)
*   these selectors didn't actually change (a5ac275)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   add screenshot regression testing to CI (8205dfe)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   allow slotted title for card (aaf7157)
*   **button:** use synthetic button instead of native (49e94bc)
*   **card:** update spectrum css input (18b6dae)
*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)
*   delivery dev mode messages in various packages (62370a1)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   sets action-menu quiet to false by default, fixes #3040 (8414cab)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **styles:** vend CSS literal versions of the typography system (6406c96)
*   update card and tabs to latest spectrum-css (55b8d67)
*   update lit-* dependencies, wip (377f3c8)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

### Reverts

#Section titled Reverts

*   Revert "chore: release new versions" (a6d655d)

### BREAKING CHANGES

#Section titled BREAKING CHANGES

*   renamed title/subtitle attributes and slot.

### 0.14.2 (2023-04-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.14.1 (2023-04-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.14.0 (2023-03-22)
-------------------

#Section titled 

### Features

#Section titled Features

*   sets action-menu quiet to false by default, fixes #3040 (8414cab)

### 0.13.9 (2023-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.8 (2023-02-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.7 (2023-02-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.6 (2023-01-23)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.5 (2023-01-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.4 (2022-12-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.3 (2022-11-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.2 (2022-11-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.13.1 (2022-10-28)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.13.0 (2022-10-17)
-------------------

#Section titled 

### Features

#Section titled Features

*   update card and tabs to latest spectrum-css (55b8d67)

### 0.12.3 (2022-10-10)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   match "pointerup" listeners with "pointercancel" for full coverage (7f2ce92)

### 0.12.2 (2022-09-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.12.1 (2022-08-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.12.0 (2022-08-09)
-------------------

#Section titled 

### Features

#Section titled Features

*   include all Dev Mode files in side effects (f70817c)

0.11.0 (2022-08-04)
-------------------

#Section titled 

### Features

#Section titled Features

*   delivery dev mode messages in various packages (62370a1)

### 0.10.13 (2022-07-18)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **card:** stop event propogation on handleselectedchange (0ef95e5)

### 0.10.12 (2022-06-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.11 (2022-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.10 (2022-05-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.9 (2022-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.8 (2022-04-21)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.7 (2022-03-30)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.6 (2022-03-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.5 (2022-03-04)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add Grid pattern (341f493)

### 0.10.4 (2022-02-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.3 (2022-01-26)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.2 (2022-01-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.10.1 (2021-12-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.10.0 (2021-11-08)
-------------------

#Section titled 

### Features

#Section titled Features

*   update lit-* dependencies, wip (377f3c8)

### 0.9.1 (2021-11-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.9.0 (2021-11-02)
------------------

#Section titled 

### Features

#Section titled Features

*   adopt DNA@7 base Spectrum CSS (e08cafd)

### 0.8.18 (2021-10-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   add likeAnchor API to Card element (5c338fb)

### 0.8.17 (2021-09-20)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.16 (2021-09-13)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.15 (2021-08-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.14 (2021-08-17)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **card:** normalize sizing technique to align with future t-shirt size usage (6f05b3b)
*   **dialog:** normalize sizing technique to align with future t-shirt size usage (da33797)

### 0.8.13 (2021-08-03)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.12 (2021-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.11 (2021-07-01)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.10 (2021-06-16)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.9 (2021-06-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.8 (2021-05-24)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.7 (2021-05-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.6 (2021-04-15)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.5 (2021-04-09)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.4 (2021-03-29)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.3 (2021-03-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.8.2 (2021-03-22)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   remove `<sp-menu>` usage where deprecated (387db3b)

### 0.8.1 (2021-03-05)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.8.0 (2021-03-04)
------------------

#Section titled 

### Features

#Section titled Features

*   use latest exports specification (a7ecf4b)

### 0.7.3 (2021-02-11)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update to latest spectrum-css packages (a5ca19f)

### 0.7.2 (2021-02-02)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.7.1 (2021-01-28)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **card:** create no preview image variant of card instead of no imageless variant at all (7b102b9)
*   remove standard variant from image getter (97e4713)
*   **card:** allow for preview or cover-photo (2d2f42b)
*   **card:** removed empty card from documentation/stories (8322894)

0.7.0 (2021-01-21)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   ensure that all paths to user change of selected trigger a change event (2eee81e)
*   include the "types" entry in package.json files (b432f59)
*   override and clear text-transform: uppercase (dddce4b)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   **card:** do not transform subheadling text to uppercase (4244390)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   **button:** use synthetic button instead of native (49e94bc)
*   **card:** update spectrum css input (18b6dae)
*   **styles:** vend CSS literal versions of the typography system (6406c96)

0.6.0 (2021-01-13)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include the "types" entry in package.json files (b432f59)
*   override and clear text-transform: uppercase (dddce4b)
*   stop merging selectors in a way that alters the cascade (369388f)
*   switch to heading/subheading instead of title (d182a0f)
*   tests weren't fully updated (22bf3b1)
*   these selectors didn't actually change (a5ac275)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   **card:** do not transform subheadling text to uppercase (4244390)
*   use latest @spectrum-css/* versions (c35eb86)

### Features

#Section titled Features

*   **button:** use synthetic button instead of native (49e94bc)
*   **card:** update spectrum css input (18b6dae)
*   **styles:** vend CSS literal versions of the typography system (6406c96)

### BREAKING CHANGES

#Section titled BREAKING CHANGES

*   renamed title/subtitle attributes and slot.

1.0.0 (2020-11-20)
------------------

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   switch to heading/subheading instead of title (d182a0f)
*   tests weren't fully updated (22bf3b1)
*   these selectors didn't actually change (a5ac275)

### BREAKING CHANGES

#Section titled BREAKING CHANGES

*   renamed title/subtitle attributes and slot.

### 0.5.4 (2020-10-12)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.5.3 (2020-10-12)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **card:** include dependencies (18beaf6)
*   include default export in the "exports" fields (f32407d)

### 0.5.2 (2020-09-25)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   update side effect listings (8160d3a)

### 0.5.1 (2020-09-14)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.5.0 (2020-08-31)
------------------

#Section titled 

### Features

#Section titled Features

*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)

### 0.4.3 (2020-08-19)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.4.2 (2020-07-27)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.4.1 (2020-07-22)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.4.0 (2020-07-17)
------------------

#Section titled 

### Features

#Section titled Features

*   leverage "exports" field in package.json (321abd7)

### 0.3.5 (2020-06-08)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.3.4 (2020-05-08)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   **card:** correctly apply :focus-visible styling to variants (d7c7539)

### 0.3.3 (2020-04-16)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   use "sideEffects" listing in package.json (7271614)

### 0.3.2 (2020-04-07)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.3.1 (2020-03-11)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

0.3.0 (2020-02-05)
------------------

#Section titled 

### Features

#Section titled Features

*   allow slotted title for card (aaf7157)

### 0.2.3 (2020-01-30)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.2.2 (2020-01-06)

#Section titled 

**Note:** Version bump only for package @spectrum-web-components/card

### 0.2.1 (2019-11-27)

#Section titled 

### Bug Fixes

#Section titled Bug Fixes

*   include "type" in package.json, generate custom-elements.json (1a8d716)

0.2.0 (2019-11-19)
------------------

#Section titled 

### Features

#Section titled Features

*   add screenshot regression testing to CI (8205dfe)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

### 0.1.4 (2019-10-14)

#Section titled 

### Performance Improvements

#Section titled Performance Improvements

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

0.1.3 (2019-10-03)
------------------

#Section titled 0.1.3 (2019-10-03)

**Note:** Version bump only for package @spectrum-web-components/card

API
---

### Attributes and Properties

#Section titled Attributes and Properties

 Property  Attribute  Type  Default  Description `asset``asset``'file' | 'folder' | undefined``download``download``string | undefined` Causes the browser to treat the linked URL as a download. `focused``focused``boolean``false``heading``heading``string``''``horizontal``horizontal``boolean``false``href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `selected``selected``boolean``subheading``subheading``string``''``target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `toggles``toggles``boolean``false` Indicates whether the card can be toggled between selected and unselected states. `value``value``string``''``variant``variant``'standard' | 'gallery' | 'quiet'``'standard'`

### Slots

#Section titled Slots

 Name  Description `actions` an `sp-action-menu` element outlining actions to take on the represened object `cover-photo` This is the cover photo for Default and Quiet Cards `description` A description of the card `footer` Footer text `heading` HTML content to be listed as the heading `preview` This is the preview image for Gallery Cards `subheading` HTML content to be listed as the subheading 

### Events

#Section titled Events

 Name  Type  Description `change``Event``Announces a change in the `selected` property of a card``click``Event`

[Getting started](https://opensource.adobe.com/spectrum-web-components/getting-started)[Dev mode](https://opensource.adobe.com/spectrum-web-components/dev-mode)[Registry conflicts](https://opensource.adobe.com/spectrum-web-components/registry-conflicts)Components[Accordion](https://opensource.adobe.com/spectrum-web-components/components/accordion/)[Accordion Item](https://opensource.adobe.com/spectrum-web-components/components/accordion-item/)[Action Bar](https://opensource.adobe.com/spectrum-web-components/components/action-bar/)[Action Button](https://opensource.adobe.com/spectrum-web-components/components/action-button/)[Action Group](https://opensource.adobe.com/spectrum-web-components/components/action-group/)[Action Menu](https://opensource.adobe.com/spectrum-web-components/components/action-menu/)[Alert Banner](https://opensource.adobe.com/spectrum-web-components/components/alert-banner/)[Alert Dialog](https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/)[Asset](https://opensource.adobe.com/spectrum-web-components/components/asset/)[Avatar](https://opensource.adobe.com/spectrum-web-components/components/avatar/)[Badge](https://opensource.adobe.com/spectrum-web-components/components/badge/)[Breadcrumbs](https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/)[Breadcrumb Item](https://opensource.adobe.com/spectrum-web-components/components/breadcrumb-item/)[Button](https://opensource.adobe.com/spectrum-web-components/components/button/)[Clear Button](https://opensource.adobe.com/spectrum-web-components/components/clear-button/)[Close Button](https://opensource.adobe.com/spectrum-web-components/components/close-button/)[Button Group](https://opensource.adobe.com/spectrum-web-components/components/button-group/)[Card](https://opensource.adobe.com/spectrum-web-components/components/card/)[Checkbox](https://opensource.adobe.com/spectrum-web-components/components/checkbox/)[Coachmark](https://opensource.adobe.com/spectrum-web-components/components/coachmark/)[Coach Indicator](https://opensource.adobe.com/spectrum-web-components/components/coach-indicator/)[Color Area](https://opensource.adobe.com/spectrum-web-components/components/color-area/)[Color Field](https://opensource.adobe.com/spectrum-web-components/components/color-field/)[Color Handle](https://opensource.adobe.com/spectrum-web-components/components/color-handle/)[Color Loupe](https://opensource.adobe.com/spectrum-web-components/components/color-loupe/)[Color Slider](https://opensource.adobe.com/spectrum-web-components/components/color-slider/)[Color Wheel](https://opensource.adobe.com/spectrum-web-components/components/color-wheel/)[Combobox](https://opensource.adobe.com/spectrum-web-components/components/combobox/)[Contextual Help](https://opensource.adobe.com/spectrum-web-components/components/contextual-help/)[Dialog](https://opensource.adobe.com/spectrum-web-components/components/dialog/)[Dialog Base](https://opensource.adobe.com/spectrum-web-components/components/dialog-base/)[Dialog Wrapper](https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/)[Divider](https://opensource.adobe.com/spectrum-web-components/components/divider/)[Dropzone](https://opensource.adobe.com/spectrum-web-components/components/dropzone/)[Field Group](https://opensource.adobe.com/spectrum-web-components/components/field-group/)[Field Label](https://opensource.adobe.com/spectrum-web-components/components/field-label/)[Help Text](https://opensource.adobe.com/spectrum-web-components/components/help-text/)[Help Text Mixin](https://opensource.adobe.com/spectrum-web-components/components/help-text-mixin/)[Icon](https://opensource.adobe.com/spectrum-web-components/components/icon/)[Icons](https://opensource.adobe.com/spectrum-web-components/components/icons/)[Icons UI](https://opensource.adobe.com/spectrum-web-components/components/icons-ui/)[Icons Workflow](https://opensource.adobe.com/spectrum-web-components/components/icons-workflow/)[Iconset](https://opensource.adobe.com/spectrum-web-components/components/iconset/)[Illustrated Message](https://opensource.adobe.com/spectrum-web-components/components/illustrated-message/)[Infield Button](https://opensource.adobe.com/spectrum-web-components/components/infield-button/)[Link](https://opensource.adobe.com/spectrum-web-components/components/link/)[Menu](https://opensource.adobe.com/spectrum-web-components/components/menu/)[Menu Group](https://opensource.adobe.com/spectrum-web-components/components/menu-group/)[Menu Item](https://opensource.adobe.com/spectrum-web-components/components/menu-item/)[Meter](https://opensource.adobe.com/spectrum-web-components/components/meter/)[Number Field](https://opensource.adobe.com/spectrum-web-components/components/number-field/)[Overlay](https://opensource.adobe.com/spectrum-web-components/components/overlay/)[Imperative Api](https://opensource.adobe.com/spectrum-web-components/components/imperative-api/)[Overlay Trigger](https://opensource.adobe.com/spectrum-web-components/components/overlay-trigger/)[Slottable Request](https://opensource.adobe.com/spectrum-web-components/components/slottable-request/)[Trigger Directive](https://opensource.adobe.com/spectrum-web-components/components/trigger-directive/)[Picker](https://opensource.adobe.com/spectrum-web-components/components/picker/)[Picker Button](https://opensource.adobe.com/spectrum-web-components/components/picker-button/)[Popover](https://opensource.adobe.com/spectrum-web-components/components/popover/)[Progress Bar](https://opensource.adobe.com/spectrum-web-components/components/progress-bar/)[Progress Circle](https://opensource.adobe.com/spectrum-web-components/components/progress-circle/)[Radio](https://opensource.adobe.com/spectrum-web-components/components/radio/)[Radio Group](https://opensource.adobe.com/spectrum-web-components/components/radio-group/)[Search](https://opensource.adobe.com/spectrum-web-components/components/search/)[Sidenav](https://opensource.adobe.com/spectrum-web-components/components/sidenav/)[Sidenav Heading](https://opensource.adobe.com/spectrum-web-components/components/sidenav-heading/)[Sidenav Item](https://opensource.adobe.com/spectrum-web-components/components/sidenav-item/)[Slider](https://opensource.adobe.com/spectrum-web-components/components/slider/)[Slider Handle](https://opensource.adobe.com/spectrum-web-components/components/slider-handle/)[Split View](https://opensource.adobe.com/spectrum-web-components/components/split-view/)[Status Light](https://opensource.adobe.com/spectrum-web-components/components/status-light/)[Swatch](https://opensource.adobe.com/spectrum-web-components/components/swatch/)[Swatch Group](https://opensource.adobe.com/spectrum-web-components/components/swatch-group/)[Switch](https://opensource.adobe.com/spectrum-web-components/components/switch/)[Table](https://opensource.adobe.com/spectrum-web-components/components/table/)[Tabs](https://opensource.adobe.com/spectrum-web-components/components/tabs/)[Tab Panel](https://opensource.adobe.com/spectrum-web-components/components/tab-panel/)[Tab](https://opensource.adobe.com/spectrum-web-components/components/tab/)[Tabs Overflow](https://opensource.adobe.com/spectrum-web-components/components/tabs-overflow/)[Tags](https://opensource.adobe.com/spectrum-web-components/components/tags/)[Tag](https://opensource.adobe.com/spectrum-web-components/components/tag/)[Textfield](https://opensource.adobe.com/spectrum-web-components/components/textfield/)[Textarea](https://opensource.adobe.com/spectrum-web-components/components/textarea/)[Thumbnail](https://opensource.adobe.com/spectrum-web-components/components/thumbnail/)[Toast](https://opensource.adobe.com/spectrum-web-components/components/toast/)[Tooltip](https://opensource.adobe.com/spectrum-web-components/components/tooltip/)[Tooltip Directive](https://opensource.adobe.com/spectrum-web-components/components/tooltip-directive/)[Top Nav](https://opensource.adobe.com/spectrum-web-components/components/top-nav/)[Top Nav Item](https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/)[Tray](https://opensource.adobe.com/spectrum-web-components/components/tray/)[Underlay](https://opensource.adobe.com/spectrum-web-components/components/underlay/)Tools[Base](https://opensource.adobe.com/spectrum-web-components/tools/base/)[Bundle](https://opensource.adobe.com/spectrum-web-components/tools/bundle/)[Grid](https://opensource.adobe.com/spectrum-web-components/tools/grid/)[Opacity Checkerboard](https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/)[Reactive Controllers](https://opensource.adobe.com/spectrum-web-components/tools/reactive-controllers/)[Color Controller](https://opensource.adobe.com/spectrum-web-components/tools/color-controller/)[Dependency Manager](https://opensource.adobe.com/spectrum-web-components/tools/dependency-manager/)[Element Resolution](https://opensource.adobe.com/spectrum-web-components/tools/element-resolution/)[Language Resolution](https://opensource.adobe.com/spectrum-web-components/tools/language-resolution/)[Match Media](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)[Pending State](https://opensource.adobe.com/spectrum-web-components/tools/pending-state/)[Roving Tab Index](https://opensource.adobe.com/spectrum-web-components/tools/roving-tab-index/)[System Context Resolution](https://opensource.adobe.com/spectrum-web-components/tools/system-context-resolution/)[Shared](https://opensource.adobe.com/spectrum-web-components/tools/shared/)[Styles](https://opensource.adobe.com/spectrum-web-components/tools/styles/)[Theme](https://opensource.adobe.com/spectrum-web-components/tools/theme/)[Core Tokens](https://opensource.adobe.com/spectrum-web-components/tools/core-tokens/)[Truncated](https://opensource.adobe.com/spectrum-web-components/tools/truncated/)Contributing[Developing a Component](https://opensource.adobe.com/spectrum-web-components/guides/adding-component/)[Configuring your project](https://opensource.adobe.com/spectrum-web-components/guides/configuring-openwc/)[Generating a new component](https://opensource.adobe.com/spectrum-web-components/guides/generating-components/)[Styling Components](https://opensource.adobe.com/spectrum-web-components/guides/styling-components/)[Writing Changesets](https://opensource.adobe.com/spectrum-web-components/guides/writing-changesets/)Migration Guides[2024/10/31 (v1.0.0)](https://opensource.adobe.com/spectrum-web-components/migrations/2024-10-31%20(1.0.0)/)[2021/11/8](https://opensource.adobe.com/spectrum-web-components/migrations/2021-8-11/)[2023/8/18](https://opensource.adobe.com/spectrum-web-components/migrations/2023-8-18/)[Deprecation Guide](https://opensource.adobe.com/spectrum-web-components/deprecation)[Using swc-react](https://opensource.adobe.com/spectrum-web-components/using-swc-react)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/card/storybook/index.html)[Storybook](https://opensource.adobe.com/spectrum-web-components/components/card/storybook/index.html)[Spectrum](https://spectrum.adobe.com/)[Spectrum CSS](https://opensource.adobe.com/spectrum-css/)
