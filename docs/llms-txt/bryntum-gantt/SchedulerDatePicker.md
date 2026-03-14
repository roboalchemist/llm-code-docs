# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/widget/SchedulerDatePicker.md

# [SchedulerDatePicker](https://bryntum.com/docs/gantt/api/Scheduler/widget/SchedulerDatePicker)

A subclass of [DatePicker](https://bryntum.com/docs/gantt/api/#Core/widget/DatePicker) which is able to show the presence of events in its cells if configured with an [eventStore](https://bryntum.com/docs/gantt/api/#Scheduler/widget/SchedulerDatePicker#config-eventStore), and [showEvents](https://bryntum.com/docs/gantt/api/#Scheduler/widget/SchedulerDatePicker#config-showEvents) is set to a truthy value.

The `datepicker` Widget type is implemented by this class when this class is imported, or built into a bundle, and so any [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField) may have its [picker](https://bryntum.com/docs/gantt/api/#Core/widget/PickerField#config-picker) configured to use its capabilities of showing the presence of events in its date cells.

This class implements its own `cellRenderer` to show event presence. If you add a `cellRenderer` to a `SchedulerDatePicker`, [showEvents](https://bryntum.com/docs/gantt/api/#Scheduler/widget/SchedulerDatePicker#config-showEvents) will not work as expected.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showEvents](https://bryntum.com/docs/gantt/api/Scheduler/widget/SchedulerDatePicker#config-showEvents)
How to show presence of events in the configured [eventStore](https://bryntum.com/docs/gantt/api/#Scheduler/widget/SchedulerDatePicker#config-eventStore) in the day cells. Values may be:

* `false` - Do not show events in cells.
* `true` - Show a themeable bullet to indicate the presence of events for a date.
* `'count'` - Show a themeable badge containing the event count for a date.
* `'heatmap'` - show warmer background colors the more events are present for a date

[eventStore](https://bryntum.com/docs/gantt/api/Scheduler/widget/SchedulerDatePicker#config-eventStore)
The [event store](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore) from which the in-cell event presence indicators are drawn.

[eventFilter](https://bryntum.com/docs/gantt/api/Scheduler/widget/SchedulerDatePicker#config-eventFilter)
A function, or the name of a function in the ownership hierarchy to filter which events are collected into the day cell data blocks.

Return `true` to include the passed event, or a _falsy_ value to exclude the event.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerDatePicker](https://bryntum.com/docs/gantt/api/Scheduler/widget/SchedulerDatePicker#property-isSchedulerDatePicker)
Identifies an object as an instance of [SchedulerDatePicker](https://bryntum.com/docs/gantt/api/#Scheduler/widget/SchedulerDatePicker) class, or subclass thereof.

[isSchedulerDatePicker](https://bryntum.com/docs/gantt/api/Scheduler/widget/SchedulerDatePicker#property-isSchedulerDatePicker-static)
Identifies an object as an instance of [SchedulerDatePicker](https://bryntum.com/docs/gantt/api/#Scheduler/widget/SchedulerDatePicker) class, or subclass thereof.
