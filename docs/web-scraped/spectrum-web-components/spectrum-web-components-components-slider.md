# Source: https://opensource.adobe.com/spectrum-web-components/components/slider/

Title: Slider: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/slider/

Markdown Content:
`<sp-slider>` allows users to quickly select a value within a range. They should be used when the upper and lower bounds of the range are invariable.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/slider?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/slider?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/slider

Import the side effectful registration of `<sp-slider>` via:

import '@spectrum-web-components/slider/sp-slider.js';

When leveraging the `editable` attribute, the `@spectrum-web-components/number-field/sp-number-field.js` dependency will be asynchronously loaded via a dynamic import to reduce JS payload for applications not leveraging this feature. In the case that you would like to import those transverse dependencies statically, import the side effectful registration of `<sp-slider>` as follows:

import '@spectrum-web-components/slider/sync/sp-slider.js';

When looking to leverage the `Slider` base class as a type and/or for extension purposes, do so via:

import { Slider } from '@spectrum-web-components/slider';
<sp-slider label="Slider Label"></sp-slider>
<sp-slider label="Slider Label - Disabled" disabled></sp-slider>
By default, an `<sp-slider>` element has both a "text" label and a "value" label. The "value" label is output by the element itself based on its state, but the "text" label must be supplied by the consuming developer in order for the `<sp-slider>` to be delivered in an accessible manner.

Either or both of these can be suppressed visually as needed by your application UI, while still fulfilling their role in delivering a quality accessibility tree to the browser. This delivery is controlled by the `label-visibility` attribute (or `labelVisibility` property) which accepts `text`, `value`, or `none` as values.

Use `label-visibility="text"` to suppress the "value" label, use `label-visibility="value"` to suppress the "text" label, or use `label-visibility="none"` to suppress the "text" label. In each case outlined above the content for both labels will be made available to screen readers, so be sure to manage the content delivered to visitors in that context.

Text<sp-slider label="No visible value label" label-visibility="text" value="50"></sp-slider>Value<sp-slider label="No visible text label" label-visibility="value"></sp-slider>None<sp-slider label="No visible labels" label-visibility="none"></sp-slider>
The slider also optionally accepts two or more `<sp-slider-handle>` elements with `slot="handle"`:

<sp-slider step="1" min="0" max="255">
  Output Levels
  <sp-slider-handle slot="handle" name="low" label="Low" value="5" max="next" ></sp-slider-handle>
  <sp-slider-handle slot="handle" name="mid" label="Mid" value="100" min="previous" max="next" ></sp-slider-handle>
  <sp-slider-handle slot="handle" name="high" label="High" value="250" min="previous" ></sp-slider-handle>
</sp-slider>Small<sp-slider label="Slider Label" size="s"></sp-slider>
<sp-slider label="Slider Label - Editable" editable size="s"></sp-slider>Medium<sp-slider label="Slider Label"></sp-slider>
<sp-slider label="Slider Label - Editable" editable></sp-slider>Large<sp-slider label="Slider Label" size="l"></sp-slider>
<sp-slider label="Slider Label - Editable" editable size="l"></sp-slider>Extra Large<sp-slider label="Slider Label" size="xl"></sp-slider>
<sp-slider label="Slider Label - Editable" editable size="xl"></sp-slider>
An `<sp-slider>` element can be paired with an `<sp-number-field>` element via the `editable` attribute. The `<sp-number-field>` will be passed all of the standard options from the `<sp-slider>` element (e.g. `min`, `max`, `formatOptions`, etc.) and will also accept the `hide-stepper` attribute in order to prevent the display of its stepper UI.

The `quiet` attribute applies Quiet styling to the number field when a slider is `editable`.

