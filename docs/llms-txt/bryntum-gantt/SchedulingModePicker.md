# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/SchedulingModePicker.md

# [SchedulingModePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/SchedulingModePicker)

Combo box preconfigured with possible scheduling mode values.

This field can be used as an editor for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the `SchedulingModeColumn`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[allowedModes](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/SchedulingModePicker#config-allowedModes)
Specifies a list of allowed scheduling modes to be shown in the picker. Supports either a string of comma separated values:

````
new SchedulingModePicker ({
    allowedModes : 'FixedDuration,Normal'
    ...
})

or an array of values:

```javascript
new SchedulingModePicker ({
    allowedModes : ['FixedDuration', 'Normal']
    ...
})
````

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulingModePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/SchedulingModePicker#property-isSchedulingModePicker)
Identifies an object as an instance of [SchedulingModePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingModePicker) class, or subclass thereof.

[isSchedulingModePicker](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/SchedulingModePicker#property-isSchedulingModePicker-static)
Identifies an object as an instance of [SchedulingModePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingModePicker) class, or subclass thereof.
