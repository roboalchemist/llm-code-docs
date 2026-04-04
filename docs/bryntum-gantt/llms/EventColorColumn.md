# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/column/EventColorColumn.md

# [EventColorColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/EventColorColumn)

A column that displays Event's `eventColor` values (built-in color classes or CSS colors) as a colored element similar to the [EventColorField](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorField). When the user clicks the element, a [EventColorPicker](https://bryntum.com/docs/gantt/api/#Scheduler/widget/EventColorPicker) lets the user select from a [range of colors](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#config-eventColor).

```
new Scheduler({
   columns : [
      {
         type : 'eventColor',
         text : 'EventColor'
      }
   ]
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventColorColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/EventColorColumn#property-isEventColorColumn)
Identifies an object as an instance of [EventColorColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/EventColorColumn) class, or subclass thereof.

[isEventColorColumn](https://bryntum.com/docs/gantt/api/Scheduler/column/EventColorColumn#property-isEventColorColumn-static)
Identifies an object as an instance of [EventColorColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/EventColorColumn) class, or subclass thereof.