Editable<sp-slider label="Hours of the day (editable)" editable max="24" min="0" value="7.25" step="0.25" style="--spectrum-slider-editable-number-field-width: 100px;" format-options='{ "style": "unit", "unit": "hour" }'></sp-slider>Editable, hide-stepper<sp-slider label="Angle (editable)" editable hide-stepper min="0" max="360" format-options='{ "style": "unit", "unit": "degree", "unitDisplay": "narrow" }'></sp-slider>Editable, quiet<sp-slider quiet editable value="50"></sp-slider>
<sp-slider quiet editable hide-stepper value="50"></sp-slider>
Use `variant="filled"` to add a filled style to the slider from a starting point to the current value. By default the starting point is the `min` value.

<sp-slider label="Slider Label" max="1" variant="filled" min="0" value=".5" step="0.01"></sp-slider>
<sp-slider label="Slider Label - Disabled" max="1" variant="filled" min="0" value=".5" step="0.01" disabled></sp-slider>
When both `fill-start` and `variant="filled"` are used in `<sp-slider>`, the `fill-start` property defines the starting point. If fill start does not have a number associated with it, the starting point will be the `value`.

Any number (including `0`) can be used as a fill-start value. If a custom normalization function is provided, it will also normalize all fill-related params.

fill-start<sp-slider label="Slider Label" max="1" fill-start variant="filled" min="0" value=".5" step="0.01"></sp-slider>
<sp-slider label="Slider Label" max="1" fill-start variant="filled" min="0" value=".8" step="0.01" disabled></sp-slider>fill-start > value<sp-slider id="fill-start-slider" label="fill-start greater than value" max="1" min="0" value=".3" step="0.1" fill-start="0.7" variant="filled"></sp-slider>fill-start < value<sp-slider id="fill-start-slider" label="Fill Start less than Value" max="1" min="0" value=".7" step="0.1" fill-start="0.25" variant="filled"></sp-slider>fill-start="0" and negative min<sp-slider label="fill-start set to 0" max="1" min="-1" value=".7" step="0.1" fill-start="0" variant="filled"></sp-slider>
With `variant="tick"`, ticks are applied at intervals defined with the `tick-step` attribute. The `tick-labels` attribute will apply labels to the ticks.

Tick with No Labels<sp-slider label="Slider Label" variant="tick" tick-step="5"></sp-slider>
<sp-slider label="Slider Label - Disabled" variant="tick" tick-step="5" disabled></sp-slider>Tick with Labels<sp-slider label="Slider Label" variant="tick" tick-step="5" tick-labels></sp-slider>
<sp-slider label="Slider Label - Disabled" variant="tick" tick-step="5" tick-labels disabled></sp-slider>
With `variant="ramp"`, the slider with increases as it approaches the `max` position.

<sp-slider label="Slider Label" variant="ramp"></sp-slider>
<sp-slider label="Slider Label - Disabled" variant="ramp" disabled></sp-slider>
The `"range"` variant along with two handles to create a range slider. (See slider handle.)

<sp-slider variant="range" step="1" min="0" max="255">
  Output Levels
  <sp-slider-handle slot="handle" name="min" label="Minimum" value="5" ></sp-slider-handle>
  <sp-slider-handle slot="handle" name="max" label="Maximum" value="250" ></sp-slider-handle>
</sp-slider>
An `<sp-slider>` or `<sp-slider-handle>` element will process its numeric value with `new Intl.NumberFormat(this.resolvedLanguage, this.formatOptions).format(this.value)` in order to prepare it for visual delivery in the input. In order to customize this processing supply your own `Intl.NumberFormatOptions` via the `formatOptions` property, or `format-options` attribute as seen below.

`this.resolvedLanguage` represents the language in which the `<sp-slider>` or `<sp-slider-handle>` element is currently being delivered. By default, this value will represent the language established by the `lang` attribute on the root `<html>` element while falling back to `navigator.language` when that is not present. This value can be customized via a language context provided by a parent element that listens for the `sp-language-context` event and supplies updated language settings to the `callback` function contained therein. Applications leveraging the `<sp-theme>` element to manage the visual delivery or text direction of their content will also be provided a reactive context for supplying language information to its descendants.

