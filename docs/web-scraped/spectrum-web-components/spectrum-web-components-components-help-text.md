# Source: https://opensource.adobe.com/spectrum-web-components/components/help-text/

Title: Help Text: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/help-text/

Markdown Content:
An `<sp-help-text>` provides either an informative description or an error message that gives more context about what a user needs to input. It's commonly used in forms.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/help-text?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/help-text?style=for-the-badge)

yarn add @spectrum-web-components/help-text

Import the side effectful registration of `<sp-help-text>` via:

import '@spectrum-web-components/help-text/sp-help-text.js';

When looking to leverage the `HelpText` base class as a type and/or for extension purposes, do so via:

import { HelpText } from '@spectrum-web-components/help-text';
Small<sp-field-label size="s" for="size-s">Password</sp-field-label>
<sp-textfield size="s" id="size-s" type="password">
  <sp-help-text size="s" slot="help-text">
    Create a password with at least 8 characters.
  </sp-help-text>
</sp-textfield>Medium<sp-field-label size="m" for="size-m">Password</sp-field-label>
<sp-textfield size="m" id="size-m" type="password">
  <sp-help-text size="m" slot="help-text">
    Create a password with at least 8 characters.
  </sp-help-text>
</sp-textfield>Large<sp-field-label size="l" for="size-l">Password</sp-field-label>
<sp-textfield size="l" id="size-l" type="password">
  <sp-help-text size="l" slot="help-text">
    Create a password with at least 8 characters.
  </sp-help-text>
</sp-textfield>Extra Large<sp-field-label size="xl" for="size-xl">Password</sp-field-label>
<sp-textfield size="xl" id="size-xl" type="password">
  <sp-help-text size="xl" slot="help-text">
    Create a password with at least 8 characters.
  </sp-help-text>
</sp-textfield>
The negative variant of `<sp-help-text>` is used to convey error messages.

Help text displays either a description (the neutral variant) or an error message (the negative variant) in the same space. When a description is present and an error is triggered, it is replaced with an error message. Once the error is resolved, the help text description reappears.

Since one gets replaced by the other, the language of the help text description and the error need to work together to convey the same messaging. The description text explains the requirements or adds supplementary context for how to successfully interact with a component. The error message text tells a user how to fix the error by re-stating the interaction requirements. Make sure that the help text description and error message include the same essential information so that it isn’t lost if one replaces the other.

Communicate error messages in a human-centered way by guiding a user and showing them a solution — don’t simply state what’s wrong and then leave them guessing as to how to resolve it. Ambiguous error messages can be frustrating and even shame-inducing for users. Also, keep in mind that something that a system may deem an error may not actually be perceived as an error to a user.

For help text, usually the error is related to something that needs to be fixed for in-line validation, so a helpful tone is most appropriate. For example, if someone were to miss filling out a required field that asks for their email address, write the error text like you’re offering a hint or a tip to help guide them to understand what needs to go in the missing field: “Enter your email address.”

<sp-field-label for="negative">Password</sp-field-label>
<sp-textfield id="negative" type="password" required invalid>
  <sp-help-text slot="help-text">
    Create a password with at least 8 characters.
  </sp-help-text>
  <sp-help-text variant="negative" slot="negative-help-text">
    Passwords must be at least 8 characters
  </sp-help-text>
</sp-textfield>
When associated with content that does not supply an icon outlining the presence of an error, use the `icon` attribute to display one as part of the `<sp-help-text>` element.

<sp-field-group horizontal id="fruit">
  <sp-checkbox value="apple">Apple</sp-checkbox>
  <sp-checkbox value="not-a-fruit" onchange="javascript:this.parentElement.invalid = this.checked" >
    Lettuce
  </sp-checkbox>
  <sp-checkbox value="strawberry" checked>Strawberry</sp-checkbox>
  <sp-help-text slot="help-text">One of these is not a fruit.</sp-help-text>
  <sp-help-text icon slot="negative-help-text" icon>
    Choose actual fruit(s).
  </sp-help-text>
</sp-field-group>
When the content associated to the element is disabled, use the `disabled` attribute to match the delivery of the `<sp-help-text>` element to that content.

<sp-field-label for="color" disabled>Color</sp-field-label>
<sp-combobox id="color" disabled>
  <sp-menu-item value="red">Red</sp-menu-item>
  <sp-menu-item value="green">Green</sp-menu-item>
  <sp-menu-item value="blue">Blue</sp-menu-item>
  <sp-help-text slot="help-text" disabled>
    Choose or add at least one color.
  </sp-help-text>
</sp-combobox>
Good, descriptive help text includes 1-2 short sentences of information such as:

*   An overall description of an input field or controls
*   Hints for what kind of information needs to be inputted or selected
*   Specific formatting examples or requirements

It is not currently possible to provide accessible ARIA references between elements in different shadow roots. To ensure proper association between elements, help text must be included via the `slot="help-text"` or `slot="negative-help-text"` in an `<sp-text-field>`, `<sp-field-group>`, `<sp-combobox>` or `<sp-picker>`.

To add help text to your own custom element, see Help Text Mixin.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   #5865`7af5e8f` Thanks @rise-erpelding! - Fix missing CSS custom property overrides for field-label and help-text components

Previously, these components had empty override files despite having corresponding `--system-*` tokens defined in the system theme bridge. This caused the components to not properly apply size-specific spacing tokens for top and bottom text positioning. The fix adds the missing CSS custom property mappings to ensure proper theming across all component sizes (s, m, l, xl).

*   Updated dependencies [`f8bdeec`, `9cb816b`]:

    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5721`72d807c` Thanks @iuliauta! - - **Fixed**: Update block paddings for S2 and Express themes

*   Updated dependencies [`bdf54c1`]:

    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`f6cebbd`]: 
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

*   **help-text:** apply aria-live to ensure full help text is read to user (#4210) (049dc56)

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

*   **dialog:** updates for delivering dialog content accessibly (f0ed33c)

*   add Help Text pattern (fdbb812)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

**Note:** Version bump only for package @spectrum-web-components/help-text

*   **dialog:** updates for delivering dialog content accessibly (f0ed33c)

**Note:** Version bump only for package @spectrum-web-components/help-text

*   add Help Text pattern (fdbb812)

Property  Attribute  Type  Default  Description `icon``icon``boolean``false``variant``variant``HelpTextVariants``'neutral'` The visual variant to apply to this help text.
