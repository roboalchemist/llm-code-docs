# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Checkbox.md

# [Checkbox](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox)

Checkbox field, wraps `<input type="checkbox">`.

Color can be specified, and you can optionally configure [text](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-text) to display in a label to the right of the checkbox in addition to a standard field [label](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-label):

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column).

Nested Items
------------

A checkbox can also have a [container](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-container) of additional [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items). These items can be displayed immediately following the field's label (which is the default when there is only one item) or below the checkbox. This can be controlled using the [inline](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-inline) config.

In the demo below notice how additional fields are displayed when the checkboxes are checked:

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoCollapse](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#config-autoCollapse)
Specify `true` to automatically [collapse](https://bryntum.com/docs/gantt/api/#Core/widget/FieldContainer#config-collapsed) the field's [container](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-container) when the field is not [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#property-checked).

Alternatively, this can be a function that returns the desired `collapse` state when passed the field instance as its one parameter.

[text](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#config-text)
Text to display on checkbox label

[checkedValue](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#config-checkedValue)
The value to provide for this widget in [values](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-values) when it is [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#property-checked). A value of `undefined` will cause this widget not to include its value when checked.

[uncheckedValue](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#config-uncheckedValue)
The value to provide for this widget in [values](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-values) when it is not [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#property-checked).

A value of `undefined` will cause this widget to not include its value when it is unchecked.

[checked](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#config-checked)
The checked state. The same as `value`.

[color](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#config-color)
Checkbox color, must have match in CSS

[value](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#config-value)
The value of the checkbox. This is the same as `checked`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCheckbox](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#property-isCheckbox)
Identifies an object as an instance of [Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox) class, or subclass thereof.

[isCheckbox](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#property-isCheckbox-static)
Identifies an object as an instance of [Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox) class, or subclass thereof.

[name](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#property-name)
Get/set label

[checked](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#property-checked)
The checked state. The same as `value`.

[value](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#property-value)
The value of the checkbox. This is the same as `checked`.

## Functions

Functions are methods available for calling on the class

[check](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#function-check)
Check the box

[uncheck](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#function-uncheck)
Uncheck the box

[toggle](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#function-toggle)
Toggle checked state. If you want to force a certain state, assign to [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#property-checked) instead.

[internalOnChange](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#function-internalOnChange)
Triggers events when user toggles the checkbox

[triggerChange](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#function-triggerChange)
Triggers events when checked state is changed

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[click](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#event-click)
Fires when the checkbox is clicked

[beforeChange](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#event-beforeChange)
Fired before checkbox is toggled. Returning false from a listener prevents the checkbox from being toggled.

[action](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#event-action)
User performed the default action (toggled the checkbox)

[change](https://bryntum.com/docs/gantt/api/Core/widget/Checkbox#event-change)
Fired when checkbox is toggled
