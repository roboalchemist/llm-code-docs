# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/EndDateField.md

# [EndDateField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/EndDateField)

Date field widget (text field + date picker) to be used together with Scheduling Engine. This field adjusts time to the latest possible time of the day based on either:

* the event calendars (which is a combination of its own calendar and assigned resources ones) - if [eventRecord](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField#config-eventRecord) is provided.
* the project [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ProjectModel#field-calendar) - if [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField#config-project) is provided. The default value of the [max](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField#property-max) property is set to be 200 years after the project's end date (or to the year 2300 if no project is provided).

**Please note, that either [eventRecord](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField#config-eventRecord) or [project](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField#config-project) value must be provided.**

This field can be used as an editor for a [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the `EndDateColumn`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[project](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/EndDateField#config-project)
Project model calendar of which should be used by the field.

[eventRecord](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/EndDateField#config-eventRecord)
The Event model defining the calendar to be used by the field.

[keepTime](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/EndDateField#config-keepTime)
A flag which indicates what time should be used for selected date. `eod` by default which adjusts user provided value time to end of the working day.

Possible options are:

* `'eod'` adjust user provided value time to end of the working day
* `false` to reset time to midnight
* `true` to keep original time value
* `'17:00'` a string which is parsed automatically
* `new Date(2020, 0, 1, 17)` a date object to copy time from
* `'entered'` to keep time value entered by user (in case [format](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField#config-format) includes time info)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEndDateField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/EndDateField#property-isEndDateField)
Identifies an object as an instance of [EndDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField) class, or subclass thereof.

[isEndDateField](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/EndDateField#property-isEndDateField-static)
Identifies an object as an instance of [EndDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField) class, or subclass thereof.
