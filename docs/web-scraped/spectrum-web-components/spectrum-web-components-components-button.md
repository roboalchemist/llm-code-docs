# Source: https://opensource.adobe.com/spectrum-web-components/components/button/

Title: Button: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/button/

Markdown Content:
An `<sp-button>` represents an action a user can take. sp-buttons can be clicked or tapped to perform an action or to navigate to another page. Buttons in Spectrum have several variations for different uses and multiple levels of loudness for various attention-getting needs.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/button?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/button?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/button
Import the side effectful registration of `<sp-button>` as follows:

import '@spectrum-web-components/button/sp-button.js';
When looking to leverage the `Button` base classes as a type and/or for extension purposes, do so via:

import { Button } from '@spectrum-web-components/button';<sp-button>Try me</sp-button>
`<sp-button>` elements can be provided a visible label, a label and an icon, or just an icon.

An icon is provided by placing an icon element in the `icon` slot.

If the button is `icon-only`, a non-visible label can be provided via the `label` attribute on an `<sp-button>` or on an `<sp-icon*>` element child to appropriately fulfill the accessibility contract of the button.

Label only<sp-button variant="primary">Label only</sp-button>Icon + label<sp-button variant="primary">
  <sp-icon-help slot="icon"></sp-icon-help>
  Icon + Label
</sp-button>SVG Icon + label<sp-button variant="primary">
  <svg slot="icon" viewBox="0 0 36 36" focusable="false" aria-hidden="true" role="img" >
    <path d="M16 36a4.407 4.407 0 0 0 4-4h-8a4.407 4.407 0 0 0 4 4zm9.143-24.615c0-3.437-3.206-4.891-7.143-5.268V3a1.079 1.079 0 0 0-1.143-1h-1.714A1.079 1.079 0 0 0 14 3v3.117c-3.937.377-7.143 1.831-7.143 5.268C6.857 26.8 2 26.111 2 28.154V30h28v-1.846C30 26 25.143 26.8 25.143 11.385z" ></path>
  </svg>
  SVG Icon + Label
</sp-button>Icon only<sp-button variant="primary" icon-only label="Icon only">
  <sp-icon-help slot="icon"></sp-icon-help>
</sp-button>Small<sp-button size="s">Small</sp-button>Medium<sp-button size="m">Medium</sp-button>Large<sp-button size="l">Large</sp-button>Extra Large<sp-button size="xl">Extra Large</sp-button>
There are many button variants to choose from in Spectrum. The `variant` attribute defaults to `accent`, but also accepts the following value: `accent`, `primary`, `secondary`, `negative`. They display as follows:

Accent<sp-button-group style="min-width: max-content">
  <sp-button variant="accent">Label only</sp-button>
  <sp-button variant="accent">
    <sp-icon-help slot="icon"></sp-icon-help>
    Icon + Label
  </sp-button>
  <sp-button variant="accent" label="Icon only" icon-only>
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-button>
</sp-button-group>Primary<sp-button-group style="min-width: max-content">
  <sp-button variant="primary">Label only</sp-button>
  <sp-button variant="primary">
    <sp-icon-help slot="icon"></sp-icon-help>
    Icon + Label
  </sp-button>
  <sp-button variant="primary" label="Icon only" icon-only>
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-button>
</sp-button-group>Secondary<sp-button-group style="min-width: max-content">
  <sp-button variant="secondary">Label only</sp-button>
  <sp-button variant="secondary">
    <sp-icon-help slot="icon"></sp-icon-help>
    Icon + Label
  </sp-button>
  <sp-button variant="secondary" label="Icon only" icon-only>
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-button>
</sp-button-group>Negative<sp-button-group style="min-width: max-content">
  <sp-button variant="negative">Label only</sp-button>
  <sp-button variant="negative">
    <sp-icon-help slot="icon"></sp-icon-help>
    Icon + Label
  </sp-button>
  <sp-button variant="negative" label="Icon only" icon-only>
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-button>
</sp-button-group>
The `treatment` attribute accepts `fill` and `outline` as values, and defaults to `fill`. These display as follows:

