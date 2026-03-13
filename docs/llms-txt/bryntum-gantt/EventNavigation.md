# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/EventNavigation.md

# [EventNavigation](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation)

Mixin that tracks event or assignment selection by clicking on one or more events in the scheduler.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[navigator](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation#config-navigator)
A config object to use when creating the [Navigator](https://bryntum.com/docs/gantt/api/#Core/helper/util/Navigator) to use to perform keyboard navigation in the timeline.

[focusCls](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation#config-focusCls)
A CSS class name to add to focused events.

[enableDeleteKey](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation#config-enableDeleteKey)
Allow using \[Delete\] and \[Backspace\] to remove events/assignments

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventNavigation](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation#property-isEventNavigation)
Identifies an object as an instance of [EventNavigation](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/EventNavigation) class, or subclass thereof.

[isEventNavigation](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation#property-isEventNavigation-static)
Identifies an object as an instance of [EventNavigation](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/EventNavigation) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[isInTimeAxis](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation#function-isInTimeAxis)
Determines if an event is within the time axis.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[navigate](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/EventNavigation#event-navigate)
Fired when a user gesture causes the active item to change.
