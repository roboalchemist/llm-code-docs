# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/feature/EventResize.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/EventResize.md

# [EventResize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize)

Feature that allows resizing an event by dragging its end.

By default, it displays a tooltip with the new start and end dates, formatted using [displayDateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/TimelineViewPresets#config-displayDateFormat).

Customizing the resize tooltip
------------------------------

To show custom HTML in the tooltip, please see the [tooltipTemplate](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventResize#config-tooltipTemplate) config. Example:

```
eventResize : {
    // A minimal end date tooltip
    tooltipTemplate : ({ record, endDate }) => {
        return DateHelper.format(endDate, 'MMM D');
    }
}
```

This feature is **enabled** by default

This feature is extended with a few overrides by the Gantt's `TaskResize` feature.

This feature updates the event's `startDate` or `endDate` live in order to leverage the rendering pathway to always yield a correct appearance. The changes are done in [batched](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-beginBatch) mode so that changes do not become eligible for data synchronization or propagation until the operation is completed.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[leftHandle](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-leftHandle)
Use left handle when resizing. Only applies when owning client's `direction` is 'horizontal'

[rightHandle](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-rightHandle)
Use right handle when resizing. Only applies when owning client's `direction` is 'horizontal'

[topHandle](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-topHandle)
Use top handle when resizing. Only applies when owning client's direction\` is 'vertical'

[bottomHandle](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-bottomHandle)
Use bottom handle when resizing. Only applies when owning client's `direction` is 'vertical'

[dynamicHandleSize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-dynamicHandleSize)
Automatically shrink virtual handles when available space < handleSize. The virtual handles will decrease towards width/height 1, reserving space between opposite handles to for example leave room for dragging. To configure reserved space, see [reservedSpace](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventResize#config-reservedSpace).

[allowResizeToZero](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-allowResizeToZero)
Set to `true` to allow resizing to a zero-duration span

[reservedSpace](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-reservedSpace)
Room in px to leave unoccupied by handles when shrinking them dynamically (see [dynamicHandleSize](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventResize#config-dynamicHandleSize)).

[dragThreshold](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-dragThreshold)
The amount of pixels to move pointer/mouse before it counts as a drag operation.

[dragTouchStartDelay](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-dragTouchStartDelay)
The amount of time (ms) to delay a touch-resize interaction.

[showTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-showTooltip)
`false` to not show a tooltip while resizing

[showExactResizePosition](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-showExactResizePosition)
true to see exact event length during resizing

[validatorFn](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-validatorFn)
An empty function by default, but provided so that you can perform custom validation on the item being resized. Return true if the new duration is valid, false to signal that it is not.

[validatorFnThisObj](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-validatorFnThisObj)
`this` reference for the validatorFn

[tip](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-tip)
If a tooltip is required to illustrate the resize, specify this as `true`, or a config object for the [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip).

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-tooltipTemplate)
A template function returning the content to show during a resize operation.

[lockLayout](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-lockLayout)
Locks the layout during drag resize, opt out to use the same rendering pathway for drag resize as for already existing events (updating the layout of all events during the resize operation).

Keeping this config enabled also leads to cheaper resizing, only the resized event's resources are refreshed during the operation.

For even cheaper resizing, configure it as `'minimal-updates'`. In this mode, only the resized event is refreshed during the operation (not the other events assigned to the same resource).

[resizeSelected](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#config-resizeSelected)
Set to `false` to not resize all selected events simultaneously.

Please note that [multiEventSelect](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler#config-multiEventSelect) needs to be enabled for it to work

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isEventResize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#property-isEventResize)
Identifies an object as an instance of [EventResize](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventResize) class, or subclass thereof.

[isEventResize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#property-isEventResize-static)
Identifies an object as an instance of [EventResize](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventResize) class, or subclass thereof.

[tip](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#property-tip)
Setting this property may change the configuration of the [tip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/EventResize#config-tip), or cause it to be destroyed if `null` is passed.

Reading this property returns the Tooltip instance.

[isResizing](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#property-isResizing)
Returns true if a resize operation is active

[isMultiResizing](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#property-isMultiResizing)
Returns true if resizing multiple events

## Functions

Functions are methods available for calling on the class

[hasValidSize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#function-hasValidSize)
Validates that the resized event has a valid size based on configuration. Returns true if zero-size events are allowed or if snapping is enabled. Otherwise checks that the event duration is non-zero.

[checkResizeHandles](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#function-checkResizeHandles)
Check if mouse is over a resize handle (virtual). If so, highlight.

[highlightHandle](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#function-highlightHandle)
Highlights handles (applies css that changes cursor).

[unHighlightHandle](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#function-unHighlightHandle)
Unhighlight handles (removes css).

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeEventResize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#event-beforeEventResize)
Fired on the owning Scheduler before resizing starts. Return `false` to prevent the action.

[eventResizeStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#event-eventResizeStart)
Fires on the owning Scheduler when event resizing starts

[eventPartialResize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#event-eventPartialResize)
Fires on the owning Scheduler on each resize move event

[beforeEventResizeFinalize](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#event-beforeEventResizeFinalize)
Fired on the owning Scheduler to allow implementer to prevent immediate finalization by returning a promise in the listener, to show a confirmation popup etc

```
 scheduler.on('beforeeventresizefinalize', event => {
     event.async = true;
     setTimeout(() => {
         // async code don't forget to call finalize
         event.finalize();
     }, 1000);
 })
```

[eventResizeEnd](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#event-eventResizeEnd)
Fires on the owning Scheduler after the resizing gesture has finished.

## Typedefs

Typedefs are type definitions for the class

[EventResizeData](https://bryntum.com/docs/gantt/api/Scheduler/feature/EventResize#typedef-EventResizeData)
An object containing data related to event resize.