Fill<sp-button-group style="min-width: max-content">
  <sp-button treatment="fill" variant="primary">Primary, Fill</sp-button>
  <sp-button treatment="fill" variant="secondary">Secondary, Fill</sp-button>
  <sp-button treatment="fill" variant="negative">Negative, Fill</sp-button>
</sp-button-group>Outline<sp-button-group style="min-width: max-content">
  <sp-button treatment="outline" variant="primary">Primary, Outline</sp-button>
  <sp-button treatment="outline" variant="secondary">
    Secondary, Outline
  </sp-button>
  <sp-button treatment="outline" variant="negative">
    Negative, Outline
  </sp-button>
</sp-button-group>Outline, black<sp-button-group style="background: var(--spectrum-seafoam-600); padding: 0.5em; min-width: max-content">
  <sp-button treatment="outline" static-color="black">Label only</sp-button>
  <sp-button treatment="outline" static-color="black">
    <sp-icon-help slot="icon"></sp-icon-help>
    Icon + Label
  </sp-button>
  <sp-button treatment="outline" static-color="black" label="Icon only" icon-only >
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-button>
</sp-button-group>Outline, white<sp-button-group style="background: var(--spectrum-seafoam-600); padding: 0.5em; min-width: max-content">
  <sp-button treatment="outline" static-color="white">Label only</sp-button>
  <sp-button treatment="outline" static-color="white">
    <sp-icon-help slot="icon"></sp-icon-help>
    Icon + Label
  </sp-button>
  <sp-button treatment="outline" static-color="white" label="Icon only" icon-only >
    <sp-icon-help slot="icon"></sp-icon-help>
  </sp-button>
</sp-button-group>
In addition to the variant, `<sp-button>` elements support two different visual states, disabled and pending, which can be applied by adding the attribute `disabled` or `pending` respectively. All `<sp-button>` variants support these states.

While disabled, `<sp-button>` elements will not respond to click events and will appear faded.

<sp-button-group>
  <sp-button variant="primary">Normal</sp-button>
  <sp-button variant="primary" disabled>Disabled</sp-button>
</sp-button-group>
While in pending state, `<sp-button>` elements will not respond to click events and will appear faded with an indeterminate `<sp-progress-circle>`. The `<sp-button>` element's label and icon will be hidden while in pending state.

Note: The pending state of the `<sp-button>` element is applied after a 1s delay to avoid flashing the pending state for quick actions. You can override the delay by adding custom css var `--pending-delay` to your css.

<sp-button-group>
  <sp-button variant="primary">Normal</sp-button>
  <sp-button variant="primary" pending>Pending</sp-button>
</sp-button-group>
Events handlers for clicks and other user actions can be registered on a `<sp-button>` as one would on a standard HTML `<button>` element.

<sp-button onclick="spAlert(this, '<sp-button> clicked!')">Click me</sp-button>
> **Deprecated**: The `href`, `target`, `download`, `referrerpolicy`, and `rel` attributes on `<sp-button>` are deprecated and will be removed in a future release. Use a native HTML anchor (`<a>`) element with the `spectrum-Button` class instead.

Using `<sp-button href="...">` conflates button and link semantics, which creates accessibility issues: screen reader users navigating by form controls will not find link-styled buttons, and vice versa. Native HTML elements provide correct semantics by default.

If you intend to create a link with a `href` attribute, we instead offer CSS classes for creating button-styled links. To migrate, import the global elements stylesheet and apply button classes to native `<a>` elements:

@import '@spectrum-web-components/styles/global-elements.css';
**Before (deprecated):**

<sp-button href="https://opensource.adobe.com/spectrum-web-components">
  Visit docs
</sp-button>
**After (recommended):**

