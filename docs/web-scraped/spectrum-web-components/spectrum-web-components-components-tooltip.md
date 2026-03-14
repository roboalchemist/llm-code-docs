# Source: https://opensource.adobe.com/spectrum-web-components/components/tooltip/

Title: Tooltip: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/tooltip/

Markdown Content:
`<sp-tooltip>` allow users to get contextual help or information about specific components when hovering or focusing on them.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/tooltip?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/tooltip?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/tooltip
Import the side effectful registration of `<sp-tooltip>` via:

import '@spectrum-web-components/tooltip/sp-tooltip.js';
When looking to leverage the `Tooltip` base class as a type and/or for extension purposes, do so via:

import { Tooltip } from '@spectrum-web-components/tooltip';
The tooltip consists of several key parts:

*   The message content in its default slot
*   An optional icon using `slot="icon"`
*   A tip element that points to the trigger

<sp-tooltip open>
  <sp-icon-info slot="icon"></sp-icon-info>
  Tooltip message
</sp-tooltip>
Tooltips can be positioned relative to their trigger element using the `placement` attribute:

<sp-tooltip open placement="left">Left</sp-tooltip>
<sp-tooltip open placement="bottom">Bottom</sp-tooltip>
<sp-tooltip open placement="right">Right</sp-tooltip>
<sp-tooltip open placement="top">Top</sp-tooltip>
The tooltip supports several variants to convey different types of messages:

Info
Use `variant="info"` for informational messages.

<sp-tooltip open placement="top" variant="info">
  <sp-icon-info slot="icon" size="s"></sp-icon-info>
  Embark on a side quest.
</sp-tooltip>Positive
Use `variant="positive"` for success messages.

<sp-tooltip open placement="top" variant="positive">
  <sp-icon-checkmark-circle slot="icon" size="s"></sp-icon-checkmark-circle>
  Quest completed!
</sp-tooltip>Negative
Use `variant="negative"` for error messages.

<sp-tooltip open placement="top" variant="negative">
  <sp-icon-alert slot="icon" size="s"></sp-icon-alert>
  Quest failed!
</sp-tooltip>
By default, Tooltip provides styling without behavior.

Overlay Trigger
You must combine it with an Overlay Trigger to manage its overlay behavior.

<overlay-trigger triggered-by="hover">
  <sp-button slot="trigger" variant="secondary">Hover me</sp-button>
  <sp-tooltip slot="hover-content" placement="bottom">
    Tooltip overlay triggered by hover
  </sp-tooltip>
</overlay-trigger>Self-managed
For simpler use cases, you can use the `self-managed` attribute which automatically binds the Tooltip to its first interactive ancestor element's focus/hover interactions:

<sp-action-button>
  Items
  <sp-tooltip self-managed>Use items during battle.</sp-tooltip>
</sp-action-button>
This is especially useful when inserting an intermediate `<overlay-trigger>` would interfere with parent/child relationships, such as between `<sp-action-group>` and `<sp-action-button>`.

A tooltip can be configured to delay its opening using the `delayed` attribute. This adds a warm-up period of 1000ms before showing the tooltip:

<sp-action-button>
  Show delayed tooltip
  <sp-tooltip self-managed delayed>
    This tooltip will show after a delay
  </sp-tooltip>
</sp-action-button>
The tooltip is automatically assigned appropriate ARIA attributes:

*   `role="tooltip"` is applied to the tooltip content
*   The tooltip is associated with its trigger element via `aria-describedby`

When using `self-managed` tooltips:

*   The tooltip appears on hover or focus of the trigger element
*   The tooltip disappears when focus or hover leaves the trigger element
*   Escape dismisses the tooltip

Icons are not always easy to identify on their own. When you use components that don’t have labels — for example, icon-only action buttons and tabs — make sure to use tooltips to provide context for the icons.

Given that tooltip is not focusable by itself, it would not show up during tab navigation. A tooltip should only be used with interactive elements that can receive focus during tab navigation, such as:

*   `<sp-action-button>`
*   `<sp-action-menu>`
*   `<sp-field-label>`

For non-interactive elements like icons, wrap them in an interactive element:

<sp-action-button size="s">
  <sp-icon-book slot="icon"></sp-icon-book>
  <sp-tooltip self-managed placement="right">Save progress.</sp-tooltip>
</sp-action-button>
Because a tooltip is not focusable by itself, it should not contain any interactive elements. Additionally, because a tooltip is referenced in an `aria-describedby` attribute, it should not contain any rich formatting, such as headings, lists, bold, italic, or other complex content.

Show crucial information at all times, not just when a tooltip is displayed. A tooltip should only be used to provide supplementary context or hints to the message shown in help text.

For example, in a scenario where a user is entering their password into a field, the crucial information would be to state the password requirements. Supplementary context would be a message about how to get help if they have forgotten their password.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/overlay@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/overlay@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5878`e780f82` Thanks @rise-erpelding! - **Fixed**: Fixed an issue with text overflow in `sp-tooltip`: long, unbroken words were not wrapping and overflowed the container.