<sp-slider min="0" max="1" step="0.01" value="0.5" label="Slider Label" format-options='{ "style": "percent" }'></sp-slider>
More advanced formatting is available by specifying a formatting function to the `getAriaHandleText` property on an `sp-slider` or `sp-slider-handle`. Or, for a multi-handle slider, you can format the combined value label for all handles by passing a formatting function to the `getAriaValueText` property on the parent `sp-slider`.

While `Intl.NumberFormatOptions` does support a wide range of units, it is possible to encounter units (e.g. the graphics units of `pixel`, `pixels`, `points`, etc.) that are not supported therein. When this occurs, an `<sp-slider>` element will attempt to polyfill support for this unit. See the following example delivering `{ style: "unit", unit: "px" }` below:

<sp-slider style="width: 200px" value="500" format-options='{ "style": "unit", "unit": "px" }'>
  Document width in pixels
</sp-slider>
Note: the polyfilling done here is very simplistic and is triggered by supplying options that would otherwise cause the `Intl.NumberFormat()` call to throw an error. Once the unsupporting unit of `px` causes the construction of the object to throw, a backup formatter/parser pair will be created without the supplied unit data. When the `style` is set to `unit`, the `unit` value will be adopted as the _static_ unit display. This means that neither pluralization nor translation will be handled within the `<sp-number-field>` element itself. If pluralization or translation is important to the delivered interface, please be sure to handle passing those strings into to element via the `formatOptions` property reactively to the value of the element or locale of that page in question.

Slider will reset to its `default-value` when the user double clicks on the slider handle or if the user presses the `escape` key when the slider handle is focused.

<sp-slider value="50" default-value="20"></sp-slider>
Note: If a slider with `default-value` attribute is contained in a modal and the slider handle is focused then the following interaction will occur on pressing the `escape` key:

*   If the slider value is different from the default value then the slider value will be reset to the default value and the modal will not be closed.
*   If the slider value is equal to the default value then the modal will be closed.

By default, `sp-slider` assumes a linear scale between the `min` and `max` values. For advanced applications, it is sometimes necessary to specify a custom "normalization."

Normalization is the process of converting a slider to a value between 0 and 1 where 0 represents the minimum and 1 represents the maximum. See the "Three Handles Complex" example in the playground.

<sp-slider disabled value="50"></sp-slider>
<sp-slider disabled quiet value="50"></sp-slider>
<sp-slider disabled editable value="50"></sp-slider>
<sp-slider disabled variant="filled" value="50"></sp-slider>
<sp-slider disabled variant="ticks" value="50"></sp-slider>
<sp-slider disabled variant="ramp" value="50"></sp-slider>
The indeterminate attribute will be passed to the internal `<sp-number-field>` element and alter its visual delivery until a change has been made to the `<sp-slider>` element at which point the `change` event that is dispatched can be understood as always removing the indeterminate attribute from the `<sp-slider>`.

<sp-slider indeterminate value="50"></sp-slider>
<sp-slider indeterminate quiet value="50"></sp-slider>
<sp-slider indeterminate editable value="50"></sp-slider>
<sp-slider indeterminate variant="filled" value="50"></sp-slider>
<sp-slider indeterminate variant="ticks" value="50"></sp-slider>
<sp-slider indeterminate variant="ramp" value="50"></sp-slider>
Like the `<input type="range">` element after which the `<sp-slider>` is fashioned, it will dispatch `input` events in a stream culminating with a `change` event (representing the final commit of the `value` to the element) once the user has finished interacting with the element. Both other these events can access the `value` of their dispatching target via `event.target.value`. In this way, a steaming listener pattern similar to the following can prove useful:

const slider = document.querySelector('sp-slider');

