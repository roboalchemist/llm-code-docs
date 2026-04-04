# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/DateTimeField.md

# [DateTimeField](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField)

A field combining a [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) and a [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField).

Input configuration properties (such as `inputWidth`, `inputAlign`, `autoComplete`, `inputAttributes`, `inputType`, `spellCheck`, `tabIndex`, and `validateOnInput`) cannot be set directly on `DateTimeField`. Instead, configure them individually on the underlying [dateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateTimeField#config-dateField) and [timeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateTimeField#config-timeField) configuration objects.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[timeField](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#config-timeField)
Configuration for the [TimeField](https://bryntum.com/docs/gantt/api/#Core/widget/TimeField)

[dateField](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#config-dateField)
Configuration for the [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

[weekStartDay](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#config-weekStartDay)
The week start day in the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-picker), 0 meaning Sunday, 6 meaning Saturday. Uses localized value per default.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#config-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDateTimeField](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#property-isDateTimeField)
Identifies an object as an instance of [DateTimeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateTimeField) class, or subclass thereof.

[isDateTimeField](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#property-isDateTimeField-static)
Identifies an object as an instance of [DateTimeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateTimeField) class, or subclass thereof.

[timeField](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#property-timeField)
Returns the TimeField instance

[dateField](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#property-dateField)
Returns the DateField instance

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/DateTimeField#property-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.
