# Source: https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/

Title: Top Nav Item: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/

Markdown Content:
`<sp-top-nav-item>` represents individual navigation links within a `<sp-top-nav>` component. Each item extends standard anchor functionality with Spectrum styling, automatic selection management, and enhanced accessibility features.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/top-nav?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/top-nav?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/top-nav
Import the side effectful registration of `<sp-top-nav>` and `<sp-top-nav-item>` as follows:

import '@spectrum-web-components/top-nav/sp-top-nav.js';
import '@spectrum-web-components/top-nav/sp-top-nav-item.js';
When looking to leverage the `TopNav` or `TopNavItem` base classes as a type and/or for extension purposes, do so via:

import { TopNav, TopNavItem } from '@spectrum-web-components/top-nav';
The `<sp-top-nav-item>` consists of the following parts:

*   **Default slot**: text content for the navigation item
*   **Label**: Sets a visually-hidden `aria-label` on the item

Default<sp-top-nav>
  <sp-top-nav-item href="#pam">Pam</sp-top-nav-item>
  <sp-top-nav-item href="#phyllis">Phyllis</sp-top-nav-item>
  <sp-top-nav-item href="#angela">Angela</sp-top-nav-item>
  <sp-top-nav-item href="#meredith">Meredith</sp-top-nav-item>
</sp-top-nav>Target
The `target` property specifies where to display the linked URL, such as in a new tab (`_blank`), parent frame (`_parent`), same frame (`_self`), or top frame (`_top`).

<sp-top-nav>
  <sp-top-nav-item href="/components/top-nav" target="_blank">
    The Office
  </sp-top-nav-item>
</sp-top-nav>Download
When set, the `download` property causes the browser to treat the linked URL as a downloadable file, rather than navigating to it. It works in conjunction with the `href` attribute to trigger file downloads when the top nav item is clicked.

<sp-top-nav>
  <sp-top-nav-item href="/components/top-nav" download>
    The Office
  </sp-top-nav-item>
</sp-top-nav>Rel
The `rel` property defines the relationship between the current page and the linked URL using space-separated link types (like `nofollow`, `noreferrer`, or `external`). It provides semantic information to browsers and search engines about the nature of the link relationship.

<sp-top-nav>
  <sp-top-nav-item href="/components/top-nav" rel="noreferrer">
    The Office
  </sp-top-nav-item>
</sp-top-nav>Referrer policy
Setting `referrer-policy` will control how much referrer information is sent when following the link, with options ranging from no referrer (`no-referrer`) to full URL (`unsafe-url`).

<sp-top-nav>
  <sp-top-nav-item href="/components/top-nav" referrerpolicy="no-referrer">
    The Office
  </sp-top-nav-item>
</sp-top-nav>Disabled
Adding the `disabled` attribute to a top nav item renders it non-interactive.

<sp-top-nav>
  <sp-top-nav-item href="#pam">Pam</sp-top-nav-item>
  <sp-top-nav-item href="#phyllis">Phyllis</sp-top-nav-item>
  <sp-top-nav-item href="#angela" disabled>Angela</sp-top-nav-item>
  <sp-top-nav-item href="#meredith">Meredith</sp-top-nav-item>
</sp-top-nav>Selected
When a user selects a top nav item, the `selected` property is added.

The `selected` status of a top nav item will populate the parent `<sp-top-nav>` component's `selected` property with the resolved URL.

For demonstration purposes only, the `href` value of the selected top nav item below is hardcoded, as opposed to being a dynamic `href` or a jump link.

<sp-top-nav selected="https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/">
  <sp-top-nav-item href="#michael">Michael</sp-top-nav-item>
  <sp-top-nav-item href="https://opensource.adobe.com/spectrum-web-components/components/top-nav-item/" selected >
    Dwight
  </sp-top-nav-item>
  <sp-top-nav-item href="#kevin">Kevin</sp-top-nav-item>
  <sp-top-nav-item href="#jim">Jim</sp-top-nav-item>
</sp-top-nav>
Selection state is automatically managed by the parent `<sp-top-nav>` component. When selected, the `selected` property is set to `true` and visual styles will update. Only one item can be selected at a time within a navigation group

Clicking anywhere within the item area triggers navigation. Standard anchor behaviors apply to top nav items (new tab with Ctrl/Cmd+click, etc.).

*   Selected items automatically receive `aria-current="page"`
*   The `label` property can optionally set `aria-label` on the anchor element if screen reader text is significantly different from visible text
*   Top nav items renders as anchor elements for accessible screen reader navigation

*   `Tab` and `Shift+Tab` moves focus between items in a natural, logical order
*   `Enter` or `Space` trigger navigation

*   **Use descriptive link text** that makes sense out of context
*   **Use the `label` property sparingly** for additional accessibility information when needed
*   **Avoid icon-only items** without accessible text or labels

Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `selected``selected``boolean``false``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>).

Name  Description `default slot` text label of the Top Nav Item
