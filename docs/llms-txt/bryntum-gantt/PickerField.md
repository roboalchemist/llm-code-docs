# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/PickerField.md

# [PickerField](https://bryntum.com/docs/gantt/api/Core/widget/PickerField)

Base class used for [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo), [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField), and [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField). Displays a picker ([List](https://bryntum.com/docs/gantt/api/#Core/widget/List), [DatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker)) anchored to the field.

This field's subclasses can be used as editors for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). Used by the Priority column in this demo:

When focused by means of _touch_ tapping on the trigger element (eg, the down arrow on a Combo) on a tablet, the keyboard will not be shown by default to allow for interaction with the dropdown.

A second tap on the input area will then show the keyboard if required.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[editable](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#config-editable)
User can edit text in text field (otherwise only pick from attached picker)

[pickerAlignElement](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#config-pickerAlignElement)
The name of the element property to which the picker should size and align itself.

[autoExpand](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#config-autoExpand)
Configure as `true` to have the picker expand upon focus enter.

[picker](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#config-picker)
Configuration object for the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) on initialization. Returns the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) instance at runtime.

A config object which is merged into the generated picker configuration on initialization to allow specific use cases to override behaviour. For example:

```
    picker: {
        align: {
            anchor: true
        }
    }
```

Returns the picker instance at runtime.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPickerField](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#property-isPickerField)
Identifies an object as an instance of [PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField) class, or subclass thereof.

[isPickerField](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#property-isPickerField-static)
Identifies an object as an instance of [PickerField](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField) class, or subclass thereof.

[picker](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#property-picker)
Configuration object for the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) on initialization. Returns the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) instance at runtime.

A config object which is merged into the generated picker configuration on initialization to allow specific use cases to override behaviour. For example:

```
    picker: {
        align: {
            anchor: true
        }
    }
```

Returns the picker instance at runtime.

## Functions

Functions are methods available for calling on the class

[eachWidget](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#function-eachWidget)
Iterate over all widgets owned by this widget and any descendants.

_Note_: Due to this method aborting when the function returns `false`, beware of using short form arrow functions. If the expression executed evaluates to `false`, iteration will terminate.

_Due to the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField#config-picker) config being a lazy config and only being converted to be a `List` instance just before it's shown, the picker will not be part of the iteration before it has been shown once_.

[onEditComplete](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#function-onEditComplete)
Check if field value is valid

[internalOnKeyEvent](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#function-internalOnKeyEvent)
Allows using arrow keys to open/close list. Relays other keypresses to list if open.

[onTriggerClick](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#function-onTriggerClick)
User clicked trigger icon, toggle list.

[togglePicker](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#function-togglePicker)
Toggle the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField#property-picker) visibility

[showPicker](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#function-showPicker)
Show the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField#property-picker)

[hidePicker](https://bryntum.com/docs/gantt/api/Core/widget/PickerField#function-hidePicker)
Hide picker
