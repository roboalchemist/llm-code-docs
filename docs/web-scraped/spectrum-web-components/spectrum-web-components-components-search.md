# Source: https://opensource.adobe.com/spectrum-web-components/components/search/

Title: Search: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/search/

Markdown Content:
The `<sp-search>` element is used for searching and filtering items.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/search?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/search?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/search
Import the side effectful registration of `<sp-search>` via:

import '@spectrum-web-components/search/sp-search.js';
When looking to leverage the `Search` base class as a type and/or for extension purposes, do so via:

import { Search } from '@spectrum-web-components/search';
The search field consists of several key parts:

*   Label/placeholder
*   Text field
*   In-field button to clear the search term

Search fields come in four different sizes for mobile and desktop platform scales: `small`, `medium`, `large`, and `extra-large`.

The default and most frequently used size is `medium`.

Small<sp-search size="s"></sp-search>Medium<sp-search></sp-search>Large<sp-search size="l"></sp-search>Extra Large<sp-search size="xl"></sp-search>
The search icon is set using the `icon magnifier icon-workflow icon-search` classes in the component.

<sp-search label="This is a label"></sp-search>
A placeholder is a hint to the user about what to input in the search field. It is displayed when the search field is empty and is removed when the user starts typing.

<sp-search placeholder="Enter a search term"></sp-search>
A search field can have help text below the field to give extra context or instruction about what a user should input. The description communicates a hint or helpful information, such as a search's scope. The component also supports negative help text, which is displayed when the search field is invalid.

<sp-search>
  <sp-help-text slot="help-text">Enter a search term.</sp-help-text>
  <sp-help-text slot="negative-help-text">Invalid search term.</sp-help-text>
</sp-search>
A clear button is a button that clears the search term. It is displayed when the search field is not empty.

<sp-search value="Flights to Hawaii"></sp-search>
A search field in a disabled state shows that a search option exists, but is not available in that circumstance. This can be used to maintain layout continuity and communicate that it may become available later.

<sp-search disabled></sp-search>
The `submit` event fires when the `<sp-search>` is submitted. This is a non-`composed` event in line with what you would expect a `<form />` to fire. If you choose to prevent the default behavior of this event, the default action for the underlying `<form />` element will also be prevented, allowing you to handle the search action in JavaScript.

Every text field should have a label. A field without a label is ambiguous and not accessible.

The `aria-label` for the search field is set to `Search` by default. The text set in the `label` property is used as the `aria-label` for the search field.

The description in the help text is flexible and encompasses a range of guidance. Sometimes this guidance is about what to input, and sometimes it's about how to input. This includes information such as:

*   An overall description of the input field
*   Hints for what kind of information needs to be input
*   Specific formatting examples or requirements

Learn more about using help text.

Write error messaging in a human-centered way by guiding a user and showing them a solution — don't simply state what's wrong and then leave them guessing as to how to resolve it. Ambiguous error messages can be frustrating and even shame-inducing for users. Also, keep in mind that something that a system may deem an error may not actually be perceived as an error to a user.

Learn more about writing error messages.

Putting instructions for how to complete an input, requirements, or any other essential information into placeholder text is not accessible. Once a value is entered, placeholder text is no longer viewable; if someone is using an automatic form filler, they will never get the information in the placeholder text.

Instead, use the help text description to convey requirements or to show any formatting examples that would help user comprehension. If there's placeholder text and help text at the same time, it becomes redundant and distracting, especially if they're communicating the same thing.

The `holdValueOnEscape` attribute controls whether the typed value should be held (i.e., not cleared or reset) when the Escape key is pressed. If set to true, pressing the Escape key will not affect the value in the search field.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2
    *   @spectrum-web-components/textfield@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/textfield@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/textfield@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/textfield@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/textfield@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies [`7d23140`, `bdf54c1`, `72d807c`, `14ebeb9`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/textfield@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/textfield@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies [`cde976d`]: 
    *   @spectrum-web-components/textfield@1.7.0
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/base@1.7.0

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

*   Updated dependencies [`f6cebbd`, `00eb0a8`, `9e15a66`]:

    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/textfield@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies [`4e06533`]: 
    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/textfield@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/textfield@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/textfield@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/search

*   **search:** clear button ui in express (#4910) (f88e1e2)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   **icon:** use core tokens (a11ef6b)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   **search:** add mod to remove clear button padding (65168fe)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   **number-field,search,textfield:** add t-shirt sizes (fda8f96)

**Note:** Version bump only for package @spectrum-web-components/search

*   **search:** use core tokens (c62a7cd)

*   **search,textfield:** use core tokens (2ed5135)

**Note:** Version bump only for package @spectrum-web-components/search

*   add tslib as dependency where needed (78885d9)
*   apply "HelpTextMixin" to form elements (a952447)
*   correct @element jsDoc listing across library (c97a632)
*   ensure browser understandable extensions (f4e59f7)
*   ensure CCX search visual delivery (22b90b9)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   normalize "event" and "error" argument names (8d382cd)
*   **search:** ensure "reset" surfaces "input" and "change" events (d8204a9)
*   **search:** prevent overflow content from going behind clear button (956f947)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)
*   use type="search" for nicer virtual keyboards (c439eb3)

*   **action-button:** add action button pattern (03ac00a)
*   add and use icons-ui package (d9c3ab2)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **button:** use synthetic button instead of native (49e94bc)
*   conditionally load focus-visible polyfill (6b5e5cf)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   **search:** adds sp-search element (d484fc2)
*   **search:** introduce API to control form interactions (42fac00)
*   **search:** submit will bubble (8014345)
*   **search:** support "quiet" variant (d0f85f1)
*   **search:** update spectrum css input (05d8131)
*   **search:** use Spectrum CSS ^3.0.0 (7830ac0)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)

