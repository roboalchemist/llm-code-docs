# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/ResourceNonWorkingTime.md

# [ResourceNonWorkingTime](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime)

Feature that highlights the non-working intervals for resources based on their [calendar](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/ResourceModel#field-calendar). If a resource has no calendar defined, the project's calendar will be used. The non-working time interval can also be recurring. You can find a live example showing how to achieve this in the [Resource Non-Working Time Demo](https://bryntum.com/docs/gantt/api/../examples/resource-non-working-time/).

Data structure
--------------

Example data defining calendars and assigning the resources a calendar:

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
                      "isWorking"          : true,
                  }
              ]
          }
   ],
   "resources" : {
      "rows" : [
          {
              "id"         : 1,
              "name"       : "George",
              "calendar"   : "day",
              "role"       : "Office",
              "eventColor" : "blue"
          },
          {
              "id"         : 2,
              "name"       : "Rob",
              "calendar"   : "day",
              "role"       : "Office",
              "eventColor" : "blue"
          }
       ]
  [...]
```

```
const scheduler = new SchedulerPro({
  // A Project holding the data and the calculation engine for Scheduler Pro. It also acts as a CrudManager, allowing
  // loading data into all stores at once
  project : {
      autoLoad  : true,
      transport : {
          load : {
              url : './data/data.json'
          }
      }
  },
  features : {
      resourceNonWorkingTime : true
  },
  [...]
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

[maxTimeAxisUnit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#config-maxTimeAxisUnit)
The largest time axis unit to display non working ranges for ('hour' or 'day' etc). When zooming to a view with a larger unit, no non-working time elements will be rendered.

**Note:** Be careful with setting this config to big units like 'year'. When doing this, make sure the timeline [start](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-startDate) and [end](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-endDate) dates are set tightly. When using a long range (for example many years) with non-working time elements rendered per hour, you will end up with millions of elements, impacting performance. When zooming, use the [zoomKeepsOriginalTimespan](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-zoomKeepsOriginalTimespan) config.

[enableMouseEvents](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#config-enableMouseEvents)
Set to `true` to allow mouse interactions with the rendered range elements. By default, the range elements are not reachable with the mouse, and only serve as a static background.

[resourceTimeRangeModelClass](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#config-resourceTimeRangeModelClass)
The Model class to use for representing a [ResourceTimeRangeModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTimeRangeModel)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceNonWorkingTime](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#property-isResourceNonWorkingTime)
Identifies an object as an instance of [ResourceNonWorkingTime](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/ResourceNonWorkingTime) class, or subclass thereof.

[isResourceNonWorkingTime](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#property-isResourceNonWorkingTime-static)
Identifies an object as an instance of [ResourceNonWorkingTime](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/ResourceNonWorkingTime) class, or subclass thereof.

[enableMouseEvents](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#property-enableMouseEvents)
Set to `true` to allow mouse interactions with the rendered range elements. By default, the range elements are not reachable with the mouse, and only serve as a static background.

## Functions

Functions are methods available for calling on the class

[resolveResourceNonWorkingTimeInterval](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#function-resolveResourceNonWorkingTimeInterval)
Returns a resource nonworking time range record from the passed element

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[resourceNonWorkingTimeMouseDown](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#event-resourceNonWorkingTimeMouseDown)
Triggered for mouse down ona resource nonworking time range. Only triggered if the ResourceNonWorkingTime feature is configured with `enableMouseEvents: true`.

[resourceNonWorkingTimeMouseUp](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#event-resourceNonWorkingTimeMouseUp)
Triggered for mouse up ona resource nonworking time range. Only triggered if the ResourceNonWorkingTime feature is configured with `enableMouseEvents: true`.

[resourceNonWorkingTimeClick](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#event-resourceNonWorkingTimeClick)
Triggered for click on a resource nonworking time range. Only triggered if the ResourceNonWorkingTime feature is configured with `enableMouseEvents: true`.

[resourceNonWorkingTimeDblClick](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#event-resourceNonWorkingTimeDblClick)
Triggered for double-click on a resource nonworking time range. Only triggered if the ResourceNonWorkingTime feature is configured with `enableMouseEvents: true`.

[resourceNonWorkingTimeContextMenu](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#event-resourceNonWorkingTimeContextMenu)
Triggered for right-click on a resource nonworking time range. Only triggered if the ResourceNonWorkingTime feature is configured with `enableMouseEvents: true`.

[resourceNonWorkingTimeMouseOver](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#event-resourceNonWorkingTimeMouseOver)
Triggered for mouse over on a resource nonworking time range. Only triggered if the ResourceNonWorkingTime feature is configured with `enableMouseEvents: true`.

[resourceNonWorkingTimeMouseOut](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/ResourceNonWorkingTime#event-resourceNonWorkingTimeMouseOut)
Triggered for mouse out of a resource nonworking time range. Only triggered if the ResourceNonWorkingTime feature is configured with `enableMouseEvents: true`.
