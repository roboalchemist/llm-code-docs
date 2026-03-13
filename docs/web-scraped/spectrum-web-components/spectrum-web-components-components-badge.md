# Source: https://opensource.adobe.com/spectrum-web-components/components/badge/

Title: Badge: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/badge/

Markdown Content:
`<sp-badge>` elements display a small amount of color-categorized metadata. They're ideal for getting a user's attention.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/badge?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/badge?style=for-the-badge)

yarn add @spectrum-web-components/badge
Import the side effectful registration of `<sp-badge>` via:

import '@spectrum-web-components/badge/sp-badge.js';
When looking to leverage the `Badge` base class as a type and/or for extension purposes, do so via:

import { Badge } from '@spectrum-web-components/badge';
A badge is made up of the following parts:

*   **Icon**: an `<sp-icon-*>` element can be used to display an icon within the badge.
*   **Label**: text can be displayed within the badge by using the default slot.

Badges can contain either a label, an icon, or both.

<sp-badge size="s">Label only</sp-badge>
<sp-badge size="s">
  <sp-icon-checkmark-circle label="Icon-only badge" slot="icon" ></sp-icon-checkmark-circle>
</sp-badge>
<sp-badge size="s">
  <sp-icon-settings slot="icon"></sp-icon-settings>
  Icon and label
</sp-badge>
It is not recommended to make badges interactive. Consider using a different component if you need interactivity, such as buttons, tags, or links.

Small<div style="display: flex; gap: var(--spectrum-spacing-75);">
  <sp-badge size="s">Label</sp-badge>
  <sp-badge size="s">
    <sp-icon-checkmark-circle label="Icon-only badge" slot="icon" ></sp-icon-checkmark-circle>
  </sp-badge>
  <sp-badge size="s">
    <sp-icon-checkmark-circle slot="icon"></sp-icon-checkmark-circle>
    Icon and label
  </sp-badge>
</div>Medium<div style="display: flex; gap: var(--spectrum-spacing-75);">
  <sp-badge size="m">Label</sp-badge>
  <sp-badge size="m">
    <sp-icon-checkmark-circle label="Icon-only badge" slot="icon" ></sp-icon-checkmark-circle>
  </sp-badge>
  <sp-badge size="m">
    <sp-icon-checkmark-circle slot="icon"></sp-icon-checkmark-circle>
    Icon and label
  </sp-badge>
</div>Large<div style="display: flex; gap: var(--spectrum-spacing-75);">
  <sp-badge size="l">Label</sp-badge>
  <sp-badge size="l">
    <sp-icon-checkmark-circle label="Icon-only badge" slot="icon" ></sp-icon-checkmark-circle>
  </sp-badge>
  <sp-badge size="l">
    <sp-icon-checkmark-circle slot="icon"></sp-icon-checkmark-circle>
    Icon and label
  </sp-badge>
</div>Extra Large<div style="display: flex; gap: var(--spectrum-spacing-75);">
  <sp-badge size="xl">Label</sp-badge>
  <sp-badge size="xl">
    <sp-icon-checkmark-circle label="Icon-only badge" slot="icon" ></sp-icon-checkmark-circle>
  </sp-badge>
  <sp-badge size="xl">
    <sp-icon-checkmark-circle slot="icon"></sp-icon-checkmark-circle>
    Icon and label
  </sp-badge>
</div>
The `<sp-badge>` can be customized with either semantic or non-semantic variants. Badges are intended as display elements (like status lights), so avoid using badges for critical actions.

Semantic
When badges have a semantic meaning, they use semantic colors. Use these variants for the following statuses:

*   **Positive**: approved, complete, success, new, purchased, licensed
*   **Informative**: active, in use, live, published
*   **Negative**: error, alert, rejected, failed
*   **Neutral**: archived, deleted, paused, draft, not started, ended

<div style="display: flex; gap: var(--spectrum-spacing-75);">
  <sp-badge variant="accent">Accent</sp-badge>
  <sp-badge variant="neutral">Neutral</sp-badge>
  <sp-badge variant="informative">Informative</sp-badge>
  <sp-badge variant="positive">Positive</sp-badge>
  <sp-badge variant="negative">Negative</sp-badge>
  <sp-badge variant="notice">Notice</sp-badge>
</div>Non-semantic
When badges are for color-coded categories, they use non-semantic colors. Non-semantic variants are ideally used for when there are 8 categories or less.