*   Revert "chore: release new versions" (a6d655d)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   **search:** prevent overflow content from going behind clear button (956f947)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   ensure CCX search visual delivery (22b90b9)

*   conditionally load focus-visible polyfill (6b5e5cf)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   apply "HelpTextMixin" to form elements (a952447)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/search

*   use type="search" for nicer virtual keyboards (c439eb3)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **search:** update spectrum css input (05d8131)

*   include the "types" entry in package.json files (b432f59)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use icons without "size" values (3fc7c91)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-button:** add action button pattern (03ac00a)
*   **button:** use synthetic button instead of native (49e94bc)
*   **icons-workflow:** vend fully registered icon components (941f3a4)
*   **search:** update spectrum css input (05d8131)

**Note:** Version bump only for package @spectrum-web-components/search

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/search

*   **search:** use Spectrum CSS ^3.0.0 (7830ac0)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   ensure browser understandable extensions (f4e59f7)

**Note:** Version bump only for package @spectrum-web-components/search

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   add and use icons-ui package (d9c3ab2)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   **search:** ensure "reset" surfaces "input" and "change" events (d8204a9)

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

**Note:** Version bump only for package @spectrum-web-components/search

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use @adobe/spectrum-css@2.15.1 (3918888)

**Note:** Version bump only for package @spectrum-web-components/search

*   add tslib as dependency where needed (78885d9)

**Note:** Version bump only for package @spectrum-web-components/search

*   **search:** adds sp-search element (d484fc2)
*   **search:** introduce API to control form interactions (42fac00)
*   **search:** submit will bubble (8014345)
*   **search:** support "quiet" variant (d0f85f1)

 Property  Attribute  Type  Default  Description `action``action``string``''``allowedKeys``allowed-keys``string``''` A regular expression outlining the keys that will be allowed to update the value of the form control. `autocomplete``autocomplete``| 'list' | 'none' | HTMLInputElement['autocomplete'] | HTMLTextAreaElement['autocomplete'] | undefined` What form of assistance should be provided when attempting to supply a value to the form control 
Note: combobox overrides `autocomplete` intentionally with `aria-autocomplete` values, which is why those values (although invalid for native `autocomplete`) are included here to support the combobox accessibility pattern.

`disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `grows``grows``boolean``false` Whether a form control delivered with the `multiline` attribute will change size vertically to accomodate longer input `holdValueOnEscape``holdValueOnEscape``boolean` Controls whether the typed value should be held (i.e., not cleared or reset) when the Escape key is pressed. If set to true, pressing the Escape key will not affect the value in the search field. `invalid``invalid``boolean``false` Whether the `value` held by the form control is invalid. `label``label``string``'Search'` A string applied via `aria-label` to the form control when a user visible label is not provided. `maxlength``maxlength``number``-1` Defines the maximum string length that the user can enter `method``method``'get' | 'post' | 'dialog' | undefined``minlength``minlength``number``-1` Defines the minimum string length that the user can enter `multiline``multiline``boolean``false` Whether the form control should accept a value longer than one line `name``name``string | undefined` Name of the form control. `pattern``pattern``string | undefined` Pattern the `value` must match to be valid `placeholder``placeholder``string``'Search'` Text that appears in the form control when it has no value set `quiet``quiet``boolean``false` Whether to display the form control with no visible background `readonly``readonly``boolean``false` Whether a user can interact with the value of the form control `required``required``boolean``false` Whether the form control will be found to be invalid when it holds no `value` `rows``rows``number``-1` The specific number of rows the form control should provide in the user interface `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `valid``valid``boolean``false` Whether the `value` held by the form control is valid. `value``value``string | number` The value held by the form control 

Name  Description `help-text` default or non-negative help text to associate to your form element `negative-help-text` negative help text to associate to your form element when `invalid`

Name  Type  Description `change``Event``An alteration to the value of the element has been committed by the user.``input``Event``The value of the element has changed.``submit``Event``The search form has been submitted.`