const endListener = ({ target }) => {
  target.addEventListener('input', startListener);
  target.removeEventListener('input', streamListener);
  target.removeEventListener('change', endListener);
  console.log(target.value);
};

const streamListener = ({ target }) => {
  console.log(target.value);
};

const startListener = ({ target }) => {
  target.removeEventListener('input', startListener);
  target.addEventListener('input', streamListener);
  target.addEventListener('change', endListener);
  console.log(target.value);
};

slider.addEventListener('input', startListener);
Every slider should have a label. A slider without a label is ambiguous and not accessible. Write the label in sentence case.

In rare cases where context is sufficient and a label doesn't require visibility, make sure to have the design reviewed and approved by an accessibility expert. Use `label-visibility` to set which labels should remain visible, and non-visible labels will still be read by assistive technology.

Multi-handle sliders must always have visible labels to ensure their purpose is clear to all users. Each handle in a multi-handle slider should have:

1.   A descriptive `label` attribute that explains what the handle represents (e.g., "Minimum", "Maximum")
2.   A visible value indicator so users can see the current value of each handle

When using `label-visibility="none"` or `label-visibility="text"` with multi-handle sliders (hiding the value labels), value tooltips will automatically appear on hover and focus to show each handle's current value. This ensures users can still identify individual handle values even when the combined value label is hidden.

<sp-slider label="Output Levels" step="1" min="0" max="255" label-visibility="none">
  <sp-slider-handle slot="handle" name="min" label="Minimum" value="5" ></sp-slider-handle>
  <sp-slider-handle slot="handle" name="max" label="Maximum" value="250" ></sp-slider-handle>
</sp-slider>
For optimal accessibility:

*   Always provide a `label` attribute on each `<sp-slider-handle>` to describe its purpose
*   The slider's value label displays all handle values (e.g., "5 - 250" for a range slider)
*   Screen readers announce the `aria-valuetext` for each handle, which includes the formatted value
*   When value labels are hidden, tooltips appear on hover/focus to display individual handle values

See the WAI-ARIA Slider Pattern and Deque University Slider for additional guidance.

The Tab and Shift+Tab keys are used to navigate to and set focus on the slider control. The Arrow Up (↑) and Arrow Down (↓) keys are used to increment the slider value, respectively.

