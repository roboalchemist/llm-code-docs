# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerScroll.md

# [SchedulerScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll)

Functions for scrolling to events, dates etc.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[scrollExtensionThreshold](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#config-scrollExtensionThreshold)
Specifies the maximum duration for extending the current [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) to allow for smooth scrolling to an event.

This configuration determines how far the scheduler should extend the visible timespan to enable smooth scrolling. If the target event is within this duration from the current view, the scheduler will animate the scroll. If the event lies beyond this threshold, the scheduler will directly jump to it without animation.

Setting a shorter duration can enhance performance in views with many events, as it limits the number of events that need to be rendered when extending the timespan.

The value can be specified as a string or a [DurationConfig](https://bryntum.com/docs/gantt/api/#Core/data/Duration#typedef-DurationConfig) object, allowing for flexible duration definitions, such as '1 week' for one week or `{unit: 'week', magnitude: 1}`.

Default value is the duration of the currently rendered timespan at the time of invocation.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#property-isSchedulerScroll)
Identifies an object as an instance of [SchedulerScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerScroll) class, or subclass thereof.

[isSchedulerScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#property-isSchedulerScroll-static)
Identifies an object as an instance of [SchedulerScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerScroll) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[scrollEventIntoView](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#function-scrollEventIntoView)
Scrolls an event record into the viewport. If the resource store is a tree store, this method will also expand all relevant parent nodes to locate the event.

This function is not applicable for events with multiple assignments, please use #scrollResourceEventIntoView instead.

[scrollAssignmentIntoView](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#function-scrollAssignmentIntoView)
Scrolls an assignment record into the viewport.

If the resource store is a tree store, this method will also expand all relevant parent nodes to locate the event.

[scrollResourceEventIntoView](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#function-scrollResourceEventIntoView)
Scrolls a resource event record into the viewport.

If the resource store is a tree store, this method will also expand all relevant parent nodes to locate the event.

[scrollUnrenderedEventIntoView](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#function-scrollUnrenderedEventIntoView)
Scrolls an unrendered event into view. Internal function used from #scrollResourceEventIntoView.

[scrollResourceIntoView](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerScroll#function-scrollResourceIntoView)
Scrolls the specified resource into view, works for both horizontal and vertical modes.
