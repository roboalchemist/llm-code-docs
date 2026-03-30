# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventDragSelect.md

# [EventDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect)

Enables users to click and drag to select events (or assignments in multi assignment mode) inside the Scheduler's timeline. Press CTRL/CMD to extend an existing selection.

The selection rectangle element is styled using the CSS class name `b-drag-select-rect`. You may use application CSS to change its appearance from the default.

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

Incompatible with the [EventDragCreate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragCreate) and the [Pan](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Pan) features.

```
const scheduler = new Scheduler({
  features : {
    eventDragSelect : true,
    eventDragCreate : false
  }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[includeNested](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect#config-includeNested)
Configure as `true` to include nested events in the selection. Only applies to SchedulerPro, when using nested events. When `false` only parent events and events without nesting will be selected.

Marque selection cannot be started inside a parent event, and marque selecting a nested event will always also select the parent event.

```
const scheduler = new SchedulerPro({
    features : {
        nestedEvents : true, // Enable nested events
        eventDragSelect : {
            includeNested : true // Include nested events in the selection
        }
    }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect#property-isEventDragSelect)
Identifies an object as an instance of [EventDragSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragSelect) class, or subclass thereof.

[isEventDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect#property-isEventDragSelect-static)
Identifies an object as an instance of [EventDragSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragSelect) class, or subclass thereof.

[includeNested](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect#property-includeNested)
Configure as `true` to include nested events in the selection. Only applies to SchedulerPro, when using nested events. When `false` only parent events and events without nesting will be selected.

Marque selection cannot be started inside a parent event, and marque selecting a nested event will always also select the parent event.

```
const scheduler = new SchedulerPro({
    features : {
        nestedEvents : true, // Enable nested events
        eventDragSelect : {
            includeNested : true // Include nested events in the selection
        }
    }
});
```

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeEventDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect#event-beforeEventDragSelect)
Fires on the owning Scheduler before drag selection starts. Return false to prevent the operation.

[afterEventDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect#event-afterEventDragSelect)
Fires on the owning Scheduler after the selection is finished.

[eventDragSelect](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventDragSelect#event-eventDragSelect)
Fires on the owning Scheduler when the selection area is updated.
