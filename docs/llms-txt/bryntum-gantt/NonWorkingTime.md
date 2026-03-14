# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/NonWorkingTime.md

# [NonWorkingTime](https://bryntum.com/docs/gantt/api/Scheduler/feature/NonWorkingTime)

Feature that allows styling of weekends (and other non-working time) by adding timeRanges for those days.

By default, the basic Scheduler's calendar is empty. When enabling this feature in the basic Scheduler, it injects Saturday and Sunday weekend intervals if no intervals are encountered. For Scheduler Pro, it visualizes the project calendar and does not automatically inject anything. You have to define a Calendar in the application and assign it to the project, for more information on how to do that, please see Scheduler Pro's Scheduling/Calendars guide.

Please note that to not clutter the view (and have a large negative effect on performance) the feature does not render ranges shorter than the base unit used by the time axis. The behavior can be disabled with [hideRangesOnZooming](https://bryntum.com/docs/gantt/api/#Scheduler/feature/NonWorkingTime#config-hideRangesOnZooming) config.

The feature also bails out of rendering ranges for very zoomed out views completely for the same reasons (see [maxTimeAxisUnit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/NonWorkingTime#config-maxTimeAxisUnit) for details).

Also note that the feature uses virtualized rendering, only the currently visible non-working-time ranges are available in the DOM.

This feature is **disabled** by default for Scheduler, but **enabled** by default for Scheduler Pro. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[hideRangesOnZooming](https://bryntum.com/docs/gantt/api/Scheduler/feature/NonWorkingTime#config-hideRangesOnZooming)
The feature by default does not render ranges smaller than the base unit used by the time axis. Set this config to `false` to disable this behavior.

The [maxTimeAxisUnit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/NonWorkingTime#config-maxTimeAxisUnit) config defines a zoom level at which to bail out of rendering ranges completely.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isNonWorkingTime](https://bryntum.com/docs/gantt/api/Scheduler/feature/NonWorkingTime#property-isNonWorkingTime)
Identifies an object as an instance of [NonWorkingTime](https://bryntum.com/docs/gantt/api/#Scheduler/feature/NonWorkingTime) class, or subclass thereof.

[isNonWorkingTime](https://bryntum.com/docs/gantt/api/Scheduler/feature/NonWorkingTime#property-isNonWorkingTime-static)
Identifies an object as an instance of [NonWorkingTime](https://bryntum.com/docs/gantt/api/#Scheduler/feature/NonWorkingTime) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[shouldRenderRange](https://bryntum.com/docs/gantt/api/Scheduler/feature/NonWorkingTime#function-shouldRenderRange)
Based on this method result the feature decides whether the provided non-working period should be rendered or not. The method checks that the range has non-zero [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-duration), lays in the visible timespan and its duration is longer or equal the base timeaxis unit (if [hideRangesOnZooming](https://bryntum.com/docs/gantt/api/#Scheduler/feature/NonWorkingTime#config-hideRangesOnZooming) is `true`).

Override the method to implement your custom range rendering vetoing logic.
