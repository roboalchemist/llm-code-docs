# Source: https://opensource.adobe.com/spectrum-web-components/components/textarea/

Title: Textarea: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/textarea/

Markdown Content:
`sp-textfield[multiline]` components are text areas that allow users to input custom multiline text entries with a keyboard. Various decorations can be displayed around the field to communicate the entry requirements.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/textfield?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/textfield?style=for-the-badge)

yarn add @spectrum-web-components/textfield
Import the side effectful registration of `<sp-textfield>` via:

import '@spectrum-web-components/textfield/sp-textfield.js';
When looking to leverage the `Textfield` base class as a type and/or for extension purposes, do so via:

import { Textfield } from '@spectrum-web-components/textfield';
A text area consists of an area for the user to enter text and optional placeholder text. It should be used with an field label element.

<sp-field-label for="story-0">Background</sp-field-label>
<sp-textfield id="story-0" multiline placeholder="Enter your life story" pattern="[\s\S]{0,1000}">
  <sp-help-text slot="help-text">1000 character limit</sp-help-text>
  <sp-help-text slot="negative-help-text">
    Exceeded 1000 character limit
  </sp-help-text>
</sp-textfield>
A textarea must have a label in order to be accessible. A label can be provided either via the `label` attribute or with an `<sp-field-label>` element.

<sp-textfield label="questions" multiline placeholder="Do you have any questions?"></sp-textfield>

<sp-field-label for="comments">Comments</sp-field-label>
<sp-textfield id="comments" multiline></sp-textfield>
Help text can be accessibly associated with an `<sp-textfield multiline>` element by using the `help-text` or `negative-help-text` slots. When using the `negative-help-text` slot, `<sp-textfield multiline>` will self manage the presence of this content based on the value of the `invalid` property on your `<sp-textfield multiline>` element. Content within the `help-text` slot will be shown by default. When your `<sp-textfield multiline>` should receive help text based on state outside of the complexity of `invalid` or not, manage the content addressed to the `help-text` from above to ensure that it displays the right messaging and possesses the right `variant`. See help text for more information.

<sp-field-label for="feedback">Feedback</sp-field-label>
<sp-textfield id="feedback" multiline pattern=".{0,500}">
  <sp-help-text slot="help-text">500 character limit</sp-help-text>
  <sp-help-text slot="negative-help-text">
    Exceeded character limit
  </sp-help-text>
</sp-textfield>
Use the `placeholder` attribute to include placeholder text. **Note**: Placeholder text should not be used as a replacement for a label or help text.

<sp-field-label for="goal">Professional goal</sp-field-label>
<sp-textfield id="goal" multiline placeholder="I would like to..."></sp-textfield>Small<sp-field-label size="s" for="story-s">Background</sp-field-label>
<sp-textfield size="s" id="story-s" multiline placeholder="Enter your life story">
  <sp-help-text slot="help-text">1000 character limit</sp-help-text>
  <sp-help-text slot="negative-help-text">
    Exceeded 1000 character limit
  </sp-help-text>
</sp-textfield>Medium<sp-field-label for="story-m">Background</sp-field-label>
<sp-textfield id="story-m" multiline placeholder="Enter your life story">
  <sp-help-text slot="help-text">1000 character limit</sp-help-text>
  <sp-help-text slot="negative-help-text">
    Exceeded 1000 character limit
  </sp-help-text>
</sp-textfield>Large<sp-field-label size="l" for="story-l">Background</sp-field-label>
<sp-textfield size="l" id="story-l" multiline placeholder="Enter your life story">
  <sp-help-text slot="help-text">1000 character limit</sp-help-text>
  <sp-help-text slot="negative-help-text">
    Exceeded 1000 character limit
  </sp-help-text>
</sp-textfield>Extra Large<sp-field-label size="xl" for="story-xl">Background</sp-field-label>
<sp-textfield size="xl" id="story-xl" multiline placeholder="Enter your life story">
  <sp-help-text slot="help-text">1000 character limit</sp-help-text>
  <sp-help-text slot="negative-help-text">
    Exceeded 1000 character limit
  </sp-help-text>
</sp-textfield>
The quiet style works best when a clear layout (vertical stack, table, grid) assists in a user's ability to parse the element. Too many quiet components in a small space can be hard to read.

<sp-field-label for="story-3">Message</sp-field-label>
<sp-textfield id="message" multiline placeholder="Write your message..." quiet></sp-textfield>
By default the text area has a fixed height and will scroll when text entry goes beyond the available space. With the use of the `grows` attribute the text area will grow to accommodate the full content of the element.

<div style="display: flex; flex-wrap: wrap; gap: 20px;">
  <div style="overflow: scroll">
    <sp-field-label for="pinocchio-1">Tell me a story</sp-field-label>
    <sp-textfield id="pinocchio-1" multiline value="Pinocchio eats sugar, but refuses to take medicine. When the undertakers come for him, he drinks the medicine and feels better. Afterwards he tells a lie and, in punishment, his nose grows longer and longer." ></sp-textfield>
  </div>
  <div>
    <sp-field-label for="pinocchio-2">Tell me a story</sp-field-label>
    <sp-textfield id="pinocchio-2" grows multiline value="Pinocchio eats sugar, but refuses to take medicine. When the undertakers come for him, he drinks the medicine and feels better. Afterwards he tells a lie and, in punishment, his nose grows longer and longer. As soon as the three doctors had left the room, the Fairy went to Pinocchio’s bed and, touching him on the forehead, noticed that he was burning with fever." ></sp-textfield>
  </div>
  <div>
    <sp-field-label for="pinocchio-3">Tell me a story</sp-field-label>
    <sp-textfield id="pinocchio-3" grows multiline value="Pinocchio eats sugar, but refuses to take medicine. When the undertakers come for him, he drinks the medicine and feels better. Afterwards he tells a lie and, in punishment, his nose grows longer and longer. As soon as the three doctors had left the room, the Fairy went to Pinocchio’s bed and, touching him on the forehead, noticed that he was burning with fever." quiet ></sp-textfield>
  </div>
