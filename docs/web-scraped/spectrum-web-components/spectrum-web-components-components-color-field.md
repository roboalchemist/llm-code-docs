# Source: https://opensource.adobe.com/spectrum-web-components/components/color-field/

Title: Color Field: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/color-field/

Markdown Content:
`<sp-color-field>` elements are textfields that allow users to input custom color values. They support multiple color formats including `HEX`, `RGB`, `HSL`, `HSV`, and shorthand `HEX` formats, providing a flexible interface for color selection in applications.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/color-field?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/color-field?style=for-the-badge)

yarn add @spectrum-web-components/color-field
Import the side effectful registration of `<sp-color-field>` via:

import '@spectrum-web-components/color-field/sp-color-field.js';
When looking to leverage the `ColorField` base class as a type and/or for extension purposes, do so via:

import { ColorField } from '@spectrum-web-components/color-field';
The color field consists of several key parts:

*   **Input field**: The main text input area where users can type color values
*   **Color handle**: An optional visual indicator showing the current color (when `view-color` attribute is enabled)
*   **Validation feedback**: Visual indicators for valid and invalid color inputs
*   **Size variations**: Different size options to match your design requirements

<sp-color-field value="#ffff00"></sp-color-field>Small<sp-color-field size="s" value="#ffff00"></sp-color-field>Medium<sp-color-field size="m" value="#ffff00"></sp-color-field>Large<sp-color-field size="l" value="#ffff00"></sp-color-field>Xtra Large<sp-color-field size="xl" value="#ffff00"></sp-color-field>
When `view-color` is true, the color handle will be rendered. This is useful for development and debugging purposes.

<sp-color-field view-color value="#f00"></sp-color-field>
A quiet color field provides a more subtle appearance:

<sp-color-field quiet value="#e6e600"></sp-color-field>
The default state of the color field, ready for user input:

<sp-color-field value="#ffff00"></sp-color-field>
A readonly color field that displays the color value but prevents user modification:

<sp-color-field readonly value="#ffff00"></sp-color-field>
If the input value is not a valid color, `<sp-color-field>` will not accept it and may show validation feedback:

<sp-color-field value="not a color"></sp-color-field>
The `<sp-color-field>` component accepts color values in various formats: `HEX`, `RGB`, `HSL`, `HSV`, and shorthand `HEX`

For a complete list of supported color formats, see the ColorController documentation.

HEX
A hexadecimal color is specified with: `#RRGGBB`. `RR` (red), `GG` (green) and `BB` (blue) are hexadecimal integers between `00` and `FF` specifying the intensity of the color.

<sp-color-field view-color value="#ff0000"></sp-color-field>Shorthand HEX
Shorthand hexadecimal color values are also supported. `#RGB` is a shorthand for `#RRGGBB`. In the shorthand form, `R` (red), `G` (green), and `B` (blue) are hexadecimal characters between `0` and `F`. Each character is repeated to create the full 6-digit color code. For example, `#123` would expand to `#112233`.

<sp-color-field view-color value="#f00"></sp-color-field>RGB
An RGB color value is specified with: rgb(red, green, blue). Each parameter defines the intensity of the color with a value between 0 and 255.

<sp-color-field view-color value="rgb(255,0,0)"></sp-color-field>RGBA
An RGBA color value is specified with: `rgba(red, green, blue, alpha)`. The `alpha` parameter is a number between 0.0 (fully transparent) and 1.0 (fully opaque).

<sp-color-field view-color value="rgba(0,255,0,0.3)"></sp-color-field>HSL
An HSL color value is specified with: hsl(hue, saturation, lightness). Hue is a degree on the color wheel from 0 to 360. 0 is red, 120 is green, and 240 is blue. Saturation and lightness are percentages.

<sp-color-field view-color value="hsl(234, 70%, 50%)"></sp-color-field>HSV
An HSV color value is specified with: hsv(hue, saturation, value). Hue is a degree on the color wheel from 0 to 360. 0 is red, 120 is green, and 240 is blue. Saturation and value are percentages.

<sp-color-field view-color value="hsv(0, 70%, 50%)"></sp-color-field>
The `<sp-color-field>` component fires two types of events for color value changes:

*   **`input` event**: Fired when the value of the color-field has changed (fires on every keystroke)
*   **`change` event**: Fired when an alteration to the value of the color-field has been committed by the user (fires when the user finishes editing)

You can listen for these events to react to changes in the color value:

const colorField = document.querySelector('sp-color-field');

colorField.addEventListener('input', (event) => {
  console.log('Color value changed:', event.target.value);
});

colorField.addEventListener('change', (event) => {
  console.log('Color value committed:', event.target.value);
});
The `<sp-color-field>` component provides comprehensive accessibility support:

*   **Tab Navigation**: The color field is keyboard accessible and can be navigated to using the Tab key
*   **Input Validation**: Invalid color values are clearly indicated to assistive technologies
*   **Focus Management**: Proper focus indicators are provided for keyboard users

