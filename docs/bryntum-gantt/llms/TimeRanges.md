# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/TimeRanges.md

# [TimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges)

Feature that renders global ranges of time in the timeline. Use this feature to visualize a `range` like a 1 hr lunch or some important point in time (a `line`, i.e. a range with 0 duration). This feature can also show a current time indicator if you set [showCurrentTimeLine](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges#config-showCurrentTimeLine) to true. To style the rendered elements, use the [cls](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-cls) field of the `TimeSpan` class.

Each time range is represented by an instances of [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan), held in a simple [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store). The feature uses [timeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#property-timeRangeStore) defined on the project by default. The store's persisting/loading is handled by Crud Manager (if it's used by the component).

Note that the feature uses virtualized rendering, only the currently visible ranges are available in the DOM.

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

Showing an icon in the time range header
----------------------------------------

You can use Font Awesome icons easily (or set any other icon using CSS) by using the [iconCls](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan#field-iconCls) field. The JSON data below will show a flag icon:

```
{
    "id"        : 5,
    "iconCls"   : "fa fa-flag",
    "name"      : "v5.0",
    "startDate" : "2019-02-07 15:45"
},
```

Recurring time ranges
---------------------

The feature supports recurring ranges in case the provided store and models have [RecurringTimeSpansMixin](https://bryntum.com/docs/gantt/api/#Scheduler/data/mixin/RecurringTimeSpansMixin) and [RecurringTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/RecurringTimeSpan) mixins applied:

```
// We want to use recurring time ranges, so we make a special model extending standard TimeSpan model with
// RecurringTimeSpan which adds recurrence support
class MyTimeRange extends RecurringTimeSpan(TimeSpan) {}

// Define a new store extending standard Store with RecurringTimeSpansMixin mixin to add recurrence support to the
// store. This store will contain time ranges.
class MyTimeRangeStore extends RecurringTimeSpansMixin(Store) {
    static configurable = {
        // use our new MyResourceTimeRange model
        modelClass : MyTimeRange
    }
};

// Instantiate store for timeRanges using our new classes
const timeRangeStore = new MyTimeRangeStore({
    data : [{
        id             : 1,
        resourceId     : 'r1',
        startDate      : '2019-01-01T11:00',
        endDate        : '2019-01-01T13:00',
        name           : 'Lunch',
        // this time range should repeat every day
        recurrenceRule : 'FREQ=DAILY'
    }]
});

const scheduler = new Scheduler({
    ...
    features : {
        timeRanges : true
    },

    crudManager : {
        // store for "timeRanges" feature
        timeRangeStore
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[currentTimeLineUpdateInterval](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#config-currentTimeLineUpdateInterval)
The interval (as amount of ms) defining how frequently the current timeline will be updated

[currentDateFormat](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#config-currentDateFormat)
The date format to show in the header for the current time line (when [showCurrentTimeLine](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges#config-showCurrentTimeLine) is configured). See [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) for the possible formats to use.

[showCurrentTimeLine](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#config-showCurrentTimeLine)
Show a line indicating current time. Either `true` or `false` or a [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) configuration object to apply to this special time range (allowing you to provide a custom text):

```
showCurrentTimeLine : {
    name : 'Now'
}
```

The line carries the CSS class name `b-sch-current-time`, and this may be used to add custom styling to it.

[instantUpdate](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#config-instantUpdate)
Set to true to update the TimeRange header contents as well as the underlying record data while dragging it. In this case the record will be batch-updated during drag operations, you can listen for updates using the `batchUpdate` event fired by the time range store.

This flag is automatically set to `true` when you use a [headerRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges#config-headerRenderer).

[dragTipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#config-dragTipTemplate)
Template function used to generate the HTML for the drag tooltip that displays when dragging a time range. Override this to customize the drag tooltip content.

```
const scheduler = new Scheduler({
  features : {
    timeRanges : {
      dragTipTemplate({ timeRange, startText, endText, valid }) {
        return `
          <div class="my-drag-tip ${valid ? 'valid' : 'invalid'}">
            <div>Range: ${timeRange.name}</div>
            <div>Start: ${startText}</div>
            ${endText ? `<div>End: ${endText}</div>` : ''}
          </div>
        `;
      }
    }
  }
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#property-isTimeRanges)
Identifies an object as an instance of [TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) class, or subclass thereof.

[isTimeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#property-isTimeRanges-static)
Identifies an object as an instance of [TimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) class, or subclass thereof.

[showCurrentTimeLine](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#property-showCurrentTimeLine)
Show a line indicating current time. Either `true` or `false` or a [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) configuration object to apply to this special time range (allowing you to provide a custom text):

```
showCurrentTimeLine : {
    name : 'Now'
}
```

The line carries the CSS class name `b-sch-current-time`, and this may be used to add custom styling to it.

[timeRanges](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#property-timeRanges)
Returns the TimeRanges which occur within the client Scheduler's time axis.

[store](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#property-store)
Returns the [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) used by this feature. This is always the owning Scheduler/Gantt's Project TimeRangeStore.

## Functions

Functions are methods available for calling on the class

[populateTimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#function-populateTimeAxisHeaderMenu)
Adds a menu item to show/hide current time line.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[currentTimelineUpdate](https://bryntum.com/docs/gantt/api/Scheduler/feature/TimeRanges#event-currentTimelineUpdate)
Fires on the owning Scheduler/Gantt when the line indicating the current time is updated (see [currentTimeLineUpdateInterval](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges#config-currentTimeLineUpdateInterval)).
