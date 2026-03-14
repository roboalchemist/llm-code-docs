# Source: https://opensource.adobe.com/spectrum-web-components/components/toast/

Title: Toast: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/toast/

Markdown Content:
`<sp-toast>` elements display brief, temporary notifications. They are noticeable but do not disrupt the user experience and do not require an action to be taken.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/toast?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/toast?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/toast
Import the side effectful registration of `<sp-toast>` via:

import '@spectrum-web-components/toast/sp-toast.js';
When looking to leverage the `Toast` base class as a type and/or for extension purposes, do so via:

import { Toast } from '@spectrum-web-components/toast';
The toast consists of two key parts:

*   The message content in its default slot
*   An optional action button using `slot="action"`

The message in its default slot:

<sp-toast open>
  This is important information that you should read, soon.
</sp-toast>
An optional action using `slot="action"`:

<sp-toast open>
  This is important information that you should read, soon.
  <sp-button slot="action" static-color="white" variant="secondary" treatment="outline" >
    Do something
  </sp-button>
</sp-toast>
The toast can be constrained to a specific width, and its content will wrap accordingly:

<sp-toast open style="width: 300px">
  This is important information that you should read, soon.
  <sp-button slot="action" static-color="white" variant="secondary" treatment="outline" >
    Do something
  </sp-button>
</sp-toast>
By default, the toast is rendered in gray and does not have an icon. This is used when the message is neutral in tone or when its semantics do not fit in any of the other variants.

However, the toast supports several variants to convey different types of messages:

Use `variant="negative"` to show an error or failure.

<sp-toast open variant="negative">
  This is negative information that you should read, soon.
</sp-toast>
Use `variant="positive"` to show a successful action or completion of a task.

<sp-toast open variant="positive">
  This is positive information that you should read, soon.
</sp-toast>
Use `variant="info"` to show an informative message.

<sp-toast open variant="info">
  This is information that you should read.
</sp-toast>
The toast can be configured to automatically dismiss itself after a specified duration. For accessibility reasons, the minimum timeout is 6000ms (6 seconds). For longer messages, it's recommended to add 1000ms for every 120 words.

<sp-toast open timeout="6000">
  This message will disappear after 6 seconds.
</sp-toast>
The toast dispatches a `close` event when it's being closed, either by user action or timeout. This event can be prevented using `event.preventDefault()`.

The toast supports keyboard navigation:

*   When an action button is present, it can be accessed using the Tab key
*   The close button (when present) can be activated using Enter or Space

The `<sp-toast>` element is rendered with a `role` of `alert` to notify screen readers. When rendering a toast on a page, it should be placed in a container with a `role` of `region` for better accessibility.

<div role="region" aria-label="Toast Notifications">
  <sp-toast open>
    This is important information that you should read, soon.
  </sp-toast>
</div>
Accessibility concerns require that a Toast is available for at least 6000ms before being dismissed.

The toast ensures that messages are visible for a minimum of 6 seconds to give users enough time to read and comprehend the information. For longer messages, the timeout is automatically extended.

It is suggested that messages longer than 120 words should receive an additional 1000ms in their timeout for each additional 120 words in the message.

For example, a message with 240 words should have a timeout of 7000ms, and a message with 360 words should have a timeout of 8000ms.

*   The toast's variant icon includes an appropriate `icon-label` for screen readers (e.g., "Information" for info variant)
*   Action buttons should have clear, descriptive labels

<sp-toast open variant="negative" icon-label="Warning">
  This is important information that you should read, soon.
  <sp-button slot="action" static-color="white" variant="secondary" treatment="outline" >
    Ignore warning
  </sp-button>
</sp-toast>

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   Updated dependencies [`f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`, `bdf54c1`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`f6cebbd`, `00eb0a8`]:

    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`4e06533`]: 
    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   **toast:** adds iconLabel to address accessibility (#4944) (8121057)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/toast

*   **toast:** added ability to wrap toast content with long words (#4738) (302d6fe)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   **progress-circle,toast,tooltip:** ensure complete dependency graph (#3701) (a5dfada)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   close button static white (d324017)
*   **toast:** switches toast[open] to use visibility hidden to fix overlay handling (#3511) (8428cad), closes #3510

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   correct @element jsDoc listing across library (c97a632)
*   ensure browser understandable extensions (f4e59f7)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **toast:** ensure "close" event only triggers when open===false (7fa08ba)
*   **toast:** include dependencies (1b82212)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   add and use icons-ui package (d9c3ab2)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   pass through autocomplete attribute to inputs (5416510)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **toast:** add "sp-toast" pattern (d0a5f00)
*   **toast:** default to "open === false", always dispatch "close" event (fcb3729)
*   **toast:** update spectrum css input (183ee95)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/toast

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   **toast:** ensure "close" event only triggers when open===false (7fa08ba)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **toast:** default to "open === false", always dispatch "close" event (fcb3729)
*   **toast:** update spectrum css input (183ee95)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **toast:** default to "open === false", always dispatch "close" event (fcb3729)
*   **toast:** update spectrum css input (183ee95)

**Note:** Version bump only for package @spectrum-web-components/toast

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/toast

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   ensure browser understandable extensions (f4e59f7)

**Note:** Version bump only for package @spectrum-web-components/toast

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   add and use icons-ui package (d9c3ab2)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

**Note:** Version bump only for package @spectrum-web-components/toast

*   pass through autocomplete attribute to inputs (5416510)

**Note:** Version bump only for package @spectrum-web-components/toast

*   **toast:** include dependencies (1b82212)

*   **toast:** add "sp-toast" pattern (d0a5f00)

 Property  Attribute  Type  Default  Description `iconLabel``icon-label``string | undefined` The `iconLabel` property is used to set the `label` attribute on the icon element. This is used to provide a text alternative for the icon to ensure accessibility. 
If the `iconLabel` property is not set, the icon will use the `variant` to dynamically set the `label`.

`open``open``boolean``false` The `open` property indicates whether the toast is visible or hidden. `timeout``timeout``number | null``null` When a timeout is provided, it represents the number of milliseconds from when the Toast was placed on the page before it will automatically dismiss itself. 
Accessibility concerns require that a Toast is available for at least 6000ms before being dismissed, so any timeout of less than 6000ms will be raised to that baseline.

It is suggested that messages longer than 120 words should receive an additional 1000ms in their timeout for each additional 120 words in the message.

For example, a message with 240 words should have a timeout of 7000ms, and a message with 360 words should have a timeout of 8000ms.

`variant``variant``ToastVariants` The variant applies specific styling when set to `negative`, `positive`, `info`, `error`, or `warning`. 
The variants `error` and `warning` are deprecated and should be replaced with `negative`.

`variant` attribute is removed when not matching one of the above.

Name  Description `default slot` The toast content `action` button element surfacing an action in the Toast

Name  Type  Description `close``CustomEvent``Announces that the Toast has been closed by the user or by its timeout.`
