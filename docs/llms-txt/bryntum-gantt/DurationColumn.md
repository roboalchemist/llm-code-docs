# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/column/DurationColumn.md

# [DurationColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn)

A column showing the task [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-fullDuration). Please note, this column is preconfigured and expects its field to be of the [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) type.

The default editor is a [DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField). It parses time units, so you can enter "4d" indicating 4 days duration, or "4h" indicating 4 hours, etc. The numeric magnitude can be either an integer or a float value. Both "," and "." are valid decimal separators. For example, you can enter "4.5d" indicating 4.5 days duration, or "4,5h" indicating 4.5 hours.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[decimalPrecision](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#config-decimalPrecision)
Precision of displayed duration, defaults to use [durationDisplayPrecision](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-durationDisplayPrecision). Specify an integer value to override that setting, or `false` to use raw value

[abbreviatedUnit](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#config-abbreviatedUnit)
Set to `true` to display duration in short form (5d, 2mo)

[field](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#config-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-name) of the [data model](https://bryntum.com/docs/gantt/api/#Core/data/Model) field to read a cells value from.

Setting **duration** as the **field** value for the duration column is not allowed since the field needs both a duration magnitude and unit, as supplied by for example the [fullDuration](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-fullDuration) field. Additionally, a custom implemented field for the duration column should return a duration object to work correctly.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDurationColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#property-isDurationColumn)
Identifies an object as an instance of [DurationColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/DurationColumn) class, or subclass thereof.

[isDurationColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#property-isDurationColumn-static)
Identifies an object as an instance of [DurationColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/DurationColumn) class, or subclass thereof.

[decimalPrecision](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#property-decimalPrecision)
Precision of displayed duration, defaults to use [durationDisplayPrecision](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-durationDisplayPrecision). Specify an integer value to override that setting, or `false` to use raw value

[abbreviatedUnit](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#property-abbreviatedUnit)
Set to `true` to display duration in short form (5d, 2mo)

[field](https://bryntum.com/docs/gantt/api/Scheduler/column/DurationColumn#property-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-name) of the [data model](https://bryntum.com/docs/gantt/api/#Core/data/Model) field to read a cells value from.

Setting **duration** as the **field** value for the duration column is not allowed since the field needs both a duration magnitude and unit, as supplied by for example the [fullDuration](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-fullDuration) field. Additionally, a custom implemented field for the duration column should return a duration object to work correctly.
