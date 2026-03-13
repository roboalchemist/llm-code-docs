# Source: https://opensource.adobe.com/spectrum-web-components/components/clear-button/

Title: Clear Button: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/clear-button/

Markdown Content:
An `<sp-clear-button>` is a special extension of the `ButtonBase` class that includes icons and styling for buttons used to clear a form.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/button?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/button?style=for-the-badge)

yarn add @spectrum-web-components/button
Import the side effectful registration of `<sp-clear-button>` as follows:

import '@spectrum-web-components/button/sp-clear-button.js';
When looking to leverage the `ClearButton` base class as a type and/or for extension purposes, do so via:

import { ClearButton } from '@spectrum-web-components/button';
The clear button is a button with only a close icon.

<sp-clear-button label="Reset"></sp-clear-button>
An accessible label for an `<sp-clear-button>` must be provided using the `label` attribute. This sets the `aria-label` for screen readers. Unlike other button types, the clear button only displays an icon and does not render slot content, so the `label` attribute is the only way to provide an accessible name.

<sp-clear-button label="Clear"></sp-clear-button>
The `label` attribute is required and will be set as the `aria-label` on the element.

Small<sp-clear-button size="s" label="Clear"></sp-clear-button>Medium<sp-clear-button size="m" label="Clear"></sp-clear-button>Large<sp-clear-button size="l" label="Clear"></sp-clear-button>Extra Large<sp-clear-button size="xl" label="Clear"></sp-clear-button>
The `quiet` attribute will render the `<sp-clear-button>` as a quiet button. This is useful for cases where you want to use the clear button in a more subtle way.

<sp-clear-button quiet label="Clear content"></sp-clear-button>
The `static-color` attribute will render the `<sp-clear-button>` with a static color. This is useful for cases where the button appears on a dark background texture. This is a replacement for the previously used `variant="overBackground"` attribute which is deprecated.

<sp-clear-button static-color="white" label="Clear content"></sp-clear-button>
In addition to the variant, the `<sp-clear-button>` elements supports a disabled state, which can be applied by adding the attribute `disabled`.

While disabled, the `<sp-clear-button>` element will not respond to click events and will appear faded.

<sp-button-group>
  <sp-clear-button label="Clear"></sp-clear-button>
  <sp-clear-button label="Clear" disabled></sp-clear-button>
</sp-button-group>
Events handlers for clicks and other user actions can be registered on a `<sp-clear-button>` as one would on a standard HTML `<button>` element.

<sp-clear-button label="Click me" onclick="spAlert(this, '<sp-clear-button> clicked!')"></sp-clear-button>
The `autofocus` attribute sets focus on the `<sp-clear-button>` when the component mounts. This is useful for setting focus to a specific sp-clear-button when a popover or dialog opens.

<sp-button id="trigger">Open</sp-button>
<sp-overlay trigger="trigger@click" placement="bottom">
  <sp-popover>
    
    <sp-clear-button label="Clear" autofocus></sp-clear-button>
  </sp-popover>
</sp-overlay>
A button is required to have a `label` attribute on the `<sp-clear-button>` to provide an accessible name for screen readers. The `label` attribute sets the `aria-label` property, ensuring the button is properly announced to assistive technologies.

Property  Attribute  Type  Default  Description `active``active``boolean``false``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. This attribute is required for clear buttons. `quiet``quiet``boolean``false``referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `staticColor``static-color``'white' | undefined` The visual variant to apply to this button. `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `type``type``'button' | 'submit' | 'reset'``'button'` The default behavior of the button. Possible values are: `button` (default), `submit`, and `reset`. `variant``variant``'overBackground' | undefined` The visual variant to apply to this button.

Name  Description `default slot` text content to be displayed in the Button element `icon` icon element(s) to display at the start of the button

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0

*   #5320`15be17d` Thanks @renovate! - Clear button styles have been updated to the latest Spectrum CSS version of the clear button. This update includes a major reduction in the number of custom property abstractions needed to support the multiple theming layers (as seen in the `styles` package).

This update spans the following additional packages:

    *   @spectrum-web-components/button
    *   @spectrum-web-components/styles

As the updated styles now offer additional styling options, we have added the following API to the clear button component that exists in the `button` package:

    *   `quiet` - when set to true, the button will be rendered as a quiet button. This is useful for cases where you want to use the clear button in a more subtle way.
    *   `disabled` - when set to true, the button will be rendered as a disabled button.
    *   `static-color` - currently this only supports the `white` context color. This is useful for cases where the button appears on a dark background texture. This is a replacement for the previously used `variant="overBackground"` attribute which is deprecated.

The `variant="overBackground"` attribute is deprecated; please use the new `static-color="white"` attribute instead. When this property is used in the component, a deprecation warning will be shown in the console when in debug mode. The `variant` attribute will be removed in a future release.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   **search:** clear button ui in express (#4910) (f88e1e2)

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

*   **clear-button:** migrate to core tokens (64be98a)

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

*   prevent default hoisting of custom pseudo elements (7f66346)

*   include all Dev Mode files in side effects (f70817c)
*   leverage latest Spectrum button API (9caf2f6)

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

*   prevent default hoisting of custom pseudo elements (7f66346)

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

**Note:** Version bump only for package @spectrum-web-components/clear-button

*   leverage latest Spectrum button API (9caf2f6)
