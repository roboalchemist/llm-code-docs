# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/base/TooltipBase.md

# [TooltipBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase)

Base class for `EventTooltip` (Scheduler) and `TaskTooltip` (Gantt) features. Shows a tooltip next to an event bar in the timeline.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[autoUpdate](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#config-autoUpdate)
Specify true to have tooltip updated when mouse moves, if you for example want to display date at mouse position.

[hoverDelay](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#config-hoverDelay)
The amount of time to hover before showing

[hideDelay](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#config-hideDelay)
The time (in milliseconds) for which the Tooltip remains visible when the mouse leaves the target.

May be configured as `false` to persist visible after the mouse exits the target element. Configure it as 0 to always retrigger `hoverDelay` even when moving mouse inside `fromElement`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTooltipBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#property-isTooltipBase)
Identifies an object as an instance of [TooltipBase](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/TooltipBase) class, or subclass thereof.

[isTooltipBase](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#property-isTooltipBase-static)
Identifies an object as an instance of [TooltipBase](https://bryntum.com/docs/gantt/api/#Scheduler/feature/base/TooltipBase) class, or subclass thereof.

[tooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#property-tooltip)
A reference to the tooltip instance, which will have a special `eventRecord` property that you can use to get data from the contextual event record to which this tooltip is related.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#event-beforeShow)
Triggered before a tooltip is shown. Return `false` to prevent the action.

[show](https://bryntum.com/docs/gantt/api/Scheduler/feature/base/TooltipBase#event-show)
Triggered after a tooltip is shown.
