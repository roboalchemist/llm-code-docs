# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/CheckboxGroup.md

# [CheckboxGroup](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup)

The `CheckboxGroup` widget contains a set of related `[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)` widgets.

For example, to present three choices and have the user select one or more of them:

```
 const checkboxGroup = new CheckboxGroup({
     appendTo : document.body,
     title    : 'Select cities',
     name     : 'cities',
     value    : 'London',  // the default choice
     options  : {
         London    : 'London',
         Madrid    : 'Madrid',
         Stockholm : 'Stockholm',
         Sydney    : 'Sydney'
     }
 });
```

The [name](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#config-name) config is required for this widget, and it will be assigned to all checkboxes created by processing the [options](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#config-options) config.

Vertical or horizontal layout
-----------------------------

The default orientation is vertical, but you can change it to horizontal by setting the [inline](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#config-inline) config to `true`.

Disabled
--------

Validation
----------

You can set [requiredSelectedOptions](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-requiredSelectedOptions), [minSelectedOptions](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-minSelectedOptions) and [maxSelectedOptions](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-maxSelectedOptions) to force users to select the right amount of options.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[options](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#config-options)
The set of options for this checkbox group. The keys of this object hold the checkbox's [checkedValue](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-checkedValue) while the object values are a string for the checkbox's [text](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-text) or a config object for that checkbox.

The [value](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-value) of this checkbox group will be one of the keys in this object or `null` if no checkbox is checked.

Example:

```
 {
     type    : 'checkboxgroup',
     name    : 'resolution',
     value   : 'A',
     title   : 'Allergies',
     options : {
         A : 'Gluten',
         B : 'Bacon',
         C : 'Lactose',
         D : 'Fish'
     }
 }
```

[requiredSelectedOptions](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#config-requiredSelectedOptions)
The number of options the user is required to select for this field to be valid. See also [minSelectedOptions](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-minSelectedOptions) and [maxSelectedOptions](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-maxSelectedOptions) if you would like to use a range.

[minSelectedOptions](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#config-minSelectedOptions)
The minimum number of options to select

[maxSelectedOptions](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#config-maxSelectedOptions)
The maximum number of options to select

[value](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#config-value)
This property corresponds to the [checkedValue](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-checkedValue) of all the currently [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#property-checked) checkboxes.

Accepts a comma-separated string representing the checked values.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCheckboxGroup](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#property-isCheckboxGroup)
Identifies an object as an instance of [CheckboxGroup](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup) class, or subclass thereof.

[isCheckboxGroup](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#property-isCheckboxGroup-static)
Identifies an object as an instance of [CheckboxGroup](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup) class, or subclass thereof.

[requiredSelectedOptions](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#property-requiredSelectedOptions)
The number of options the user is required to select for this field to be valid. See also [minSelectedOptions](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-minSelectedOptions) and [maxSelectedOptions](https://bryntum.com/docs/gantt/api/#Core/widget/CheckboxGroup#property-maxSelectedOptions) if you would like to use a range.

[minSelectedOptions](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#property-minSelectedOptions)
The minimum number of options to select

[maxSelectedOptions](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#property-maxSelectedOptions)
The maximum number of options to select

[value](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#property-value)
This property corresponds to the [checkedValue](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#config-checkedValue) of all the currently [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox#property-checked) checkboxes.

Accepts a comma-separated string representing the checked values.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeChange](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#event-beforeChange)
Fired before one of the checkboxes is toggled, return `false` to prevent the action.

[change](https://bryntum.com/docs/gantt/api/Core/widget/CheckboxGroup#event-change)
Fired when one of the checkboxes is toggled.
