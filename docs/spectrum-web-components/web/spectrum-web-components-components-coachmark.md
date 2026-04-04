# Source: https://opensource.adobe.com/spectrum-web-components/components/coachmark/

Title: Coachmark: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/coachmark/

Markdown Content:
`<sp-coachmark>` is a temporary message that educates users through new or unfamiliar product experiences. They can be chained into a sequence to form a tour.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/coachmark?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/coachmark?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/coachmark

Import the side effectful registration of `<sp-coachmark>` via:

import '@spectrum-web-components/coachmark/sp-coachmark.js';

When looking to leverage the `Coachmark` base class as a type and/or for extension purposes, do so via:

import { Coachmark } from '@spectrum-web-components/coachmark';

The coachmark consists of several key parts:

*   A title (via `slot="title"`)
*   Content (via `slot="content"`)
*   Optional action menu (via `slot="actions"`)
*   Optional media content (via `slot="asset"` or `src` attribute)
*   Navigation controls (via `primary-cta` and `secondary-cta` attributes)
*   Tour progress indicators (via `current-step` and `total-steps` attributes)
*   Optional keyboard shortcuts (via `modifierKeys` and `shortcutKey` properties)

Here's a complete example showing the anatomy:

<sp-coachmark current-step="2" total-steps="8" open primary-cta="Next" secondary-cta="Previous">
  
  <div slot="title">Welcome to the Tour</div>

  
  <div slot="content">
    This coachmark demonstrates the various parts that make up the component.
  </div>

  
  <img slot="asset" src="https://picsum.photos/id/237/200/300" alt="Feature demonstration" />

  
  <sp-action-menu slot="actions" label="More Actions" placement="bottom-end" quiet >
    <sp-menu-item>Skip tour</sp-menu-item>
    <sp-menu-item>Restart tour</sp-menu-item>
  </sp-action-menu>
</sp-coachmark>Navigation
The `primary-cta` and `secondary-cta` attributes are used to display navigation buttons.

<sp-coachmark id="coachmark-navigation" open primary-cta="Next" secondary-cta="Previous">
  <div slot="title">Coachmark with navigation</div>
  <div slot="content">This coachmark demonstrates the navigation buttons.</div>
  
  <sp-action-menu slot="actions" label="More Actions" placement="bottom-end" quiet >
    <sp-menu-item>Skip tour</sp-menu-item>
    <sp-menu-item>Restart tour</sp-menu-item>
  </sp-action-menu>
</sp-coachmark>Progress Indicator
The `current-step` and `total-steps` attributes are used to display a progress indicator.

<sp-coachmark id="coachmark-progress" open current-step="2" total-steps="8" primary-cta="Next" secondary-cta="Previous">
  <div slot="title">Coachmark with progress indicator</div>
  <div slot="content">This coachmark demonstrates the progress indicator.</div>
  
  <sp-action-menu slot="actions" label="More Actions" placement="bottom-end" quiet >
    <sp-menu-item>Skip tour</sp-menu-item>
    <sp-menu-item>Restart tour</sp-menu-item>
  </sp-action-menu>
</sp-coachmark>Keyboard Shortcuts
The `shortcut-key` is the primary key used to trigger an interaction and are typically an alphanumeric value (and thus will be rendered as an uppercase character).

<sp-coachmark open current-step="2" total-steps="8" primary-cta="Next" secondary-cta="Previous" shortcut-key="⌘">
    <div slot="title">Shortcut Key</div>
    <div slot="content">This coachmark demonstrates the shortcut key.</div>

    
    <sp-action-menu slot="actions" label="More Actions" placement="bottom-end" quiet >
        <sp-menu-item>Skip tour</sp-menu-item>
        <sp-menu-item>Restart tour</sp-menu-item>
    </sp-action-menu>
</sp-coachmark>Modifier Keys
The `modifierKeys` is an array of modifier keys used to trigger an interaction. This is not an attribute, but a property so we need to set it via JavaScript.

<sp-coachmark open current-step="2" total-steps="8" primary-cta="Next" secondary-cta="Previous" id="coachmark-keys">
    <div slot="title">Coachmark with modifier keys</div>
    <div slot="content">This coachmark demonstrates the modifier keys.</div>
    
    <sp-action-menu slot="actions" label="More Actions" placement="bottom-end" quiet >
        <sp-menu-item>Skip tour</sp-menu-item>
        <sp-menu-item>Restart tour</sp-menu-item>
    </sp-action-menu>
