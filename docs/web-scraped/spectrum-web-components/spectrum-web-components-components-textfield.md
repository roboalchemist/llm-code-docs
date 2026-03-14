# Source: https://opensource.adobe.com/spectrum-web-components/components/textfield/

Title: Textfield: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/textfield/

Markdown Content:
`sp-textfield` components are text boxes that allow users to input custom text entries with a keyboard. Various decorations can be displayed around the field to communicate the entry requirements.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/textfield?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/textfield?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/textfield
Import the side effectful registration of `<sp-textfield>` via:

import '@spectrum-web-components/textfield/sp-textfield.js';
When looking to leverage the `Textfield` base class as a type and/or for extension purposes, do so via:

import { Textfield } from '@spectrum-web-components/textfield';<sp-textfield id="basic" label="Name"></sp-textfield>
A text field must have a label in order to be accessible. A label can be provided either via the `label` attribute, like the previous example or with an `<sp-field-label>` element.

<sp-field-label for="with-field-label">Name</sp-field-label>
<sp-textfield id="with-field-label"></sp-textfield>
Use the `placeholder` attribute to include placeholder text. **Note**: Placeholder text should not be used as a replacement for a label or help help text.

<sp-field-label for="has-placeholder">Name</sp-field-label>
<sp-textfield id="has-placeholder" placeholder="ex., John Doe"></sp-textfield>
Help text can be accessibly associated with an `<sp-textfield>` element by using the `help-text` or `negative-help-text` slots. When using the `negative-help-text` slot, `<sp-textfield>` will self manage the presence of this content based on the value of the `invalid` property on your `<sp-textfield>` element. Content within the `help-text` slot will be show by default. When your `<sp-textfield>` should receive help text based on state outside of the complexity of `invalid` or not, manage the content addressed to the `help-text` from above to ensure that it displays the right messaging and possesses the right `variant`.

See help text for more information.

Self managed<sp-field-label for="self">Stay "Positive"</sp-field-label>
<sp-textfield id="self" pattern="[P][o][s][i][t][i][v][e]" value="Positive">
  <sp-help-text slot="help-text">
    Tell us how you are feeling today.
  </sp-help-text>
  <sp-help-text slot="negative-help-text">Please be "Positive".</sp-help-text>
</sp-textfield>Managed from above<sp-field-label for="managed">Stay "Positive"</sp-field-label>
<sp-textfield id="managed" pattern="[P][o][s][i][t][i][v][e]" value="Positive" oninput=' const helpText = this.querySelector(`[slot="help-text"]`); helpText.textContent = this.invalid ? `Please be "Positive".` : `Tell us how you are feeling today.`; helpText.variant = this.invalid ? `negative` : `neutral`; '>
  <sp-help-text slot="neutral-text">
    Tell us how you're feeling today.
  </sp-help-text>
  <sp-help-text slot="help-text">Please be "Positive".</sp-help-text>
</sp-textfield>Small<sp-field-label size="s" for="name-0-s">Name</sp-field-label>
<sp-textfield size="s" id="name-0-s" placeholder="Enter your name"></sp-textfield>Medium<sp-field-label for="name-0-m">Name</sp-field-label>
<sp-textfield id="name-0-m" placeholder="Enter your name"></sp-textfield>Large<sp-field-label size="l" for="name-0-l">Name</sp-field-label>
<sp-textfield size="l" id="name-0-l" placeholder="Enter your name"></sp-textfield>Extra Large<sp-field-label size="xl" for="name-0-xl">Name</sp-field-label>
<sp-textfield size="xl" id="name-0-xl" placeholder="Enter your name"></sp-textfield>
When inputting URLs, telephone numbers, email addresses, or passwords, specify a `type` to provide user affordances like mobile keyboards and obscured characters:

*   `url`
*   `tel`
*   `email`
*   `password`
*   `text` (default)

<sp-field-label for="tel-1">Telephone</sp-field-label>
<sp-textfield id="tel-1" type="tel" placeholder="Enter your phone number" autocomplete="tel"></sp-textfield>
<sp-field-label for="password-1">Password</sp-field-label>
<sp-textfield id="password-1" type="password" autocomplete="current-password"></sp-textfield>
If the `type` attribute is not specified, or if it does not match any of these values, the default type adopted is "text."

