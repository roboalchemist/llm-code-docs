# Source: https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/

Title: Breadcrumbs: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/breadcrumbs/

Markdown Content:
An `<sp-breadcrumbs>` shows hierarchy and navigational context for a user's location within an app. The `<sp-breadcrumbs>` component defines its list of items using child `<sp-breadcrumb-item>` elements placed in its default slot.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/breadcrumbs?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/breadcrumbs?style=for-the-badge)

yarn add @spectrum-web-components/breadcrumbs
Import the side effectful registration of `<sp-breadcrumbs>` and `<sp-breadcrumb-item>` via:

import '@spectrum-web-components/breadcrumbs/sp-breadcrumbs.js';
import '@spectrum-web-components/breadcrumbs/sp-breadcrumb-item.js';
When looking to leverage the `Breadcrumbs` or `BreadcrumbItem` base class as a type and/or for extension purposes, do so via:

import {
  Breadcrumbs,
  BreadcrumbItem,
} from '@spectrum-web-components/breadcrumbs';
Breadcrumbs consist of several key parts:

*   A breadcrumbs list, usually consisting of multiple breadcrumb items, with a separator between each item.
*   A breadcrumbs title at the end of the list displaying the current location within the hierarchy.
*   A truncation menu may also appear, which displays all options within a breadcrumb. Within the menu, items are listed with the hierarchy ordered from the top (root) to the bottom, and will include the currently selected item. Breadcrumbs truncate when there isn't enough space to show all items, or when the list contains five or more levels. Truncation helps manage space and keep the most relevant breadcrumbs visible in deeply nested hierarchies.

<sp-breadcrumbs>
  <sp-breadcrumb-item value="home">Home</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">March 2019 Assets</sp-breadcrumb-item>
</sp-breadcrumbs>
When needing to optimize for functional space of `<sp-breadcrumbs>`, the `compact` property can be used to reduce the height of the breadcrumbs while still maintaining the proper user context.

<sp-breadcrumbs compact>
  <sp-breadcrumb-item value="1">Home</sp-breadcrumb-item>
  <sp-breadcrumb-item value="2">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="3">March 2019 Assets</sp-breadcrumb-item>
</sp-breadcrumbs>
When space becomes limited or the maximum visible items are reached, the component automatically moves the first breadcrumbs into an action menu, adjusting dynamically as the window is resized.

By default, the maximum number of visible breadcrumbs is 4, as recommended by Spectrum Design. You can override this by using the `max-visible-items` attribute. The `<sp-breadcrumbs>` component will always display the action menu and the breadcrumbs title, so the minimum number of visible items is 1.

Default<sp-breadcrumbs>
  <sp-breadcrumb-item value="your_stuff">Your stuff</sp-breadcrumb-item>
  <sp-breadcrumb-item value="team">Team</sp-breadcrumb-item>
  <sp-breadcrumb-item value="in_progress">In progress</sp-breadcrumb-item>
  <sp-breadcrumb-item value="files">Files</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="winter">Winter</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">Assets</sp-breadcrumb-item>
  <sp-breadcrumb-item value="18x24">18x24</sp-breadcrumb-item>
</sp-breadcrumbs>One maximum visible item<sp-breadcrumbs max-visible-items="1">
  <sp-breadcrumb-item value="your_stuff">Your stuff</sp-breadcrumb-item>
  <sp-breadcrumb-item value="team">Team</sp-breadcrumb-item>
  <sp-breadcrumb-item value="in_progress">In progress</sp-breadcrumb-item>
  <sp-breadcrumb-item value="files">Files</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="winter">Winter</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">Assets</sp-breadcrumb-item>
  <sp-breadcrumb-item value="18x24">18x24</sp-breadcrumb-item>
</sp-breadcrumbs>Three maximum visible items<sp-breadcrumbs max-visible-items="3">
  <sp-breadcrumb-item value="your_stuff">Your stuff</sp-breadcrumb-item>
  <sp-breadcrumb-item value="team">Team</sp-breadcrumb-item>
  <sp-breadcrumb-item value="in_progress">In progress</sp-breadcrumb-item>
  <sp-breadcrumb-item value="files">Files</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="winter">Winter</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">Assets</sp-breadcrumb-item>
  <sp-breadcrumb-item value="18x24">18x24</sp-breadcrumb-item>
