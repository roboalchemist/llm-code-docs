# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/widget/taskeditor/GeneralTab.md

# [GeneralTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/GeneralTab)

A tab inside the [scheduler task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/SchedulerTaskEditor) or [gantt task editor](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/GanttTaskEditor) showing the general information for a task.

Field ref

Type

Text

Weight

Description

`name`

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

Name

100

Task name

`percentDone`

[NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField)

% Complete

200

Shows what part of task is done already in percentage

`effort`

[EffortField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EffortField)

Effort

300

Shows how much working time is required to complete the whole task

`divider`

[Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget)

400

Visual splitter between 2 groups of fields

`startDate`

[StartDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/StartDateField)

Start

500

Shows when the task begins

`endDate`

[EndDateField](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/EndDateField)

Finish

600

Shows when the task ends

`duration`

[DurationField](https://bryntum.com/docs/gantt/api/#Core/widget/DurationField)

Duration

700

Shows how long the task is

`colorField` ¹

[EventColorField](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField)

Color ¹

800

Choose background color for the task bar

**¹** Set the [showTaskColorPickers](https://bryntum.com/docs/gantt/api/#SchedulerPro/view/SchedulerProBase#config-showTaskColorPickers) config to `true` to enable this field

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGeneralTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/GeneralTab#property-isGeneralTab)
Identifies an object as an instance of [GeneralTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/GeneralTab) class, or subclass thereof.

[isGeneralTab](https://bryntum.com/docs/gantt/api/SchedulerPro/widget/taskeditor/GeneralTab#property-isGeneralTab-static)
Identifies an object as an instance of [GeneralTab](https://bryntum.com/docs/gantt/api/#SchedulerPro/widget/taskeditor/GeneralTab) class, or subclass thereof.
