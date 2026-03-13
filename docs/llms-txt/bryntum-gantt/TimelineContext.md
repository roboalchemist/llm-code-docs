# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/util/TimelineContext.md

# [TimelineContext](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext)

This class encapsulates a schedule timeline tick context based on a DOM event. This will include the row and resource information and the tick and time information for a DOM pointer event detected in the timeline.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[tick](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-tick)
A [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) record which encapsulates the contextual tick

[tickIndex](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-tickIndex)
The contextual tick index. This may be fractional.

[tickStartDate](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-tickStartDate)
The start date of the contextual tick.

[tickEndDate](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-tickEndDate)
The end date of the contextual tick.

[row](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-row)
The contextual [row](https://bryntum.com/docs/gantt/api/#Grid/row/Row)

[record](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-record)
The contextual record

[eventRecord](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-eventRecord)
The contextual event record (if any)

[assignmentRecord](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-assignmentRecord)
The contextual assignment record (if any)

[resourceRecord](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-resourceRecord)
The contextual resource record (if any)

[scheduler](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-scheduler)
The owning scheduler/gantt widget.

[domEvent](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-domEvent)
The DOM event which triggered the context change.

[eventElement](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-eventElement)
If the `domEvent` was on an event bar, this will be the event bar element.

[cellElement](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-cellElement)
The cell element under the `domEvent`

[date](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-date)
The date corresponding to the `domEvent` position in the timeline floored to the [TimeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis) resolution and resolutionIncrement

[time](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-time)
The date corresponding as close as can be determined to the `domEvent` position in the timeline

[rowIndex](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-rowIndex)
The contextual row index

[index](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#config-index)
The contextual row index. An alias for [rowIndex](https://bryntum.com/docs/gantt/api/#Scheduler/util/TimelineContext#property-rowIndex).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[tick](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-tick)
A [TimeSpan](https://bryntum.com/docs/gantt/api/#Scheduler/model/TimeSpan) record which encapsulates the contextual tick

[tickIndex](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-tickIndex)
The contextual tick index. This may be fractional.

[tickParentIndex](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-tickParentIndex)
The integer contextual tick index.

[tickStartDate](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-tickStartDate)
The start date of the contextual tick.

[tickEndDate](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-tickEndDate)
The end date of the contextual tick.

[row](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-row)
The contextual [row](https://bryntum.com/docs/gantt/api/#Grid/row/Row)

[record](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-record)
The contextual record

[eventRecord](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-eventRecord)
The contextual event record (if any)

[assignmentRecord](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-assignmentRecord)
The contextual assignment record (if any)

[resourceRecord](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-resourceRecord)
The contextual resource record (if any)

[scheduler](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-scheduler)
The owning scheduler/gantt widget.

[domEvent](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-domEvent)
The DOM event which triggered the context change.

[eventElement](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-eventElement)
If the `domEvent` was on an event bar, this will be the event bar element.

[cellElement](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-cellElement)
The cell element under the `domEvent`

[date](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-date)
The date corresponding to the `domEvent` position in the timeline floored to the [TimeAxis](https://bryntum.com/docs/gantt/api/#Scheduler/data/TimeAxis) resolution and resolutionIncrement

[time](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-time)
The date corresponding as close as can be determined to the `domEvent` position in the timeline

[rowIndex](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-rowIndex)
The contextual row index

[index](https://bryntum.com/docs/gantt/api/Scheduler/util/TimelineContext#property-index)
The contextual row index. An alias for [rowIndex](https://bryntum.com/docs/gantt/api/#Scheduler/util/TimelineContext#property-rowIndex).
