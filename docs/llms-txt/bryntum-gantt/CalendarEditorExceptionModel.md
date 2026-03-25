# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel.md

# [CalendarEditorExceptionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel)

This class represents a calendar exception - a special interval providing working time changes. The class is used by the calendar editor.

## Fields

Fields belong to a Model class and define the Model data structure

[availability](https://bryntum.com/docs/gantt/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-availability)
The field specifies availability provided by this exception. When some availability is provided the system uses the provided time ranges inside of the exception [startDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-startDate) - [endDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-endDate) period of time.

Implemented as a field of [StoreDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/StoreDataField) type

[isWorking](https://bryntum.com/docs/gantt/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-isWorking)
Specifies whether the exception is a working period of time or not. If the value is `true`:

* if [availability](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-availability) is not provided the whole [startDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-startDate) - [endDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-endDate) period of time is treated as working.
* if [availability](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-availability) is provided then the Engine uses the availability time ranges inside of the [startDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-startDate) - [endDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-endDate) period of time.

[recurrentStartDate](https://bryntum.com/docs/gantt/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-recurrentStartDate)
Recurring start date of the exception.

[recurrentEndDate](https://bryntum.com/docs/gantt/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#field-recurrentEndDate)
Recurring end date of the exception.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCalendarEditorExceptionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#property-isCalendarEditorExceptionModel)
Identifies an object as an instance of [CalendarEditorExceptionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel) class, or subclass thereof.

[isCalendarEditorExceptionModel](https://bryntum.com/docs/gantt/api/SchedulerPro/model/calendareditor/CalendarEditorExceptionModel#property-isCalendarEditorExceptionModel-static)
Identifies an object as an instance of [CalendarEditorExceptionModel](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/calendareditor/CalendarEditorExceptionModel) class, or subclass thereof.
