# Source: https://opensource.adobe.com/spectrum-web-components/components/close-button/

Title: Close Button: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/close-button/

Markdown Content:
An `<sp-close-button>` is a special extension of the `ButtonBase` class that includes icons and styling for buttons used to close a modal or dialog.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/button?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/button?style=for-the-badge)

yarn add @spectrum-web-components/button
Import the side effectful registration of `<sp-close-button>` as follows:

import '@spectrum-web-components/button/sp-clear-button.js';
When looking to leverage the `CloseButton` base class as a type and/or for extension purposes, do so via:

import { ClearButton } from '@spectrum-web-components/button';
The close button is a button with only close icon.

<sp-close-button>Close Dialog</sp-close-button>
The label for an `<sp-close-button>` element can be set via it's default slot or with the `label` attribute. With either method, the label will not be visible but still read by screenreaders.

Default slot<sp-close-button>Close</sp-close-button>Label attribute<sp-close-button label="Close"></sp-close-button>Small<sp-close-button size="s">Small</sp-close-button>Medium<sp-close-button size="m">Medium</sp-close-button>Large<sp-close-button size="l">Large</sp-close-button>Extra Large<sp-close-button size="xl">Extra Large</sp-close-button>
In addition to the variant, the `<sp-close-button>` element supports a disabled state, which can be applied by adding the attribute `disabled`.

While disabled, the `<sp-close-button>` element will not respond to click events and will appear faded.

<sp-button-group>
  <sp-close-button>Normal</sp-close-button>
  <sp-close-button disabled>Disabled</sp-close-button>
</sp-button-group>
Events handlers for clicks and other user actions can be registered on a `<sp-close-button>` as one would on a standard HTML `<button>` element.

<sp-close-button onclick="spAlert(this, '<sp-close-button> clicked!')">
  Click me
</sp-close-button>
The `autofocus` attribute sets focus on the `<sp-close-button>` when the component mounts. This is useful for setting focus to a specific `sp-close-button` when a popover or dialog opens.

<sp-button id="trigger">Open</sp-button>
<sp-overlay trigger="trigger@click" placement="bottom">
  <sp-popover>
    
    <sp-close-button autofocus>Close</sp-close-button>
  </sp-popover>
</sp-overlay>
A button is required to have either text in the default slot or a `label` attribute on the `<sp-close-button>`.

Property  Attribute  Type  Default  Description `active``active``boolean``false``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `staticColor``static-color``'black' | 'white' | undefined``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `type``type``'button' | 'submit' | 'reset'``'button'` The default behavior of the button. Possible values are: `button` (default), `submit`, and `reset`. `variant``variant``ButtonStaticColors | ''``''` The visual variant to apply to this button.

Name  Description `default slot` text label of the Close Button `icon` icon element(s) to display at the start of the button

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1

*   #5881`50ad026` Thanks @cdransf! - Added visually hidden default slot rendering to sp-close-button so text content is accessible to screen readers while remaining invisible to sighted users.

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   **action-bar:** use core tokens (4e21edf)

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   prevent default hoisting of custom pseudo elements (7f66346)

*   **close-button:** add Close Button pattern (8e9e1ad)
*   **close-button:** use core tokens (e6a4efe)
*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   prevent default hoisting of custom pseudo elements (7f66346)

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   include all Dev Mode files in side effects (f70817c)

*   **close-button:** use core tokens (e6a4efe)

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

**Note:** Version bump only for package @spectrum-web-components/close-button

*   **close-button:** add Close Button pattern (8e9e1ad)