Because multiple sliders are often used on the same page, the number field in the `editable` slider is designed to not be keyboard focusable via Tab or Shift+Tab keys. (See WAI ARIA APG's Keyboard Navigation Inside Components.) Since the slider itself can already be incremented via the arrow keys, a roving tabindex controller cannot be used within the slider; therefore, the number field will not be keyboard navigable.

Review the accessibility guidelines for the slider handle.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/theme@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/field-label@1.11.2
    *   @spectrum-web-components/number-field@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/theme@1.11.1
    *   @spectrum-web-components/field-label@1.11.1
    *   @spectrum-web-components/number-field@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   #5965`b95e254` Thanks @rubencarvalho! - **Fixed**: Arrow key events now stop propagation when handled by the slider, preventing them from bubbling up to parent elements.

Previously, arrow key events (`ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`) would propagate to ancestor containers even when the slider was actively handling value adjustments. This could cause unintended side effects in layouts or applications that also listen for arrow key events.

*   Updated dependencies [`7af5e8f`, `b95e254`, `f8bdeec`, `9cb816b`]:

    *   @spectrum-web-components/field-label@1.11.0
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/number-field@1.11.0
    *   @spectrum-web-components/theme@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/field-label@1.10.0
    *   @spectrum-web-components/number-field@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/theme@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-label@1.9.1
    *   @spectrum-web-components/number-field@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1
    *   @spectrum-web-components/theme@1.9.1

*   Updated dependencies [`7d23140`, `72d807c`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/field-label@1.9.0
    *   @spectrum-web-components/number-field@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0
    *   @spectrum-web-components/theme@1.9.0

*   #5554`b0570bc` Thanks @augustjk! - Editable sliders will now reliably emit `input` events when interaction starts with the track.

*   Updated dependencies []:

    *   @spectrum-web-components/theme@1.8.0
    *   @spectrum-web-components/number-field@1.8.0
    *   @spectrum-web-components/field-label@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/theme@1.7.0
    *   @spectrum-web-components/number-field@1.7.0
    *   @spectrum-web-components/field-label@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   #5344`02af616` Thanks @renovate! - #​3611 Thanks @​aramos-adobe!

The border radius styles were not being applied to the second instance of the slider track when the offset variant is activated. When the offset is selected, the template structure changes as fill gets added to the slider.

Adding a sibling combinator to track when offset is activated resolved the issue.

*   Updated dependencies [`74386e8`, `9e15a66`]:

    *   @spectrum-web-components/number-field@1.6.0
    *   @spectrum-web-components/theme@1.6.0
    *   @spectrum-web-components/field-label@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`165a904`, `5a3bc6d`]: 
    *   @spectrum-web-components/field-label@1.5.0
    *   @spectrum-web-components/number-field@1.5.0
    *   @spectrum-web-components/theme@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/theme@1.4.0
    *   @spectrum-web-components/field-label@1.4.0
    *   @spectrum-web-components/number-field@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/field-label@1.3.0
    *   @spectrum-web-components/number-field@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0
    *   @spectrum-web-components/theme@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

*   **slider:** make label not disappear when using overlays in Safari (#5118) (191a15b)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   add an optional chromatic vrt action (7d2f840)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **number-field, slider:** ensure cached value is cleared when toggling between different steps (#4846) (1c84c96)
*   **slider:** update slider config to process the tick css correctly (#4905) (7b1dfd0)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** update variant attribute correctly (#4714) (9c22dd6)

*   **slider:** bump css version to increase slider z-index (#4682) (04bba95)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   Silder: adjust fillStart calculation for value=0 and normalization function (#4573) (369fee7), closes #4558

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   **number-field, slider:** floating point roundoff precision bug (#4263) (74480ef)
*   **slider,overlay:** ensure that pointer events in Slider are handled as expected in Overlay (#4438) (db193e8)

*   **number-field, slider:** floating point roundoff precision bug (#4263) (74480ef)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** skip variant="filled" css when fill-start (#4217) (b6d389d)

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **asset:** use core tokens (99e76f4)

*   **slider:** double click on slider handle to reset slider position (#3991) (64c594a)

*   **slider:** revert handle ui at min/max values (#4042) (da13af7)

*   **slider:** high contrast improvements for filled track (#3952) (782560d)

*   **slider:** reimplement gradient slider track application (a10b91e)

*   **slider:** add "fill-start" attribute/property and associated "variant="filled" visual delivery (#3876) (2c3e35e)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** update handle alignment and color application (#3860) (bed73c0)

*   **slider:** align editable slider when no label provided (#3816) (a5f4900)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **infield-button:** add infield-button package (057b885)

*   **number-field:** prevent over excited "change" events (7b93724)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** ensure z-index in Express theme (c0cc655)

*   **slider:** add t-shirt sizing (24dac78)

*   **slider:** ensure first render when no "value" is supplied (eed860b)
*   **slider:** update CSS conversion for more correct visual delivery (99c83e4)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:**#3340 fix visual regression (88e0bda)
*   **slider:** slider input aria-valuetext omits formatOptions for unit #3340 (d5ff7e6)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **number-field:** simplify width management (ef4765a)

*   **base:** ensure streaming listener "streams" on the animation frame (1478db1)

*   **popover:** use core tokens (68328cc)
*   **slider:** use spectrum-tokens (8b1e72c)

**Note:** Version bump only for package @spectrum-web-components/slider

*   add "editable" option to "sp-slider" (e86d7fa)
*   allow tick labels to start counting from "min" (e7e44e3)
*   apply Focuable styles in class extensions (38f7afd)
*   convert the langage resolution workflow to a Reactive Controller (b7781db)
*   correct @element jsDoc listing across library (c97a632)
*   correct slider math in RTL contexts (4d73fa9)
*   ensure browser understandable extensions (f4e59f7)
*   ensure dependencies included in package.json (eb77858)
*   ensure lazily loaded focusElements do not crash (64f2a54)
*   ensure reactivity of resolved language (5863a15)
*   ensure streamingListener ends even if pointercancel not fired (74105f2)
*   fast forward changes in #2905 (3a30b27)
*   flappy Slider/Color Area tests (c769c87)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   include touch-action rule for draggable content (53221da)
*   include touch-action rule for draggable content (3f507e6)
*   manage "lang" via context provided by "sp-theme" (b1e3457)
*   manage updated node types (0517fc1)
*   normalize "event" and "error" argument names (8d382cd)
*   prevent active pointer events when slider toggles to [disabled] (ceb4d74)
*   prevent mobile interactions from triggering the virtual keyboard (d06ad17)
*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)
*   remove right click value setting (a44968d)
*   resolve "updateComplete" with a boolean like LitElement (2ebcd44)
*   simplify touch-action application (d23f735)
*   **slider:** add less visually effectacious style to the slider output when editable (8702294)
*   **slider:** add quiet and indeterminate (8990573)
*   **slider:** allow irregular tick spacing and correct RTL value application (a83f879)
*   **slider:** allow pointer interactions that start at the very begin/end to be tracked (ff8c95c)
*   **slider:** allow slot based label content (d2d474e)
*   **slider:** apply "handle.highlight = true" when using the keyboard to interact with handles (94e6349)
*   **slider:** dispatch synthetic pointerdown event (7dc74af)
*   **slider:** ensure "sp-slider:input" is dispatched appropriately (ded5440)
*   **slider:** ensure min/max/value application order (80e8cb5)
*   **slider:** ensure pointer events on the track and handle act the same (03adb36)
*   **slider:** ensure that handles are upgraded before extracting a model from them (bbbb21f)
*   **slider:** ensure track widths follow dynamic Spectrum CSS values (5ad1c1a)
*   **slider:** ensure value is bound as a property (96bd01a)
*   **slider:** fixes usage of aria-valuetext, adds aria-valuenow (4b25a89)
*   **slider:** make implicit dependency on sp-slider-handle explicit (cb8d84b)
*   **slider:** manage focus more like a native rage input (865115e)
*   **slider:** manage value and max changing in unison (4359fbe)
*   **slider:** prevent pointercancel events by container touch-action (4687d03)
*   **slider:** renamed flag from stepperActive to managed input to allow verified (scroll) input event (89d6ac5)
*   **slider:** response to orientation changes when measuring the bounding box (c1412f1)
*   **slider:** simplify application of the gradient backgrounds (f96a97e)
*   **slider:** support customizing visible label delivery (a55b585)
*   **slider:** support non-supported units in "Intl.numberFormat" (ac32355)
*   **slider:** update a11y tree and default max value (3cbf222)
*   **slider:** use internal "input" for value sanitation (dd588c9)
*   **slider:** use standard "change" and "input" events (59cf786)
*   **slider:** work around Spectrum CSS bug in variant="range" styling (e5810a9)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update consumption of Spectrum CSS for latest version (ed2305b)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update method extension types to match (6eb686f)
*   update side effect listings (8160d3a)
*   update spelling (283d10a)
*   update to latest spectrum-css packages (a5ca19f)
*   use ObserveSlotText mixin to prevent white space from overriding label attribute (610fb4b)
*   use the "browsers" listing in postcss-preset-env (4eaf6a2)

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   delivery dev mode messages in various packages (62370a1)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   multi-handle slider implementation (8d5a743), closes #1385
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **slider:** add "ramp" and "tick" variant support (bb98bb6)
*   **slider:** adds getAriaValueText property, fixes #381 (5800915)
*   **slider:** mouse event fallback from pointer events (b69e7fc)
*   **slider:** support tick labels and tick steps (1ccf8d6)
*   **slider:** update "value" default to match browser native range input (0050f63)
*   **slider:** update spectrum css input (21ebe36)
*   **slider:** use latest @spectrum-css/slider beta (9f29bbe)
*   update lit-* dependencies, wip (377f3c8)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

*   ensure streamingListener ends even if pointercancel not fired (74105f2)
*   fast forward changes in #2905 (3a30b27)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   ensure dependencies included in package.json (eb77858)

*   ensure reactivity of resolved language (5863a15)
*   **slider:** add less visually effectacious style to the slider output when editable (8702294)

*   manage updated node types (0517fc1)

*   **slider:** update "value" default to match browser native range input (0050f63)

**Note:** Version bump only for package @spectrum-web-components/slider

*   convert the langage resolution workflow to a Reactive Controller (b7781db)
*   prevent mobile interactions from triggering the virtual keyboard (d06ad17)

*   update spelling (283d10a)
*   **slider:** renamed flag from stepperActive to managed input to allow verified (scroll) input event (89d6ac5)

**Note:** Version bump only for package @spectrum-web-components/slider

*   include all Dev Mode files in side effects (f70817c)

*   delivery dev mode messages in various packages (62370a1)

*   **slider:** add quiet and indeterminate (8990573)

*   correct slider math in RTL contexts (4d73fa9)

*   update method extension types to match (6eb686f)

*   update consumption of Spectrum CSS for latest version (ed2305b)

*   allow tick labels to start counting from "min" (e7e44e3)
*   prevent active pointer events when slider toggles to [disabled] (ceb4d74)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** ensure that handles are upgraded before extracting a model from them (bbbb21f)

*   simplify touch-action application (d23f735)

*   **slider:** response to orientation changes when measuring the bounding box (c1412f1)

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/slider

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** make implicit dependency on sp-slider-handle explicit (cb8d84b)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** support non-supported units in "Intl.numberFormat" (ac32355)
*   ensure lazily loaded focusElements do not crash (64f2a54)
*   flappy Slider/Color Area tests (c769c87)

*   correct @element jsDoc listing across library (c97a632)

*   add "editable" option to "sp-slider" (e86d7fa)
*   **slider:** support customizing visible label delivery (a55b585)

*   resolve "updateComplete" with a boolean like LitElement (2ebcd44)

**Note:** Version bump only for package @spectrum-web-components/slider

*   manage "lang" via context provided by "sp-theme" (b1e3457)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** apply "handle.highlight = true" when using the keyboard to interact with handles (94e6349)
*   **slider:** work around Spectrum CSS bug in variant="range" styling (e5810a9)

*   multi-handle slider implementation (8d5a743), closes #1385

*   use ObserveSlotText mixin to prevent white space from overriding label attribute (610fb4b)

*   prevent tabindex=-1 elements from placing focus on their host (1ac1293)

*   include touch-action rule for draggable content (53221da)
*   include touch-action rule for draggable content (3f507e6)
*   **slider:** ensure min/max/value application order (80e8cb5)
*   **slider:** ensure pointer events on the track and handle act the same (03adb36)
*   **slider:** ensure value is bound as a property (96bd01a)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** update a11y tree and default max value (3cbf222)

*   remove right click value setting (a44968d)

**Note:** Version bump only for package @spectrum-web-components/slider

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   **slider:** manage focus more like a native rage input (865115e)

*   use the "browsers" listing in postcss-preset-env (4eaf6a2)
*   **slider:** allow irregular tick spacing and correct RTL value application (a83f879)
*   **slider:** allow pointer interactions that start at the very begin/end to be tracked (ff8c95c)
*   **slider:** allow slot based label content (d2d474e)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   **slider:** prevent pointercancel events by container touch-action (4687d03)

*   **action-button:** add action button pattern (03ac00a)
*   **slider:** update spectrum css input (21ebe36)
*   **slider:** use latest @spectrum-css/slider beta (9f29bbe)

*   **slider:** allow irregular tick spacing and correct RTL value application (a83f879)
*   **slider:** allow pointer interactions that start at the very begin/end to be tracked (ff8c95c)
*   **slider:** allow slot based label content (d2d474e)
*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   **slider:** prevent pointercancel events by container touch-action (4687d03)

*   **action-button:** add action button pattern (03ac00a)
*   **slider:** update spectrum css input (21ebe36)
*   **slider:** use latest @spectrum-css/slider beta (9f29bbe)

**Note:** Version bump only for package @spectrum-web-components/slider

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)
*   **slider:** simplify application of the gradient backgrounds (f96a97e)

**Note:** Version bump only for package @spectrum-web-components/slider

*   update to Spectrum CSS v3.0.0 (e8b3d8f)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   ensure browser understandable extensions (f4e59f7)

**Note:** Version bump only for package @spectrum-web-components/slider

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/slider

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** dispatch synthetic pointerdown event (7dc74af)

*   **slider:** use internal "input" for value sanitation (dd588c9)

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

**Note:** Version bump only for package @spectrum-web-components/slider

*   **slider:** fixes usage of aria-valuetext, adds aria-valuenow (4b25a89)

*   **slider:** adds getAriaValueText property, fixes #381 (5800915)

*   apply Focuable styles in class extensions (38f7afd)

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

*   **slider:** ensure track widths follow dynamic Spectrum CSS values (5ad1c1a)
*   **slider:** use standard "change" and "input" events (59cf786)

*   **slider:** ensure "sp-slider:input" is dispatched appropriately (ded5440)

*   **slider:** manage value and max changing in unison (4359fbe)

*   **slider:** add "ramp" and "tick" variant support (bb98bb6)
*   **slider:** mouse event fallback from pointer events (b69e7fc)
*   **slider:** support tick labels and tick steps (1ccf8d6)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/slider

Property  Attribute  Type  Default  Description `defaultValue``default-value``number` Set the default value of the handle. Setting this property will cause the handle to reset to the default value on double click or pressing the `escape` key. `disabled``disabled``boolean``false` Disable this control. It will not receive focus or events `dragging``dragging``boolean``false``editable``editable``boolean` Whether to display a Number Field along side the slider UI `fillStart``fill-start``number | boolean | undefined``formatOptions``format-options``NumberFormatOptions | undefined``hideStepper``hide-stepper``boolean``false` Whether the stepper UI of the Number Field is hidden or not `highlight``highlight``boolean``false``indeterminate``indeterminate``boolean``false` Applies `indeterminate` to the underlying `sp-number-field` when `editable === true`. Is removed on the next `change` event. `label``label``string``''``labelVisibility``label-visibility``'text' | 'value' | 'none' | undefined``max``max``number | 'next' | undefined``100``min``min``number | 'previous' | undefined``0``name``name``string``''``quiet``quiet``boolean``false` Applies `quiet` to the underlying `sp-number-field` when `editable === true`. `step``step``number | undefined``1``tabIndex``tabIndex``number` The tab index to apply to this control. See general documentation about the tabindex HTML property `tickLabels``tick-labels``boolean``false``tickStep``tick-step``number``0``type``type``string``''``value``value``number` By default, the value of a Slider Handle will be halfway between its `min` and `max` values, or the `min` value when `max` is less than `min`. `variant``variant``string`

Name  Description `default slot` @deprecated Text label for the Slider. Use the `label` property instead. `handle` optionally accepts two or more sp-slider-handle elements

Name  Type  Description `change``Event``An alteration to the value of the element has been committed by the user.``input``Event``The value of the element has changed.``sp-slider-handle-ready``CustomEvent`
