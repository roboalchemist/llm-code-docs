# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/HeaderZoom.md

# [HeaderZoom](https://bryntum.com/docs/gantt/api/Scheduler/feature/HeaderZoom)

Enables users to click and drag to zoom to a date range in Scheduler's header time axis. Only supported in horizontal mode.

```
const scheduler = new Scheduler({
  features : {
    headerZoom : true
  }
});
```

This feature uses the [zoomToSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#function-zoomToSpan) method internally. If the selected date range cannot fit within zoom levels greater than the current zoom level, the zoom level will not be increased and will remain unchanged. [noZoomChange](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#event-noZoomChange) event is fired in this case.

Not compatible with the [TimeSelection](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeSelection) feature, or with vertical mode.

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isHeaderZoom](https://bryntum.com/docs/gantt/api/Scheduler/feature/HeaderZoom#property-isHeaderZoom)
Identifies an object as an instance of [HeaderZoom](https://bryntum.com/docs/gantt/api/#Scheduler/feature/HeaderZoom) class, or subclass thereof.

[isHeaderZoom](https://bryntum.com/docs/gantt/api/Scheduler/feature/HeaderZoom#property-isHeaderZoom-static)
Identifies an object as an instance of [HeaderZoom](https://bryntum.com/docs/gantt/api/#Scheduler/feature/HeaderZoom) class, or subclass thereof.
