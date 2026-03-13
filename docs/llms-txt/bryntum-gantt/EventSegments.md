# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/EventSegments.md

# [EventSegments](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments)

This feature provides segmented events support. It implements rendering of such events and also adds a entries to the event context menu allowing to split the selected event and rename segments.

**Note**: this feature is not compatible with Revisions feature.

This feature is **enabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[splitDuration](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#config-splitDuration)
The split duration to be used when "Split event" menu item is called. When set to zero (default) the duration is calculated automatically as the clicked tick duration restricted by [minSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-minSplitDuration) and [maxSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-maxSplitDuration) values.

The duration can be provided as [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) instance (or its configuration object) including both numeric and unit parts.

```
...
features : {
    eventSegments : {
        // split events by 1 day
        splitDuration : {
            magnitude : 1,
            unit      : "day"
        }
    }
...
```

Or it can be provided as a positive number which means it's expressed in the clicked event [duration units](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-durationUnit).

[maxSplitDuration](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#config-maxSplitDuration)
Maximum allowed [split duration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-splitDuration). The value is used when calculating split duration automatically.

Setting the config to zero means not limiting [split duration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-splitDuration) max value.

The duration can be provided as [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) instance (or its configuration object) including both numeric and unit parts.

```
...
features : {
    eventSegments : {
        // split duration is automatic and changes depending on zoom level
        // but we limit its maximum as 1 week
        maxSplitDuration : {
            magnitude : 1,
            unit      : "week"
        }
    }
...
```

Or it can be provided as a positive number which means it's expressed in the clicked event [duration units](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-durationUnit).

Defaults to 1 day.

[minSplitDuration](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#config-minSplitDuration)
Minimum allowed [split duration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-splitDuration). The value is used when calculating split duration automatically.

Setting the config to zero (default) means not limiting [split duration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-splitDuration) min value.

The duration can be provided as [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) instance (or its configuration object) including both numeric and unit parts.

```
...
features : {
    eventSegments : {
        // split duration is automatic and changes depending on zoom level
        // limit its minimum as 1 hour
        minSplitDuration : {
            magnitude : 1,
            unit      : "hour"
        }
        // we limit its maximum as 1 day
        maxSplitDuration : {
            magnitude : 1,
            unit      : "day"
        }
    }
...
```

Or it can be provided as a positive number which means it's expressed in the clicked event [duration units](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-durationUnit).

[roundedSplit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#config-roundedSplit)
If `true`, it uses rounded dates when splitting

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventSegments](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#property-isEventSegments)
Identifies an object as an instance of [EventSegments](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments) class, or subclass thereof.

[isEventSegments](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#property-isEventSegments-static)
Identifies an object as an instance of [EventSegments](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments) class, or subclass thereof.

[roundedSplit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#property-roundedSplit)
If `true`, it uses rounded dates when splitting

## Functions

Functions are methods available for calling on the class

[getSplitDate](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#function-getSplitDate)
Returns a date at which to split an event.

Returns start date of the tick being clicked if the tick duration is less than [maxSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-maxSplitDuration) or [maxSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-maxSplitDuration) is zero. When the tick duration is greater than [maxSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-maxSplitDuration) returns `context.date` rounded based on active time axis resolution unit.

Override this method if you want to implement another way of calculating the split date.

See also: [getSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#function-getSplitDuration), [getSplitDurationUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#function-getSplitDurationUnit).

[getSplitDuration](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#function-getSplitDuration)
Returns the event split duration.

If [splitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-splitDuration) value is provided:

* as a `Number`the method returns the value as is
* as an `Object` or [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) instance - the method returns the value `unit` part

If [splitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-splitDuration) is **NOT** provided the method returns the clicked tick duration constrained by [minSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-minSplitDuration) and [maxSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-maxSplitDuration) values.

Override this method if you want to implement another way of the split duration calculating.

See also: [getSplitDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#function-getSplitDate), [getSplitDurationUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#function-getSplitDurationUnit).

[getSplitDurationUnit](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#function-getSplitDurationUnit)
Returns the duration unit to be used for the event splitting.

When [splitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#config-splitDuration) is provided as [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) instance or its configuration Object:

```
...
features : {
    eventSegments : {
        // split events by 1 day
        splitDuration : {
            magnitude : 1,
            unit      : "day"
        }
    }
    ...
}

```

the method returns the value `unit` part otherwise it returns the event [durationUnit](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/EventModel#field-durationUnit).

Override this method config-if you want to implement another way of the split duration unit defining.

See also: [getSplitDate](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#function-getSplitDate), [getSplitDuration](https://bryntum.com/docs/gantt/api/#SchedulerPro/feature/EventSegments#function-getSplitDuration).

[splitEvent](https://bryntum.com/docs/gantt/api/SchedulerPro/feature/EventSegments#function-splitEvent)
Handler for the "Split event" menu item
