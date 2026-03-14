# Source: https://opensource.adobe.com/spectrum-web-components/components/top-nav/

Title: Top Nav: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/top-nav/

Markdown Content:
`<sp-top-nav>` delivers site navigation, particularly for when that navigation will change the majority of the page's content and/or the page's URL when selected. All primary elements of an `<sp-top-nav>` should be directly accessible in the tab order, typically as `<sp-top-nav-item>` elements. There should only ever be one `<sp-top-nav>` on a page.

Refer to the Spectrum Design System documentation for visual design guidelines and the application frame patterns for usage in application contexts.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/top-nav?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/top-nav?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/top-nav
Import the side effectful registration of `<sp-top-nav>` and `<sp-top-nav-item>` as follows:

import '@spectrum-web-components/top-nav/sp-top-nav.js';
import '@spectrum-web-components/top-nav/sp-top-nav-item.js';
When looking to leverage the `TopNav` or `TopNavItem` base classes as a type and/or for extension purposes, do so via:

import { TopNav, TopNavItem } from '@spectrum-web-components/top-nav';
The `<sp-top-nav>` component consists of the following parts:

*   **Container** (`<sp-top-nav>`): The main navigation container component with `role="navigation"` that manages nav items and selection states
*   **Navigation items** (`<sp-top-nav-item>`): Default slot; individual clickable navigation links
*   **Label**: Optional property to set an `aria-label` for the top navigation
*   **Selection indicator**: A visual indicator that animates to the selected item
*   **Divider**: Optional `<div>` divider that acts as the track for the selection indicator

Default<sp-top-nav>
  <sp-top-nav-item href="#">Site Name</sp-top-nav-item>
  <sp-top-nav-item href="#page-1" style="margin-inline-start: auto;">
    Page 1
  </sp-top-nav-item>
  <sp-top-nav-item href="#page-2">Page 2</sp-top-nav-item>
  <sp-top-nav-item href="#page-3">Page 3</sp-top-nav-item>
  <sp-top-nav-item href="#page-4">Page with really long name</sp-top-nav-item>
</sp-top-nav>With action menu integration
Other web components, like action menus and/or buttons, can be included in the `<sp-top-nav>` slots in order to extend functionality.

<sp-top-nav>
  <sp-top-nav-item href="#">Site Name</sp-top-nav-item>
  <sp-top-nav-item href="#page-1" style="margin-inline-start: auto;">
    Page 1
  </sp-top-nav-item>
  <sp-top-nav-item href="#page-2">Page 2</sp-top-nav-item>
  <sp-top-nav-item href="#page-3">Page 3</sp-top-nav-item>
  <sp-action-menu label="Account" placement="bottom-end" style="margin-inline-start: auto;" quiet >
    <sp-menu-item>Account settings</sp-menu-item>
    <sp-menu-item>My profile</sp-menu-item>
    <sp-menu-divider></sp-menu-divider>
    <sp-menu-item>Help</sp-menu-item>
    <sp-menu-item>Sign out</sp-menu-item>
  </sp-action-menu>
</sp-top-nav>With default selection
Setting the `selected` property to a URL that matches a top navigation item's resolved `href` value will render that item selected by default. The `selected` value must match the fully resolved URL, not just the `href` attribute value.

For demonstration purposes only, the `href` value of the selected top nav item is hardcoded, as opposed to being a dynamic `href` or a jump link.

<sp-top-nav selected="https://opensource.adobe.com/spectrum-web-components/components/top-nav/">
  <sp-top-nav-item href="#">Site Name</sp-top-nav-item>
  <sp-top-nav-item href="#home" style="margin-inline-start: auto;">
    Home
  </sp-top-nav-item>
  <sp-top-nav-item href="#services">Services</sp-top-nav-item>
  <sp-top-nav-item href="https://opensource.adobe.com/spectrum-web-components/components/top-nav/" selected >
    About
  </sp-top-nav-item>
</sp-top-nav>Ignoring URL parts for selection
If implementations wish to ignore certain URL parts when matching for selection, the `ignore-url-parts` can be defined with a space-separated list. Currently supported values are `hash` and `search`, which will remove the `#hash` and `?search=value` respectively.

<sp-top-nav ignore-url-parts="search hash">
  <sp-top-nav-item href="/page1">Page 1</sp-top-nav-item>
  <sp-top-nav-item href="/page2">Page 2</sp-top-nav-item>
</sp-top-nav>Quiet variant
The `quiet` property renders the top navigation component without the bottom border.

<sp-top-nav quiet>
  <sp-top-nav-item href="#">Home</sp-top-nav-item>
  <sp-top-nav-item href="/products">Products</sp-top-nav-item>
</sp-top-nav>Small<sp-top-nav size="s">
  <sp-top-nav-item href="#">Site Name</sp-top-nav-item>
  <sp-top-nav-item href="#page-1" style="margin-inline-start: auto;">
    Page 1
  </sp-top-nav-item>
  <sp-top-nav-item href="#page-2">Page 2</sp-top-nav-item>
  <sp-top-nav-item href="#page-3">Page 3</sp-top-nav-item>
  <sp-top-nav-item href="#page-4">Page with really long name</sp-top-nav-item>
</sp-top-nav>Medium<sp-top-nav size="m">
  <sp-top-nav-item href="#">Site Name</sp-top-nav-item>
  <sp-top-nav-item href="#page-1" style="margin-inline-start: auto;">
    Page 1
  </sp-top-nav-item>
  <sp-top-nav-item href="#page-2">Page 2</sp-top-nav-item>
  <sp-top-nav-item href="#page-3">Page 3</sp-top-nav-item>
  <sp-top-nav-item href="#page-4">Page with really long name</sp-top-nav-item>
