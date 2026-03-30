# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/TimelineBase.md

# [TimelineBase](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase)

Abstract base class used by timeline based components such as Scheduler and Gantt. Based on Grid, supplies a "locked" region for columns and a "normal" for rendering of events etc.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[startDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-startDate)
The start date of the timeline (if not configure with [infiniteScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-infiniteScroll)).

If omitted, and a TimeAxis has been set, the start date of the provided [TimeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis) will be used. If no TimeAxis has been configured, it'll use the start/end dates of the loaded event dataset. If no date information exists in the event data set, it defaults to the current date and time.

If a string is supplied, it will be parsed using [DateHelper.defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static).

When using [infiniteScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-infiniteScroll), use [visibleDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-visibleDate) to control initially visible date instead.

**Note:** If you need to set start and end date at the same time, use the [setTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-setTimeSpan) method.

[endDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-endDate)
The end date of the timeline (if not configure with [infiniteScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-infiniteScroll)).

If omitted, it will be calculated based on the [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-startDate) setting and the 'defaultSpan' property of the current [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-viewPreset).

If a string is supplied, it will be parsed using [DateHelper.defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static).

**Note:** If you need to set start and end date at the same time, use the [setTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-setTimeSpan) method.

[minDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-minDate)
Get/set start date limit of the timeline. Actions such as timeline scrolling, all types of timeline zooms and shifts will respect this limit.

[maxDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-maxDate)
Get/set end date limit of the timeline. Actions such as timeline scrolling, all types of timeline zooms and shifts will respect this limit.

[partner](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-partner)
Partners this Timeline panel with another Timeline in order to sync their region sizes (sub-grids like locked, normal will get the same width), start and end dates, view preset, zoom level and scrolling position. All these values will be synced with the timeline defined as the `partner`.

Can be specified as:

* A Timeline instance reference

* A string selector: widget type (e.g. `'gantt'`), id selector (e.g. `'#myGantt'`), or attribute selector (e.g. `'[ref=myGantt]'`)

* To add a new partner dynamically see [addPartner](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-addPartner) method.

* To remove existing partner see [removePartner](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-removePartner) method.

* To check if timelines are partners see [isPartneredWith](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-isPartneredWith) method.

Column widths and hide/show state are synced between partnered schedulers when the column set is identical.

[stickyHeaders](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-stickyHeaders)
When set, the text in the major time axis header sticks in the scrolling viewport as long as possible.

[visibleDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-visibleDate)
A date to bring into view initially on the scrollable timeline.

This may be configured as either a `Date` or a scrolling `options` object describing the scroll action, including a `date` option which references a `Date`.

See [scrollToDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-scrollToDate) for details about scrolling options.

Note that if a naked `Date` is passed, it will be stored internally as a scrolling options object using the following defaults:

```
{
    date  : <The Date object>,
    block : 'nearest'
}
```

This moves the date into view by the shortest scroll, so that it just appears at an edge.

To bring your date of interest to the center of the viewport, configure your Scheduler thus:

```
    visibleDate : {
        date  : new Date(2023, 5, 17, 12),
        block : 'center'
    }
```

[eventCls](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-eventCls)
CSS class to add to rendered events

[forceFit](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-forceFit)
Set to `true` to force the time columns to fit to the available space (horizontal or vertical depends on mode). Note that setting [suppressFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-suppressFit) to `true`, will disable `forceFit` functionality. Zooming cannot be used when `forceFit` is set.