The `<sp-color-field>` inherits comprehensive focus management capabilities from the `TextfieldBase` class:

*   **Focus Element**: The component automatically delegates focus to the underlying input element, ensuring proper keyboard navigation
*   **Focus State Tracking**: The component tracks focus state with the `focused` property, which is reflected as an attribute for styling
*   **Focus Event Handling**: Proper focus and blur event handling ensures accessibility compliance
*   **Tab Index Management**: Automatic tab index management ensures the component is properly included in the tab order
*   **Focus Delegation**: The component properly delegates focus to the underlying input element for keyboard navigation

*   **ARIA Labels**: The component uses appropriate ARIA attributes to describe its purpose and state
*   **Value Announcements**: Changes to the color value are announced to screen readers
*   **Validation Feedback**: Invalid input states are communicated to assistive technologies

*   **Color Contrast**: The component ensures sufficient contrast for text and visual elements
*   **Color Independence**: The component works effectively for users with color vision deficiencies
*   **Alternative Input**: Multiple color format support provides flexibility for different user needs

*   **Provide Labels**: Always include a descriptive label for the color field to provide context
*   **Use View Color**: Enable the `view-color` attribute to provide visual feedback alongside text input
*   **Validate Input**: Handle invalid color inputs gracefully and provide clear feedback to users

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/color-handle@1.11.2
    *   @spectrum-web-components/textfield@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/textfield@1.11.1
    *   @spectrum-web-components/color-handle@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/textfield@1.11.0
    *   @spectrum-web-components/color-handle@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/color-handle@1.10.0
    *   @spectrum-web-components/textfield@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.9.1
    *   @spectrum-web-components/textfield@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies [`72d807c`, `14ebeb9`]: 
    *   @spectrum-web-components/textfield@1.9.0
    *   @spectrum-web-components/color-handle@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.8.0
    *   @spectrum-web-components/textfield@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies [`cde976d`]: 
    *   @spectrum-web-components/textfield@1.7.0
    *   @spectrum-web-components/color-handle@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies [`9e15a66`]: 
    *   @spectrum-web-components/textfield@1.6.0
    *   @spectrum-web-components/color-handle@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   #5322`e19e55f` Thanks @blunteshwar! - Fix Color Handle Positioning in Scrollable Containers

*   Updated dependencies [`165a904`]: 
    *   @spectrum-web-components/color-handle@1.5.0
    *   @spectrum-web-components/textfield@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   #5246`e247de9` Thanks @blunteshwar! - Alpha values for hex color formats wil be represented using hex instead of decimal

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.4.0
    *   @spectrum-web-components/textfield@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/color-handle@1.3.0
    *   @spectrum-web-components/textfield@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **reactive-controllers:** Migrate to Colorjs from Tinycolor (#4713) (9d740f0)

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

**Note:** Version bump only for package @spectrum-web-components/color-field

*   **color-field:** added missing dependencies (#4141) (b3bb23a)

*   **color-field:** add color-field package (#3870) (5081634)

 Property  Attribute  Type  Default  Description `allowedKeys``allowed-keys``string``''` A regular expression outlining the keys that will be allowed to update the value of the form control. `autocomplete``autocomplete``| 'list' | 'none' | HTMLInputElement['autocomplete'] | HTMLTextAreaElement['autocomplete'] | undefined` What form of assistance should be provided when attempting to supply a value to the form control 
Note: combobox overrides `autocomplete` intentionally with `aria-autocomplete` values, which is why those values (although invalid for native `autocomplete`) are included here to support the combobox accessibility pattern.

`disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `grows``grows``boolean``false` Whether a form control delivered with the `multiline` attribute will change size vertically to accomodate longer input `invalid``invalid``boolean``false` Whether the `value` held by the form control is invalid. `label``label``string``''` A string applied via `aria-label` to the form control when a user visible label is not provided. `maxlength``maxlength``number``-1` Defines the maximum string length that the user can enter `minlength``minlength``number``-1` Defines the minimum string length that the user can enter `multiline``multiline``boolean``false` Whether the form control should accept a value longer than one line `name``name``string | undefined` Name of the form control. `pattern``pattern``string | undefined` Pattern the `value` must match to be valid `placeholder``placeholder``string``''` Text that appears in the form control when it has no value set `quiet``quiet``boolean``false` Whether to display the form control with no visible background `readonly``readonly``boolean``false` Whether a user can interact with the value of the form control `required``required``boolean``false` Whether the form control will be found to be invalid when it holds no `value` `rows``rows``number``-1` The specific number of rows the form control should provide in the user interface `tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `valid``valid``boolean``false` Whether the `value` held by the form control is valid. `value``value``string | number` The value held by the form control `viewColor``view-color``boolean``false`

Name  Type  Description `change``Event``An alteration to the value of the color-field has been committed by the user.``input``Event``The value of the color-field has changed.`
