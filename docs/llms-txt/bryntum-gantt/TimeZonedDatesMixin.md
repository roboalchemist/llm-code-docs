# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/model/mixin/TimeZonedDatesMixin.md

# [TimeZonedDatesMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/TimeZonedDatesMixin)

This mixin class overrides default Model functionality to provide support for time zone converted dates

## Fields

Fields belong to a Model class and define the Model data structure

[timeZone](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/TimeZonedDatesMixin#field-timeZone)
The current timeZone this record is converted to. Used internally to keep track of time zone conversions.

Can also be used to create a new record with dates in a specific non-local timezone. That is useful for example when replacing a store dataset. That would be interpreted as a new load, and all dates would be converted to the configured timezone.

If specifically set to `null` when adding a new record to a Store, the new record's dates will be converted to the Project's configured timezone.

If set to `false` on a record, that record will be excluded from timezone conversion.

For more information about timezone conversion, se [timeZone](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#config-timeZone).

This field will not [persist](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-persist) by default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeZonedDatesMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/TimeZonedDatesMixin#property-isTimeZonedDatesMixin)
Identifies an object as an instance of [TimeZonedDatesMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/TimeZonedDatesMixin) class, or subclass thereof.

[isTimeZonedDatesMixin](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/TimeZonedDatesMixin#property-isTimeZonedDatesMixin-static)
Identifies an object as an instance of [TimeZonedDatesMixin](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/TimeZonedDatesMixin) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[isTimeZoneDateField](https://bryntum.com/docs/gantt/api/Scheduler/model/mixin/TimeZonedDatesMixin#function-isTimeZoneDateField-static)
Returns `true` if the field is adjusted by `timeZone` config.
