# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventFilter.md

# [EventFilter](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventFilter)

Adds event filter menu items to the timeline header context menu.

```
const scheduler = new Scheduler({
  features : {
    eventFilter : true // `true` by default, set to `false` to disable the feature and remove the menu item from the timeline header
  }
});
```

This feature is **enabled** by default

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventFilter](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventFilter#property-isEventFilter)
Identifies an object as an instance of [EventFilter](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventFilter) class, or subclass thereof.

[isEventFilter](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventFilter#property-isEventFilter-static)
Identifies an object as an instance of [EventFilter](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventFilter) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[populateTimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventFilter#function-populateTimeAxisHeaderMenu)
Populates the header context menu items.
