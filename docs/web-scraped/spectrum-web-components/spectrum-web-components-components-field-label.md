# Source: https://opensource.adobe.com/spectrum-web-components/components/field-label/

Title: Field Label: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/field-label/

Markdown Content:
An `<sp-field-label>` provides accessible labelling for form elements. Use the `for` attribute to outline the `id` of an element in the same DOM tree to which it should associate itself. Field labels give context to information that a user needs to input and are commonly used in forms to provide users with clear guidance about what information is required.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/field-label?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/field-label?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/field-label

Import the side effectful registration of `<sp-field-label>` via:

import '@spectrum-web-components/field-label/sp-field-label.js';
When looking to leverage the `FieldLabel` base class as a type and/or for extension purposes, do so via:

import { FieldLabel } from '@spectrum-web-components/field-label';
Field labels can be associated with form elements by using the `for` attribute, which should reference the `id` of the related input element.

<sp-field-label for="product-name">Product name</sp-field-label>
<sp-textfield id="product-name" placeholder="Enter product name"></sp-textfield>
Field labels can also be used to label a group of related inputs:

<sp-field-label for="account-type">Account type</sp-field-label>
<sp-radio-group id="account-type">
  <sp-radio value="admin">Admin</sp-radio>
  <sp-radio value="member" checked>Member</sp-radio>
  <sp-radio value="guest">Guest</sp-radio>
</sp-radio-group>Small<sp-field-label for="lifestory-0" size="s">Life Story (Small)</sp-field-label>
<sp-textfield placeholder="Enter your life story" id="lifestory-0" size="s"></sp-textfield>Medium<sp-field-label for="lifestory-1" size="m">Life Story (Medium)</sp-field-label>
<sp-textfield placeholder="Enter your life story" id="lifestory-1" size="m"></sp-textfield>Large<sp-field-label for="lifestory-2" size="l">Life Story (Large)</sp-field-label>
<sp-textfield placeholder="Enter your life story" id="lifestory-2" size="l"></sp-textfield>Extra Large<sp-field-label for="lifestory-3" size="xl">
  Life Story (Extra Large)
</sp-field-label>
<sp-textfield placeholder="Enter your life story" id="lifestory-3" size="xl"></sp-textfield>
Field labels can be positioned either on top of an input (default) or to the side of an input. The top position is recommended for most cases as it works better with long text, localization, and responsive layouts.

Using the `side-aligned` attribute will display the `<sp-field-label>` element inline with surrounding elements and the `start` and `end` values outline the alignment of the label text in the width specified.

Top (Default)<sp-field-label for="country-top">Country</sp-field-label>
<sp-textfield placeholder="Enter your country" id="country-top"></sp-textfield>Side (Start Aligned)
Use `side-aligned="start"` to display the `<sp-field-label>` inline and to align the label text to the "start" of the flow of text:

<sp-field-label for="lifestory-1" side-aligned="start" style="width: 120px">
  Life Story
</sp-field-label>
<sp-textfield placeholder="Enter your life story" id="lifestory-1"></sp-textfield>
<br />
<br />
<sp-field-label for="birth-place-1" side-aligned="start" required style="width: 120px">
  Birthplace
</sp-field-label>
<sp-picker id="birth-place-1">
  <span slot="label">Choose a location:</span>
  <sp-menu-item>Istanbul</sp-menu-item>
  <sp-menu-item>London</sp-menu-item>
  <sp-menu-item>Maputo</sp-menu-item>
  <sp-menu-item>Melbourne</sp-menu-item>
  <sp-menu-item>New York</sp-menu-item>
  <sp-menu-item>San Francisco</sp-menu-item>
  <sp-menu-item>Santiago</sp-menu-item>
  <sp-menu-item>Tokyo</sp-menu-item>
</sp-picker>Side (End Aligned)
Use `side-aligned="end"` to display the `<sp-field-label>` inline and to align the label text to the "end" of the flow of text:

<sp-field-label for="lifestory-2" side-aligned="end" required style="width: 120px">
  Life Story
</sp-field-label>
<sp-textfield placeholder="Enter your life story" id="lifestory-2"></sp-textfield>
<br />
<br />
<sp-field-label for="birth-place-2" side-aligned="end" style="width: 120px">
  Birthplace
</sp-field-label>
<sp-picker id="birth-place-2">
  <span slot="label">Choose a location:</span>
  <sp-menu-item>Istanbul</sp-menu-item>
  <sp-menu-item>London</sp-menu-item>
  <sp-menu-item>Maputo</sp-menu-item>
  <sp-menu-item>Melbourne</sp-menu-item>
  <sp-menu-item>New York</sp-menu-item>
  <sp-menu-item>San Francisco</sp-menu-item>
  <sp-menu-item>Santiago</sp-menu-item>
  <sp-menu-item>Tokyo</sp-menu-item>
</sp-picker>
Field labels can indicate whether an input is required or optional. By default, required fields are marked with an asterisk icon.

