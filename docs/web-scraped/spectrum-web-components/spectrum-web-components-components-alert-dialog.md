# Source: https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/

Title: Alert Dialog: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/alert-dialog/

Markdown Content:
`<sp-alert-dialog role="alertdialog" aria-labelledby="xx-heading" aria-describedby="xx-message" role="alertdialog" aria-labelledby="" aria-describedby="">` displays important information that users need to acknowledge. When used directly, the `<sp-alert-dialog role="alertdialog" aria-labelledby="xx-heading" aria-describedby="xx-message" role="alertdialog" aria-labelledby="" aria-describedby="">` element surfaces a `slot` based API for deep customization of the content to be included in the overlay.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/alert-dialog?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/alert-dialog?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/alert-dialog
Import the side effectful registration of `<sp-alert-dialog role="alertdialog" aria-labelledby="xx-heading" aria-describedby="xx-message" role="alertdialog" aria-labelledby="" aria-describedby="">` via:

import '@spectrum-web-components/alert-dialog/sp-alert-dialog.js';
When looking to leverage the `AlertDialog` base class as a type and/or for extension purposes, do so via:

import { AlertDialog } from '@spectrum-web-components/alert-dialog';
The alert dialog consists of several key parts:

*   **Title:** All alert dialogs must have a title, using `slot="heading"`, that uses a few words to convey the outcome of what will happen if a user continues with an action
*   **Content:** Alert dialogs can include a description using the default slot. A description briefly communicates any additional information or context that a user needs to know to continue with an action
*   Action buttons, using `slot="button"`, that allow users to respond

<sp-alert-dialog role="alertdialog" aria-labelledby="example-heading" aria-describedby="example-message" variant="confirmation">
  <h2 id="example-heading" slot="heading">Important Notice</h2>
  <p id="example-message">This action requires your confirmation.</p>
  <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Cancel
  </sp-button>
  <sp-button slot="button" variant="accent" treatment="fill" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Confirm
  </sp-button>
</sp-alert-dialog>
Use `slot="button"` to render your action button(s) that allow users to respond

*   An alert dialog must have one primary action button (with `variant="primary"`) with the option to include a secondary action and/or a cancel action.
*   Non-primary action buttons should be `variant="secondary"` and `treatment="outline"`.
*   The three buttons should be rendered in the DOM in the following order: 
    *   **Cancel action:** Offers an option to go back and cancel the action.
    *   **Secondary action:** Offers a secondary action. e.g. "Remind me later"
    *   **Primary action:** The first (right-most) button communicates what the button will do if selected, or to acknowledge and dismiss the dialog. Check variants for the correct primary button styling. See also the Alert Dialog design options.

<sp-alert-dialog role="alertdialog" aria-labelledby="rate-heading" aria-describedby="rate-message" variant="information">
  <h2 id="rate-heading" slot="heading">Rate this app</h2>
  <p id="rate-message">
    If you enjoy our app, would you mind taking a moment to rate it?
  </p>
  <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    No, thanks
  </sp-button>
  <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Remind me later
  </sp-button>
  <sp-button slot="button" variant="primary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Rate now
  </sp-button>
</sp-alert-dialog>
The alert dialog supports `confirmation`, `information`, `warning`, `error`, and `destructive` variants to convey the nature and importance of the message:

Confirmation
Confirmation is the default variant for alert dialogs. Use a confirmation variant for asking a user to confirm a choice.

<sp-alert-dialog role="alertdialog" aria-labelledby="disclaimer-heading" aria-describedby="disclaimer-message" variant="confirmation">
  <h2 id="disclaimer-heading" slot="heading">Disclaimer</h2>
  <p id="disclaimer-message">
    Smart filters are nondestructive and will preserve your original images.
  </p>
  <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Cancel
  </sp-button>
  <sp-button slot="button" variant="accent" treatment="fill" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Enable
  </sp-button>
</sp-alert-dialog>Information
Information alert dialogs communicate important information that a user needs to acknowledge. Before using this kind of alert dialog, make sure it’s the appropriate communication channel for the message instead of a toast or a more lightweight messaging option.

<sp-alert-dialog role="alertdialog" aria-labelledby="information-heading" aria-describedby="information-message" variant="information">
  <h2 id="information-heading" slot="heading">Connect to wifi</h2>
  <p id="information-message">
    Please connect to wifi to sync your projects or go to Settings to change
    your preferences.
  </p>
  <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Cancel
  </sp-button>
  <sp-button slot="button" variant="primary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Continue
  </sp-button>
</sp-alert-dialog>Warning
Warning alert dialogs communicate important information to users in relation to an issue that needs to be acknowledged, but does not block the user from moving forward.

