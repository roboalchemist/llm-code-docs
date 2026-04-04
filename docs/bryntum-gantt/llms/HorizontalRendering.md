# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/orientation/HorizontalRendering.md

# [HorizontalRendering](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering)

Handles event rendering in Schedulers horizontal mode. Reacts to project/store changes to keep the UI up to date.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[bufferSize](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#config-bufferSize)
Amount of pixels to extend the current visible range at both ends with when deciding which events to render. Only applies when using labels or for milestones

## Functions

Functions are methods available for calling on the class

[getScheduleRegion](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-getScheduleRegion)
Gets the region, relative to the page, represented by the schedule and optionally only for a single resource. This method will call getDateConstraints to allow for additional resource/event based constraints. By overriding that method you can constrain events differently for different resources.

[getRowRegion](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-getRowRegion)
Gets the Region, relative to the timeline view element, representing the passed row and optionally just for a certain date interval.

[getConnectorStartSide](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-getConnectorStartSide)
Gets displaying item start side

[getConnectorEndSide](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-getConnectorEndSide)
Gets displaying item end side

[refreshResourcesWhenReady](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-refreshResourcesWhenReady)
Clears resources directly and redraws them on next project refresh

[refreshResources](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-refreshResources)
Clears and redraws resources directly. Respects schedulers refresh suspension

[addTemporaryDragElement](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-addTemporaryDragElement)
Used by event drag features to bring into existence event elements that are outside of the rendered block.

[calculateMS](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-calculateMS)
Converts a start/endDate into a MS value used when rendering the event. If scheduler is configured with `fillTicks: true` the value returned will be snapped to tick start/end.

[setupRenderData](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-setupRenderData)
Returns event render data except actual position information.

[fillTimeSpanHorizontalPosition](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-fillTimeSpanHorizontalPosition)
Populates render data with information about width and horizontal position of the wrap.

[calculateHorizontalPosition](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-calculateHorizontalPosition)
Fills render data with `insetInlineStart` and `width` properties

[getTimeSpanRenderData](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-getTimeSpanRenderData)
Gets timespan coordinates etc. Relative to containing row. If the timespan is outside of the zone in which timespans are rendered, that is outside of the TimeAxis, or outside of the vertical zone in which timespans are rendered, then `undefined` is returned.

[refreshEventsForResource](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#function-refreshEventsForResource)
Refresh events for resource record (or Row), clearing its cache and forcing DOM refresh.

## Typedefs

Typedefs are type definitions for the class

[HorizontalRenderData](https://bryntum.com/docs/gantt/api/Scheduler/view/orientation/HorizontalRendering#typedef-HorizontalRenderData)
