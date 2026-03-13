# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/RadioGroup.md

# [RadioGroup](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup)

The `RadioGroup` widget contains a set of related `[Radio](https://bryntum.com/docs/gantt/api/#Core/widget/Radio)` button widgets.

For example, to present three choices and have the user select one of them:

```
 {
     type    : 'radiogroup',
     title   : 'Resolve Conflict',
     name    : 'resolution', // optional, will be set to the `ref` or `id` of the widget if not provided
     value   : 'A',  // the default choice
     options : {
         A : 'Keep the original version',
         B : 'Use the new version',
         C : 'Reconcile individual conflicts'
     }
 }
```

Nested Items
------------

Radio buttons can also have a [container](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-container) of additional [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items). These items can be displayed immediately following the field's label (which is the default when there is only one item) or below the radio button. This can be controlled using the [inline](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-inline) config.

In the demo below notice how additional fields are displayed for the checked radio button:

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[clearable](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup#config-clearable)
Set this to `true` so that clicking the currently checked radio button will clear the check from all radio buttons in the group.

[name](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup#config-name)
The name by which this widget's [value](https://bryntum.com/docs/gantt/api/#Core/widget/RadioGroup#property-value) is accessed using the parent container's [values](https://bryntum.com/docs/gantt/api/#Core/widget/Container#property-values).

It is used to set the [name](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-name) of the child [radio buttons](https://bryntum.com/docs/gantt/api/#Core/widget/Radio).

If not provided, it will be set to the `ref` or `id` of the widget.

[options](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup#config-options)
The set of radio button options for this radio button group. This is a shorthand for defining these in the [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items). The keys of this object hold the radio button's [checkedValue](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-checkedValue) while the object values are a string for the radio button's [text](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-text) or a config object for that radio button.

The [value](https://bryntum.com/docs/gantt/api/#Core/widget/RadioGroup#property-value) of this radio button group will be one of the keys in this object or `null` if no radio button is checked.

For example, consider the following configuration:

```
 {
     type    : 'radiogroup',
     name    : 'resolution',
     value   : 'A',
     options : {
         A : 'Keep the original version',
         B : 'Use the new version',
         C : 'Reconcile individual conflicts'
     }
 }
```

The above is equivalent to this configuration below using [items](https://bryntum.com/docs/gantt/api/#Core/widget/RadioGroup#config-items):

```
 {
     type  : 'radiogroup',
     items : [{
         text         : 'Keep the original version',
         name         : 'resolution',
         ref          : 'resolution_A',
         checked      : true,
         checkedValue : 'A'
     }, {
         text         : 'Use the new version',
         name         : 'resolution',
         ref          : 'resolution_B',
         checkedValue : 'B'
     }, {
         text         : 'Reconcile individual conflicts',
         name         : 'resolution',
         ref          : 'resolution_C',
         checkedValue : 'C'
     }]
 }
```

[value](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup#config-value)
This property corresponds to the [checkedValue](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-checkedValue) of the currently [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#property-checked) radio button.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRadioGroup](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup#property-isRadioGroup)
Identifies an object as an instance of [RadioGroup](https://bryntum.com/docs/gantt/api/#Core/widget/RadioGroup) class, or subclass thereof.

[isRadioGroup](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup#property-isRadioGroup-static)
Identifies an object as an instance of [RadioGroup](https://bryntum.com/docs/gantt/api/#Core/widget/RadioGroup) class, or subclass thereof.

[value](https://bryntum.com/docs/gantt/api/Core/widget/RadioGroup#property-value)
This property corresponds to the [checkedValue](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-checkedValue) of the currently [checked](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#property-checked) radio button.
