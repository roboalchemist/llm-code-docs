# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/SchedulerBase.md

# [SchedulerBase](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase)

A thin base class for [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler). Does not include any features by default, allowing smaller custom-built bundles if used in place of [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler).

**NOTE:** In most scenarios you do probably want to use Scheduler instead of SchedulerBase.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[readOnly](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-readOnly)
Configure as `true` to make the scheduler read-only, by disabling any UIs for modifying data.

**Note that checks MUST always also be applied at the server side.**

[responsiveLevels](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-responsiveLevels)
"Break points" for which responsive config to use.

Each level can be specified as:

* A number representing the width threshold (e.g., `400`)
* The string `'*'` to match all sizes above other thresholds
* A [SchedulerResponsiveLevelConfig](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#typedef-SchedulerResponsiveLevelConfig) object with `levelWidth` and scheduler properties

See the [responsive guide](https://bryntum.com/docs/gantt/api/#Scheduler/guides/customization/responsive.md) for details and examples.

[date](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-date)
The date to display when used as a component of a Calendar.

This is required by the Calendar Mode Interface.

[listRangeMenu](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-listRangeMenu)
This property is for use when the Scheduler is used as a Calendar view - a `mode`.

A [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) configuration block which configures the range choosing menu provided which by default selects one of the following:

* day
* week
* month
* year
* decade

This menu is added to the [TimeAxisHeaderMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeAxisHeaderMenu) when the Scheduler is used as a Calendar view.

This may be used to either reconfigure that menu, or, by configuring it as `null`, could remove the menu entirely if the date range of this view is controlled by other means.

The individual range menu items are under the `items` property and have the following property names:

* `listRangeDayItem`
* `listRangeWeekItem`
* `listRangeMonthItem`
* `listRangeYearItem`
* `listRangeDecadeItem`

These may be reconfigured:

```
calendar = new Calendar({
    ...
    modes : {
        timeline : {
            type          : 'scheduler',
            range         : 'month',
            listRangeMenu : {
                items : {
                    // We don't want the decade range option
                    listRangeDecadeItem : null
                }
            }
        }
    }
});
```

[shiftIncrement](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-shiftIncrement)
This property is for use when the Scheduler is used as a Calendar view - a `mode`. it will have no effect on a Scheduler which is not inside a Calendar.

The time range to move by when [next](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#function-next) or [previous](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#function-previous) is called.

If not specified, this view moves by its duration in days as derived from its [range](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-range).

Valid values are:

* day
* week
* month
* year
* decade

This may also be specified as a duration with a magnitude part and a unit part. For example `'1m'` would mean one month, and `'4w'` would mean four weeks. See [parseDuration](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parseDuration-static) for details of syntax.

When using a range of weeks, months, years or decades, then when this widget's [date](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-date) is synced with its owning Calendar's date, this widget's [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) is snapped to the closest start point of the range which encompasses that date.

So if using `range : '1w'`, then setting the date to Thursday, 28th October 2021 Would mean that the `startDate` snaps to Sunday 24th October 2021 (assuming the locale uses Sunday as the week start day).

If configured to use a range of _days_, no snapping is done. There's no defined start point so the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) is set to the incoming Calendar date.

[range](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-range)
Range used to set the length of the time axis when used as a component of a Calendar. Suitable units are `'month'`, `'week'` and `'day'`.

This may also be specified as a duration with a magnitude part and a unit part. For example `'1m'` would mean one month, and `'4w'` would mean four weeks. See [parseDuration](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parseDuration-static) for details of syntax.

When using a range of weeks or months, then when this widget's [date](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-date) is synced with its owning Calendar's date property, this widget's [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) is snapped to the closest start point of the range which encompasses that date.

So if using `range : '1w'`, then setting the date to Thursday, 28th October 2021 Would mean that the `startDate` snaps to Sunday 24th October 2021 (assuming the locale uses Sunday as the week start day).

[getDateConstraints](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-getDateConstraints)
A method allowing you to define date boundaries that will constrain resize, create and drag drop operations. The method will be called with the Resource record, and the Event record.

```
 new Scheduler({
     getDateConstraints(resourceRecord, eventRecord) {
         // Assuming you have added these extra fields to your own EventModel subclass
         const { minStartDate, maxEndDate } = eventRecord;

         return {
             start : minStartDate,
             end   : maxEndDate
         };
     }
 });
```

[verticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-verticalTimeAxisColumn)
The time axis column config for vertical [mode](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-mode).

Object with [VerticalTimeAxisColumn](https://bryntum.com/docs/gantt/api/#Scheduler/column/VerticalTimeAxisColumn) configuration.

This object will be used to configure the vertical time axis column instance.

The config allows configuring the `VerticalTimeAxisColumn` instance used in vertical mode with any Column options that apply to it.

Example:

```
new Scheduler({
    mode     : 'vertical',
    features : {
        filterBar : true
    },
    verticalTimeAxisColumn : {
        text  : 'Filter by event name',
        width : 180,
        filterable : {
            // add a filter field to the vertical column access header
            filterField : {
                type        : 'text',
                placeholder : 'Type to search',
                onChange    : ({ value }) => {
                    // filter event by name converting to lowerCase to be equal comparison
                    scheduler.eventStore.filter({
                        filters : event => event.name.toLowerCase().includes(value.toLowerCase()),
                        replace : true
                    });
                }
            }
        }
    },
    ...
});
```

[keyMap](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#keyboard-shortcuts) for details

[autoCreate](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-autoCreate)
If this config is set, then its `gesture` property (which defaults to `dblclick`) creates a new event at the mouse or touch event's time point.

When set to `true`, the gesture is `dblclick`, and the new event will have a duration of 1 time axis tick.

This may be specified as the string DOM event name to listen for, such as `'click'`, `'dblclick'` and the new event will have a duration of 1 time axis tick.

The duration of the new event can be set by specifying the `duration` property as a [DurationConfig](https://bryntum.com/docs/gantt/api/#Core/data/Duration#typedef-DurationConfig).

If that is not set, then setting the `useEventModelDefaults` property will cause the duration to be specified by the default values of the [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-duration) and [durationUnit](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-durationUnit) fields

Example:

```
new Scheduler({
    autoCreate : {
        gesture  : 'click',
        duration : '2 hours',
        newName  : 'New appointment'
    }
});
```

[scrollBuffer](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-scrollBuffer)
Number of pixels to horizontally extend the visible render zone by, controlling the events that will be rendered. You can use this to increase or reduce the amount of event rendering happening when scrolling along a horizontal time axis. This can be useful if you render huge amount of events.

To force the scheduler to render all events within the TimeAxis start & end dates, set this to -1. The initial render will take slightly longer but no extra event rendering will take place when scrolling.

NOTE: This is an experimental API which might change in future releases.

[showEventColorPickers](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-showEventColorPickers)
If set to `true` this will show a color field in the [EventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit) editor and also a picker in the [EventMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventMenu). Both enables the user to choose a color which will be applied to the event bar's background. See EventModel's [eventColor](https://bryntum.com/docs/gantt/api/#Scheduler/model/mixin/EventModelMixin#field-eventColor) config. config.

[updateTimelineContextOnScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-updateTimelineContextOnScroll)
By default, scrolling the schedule will update the [timelineContext](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-timelineContext) to reflect the new currently hovered context. When displaying a large number of events on screen at the same time, this will have a slight impact on scrolling performance. In such scenarios, opt out of this behavior by setting this config to `false`.

[lazyLoadingIndicator](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-lazyLoadingIndicator)
By default, when the `EventStore` (and similar stores) is lazy loading, a loading indicator will be displayed just below the timeline headers. Set this to `false` to prevent this indicator being shown.

[transition](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-transition)
Configure UI transitions for various actions in the grid.

[mode](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-mode)
Scheduler mode. Supported values: horizontal, vertical

[eventCls](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-eventCls)
CSS class to add to rendered events

[timeCellCls](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-timeCellCls)
CSS class to add to cells in the timeaxis column

[overScheduledEventClass](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-overScheduledEventClass)
A CSS class to apply to each event in the view on mouseover (defaults to 'b-hover').

[allowOverlap](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-allowOverlap)
Set to `false` if you don't want to allow events overlapping times for any one resource (defaults to `true`).

Note that toggling this at runtime won't affect already overlapping events.

[rowHeight](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-rowHeight)
The height in pixels of Scheduler rows.

[getRowHeight](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-getRowHeight)
Scheduler overrides Grid's default implementation of [getRowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-getRowHeight) to pre-calculate row heights based on events in the rows.

The amount of rows that are pre-calculated is limited for performance reasons. The limit is configurable by specifying the [preCalculateHeightLimit](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-preCalculateHeightLimit) config.

The results of the calculation are cached internally.

Apps are not currently intended to override this logic, instead they can control height of individual rows using a cell `renderer`. See the snippet below for an example.

```
new Scheduler({
    columns : [
        {
            text  : 'Name',
            field : 'name',
            width : 130,
            renderer({ value, record, size }) {
                // Set your desired height here
                size.height = record.parentIndex % 2 === 0 ? 100 : 40;

                return value;
            }
        }
    ]
});
```

Also note that the height set is used as the base height for the event layout used, for example if stacking two events in a stack layout, the row will be twice as heigh (+ any margins).

[preCalculateHeightLimit](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-preCalculateHeightLimit)
Maximum number of resources for which height is pre-calculated. If you have many events per resource you might want to lower this number to gain some initial rendering performance.

Specify a falsy value to opt out of row height pre-calculation.

[inheritEventColor](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-inheritEventColor)
Set to true for child nodes in a tree store to inherit their parent´s `eventColor`

[events](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-events)
Inline events, will be loaded into an internally created EventStore.

[eventStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-eventStore)
The [EventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/EventStore) holding the events to be rendered into the scheduler (required).

[resources](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-resources)
Inline resources, will be loaded into an internally created ResourceStore.

[resourceStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-resourceStore)
The [ResourceStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceStore) holding the resources to be rendered into the scheduler (required).

[assignments](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-assignments)
Inline assignments, will be loaded into an internally created AssignmentStore.

[assignmentStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-assignmentStore)
The optional [AssignmentStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/AssignmentStore), holding assignments between resources and events. Required for multi assignments.

[dependencies](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-dependencies)
Inline dependencies, will be loaded into an internally created DependencyStore.

[dependencyStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#config-dependencyStore)
The optional [DependencyStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/DependencyStore).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSchedulerBase](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-isSchedulerBase)
Identifies an object as an instance of [SchedulerBase](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase) class, or subclass thereof.

[isSchedulerBase](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-isSchedulerBase-static)
Identifies an object as an instance of [SchedulerBase](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase) class, or subclass thereof.

[readOnly](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-readOnly)
Get/set the scheduler's read-only state. When set to `true`, any UIs for modifying data are disabled.

[date](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-date)
The date to display when used as a component of a Calendar.

This is required by the Calendar Mode Interface.

[shiftIncrement](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-shiftIncrement)
This property is for use when the Scheduler is used as a Calendar view - a `mode`. it will have no effect on a Scheduler which is not inside a Calendar.

The time range to move by when [next](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#function-next) or [previous](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#function-previous) is called.

If not specified, this view moves by its duration in days as derived from its [range](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-range).

Valid values are:

* day
* week
* month
* year
* decade

This may also be specified as a duration with a magnitude part and a unit part. For example `'1m'` would mean one month, and `'4w'` would mean four weeks. See [parseDuration](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parseDuration-static) for details of syntax.

When using a range of weeks, months, years or decades, then when this widget's [date](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-date) is synced with its owning Calendar's date, this widget's [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) is snapped to the closest start point of the range which encompasses that date.

So if using `range : '1w'`, then setting the date to Thursday, 28th October 2021 Would mean that the `startDate` snaps to Sunday 24th October 2021 (assuming the locale uses Sunday as the week start day).

If configured to use a range of _days_, no snapping is done. There's no defined start point so the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) is set to the incoming Calendar date.

[range](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-range)
The time range encapsulated by the current [date](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-date).

When a range is used, changing the [date](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-date) snaps the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) to the closest starting date of the range. For Example if the range was configured as `'1 week'` then setting the date to the date of next Wednesday would mean that the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-startDate) would be the **start** of next week, and an entire week would be encapsulated by this view.

[autoCreate](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-autoCreate)
If this config is set, then its `gesture` property (which defaults to `dblclick`) creates a new event at the mouse or touch event's time point.

When set to `true`, the gesture is `dblclick`, and the new event will have a duration of 1 time axis tick.

This may be specified as the string DOM event name to listen for, such as `'click'`, `'dblclick'` and the new event will have a duration of 1 time axis tick.

The duration of the new event can be set by specifying the `duration` property as a [DurationConfig](https://bryntum.com/docs/gantt/api/#Core/data/Duration#typedef-DurationConfig).

If that is not set, then setting the `useEventModelDefaults` property will cause the duration to be specified by the default values of the [duration](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-duration) and [durationUnit](https://bryntum.com/docs/gantt/api/#Scheduler/model/EventModel#field-durationUnit) fields

Example:

```
new Scheduler({
    autoCreate : {
        gesture  : 'click',
        duration : '2 hours',
        newName  : 'New appointment'
    }
});
```

[updateTimelineContextOnScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-updateTimelineContextOnScroll)
By default, scrolling the schedule will update the [timelineContext](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-timelineContext) to reflect the new currently hovered context. When displaying a large number of events on screen at the same time, this will have a slight impact on scrolling performance. In such scenarios, opt out of this behavior by setting this config to `false`.

[lazyLoadingIndicator](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-lazyLoadingIndicator)
By default, when the `EventStore` (and similar stores) is lazy loading, a loading indicator will be displayed just below the timeline headers. Set this to `false` to prevent this indicator being shown.

[transition](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-transition)
Configure UI transitions for various actions in the grid.

[allowOverlap](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-allowOverlap)
Set to `false` if you don't want to allow events overlapping times for any one resource (defaults to `true`).

Note that toggling this at runtime won't affect already overlapping events.

[inheritEventColor](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-inheritEventColor)
Set to true for child nodes in a tree store to inherit their parent´s `eventColor`

[events](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-events)
Get/set events, applies to the backing project's EventStore.

[eventStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-eventStore)
Get/set the event store instance of the backing project.

[resources](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-resources)
Get/set resources, applies to the backing project's ResourceStore.

[resourceStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-resourceStore)
Get/set the resource store instance of the backing project

[assignments](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-assignments)
Get/set assignments, applies to the backing project's AssignmentStore.

[assignmentStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-assignmentStore)
Get/set the event store instance of the backing project.

[dependencies](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-dependencies)
Get/set dependencies, applies to the backing projects DependencyStore.

[dependencyStore](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-dependencyStore)
Get/set the dependencies store instance of the backing project.

[visibleResources](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-visibleResources)
Returns an object defining the range of visible resources

[isHorizontal](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-isHorizontal)
Checks if scheduler is in horizontal mode

[isVertical](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-isVertical)
Checks if scheduler is in vertical mode

[mode](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-mode)
Get mode (horizontal/vertical)

[dateBounds](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-dateBounds)
Returns the date or ranges of included dates as an array. If only the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) is significant, the array will have that date as its only element. Otherwise, a range of dates is returned as a two-element array with `[0]` is the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-startDate) and `[1]` is the [lastDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-lastDate).

[lastDate](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-lastDate)
The last day that is included in the date range. This is different than [endDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-endDate) since that date is not inclusive. For example, an `endDate` of 2022-07-21 00:00:00 indicates that the time range ends at that time, and so 2022-07-21 is _not_ in the range. In this example, `lastDate` would be 2022-07-20 since that is the last day included in the range.

[listRangeMenu](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-listRangeMenu)
This property is for use when the Scheduler is used as a Calendar view - a `mode`.

This property yields a [Menu](https://bryntum.com/docs/gantt/api/#Core/widget/Menu) configuration block which encapsulates the range choices which this widget may be set to encapsulate:

* day
* week
* month
* year
* decade

By default a `list` view adds these choices to the header context menu. An `agenda` view creates a floating settings button which offers this menu. The property may be used to create a custom UI for changing the range. The value yielded by the default `get listRangeMenu()` implementation looks like this:

```
{
    items : {
        listRangeDayItem    : {config for DAY range menu item },
        listRangWeekItem    : {config for WEEK range menu item },
        listRangMonthItem   : {config for MONTH range menu item },
        listRangeYearItem   : {config for YEAR range menu item },
        listRangeDecadeItem : {config for DECADE range menu item }
    }
}
```

A subclass can override `get listRangeMenu()` and mutate the object returned by the `super` call.

For example, it could `delete` properties of the `items` block to limit which ranges may be selected.

[eventCount](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#property-eventCount)
Gets the count of events within a date range between current `startDate` and `endDate`.

## Functions

Functions are methods available for calling on the class

[editEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-editEvent)
Opens an editor UI to edit the passed event, or a config object for a new event.

_NOTE: Only available when the [EventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit) feature is enabled._

[resolveDependencyRecord](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-resolveDependencyRecord)
Returns the dependency record for a DOM element

_NOTE: Only available when the [Dependencies](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Dependencies) feature is enabled._

[onEventCreated](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-onEventCreated)
Called when new event is created. Сan be overridden to supply default record values etc.

[createEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-createEvent)
Creates an event on the specified date which conforms to the [autoCreate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-autoCreate) setting for the specified resource. The event is then scrolled into view.

NOTE: If the scheduler is readonly, or resource type is invalid (group header), or if `allowOverlap` is `false` and slot is already occupied - no event is created.

This method may be called programmatically by application code if the [autoCreate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-autoCreate) setting is `false`, in which case the default values for [autoCreate](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-autoCreate) will be used.

If the [EventEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventEdit) feature is active, the new event will be displayed in the event editor.

[isDateRangeAvailable](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-isDateRangeAvailable)
Checks if a date range is allocated or not for a given resource.

[resumeRefresh](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-resumeRefresh)
Resumes UI refresh on store operations.

Multiple calls to `suspendRefresh` stack up, and will require an equal number of `resumeRefresh` calls to actually resume UI refresh.

Specify `true` as the first param to trigger a refresh if this call unblocked the refresh suspension. If the underlying project is calculating changes, the refresh will be postponed until it is done.

[refreshResource](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-refreshResource)
Triggers a render of all the cells (in horizontal mode) in and event bars for the passed resource.

Since Scheduler uses virtualized resources, calling this method for a resource that is not currently rendered will not have any effect.

Manipulating resource or event records and Scheduler settings refreshes the Scheduler automatically. You should only need to call this function if you have outside data/settings unknown to the Scheduler that has changed and requires the resource to update to reflect the changes

[refreshResources](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-refreshResources)
Triggers a render of all the cells (in horizontal mode) and event bars for the passed resources. Leave the argument out to refresh all resources.

Since Scheduler uses virtualized resources, calling this method for resources that are not currently rendered will not have any effect.

Manipulating resource or event records and Scheduler settings refreshes the Scheduler automatically. You should only need to call this function if you have outside data/settings unknown to the Scheduler that has changed and requires some resources to update to reflect the changes

[previous](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-previous)
Interface method used by an encapsulating Calendar view to implement the "prev" button.

[next](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-next)
Interface method used by an encapsulating Calendar view to implement the "next" button.

[scheduleEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-scheduleEvent)
Assigns and schedules an unassigned event record (+ adds it to this Scheduler's event store unless already in it).

[internalGetAssignmentsToHighlight](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-internalGetAssignmentsToHighlight)
Internal function to get an array of assignment instances from:

* Single event or assignment instance
* Array of event or assignment instances
* Single event or assignment id (depending on `usesSingleAssignment`)
* Array of event or assignment ids (depending on `usesSingleAssignment`)

[getEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#function-getEvents)
Returns an array of events for the date range specified by the `startDate` and `endDate` options.

By default, for any date, this includes any event which _intersects_ that date.

To only include events that are fully contained _within_ the date range, pass the `allowPartial` option as `false`.

By default, any occurrences of recurring events are included in the resulting array (not applicable in Gantt). If that is not required, pass the `includeOccurrences` option as `false`.

Note that if `includeOccurrences` is `true`, the start date and end date options are mandatory. The method must know what range of occurrences needs to be generated and returned.

Example:

```
 visibleEvents = eventStore.getEvents({
     resourceRecord : myResource,
     startDate      : scheduler.timeAxis.startDate,
     endDate        : scheduler.timeAxis.endDate
 });
```

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[renderEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-renderEvent)
Fired after rendering an event, when its element is available in DOM.

[releaseEvent](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-releaseEvent)
Fired after releasing an event, useful to cleanup of custom content added on `renderEvent` or in `eventRenderer`.

[resourceHeaderClick](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-resourceHeaderClick)
Fired when clicking a resource header cell

[resourceHeaderDblclick](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-resourceHeaderDblclick)
Fired when double clicking a resource header cell

[resourceHeaderContextmenu](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-resourceHeaderContextmenu)
Fired when activating context menu on a resource header cell

[eventKeyDown](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-eventKeyDown)
Triggered when a keydown event is observed if there are selected events.

[eventKeyUp](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-eventKeyUp)
Triggered when a keyup event is observed if there are selected events.

[beforeAutoCreate](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-beforeAutoCreate)
This event fires whenever the [autoCreate gesture](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#config-autoCreate) is detected.

This event is preventable and may be used to validate autoCreate-initiated event creation.

[beforeEventAdd](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-beforeEventAdd)
Fires before an event is added. Can be triggered by schedule double click or drag create action.

[eventAutoCreated](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-eventAutoCreated)
Fired when a double click or drag gesture has created a new event and added it to the event store.

[shiftIncrementChange](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#event-shiftIncrementChange)
Fired when the [shiftIncrement](https://bryntum.com/docs/gantt/api/#Scheduler/view/SchedulerBase#property-shiftIncrement) of this view changes.

This event is only fired when used as a mode of a Calendar

## Typedefs

Typedefs are type definitions for the class

[DateConstraint](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#typedef-DateConstraint)
Type containing `start` and `end` constraints.

[SchedulerResponsiveLevelConfig](https://bryntum.com/docs/gantt/api/Scheduler/view/SchedulerBase#typedef-SchedulerResponsiveLevelConfig)
Configuration object for a responsive level. Contains a required `levelWidth` plus any [SchedulerState](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/SchedulerState) properties to apply when this level is active.
