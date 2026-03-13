# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Field.md

# [Field](https://bryntum.com/docs/gantt/api/Core/widget/Field)

Base class for [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField) and [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField). Not to be used directly.

Most subclasses can be used as editors for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). The most popular are:

* [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)
* [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)
* [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)
* [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField)
* [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[skipValidation](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-skipValidation)
Set to `true`, completely bypasses validation logic (could be userful if your field is not `editable` to the user).

[placeholder](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-placeholder)
Text to display in empty field.

[value](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-value)
Default value

[name](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-name)
Name of the field which is used as a key to get/set values from/to the field. Used prior to [ref](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-ref) and [id](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-id) in [Container.values](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-values).

The config is useful when the field is used in EventEditor or TaskEditor to load/save values automatically.

[labels](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-labels)
The labels to add either before or after the input field. Each label may have the following properties:

* `html` The label text.
* `align` `'start'` or `'end'` which end of the field the label should go.

[required](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-required)
Configure as `true` to indicate that a `null` field value is to be marked as invalid. This will optionally append a \* to the field label if [showRequiredIndicator](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-showRequiredIndicator) is set.

[showRequiredIndicator](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-showRequiredIndicator)
`true` to automatically display a \* after the label for this field when it is [required](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-required).

[clearable](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-clearable)
Show a trigger to clear field, if this field is not [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-readOnly). The trigger is available in the [triggers](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-triggers) object under the name `clear`. May also be an object which configures the `clear` [trigger](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-triggers).

[revertOnEscape](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-revertOnEscape)
If this field is not [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-readOnly), then setting this option means that pressing the `ESCAPE` key after editing the field will revert the field to the value it had when the user focused the field. If the field is _not_ changed from when focused, the [clearable](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-clearable) behaviour will be activated.

[hint](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-hint)
An optional string to display inside the input field as an overlay. This can be useful for displaying a field's units.

This config is ignored if [hintHtml](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-hintHtml) is set.

For example:

```
 {
     type  : 'numberfield',
     label : 'Temperature',
     hint  : '°C'
 }
```

This config can be set to a function to dynamically generate the `hint` text:

```
 {
     type  : 'numberfield',
     label : 'Duration',
     hint  : ({ value }) => (value === 1) ? 'Day' : 'Days'
 }
```

The function is passed an object with the following properties:

* `source` A reference to the field instance.
* `value` The current value of the field.

A `hint` function will be called when the field changes value.

[hintHtml](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-hintHtml)
This config is similar to [hint](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-hint) except that this config is used to display HTML content. Since this can allow malicious content to be executed, be sure not to include user-entered data or to encode such data (see [encodeHtml](https://bryntum.com/docs/gantt/api/#Core/helper/StringHelper#function-encodeHtml-static)).

If this config is set, [hint](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-hint) is ignored.

For example:

```
 {
     type     : 'numberfield',
     label    : 'Temperature',
     hintHtml : '<i>°C</i>'
 }
```

This config can be set to a function to dynamically generate the `hintHtml` text:

```
 {
     type     : 'numberfield',
     label    : 'Duration',
     hintHtml : ({ value }) => (value === 1) ? '<i>Day</i>' : '<i>Days</i>'
 }
```

The function is passed an object with the following properties:

* `source` A reference to the field instance.
* `value` The current value of the field.

A `hintHtml` function will be called when the field changes value.

[inputWidth](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-inputWidth)
The width to apply to the `.b-field-inner` element, which encompasses the `input` element and any triggers. If a number is specified, `px` will be used.

[keyStrokeChangeDelay](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-keyStrokeChangeDelay)
The delay in milliseconds to wait after the last keystroke before triggering a change event. Set to 0 to not trigger change events from keystrokes (listen for input event instead to have immediate feedback, change will still be triggered on blur).

If the field is [clearable](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-clearable), the change event fires immediately on receiving the clear gesture.

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-readOnly)
Makes the field unmodifiable by user action. The input area is not editable, and triggers are unresponsive.

This is a wider-acting setting than [editable](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-editable) which _only_ sets the `readOnly` attribute of the `<input>` field.

[PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField)s such as `Combo` and `DateField` can be `editable : false`, but still modifiable through the UI.

[editable](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-editable)
Set to `false` to prevent user from editing the field. For TextFields it is basically the same as setting [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-readOnly), but for PickerFields there is a distinction where it allows you to pick a value but not to type one in the field.

[PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField)s such as `Combo` and `DateField` can be `editable : false`, but still modifiable through the UI.

On mobile devices, [PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField)s are set to `editable : false` by default so that the user must select a value from the dropdown picker rather than having to type a value which will cause a display of the virtual keyboard.

If typing is essential to the functioning of the field, configuring the field with `editable : true` will override this behaviour.

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-triggers)
The triggers to add either before or after the input field. Each property name is the reference by which an instantiated Trigger Widget may be retrieved from the live `triggers` property.

Each trigger may have the following properties:

* `cls` The CSS class to apply.
* `handler` A method in the field to call upon click
* `align` (Optional) `'start'` or `'end'` which end of the field the trigger should go.
* `weight` (Optional) Higher weighted triggers gravitate towards the input field.
* `key` (Optional) The [`key` name](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values) of the key to use as the activation key of this trigger.

```
const textField = new TextField({
  triggers : {
      check : {
          cls : 'fa fa-check',
          handler() {
              ...
          }
      },
      ...
  }
})
```

[highlightExternalChange](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-highlightExternalChange)
Specify `true` to highlight field after external value changes

[autoSelect](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-autoSelect)
Specify `true` to auto select field contents on focus

[autoComplete](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-autoComplete)
Sets the native `autocomplete` property of the underlying input element. For more information, please refer to [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)

[spellCheck](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-spellCheck)
Sets the native `spellcheck` property of the underlying input element. For more information, please refer to [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/spellcheck)

[validateOnInput](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-validateOnInput)
Set to `false` to not highlight a field as invalid while typing, to instead show it on ENTER key press or similar.

[inputAttributes](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-inputAttributes)
Sets custom attributes of the underlying input element. For more information, please refer to [MDN](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)

[inputType](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-inputType)
Sets the `type` attribute of the underlying input element (password, hidden, date, color, etc.).

[inputAlign](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-inputAlign)
Text alignment for the input field.

[tabIndex](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-tabIndex)
The tab index of the input field or fields, or `null` for natural tab order (recommended). Setting to `0` is equivalent to natural tab order, but is unnecessary for fields since they are naturally tabbable (i.e., accessible via the TAB key). Setting to `-1` disables tabbability but allows for focus to be set to the element programmatically.

From [MDN documentation](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex):

**Warning**: You are recommended to only use `0` and `-1` as tabindex values. Avoid using tabindex values greater than 0 and CSS properties that can change the order of focusable HTML elements ([Ordering flex items](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Ordering_flex_items)). Doing so makes it difficult for people who rely on using keyboard for navigation or assistive technology to navigate and operate page content. Instead, write the document with the elements in a logical sequence.

[container](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-container)
The configuration for additional items associated to this field. This is typically used to add contextual fields related to a [checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox) or [radio button](https://bryntum.com/docs/gantt/api/#Core/widget/Radio). See these classes for examples of nested fields.

This config can be provided as an array of widget config objects, an object with named widgets (see [namedItems](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer#config-namedItems), or a config object for the whole [field container](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer).

To determine if the object is a `namedItems` object or a [field container](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer) config, the object is checked for either a `type` or an `items` property. If it has either of these properties, it is a field container config object. Configuring the container is useful for applying [classes](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer#config-cls) or [styles](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer#config-style) to the container as a whole.

For example, to add named items:

```
 new Checkbox({
     text : 'Separate shipping address',
     container : {
         address1 : {
             type : 'textfield'
         },
         address2 : {
             type : 'textfield'
         }
     }
 });
```

To style the container as well, move the items to the `items` property and add `cls`:

```
 new Checkbox({
     text : 'Separate shipping address',
     container : {
         cls   : 'address-form',
         items : {
             address1 : {
                 type : 'textfield'
             },
             address2 : {
                 type : 'textfield'
             }
         }
     }
 });
```

[containerDefaults](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-containerDefaults)
The default configuration for the [container](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-container).

[containValues](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-containValues)
The config controls how the value of nested items are handled when a parent container gets or sets its [values](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-values).

The valid values for this config are:

* `null` (the default) will include the values of this field's items if this field stores its own value.
* `true` to always include the values of this field's items.
* `false` to never include the values of this field's items.
* `'nested'` to include the values of this field's items as a nested object under the field's `name`. This field's `value` is stored as the `'value'` property of that object.
* Any other string is treated as the name of a property on this field. When truthy, the values of this field's items will be included.
* A function can be supplied that must return a value given this field as its sole argument. If that value is truthy, this field's items will be included.

[inline](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-inline)
Set this config to `true` to always display items horizontally along with this field. This assigns an [hbox](https://bryntum.com/docs/gantt/api/#Core/widget/layout/Box) as the [layout](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-layout) to the [container](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-container).

Alternatively, set this config to `false` to wrap this field's items below. This assigns a [VBox](https://bryntum.com/docs/gantt/api/#Core/widget/layout/VBox) as the [layout](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-layout) to the [container](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-container).

This config defaults to `true` if there is exactly one item, and `false` otherwise.

[inputTag](https://bryntum.com/docs/gantt/api/Core/widget/Field#config-inputTag)
If you need to use something else than a default `input` element, as the input element, provide the tag name here. Please note that this is used for advanced usage only, for example when using WebComponents (custom elements), and that the configured element must fulfil the same contract as a regular input element.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isField](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-isField)
Identifies an object as an instance of [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field) class, or subclass thereof.

[isField](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-isField-static)
Identifies an object as an instance of [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field) class, or subclass thereof.

[placeholder](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-placeholder)
Text to display in empty field.

[value](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-value)
Gets or sets the value. The returned type will depend upon the Field subclass.

`TextField` returns a `String`.

`NumberField` returns a `Number`.

`DateField` and `TimeField` return a `Date` object, and `null` if the field is empty.

`Combo` will return a `String` if configured with `items` as a simple string array. Otherwise it will return the [valueField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-valueField) value from the selected record, or `null` if no selection has been made.

[required](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-required)
Configure as `true` to indicate that a `null` field value is to be marked as invalid. This will optionally append a \* to the field label if [showRequiredIndicator](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-showRequiredIndicator) is set.

[showRequiredIndicator](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-showRequiredIndicator)
`true` to automatically display a \* after the label for this field when it is [required](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-required).

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-readOnly)
Makes the field unmodifiable by user action. The input area is not editable, and triggers are unresponsive.

This is a wider-acting setting than [editable](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-editable) which _only_ sets the `readOnly` attribute of the `<input>` field.

[PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField)s such as `Combo` and `DateField` can be `editable : false`, but still modifiable through the UI.

[editable](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-editable)
Set to `false` to prevent user from editing the field. For TextFields it is basically the same as setting [readOnly](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-readOnly), but for PickerFields there is a distinction where it allows you to pick a value but not to type one in the field.

[PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField)s such as `Combo` and `DateField` can be `editable : false`, but still modifiable through the UI.

On mobile devices, [PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField)s are set to `editable : false` by default so that the user must select a value from the dropdown picker rather than having to type a value which will cause a display of the virtual keyboard.

If typing is essential to the functioning of the field, configuring the field with `editable : true` will override this behaviour.

[triggers](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-triggers)
The triggers to add either before or after the input field. Each property name is the reference by which an instantiated Trigger Widget may be retrieved from the live `triggers` property.

Each trigger may have the following properties:

* `cls` The CSS class to apply.
* `handler` A method in the field to call upon click
* `align` (Optional) `'start'` or `'end'` which end of the field the trigger should go.
* `weight` (Optional) Higher weighted triggers gravitate towards the input field.
* `key` (Optional) The [`key` name](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values) of the key to use as the activation key of this trigger.

```
const textField = new TextField({
  triggers : {
      check : {
          cls : 'fa fa-check',
          handler() {
              ...
          }
      },
      ...
  }
})
```

[attributes](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-attributes)
A list of property names to be set in the underlying input element from properties by the same name in this Field object if the value is not `== null`.

[input](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-input)
The input element at the heart if this field

[isValid](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-isValid)
Returns true if the field value is valid

[isEmpty](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-isEmpty)
Returns `true` if this field is empty. That is, if it would violate the [required](https://bryntum.com/docs/gantt/api/#Core/widget/Field#config-required) setting.

This may have different definitions in subclasses from simple text fields.

[isEmptyInput](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-isEmptyInput)
Returns true if the field's input is empty

[validity](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-validity)
Returns the DOM `ValidityState` for this widget's input element, or `null` if there isn't one.

[inputValue](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-inputValue)
A String representation of the value of this field for [syncInputFieldValue](https://bryntum.com/docs/gantt/api/#Core/widget/Field#function-syncInputFieldValue) to use as the input element's value.

Subclasses may override this to create string representations.

For example, [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)'s implementation will format the field date value according to its configured [format](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-format). And [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo)'s implementation will return the [displayField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-displayField) of the selected record.

[needsInputSync](https://bryntum.com/docs/gantt/api/Core/widget/Field#property-needsInputSync)
Returns `true` if the [input](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-input) field needs to be synced with the internal [value](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-value) of this field.

May be overridden in subclasses where this is more complex such as multiSelect Combo with a `ChipView` where the input area does not reflect the field's value.

## Functions

Functions are methods available for calling on the class

[onEditComplete](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-onEditComplete)
Template function which may be implemented by subclasses to synchronize input state and validity state upon completion of the edit.

[getAfterValue](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-getAfterValue)
Returns the input value for this field's input element that will be present if the event carrying the given text is allowed to proceed.

[select](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-select)
Selects the field contents. Optionally may be passed a start and end.

[hasChanged](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-hasChanged)
Compares this field's value with its previous value. May be overridden in subclasses which have more complex value types. See, for example, [DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField).

[syncInputFieldValue](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-syncInputFieldValue)
Called by the base Field class's `set value` to sync the state of the UI with the field's value.

Relies upon the class implementation of `get inputValue` to return a string representation of the value for user consumption and editing.

This method can be overridden.

[internalOnChange](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-internalOnChange)
Trigger event when fields input changes

[internalOnInput](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-internalOnInput)
Trigger event when user inputs into field

[clear](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-clear)
Clears the value of this Field, and triggers the [clear](https://bryntum.com/docs/gantt/api/#Core/widget/Field#event-clear) event.

[onDisabled](https://bryntum.com/docs/gantt/api/Core/widget/Field#function-onDisabled)
Called when disabled state is changed. Used to add or remove 'b-invalid' class for the invalid field based on current disabled state.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[input](https://bryntum.com/docs/gantt/api/Core/widget/Field#event-input)
Fired when the user types into this field.

[change](https://bryntum.com/docs/gantt/api/Core/widget/Field#event-change)
Fired when this field's value changes.

[action](https://bryntum.com/docs/gantt/api/Core/widget/Field#event-action)
User performed default action (typed into this field).

[clear](https://bryntum.com/docs/gantt/api/Core/widget/Field#event-clear)
Fired when this field is [cleared](https://bryntum.com/docs/gantt/api/#Core/widget/Field#function-clear).

This will be triggered when a user clicks this field's clear [trigger](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-triggers)

[trigger](https://bryntum.com/docs/gantt/api/Core/widget/Field#event-trigger)
User clicked one of this field's [triggers](https://bryntum.com/docs/gantt/api/#Core/widget/Field#property-triggers)

## Typedefs

Typedefs are type definitions for the class

[FieldTriggerConfig](https://bryntum.com/docs/gantt/api/Core/widget/Field#typedef-FieldTriggerConfig)
Config object for a field trigger.
