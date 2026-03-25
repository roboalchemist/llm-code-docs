# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/util/ScheduleTableExporter.md

# [ScheduleTableExporter](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter)

This class transforms scheduler component into two arrays: rows and columns. Columns array contains objects with meta information about column: field name, column name, width and type of the rendered value, rows array contains arrays of cell values.

```
const exporter = new ScheduleTableExporter({ target : scheduler });
exporter.export()

// Output
{
    columns : [
        { field : 'name',      value : 'First name', type : 'string',  width : 100 },
        { field : 'name',      value : 'Task',       type : 'string',  width : 100, eventColumn : true },
        { field : 'startDate', value : 'Starts',     type : 'date',    width : 100, eventColumn : true },
        { field : 'endDate',   value : 'Ends',       type : 'date',    width : 100, eventColumn : true }
    ],
    rows : [
        ['Michael', 'Hand out dundies',      Date, Date],
        ['Michael', 'Buy condo',             Date, Date],
        ['Jim',     'Close sale to library', Date, Date]
    ]
}
```

How data is exported
--------------------

Data is exported as in the base class with minor addition: every event is exported on a separate row, like demonstrated above.

In case there are unassigned events, by default they will be exported as well

```
// output
{
    rows : [
        ['Michael', 'Hand out dundies',      Date, Date],
        ['Michael', 'Buy condo',             Date, Date],
        ['Jim',     'Close sale to library', Date, Date],
        ['',        'No resource assigned'],
        ['',        'Halloween prep',        Date, Date],
        ['',        'New year prep',         Date, Date]
    ]
}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[includeUnassigned](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter#config-includeUnassigned)
Set to `false` to not include unassigned events in the export. `true` by default.

[includeEventsOutsideTimeAxis](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter#config-includeEventsOutsideTimeAxis)
Set to `true` to include events that do not intersect the span of the current time axis.

[eventColumns](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter#config-eventColumns)
An array of Event columns configuration used to specify columns width, headers name, and column fields to get the data from. 'field' config is required. If 'text' is missing, the 'field' config will be used instead.

For example:

```
eventColumns    : [
    { text : 'Task', field : 'name' },
    { text : 'Starts', field : 'startDate', width : 140 },
    { text : 'Ends', field : 'endDate', width : 140 }
]
```

[resourceColumns](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter#config-resourceColumns)
An array of resource column configuration objects used to specify column widths, header text, and data fields to get the data from. 'field' config is required. If 'text' is missing, it will read it from the grid column or the 'field' config. If 'width' is missing, it will try to get it retrieved from the grid column or [defaultColumnWidth](https://bryntum.com/docs/gantt/api/#Scheduler/util/ScheduleTableExporter#config-defaultColumnWidth) config. If no columns provided the config will be generated from the scheduler columns (in horizontal mode).

For example:

```
resourceColumns : [
    'firstName', // field
    { text : 'Role', field : 'role', width : 140 }
]
```

[eventSortFn](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter#config-eventSortFn)
Function to sort events for each resource. By default, events are sorted in the order of appending to the store. For example:

```
// Sorting by start date
eventSortFn : (a, b) => a.startDate - b.startDate
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScheduleTableExporter](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter#property-isScheduleTableExporter)
Identifies an object as an instance of [ScheduleTableExporter](https://bryntum.com/docs/gantt/api/#Scheduler/util/ScheduleTableExporter) class, or subclass thereof.

[isScheduleTableExporter](https://bryntum.com/docs/gantt/api/Scheduler/util/ScheduleTableExporter#property-isScheduleTableExporter-static)
Identifies an object as an instance of [ScheduleTableExporter](https://bryntum.com/docs/gantt/api/#Scheduler/util/ScheduleTableExporter) class, or subclass thereof.
