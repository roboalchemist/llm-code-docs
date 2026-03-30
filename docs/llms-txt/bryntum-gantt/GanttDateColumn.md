# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/column/GanttDateColumn.md

# [GanttDateColumn](https://bryntum.com/docs/gantt/api/Gantt/column/GanttDateColumn)

Base column class that displays dates, in the `ll` format by default. If set to `null` uses Gantt's [date format](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-displayDateFormat) as a default. The format will be dynamically updated while zooming according to the [displayDateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-displayDateFormat) value specified for the ViewPreset being selected.

By default, this class hides the left/right arrows to modify the date incrementally, you can enable this with the [step](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn#config-step) config of the [editor](https://bryntum.com/docs/gantt/api/#Gantt/column/GanttDateColumn#config-editor) config.

Default editor is a [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[format](https://bryntum.com/docs/gantt/api/Gantt/column/GanttDateColumn#config-format)
The date format used to display dates in this column. If `format` is set to `null`, the current value of the Gantt's [displayDateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-displayDateFormat) will be used to format the date value.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGanttDateColumn](https://bryntum.com/docs/gantt/api/Gantt/column/GanttDateColumn#property-isGanttDateColumn)
Identifies an object as an instance of [GanttDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/GanttDateColumn) class, or subclass thereof.

[isGanttDateColumn](https://bryntum.com/docs/gantt/api/Gantt/column/GanttDateColumn#property-isGanttDateColumn-static)
Identifies an object as an instance of [GanttDateColumn](https://bryntum.com/docs/gantt/api/#Gantt/column/GanttDateColumn) class, or subclass thereof.

[format](https://bryntum.com/docs/gantt/api/Gantt/column/GanttDateColumn#property-format)
The date format used to display dates in this column. If `format` is set to `null`, the current value of the Gantt's [displayDateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-displayDateFormat) will be used to format the date value.
