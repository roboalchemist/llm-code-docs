# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/FieldFilterPicker.md

# [FieldFilterPicker](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker)

Widget for defining a [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) for use in filtering a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store). Filters consist of `property` (the name of the data field whose values are checked), `operator` (the type of comparison to use), and `value` (the pre-defined value against which to compare the data field value during filtering).

For example:

```
new FieldFilterPicker({
    appendTo : domElement,

    fields: {
        // Allow filters to be defined against the 'age' and 'role' fields in our data
        age       : { title: 'Age', type: 'number' },
        startDate : { title: 'Start Date', type: 'date' }
    },

    filter : {
        property : 'startDate',
        operator : '<',
        value    : new Date()
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[fields](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-fields)
Dictionary of [FieldOption](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#typedef-FieldOption) representing the fields against which filters can be defined, keyed by field name.

If filtering a [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid), consider using [GridFieldFilterPicker](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPicker), which can be configured with an existing [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) instead of, or in combination with, defining fields manually.

Example:

```
fields: {
    // Allow filters to be defined against the 'age' and 'role' fields in our data
    age  : { title: 'Age', type: 'number' },
    role : { title: 'Role', type: 'string' }
}
```

[disabled](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-disabled)
Make the entire picker disabled.

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-readOnly)
Make the entire picker read-only.

[propertyLocked](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-propertyLocked)
Make only the property selector readOnly.

[operatorLocked](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-operatorLocked)
Make only the operator selector readOnly.

[valueLocked](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-valueLocked)
Make only the value input(s) readOnly.

[filter](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-filter)
Configuration object for the [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) displayed and editable in this picker.

Example:

```
{
    property: 'age',
    operator: '=',
    value: 25
}
```

[propertyFieldConfig](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-propertyFieldConfig)
Optional configuration for the property selector [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo).

[operatorFieldConfig](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-operatorFieldConfig)
Optional configuration for the operator selector [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo).

[valueFieldCls](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-valueFieldCls)
Optional CSS class to apply to the value field(s).

[triggerChangeOnInput](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-triggerChangeOnInput)
Whether to raise [change](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#event-change) events as the user types into a value field. If `false`, [change](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#event-change) events will be raised only when the value input field's own `change` event occurs, for example on field blur.

[operators](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-operators)
Overrides the built-in list of operators that are available for selection. Specify operators as an object with data types as keys and lists of operators as values, like this:

```
operators : {
    string : [
        { value : 'empty', text : 'is empty', argCount : 0 },
        { value : 'notEmpty', text : 'is not empty', argCount : 0 }
    ],
    number : [
        { value : '=', text : 'equals' },
        { value : '!=', text : 'does not equal' }
    ],
    date : [
        { value : '<', text : 'is before' }
    ]
}
```

Here `value` is what will be stored in the `operator` field in the filter when selected, `text` is the text displayed in the Combo for selection, and `argCount` is the number of arguments (comparison values) the operator requires. The default argCount if not specified is 1.

**Note:** The operators config is a subset of valid operators described in [CollectionCompareOperator](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#typedef-CollectionCompareOperator). The use of any other operator apart from these is not supported and will lead to unexpected behavior.

[dateFormat](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-dateFormat)
The date format string used to display dates in value input fields. Defaults to the current locale's `FieldFilterPicker.dateFormat` value.

[store](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-store)
Optional {Core.data.Store} against which filters are being defined. This is used to supply options to filter against when using the 'is one of' and 'is not one of' operators.

[valueFieldPlaceholders](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-valueFieldPlaceholders)
Optional [ValueFieldPlaceholders](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#typedef-ValueFieldPlaceholders) object specifying custom placeholder text for value input fields.

[getValueFieldConfig](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#config-getValueFieldConfig)
Optional function that modifies the configuration of value fields shown for a filter. The default configuration is received as an argument and the returned value will be used as the final configuration. For example:

```
getValueFieldConfig : (filter, fieldConfig) => {
    return {
        ...fieldConfig,
        title : fieldName    // Override the `title` config for the field
    };
}
```

The supplied function should accept the following arguments:

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFieldFilterPicker](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#property-isFieldFilterPicker)
Identifies an object as an instance of [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker) class, or subclass thereof.

[isFieldFilterPicker](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#property-isFieldFilterPicker-static)
Identifies an object as an instance of [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker) class, or subclass thereof.

[items](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#property-items)

[operatorArgCountLookup](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#property-operatorArgCountLookup)

## Functions

Functions are methods available for calling on the class

[getUniqueDataValues](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#function-getUniqueDataValues)
Return an array of unique values in the data store for the currently selected field. If no store is configured or no field is selected, returns an empty array.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[change](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#event-change)
Fires when the filter is modified.

## Typedefs

Typedefs are type definitions for the class

[FieldOption](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#typedef-FieldOption)
A field that is available for selection when defining filters.

[ValueFieldPlaceholders](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPicker#typedef-ValueFieldPlaceholders)
A dictionary of value field placeholder strings, keyed by data type.
