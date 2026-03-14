# Source: https://opensource.adobe.com/spectrum-web-components/components/tray/

Title: Tray: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/tray/

Markdown Content:
`<sp-tray>` elements are typically used to portray information on mobile device or smaller screens.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/tray?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/tray?style=for-the-badge)

yarn add @spectrum-web-components/tray
Import the side effectful registration of `<sp-tray>` via:

import '@spectrum-web-components/tray/sp-tray.js';
When looking to leverage the `Tray` base class as a type and/or for extension purposes, do so via:

import { Tray } from '@spectrum-web-components/tray';
A tray has a single default `slot`. Expected content typically includes dialogs and their content, plain text, forms and/or form elements, and some native HTML elements. Always ensure that your tray's content is accessible according to WCAG standards.

<overlay-trigger type="modal">
  <sp-button slot="trigger" variant="secondary">Toggle tray</sp-button>
  <sp-tray slot="click-content">
    <sp-dialog size="s" dismissable>
      <h2 slot="heading">New Messages</h2>
      You have 5 new messages.
    </sp-dialog>
  </sp-tray>
</overlay-trigger>
`<sp-tray>` presents a page blocking experience and should be opened with the `Overlay` API using the `modal` interaction to ensure that the content appropriately manages the presence of other content in the tab order of the page and the availability of that content for a screen reader.

By default, `<sp-tray>` automatically detects whether its slotted content includes keyboard-accessible dismiss buttons (like `<sp-button>`, `<sp-close-button>`, or HTML `<button>` elements). When no dismiss buttons are found, the tray renders visually hidden dismiss buttons before and after its content to support mobile screen readers, particularly VoiceOver on iOS where users navigate through interactive elements sequentially.

These built-in dismiss buttons:

*   Are visually hidden but accessible to screen readers
*   Allow mobile screen reader users to easily dismiss the tray from either the beginning or end of the content
*   Are labeled "Dismiss" for clear screen reader announcements

This dismiss helper pattern is also implemented in the `<sp-picker>` component, which uses the same approach when rendering menu content in a tray on mobile devices.

Content has no buttons
This example shows the default behavior where the tray automatically detects that the content lacks dismiss buttons and renders visually hidden helpers. Screen readers will announce them as "Dismiss, button" and these helpers are keyboard accessible.

<overlay-trigger type="modal">
  <sp-button slot="trigger" variant="secondary">Toggle tray content</sp-button>
  <sp-tray slot="click-content">
    <div style="display: flex; flex-direction: column; margin: 16px;">
      <p style="margin-block-start: 0;">
        Custom content that doesn't have dismiss functionality, so the tray
        detects it needs the visually-hidden dismiss buttons.
      </p>
      <label>
        What's your favorite Super Mario character?
        <select name="favorite-characters" style="margin-block-start: 8px;">
          <option value="">Choose your favorite Super Mario character.</option>
          <option value="mario">Mario</option>
          <option value="luigi">Luigi</option>
          <option value="toad">Toad</option>
          <option value="bowser">Bowser</option>
        </select>
      </label>
    </div>
  </sp-tray>
</overlay-trigger>Content has buttons
This example shows auto-detection recognizing that the dialog has its own dismiss functionality, so no additional helpers are rendered.

<overlay-trigger type="modal">
  <sp-button slot="trigger" variant="secondary">
    Toggle dialog content
  </sp-button>
  <sp-tray slot="click-content">
    <sp-dialog size="s" dismissable>
      <h2 slot="heading">New messages</h2>
      You have 5 new messages.
    </sp-dialog>
  </sp-tray>
</overlay-trigger>Manual override
Set `has-keyboard-dismiss` (or `has-keyboard-dismiss="true"`) to prevent the tray from rendering visually hidden dismiss helpers, even when no buttons are detected. You are then responsible for ensuring that your tray content has keyboard-accessible dismiss functionality.

<overlay-trigger type="modal">
  <sp-button slot="trigger" variant="secondary">
    Toggle without helpers
  </sp-button>
  <sp-tray slot="click-content" has-keyboard-dismiss>
    <p style="margin: 16px;">
      Custom content that should have custom dismiss functionality, even though
      the tray didn't detect buttons in this slot.
    </p>
  </sp-tray>
