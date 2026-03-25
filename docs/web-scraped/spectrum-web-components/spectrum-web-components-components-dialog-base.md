# Source: https://opensource.adobe.com/spectrum-web-components/components/dialog-base/

Title: Dialog Base: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/dialog-base/

Markdown Content:
`DialogBase` is a foundational class that handles the core functionality of displaying and managing dialog content in an overlay. This base class provides the foundation for more specific dialog implementations like `sp-dialog` and `sp-dialog-wrapper`, handling the core functionality while allowing those implementations to focus on their specific features.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/dialog?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/dialog?style=for-the-badge)

yarn add @spectrum-web-components/dialog
Import the side effectful registration of `<sp-dialog-base>` via:

import '@spectrum-web-components/dialog/sp-dialog-base.js';
When looking to leverage the `DialogBase` base class as a type and/or for extension purposes, do so via:

import { DialogBase } from '@spectrum-web-components/dialog';
The `sp-dialog-base` element is a wrapper that provides animation and positioning for the dialog content.

The dialog base manages several behaviors:

1.   Animation of the dialog content when opening/closing
2.   Focus management when the dialog opens
3.   Event handling for closing the dialog

Use `DialogBase` when:

*   You need to present important information that requires user acknowledgment
*   You're building a modal interface that blocks interaction with the page
*   You need a structured container with features like backdrop/underlay
*   Your content is complex and requires formal layout with headings, content sections, and actions

Use an `sp-popover` when:

*   You need a lightweight, contextual container that's positioned relative to a trigger element
*   You want to display simple content like menus, tooltips, or additional options
*   You're building a non-modal interface where users can still interact with the page
*   You need an element with an arrow/tip pointing to the trigger

<overlay-trigger type="modal">
  <sp-dialog-base underlay slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
      <p>
        The click events for the "OK" button are bound to the story not to the
        components in specific.
      </p>
      <sp-button variant="secondary" treatment="fill" slot="button" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Ok
      </sp-button>
      <sp-checkbox slot="footer">Don't show me this again</sp-checkbox>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
The `underlay` attribute can be used to add an underlay element between the page content and the dialog.

With underlay<overlay-trigger type="modal">
  <sp-dialog-base underlay slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
      <sp-button variant="secondary" treatment="fill" slot="button" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Ok
      </sp-button>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Without underlay<overlay-trigger type="modal">
  <sp-dialog-base slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
      <sp-button variant="secondary" treatment="fill" slot="button" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Ok
      </sp-button>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
The `dismissable` attribute can be used to add an underlay element between the page content and the dialog.

Dismissable<overlay-trigger type="modal">
  <sp-dialog-base dismissable slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Not dismissable<overlay-trigger type="modal">
  <sp-dialog-base underlay slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
      <sp-button variant="secondary" treatment="fill" slot="button" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Ok
      </sp-button>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
The dialog base supports different display modes: `fullscreen` and `fullscreenTakeover`.

Fullscreen<overlay-trigger type="modal">
  <sp-dialog-base mode="fullscreen" slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
      <sp-button variant="secondary" treatment="fill" slot="button" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Ok
      </sp-button>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Fullscreen Takeover<overlay-trigger type="modal">
  <sp-dialog-base mode="fullscreenTakeover" slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
      <sp-button variant="secondary" treatment="fill" slot="button" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Ok
      </sp-button>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
Extend the dialog base to create a new component that uses the same base functionality but with additional features.

`sp-dialog-base` expects a single slotted child element to play the role of the dialog that it will deliver within your application. When leveraging it as a base class be sure to customize the `dialog` getter to ensure that it acquires the appropriate element for your use case in order to correctly pass focus into your content when the dialog is opened.

See `DialogWrapper.ts` for an example component that extends the dialog base.

import { DialogBase } from '@spectrum-web-components/dialog';

export class MyCustomDialogWrapper extends DialogBase {
    public static override get styles(): CSSResultArray {
        return [...super.styles];

    protected override renderDialog(): TemplateResult {
        return html` <my-custom-dialog> <slot></slot> </my-custom-dialog> `;
    }

    protected override get dialog(): Dialog {
        return this.shadowRoot.querySelector('my-custom-dialog') as Dialog;
    }
}
The `heading` slot is of the `sp-dialog` dialog element is used to label the dialog content for screen readers.

The dialog base component ensures proper focus management by:

*   Moving focus into the dialog when opened
*   Trapping tab order within the dialog while open
*   Returning focus to the trigger element when closed

The `receives-focus` attribute can be used to control whether the dialog should receive focus when it is opened. Leverage the `type="modal"` and `receives-focus="auto"` settings in the Overlay API to ensure that focus is thrown into the dialog content when opened and that the tab order will be trapped within it while open.

The `receives-focus` attribute on `overlay-trigger` has three possible values:

*   `auto` (default): Focus will automatically move to the first focusable element in the dialog
*   `true`: Forces focus to move to the overlay content
*   `false`: Prevents focus from moving to the overlay

<overlay-trigger type="modal" receives-focus="true">
  <sp-dialog-base mode="fullscreenTakeover" slot="click-content">
    <sp-dialog>
      <h2 slot="heading">A thing is about to happen</h2>
      <p>Something that might happen a lot is about to happen.</p>
      <sp-button variant="secondary" treatment="fill" slot="button" onclick="this.dispatchEvent(new Event('close', { bubbles: true, composed: true }));" >
        Ok
      </sp-button>
    </sp-dialog>
  </sp-dialog-base>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>

Property  Attribute  Type  Default  Description `dismissable``dismissable``boolean``false``mode``mode``'fullscreen' | 'fullscreenTakeover' | undefined``open``open``boolean``false``responsive``responsive``boolean``false` When set to true, fills screens smaller than 350px high and 400px wide with the full dialog. `underlay``underlay``boolean``false`

Name  Description `default slot` A Dialog element to display.

Name  Type  Description `close``Event``Announces that the dialog has been closed.``undefined``TransitionEvent`
