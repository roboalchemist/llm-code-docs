# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/drag/DragContext.md

# [DragContext](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext)

This class is created during drag operations of [Draggable](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable). It holds the state of an ongoing drag operation.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[itemElement](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#config-itemElement)
The element that will have the [draggingItemCls](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#property-draggingItemCls). This element is determined by the [dragItemSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragItemSelector).

[scrollManager](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#config-scrollManager)
The `ScrollManager` instance to use for scrolling while dragging.

[monitoringConfig](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#config-monitoringConfig)
Config for `startMonitoring` call.

[source](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#config-source)
The source of the drag operation.

[threshold](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#config-threshold)
The minimum distance from the touchstart/mousedown/pointerdown that must be moved to actually start a drag operation.

[touchStartDelay](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#config-touchStartDelay)
The minimum amount of time a touch must be maintained before it will initiate a drag. Movement prior to this time will cancel the drag in order to allow touch scrolling.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDragContext](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-isDragContext)
Identifies an object as an instance of [DragContext](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext) class, or subclass thereof.

[isDragContext](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-isDragContext-static)
Identifies an object as an instance of [DragContext](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext) class, or subclass thereof.

[target](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-target)
The current target of the drag.

[targetElement](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-targetElement)
The current target element of the drag.

[event](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-event)
The current DOM event being processed.

[altKey](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-altKey)
This property holds the `altKey` state of the most recent event.

[cleaners](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-cleaners)
An array of functions to call when cleaning up the context instance.

[ctrlKey](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-ctrlKey)
This property holds the `ctrlKey` state of the most recent event.

[data](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-data)
Container for data associated with the drag. Data items are added by the [Draggable](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable) when the drag starts.

[element](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-element)
The element from which the drag operation started.

[endEvent](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-endEvent)
The event that completed the drag (a `mouseup`, `pointerup` or `touchend`).

[lastMoveEvent](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-lastMoveEvent)
The most recent `mousemove`, `pointermove` or `touchmove` event.

[metaKey](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-metaKey)
This property holds the `metaKey` state of the most recent event.

[previousTarget](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-previousTarget)
The previous [target](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-target) of the drag.

[scrollerAction](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-scrollerAction)
The scroll actions reported by the [scrollManager](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#config-scrollManager).

[shiftKey](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-shiftKey)
This property holds the `shiftKey` state of the most recent event.

[state](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-state)
This property holds the current state of the drag process.

This will be one of the following values:

* `DragContext.STATE.INIT` - The button is down but there is insufficient movement to start the drag.
* `DragContext.STATE.DRAGGING` - The button is down and movement has started the drag.
* `DragContext.STATE.DROPPED` - The button has been released and drop has occurred.
* `DragContext.STATE.ABORTED` - The drag has been aborted (this happens if the user presses the `ESC` key or if the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method is called).

[startEvent](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-startEvent)
The event that started the drag operation.

[touchStartTimer](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-touchStartTimer)
The timer that fires when a touch pointermove is allowed to start the drag. A touch pointermove event prior to this will `abort()` the drag to allow touch scrolling.

[_valid](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-_valid)
Stores the value from writes to the [valid](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-valid) property.

[aborted](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-aborted)
This property is `true` if the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method was called and `false` otherwise. This is typically because the user pressed the ESC key, however, a drag can be aborted for other reasons.

[completed](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-completed)
Returns `true` if the drag has completed either by mouse/pointerup or the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method.

[pending](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-pending)
This property is `true` if the drag [threshold](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#config-threshold) has not yet been reached.

[started](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-started)
This property is `true` if the drag [threshold](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#config-threshold) has been reached and the drag operation is active.

[valid](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#property-valid)
This property is `true` when the drag is in a valid drop state. This can be set to `false` to indicate the drop is invalid. Setting to `true` does not ensure that the property will be `true` when next read due to other factors that are required to make the drop valid. For example, setting `valid = true` will still return `false` if called before the drag [threshold](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#config-threshold) has not been reached or if the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method has been called.

## Functions

Functions are methods available for calling on the class

[get](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#function-get)
Retrieves a data item from the drag source. This method can only be called after the drag has completed.

[has](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#function-has)
Returns `true` if the named data item is present.

[peek](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#function-peek)
Retrieves a data item from the drag source if it is available. This will return `true` for an item that was [set](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-set) using a renderer function.

[set](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#function-set)
Sets a data item for the drag. If a function is passed, it is called to render the data only if that data is actually requested via the [get](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-get) method. A data renderer function can be `async`.

[abort](https://bryntum.com/docs/gantt/api/Core/util/drag/DragContext#function-abort)
Aborts the drag. After calling this method, [aborted](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-aborted) will be `true`, [valid](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-valid) will be `false` and [completed](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-completed) will be `true`.
