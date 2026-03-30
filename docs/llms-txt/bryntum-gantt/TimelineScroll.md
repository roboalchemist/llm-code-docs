# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineScroll.md

# [TimelineScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll)

Functions for scrolling to events, dates etc.

Note: the mixin applies [TimelineZoomable](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable) mixin if it's not applied yet.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[bufferCoef](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#config-bufferCoef)
This config defines the size of the start and end invisible parts of the timespan when [infiniteScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll#config-infiniteScroll) set to `true`.

It should be provided as a coefficient, which will be multiplied by the size of the scheduling area.

For example, if `bufferCoef` is `5` and the panel view width is 200px then the timespan will be calculated to have approximately 1000px (`5 * 200`) to the left and 1000px to the right of the visible area, resulting in 2200px of totally rendered content.

[bufferThreshold](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#config-bufferThreshold)
This config defines the scroll limit, which, when exceeded will cause a timespan shift. The limit is calculated as the `panelWidth * [bufferCoef](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll#config-bufferCoef) * bufferThreshold`. During scrolling, if the left or right side has less than that of the rendered content - a shift is triggered.

For example if `bufferCoef` is `5` and the panel view width is 200px and `bufferThreshold` is 0.2, then the timespan will be shifted when the left or right side has less than 200px (5 \* 200 \* 0.2) of content.

[infiniteScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#config-infiniteScroll)
Set to `true` to automatically adjust the panel timespan during scrolling in the time dimension, when the scroller comes close to the start/end edges.

The actually rendered timespan in this mode (and thus the amount of HTML in the DOM) is calculated based on the [bufferCoef](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll#config-bufferCoef) option, and is thus not controlled by the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-startDate) and [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-endDate) configs. The moment when the timespan shift happens is determined by the [bufferThreshold](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll#config-bufferThreshold) value.

To specify initial point in time to view, supply the [visibleDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-visibleDate) config.

If you activate [lazy loading](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#lazy-loading-data-infinite-scroll) you get an infinitely scrollable timeline with lazy loading of content.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#property-isTimelineScroll)
Identifies an object as an instance of [TimelineScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll) class, or subclass thereof.

[isTimelineScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#property-isTimelineScroll-static)
Identifies an object as an instance of [TimelineScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll) class, or subclass thereof.

[infiniteScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#property-infiniteScroll)
Set to `true` to automatically adjust the panel timespan during scrolling in the time dimension, when the scroller comes close to the start/end edges.

The actually rendered timespan in this mode (and thus the amount of HTML in the DOM) is calculated based on the [bufferCoef](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll#config-bufferCoef) option, and is thus not controlled by the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-startDate) and [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-endDate) configs. The moment when the timespan shift happens is determined by the [bufferThreshold](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll#config-bufferThreshold) value.

To specify initial point in time to view, supply the [visibleDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-visibleDate) config.

If you activate [lazy loading](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#lazy-loading-data-infinite-scroll) you get an infinitely scrollable timeline with lazy loading of content.

[timelineScroller](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#property-timelineScroller)
A [Scroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/Scroller) which scrolls the time axis in whatever [mode](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-mode) the Scheduler is configured, either `horizontal` or `vertical`.

The width and height dimensions are replaced by `size`. So this will expose the following properties:

* `clientSize` The size of the time axis viewport.
* `scrollSize` The full scroll size of the time axis viewport
* `position` The position scrolled to along the time axis viewport

[scrollLeft](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#property-scrollLeft)
Get/set the `scrollLeft` value of the SubGrid that holds the scheduler.

This may be **negative** when the writing direction is right-to-left.

[scrollX](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#property-scrollX)
Get/set the writing direction agnostic horizontal scroll position.

This is always the **positive** offset from the scroll origin whatever the writing direction in use.

Applies to the SubGrid that holds the scheduler

[scrollTop](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#property-scrollTop)
Get/set vertical scroll

## Functions

Functions are methods available for calling on the class

[calculateInfiniteScrollingDateRange](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#function-calculateInfiniteScrollingDateRange)
Used to calculate the range to extend the TimeAxis to during infinite scroll.

[scrollToDate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#function-scrollToDate)
Scrolls the timeline "tick" encapsulating the passed `Date` into view according to the passed options.

[scrollToNow](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#function-scrollToNow)
Scrolls to current time.

[scrollToCoordinate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#function-scrollToCoordinate)
Used by [scrollToDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineScroll#function-scrollToDate) to scroll to correct coordinate.

[scrollHorizontallyTo](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#function-scrollHorizontallyTo)
Horizontal scrolling. Applies to the SubGrid that holds the scheduler

[scrollVerticallyTo](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#function-scrollVerticallyTo)
Vertical scrolling

[scrollTo](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineScroll#function-scrollTo)
Scrolls the subgrid that contains the scheduler
