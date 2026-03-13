# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/StartDateField.md

# [StartDateField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField)

Date field widget (text field + date picker) to be used together with Scheduling Engine. This field adjusts time to the earliest possible time of the day based on either:

* the event calendars (which is a combination of its own calendar and assigned resources ones) - if [eventRecord](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#config-eventRecord) is provided.
* the project [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel#field-calendar) - if [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#config-project) is provided. The project start date is used as a default value for the [min](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#property-min) property. Also, the default value of the [max](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#property-max) property is set to be 200 years after the project's end date (or to the year 2300 if no project is provided).

**Please note, that either [eventRecord](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#config-eventRecord) or [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#config-project) value must be provided.**

This field can be used as an editor for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the `StartDateColumn`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField#config-project)
Project model calendar of which should be used by the field.

[eventRecord](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField#config-eventRecord)
Event model calendars of which should be used by the field.

[minDateDelta](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField#config-minDateDelta)
Number of milliseconds to add to the project's start date (should be negative). Then, during editing, the resulting date is assigned to the [min](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#config-min) property of the field, preventing the user from entering too low values.

This also prevents freezing, when user enters the incomplete date with one-digit year.

The value of this config will be passed to [add](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-add-static), so in addition to number of milliseconds, strings like "-1 year" are recognized.

Default value is '-10 years'

[maxDateDelta](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField#config-maxDateDelta)
Number of milliseconds to add to the project's start date. Then, during editing, the resulting date is assigned to the [max](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#config-max) property of the field, preventing the user from entering too high values.

This also prevents freezing, when user enters the date with five-digits year.

The value of this config will be passed to [add](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-add-static), so in addition to number of milliseconds, strings like "1 year" are recognized.

Default value is '200 years'

[keepTime](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField#config-keepTime)
A flag which indicates what time should be used for selected date. `sod` by default which adjusts user provided value time to start of the working day.

Possible options are:

* `'sod'` adjust user provided value time to start of the working day
* `false` to reset time to midnight
* `true` to keep original time value
* `'17:00'` a string which is parsed automatically
* `new Date(2020, 0, 1, 17)` a date object to copy time from
* `'entered'` to keep time value entered by user (in case [format](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField#config-format) includes time info)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStartDateField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField#property-isStartDateField)
Identifies an object as an instance of [StartDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField) class, or subclass thereof.

[isStartDateField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/StartDateField#property-isStartDateField-static)
Identifies an object as an instance of [StartDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField) class, or subclass thereof.