<a class="spectrum-Button spectrum-Button--accent" href="https://opensource.adobe.com/spectrum-web-components">
  Visit docs
</a>
See the accessibility section for more details.

The `autofocus` attribute sets focus on the `<sp-button>` when the component mounts. This is useful for setting focus to a specific sp-button when a popover or dialog opens.

<sp-button id="trigger">Open</sp-button>
<sp-overlay trigger="trigger@click" placement="bottom">
  <sp-popover>
    
    <sp-button autofocus>Confirm</sp-button>
  </sp-popover>
</sp-overlay>
A button is required to have either a visible text label or a `label` attribute on either the `<sp-button>` itself or on an `<sp-icon*>` element child.

Do not use custom colors for buttons. The colors of different button variations have been designed to be consistent and accessible.

> **Deprecated**: The `href` attribute and other link-related properties (`target`, `download`, `referrerpolicy`, `rel`) on `<sp-button>` are deprecated and will be removed in a future release.

You may use a native link with classes to style it like a button. Refer to the Storybook examples that include `href` for the appropriate classes to use.

For styles to be fully available to slotted links, you must include the stylesheet for `@spectrum-web-components/styles/global-elements.css`.

To successfully receive button styling, the link must be one of the following:

*   A direct child of `<sp-theme>`
*   A slotted child of a component within `<sp-theme>`

To allow button-styled native links in the shadow DOM of extended components, ensure their stylesheet also imports `@spectrum-web-components/styles/global-elements.css`.

**Note**: native button-styled links do not support disabled or pending states.

<a class="spectrum-Button spectrum-Button--accent" href="https://github.com/adobe/spectrum-web-components">
  Accent link button
</a>
<a class="spectrum-Button spectrum-Button--secondary spectrum-Button--outline" href="https://github.com/adobe/spectrum-web-components">
  
  <sp-icon-help slot="icon"></sp-icon-help>
  Secondary outline link button
</a>
A screen reader user will not encounter href buttons when navigating by buttons or form controls. While they can both be used in the same page, problems could occur if mixing the types in close proximity to each other.

To ensure maximum contrast with the background, use static black for light backgrounds and images, and static white for dark backgrounds and images. Avoid placing static components on top of busy images with a lot of variance in contrast.

Static black on light background<div style="background-color: var(--spectrum-docs-static-black-background-color); padding: 20px">
  <sp-button static-color="black">Click me</sp-button>
  <sp-button static-color="black" treatment="outline">Click me</sp-button>
</div>Static white on dark background<div style="background-color: var(--spectrum-docs-static-white-background-color); padding: 20px">
  <sp-button static-color="white">Click me</sp-button>
  <sp-button static-color="white" treatment="outline">Click me</sp-button>
</div>
Make sure that a button’s label clearly states the outcome of the action. Use the same word or phrase as found elsewhere in the experience.

*   Updated dependencies []: 
    *   @spectrum-web-components/progress-circle@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/clear-button@1.11.2
    *   @spectrum-web-components/close-button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/progress-circle@1.11.1
    *   @spectrum-web-components/clear-button@1.11.1
    *   @spectrum-web-components/close-button@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`b95e254`, `f8bdeec`, `50ad026`, `9cb816b`]: 
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/close-button@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/progress-circle@1.11.0
    *   @spectrum-web-components/clear-button@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/clear-button@1.10.0
    *   @spectrum-web-components/close-button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/progress-circle@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/clear-button@1.9.1
    *   @spectrum-web-components/close-button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/progress-circle@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5730`7d23140` Thanks @caseyisonit! - - **Fixed**: Aria-label handling in `<sp-button>` component.

    *   **Fixed**: Moved aria-label updates to occur after slot content changes are processed to prevent timing issues
    *   **Added**: Enhanced `label` property support for programmatic aria-label control
    *   **Added**: Comprehensive tests for aria-label behavior during content and pending state changes
    *   **Fixed**: Removed duplicate aria-label update logic in `update()` method

