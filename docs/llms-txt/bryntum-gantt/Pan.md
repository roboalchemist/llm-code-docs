# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/Pan.md

# [Pan](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan)

Makes the scheduler's timeline pannable by dragging with the mouse. Try it out in the demo below.

```
// Enable Pan
const scheduler = new Scheduler({
  features : {
    pan : true,
    eventDragCreate : false
  }
});
```

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

Incompatible with the [EventDragCreate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragCreate) and the [EventDragSelect](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventDragSelect) features.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[horizontal](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#config-horizontal)
Set to `false` to not pan horizontally

[vertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#config-vertical)
Set to `false` to not pan vertically

[enableInHeader](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#config-enableInHeader)
Set to `false` to not pan horizontally when dragging in the time axis header

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPan](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#property-isPan)
Identifies an object as an instance of [Pan](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Pan) class, or subclass thereof.

[isPan](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#property-isPan-static)
Identifies an object as an instance of [Pan](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Pan) class, or subclass thereof.

[horizontal](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#property-horizontal)
Set to `false` to not pan horizontally

[vertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#property-vertical)
Set to `false` to not pan vertically

[enableInHeader](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#property-enableInHeader)
Set to `false` to not pan horizontally when dragging in the time axis header

[isActive](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#property-isActive)
Yields `true` if a pan gesture is in process.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforePan](https://bryntum.com/docs/gantt/api/Scheduler/feature/Pan#event-beforePan)
Fires on the owning Scheduler or Gantt widget before pan starts. Return `false` to prevent the operation.