</sp-coachmark>
<script type="module"> const initCoachMark = () => { const coachmark = document.querySelector('#coachmark-keys'); const modifierKeys = ['⇧ Shift', '⌘']; coachmark.modifierKeys = modifierKeys; }; customElements.whenDefined('code-example').then(() => { customElements.whenDefined('sp-coachmark').then(() => { initCoachMark(); }); });</script>
User action-dependent coachmarks are designed to guide users based on their interactions within your application. In such cases, there is no "Next Step" button, as the coachmark progresses when the user takes a specific action. This allows users to learn by doing, rather than simply reading instructions. The coachmark remains until the user performs the required action or takes an alternative route in the tour, such as skipping, restarting, or moving back to a previous step.

Inside the `<sp-coachmark>`, add the content and instructions for the coachmark in the `<sp-coachmark>`. You can also define primary and secondary CTA buttons for user interaction.

<sp-coachmark id="coachmark-action" open current-step="2" total-steps="8" primary-cta="Asset added" secondary-cta="Previous">
  <div slot="title">Coachmark with user action</div>
  <div slot="content">
    This coachmark waits for the user to complete a specific action.
  </div>
  <sp-action-menu label="More Actions" placement="bottom-end" quiet slot="actions" >
    <sp-menu-item>Skip tour</sp-menu-item>
    <sp-menu-item>Restart tour</sp-menu-item>
  </sp-action-menu>
</sp-coachmark>
Coachmarks should be designed with accessibility in mind:

*   Always provide clear, concise title and content text
*   Use descriptive labels for navigation buttons
*   Ensure keyboard navigation works for multi-step tours
*   Make sure images have appropriate alt text
*   Consider focus management during tour progression

For users that rely on screen readers, coachmarks announce their presence and content appropriately. The component manages focus to ensure users can navigate through the tour using only a keyboard.

*   Updated dependencies []: 
    *   @spectrum-web-components/asset@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/button-group@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/popover@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/asset@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/button-group@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/popover@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5900`283f0fe` Thanks @TarunAdobe! - Added missing dependencies to the package.json files of several components to align with their usage in source code.

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]:

    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/popover@1.11.0
    *   @spectrum-web-components/asset@1.11.0
    *   @spectrum-web-components/button-group@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/asset@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/button-group@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/asset@1.9.1
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/button-group@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`, `7d23140`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/button-group@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/asset@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/button-group@1.8.0
    *   @spectrum-web-components/asset@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/asset@1.7.0
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/button-group@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`00eb0a8`]: 
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/button-group@1.6.0
    *   @spectrum-web-components/asset@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`165a904`, `4e06533`]: 
    *   @spectrum-web-components/asset@1.5.0
    *   @spectrum-web-components/button-group@1.5.0
    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/asset@1.4.0
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/button-group@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/button-group@1.3.0
    *   @spectrum-web-components/asset@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   add an optional chromatic vrt action (7d2f840)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   remove 'variant' and 'static' attributes from coach-indicator (#4772)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   **coachmark,overlay:** adjust imports of overlay and coachmark (#4455) (39706da)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   **coachmark:** add "step-count" slot for custom/internationalized pagination content (#4215) (f4136a6)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   **coachmark:** rename "sp-coachmark" to "sp-coachmark-indicator", add "sp-coachmark" (#3639) (a94389c)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **coachmark:** add coachmark pattern (f53ae70)
*   **coachmark:** update spectrum css input (a099ee6)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   leverage latest Spectrum button API (9faeade)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   leverage latest Spectrum button API (9faeade)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **coachmark:** update spectrum css input (a099ee6)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **coachmark:** update spectrum css input (a099ee6)

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/coachmark

*   use "sideEffects" listing in package.json (7271614)

*   **coachmark:** add coachmark pattern (f53ae70)

Property  Attribute  Type  Default  Description `asset``asset``'file' | 'folder' | undefined``currentStep``current-step``number | undefined``hasAsset``has-asset``boolean``false``item``item``CoachmarkItem | undefined``modifierKeys``modifierKeys``string[] | undefined``[]``open``open``boolean``false` Whether the popover is visible or not. `placement``placement``"top" | "top-start" | "top-end" | "right" | "right-start" | "right-end" | "bottom" | "bottom-start" | "bottom-end" | "left" | "left-start" | "left-end"``'right'``primaryCTA``primary-cta``string | undefined``secondaryCTA``secondary-cta``string | undefined``tip``tip``boolean``false``totalSteps``total-steps``number | undefined`

Name  Description `actions` an `sp-action-menu` element outlining actions to take on the represened object `cover-photo` This is the cover photo for Default and Quiet Coachmark `description` A description of the card `heading` HTML content to be listed as the heading `step-count` Override the default pagination delivery with your own internationalized content `default slot` content to display within the Popover

Name  Type  Description `primary``Event``Announces that the "primary" button has been clicked.``secondary``Event``Announces that the "secondary" button has been clicked.`