These changes ensure that aria-labels are properly managed and preserved across component state changes, improving accessibility for screen reader users.

*   Updated dependencies [`7d23140`, `7d23140`]:

    *   @spectrum-web-components/progress-circle@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/clear-button@1.9.0
    *   @spectrum-web-components/close-button@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   #5320`15be17d` Thanks @renovate! - Clear button styles have been updated to the latest Spectrum CSS version of the clear button. This update includes a major reduction in the number of custom property abstractions needed to support the multiple theming layers (as seen in the `styles` package).

This update spans the following additional packages:

    *   @spectrum-web-components/button
    *   @spectrum-web-components/styles

As the updated styles now offer additional styling options, we have added the following API to the clear button component that exists in the `button` package:

    *   `quiet` - when set to true, the button will be rendered as a quiet button. This is useful for cases where you want to use the clear button in a more subtle way.
    *   `disabled` - when set to true, the button will be rendered as a disabled button.
    *   `static-color` - currently this only supports the `white` context color. This is useful for cases where the button appears on a dark background texture. This is a replacement for the previously used `variant="overBackground"` attribute which is deprecated.

The `variant="overBackground"` attribute is deprecated; please use the new `static-color="white"` attribute instead. When this property is used in the component, a deprecation warning will be shown in the console when in debug mode. The `variant` attribute will be removed in a future release.

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/clear-button@1.8.0
    *   @spectrum-web-components/close-button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/progress-circle@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/clear-button@1.7.0
    *   @spectrum-web-components/close-button@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/progress-circle@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5174`00eb0a8` Thanks @Rajdeepc! - Updated the deprecation warning to allow `variant` and `static-color` exist on the same component. Added `primary` and `secondary` stories to `white` and `black` button directories on storybook. Updates documentation site to reflect this as well.
*   Updated dependencies [`a9727d2`]: 
    *   @spectrum-web-components/close-button@1.6.0
    *   @spectrum-web-components/clear-button@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/progress-circle@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5363`4e06533` Thanks @castastrophe!

Adjust S1/Express static outline variant content color (from transparent-black/white to solid black/white) to fix unintentional regression.

From @spectrum-css/button v14.1.6: #3665 Thanks @rise-erpelding!

This update aims to simplify `--mod-*` access by ensuring local variants and states aren't hooking into those custom properties for overrides. This updates all local variants and states to override the `--spectrum-button-*` properties instead and adjusts the specificity to ensure no regressions in rendered results.

From @spectrum-css/button v14.1.3: #3613 Thanks @​rise-erpelding!

Adjusts static color buttons to more closely resemble the S2 specifications. There are no expected changes to non-static button variants in S2, and no expected changes to other themes.

This PR includes changes to:

    *   Static white primary button (outline variant), static white secondary button (fill variant), static black primary button (outline variant), static black secondary button (fill variant)
    *   Static white secondary button (outline variant) and static black secondary button (outline variant) border and background colors
    *   Static color buttons' content color
    *   Static white primary button (fill variant) and static black primary button (fill variant) background colors

From @spectrum-css/button v14.1.2: #​3600 Thanks @​rise-erpelding!

Adjust border colors for static black and static white outline buttons, primary variant to match S2 specifications.

*   Updated dependencies []:

    *   @spectrum-web-components/clear-button@1.5.0
    *   @spectrum-web-components/close-button@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/progress-circle@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/clear-button@1.4.0
    *   @spectrum-web-components/close-button@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/progress-circle@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/clear-button@1.3.0
    *   @spectrum-web-components/close-button@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/progress-circle@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)