</sp-breadcrumbs>Resizable
These breadcrumbs are in a resizable container. Reduce the size of the container to see how the maximum number of visible items changes.

<div style="border: 2px solid; padding: 20px; resize: both; overflow: auto;">
  <sp-breadcrumbs max-visible-items="8">
    <sp-breadcrumb-item value="your_stuff">Your stuff</sp-breadcrumb-item>
    <sp-breadcrumb-item value="team">Team</sp-breadcrumb-item>
    <sp-breadcrumb-item value="in_progress">In progress</sp-breadcrumb-item>
    <sp-breadcrumb-item value="files">Files</sp-breadcrumb-item>
    <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
    <sp-breadcrumb-item value="winter">Winter</sp-breadcrumb-item>
    <sp-breadcrumb-item value="assets">Assets</sp-breadcrumb-item>
    <sp-breadcrumb-item value="18x24">18x24</sp-breadcrumb-item>
  </sp-breadcrumbs>
</div>
Use the `root` slot on the first breadcrumb item to always render the first breadcrumb item, even if the breadcrumbs are overflowing. The root will always show in addition to the number of items specified with `max-visible-items`.

Overflowing<sp-breadcrumbs>
  <sp-breadcrumb-item slot="root" value="your_stuff">
    Your stuff
  </sp-breadcrumb-item>
  <sp-breadcrumb-item value="team">Files</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="winter">Winter</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">Assets</sp-breadcrumb-item>
  <sp-breadcrumb-item value="18x24">18x24</sp-breadcrumb-item>
</sp-breadcrumbs>Not overflowing<sp-breadcrumbs>
  <sp-breadcrumb-item slot="root" value="your_stuff">
    Your stuff
  </sp-breadcrumb-item>
  <sp-breadcrumb-item value="files">Files</sp-breadcrumb-item>
  <sp-breadcrumb-item value="trend">Trend</sp-breadcrumb-item>
  <sp-breadcrumb-item value="winter">Winter</sp-breadcrumb-item>
  <sp-breadcrumb-item value="assets">Assets</sp-breadcrumb-item>
</sp-breadcrumbs>
By default, `sp-breadcrumbs` emits a `change` event when clicking on one of its children. However, there may be cases in which clicking should redirect to another page. This can be achieved by using the `href` attribute instead of `value`. Please note that the `change` event will no longer be triggered in this case.

<sp-breadcrumbs>
  <sp-breadcrumb-item href="https://opensource.adobe.com/">
    Home
  </sp-breadcrumb-item>
  <sp-breadcrumb-item href="https://opensource.adobe.com/trend">
    Trend
  </sp-breadcrumb-item>
  <sp-breadcrumb-item href="https://opensource.adobe.com/assets">
    March 2019 Assets
  </sp-breadcrumb-item>
</sp-breadcrumbs>
The component offers the possibility to replace the action menu's icon with a custom one using the `icon` slot. Moreover, for accessibility purposes you can provide an internationalized string for the menu label using the `menu-label` attribute.

<sp-breadcrumbs menu-label="Settings">
  <sp-icon-settings slot="icon"></sp-icon-settings>

  <sp-breadcrumb-item value="displays">Displays</sp-breadcrumb-item>
  <sp-breadcrumb-item value="main">Main display</sp-breadcrumb-item>
  <sp-breadcrumb-item value="brightness">Brightness</sp-breadcrumb-item>
  <sp-breadcrumb-item value="presets">Presets</sp-breadcrumb-item>
  <sp-breadcrumb-item value="1">Preset #1</sp-breadcrumb-item>
</sp-breadcrumbs>
The `<sp-breadcrumbs>` component provides the following accessibility features:

