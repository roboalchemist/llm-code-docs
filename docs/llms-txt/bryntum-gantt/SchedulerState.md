# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/SchedulerState.md

# [SchedulerState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState)

A Mixin for Scheduler that handles state. It serializes the following scheduler properties, in addition to what is already stored by its superclass [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState):

* startDate
* endDate
* eventLayout
* barMargin
* mode
* tickSize
* zoomLevel
* eventColor
* eventStyle
* fillTicks

See [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) and [State](https://bryntum.com/docs/gantt/api/#Core/mixin/State) for more information on state.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#property-isSchedulerState)
Identifies an object as an instance of [SchedulerState](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerState) class, or subclass thereof.

[isSchedulerState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#property-isSchedulerState-static)
Identifies an object as an instance of [SchedulerState](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerState) class, or subclass thereof.

[state](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#property-state)
Gets or sets scheduler's state. Check out [SchedulerState](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerState) mixin and [GridState](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridState) for more details.

## Functions

Functions are methods available for calling on the class

[getState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#function-getState)
Get scheduler's current state for serialization. State includes rowHeight, headerHeight, readOnly, selectedCell, selectedRecordId, column states and store state etc. It also collects state from all features.

[applyState](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#function-applyState)
Apply previously stored state.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeStateSave](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#event-beforeStateSave)
Fired before state is saved by the StateProvider. Allows editing the state object or preventing the operation.

[beforeStateApply](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#event-beforeStateApply)
Fired before state is applied to the source. Allows editing the state object or preventing the operation.

## Typedefs

Typedefs are type definitions for the class

[SchedulerStateInfo](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/SchedulerState#typedef-SchedulerStateInfo)
An object which encapsulates a [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler)'s saved state.
