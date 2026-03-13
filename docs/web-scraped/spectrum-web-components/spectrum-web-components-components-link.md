# Source: https://opensource.adobe.com/spectrum-web-components/components/link/

Title: Link: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/link/

Markdown Content:
An `<sp-link>` allows users to navigate to a different location. They can be presented in-line inside a paragraph or as a standalone text.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/link?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/link?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/link
Import the side effectful registration of `<sp-link>` via:

import '@spectrum-web-components/link/sp-link.js';
When looking to leverage the `Link` base class as a type and/or for extension purposes, do so via:

import { Link } from '@spectrum-web-components/link';Primary
Primary links are blue and should be used to call attention to the link or for when the blue color won’t feel too overwhelming in the experience.

This is a <sp-link href="#">primary link</sp-link>.Secondary
The secondary variant is the same color as the paragraph text inline of which it appears. Its subdued appearance is optimal for when the primary variant is too overwhelming, such as in blocks of text with several references linked throughout.

This is a <sp-link href="#" variant="secondary">secondary link</sp-link>.Quiet
All links can have a quiet style, which means they don’t have an underline. This style should only be used when the placement and context of the link is explicit enough that a visible underline isn’t necessary. Quiet links are less accessible because users may not recognise them as links. Use only when context and placement make their purpose unmistakable, and avoid using quiet links for critical navigation.

<p>This is a <sp-link quiet href="#">quiet primary link</sp-link>.</p>
<p>This is a <sp-link quiet variant="secondary" href="#">quiet secondary link</sp-link>.</p>
<div style="background-color: var(--spectrum-docs-static-white-background-color); padding: 15px 20px; display: inline-block;">
    <p style="color: var(--spectrum-white);">
        This is a
        <sp-link static-color="white" quiet href="#">quiet link</sp-link>
        over a background.
    </p>
</div>
When a link needs to be placed on top of a colored background or a visual it may be appropriate to ship it with a static color, regardless of the theme settings with which it is delivered. Leverage the `static-color` attribute with its `white` or `black` values to ensure the delivery is the same in all contexts.

White<div style="background-color: var(--spectrum-docs-static-white-background-color); padding: 15px 20px; display: inline-block;">
  <p style="color: var(--spectrum-white);">
    This
    <sp-link static-color="white" href="#">link</sp-link>
    is over a background.
  </p>
</div>Black<div style="background-color: var(--spectrum-docs-static-black-background-color); padding: 15px 20px; display: inline-block;">
  <p style="color: var(--spectrum-black);">
    This
    <sp-link static-color="black" href="#">link</sp-link>
    is over a background.
  </p>
</div>
Disabled links are blue, unfocusable, unclickable and should not propagate any events.

This is a <sp-link disabled href="#">disabled link</sp-link>.
The download attribute on an `<a>` tag prompts a user to download a link as opposed to navigating to it. This attribute has been carried forward to `<sp-link>` to function the same.

While it functions this way without assigning a value, actually assigning the value allows custom naming of the download link in accordance with standard `<a>`rules defined by the browser.

This is a <sp-link download="myfile.txt" href="#">download link</sp-link>.
*   Use links in body copy and not in titles. For a larger call to action, consider using a button instead.
*   Identify the target of each link directly in the link text to communicate context and set clear expectations about where the link will go.
*   Be mindful of link placement and language, and create experiences that are inclusive of users navigating with screen readers, who may navigate links without their surrounding language.
*   It’s more accessible and inclusive to write link text as unique descriptions of the navigational target or function.
*   Implement skip links to improve navigation for keyboard and screen reader users when necessary, especially when the page has many sections and lengthy scroll.
*   For links that open in a new tab, add `target="_blank"`, `rel="noopener noreferrer"` and a UI icon to the link.
*   Add `aria-label` or `aria-labelledby` to links for screen readers who need additional context. Links can be more concise to lessen visible noise, but adding these attributes can help make the purpose of the link more clear.
*   Ensure strong color contrast between the link and its background. For users with low vision,consider using 7:1 ratio for critical links and 21:1 ratio for severe vision impairments.