*   Automatically sets `role="navigation"` to ensure proper semantic meaning for assistive technologies
*   Uses semantic markup by rendering a `<ul>` with each `<sp-breadcrumb-item>` assigned `role="listitem"`
*   The last breadcrumb item automatically receives `aria-current="page"` to indicate the current location
*   Sets `aria-label` based on the `label` property, defaulting to `"Breadcrumbs"` if none is provided
*   Each breadcrumb item is keyboard accessible with `tabindex="0"`
*   Provides an accessible action menu with keyboard navigation and screen reader support

*   **Limit breadcrumb depth**: Keep breadcrumbs to 4-5 levels maximum to avoid overwhelming users
*   **Use descriptive labels**: Each breadcrumb item should clearly identify the section or page
*   **Maintain consistent hierarchy**: Always start from the root and progress logically to the current page
*   **Handle overflow gracefully**: Use the `max-visible-items` property to control truncation behavior
*   **Provide meaningful menu labels**: Use the `menu-label` attribute to describe the overflow menu purpose

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/action-menu@1.11.2
    *   @spectrum-web-components/menu@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2
    *   @spectrum-web-components/link@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/action-menu@1.11.1
    *   @spectrum-web-components/link@1.11.1
    *   @spectrum-web-components/menu@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   #5900`283f0fe` Thanks @TarunAdobe! - Added missing dependencies to the package.json files of several components to align with their usage in source code.

*   Updated dependencies [`eac97a2`, `283f0fe`, `2732aad`, `f8bdeec`, `b95e254`, `9cb816b`]:

    *   @spectrum-web-components/menu@1.11.0
    *   @spectrum-web-components/action-menu@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/link@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-menu@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/link@1.10.0
    *   @spectrum-web-components/menu@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/menu@1.9.1
    *   @spectrum-web-components/action-menu@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/link@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies [`4880da4`, `bdf54c1`]: 
    *   @spectrum-web-components/menu@1.9.0
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/action-menu@1.9.0
    *   @spectrum-web-components/link@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies [`f27ab09`, `aa411d0`]: 
    *   @spectrum-web-components/menu@1.8.0
    *   @spectrum-web-components/link@1.8.0
    *   @spectrum-web-components/action-menu@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies [`3aeafdd`]: 
    *   @spectrum-web-components/menu@1.7.0
    *   @spectrum-web-components/action-menu@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/link@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies [`f6cebbd`, `a9727d2`]: 
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/menu@1.6.0
    *   @spectrum-web-components/action-menu@1.6.0
    *   @spectrum-web-components/link@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   #5277`daeb11f` Thanks @renovate! - /Users/cas/Projects/work/spectrum-web-components/yarn.lock

*   Updated dependencies [`86bcd12`, `165a904`, `4c2f908`, `a69accb`]:

    *   @spectrum-web-components/menu@1.5.0
    *   @spectrum-web-components/link@1.5.0
    *   @spectrum-web-components/action-menu@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies [`2a0422e`, `6618422`, `82212f4`]: 
    *   @spectrum-web-components/menu@1.4.0
    *   @spectrum-web-components/action-menu@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/link@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies [`ea38ef0`, `468314f`]: 
    *   @spectrum-web-components/action-menu@1.3.0
    *   @spectrum-web-components/menu@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/link@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **breadcrumbs:** show maxvisibleitems on dynamic updates (#5100) (199f989)

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

*   **breadcrumbs:** trigger change event on breadcrumbs via keyboard (#4769) (e14d082)

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

**Note:** Version bump only for package @spectrum-web-components/breadcrumbs

*   **breadcrumbs:** adjust ref directives imports (#4681) (6e7ba13)

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

Property  Attribute  Type  Default  Description `compact``compact``boolean``false` compact option is useful for reducing the height of the breadcrumbs `label``label``string``''` Accessible name for the Breadcrumbs component `maxVisibleItems``max-visible-items``number``4` Override the maximum number of visible items `menuLabel``menu-label``string``'More items'` Change the default label of the action menu

Name  Description `icon` change the default icon of the action menu `root` Breadcrumb item to always display `default slot` Breadcrumb items

Name  Type  Description `change``Event``Announces the selected breadcrumb item`
