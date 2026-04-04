# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/data/calendareditor/CalendarEditorStore.md

# [CalendarEditorStore](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore)

A store providing data for the calendar editor widget. It accepts a [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore#config-calendar) as its input and builds records based on the calendar intervals in the form convenient for the calendar editor.

This store is heterogeneous and can accept models of two classes - [CalendarEditorExceptionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel) and [CalendarEditorWeekModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorWeekModel).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoPush](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#config-autoPush)
Set to `true` to automatically apply changes of the store back to the [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore#config-calendar).

[autoPull](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#config-autoPull)
Set to `true` to automatically rebuild the store records when [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore#config-calendar) changes.

[weekModelClass](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#config-weekModelClass)
Class representing _week_ intervals.

[exceptionModelClass](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#config-exceptionModelClass)
Class representing _exception_ intervals.

[calendar](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#config-calendar)
Calendar the store processes to build own records.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCalendarEditorStore](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#property-isCalendarEditorStore)
Identifies an object as an instance of [CalendarEditorStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore) class, or subclass thereof.

[isCalendarEditorStore](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#property-isCalendarEditorStore-static)
Identifies an object as an instance of [CalendarEditorStore](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore) class, or subclass thereof.

[calendar](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#property-calendar)
Calendar the store processes to build own records.

## Functions

Functions are methods available for calling on the class

[pullFromCalendar](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#function-pullFromCalendar)
Pulls intervals from the provided calendar (or from the configured [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore#config-calendar) if not provided) and builds the store records based on the intervals.

[pushToCalendar](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#function-pushToCalendar)
Pushes the store data to the provided calendar (or to the configured [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore#config-calendar) if not provided). Processes the store records, builds intervals and loads them back into the [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/data/calendareditor/CalendarEditorStore#config-calendar).

[validateRecords](https://bryntum.com/docs/gantt/api/SchedulerPro/data/calendareditor/CalendarEditorStore#function-validateRecords)
Validate the store records and reports errors to the browser console.