Required (Icon)<sp-field-label for="name-required" required>Full name</sp-field-label>
<sp-textfield placeholder="Enter your full name" id="name-required" required></sp-textfield>Optional (Text)<sp-field-label for="description-optional">
  Profile description (optional)
</sp-field-label>
<sp-textfield placeholder="Enter a description" id="description-optional"></sp-textfield>
When the associated input field is disabled, the field label should also be disabled.

<sp-field-label for="disabled-field" disabled>Country</sp-field-label>
<sp-textfield placeholder="Enter your country" id="disabled-field" disabled></sp-textfield>
When a field label is too long for the available horizontal space, it wraps to form another line.

<sp-field-label for="seminar-field" style="max-width: 200px">
  What you're hoping to learn from the seminar and any specific topics you'd
  like covered
</sp-field-label>
<sp-textfield placeholder="Enter your expectations" id="seminar-field"></sp-textfield>
Every input should have a label. An input without a label is ambiguous and not accessible. In rare cases where context is sufficient and an accessibility expert has reviewed the design, the label could be visually hidden but should still include an `aria-label` in HTML.

The `for` attribute of the field label should match the `id` attribute of the associated input element to ensure proper association for screen readers and other assistive technologies.

Use a short, descriptive label (1-3 words) for the information that users need to provide. Supplementary information or requirements should be shown in help text below the field, not in the label.

Following Adobe's UX writing style, field labels should be written in sentence case unless they contain words that are branded terms.

The design of the component already communicates the relationship between the label and the input field, so a colon is unnecessary.

In a single form, mark only the required fields or only the optional fields, depending on whichever is less frequent in the entire form. This reduces visual noise and makes the form easier to understand.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5865`7af5e8f` Thanks @rise-erpelding! - Fix missing CSS custom property overrides for field-label and help-text components

Previously, these components had empty override files despite having corresponding `--system-*` tokens defined in the system theme bridge. This caused the components to not properly apply size-specific spacing tokens for top and bottom text positioning. The fix adds the missing CSS custom property mappings to ensure proper theming across all component sizes (s, m, l, xl).

*   Updated dependencies [`b95e254`, `f8bdeec`, `9cb816b`]:

    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5721`72d807c` Thanks @iuliauta! - - **Fixed**: Update block paddings for S2 and Express themes

*   Updated dependencies [`7d23140`]:

    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   **asset:** use core tokens (99e76f4)

*   **picker:** support inline labeling of quiet Picker (#3704) (3372286)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   support numeric IDs when resolving elements (f62bf0d)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   **slider:** add t-shirt sizing (24dac78)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   **picker:** correct label application for screen readers (8ce0cb0)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   **slider:** use spectrum-tokens (8b1e72c)

**Note:** Version bump only for package @spectrum-web-components/field-label

*   add "editable" option to "sp-slider" (e86d7fa)
*   allow sp-dropdown to accept focus visibly from sp-field-label (134bafc)
*   **field-label:** do not assume a target is available and surface t-shirt sizing (c5daead)
*   move property management into update or willUpdate (f66069f)
*   remove `<sp-menu>` usage where deprecated (387db3b)
*   update export patterns (b2da444)
*   update to latest spectrum-css packages (a5ca19f)

*   **action-button:** add action button pattern (03ac00a)
*   add t-shirt sizing to the Radio pattern (fc49343)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **field-label:** add field label pattern (2fa7c7e)
*   **field-label:** update spectrum css input (80a993d)
*   **field-label:** use core tokens (8db7ac4)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   **picker:** process field-label content for more accurate a11y tree (dc9df54)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   **field-label:** use core tokens (8db7ac4)

**Note:** Version bump only for package @spectrum-web-components/field-label

*   add t-shirt sizing to the Radio pattern (fc49343)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   move property management into update or willUpdate (f66069f)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   add "editable" option to "sp-slider" (e86d7fa)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   remove `<sp-menu>` usage where deprecated (387db3b)

*   **picker:** process field-label content for more accurate a11y tree (dc9df54)

**Note:** Version bump only for package @spectrum-web-components/field-label

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/field-label

**Note:** Version bump only for package @spectrum-web-components/field-label

*   **field-label:** do not assume a target is available and surface t-shirt sizing (c5daead)
*   allow sp-dropdown to accept focus visibly from sp-field-label (134bafc)
*   update export patterns (b2da444)

*   **action-button:** add action button pattern (03ac00a)
*   **field-label:** add field label pattern (2fa7c7e)
*   **field-label:** update spectrum css input (80a993d)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

*   allow sp-dropdown to accept focus visibly from sp-field-label (134bafc)
*   update export patterns (b2da444)

*   **action-button:** add action button pattern (03ac00a)
*   **field-label:** add field label pattern (2fa7c7e)
*   **field-label:** update spectrum css input (80a993d)
*   **icons-workflow:** vend fully registered icon components (941f3a4)

Property  Attribute  Type  Default  Description `disabled``disabled``boolean``false``for``for``string``''``id``id``string``''``required``required``boolean``false``sideAligned``side-aligned``'start' | 'end' | undefined`

Name  Description `default slot` text content of the label
