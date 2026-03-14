# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/taskeditor/AdvancedTab.md

# [AdvancedTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/AdvancedTab)

Advanced task options [scheduler task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) or [gantt task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/GanttTaskEditor) tab.

Field ref

Type

Weight

Description

`calendarField`

[CalendarField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/CalendarField)

100

Shows a list of available calendars for this task

`manuallyScheduledField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

200

If checked, the task is not considered in scheduling

`schedulingModeField`

[SchedulingModePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingModePicker)

300

Shows a list of available scheduling modes for this task

`effortDrivenField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

400

If checked, effort is preserved, and duration is updated. Applies to scheduling mode "Fixed Units"

`divider`

[Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget)

500

Visual splitter between 2 groups of fields

`constraintTypeField`

[ConstraintTypePicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/ConstraintTypePicker)

600

Shows a list of available constraints for this task

`constraintDateField`

[DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField)

700

Shows a date for the selected constraint type

`rollupField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

800

If checked, shows a bar below the parent task. Works when the "Rollup" feature is enabled.

`schedulingDirectionField`

[SchedulingDirectionPicker](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulingDirectionPicker)

850

Only shown when using `includeAsapAlapAsConstraints`

`inactiveField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

900

Allows to inactivate the task so it won't take part in the scheduling process

`ignoreResourceCalendarField`

[Checkbox](https://bryntum.com/docs/gantt/api/#Core/widget/Checkbox)

1000

If checked the task ignores the assigned resource calendars when scheduling

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAdvancedTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/AdvancedTab#property-isAdvancedTab)
Identifies an object as an instance of [AdvancedTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/AdvancedTab) class, or subclass thereof.

[isAdvancedTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/AdvancedTab#property-isAdvancedTab-static)
Identifies an object as an instance of [AdvancedTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/AdvancedTab) class, or subclass thereof.