*   **overlay:** make :focus-visible consistent when using overlay type modal (#4912) (7a5f786), closes #5021

*   **action-button:** action-button with href can be perceived by screen reader (#4927) (2a0b3a5)

**Note:** Version bump only for package @spectrum-web-components/button

*   remove deprecated 'static' references (#4818)

*   add `static-color` to replace `static` (#4808) (43cf086)
*   **button:** add noWrap property (#4779) (6760ec2)

**Note:** Version bump only for package @spectrum-web-components/button

*   **reactive-controller:** new pending state controller (#4605) (68baf94)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   **shared:** ensure the "updateComplete" in Focusable is stable (885b4a5)

*   **button:** prevent pointer interaction of child/slotted content (2cd5823)
*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **button:** add missing progress-circle dependency (#4086) (2dfeeb3)

*   **progress-circle:** ensure size can be applied to non-"size" attribute bearing elements (2bc1065)

*   **icon:** use core tokens (a11ef6b)

*   **button:** use larger icons in Close Button (c4aa02c)

*   **shared:** update and expand attribute coverage in likeAnchor (5cb5f1d)

*   **button:** adds pending button, fixes #3162 (#3163) (71254ec)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** support [icon-only] delivery (#3716) (e236a50)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   handle longpress and over filter overlays (483e52d)

**Note:** Version bump only for package @spectrum-web-components/button

*   **action-bar:** use core tokens (4e21edf)

*   added role for href button (5a4ad98)
*   text fixes (0121fd6)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   **shared:** allow "disabled" first to return to "tabindex=0" in "focusable" (160bc59)

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)
*   allow rendered anchors to be aria-hidden (2e9aa23)
*   allow sp-dropdown to accept focus visibly from sp-field-label (134bafc)
*   **button:** add "toggles" attribute to action button (3e2d80c)
*   **button:** add excludeSourceSelector to reduce duplication of styles (683e88e)
*   **button:** add multiple ui icon imports to sp-button (2f17fa9)
*   **button:** allow element content in the default/label slot (7b0ef58)
*   **button:** apply icon as slotted content in action-button styles (3b1487b)
*   **button:** clean up clear button for reuse across elements (4c71eb1)
*   **button:** delivery hold affordance when attribute available (aecc6fe)
*   **button:** include "pointerleave" in management of the "active" state (2e702e4)
*   **button:** minor docs spelling fix (a7a1359)
*   **button:** no double link clicks (02d576c)
*   **button:** prevent default on "space" based activations (708d587)
*   **button:** relate to this.href correctly (fade3ea)
*   **button:** remove old package export listings (32e8573)
*   **button:** revert default "variant" application when missing (fab993e)
*   **button:** use slot text observer pattern (a7288c3)
*   correct @element jsDoc listing across library (c97a632)
*   correct specificity of webkit appearance work around (f0d06bf)
*   correctly delivery visuals and mouse interactions for litAnchor and extensions (0ae889a)
*   docs button variant usage (894282c)
*   **dropdown:** correctly support "quiet" variant (2a51a2b)
*   ensure "click" on "NumpadEnter" key press (450fa01)
*   ensure browser understandable extensions (f4e59f7)
*   final prerelease review of canary builds (1fc032f)
*   implement "emphasized" styles (750bbe7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   match "pointerup" listeners with "pointercancel" for full coverage (7f2ce92)
*   prevent default hoisting of custom pseudo elements (7f66346)
*   remove errant readme content, correct icon selector (3dd1fb1)
*   **shared:** make Focusable pass disabled always (a339d6f)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update role application logic to not overwrite menu* roles (94b6aec)
*   update to latest spectrum-css packages (a5ca19f)
*   updating spectrum-config to support new label styles (cefeaad)
*   use icons without "size" values (3fc7c91)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)
*   work around icon positioning error in CSS source (ef5271c)

*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** add action-group pattern (d2de766)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   add and use icons-ui package (d9c3ab2)
*   add dialog, dialog-wrapped, and underlay elements (3df9050)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   allow activation of longpress content (55e71fd)
*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   **button-group:** add ButtonGroup pattern (c4d85b5)
*   **button:** accept update Spectrum Tokens (d6d6db1)
*   **button:** action-buttons with icons AND text (aa788b1)
*   **button:** add support for "sp-clear-button" (9028b6d)
*   **button:** allow icon only buttons (25623d6)
*   **button:** move "white" and "black" out of "variant" and into "static" (5cf51df)
*   **button:** pass "label" property to "aria-label" (78ae59d)
*   **button:** update spectrum css input (7b5b200)
*   **button:** use latest @spectrum-css/button beta (b3b20ed)
*   **button:** use synthetic button instead of native (49e94bc)
*   **button:** using core-tokens for button (a4a6d42)
*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)
*   **close-button:** add Close Button pattern (8e9e1ad)
*   deprecate "icon-right" in buttons as per Spectrum (064a775)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   leverage latest Spectrum button API (9caf2f6)
*   **search:** adds sp-search element (d484fc2)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **split-button:** add split-button pattern (4833a59)
*   support Spectrum Token consumption and update Action Button to use them (743ab16)
*   support static white and static black variants of Action Button (7f1e25b)
*   **tabs:** add sp-tab-panel element (b17d276)
*   update lit-* dependencies, wip (377f3c8)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)
*   use SixedMixin to manage "size" property (8819821)

*   accept new Spectrum CSS featuring simpler DOM structure (a0b042b)
*   **button:** recentralize shared styles in base (85d3d0a)
*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   prevent default hoisting of custom pseudo elements (7f66346)

*   accept new Spectrum CSS featuring simpler DOM structure (a0b042b)

*   docs button variant usage (894282c)

*   **button:** revert default "variant" application when missing (fab993e)

*   updating spectrum-config to support new label styles (cefeaad)
*   work around icon positioning error in CSS source (ef5271c)

*   **button:** move "white" and "black" out of "variant" and into "static" (5cf51df)
*   **button:** using core-tokens for button (a4a6d42)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** minor docs spelling fix (a7a1359)

**Note:** Version bump only for package @spectrum-web-components/button

*   match "pointerup" listeners with "pointercancel" for full coverage (7f2ce92)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/button

*   support Spectrum Token consumption and update Action Button to use them (743ab16)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   update consumption of Spectrum CSS for latest version (ed2305b)

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** add multiple ui icon imports to sp-button (2f17fa9)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   **close-button:** add Close Button pattern (8e9e1ad)
*   leverage latest Spectrum button API (9caf2f6)
*   support static white and static black variants of Action Button (7f1e25b)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   add t-shirt sizing to Thumbnail and support for "xxs"/"xs" sizes (520a642)

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/button

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/button

*   ensure "click" on "NumpadEnter" key press (450fa01)

**Note:** Version bump only for package @spectrum-web-components/button

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   update role application logic to not overwrite menu* roles (94b6aec)

**Note:** Version bump only for package @spectrum-web-components/button

*   **tabs:** add sp-tab-panel element (b17d276)

*   allow rendered anchors to be aria-hidden (2e9aa23)

*   **button:** no double link clicks (02d576c)

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** prevent default on "space" based activations (708d587)

**Note:** Version bump only for package @spectrum-web-components/button

*   correctly delivery visuals and mouse interactions for litAnchor and extensions (0ae889a)

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** include "pointerleave" in management of the "active" state (2e702e4)

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   allow activation of longpress content (55e71fd)

*   **button:** recentralize shared styles in base (85d3d0a)

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** remove old package export listings (32e8573)

*   allow sp-dropdown to accept focus visibly from sp-field-label (134bafc)
*   correct specificity of webkit appearance work around (f0d06bf)
*   final prerelease review of canary builds (1fc032f)
*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update file path access (8898bf7)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)
*   **button:** delivery hold affordance when attribute available (aecc6fe)
*   **button:** relate to this.href correctly (fade3ea)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   deprecate "icon-right" in buttons as per Spectrum (064a775)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **button:** update spectrum css input (7b5b200)
*   **button:** use latest @spectrum-css/button beta (b3b20ed)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

*   final prerelease review of canary builds (1fc032f)
*   use icons without "size" values (3fc7c91)
*   **button:** relate to this.href correctly (fade3ea)
*   allow sp-dropdown to accept focus visibly from sp-field-label (134bafc)
*   implement "emphasized" styles (750bbe7)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update file path access (8898bf7)
*   **button:** delivery hold affordance when attribute available (aecc6fe)
*   update latest Spectrum CSS beta releases (d8d3acc)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **action-group:** manage "one" and "multiple" selections (6fad59e)
*   **button:** update spectrum css input (7b5b200)
*   **button:** use latest @spectrum-css/button beta (b3b20ed)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

**Note:** Version bump only for package @spectrum-web-components/button

*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   **action-group:** add action-group pattern (d2de766)
*   **card:** upgrade to Spectrum CSS v3.0.0 (84cf1a9)
*   **split-button:** add split-button pattern (4833a59)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   ensure browser understandable extensions (f4e59f7)

**Note:** Version bump only for package @spectrum-web-components/button

*   leverage "exports" field in package.json (321abd7)

*   **button-group:** add ButtonGroup pattern (c4d85b5)

*   add dialog, dialog-wrapped, and underlay elements (3df9050)

*   **button:** clean up clear button for reuse across elements (4c71eb1)
*   remove errant readme content, correct icon selector (3dd1fb1)

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** add excludeSourceSelector to reduce duplication of styles (683e88e)

*   add and use icons-ui package (d9c3ab2)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** add "toggles" attribute to action button (3e2d80c)

*   **dropdown:** correctly support "quiet" variant (2a51a2b)

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

**Note:** Version bump only for package @spectrum-web-components/button

*   **button:** add support for "sp-clear-button" (9028b6d)

**Note:** Version bump only for package @spectrum-web-components/button

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

*   **button:** use slot text observer pattern (a7288c3)
*   **shared:** make Focusable pass disabled always (a339d6f)

*   **button:** allow element content in the default/label slot (7b0ef58)

*   **button:** apply icon as slotted content in action-button styles (3b1487b)

*   **button:** action-buttons with icons AND text (aa788b1)
*   **button:** allow icon only buttons (25623d6)
*   **button:** pass "label" property to "aria-label" (78ae59d)
*   **search:** adds sp-search element (d484fc2)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/button

Property  Attribute  Type  Default  Description `active``active``boolean``false``disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `download``download``string | undefined` Causes the browser to treat the linked URL as a download. `href``href``string | undefined` The URL that the hyperlink points to. `label``label``string | undefined` An accessible label that describes the component. It will be applied to aria-label, but not visually rendered. `noWrap``no-wrap``boolean``false` Disables text wrapping within the button component's label. Please note that this option is not a part of the design specification and should be used carefully, with consideration of this overflow behavior and the readability of the button's content. `pending``pending``boolean``false``pendingLabel``pending-label``string``'Pending'``quiet``quiet``boolean` Style this button to be less obvious `referrerpolicy``referrerpolicy``| 'no-referrer' | 'no-referrer-when-downgrade' | 'origin' | 'origin-when-cross-origin' | 'same-origin' | 'strict-origin' | 'strict-origin-when-cross-origin' | 'unsafe-url' | undefined` How much of the referrer to send when following the link. `rel``rel``string | undefined` The relationship of the linked URL as space-separated link types. `staticColor``static-color``'black' | 'white' | undefined` The static color variant to use for this button. `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `target``target``'_blank' | '_parent' | '_self' | '_top' | undefined` Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>). `treatment``treatment``ButtonTreatments``'fill'` The visual treatment to apply to this button. `type``type``'button' | 'submit' | 'reset'``'button'` The default behavior of the button. Possible values are: `button` (default), `submit`, and `reset`. `variant``variant``ButtonVariants` The visual variant to apply to this button.

Name  Description `default slot` text label of the Button `icon` The icon to use for Button
