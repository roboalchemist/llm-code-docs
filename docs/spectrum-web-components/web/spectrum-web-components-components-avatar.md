# Source: https://opensource.adobe.com/spectrum-web-components/components/avatar/

Title: Avatar: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/avatar/

Markdown Content:
An `<sp-avatar>` is a thumbnail representation of an entity, such as a user or an organization. Avatars can have a defined image, which is usually uploaded by a user.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/avatar?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/avatar?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/avatar
Import the side effectful registration of `<sp-avatar>` via:

import '@spectrum-web-components/avatar/sp-avatar.js';
When looking to leverage the `Avatar` base class as a type and/or for extension purposes, do so via:

import { Avatar } from '@spectrum-web-components/avatar';
Avatar sizes scale exponentially, based on the Spectrum type scale. These range from `size-50` to `size-700`. An avatar can also be customized to fit appropriately for your context. The default size is `size-100`.

50<sp-avatar size="50" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>75<sp-avatar size="75" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>100<sp-avatar size="100" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>200<sp-avatar size="200" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>300<sp-avatar size="300" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>400<sp-avatar size="400" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>500<sp-avatar size="500" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>600<sp-avatar size="600" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>700<sp-avatar size="700" label="Demo User" src="https://picsum.photos/500/500"></sp-avatar>
Use branded generic avatars when a user has not set their avatar image. These images are designed to be abstracted from all genders, locales, and cultures.

An avatar in a disabled state shows that an avatar exists, but is not available or a user is not active in that circumstance. This can be used to maintain layout continuity and communicate that an avatar may become available or active later.

The `<sp-avatar>` component requires proper accessibility attributes to ensure screen readers can appropriately handle the avatar image.

The `label` attribute of the `<sp-avatar>` will be passed into the `<img>` element as the `alt` attribute for use in defining a textual representation of the image displayed. This is the recommended approach for avatars that convey meaningful information.

<sp-avatar label="John Doe" src="https://picsum.photos/500/500"></sp-avatar>
When an avatar is purely decorative and does not convey meaningful information, use the `is-decorative` attribute to mark it as decorative. This will hide the avatar from screen readers with `alt=""` and `aria-hidden="true"`.

<sp-avatar is-decorative src="https://picsum.photos/500/500"></sp-avatar>
When an avatar has an `href` attribute, it becomes a link and requires an accessible name. Provide a `label` attribute to give the link meaningful text for screen readers.

<sp-avatar label="View John Doe's profile" src="https://picsum.photos/500/500" href="https://adobe.com"></sp-avatar>
**Note**: Decorative avatars should typically not be interactive links. If you need a decorative avatar with a link, you must provide a `label` attribute for accessibility compliance.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1

*   #5961`0c43e2e` Thanks @blunteshwar! - **Added**: `is-decorative` attribute to `<sp-avatar>` to allow developers to explicitly mark avatars as decorative. When set, the avatar is hidden from screen readers with `alt=""` and `aria-hidden="true"`.

**Fixed**: Fixed accessibility violation where `<sp-avatar>` rendered an underlying `img` without any `alt` attribute when no `label` was provided. The component now defaults to `alt=""` when neither `label` nor `is-decorative` is provided, and logs a dev mode warning to help developers catch missing accessibility attributes.

*   Updated dependencies [`f8bdeec`, `9cb816b`]:

    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   **avatar:** ensure there is ALWAYS a focusElement (c1c8644)
*   correct @element jsDoc listing across library (c97a632)
*   ensure browser understandable extensions (f4e59f7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   add screenshot regression testing to CI (8205dfe)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **avatar:** add avatar component (a6882b4)
*   **avatar:** update spectrum css input (0a6f35a)
*   **avatar:** use core tokens (6937e68)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   **avatar:** ensure there is ALWAYS a focusElement (c1c8644)

*   **avatar:** use core tokens (6937e68)

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/avatar

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/avatar

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **avatar:** update spectrum css input (0a6f35a)

*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **avatar:** update spectrum css input (0a6f35a)

**Note:** Version bump only for package @spectrum-web-components/avatar

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/avatar

*   ensure browser understandable extensions (f4e59f7)

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/avatar

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

**Note:** Version bump only for package @spectrum-web-components/avatar

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   add screenshot regression testing to CI (8205dfe)

*   **avatar:** add avatar component (a6882b4)

Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `isDecorative``is-decorative``boolean``false` When true, marks the avatar as decorative and hides it from screen readers. The underlying img will have an empty alt attribute (alt=""). `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `size``size``AvatarSize``src``src``string``''``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>).