The quiet style works best when a clear layout (vertical stack, table, grid) assists in a user's ability to parse the element. Too many quiet components in a small space can be hard to read.

<sp-field-label for="name-3">Name (quietly)</sp-field-label>
<sp-textfield id="name-3" placeholder="Enter your name" quiet autocomplete="name"></sp-textfield>
Use the `required` attribute to indicate a textfield value is required. Dictate the validity or invalidity state of the text entry with the `valid` or `invalid` attributes.

<sp-field-label for="name-1" required>Name</sp-field-label>
<sp-textfield id="name-1" placeholder="Enter your name" valid value="My Name" autocomplete="name"></sp-textfield>
<br />
<sp-field-label for="name-2" required>Name</sp-field-label>
<sp-textfield id="name-2" invalid autocomplete="name" placeholder="Enter your name"></sp-textfield>
Every text field should have a label. A field without a label is ambiguous and not accessible.

The description in the help text is flexible and encompasses a range of guidance. Sometimes this guidance is about what to input, and sometime it’s about how to input. This includes information such as:

*   An overall description of the input field
*   Hints for what kind of information needs to be input
*   Specific formatting examples or requirements

Learn more about using help text.

Write error messaging in a human-centered way by guiding a user and showing them a solution — don’t simply state what’s wrong and then leave them guessing as to how to resolve it. Ambiguous error messages can be frustrating and even shame-inducing for users. Also, keep in mind that something that a system may deem an error may not actually be perceived as an error to a user.

Learn more about writing error messages.

Use the `autocomplete` attribute to help users complete forms faster and with fewer errors, especially on mobile devices. Auto-complete is required only for common input fields that collect an individual’s personal data.

<sp-field-label for="email-1">Email</sp-field-label>
<sp-textfield id="email-1" type="email" autocomplete="email"></sp-textfield>

<sp-field-label for="phone-1">Phone</sp-field-label>
<sp-textfield id="phone-1" type="tel" autocomplete="tel"></sp-textfield>

<sp-field-label for="name-1">Full Name</sp-field-label>
<sp-textfield id="name-1" type="text" autocomplete="name"></sp-textfield>
**Common autocomplete values include**:

| Input type | Autocomplete token |
| --- | --- |
| `type="text"` | `name` - Full name |
| `type="text"` | `given-name` - First name |
| `type="text"` | `family-name` - Last name |
| `type="email"` | `email` - Email address |
| `type="tel"` | `tel` - Telephone number |
| `type="url"` | `url` - Website URL |
| `type="password"` | `current-password` - Current password for login |
| `type="password"` | `new-password` - New password when creating account or changing password |

See the MDN autocomplete reference for the complete list of values.

Putting instructions for how to complete an input, requirements, or any other essential information into placeholder text is not accessible. Once a value is entered, placeholder text is no longer viewable; if someone is using an automatic form filler, they will never get the information in the placeholder text.

