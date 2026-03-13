# Source: https://opensource.adobe.com/spectrum-web-components/components/alert-banner/

Title: Alert Banner: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/alert-banner/

Markdown Content:
The `<sp-alert-banner>` displays pressing and high-signal messages, such as system alerts. It is intended to be noticeable and prompt users to take action.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/alert-banner?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/alert-banner?style=for-the-badge)

yarn add @spectrum-web-components/alert-banner
Import the side effectful registration of `<sp-alert-banner>` via:

import '@spectrum-web-components/alert-banner/sp-alert-banner.js';
The alert dialog consists of several key parts:

The message in its default slot.

<sp-alert-banner open>
  All documents in this folder have been archived
</sp-alert-banner>
An optional action using `slot="action"`:

<sp-alert-banner open>
  Your trial has expired
  <sp-button treatment="outline" static-color="white" variant="secondary" slot="action" >
    Buy now
  </sp-button>
</sp-alert-banner>
<bd></bd>
Use the `dismissible` attribute to include an icon-only close button used to dismiss the alert banner:

<sp-alert-banner open dismissible>
  All documents in this folder have been archived
</sp-alert-banner>
The `<sp-alert-banner>` supports three variants, `neutral`(default), `info` and `negative`, to convey the nature of the message:

Info
Use `variant="info"` for informational messages.

<sp-alert-banner open variant="info" dismissible>
  Your trial will expire in 3 days
  <sp-button treatment="outline" static-color="white" slot="action">
    Buy now
  </sp-button>
</sp-alert-banner>Negative
Use `variant="negative"` for error or warning messages.

<sp-alert-banner open variant="negative" dismissible>
  Connection interrupted. Check your network to continue
</sp-alert-banner>
Alert banners should be used for system-level messages and they should be dismissed only as a result of a user action or if the internal state that triggered the alert has been resolved.

The alert can be dismissed by triggering the close button in case of a dismissible alert. It also exposes a public `close` method to allow consumers to close the alert programmatically.

The component dispatches a `close` event to announce that the alert banner has been closed. This can be prevented by using the `event.preventDefault()` API.

The `<sp-alert-banner>` is rendered with a `role` of `alert` to notify screen readers.

When rendering an alert that is dismissable or has actions on a page, ensure the alert is placed in a container with a `role` of `region` that includes a unique `aria-label` or `aria-labelledby` for better accessibility.

It supports keyboard interactions, including:

Key Action Tab Navigate to the next interactive element Shift + Tab Navigate to the previous interactive element Space/Enter Trigger the focused button Esc Dismiss a dismissible alert ArrowLeft/ArrowRight/ArrowUp/ArrowDown Once focus is on the alert banner, arrow keys can be used to navigate between the close button and the slotted action buttons

*   #5998`6f5419a` Thanks @rubencarvalho! - **Fixed** missing export for `alert-banner` from `@spectrum-web-components/core`, which could cause build failures in certain environments.

*   Updated dependencies [`6f5419a`]:

    *   @spectrum-web-components/core@0.0.4
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/core@0.0.3
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   Updated dependencies [`283f0fe`, `1d76b70`, `9cb816b`]: 
    *   @spectrum-web-components/core@0.0.2
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies [`7d23140`, `bdf54c1`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies [`f6cebbd`, `00eb0a8`]: 
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`4e06533`]:

    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

**Note:** Version bump only for package @spectrum-web-components/alert-banner

*   **alert-banner:** add alert banner component (#4266) (10d456e)
*   Silder: adjust fillStart calculation for value=0 and normalization function (#4573) (369fee7), closes #4558

Property  Attribute  Type  Default  Description `dismissible``dismissible``boolean``false` Whether to include an icon-only close button to dismiss the alert banner `open``open``boolean``false` Controls the display of the alert banner `variant``variant``AlertBannerVariants` The variant applies specific styling when set to `negative` or `info`; `variant` attribute is removed when it's passed an invalid variant.

Name  Description `default slot` The alert banner text context `action` Slot for the button element that surfaces the contextual action a user can take

Name  Type  Description `close``CustomEvent``Announces the alert banner has been closed`
