# Source: https://opensource.adobe.com/spectrum-web-components/components/contextual-help/

Title: Contextual Help: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/contextual-help/

Markdown Content:
An `<sp-contextual-help>` shows a user extra information about the state of either an adjacent component or an entire view. It explains a high-level topic about an experience and can point users to more information elsewhere.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/contextual-help?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/contextual-help?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/contextual-help
Import the side effectful registration of `<sp-contextual-help>` via:

import '@spectrum-web-components/contextual-help/sp-contextual-help.js';
When looking to leverage the `ContextualHelp` base class as a type and/or for extension purposes, do so via:

import { ContextualHelp } from '@spectrum-web-components/contextual-help';
Contextual help is a wrapper that attaches a popover to an icon-only action button.

It consists of the following parts:

*   **Heading**: assign the appropriate heading level to the `heading` slot to provide a title for the popover.
*   **Content**: text can be displayed within the popover by using the default slot.
*   **Link**: an optional `<sp-link>` can be assigned to the `link` slot per standalone link guidance.

Information
The default variant is for in-line information using the "info" icon. Use the info icon for informative content: specific, brief, and contextual guidance. This is best for supplemental or nice-to-know information, in-line with a label or a component (if there is no label). The content should be instructive in tone.

<sp-contextual-help>
  <h2 slot="heading">Permission required</h2>
  Your admin must grant you permission before you can create a segment.
  <sp-link slot="link" href="https://opensource.adobe.com/spectrum-web-components/" >
    Request permission
  </sp-link>
</sp-contextual-help>Help
Use `variant="help"` for helpful content: more detailed, in-depth guidance about a task, UI element, tool, or keyboard shortcuts. This may include an image, video, or link and should be helpful in tone.

<sp-contextual-help variant="help">
  <h2 slot="heading">What is a segment?</h2>
  Segments identify who your visitors are, what devices and services they use,
  where they navigate from, and much more.
  <sp-link slot="link" href="https://opensource.adobe.com/spectrum-web-components/" >
    Learn more about segments
  </sp-link>
</sp-contextual-help>
By default an `<sp-contextual-help>` will render its popover at the `bottom-start` position. This can be customized using the `placement` attribute and supports all the placement options an `overlay-trigger` component supports.

<sp-contextual-help placement="top-start">
  <h2 slot="heading">Permission required</h2>
  Your admin must grant you permission before you can create a segment.
  <sp-link slot="link" href="https://opensource.adobe.com/spectrum-web-components/" >
    Request permission
  </sp-link>
</sp-contextual-help>
Contextual help allows for a custom maximum width to be set using the `--mod-spectrum-contextual-help-popover-maximum-width` custom property.

Note: Maximum width should not be less than 100px.

<sp-contextual-help style="--mod-spectrum-contextual-help-popover-maximum-width: 200px;">
  <h2 slot="heading">Custom max width</h2>
  This is a test of the contextual help component with a custom max width of
  200px.
</sp-contextual-help>
`<sp-contextual-help>` does not fire any events of its own. You can listen, however, for the `sp-open` and `sp-closed` events which are fired when the popover opens or closes.

Given that the trigger is an icon-only `<sp-action-button>`, it is important to provide an accessible name for it, so that it can be properly announced by screen readers. By default, the `<sp-contextual-help>` uses an `aria-label` property with either "Information" or "Help" as values, depending on the component's `variant`. You can customize this using the `label` attribute.

When providing headings using the `heading` slot, make sure to provide actual heading elements such as `h1`, `h2`, `h3` ... or use the `role="heading"` attribute.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/dialog@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/action-button@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2
    *   @spectrum-web-components/overlay@1.11.2
    *   @spectrum-web-components/popover@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/dialog@1.11.1
    *   @spectrum-web-components/overlay@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1
    *   @spectrum-web-components/popover@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5960`e66cdb2` Thanks @blunteshwar! - ## Changeset

**Fix: Contextual Help popover inaccessible to screen readers**

Adds required ARIA attributes to associate the trigger button with popover content, enabling screen readers to announce the heading and body text when the popover opens.

*   Updated dependencies [`b95e254`, `02b2d7d`, `f07344f`, `1d76b70`, `cadc39e`, `4cb0b7b`, `9cb816b`]:

    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/popover@1.11.0
    *   @spectrum-web-components/action-button@1.11.0
    *   @spectrum-web-components/dialog@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/dialog@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/overlay@1.10.0
    *   @spectrum-web-components/popover@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies [`a19cbe3`]: 
    *   @spectrum-web-components/overlay@1.9.1
    *   @spectrum-web-components/popover@1.9.1
    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/dialog@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1

*   Updated dependencies [`bdf54c1`, `7d23140`]: 
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/dialog@1.9.0
    *   @spectrum-web-components/overlay@1.9.0
    *   @spectrum-web-components/popover@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   #5690`99ab45e` Thanks @5t3ph! - Fixed a typo in the default `info` variant label from "Informations" to "Information".

Additionally, added package dependency for `@spectrum-web-components/reactive-controllers@1.7.0`.

*   Updated dependencies [`14486d6`, `ee1bae6`, `14486d6`]:

    *   @spectrum-web-components/overlay@1.8.0
    *   @spectrum-web-components/popover@1.8.0
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/dialog@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0

*   Updated dependencies [`a646ae8`, `c1669d2`]: 
    *   @spectrum-web-components/overlay@1.7.0
    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/popover@1.7.0
    *   @spectrum-web-components/dialog@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies [`03a4439`, `f6cebbd`, `53f3769`]: 
    *   @spectrum-web-components/popover@1.6.0
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/overlay@1.6.0
    *   @spectrum-web-components/dialog@1.6.0
    *   @spectrum-web-components/action-button@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies [`8f8735c`, `6c58f50`]: 
    *   @spectrum-web-components/overlay@1.5.0
    *   @spectrum-web-components/action-button@1.5.0
    *   @spectrum-web-components/dialog@1.5.0
    *   @spectrum-web-components/popover@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   #5140`3cca7ea` Thanks @TarunAdobe! - Contextual help now supports a custom maximum width to be set using the `--mod-spectrum-contextual-help-popover-maximum-width` custom property.

*   Updated dependencies [`72dbe62`, `46cd782`, `70f5f6f`]: 
    *   @spectrum-web-components/action-button@1.4.0
    *   @spectrum-web-components/overlay@1.4.0
    *   @spectrum-web-components/popover@1.4.0
    *   @spectrum-web-components/dialog@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies [`468314f`]: 
    *   @spectrum-web-components/dialog@1.3.0
    *   @spectrum-web-components/overlay@1.3.0
    *   @spectrum-web-components/popover@1.3.0
    *   @spectrum-web-components/action-button@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

**Note:** Version bump only for package @spectrum-web-components/contextual-help

*   **contextual-help:** add contextual help pattern (#4285) (a259aa3)

Property  Attribute  Type  Default  Description `label``label``string | undefined` Provides an accessible name for the action button trigger. `offset``offset``number | [number, number]``0` The `offset` property accepts either a single number, to define the offset of the Popover along the main axis from the action button, or 2-tuple, to define the offset along the main axis and the cross axis. `open``open``boolean``false``placement``placement``"top" | "top-start" | "top-end" | "right" | "right-start" | "right-end" | "bottom" | "bottom-start" | "bottom-end" | "left" | "left-start" | "left-end"``'bottom-start'``variant``variant``'info' | 'help'``'info'` The `variant` property applies specific styling on the action button trigger.

Name  Description `Text` content to display in the popover `heading` content to display as the heading of the popover `link` link to additional informations