</sp-top-nav>Large<sp-top-nav size="l">
  <sp-top-nav-item href="#">Site Name</sp-top-nav-item>
  <sp-top-nav-item href="#page-1" style="margin-inline-start: auto;">
    Page 1
  </sp-top-nav-item>
  <sp-top-nav-item href="#page-2">Page 2</sp-top-nav-item>
  <sp-top-nav-item href="#page-3">Page 3</sp-top-nav-item>
  <sp-top-nav-item href="#page-4">Page with really long name</sp-top-nav-item>
</sp-top-nav>Extra large<sp-top-nav size="xl">
  <sp-top-nav-item href="#">Site Name</sp-top-nav-item>
  <sp-top-nav-item href="#page-1" style="margin-inline-start: auto;">
    Page 1
  </sp-top-nav-item>
  <sp-top-nav-item href="#page-2">Page 2</sp-top-nav-item>
  <sp-top-nav-item href="#page-3">Page 3</sp-top-nav-item>
  <sp-top-nav-item href="#page-4">Page with really long name</sp-top-nav-item>
</sp-top-nav>
*   Items are automatically selected based on the current `window.location.href`
*   Use `ignore-url-parts` to ignore hash fragments or search parameters when matching
*   Items can be programmatically selected via the `selected` property
*   The selection indicator automatically resizes based on item content changes
*   Items can be positioned with CSS using CSS via the `style` attribute set on `<sp-top-nav-item>` elements (e.g., `margin-inline-start: auto`)

*   `role="navigation"` is automatically applied to the top nav container
*   The `label` property set on `<sp-top-nav>` will set an `aria-label` for screen readers
*   Selected items receive `aria-current="page"`

*   `Tab` should move focus between all navigation items in a logical tab order
*   `Enter` selects navigation items

*   **Always provide a label** for the navigation container.
*   **Use semantic `href` values** that match actual page URLs for automatic selection.
*   **Provide meaningful text content** for navigation items - avoid icon-only items without labels.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/tabs@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/tabs@1.11.1

*   Updated dependencies [`f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/tabs@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/tabs@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/tabs@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/tabs@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/tabs@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies [`8da375b`]: 
    *   @spectrum-web-components/tabs@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`a9727d2`]: 
    *   @spectrum-web-components/tabs@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`c7efe31`]: 
    *   @spectrum-web-components/tabs@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/tabs@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/tabs@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **shared:** ensure the "updateComplete" in Focusable is stable (885b4a5)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **top-nav:** focus loupe on :focus-visible only (50d6870)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **top-nav:** allow consumers to "ignore-url-parts" or "search" or "hash" (#3923) (83bf70b)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **top-nav:** default to role="navigation", sprout aria-label when "label" applied (bbcea4a)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **tabs,top-nav:** use Core Tokens (c6ba355)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   add tabs sizes to TopNav (159bc89)
*   correct @element jsDoc listing across library (c97a632)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   lint away debugger statements (34a498e)
*   proper overflow rtl support (9b1c9d4)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   **tabs:** add "tablist" part to manage list styles (bbf8074)
*   **tabs:** correct indicator size by scaling from 100px (a3fb68b)
*   **top-nav:** ensure focus state in all contexts (6de83be)
*   **top-nav:** initialize nav with an undefined selection (3473f63)
*   **top-nav:** match indicator management strategy from Tabs (ecc76a0)
*   **top-nav:** minor edits to description, typos (bc2ee48)
*   **top-nav:** prototype top-nav pattern (9708f6f)
*   update indicator animation for loading and content direction (f607f8b)
*   use icons without "size" values (3fc7c91)
*   use typescript@^4.5 for "native" document.fonts typings (a3e4aea)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   sets action-menu quiet to false by default, fixes #3040 (8414cab)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   use latest exports specification (a7ecf4b)

*   reduce render cycles when managing "dir" attribute (7b28309)

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   reduce render cycles when managing "dir" attribute (7b28309)

*   add tabs sizes to TopNav (159bc89)
*   proper overflow rtl support (9b1c9d4)

*   sets action-menu quiet to false by default, fixes #3040 (8414cab)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **tabs:** correct indicator size by scaling from 100px (a3fb68b)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **top-nav:** match indicator management strategy from Tabs (ecc76a0)

*   include all Dev Mode files in side effects (f70817c)

*   **tabs:** add "tablist" part to manage list styles (bbf8074)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **top-nav:** ensure focus state in all contexts (6de83be)

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   use typescript@^4.5 for "native" document.fonts typings (a3e4aea)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   update indicator animation for loading and content direction (f607f8b)

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   lint away debugger statements (34a498e)

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   remove `<sp-menu>` usage where deprecated (387db3b)

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **top-nav:** minor edits to description, typos (bc2ee48)
*   include the "types" entry in package.json files (b432f59)
*   use icons without "size" values (3fc7c91)
*   **top-nav:** initialize nav with an undefined selection (3473f63)

*   include the "types" entry in package.json files (b432f59)
*   use icons without "size" values (3fc7c91)
*   **top-nav:** initialize nav with an undefined selection (3473f63)

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/top-nav

*   **top-nav:** prototype top-nav pattern (9708f6f)

Property  Attribute  Type  Default  Description `ignoreURLParts``ignore-url-parts``string``''` A space separated list of part of the URL to ignore when matching for the "selected" Top Nav Item. Currently supported values are `hash` and `search`, which will remove the `#hash` and `?search=value` respectively. `label``label``string``''``quiet``quiet``boolean``false` The Top Nav is displayed without a border. `selected``selected``string | undefined``selectionIndicatorStyle``selectionIndicatorStyle``noSelectionStyle`

Name  Description `default slot` Nav Items to display as a group
