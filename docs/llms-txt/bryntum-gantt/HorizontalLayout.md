# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/eventlayout/HorizontalLayout.md

# [HorizontalLayout](https://bryntum.com/docs/gantt/api/Scheduler/eventlayout/HorizontalLayout)

Base class for horizontal layouts (HorizontalLayoutPack and HorizontalLayoutStack). Should not be used directly, instead specify [eventLayout](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerEventRendering#config-eventLayout) in Scheduler config (stack, pack or none):

```
let scheduler = new Scheduler({
  eventLayout: 'stack'
});
```

## Functions

Functions are methods available for calling on the class

[applyLayout](https://bryntum.com/docs/gantt/api/Scheduler/eventlayout/HorizontalLayout#function-applyLayout)
This method performs layout on an array of event render data and returns amount of _bands_. Band is a multiplier of a configured [rowHeight](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-rowHeight) to calculate total row height required to fit all events. This method should not be used directly, it is called by the Scheduler during the row rendering process.

[layoutEventsInBands](https://bryntum.com/docs/gantt/api/Scheduler/eventlayout/HorizontalLayout#function-layoutEventsInBands)
This method iterates over events and calculates top position for each of them. Default layouts calculate positions to avoid events overlapping horizontally (except for the 'none' layout). Pack layout will squeeze events to a single row by reducing their height, Stack layout will increase the row height and keep event height intact. This method should not be used directly, it is called by the Scheduler during the row rendering process.