</div>
Dictate the validity state of the text entry with the `valid` attribute.

<sp-field-label for="description-1" required>
  Product description
</sp-field-label>
<sp-textfield id="description-1" multiline valid></sp-textfield>
Dictate the invalidity state of the text entry with the `invalid` attribute.

<sp-field-label for="description-2" required>
  Product description
</sp-field-label>
<sp-textfield id="description-2" multiline invalid></sp-textfield>
Textareas support standard form input behaviors:

*   **Text input**: Users can type and edit multiline text
*   **Scrolling**: Content scrolls vertically when it exceeds the visible area
*   **Resizing _(optional)_**: Can be resized by users when the `grows` attribute is not set
*   **Form integration**: Works with standard HTML forms and validation

Self managed<sp-field-label for="e-words-0">Words that start with "E"</sp-field-label>
<sp-textfield multiline id="e-words-0" pattern="[Ee]\w+(\s[Ee]\w+)*$" value="Elephant Engineer Echo">
  <sp-help-text slot="help-text">Words can be space-separated.</sp-help-text>
  <sp-help-text slot="negative-help-text">
    Words must start with the letter "E".
  </sp-help-text>
</sp-textfield>Managed from above<sp-field-label for="e-words-1">Words that start with "E"</sp-field-label>
<sp-textfield multiline id="e-words-1" pattern="[Ee]\w+(\s[Ee]\w+)*$" value="Elephant Engineer Echo" oninput=' const helpText = this.querySelector(`[slot="help-text"]`); const val = this.value; const notE = val.match(/\s[^Ee]\w*/) || val.match(/^[^Ee]\w+\s/); const notSeparated = val.match(/[Ee]\w+[^\w\s][Ee]\w+$/); if (!this.invalid) { helpText.textContent = `Words can be space-separated.`; helpText.variant = `neutral`; } else { helpText.variant = `negative`; if(notE && notSeparated) { helpText.textContent = `Words must be space-separated and start with the letter "E".`; } else if(notE) { helpText.textContent = `Words must start with the letter "E".`; } else { helpText.textContent = `Words must be space-separated.`; } } '>
  <sp-help-text slot="help-text">Words can be space-separated.</sp-help-text>
</sp-textfield>
Every textarea must have an associated label for accessibility. Use either:

*   The `label` attribute on the `<sp-textfield>` element
*   An `<sp-field-label>` element with a `for` attribute that matches the textarea's `id`

*   Use Tab to move focus to and from the textarea
*   Use Enter to create new lines within the textarea
*   Use arrow keys to navigate within the text content
*   Screen readers announce the textarea label and current value
*   Focus indicators are clearly visible for keyboard users

*   The `aria-multiline="true"` attribute is automatically applied
*   Labels are properly associated with the textarea
*   Help text and validation messages are announced
*   Current value and character count are accessible

 Property  Attribute  Type  Default  Description `allowedKeys``allowed-keys``string``''` A regular expression outlining the keys that will be allowed to update the value of the form control. `autocomplete``autocomplete``| 'list' | 'none' | HTMLInputElement['autocomplete'] | HTMLTextAreaElement['autocomplete'] | undefined` What form of assistance should be provided when attempting to supply a value to the form control 
Note: combobox overrides `autocomplete` intentionally with `aria-autocomplete` values, which is why those values (although invalid for native `autocomplete`) are included here to support the combobox accessibility pattern.

`disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `grows``grows``boolean``false` Whether a form control delivered with the `multiline` attribute will change size vertically to accomodate longer input `invalid``invalid``boolean``false` Whether the `value` held by the form control is invalid. `label``label``string``''` A string applied via `aria-label` to the form control when a user visible label is not provided. `maxlength``maxlength``number``-1` Defines the maximum string length that the user can enter `minlength``minlength``number``-1` Defines the minimum string length that the user can enter `multiline``multiline``boolean``false` Whether the form control should accept a value longer than one line `name``name``string | undefined` Name of the form control. `pattern``pattern``string | undefined` Pattern the `value` must match to be valid `placeholder``placeholder``string``''` Text that appears in the form control when it has no value set `quiet``quiet``boolean``false` Whether to display the form control with no visible background `readonly``readonly``boolean``false` Whether a user can interact with the value of the form control `required``required``boolean``false` Whether the form control will be found to be invalid when it holds no `value` `rows``rows``number``-1` The specific number of rows the form control should provide in the user interface `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `valid``valid``boolean``false` Whether the `value` held by the form control is valid. `value``value``string | number` The value held by the form control 

Name  Description `help-text` default or non-negative help text to associate to your form element `negative-help-text` negative help text to associate to your form element when `invalid`

Name  Type  Description `change``Event``An alteration to the value of the element has been committed by the user.``input``Event``The value of the element has changed.`
