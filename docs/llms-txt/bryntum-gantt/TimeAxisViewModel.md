# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/model/TimeAxisViewModel.md

# [TimeAxisViewModel](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel)

This class is an internal view model class, describing the visual representation of a [TimeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis). The config for the header rows is described in the [headers](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset#field-headers). To calculate the size of each cell in the time axis, this class requires:

* availableSpace - The total width or height available for the rendering
* tickSize - The fixed width or height of each cell in the lowest header row. This value is normally read from the [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) but this can also be updated programmatically using the [tickSize](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#property-tickSize) setter

Normally you should not interact with this class directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[timeAxis](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#config-timeAxis)
The time axis providing the underlying data to be visualized

[forceFit](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#config-forceFit)
`true` if cells in the bottom-most row should be fitted to the [available space](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#property-availableSpace).

[snap](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#config-snap)
`true` if there is a requirement to be able to snap events to a certain view resolution. This has implications of the [tickSize](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#config-tickSize) that can be used, since all widths must be in even pixels.

[availableSpace](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#config-availableSpace)
The available width/height, this is normally not known by the consuming UI component using this model class until it has been fully rendered. The consumer of this model should set [availableSpace](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#property-availableSpace) when its width has changed.

[tickSize](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#config-tickSize)
The "tick width" for horizontal mode or "tick height" for vertical mode, to use for the cells in the bottom most header row. This value is normally read from the [viewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTimeAxisViewModel](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-isTimeAxisViewModel)
Identifies an object as an instance of [TimeAxisViewModel](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel) class, or subclass thereof.

[isTimeAxisViewModel](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-isTimeAxisViewModel-static)
Identifies an object as an instance of [TimeAxisViewModel](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel) class, or subclass thereof.

[columnConfig](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-columnConfig)
Returns an array representing the headers of the current timeAxis. Each element is an array representing the cells for that level in the header.

[isHorizontal](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-isHorizontal)
Using horizontal mode?

[isVertical](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-isVertical)
Using vertical mode?

[forceFit](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-forceFit)
Gets/sets the forceFit value for the model. Setting it will cause it to update its contents and fire the [update](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#event-update) event.

[snapPixelAmount](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-snapPixelAmount)
Returns the pixel increment for the current view resolution.

[isStretchingTicks](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-isStretchingTicks)
Returns `true` if the ticks are currently being stretched to fit the available space.

[tickSize](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-tickSize)
Get/set the current time column size (the width or height of a cell in the bottom-most time axis header row, depending on mode)

[totalSize](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-totalSize)
Returns the total width/height of the time axis representation, depending on mode.

[availableSpace](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-availableSpace)
Get/set the available space for the time axis representation. If size changes it will cause it to update its contents and fire the [update](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#event-update) event.

[snap](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-snap)
Gets/sets the snap value for the model. Setting it will cause it to update its contents and fire the [update](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#event-update) event.

[majorHeaderLevel](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#property-majorHeaderLevel)
This method is meant to return the level of the header which 2nd lowest. It is used for [isMajorTick](https://bryntum.com/docs/gantt/api/#Scheduler/view/model/TimeAxisViewModel#function-isMajorTick) method

## Functions

Functions are methods available for calling on the class

[update](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-update)
Updates the view model current timeAxis configuration and available space.

[getDistanceBetweenDates](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-getDistanceBetweenDates)
Returns the distance in pixels for a timespan with the given start and end date.

[getDistanceForDuration](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-getDistanceForDuration)
Returns the distance in pixels for a time span

[getPositionFromDate](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-getPositionFromDate)
Gets the position of a date on the projected time axis or -1 if the date is not in the timeAxis.

[getDateFromPosition](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-getDateFromPosition)
Gets the date for a position on the time axis

[getSingleUnitInPixels](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-getSingleUnitInPixels)
Returns the amount of pixels for a single unit

[getDates](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-getDates)
Returns start dates for ticks at the specified level in format { date, isMajor }.

[fitToAvailableSpace](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-fitToAvailableSpace)
This function fits the time columns into the available space in the time axis column.

[isMajorTick](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-isMajorTick)
For vertical view (and column lines plugin) we sometimes want to know if current tick starts along with the upper header level.

[forEachInterval](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-forEachInterval)
Calls the supplied iterator function once per interval. The function will be called with three parameters, start date and end date and an index. Return false to break the iteration.

[forEachMainInterval](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#function-forEachMainInterval)
Calls the supplied iterator function once per interval. The function will be called with three parameters, start date and end date and an index. Return false to break the iteration.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[update](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#event-update)
Fires after the model has been updated.

[reconfigure](https://bryntum.com/docs/gantt/api/Scheduler/view/model/TimeAxisViewModel#event-reconfigure)
Fires after the model has been reconfigured.
