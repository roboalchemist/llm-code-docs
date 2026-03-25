# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/TimeSpanHighlight.md

# [TimeSpanHighlight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TimeSpanHighlight)

This feature exposes methods on the owning Scheduler or Gantt widget which you can use to highlight one or multiple time spans in the schedule. Please see [highlightTimeSpan](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TimeSpanHighlight#function-highlightTimeSpan) and [highlightTimeSpans](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TimeSpanHighlight#function-highlightTimeSpans) to learn more or try the demo below:

Example usage with Scheduler Pro
--------------------------------

```
const scheduler = new SchedulerPro({
    features : {
        timeSpanHighlight : true
    }
})

scheduler.highlightTimeSpan({
     startDate : new Date(2022, 4, 1),
     endDate   : new Date(2022, 4, 5),
     name      : 'Time off'
});
```

Example usage with Gantt
------------------------

```
const gantt = new Gantt({
    features : {
        timeSpanHighlight : true
    }
})

gantt.highlightTimeSpan({
     startDate : new Date(2022, 4, 1),
     endDate   : new Date(2022, 4, 5),
     padding   : 10, // Some "air" around the rectangle
     taskRecord, // You can also highlight an area specific to a Gantt task
     name      : 'Time off'
});
```

This feature is **disabled** by default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeSpanHighlight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TimeSpanHighlight#property-isTimeSpanHighlight)
Identifies an object as an instance of [TimeSpanHighlight](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TimeSpanHighlight) class, or subclass thereof.

[isTimeSpanHighlight](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TimeSpanHighlight#property-isTimeSpanHighlight-static)
Identifies an object as an instance of [TimeSpanHighlight](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/TimeSpanHighlight) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[highlightTimeSpan](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TimeSpanHighlight#function-highlightTimeSpan)
Highlights the region representing the passed time span and optionally for a single certain resource.

[highlightTimeSpans](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TimeSpanHighlight#function-highlightTimeSpans)
Highlights the regions representing the passed time spans.

[unhighlightTimeSpans](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TimeSpanHighlight#function-unhighlightTimeSpans)
Removes any highlighting elements.

## Typedefs

Typedefs are type definitions for the class

[HighlightTimeSpan](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/TimeSpanHighlight#typedef-HighlightTimeSpan)
An object describing the time span region to highlight.