*   `Tab`: Move focus to the next focusable element.
*   `Enter`: Activate the link.
*   `Shift + F10` (Optional): Open the context menu for the link.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1

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

*   #5695`aa411d0` Thanks @TiffanyAltieri! - **Fixed** quiet variant links not showing keyboard focus state in Safari. Links with the `quiet` attribute now properly display focus indicators when navigating with keyboard, improving accessibility for keyboard users.

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

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/link

*   remove deprecated 'static' references (#4818)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   **link:** added feature to stop click propagation for disabled link (#4251) (64f26a5)

*   **link:** added feature to stop click propagation for disabled link (#4251) (64f26a5)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   **shared:** update and expand attribute coverage in likeAnchor (5cb5f1d)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   add the missing quiet property to Link component (867ea43)
*   apply Focuable styles in class extensions (38f7afd)
*   correct @element jsDoc listing across library (c97a632)
*   expand sized functionality to support no default and returning to default values (acf3cfb)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   **link:** correct custom CSS processing configuration (2a24d5a)
*   **link:** correct white space in template/docs site (a48bd06)
*   **link:** correct white space management (a7a63dc)
*   **link:** process Spectrum CSS without overwriting specificity (9eb3d5c)
*   **link:** support "secondary" variant (3808b96)
*   **link:** test inner anchor attribute by accessing via focusElement (f4e97a1)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   review deque accessibility testing of docs site (31f43aa)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   leverage latest Spectrum button API (9caf2f6)
*   **link:** add download attribute to `<sp-link>` (fb02104)
*   **link:** add download attribute to `<sp-link>` (fefb28e)
*   **link:** add download attribute to `<sp-link>` (16894ba)
*   **link:** add download attribute to `<sp-link>` (0763504)
*   **link:** support rel attribute (df4b5a8)
*   **link:** update spectrum css input (e8cd359)
*   **link:** use core tokens (510173b)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)
*   use SixedMixin to manage "size" property (8819821)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   add the missing quiet property to Link component (867ea43)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   **link:** use core tokens (510173b)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   leverage latest Spectrum button API (9caf2f6)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/link

*   **link:** support "secondary" variant (3808b96)

**Note:** Version bump only for package @spectrum-web-components/link

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)

*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   use latest exports specification (a7ecf4b)

*   expand sized functionality to support no default and returning to default values (acf3cfb)
*   update to latest spectrum-css packages (a5ca19f)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **link:** update spectrum css input (e8cd359)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **link:** update spectrum css input (e8cd359)

**Note:** Version bump only for package @spectrum-web-components/link

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   **link:** test inner anchor attribute by accessing via focusElement (f4e97a1)

*   **link:** support rel attribute (df4b5a8)

**Note:** Version bump only for package @spectrum-web-components/link

*   review deque accessibility testing of docs site (31f43aa)

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/link

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/link

*   **link:** correct white space in template/docs site (a48bd06)

*   **link:** add download attribute to `<sp-link>` (fb02104)
*   **link:** add download attribute to `<sp-link>` (fefb28e)
*   **link:** add download attribute to `<sp-link>` (16894ba)
*   **link:** add download attribute to `<sp-link>` (0763504)

*   **link:** correct custom CSS processing configuration (2a24d5a)
*   **link:** process Spectrum CSS without overwriting specificity (9eb3d5c)

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

**Note:** Version bump only for package @spectrum-web-components/link

*   **link:** correct white space management (a7a63dc)

*   apply Focuable styles in class extensions (38f7afd)

**Note:** Version bump only for package @spectrum-web-components/link

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/link

Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `quiet``quiet``boolean``false` Uses quiet styles or not `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `staticColor``static-color``'black' | 'white' | undefined``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `variant``variant``'secondary' | undefined`