<sp-alert-dialog role="alertdialog" aria-labelledby="warning-heading" aria-describedby="warning-message" variant="warning">
  <h2 id="warning-heading" slot="heading">Unverified format</h2>
  <p id="warning-message">
    This format has not been verified and may not be viewable for some users. Do
    you want to continue publishing?
  </p>
  <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Cancel
  </sp-button>
  <sp-button slot="button" variant="primary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Continue
  </sp-button>
</sp-alert-dialog>Error
Error alert dialogs communicate critical information about an issue that a user needs to acknowledge.

<sp-alert-dialog role="alertdialog" aria-labelledby="error-heading" aria-describedby="error-message" variant="error">
  <h2 id="error-heading" slot="heading">Unable to share</h2>
  <p id="error-message">
    An error occurred while sharing your project. Please verify the email
    address and try again.
  </p>
  <sp-button slot="button" variant="primary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Continue
  </sp-button>
</sp-alert-dialog>Destructive
Destructive alert dialogs are for when a user needs to confirm an action that will impact their data or experience in a potentially negative way, such as deleting files or contacts.

<sp-alert-dialog role="alertdialog" aria-labelledby="destructive-heading" aria-describedby="destructive-message" variant="destructive">
  <h2 id="destructive-heading" slot="heading">Delete 3 documents?</h2>
  <p id="destructive-message">
    Are you sure you want to delete the 3 selected documents?
  </p>
  <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Cancel
  </sp-button>
  <sp-button slot="button" variant="negative" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
    Delete
  </sp-button>
</sp-alert-dialog>
An alert dialog should be placed inside a modal overlay or a dialog base:

Modal overlay<sp-button id="trigger">open modal</sp-button>
<sp-overlay trigger="trigger@click" type="modal" placement="bottom">
  <sp-popover>
    <sp-alert-dialog role="alertdialog" aria-labelledby="modal-heading" aria-describedby="modal-message" variant="confirmation" >
      <h2 id="modal-heading" slot="heading">Important Notice</h2>
      <p id="modal-message">This action requires your confirmation.</p>
      <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Cancel
      </sp-button>
      <sp-button slot="button" variant="accent" treatment="fill" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Confirm
      </sp-button>
    </sp-alert-dialog>
  </sp-popover>
</sp-overlay>Dialog base<overlay-trigger type="modal">
  <sp-dialog-base underlay slot="click-content">
    <sp-alert-dialog role="alertdialog" aria-labelledby="modal-heading" aria-describedby="modal-message" variant="confirmation" >
      <h2 id="modal-heading" slot="heading">Important Notice</h2>
      <p id="modal-message">This action requires your confirmation.</p>
      <sp-button slot="button" variant="secondary" treatment="outline" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Cancel
      </sp-button>
      <sp-button slot="button" variant="accent" treatment="fill" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Confirm
      </sp-button>
    </sp-alert-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
*   Use `role="alertdialog"` on the alert dialog
*   Make sure the alert dialog has an `aria-labelledby` attribute that references the title's `id`.
*   Make sure the alert dialog has an `aria-describedby` attribute that references the content's `id`.

*   Consider the appropriate variant based on the message's importance and urgency
*   Use concise, meaningful dialog title that clearly states the purpose
*   Use semantic heading elements (`<h2>`) for the dialog title

*   Provide clear, concise content that explains the situation and required actions

####Buttons

*   Ensure button labels clearly indicate the action they will perform

*   Updated dependencies []: 
    *   @spectrum-web-components/divider@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/button-group@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/divider@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/button-group@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   Updated dependencies [`f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/divider@1.11.0
    *   @spectrum-web-components/button-group@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/button-group@1.10.0
    *   @spectrum-web-components/divider@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/button-group@1.9.1
    *   @spectrum-web-components/divider@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5747`51f8e90` Thanks @iuliauta! - - **Fixed**: Make the divider color transparent only for Spectrum 2 theme

*   Updated dependencies [`7d23140`, `bdf54c1`]:

    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/button-group@1.9.0
    *   @spectrum-web-components/divider@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies [`15be17d`, `826a2d5`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/divider@1.8.0
    *   @spectrum-web-components/button-group@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/button-group@1.7.0
    *   @spectrum-web-components/divider@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`f6cebbd`, `00eb0a8`]: 
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/button-group@1.6.0
    *   @spectrum-web-components/divider@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`165a904`, `4e06533`]:

    *   @spectrum-web-components/button-group@1.5.0
    *   @spectrum-web-components/divider@1.5.0
    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/button-group@1.4.0
    *   @spectrum-web-components/divider@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/button-group@1.3.0
    *   @spectrum-web-components/divider@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

**Note:** Version bump only for package @spectrum-web-components/alert-dialog

*   **alert-dialog:** use resize observer in place of page resize event for content measurement work (b963813)

*   **alert-dialog:** add Alert Dialog package (#3501) (1062847)

Property  Attribute  Type  Default  Description `variant``variant``AlertDialogVariants`