<div style="display: flex; gap: var(--spectrum-spacing-75); flex-wrap:wrap;">
  <sp-badge variant="seafoam">Seafoam</sp-badge>
  <sp-badge variant="indigo">Indigo</sp-badge>
  <sp-badge variant="purple">Purple</sp-badge>
  <sp-badge variant="fuchsia">Fuchsia</sp-badge>
  <sp-badge variant="magenta">Magenta</sp-badge>
  <sp-badge variant="yellow">Yellow</sp-badge>
  <sp-badge variant="gray">Gray</sp-badge>
  <sp-badge variant="red">Red</sp-badge>
  <sp-badge variant="orange">Orange</sp-badge>
  <sp-badge variant="chartreuse">Chartreuse</sp-badge>
  <sp-badge variant="celery">Celery</sp-badge>
  <sp-badge variant="green">Green</sp-badge>
  <sp-badge variant="cyan">Cyan</sp-badge>
  <sp-badge variant="blue">Blue</sp-badge>
</div>
`<sp-badge>` can be displayed as if it is "fixed" to the edge of a UI. The `fixed` attribute can be leveraged to alter the border rounding based on the position you would like to achieve. Fixed positioning options include `block-start`, `block-end`, `inline-start`, and `inline-end`.

<div style="position: relative; width: 400px; height: 200px; background: #eee; max-width: 100%">
  <sp-badge>None</sp-badge>
  <sp-badge fixed="block-start" style="position: absolute; top: 0; left: 200px;" >
    block-start
  </sp-badge>
  <sp-badge fixed="inline-end" style="position: absolute; right: 0; top: 100px;" >
    inline-end
  </sp-badge>
  <sp-badge fixed="block-end" style="position: absolute; bottom: 0; left: 200px;" >
    block-end
  </sp-badge>
  <sp-badge fixed="inline-start" style="position: absolute; left: 0; top: 100px;" >
    inline-start
  </sp-badge>
</div>
Badges are not interactive by default.

When a badge's label is too long for the available horizontal space, it wraps to form another line. Text wrapping can be enforced when a `max-inline-size` is applied to the badge. If there is no room for a second line of text, the badge should truncate and include a tooltip to expose the full text upon hover.

<overlay-trigger>
  <sp-badge style="max-inline-size: 350px;" slot="trigger">
    Wikipedia is the best thing ever. Anyone in the world can write anything
    they want about any subject so you know you are getting the best possible
    information.
  </sp-badge>
  <sp-tooltip slot="hover-content">
    Wikipedia is the best thing ever. Anyone in the world can write anything
    they want about any subject so you know you are getting the best possible
    information.
  </sp-tooltip>
</overlay-trigger>
Do ✅Don't ❌Use badges for status indication Use badges for critical actions Use visible labels most often Overwhelm a user with too much critical information Use icon-only badges with aria-label Use badges for supplemental information

Badges should always have a label for accessibility and clear comprehension. When the label is not defined, a badge becomes icon-only. If a visible label isn't specified, an `aria-label` must be provided to the icon for accessibility. An icon-only badge is best for very small spaces, and it should include a tooltip on hover to provide more context for the icon's meaning.

Remember that a tooltip does not replace an accessible label.

<overlay-trigger>
  <sp-badge size="m" slot="trigger">
    <sp-icon-checkmark-circle label="Labels are important" slot="icon" ></sp-icon-checkmark-circle>
  </sp-badge>
  <sp-tooltip placement="top" slot="hover-content">
    <sp-icon-checkmark-circle slot="icon"></sp-icon-checkmark-circle>
    Labels are important
  </sp-tooltip>
</overlay-trigger>
*   Tab: Places focus on the badge if it is interactive.
*   Space or Enter: Filters results by the selected badge or performs the action associated with the badge.

The badge's variants provide semantic meaning through both color and ARIA attributes, ensuring that information is not conveyed through color alone.

*   Updated dependencies [`6f5419a`]: 
    *   @spectrum-web-components/core@0.0.4
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/core@0.0.3
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`283f0fe`, `1d76b70`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/core@0.0.2
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

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/badge

*   remove deprecated badge values (#4742)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

*   **badge:** expand and update variant availability and mod override usage (#4162) (19e1a49)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

*   **icon:** use core tokens (a11ef6b)

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

*   remove outdated CEM listing (2e110d9)

*   add badge component (cabfdfe)
*   **badge:** use core tokens (83e566c)
*   delivery dev mode messages in various packages (62370a1)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

*   **badge:** use core tokens (83e566c)

**Note:** Version bump only for package @spectrum-web-components/badge

*   include all Dev Mode files in side effects (f70817c)

*   delivery dev mode messages in various packages (62370a1)

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

**Note:** Version bump only for package @spectrum-web-components/badge

*   remove outdated CEM listing (2e110d9)

*   add badge component (cabfdfe)

Property  Attribute  Type  Default  Description `fixed``fixed``FixedValues | undefined` The fixed position of the badge. `variant``variant``BadgeVariantS1``'informative'` The variant of the badge.

Name  Description `default slot` Text label of the badge `icon` Optional icon that appears to the left of the label