[timeZone](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-timeZone)
Set to a time zone or a UTC offset. This will set the projects [timeZone](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#config-timeZone) config accordingly. As this config is only a referer, please see project's config [documentation](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#config-timeZone) for more information.

```
new Calendar(){
  timeZone : 'America/Chicago'
}
```

[hideRowHover](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-hideRowHover)
By default the row hover effect is not visible in the Scheduler part of the grid.

Set this to `false` to show the hover effect in Scheduler rows.

[weekStartDay](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-weekStartDay)
A valid JS day index between 0-6 (0: Sunday, 1: Monday etc.) to be considered the start day of the week. When omitted, the week start day is retrieved from the active locale class.

[workingTime](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-workingTime)
An object with format `{ fromDay, toDay, fromHour, toHour }` that describes the working days and hours. This object will be used to populate TimeAxis [include](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis#config-include) property.

Using it results in a non-continuous time axis. Any ticks not covered by the working days and hours will be excluded. Events within larger ticks (for example if using week as the unit for ticks) will be stretched to fill the gap otherwise left by the non-working hours.

As with end dates, `toDay` and `toHour` are exclusive. Thus `toDay : 6` means that day 6 (saturday) will not be included.

**NOTE:** When this feature is enabled [Zooming feature](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable) is not supported. It's recommended to disable zooming controls:

```
new Scheduler({
    zoomOnMouseWheel          : false,
    zoomOnTimeAxisDoubleClick : false,
    ...
});
```

[snapRelativeToEventStartDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-snapRelativeToEventStartDate)
Affects drag drop and resizing of events when [snap](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineDateMapper#config-snap) is enabled.

If set to `true`, dates will be snapped relative to event start. e.g. for a zoom level with `timeResolution = { unit: "s", increment: "20" }`, an event that starts at 10:00:03 and is dragged would snap its start date to 10:00:23, 10:00:43 etc.

When set to `false`, dates will be snapped relative to the timeAxis startDate (tick start)

* 10:00:03 -> 10:00:20, 10:00:40 etc.

[suppressFit](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-suppressFit)
Set to `true` to prevent auto calculating of a minimal [tickSize](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#property-tickSize) to always fit the content to the screen size. Setting this property on `true` will disable [forceFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-forceFit) behaviour.

[timeCellCls](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-timeCellCls)
CSS class to add to cells in the timeaxis column

[overScheduledEventClass](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-overScheduledEventClass)
A CSS class to apply to each event in the view on mouseover.

[enableEventAnimations](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-enableEventAnimations)
Set to `false` if you don't want event bar DOM updates to animate.

[defaultRegion](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-defaultRegion)
Region to which columns are added when they have none specified

[durationDisplayPrecision](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-durationDisplayPrecision)
Decimal precision used when displaying durations, used by tooltips and DurationColumn. Specify `false` to use raw value

[autoAdjustTimeAxis](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-autoAdjustTimeAxis)
You can set this option to `false` to make the timeline panel start and end on the exact provided [startDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-startDate)/[endDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-endDate) w/o adjusting them.

[timeAxis](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-timeAxis)
A [TimeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis) config object or instance, used to create a backing data store of 'ticks' providing the input date data for the time axis of timeline panel. Created automatically if none supplied.

[timeAxisViewModel](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#config-timeAxisViewModel)
The backing view model for the visual representation of the time axis. Either a real instance or a simple config object.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimelineBase](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-isTimelineBase)
Identifies an object as an instance of [TimelineBase](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase) class, or subclass thereof.

[isTimelineBase](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-isTimelineBase-static)
Identifies an object as an instance of [TimelineBase](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase) class, or subclass thereof.

[startDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-startDate)
Get/set startDate. Defaults to current date if none specified.

When using [infiniteScroll](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-infiniteScroll), use [visibleDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-visibleDate) to control initially visible date instead.

**Note:** If you need to set start and end date at the same time, use [setTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-setTimeSpan) method.

[endDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-endDate)
Get/set endDate. Defaults to startDate + default span of the used ViewPreset.

**Note:** If you need to set start and end date at the same time, use [setTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-setTimeSpan) method.

[minDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-minDate)
Get/set start date limit of the timeline. Actions such as timeline scrolling, all types of timeline zooms and shifts will respect this limit.

[maxDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-maxDate)
Get/set end date limit of the timeline. Actions such as timeline scrolling, all types of timeline zooms and shifts will respect this limit.

[visibleDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-visibleDate)
A scrolling `options` object describing the scroll action, including a `date` option which references a `Date`. See [scrollToDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-scrollToDate) for details about scrolling options.

```
    // The date we want in the center of the Scheduler viewport
    myScheduler.visibleDate = {
        date    : new Date(2023, 5, 17, 12),
        block   : 'center',
        animate : true
    };
```

[forceFit](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-forceFit)
Set to `true` to force the time columns to fit to the available space (horizontal or vertical depends on mode). Note that setting [suppressFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-suppressFit) to `true`, will disable `forceFit` functionality. Zooming cannot be used when `forceFit` is set.

[timeZone](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-timeZone)
Set to a time zone or a UTC offset. This will set the projects [timeZone](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#config-timeZone) config accordingly. As this config is only a referer, please see project's config [documentation](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#config-timeZone) for more information.

```
new Calendar(){
  timeZone : 'America/Chicago'
}
```

[hideRowHover](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-hideRowHover)
By default the row hover effect is not visible in the Scheduler part of the grid.

Set this to `false` to show the hover effect in Scheduler rows.

[workingTime](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-workingTime)
An object with format `{ fromDay, toDay, fromHour, toHour }` that describes the working days and hours. This object will be used to populate TimeAxis [include](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis#config-include) property.

Using it results in a non-continuous time axis. Any ticks not covered by the working days and hours will be excluded. Events within larger ticks (for example if using week as the unit for ticks) will be stretched to fill the gap otherwise left by the non-working hours.

As with end dates, `toDay` and `toHour` are exclusive. Thus `toDay : 6` means that day 6 (saturday) will not be included.

**NOTE:** When this feature is enabled [Zooming feature](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineZoomable) is not supported. It's recommended to disable zooming controls:

```
new Scheduler({
    zoomOnMouseWheel          : false,
    zoomOnTimeAxisDoubleClick : false,
    ...
});
```

[suppressFit](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-suppressFit)
Set to `true` to prevent auto calculating of a minimal [tickSize](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineEventRendering#property-tickSize) to always fit the content to the screen size. Setting this property on `true` will disable [forceFit](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-forceFit) behaviour.

[enableEventAnimations](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-enableEventAnimations)
Set to `false` if you don't want event bar DOM updates to animate.

[timeAxis](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-timeAxis)
A backing data store of 'ticks' providing the input date data for the time axis of timeline panel.

[timeAxisColumn](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-timeAxisColumn)
Returns the TimeAxisColumn instance

[hasVisibleEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-hasVisibleEvents)
Returns `true` if any of the events/tasks or feature injected elements (such as ResourceTimeRanges) are within the [timeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-timeAxis)

[partners](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-partners)
Returns the partnered timelines.

* To add a new partner see [addPartner](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-addPartner) method.
* To remove existing partner see [removePartner](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-removePartner) method.

[timeAxisViewModel](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-timeAxisViewModel)
The internal view model, describing the visual representation of the time axis.

[timeAxisSubGrid](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-timeAxisSubGrid)
Returns the subGrid containing the time axis

[timeAxisSubGridElement](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-timeAxisSubGridElement)
Returns the html element for the subGrid containing the time axis

[visibleDateRange](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#property-visibleDateRange)
Returns an object representing the visible date range

## Functions

Functions are methods available for calling on the class

[populateEventMenu](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-populateEventMenu)
Populates the event context menu. Chained in features to add menu items.

[populateScheduleMenu](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-populateScheduleMenu)
Populates the time axis context menu. Chained in features to add menu items.

[initScroll](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-initScroll)
Overrides initScroll from Grid, listens for horizontal scroll to do virtual event rendering

[preserveViewCenter](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-preserveViewCenter)
Calls the specified function (returning its return value) and preserves the timeline center point. This is a useful way of retaining the user's visual context while making updates and changes to the view which require major changes or a full refresh.

[setTimeSpan](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-setTimeSpan)
Changes the Scheduler's time axis timespan to the supplied start and end dates.

[addPartner](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-addPartner)
Partners this Timeline with the passed Timeline in order to sync the horizontal scrolling position and zoom level.

* To remove existing partner see [removePartner](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-removePartner) method.
* To get the list of partners see [partners](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#property-partners) getter.

The following properties are imported into this component from the added partner and shared:

* [timeAxisViewModel](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#property-timeAxisViewModel)
* [timeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#property-timeAxis)
* [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#property-viewPreset)

In a set of partnered Timelines, there will only be a single instance of the above properties. The time range and scroll position in that time range are always the same among all partnered timelines.

[removePartner](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-removePartner)
Breaks the link between current Timeline and the passed Timeline

* To add a new partner see [addPartner](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-addPartner) method.
* To get the list of partners see [partners](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#property-partners) getter.

[isPartneredWith](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-isPartneredWith)
Checks whether the passed timeline is partnered with the current timeline.

[setStartDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-setStartDate)
Sets the timeline start date.

**Note:**

* If you need to set start and end date at the same time, use the [setTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-setTimeSpan) method.
* If keepDuration is false and new start date is greater than end date, it will throw an exception.

[setEndDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-setEndDate)
Sets the timeline end date

**Note:**

* If you need to set start and end date at the same time, use the [setTimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#function-setTimeSpan) method.
* If keepDuration is false and new end date is less than start date, it will throw an exception.

[onBodyResize](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-onBodyResize)
Called when the element which encapsulates the Scheduler's visible height changes size. We only respond to _height_ changes here. The TimeAxisSubGrid monitors its own width.

[getHeaderDomConfigs](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-getHeaderDomConfigs)
A chainable function which Features may hook to add their own content to the timeaxis header.

[getForegroundDomConfigs](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-getForegroundDomConfigs)
A chainable function which Features may hook to add their own content to the foreground canvas

[refreshWithTransition](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-refreshWithTransition)
Refreshes the grid with transitions enabled.

[formatDuration](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-formatDuration)
Returns a rounded duration value to be displayed in UI (tooltips, labels etc)

[applyStartEndParameters](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-applyStartEndParameters)
Applies the start and end date to each event store request (formatted in the same way as the start date field, defined in the EventStore Model class).

[highlightEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-highlightEvents)
Highlights the elements of the passed event or assignment records (or record ids). If `scrollToClosest` is set to `true` (which it is by default), the highlighted event element closest to the viewport center will be scrolled into view.

The highlighting will be done by adding the css class `b-highlighted` to the highlighted event elements. Also, the css class `b-is-highlighting` will be added to the `TimeAxisSubGrid` element.

```
// Highlight single event
scheduler.highlightEvents({ events : 22 });
// Highlight multiple events
scheduler.highlightEvents({ events : [1, 40] });
// Don't scroll to highlighted event, and don't un-highlight on click
scheduler.highlightEvents({ events : 1000, scroll : false, unhighlightOnClick : false });
```

[unhighlightEvents](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#function-unhighlightEvents)
Removes highlighting from the elements of the passed event or assignment records (or record ids). If no events are passed all highlighted events will be un-highlighted.

```
scheduler.unhighlightEvents({ events : 22 }); // single event
scheduler.unhighlightEvents({ events : [1, 40] }); // multiple events
```

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[visibleDateRangeChange](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#event-visibleDateRangeChange)
Fired when the range of dates visible within the viewport changes. This will be when scrolling along a time axis.

**Note** that this event will fire frequently during scrolling, so any listener should probably be added with the `buffer` option to slow down the calls to your handler function :

```
listeners : {
    visibleDateRangeChange({ old, new }) {
        this.updateRangeRequired(old, new);
    },
    // Only call once. 300 ms after the last event was detected
    buffer : 300
}
```

[dateRangeChange](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#event-dateRangeChange)
Fired when the range of dates encapsulated by the UI changes. This will be when moving a view in time by reconfiguring its [timeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-timeAxis). This will happen when zooming, or changing [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#config-viewPreset).

Contrast this with the [visibleDateRangeChange](https://bryntum.com/docs/gantt/api/#Scheduler/view/TimelineBase#event-visibleDateRangeChange) event which fires much more frequently, during scrolling along the time axis and changing the **visible** date range.

[timeAxisChange](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#event-timeAxisChange)
Fired when the timeaxis has changed, for example by zooming or configuring a new time span.

[timelineViewportResize](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#event-timelineViewportResize)
Fired when the _scheduler_ viewport (not the overall Scheduler element) changes size. This happens when the grid changes height, or when the subgrid which encapsulates the scheduler column changes width.

## Typedefs

Typedefs are type definitions for the class

[VisibleDate](https://bryntum.com/docs/gantt/api/Scheduler/view/TimelineBase#typedef-VisibleDate)
Options accepted by the Scheduler's [visibleDate](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-visibleDate) property.
