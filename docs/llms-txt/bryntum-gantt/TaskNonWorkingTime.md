# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/TaskNonWorkingTime.md

# [TaskNonWorkingTime](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime)

Feature highlighting the non-working time intervals for tasks, based on their [calendar](https://bryntum.com/docs/gantt/api/#Gantt/model/TaskModel#field-calendar). If a task has no calendar defined, the project's calendar will be used. The non-working time interval can also be recurring. You can find a live example showing how to achieve this in the [Task Calendars Demo](https://bryntum.com/docs/gantt/api/../examples/calendars/).

The demo above shows the default `row` mode, but the feature also supports a `bar` [mode](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskNonWorkingTime#config-mode) that shades parts of the task bars:

If you want a tooltip to be displayed when hovering over the non-working time interval, you can configure a [tooltipTemplate](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskNonWorkingTime#config-tooltipTemplate).

Data structure
--------------

Below you see an example of data defining calendars and assigning the tasks a calendar:

```
const gantt = new Gantt({
    features : {
        taskNonWorkingTime : true
    },

    // A Project holding the data and the calculation engine for the Gantt. It also acts as a CrudManager, allowing
    project   : {
        tasks : [
            { id : 1, name : 'Task 1' },
            { id : 2, name : 'Task 2', calendar : 'break' }
        ],
        calendars : [
            {
                id        : 'general',
                name      : 'General',
                intervals : [
                    {
                        recurrentStartDate : 'on Sat',
                        recurrentEndDate   : 'on Mon',
                        isWorking          : false
                    }
                ]
            },
            {
                id        : 'break',
                name      : 'Breaks',
                intervals : [
                    {
                        startDate : '2022-08-07',
                        endDate   : '2022-08-11',
                        isWorking : false
                    },
                    {
                        startDate : '2022-08-18',
                        endDate   : '2022-08-20',
                        isWorking : false
                    }
                ]
            }
        ]
    }
}):
```

Styling non-working time interval elements
------------------------------------------

To style the elements representing the non-working time elements you can set the [cls](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/CalendarModel#field-cls) field in your data. This will add a CSS class to all non-working time elements for the calendar. You can also add an [iconCls](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/CalendarModel#field-iconCls) value specifying an icon to display inside the interval.

```
{
  "success"   : true,
  "calendars" : {
      "rows" : [
          {
              "id"                       : "day",
              "name"                     : "Day shift",
              "unspecifiedTimeIsWorking" : false,
              "cls"                      : "dayshift",
              "intervals"                : [
                  {
                      "recurrentStartDate" : "at 8:00",
                      "recurrentEndDate"   : "at 17:00",
                      "isWorking"          : true
                  }
              ]
          }
      ]
   }
}
```

You can also add a `cls` value and an `iconCls` to **individual** intervals:

```
{
  "success"   : true,
  "calendars" : {
      "rows" : [
          {
              "id"                       : "day",
              "name"                     : "Day shift",
              "unspecifiedTimeIsWorking" : true,
              "intervals"                : [
                  {
                     "startDate"          : "2022-03-23T02:00",
                     "endDate"            : "2022-03-23T04:00",
                     "isWorking"          : false,
                     "cls"                : "factoryShutdown",
                     "iconCls"            : "warningIcon"
                 }
              ]
          }
      ]
   }
}
```

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[maxTimeAxisUnit](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#config-maxTimeAxisUnit)
The largest time axis unit to display non working ranges for ('hour' or 'day' etc). When zooming to a view with a larger unit, no non-working time elements will be rendered.

**Note:** Be careful with setting this config to big units like 'year'. When doing this, make sure the timeline [start](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-startDate) and [end](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-endDate) dates are set tightly. When using a long range (for example many years) with non-working time elements rendered per hour, you will end up with millions of elements, impacting performance. When zooming, use the [zoomKeepsOriginalTimespan](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-zoomKeepsOriginalTimespan) config.

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#config-tooltipTemplate)
A template function used to generate contents for a tooltip when hovering non-working time intervals

```
const gantt = new Gantt({
    features : {
        taskNonWorkingTime : {
            tooltipTemplate({ taskRecord, startDate, endDate }) {
                return 'Non-working time';
            }
        }
    ]
});
```

[mode](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#config-mode)
Rendering mode, one of:

* 'row' - renders non-working time intervals to the task row
* 'bar' - renders non-working time intervals inside the task bar
* 'both - combines 'row' and 'bar' rendering modes

[respectFillTicks](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#config-respectFillTicks)
Config that allows rendering to take into account the Gantt [fillTicks](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-fillTicks) config:

* `true` - renders non-working time intervals taking into account the Gantt [fillTicks](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-fillTicks) config
* `false` - (default) renders non-working time intervals without taking into account the Gantt [fillTicks](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-fillTicks) config

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTaskNonWorkingTime](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#property-isTaskNonWorkingTime)
Identifies an object as an instance of [TaskNonWorkingTime](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskNonWorkingTime) class, or subclass thereof.

[isTaskNonWorkingTime](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#property-isTaskNonWorkingTime-static)
Identifies an object as an instance of [TaskNonWorkingTime](https://bryntum.com/docs/gantt/api/#Gantt/feature/TaskNonWorkingTime) class, or subclass thereof.

[mode](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#property-mode)
Rendering mode, one of:

* 'row' - renders non-working time intervals to the task row
* 'bar' - renders non-working time intervals inside the task bar
* 'both - combines 'row' and 'bar' rendering modes

[respectFillTicks](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#property-respectFillTicks)
Config that allows rendering to take into account the Gantt [fillTicks](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-fillTicks) config:

* `true` - renders non-working time intervals taking into account the Gantt [fillTicks](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-fillTicks) config
* `false` - (default) renders non-working time intervals without taking into account the Gantt [fillTicks](https://bryntum.com/docs/gantt/api/#Gantt/view/Gantt#config-fillTicks) config

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[taskNonWorkingTimeClick](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#event-taskNonWorkingTimeClick)
Triggered when clicking a nonworking time element

[taskNonWorkingTimeDblClick](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#event-taskNonWorkingTimeDblClick)
Triggered when double-clicking a nonworking time element

[taskNonWorkingTimeContextMenu](https://bryntum.com/docs/gantt/api/Gantt/feature/TaskNonWorkingTime#event-taskNonWorkingTimeContextMenu)
Triggered when right-clicking a nonworking time element
