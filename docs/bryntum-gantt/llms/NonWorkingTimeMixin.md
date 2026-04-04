# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/mixin/NonWorkingTimeMixin.md

# [NonWorkingTimeMixin](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/NonWorkingTimeMixin)

Mixin with functionality shared between [NonWorkingTime](https://bryntum.com/docs/gantt/api/#Scheduler/feature/NonWorkingTime) and [EventNonWorkingTime](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventNonWorkingTime).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[maxTimeAxisUnit](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/NonWorkingTimeMixin#config-maxTimeAxisUnit)
The maximum time axis unit to display non-working ranges for ('hour' or 'day' etc). When zooming to a view with a larger unit, no non-working time elements will be rendered.

**Note:** Be careful with setting this config to big units like 'year'. When doing this, make sure the timeline [start](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-startDate) and [end](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-endDate) dates are set tightly. When using a long range (for example many years) with non-working time elements rendered per hour, you will end up with millions of elements, impacting performance. When zooming, use the [zoomKeepsOriginalTimespan](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable#config-zoomKeepsOriginalTimespan) config.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isNonWorkingTimeMixin](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/NonWorkingTimeMixin#property-isNonWorkingTimeMixin)
Identifies an object as an instance of [NonWorkingTimeMixin](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/NonWorkingTimeMixin) class, or subclass thereof.

[isNonWorkingTimeMixin](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/NonWorkingTimeMixin#property-isNonWorkingTimeMixin-static)
Identifies an object as an instance of [NonWorkingTimeMixin](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/NonWorkingTimeMixin) class, or subclass thereof.