*   Updated dependencies [`b95e254`, `02b2d7d`, `f07344f`, `1d76b70`, `f8bdeec`, `cadc39e`, `4cb0b7b`, `9cb816b`]:

    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/overlay@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies [`a19cbe3`]: 
    *   @spectrum-web-components/overlay@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/overlay@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies [`14486d6`, `ee1bae6`, `14486d6`]: 
    *   @spectrum-web-components/overlay@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   #5504`cde976d` Thanks @castastrophe! - Replace deprecated `word-break: break-word` with `overflow-wrap: break-word` to align with modern CSS standards and improve cross-browser compatibility. This property was deprecated in Chrome 44 (July 2015) in favor of the standardized `overflow-wrap` property.

*   Updated dependencies [`a646ae8`]:

    *   @spectrum-web-components/overlay@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5384`700489f` Thanks @Rajdeepc! - docs: add DelayedTooltipWithOverlay story demonstrating how to handle interactions between delayed tooltips and other overlay components

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`53f3769`]:

    *   @spectrum-web-components/overlay@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`8f8735c`]: 
    *   @spectrum-web-components/overlay@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies [`46cd782`, `70f5f6f`]: 
    *   @spectrum-web-components/overlay@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`, `468314f`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/overlay@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **tooltip:** make tooltip delivery consistent across all browsers (#5056) (d01d5cd)

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   add an optional chromatic vrt action (7d2f840)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **overlay:** ensure hint Overlays within shadow roots open as expected (#4443) (7dd64b9)

*   **overlay:** ensure hint Overlays within shadow roots open as expected (#4443) (7dd64b9)

*   **overlay:** ensure hint Overlays within shadow roots open as expected (#4443) (7dd64b9)

*   **tooltip:** fix infinite loop in self-managed tooltips (#4269) (b66ee49)

*   **tooltip:** fix infinite loop in self-managed tooltips (#4269) (b66ee49)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **overlay:** move closed overlays to "display: none" (fc0278b)
*   **picker:** force close slotted Tooltip elements with disabled when Menu openes (82c8f12)
*   **tooltip:** surface "delayed" and "disabled" functionality (#3882) (ae9fcd2)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **progress-circle,toast,tooltip:** ensure complete dependency graph (#3701) (a5dfada)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   address margin effected positioning (38c8cf2)

*   **tooltip:** leverage Overlay v2 (346edac)

*   make lots of things lazy (b8fa3ad)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   allow ActiveOverlay to manage open state (a7c4cff)
*   correct @element jsDoc listing across library (c97a632)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   **overlay:** add overlay lifecycle methods to stack management (9361527)
*   **overlay:** allow overlay-trigger to declaratively open overlay content (194a44e)
*   position tip shapes for bi-directional delivery (35654de)
*   special case the possibility of leaving an overlay trigger by entering its overlay content (c32a075)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **tooltip:** correct arrow orientation, remove popper-arrow-rotate (fcd6ea2)
*   **tooltip:** ensure delayed and self-managed tooltips do not disrupt the page layout (0f43b25)
*   **tooltip:** manage describedby attributes non-destructively (8443136)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   rework overlays to use popper (e17d1bb)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tooltip:** initial release (c1331c9)
*   **tooltip:** update spectrum css input (a946b1c)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   special case the possibility of leaving an overlay trigger by entering its overlay content (c32a075)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   update consumption of Spectrum CSS for latest version (ed2305b)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **tooltip:** manage describedby attributes non-destructively (8443136)

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **tooltip:** ensure delayed and self-managed tooltips do not disrupt the page layout (0f43b25)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **overlay:** add overlay lifecycle methods to stack management (9361527)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   **overlay:** allow overlay-trigger to declaratively open overlay content (194a44e)

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   position tip shapes for bi-directional delivery (35654de)
*   **tooltip:** correct arrow orientation, remove popper-arrow-rotate (fcd6ea2)
*   allow ActiveOverlay to manage open state (a7c4cff)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **tooltip:** update spectrum css input (a946b1c)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **tooltip:** update spectrum css input (a946b1c)

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   rework overlays to use popper (e17d1bb)

**Note:** Version bump only for package @spectrum-web-components/tooltip

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use @adobe/spectrum-css@2.15.1 (3918888)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   **tooltip:** initial release (c1331c9)

Property  Attribute  Type  Default  Description `delayed``delayed``boolean``false` A Tooltip that is `delayed` will its Overlay wait until a warm-up period of 1000ms has completed before opening. Once the warmup period has completed, all subsequent Overlays will open immediately. When no Overlays are opened, a cooldown period of 1000ms will begin. Once the cooldown has completed, the next Overlay to be opened will be subject to the warm-up period if provided that option. `disabled``disabled``boolean``false` Whether to prevent a self-managed Tooltip from responding to user input. `offset``offset``number``0``open``open``boolean``false``placement``placement``"top" | "top-start" | "top-end" | "right" | "right-start" | "right-end" | "bottom" | "bottom-start" | "bottom-end" | "left" | "left-start" | "left-end"``selfManaged``self-managed``boolean``false` Automatically bind to the parent element of the assigned `slot` or the parent element of the `sp-tooltip`. Without this, you must provide your own `overlay-trigger`. `tipPadding``tipPadding``number | undefined``variant``variant``string`

Name  Description `icon` the icon element appearing at the start of the label `default slot` the text label of the Tooltip

Name  Type  Description `undefined``TransitionEvent`