Instead, use the help text description to convey requirements or to show any formatting examples that would help user comprehension. If there's placeholder text and help text at the same time, it becomes redundant and distracting, especially if they're communicating the same thing.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/help-text@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/help-text@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   Updated dependencies [`7af5e8f`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/help-text@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/help-text@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5721`72d807c` Thanks @iuliauta! - - **Fixed**: Update border radius and border width for different t-shirt sizes for textfield component for S2 and Express themes

*   #5756`14ebeb9` Thanks @castastrophe! - - **Fixed**: Update border color and block padding inside the textfield and textarea components for S2 and Express themes

*   Updated dependencies [`bdf54c1`, `72d807c`]:

    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/help-text@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   #5504`cde976d` Thanks @castastrophe! - Replace deprecated `word-break: break-word` with `overflow-wrap: break-word` to align with modern CSS standards and improve cross-browser compatibility. This property was deprecated in Chrome 44 (July 2015) in favor of the standardized `overflow-wrap` property.

*   Updated dependencies []:

    *   @spectrum-web-components/help-text@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5157`9e15a66` Thanks @TarunAdobe! - # Release Note

    *   #3615`f09c84a`Thanks@Rajdeepc! - ### Infield button fast follows 
        *   Updated infield button disabled border color to use`-spectrum-gray-300`for spectrum-two theme and`-spectrum-gray-200`for other themes.

📝#3536`f77aa72`Thanks@marissahuysentruyt!

    *   S2 Foundations fixes 
        *   Adjusts the background-color of the infield button components within stepper to use`gray-100`as opposed to`gray-25`. 
            *   This corresponds to the background-color updates picker has for S2.

        *   Corrects the border color for the default picker for S2 foundations, using`gray-500`(instead of`gray-800`) to align with other field/form components.
        *   Refactors the`&.is-keyboardFocused&.is-placeholder`selector to`&.is-keyboardFocused.spectrum-Picker-label.is-placeholder`to avoid unexpectedly targeting the nested placeholder class.

📝#3541`1a3245c`Thanks@castastrophe!

Dependency alignment across the project.

    *   Updated dependencies [`205182b`,`1a3245c`]: 
        *   @spectrum-css/icon@9.1.0
        *   @spectrum-css/tokens@16.0.1

Bump @spectrum-css/stepper to 7.1.3

    *   #3621`3aec28a`Thanks@marissahuysentruyt! 
        *   Updates`-spectrum-stepper-buttons-border-color-keyboard-focus`from`gray-900`to`gray-800`to match the rest of the border color on keyboardFocus.

📝#3594`6200a63`Thanks@TarunAdobe!

    *   Updates Stepper's key-focus border color (`-spectrum-stepper-border-color-keyboard-focus`) to`-spectrum-gray-800`.

📝#3536`f77aa72`Thanks@marissahuysentruyt!

    *   S2 Foundations fixes 
        *   Adjusts the background-color of the infield button components within stepper to use`gray-100`as opposed to`gray-25`. 
            *   This corresponds to the background-color updates picker has for S2.

        *   Corrects the border color for the default picker for S2 foundations, using`gray-500`(instead of`gray-800`) to align with other field/form components.
        *   Refactors the`&.is-keyboardFocused&.is-placeholder`selector to`&.is-keyboardFocused.spectrum-Picker-label.is-placeholder`to avoid unexpectedly targeting the nested placeholder class.

📝#3541`1a3245c`Thanks@castastrophe!

Dependency alignment across the project.

    *   Updated dependencies [`205182b`,`9b108f7`,`1a3245c`]: 
        *   @spectrum-css/actionbutton@8.0.0
        *   @spectrum-css/icon@9.1.0
        *   @spectrum-css/infieldbutton@7.0.0
        *   @spectrum-css/textfield@9.0.0
        *   @spectrum-css/tokens@16.0.1

📝#3575`2e17d10`Thanks@TarunAdobe!

    *   Updated border color on keyboard focus state for textfield in spectrum-two theme.

📝#3539`9b108f7`Thanks@rise-erpelding!

    *   Updates invalid icon spacing to be vertically centered for S2.

📝#3541`1a3245c`Thanks@castastrophe!

    *   Dependency alignment across the project.

Set component peerDependencies as optional to reduce console warnings on downstream projects.

    *   Updated dependencies [`205182b`,`1a3245c`]: 
        *   @spectrum-css/helptext@8.0.0
        *   @spectrum-css/tokens@16.0.1

    *   #3658`e9fde67`Thanks@rise-erpelding! - Change S2 theme border color to gray-800 on keyfocus per design request in order to align with text field.

📝#3593`d829abb`Thanks@TarunAdobe!

Updated`--spectrum-search-background-color-disabled`to`--spectrum-gray-25`and`--spectrum-search-border-color-disabled`to`--spectrum-gray-300`for the S2 foundations contexts.

Also defines disabled quiet border and background colors (`--system-search-quiet-background-color-disabled`and`--system-search-quiet-border-color-disabled`) in order to maintain disabled quiet styling.

📝#3541`1a3245c`Thanks@castastrophe!

Dependency alignment across the project.

    *   Updated dependencies [`205182b`,`9b108f7`,`1a3245c`]: 
        *   @spectrum-css/clearbutton@8.0.0
        *   @spectrum-css/icon@9.1.0
        *   @spectrum-css/textfield@9.0.0
        *   @spectrum-css/tokens@16.0.1

*   Updated dependencies [`f6cebbd`]:

    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/help-text@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`165a904`]: 
    *   @spectrum-web-components/help-text@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/help-text@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **number-field:** select full value when using Tab to enter a field with a unit (#4340) (a9d5cef)

*   **contextual-help:** add contextual help pattern (#4285) (a259aa3)

*   **number-field:** select full value when using Tab to enter a field with a unit (#4340) (a9d5cef)

*   **contextual-help:** add contextual help pattern (#4285) (a259aa3)

*   **number-field:** select full value when using Tab to enter a field with a unit (#4340) (a9d5cef)

*   **textfield:** textarea actually grows with multiline (#4271) (d8d0e84)

*   **textfield:** textarea actually grows with multiline (#4271) (d8d0e84)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** clearly mark/support "multiline" as a requirement of "grows" (a3e464d)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **combobox:** add combobox pattern (#3894) (47d7d71), closes #3887

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** added name attribute to textfield (#3752) (593005a)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   correct composition entry of multi-byte numbers (#3610) (5e11934)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **number-field:** update button label to use number-field-labels as part of the text (#3474) (b92daf2)
*   setting title when textfield is invalid (36d0537)
*   **textfield:** add support for [grows] when [multiline] (3b306d4)
*   **textfield:** update focus state when [multiline][quiet] (#3452) (a7f563a)

*   **number-field,search,textfield:** add t-shirt sizes (fda8f96)
*   **textfield:** add rows attribute (#3356) (1ee1c37)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **number-field:** simplify width management (ef4765a)

*   **search,textfield:** use core tokens (2ed5135)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   add support for "readonly" attribute (4bce3b7)
*   apply "HelpTextMixin" to form elements (a952447)
*   apply Focuable styles in class extensions (38f7afd)
*   **button:** relate to this.href correctly (fade3ea)
*   correct @element jsDoc listing across library (c97a632)
*   correct sp-textfield[multiline][grows] styling and add story for regression testing (58c9331)
*   disallow undefined property for min and maxlength (21547f7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   minlength now accepted as minimum length for value.toString (bc3b1c2)
*   normalize "event" and "error" argument names (8d382cd)
*   **number-field:** process 2 byte characters as their single byte cousins (f424c0a)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **textfield:** add 'u' flag to keep consistency with native input element (0af779f)
*   **textfield:** add maxlength and minlength attributes (5326649)
*   **textfield:** add select() API mapping to shadow DOM element (d467a34)
*   **textfield:** break very long words within the Textarea's sizer element (2f95ac0)
*   **textfield:** correct "multiline" and "grows" delivery (fa0ac34)
*   **textfield:** leverage aria-invalid attribute (e718c0a)
*   **textfield:** prevent IME selection misalignment in Safari when using hiragana input modality (f8e1e70)
*   **textfield:** process ".is-focused" and ".is-keyboardFocused" styles (48fd67d)
*   **textfield:** reimplement min/maxlength (23a4c2e)
*   **textfield:** remove use of sp-icons-* (9a5c213)
*   **textfield:** respect resize styling (04993c3)
*   **textfield:** respect type=text|url|tel|email|password (1b7a59a)
*   **textfield:** update for easier extensibility (9deaf9e)
*   **textfield:** update validation path, add "allowed-keys" (ae9f85d)
*   **textfield:** Use correct filename in exports field (637b166)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   delivery dev mode messages in various packages (62370a1)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   pass through autocomplete attribute to inputs (5416510)
*   **search:** use Spectrum CSS ^3.0.0 (7830ac0)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **textfield:** add support for setSelectionRange (#2070) (dd17ba0)
*   **textfield:** update spectrum css input (2ce4ba2)
*   **textfield:** use Spectrum CSS ^3.0.0 (1c1acb9)
*   update lit-* dependencies, wip (377f3c8)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   minlength now accepted as minimum length for value.toString (bc3b1c2)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   include all Dev Mode files in side effects (f70817c)

*   delivery dev mode messages in various packages (62370a1)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** correct "multiline" and "grows" delivery (fa0ac34)

*   **number-field:** process 2 byte characters as their single byte cousins (f424c0a)

*   **textfield:** add support for setSelectionRange (#2070) (dd17ba0)

*   **textfield:** prevent IME selection misalignment in Safari when using hiragana input modality (f8e1e70)

*   apply "HelpTextMixin" to form elements (a952447)

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** respect type=text|url|tel|email|password (1b7a59a)

*   adopt DNA@7 base Spectrum CSS (e08cafd)

*   **textfield:** respect resize styling (04993c3)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   correct @element jsDoc listing across library (c97a632)

*   **textfield:** break very long words within the Textarea's sizer element (2f95ac0)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   correct sp-textfield[multiline][grows] styling and add story for regression testing (58c9331)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** add select() API mapping to shadow DOM element (d467a34)

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   **textfield:** update for easier extensibility (9deaf9e)

*   **textfield:** add 'u' flag to keep consistency with native input element (0af779f)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** leverage aria-invalid attribute (e718c0a)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   add support for "readonly" attribute (4bce3b7)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   disallow undefined property for min and maxlength (21547f7)
*   **textfield:** reimplement min/maxlength (23a4c2e)
*   use icons without "size" values (3fc7c91)
*   **button:** relate to this.href correctly (fade3ea)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **textfield:** process ".is-focused" and ".is-keyboardFocused" styles (48fd67d)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **textfield:** update spectrum css input (2ce4ba2)

*   use icons without "size" values (3fc7c91)
*   **button:** relate to this.href correctly (fade3ea)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   **textfield:** process ".is-focused" and ".is-keyboardFocused" styles (48fd67d)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **textfield:** update spectrum css input (2ce4ba2)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **search:** use Spectrum CSS ^3.0.0 (7830ac0)
*   **textfield:** use Spectrum CSS ^3.0.0 (1c1acb9)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** Use correct filename in exports field (637b166)

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** add maxlength and minlength attributes (5326649)

*   **textfield:** remove use of sp-icons-* (9a5c213)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   **textfield:** update validation path, add "allowed-keys" (ae9f85d)

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

**Note:** Version bump only for package @spectrum-web-components/textfield

*   pass through autocomplete attribute to inputs (5416510)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   apply Focuable styles in class extensions (38f7afd)

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

**Note:** Version bump only for package @spectrum-web-components/textfield

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/textfield

 Property  Attribute  Type  Default  Description `allowedKeys``allowed-keys``string``''` A regular expression outlining the keys that will be allowed to update the value of the form control. `autocomplete``autocomplete``| 'list' | 'none' | HTMLInputElement['autocomplete'] | HTMLTextAreaElement['autocomplete'] | undefined` What form of assistance should be provided when attempting to supply a value to the form control 
Note: combobox overrides `autocomplete` intentionally with `aria-autocomplete` values, which is why those values (although invalid for native `autocomplete`) are included here to support the combobox accessibility pattern.

`disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `grows``grows``boolean``false` Whether a form control delivered with the `multiline` attribute will change size vertically to accomodate longer input `invalid``invalid``boolean``false` Whether the `value` held by the form control is invalid. `label``label``string``''` A string applied via `aria-label` to the form control when a user visible label is not provided. `maxlength``maxlength``number``-1` Defines the maximum string length that the user can enter `minlength``minlength``number``-1` Defines the minimum string length that the user can enter `multiline``multiline``boolean``false` Whether the form control should accept a value longer than one line `name``name``string | undefined` Name of the form control. `pattern``pattern``string | undefined` Pattern the `value` must match to be valid `placeholder``placeholder``string``''` Text that appears in the form control when it has no value set `quiet``quiet``boolean``false` Whether to display the form control with no visible background `readonly``readonly``boolean``false` Whether a user can interact with the value of the form control `required``required``boolean``false` Whether the form control will be found to be invalid when it holds no `value` `rows``rows``number``-1` The specific number of rows the form control should provide in the user interface `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `valid``valid``boolean``false` Whether the `value` held by the form control is valid. `value``value``string | number` The value held by the form control 

Name  Description `help-text` default or non-negative help text to associate to your form element `negative-help-text` negative help text to associate to your form element when `invalid`

Name  Type  Description `change``Event``An alteration to the value of the element has been committed by the user.``input``Event``The value of the element has changed.`