</overlay-trigger>

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/modal@1.11.2
    *   @spectrum-web-components/underlay@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/modal@1.11.1
    *   @spectrum-web-components/underlay@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5814`6b887f2` Thanks @marissahuysentruyt! - **Added**: Automatic dismiss button detection and visually-hidden helpers for screen reader accessibility 
    *   **Added**: `<sp-tray>` now automatically detects keyboard-accessible dismiss buttons (like `<sp-button>`, `<sp-close-button>`, or HTML `<button>` elements) in slotted content
    *   **Added**: When no dismiss buttons are detected, the tray automatically renders visually-hidden dismiss buttons before and after its content to support mobile screen readers (particularly VoiceOver on iOS)
    *   **Added**: New `has-keyboard-dismiss` boolean attribute to manually override auto-detection when slotted content has custom dismiss functionality that cannot be automatically detected
    *   **Added**: Auto-detection recognizes `<sp-dialog dismissable>` and `<sp-dialog-wrapper dismissable>` components with built-in dismiss functionality in shadow DOM
    *   **Enhanced**: Improved mobile screen reader accessibility by ensuring dismissal options are always available when appropriate

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/modal@1.11.0
    *   @spectrum-web-components/underlay@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/modal@1.10.0
    *   @spectrum-web-components/underlay@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/modal@1.9.1
    *   @spectrum-web-components/underlay@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/modal@1.9.0
    *   @spectrum-web-components/underlay@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/modal@1.8.0
    *   @spectrum-web-components/underlay@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/modal@1.7.0
    *   @spectrum-web-components/underlay@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/modal@1.6.0
    *   @spectrum-web-components/underlay@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`165a904`]:

    *   @spectrum-web-components/modal@1.5.0
    *   @spectrum-web-components/underlay@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/modal@1.4.0
    *   @spectrum-web-components/underlay@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/modal@1.3.0
    *   @spectrum-web-components/underlay@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **tray:** removed nonNull operator and initialized resolveTransitionPromise with dummy func (#4658) (1a8a479)

**Note:** Version bump only for package @spectrum-web-components/tray

*   **tray** sp-tray now doesn't automatically retract when opened with fewer items in the iOS simulator ([4572] (https://github.com/adobe/spectrum-web-components/issues/4572)) ([56366ce] (https://github.com/adobe/spectrum-web-components/commit/56366ce2750bb4bb5c6e3fa5fe7d809434497adb))

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **tray:** only allow "click" events when they "pointerdown"ed on the Underlay (#4020) (4f9aa4a)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **picker:** ensure the Menu opens in a Tray on mobile (6be2bed)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   centralize updated first focusable selector (300e84c)
*   correct the relationship between overlayWillCloseCallback and phased animations (c63db8d)
*   **dialog:** normalize sizing technique to align with future t-shirt size usage (da33797)
*   leverage "dvh" rather than measured screen height (84b9df0)
*   **tray:** add tray pattern (0915fa5)
*   **tray:** include correct dependency listing (51cb231)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   **picker:** support responsive delivery of menu (20031d1)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tray:** use spectrum tokens (cdd78b2)
*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **tray:** use spectrum tokens (cdd78b2)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   leverage "dvh" rather than measured screen height (84b9df0)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   correct the relationship between overlayWillCloseCallback and phased animations (c63db8d)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **tray:** include correct dependency listing (51cb231)

*   **picker:** support responsive delivery of menu (20031d1)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/tray

*   centralize updated first focusable selector (300e84c)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **dialog:** normalize sizing technique to align with future t-shirt size usage (da33797)

**Note:** Version bump only for package @spectrum-web-components/tray

**Note:** Version bump only for package @spectrum-web-components/tray

*   **tray:** add tray pattern (0915fa5)

 Property  Attribute  Type  Default  Description `hasKeyboardDismissButton``has-keyboard-dismiss``boolean``false` When set, prevents the tray from rendering visually-hidden dismiss helpers. Use this if your slotted content has custom keyboard-accessible dismiss functionality that the auto-detection doesn't recognize. 
By default, the tray automatically detects buttons in slotted content.

`open``open``boolean``false`

Name  Description `default slot` content to display within the Tray

Name  Type  Description `close``Event``Announces that the Tray has been closed.`
