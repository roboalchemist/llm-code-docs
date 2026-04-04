# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/TimelineState.md

# [TimelineState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineState)

Mixin for Timeline base that handles state. It serializes the following timeline properties:

* barMargin
* zoomLevel

See [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) and [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) for more information on state.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineState#property-isTimelineState)
Identifies an object as an instance of [TimelineState](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineState) class, or subclass thereof.

[isTimelineState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineState#property-isTimelineState-static)
Identifies an object as an instance of [TimelineState](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineState) class, or subclass thereof.

[state](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineState#property-state)
Gets or sets timeline's state. Check out [TimelineState](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineState) mixin for details.

## Functions

Functions are methods available for calling on the class

[getState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineState#function-getState)
Get timeline's current state for serialization. See [state](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineState#property-state) for a list of the state variables.

[applyState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineState#function-applyState)
Apply previously stored state.

## Typedefs

Typedefs are type definitions for the class

[TimelineStateInfo](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/TimelineState#typedef-TimelineStateInfo)
An object which encapsulates a [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler)'s saved state.
