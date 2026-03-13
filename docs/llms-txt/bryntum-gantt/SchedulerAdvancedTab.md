# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/taskeditor/SchedulerAdvancedTab.md

# [SchedulerAdvancedTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/SchedulerAdvancedTab)

Advanced task options for [scheduler task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) or [gantt task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/GanttTaskEditor) tab.

Contains the following fields by default (with their default weight):

Field ref

Type

Weight

Description

`constraintTypeField`

[ConstraintTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ConstraintTypePicker)

100

Shows a list of available constraints for this task

`constraintDateField`

[DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

200

Shows a date for the selected constraint type

`calendarField`

[CalendarField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CalendarField)

300

List of available calendars, if calendars are used

`manuallyScheduledField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

400

When checked, task is not considered in scheduling

`schedulingModeField`

[SchedulingModePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingModePicker)

450

Shows a list of available scheduling modes for this event

`effortDrivenField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

460

If checked, the effort of the event is kept intact when duration is provided. Works when scheduling mode is "Fixed Duration".

`inactiveField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

500

Allows inactivating the task so it won't take part in the scheduling process.

\`ignoreResourceCalendarField

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

600

If checked the event ignores the assigned resource calendars when scheduling

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerAdvancedTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/SchedulerAdvancedTab#property-isSchedulerAdvancedTab)
Identifies an object as an instance of [SchedulerAdvancedTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SchedulerAdvancedTab) class, or subclass thereof.

[isSchedulerAdvancedTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/SchedulerAdvancedTab#property-isSchedulerAdvancedTab-static)
Identifies an object as an instance of [SchedulerAdvancedTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/SchedulerAdvancedTab) class, or subclass thereof.
