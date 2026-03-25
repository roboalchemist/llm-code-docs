# Source: https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/

Title: Dialog Wrapper: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/dialog-wrapper/

Markdown Content:
`sp-dialog-wrapper` supplies an attribute-based interface for the managed customization of an sp-dialog element and the light DOM supplied to it. This is paired it with an `underlay` attribute that opts-in to the use of an `sp-underlay` element between your page content and the `sp-dialog` that opens over it.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/dialog?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/dialog?style=for-the-badge)

yarn add @spectrum-web-components/dialog
Import the side effectful registration of `<sp-dialog-wrapper>` via:

import '@spectrum-web-components/dialog/sp-dialog-wrapper.js';
The dialog wrapper is a high-level component that combines the `sp-dialog-base` functionality and the `sp-dialog` layout and stylingwith an attribute-based API.

The dialog wrapper consists of several key parts:

*   A headline used as the dialog title (via the `headline` attribute)
*   Content (via default slot)
*   Optional hero content (via the `hero` attribute)
*   Optional footer content (via the `footer` attribute)
*   Optional underlay (via the `underlay` attribute)
*   Optional buttons (via the `confirm-label`, `cancel-label`, and `secondary-label` attributes)
*   Optional dismiss button (via the `dismissable` attribute and the `dismiss-label` attribute)

<overlay-trigger type="modal">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" hero="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII" confirm-label="Confirm" cancel-label="Cancel" secondary-label="Secondary" underlay footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
The dialog wrapper supports different sizes via the `size` attribute: `s`, `m`, `l`.

Small<overlay-trigger type="modal">
  <sp-dialog-wrapper size="s" slot="click-content" headline="Dialog title" dismissable dismiss-label="Close" underlay footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Medium<overlay-trigger type="modal">
  <sp-dialog-wrapper size="m" slot="click-content" headline="Dialog title" dismissable dismiss-label="Close" underlay footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Large<overlay-trigger type="modal">
  <sp-dialog-wrapper size="l" slot="click-content" headline="Dialog title" dismissable dismiss-label="Close" underlay footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
The `underlay` attribute can be used to add an underlay element between the page content and the dialog.

With underlay<overlay-trigger type="modal">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" dismissable dismiss-label="Close" underlay footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Without underlay<overlay-trigger type="modal">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" dismissable dismiss-label="Close" footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
The `dismissable` attribute can be used to add an underlay element between the page content and the dialog.

Dismissable<overlay-trigger type="modal">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" dismissable dismiss-label="Close" underlay footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Not dismissable<overlay-trigger type="modal">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" underlay footer="Content for footer" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
The dialog wrapper supports different display modes:

Fullscreen<overlay-trigger type="modal">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" cancel-label="Cancel" underlay footer="Content for footer" mode="fullscreen" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>Fullscreen Takeover<overlay-trigger type="modal">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" cancel-label="Cancel" underlay footer="Content for footer" mode="fullscreenTakeover" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>
An sp-dialog-wrapper element leverages the headline attribute/property to label the dialog content for screen readers. The headline-visibility attribute will accept a value of "none" to suppress the headline visually.

The dialog wrapper component ensures proper focus management by:

*   Moving focus into the dialog when opened
*   Trapping tab order within the dialog while open
*   Returning focus to the trigger element when closed

The `receives-focus` attribute can be used to control whether the dialog should receive focus when it is opened. Leverage the `type="modal"` and `receives-focus="auto"` settings in the Overlay API to ensure that focus is thrown into the dialog content when opened and that the tab order will be trapped within it while open.

The `receives-focus` attribute on `overlay-trigger` has three possible values:

*   `auto` (default): Focus will automatically move to the first focusable element in the dialog
*   `true`: Forces focus to move to the overlay content
*   `false`: Prevents focus from moving to the overlay

For accessible dialogs, always use `receives-focus="auto"` or `receives-focus="true"` to ensure keyboard users can interact with the dialog content.

<overlay-trigger type="modal" receives-focus="true">
  <sp-dialog-wrapper slot="click-content" headline="Dialog title" dismissable dismiss-label="Close" underlay footer="Content for footer" mode="fullscreenTakeover" >
    Content of the dialog
  </sp-dialog-wrapper>
  <sp-button slot="trigger" variant="primary">Toggle Dialog</sp-button>
</overlay-trigger>

Property  Attribute  Type  Default  Description `cancelLabel``cancel-label``string``''``confirmLabel``confirm-label``string``''``dismissLabel``dismiss-label``string``'Close'``dismissable``dismissable``boolean``false``error``error``boolean``false``footer``footer``string``''``headline``headline``string``''``headlineVisibility``headline-visibility``'none' | undefined``hero``hero``string``''``heroLabel``hero-label``string``''``mode``mode``'fullscreen' | 'fullscreenTakeover' | undefined``noDivider``no-divider``boolean``false``open``open``boolean``false``responsive``responsive``boolean``false` When set to true, fills screens smaller than 350px high and 400px wide with the full dialog. `secondaryLabel``secondary-label``string``''``size``size``'s' | 'm' | 'l' | undefined``underlay``underlay``boolean``false`

Name  Description `default slot` content for the dialog

Name  Type  Description `cancel``Event``Announces that the "cancel" button has been clicked.``close``Event``Announces that the dialog has been closed.``confirm``Event``Announces that the "confirm" button has been clicked.``secondary``Event``Announces that the "secondary" button has been clicked.``undefined``TransitionEvent`
