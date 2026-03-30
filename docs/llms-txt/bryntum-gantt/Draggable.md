# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Draggable.md

# [Draggable](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable)

Mix this into another class to enable drag/drop support.

To use a draggable, it must be associated with an element that contains draggable content:

```
 let draggable = new MyDraggable({
     dragRootElement : someElement
 });
```

Once the `dragRootElement` is assigned, any element inside that root is a candidate for dragging. To limit the allowed element, set the [dragSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragSelector) config.

```
 let draggable = new MyDraggable({
     dragRootElement : someElement,
     dragSelector    : '.drag-this'
 });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[draggingClsSelector](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-draggingClsSelector)
A CSS selector to use to ascend from the [dragRootElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragRootElement) to find the element that will gain the [draggingCls](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#property-draggingCls) and [draggingStartedCls](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#property-draggingStartedCls) CSS classes.

[dragDocumentListeners](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragDocumentListeners)
The listeners to add to the `document` during a drag.

[dragItemSelector](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragItemSelector)
A CSS selector to use to ascend from the drag element to find the element that will gain the [draggingItemCls](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#property-draggingItemCls) CSS class. If not supplied, the drag element will gain this CSS class.

[dragItemOverCls](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragItemOverCls)
A CSS class to add to items identified by the [dragItemSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragItemSelector) when the mouse enters.

[onDragItemMouseEnter](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-onDragItemMouseEnter)
A function to call when the pointer enters a [dragItemSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragItemSelector).

[onDragItemMouseMove](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-onDragItemMouseMove)
A function to call when the pointer moves inside a [dragItemSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragItemSelector).

[onDragItemMouseLeave](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-onDragItemMouseLeave)
A function to call when the pointer leaves a [dragItemSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragItemSelector).

[dragLock](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragLock)
Configure as `'x'` to lock dragging to the `X` axis (the drag will only move horizontally) or `'y'` to lock dragging to the `Y` axis (the drag will only move vertically).

[dragMinDistance](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragMinDistance)
The minimum distance a drag must move to be considered a drop and not [aborted](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-aborted).

[dragProxy](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragProxy)
The [drag proxy](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy) is a helper object that can be used to display feedback during a drag.

[dragRootElement](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragRootElement)
The outer element where dragging will operate (attach events to it and use as root limit when looking for ancestors).

[dragSameTargetDrop](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragSameTargetDrop)
Set to `true` to allow a drag to drop on to the same element from which the drag started.

[dragSelector](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragSelector)
A CSS selector used to determine which element(s) can be dragged.

[ignoreSelector](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-ignoreSelector)
A CSS selector used to identify child element(s) that should not trigger drag.

[dragSwallowClickTime](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragSwallowClickTime)
The number of milliseconds after a pointerup to ignore click events on the document. This is used to avoid the "up" event itself generating a `click` on the target.

[dragThreshold](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragThreshold)
The amount of pixels to move pointer/mouse before it counts as a drag operation.

[dragTouchStartDelay](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dragTouchStartDelay)
The number of milliseconds that must elapse after a `touchstart` event before it is considered a drag. If movement occurs before this time, the drag is aborted. This is to allow touch swipes and scroll gestures.

[dropTargetSelector](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#config-dropTargetSelector)
The CSS selector to use to identify the closest valid target from the event target.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDraggable](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-isDraggable)
Identifies an object as an instance of [Draggable](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable) class, or subclass thereof.

[isDraggable](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-isDraggable-static)
Identifies an object as an instance of [Draggable](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable) class, or subclass thereof.

[dragging](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-dragging)
The current `DragContext`. This is created immediately on pointerdown but does not become active until some movement occurs. This [threshold](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragThreshold) is configurable.

[overItem](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-overItem)
The [dragSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragSelector) item the mouse is currently over.

[draggingCls](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-draggingCls)
The CSS class to add to the [dragRootElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragRootElement) (or [draggingClsSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-draggingClsSelector) from there) as soon as the pointerdown event occurs.

[draggingBodyCls](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-draggingBodyCls)
The CSS class to add to the `body` element as soon as the [dragThreshold](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragThreshold) is reached and an actual drag is in progress.

[draggingItemCls](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-draggingItemCls)
The CSS class to add to the element being dragged as soon as the pointerdown event occurs.

[draggingStartedCls](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-draggingStartedCls)
The CSS class to add to the [dragRootElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragRootElement) (or [draggingClsSelector](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-draggingClsSelector) from there) as soon as the [dragThreshold](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragThreshold) is reached and an actual drag is in progress.

[draggableCls](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-draggableCls)
The CSS class that is added to the [dragRootElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragRootElement), i.e., `'b-draggable'`.

[dragEventer](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#property-dragEventer)
Return the `Events` instance from which drag events are fired.

## Functions

Functions are methods available for calling on the class

[beforeDrag](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-beforeDrag)
This template method is called when the mousedown of a potential drag operation occurs. This happens before the gesture is known to be a drag, meaning the [dragThreshold](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragThreshold) has not been reached. This method should initialize the [DragContext](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext) using the [set](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-set) method. Alternatively, this method may return `false` to prevent the drag operation.

_Important:_ Because no drag has occurred at the time this method is called, only minimal processing should be done (such as initializing the [DragContext](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext)). Anything more should be done in the [dragStart](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#function-dragStart) method or in response to the [dragStart](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#event-dragStart) event which happen only if the user drags the mouse before releasing the mouse button.

[dragStart](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-dragStart)
This template method is called when the drag operation starts. This occurs when the [dragThreshold](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragThreshold) has been reached. Your implementation may return `false` to prevent the startup of the drag operation.

[dragOver](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-dragOver)
This template method is called as the drag moves. This occurs on each mouse/pointer/touchmove event.

[dragEnterTarget](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-dragEnterTarget)
This template method is called when the drag enters a [target](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable).

[dragLeaveTarget](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-dragLeaveTarget)
This template method is called when the drag leaves a [target](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable).

[dragDrop](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-dragDrop)
This template method is called when the drag operation completes. This occurs on the pointerup event.

This method is not called if the drag is [aborted](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-aborted).

[dragEnd](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-dragEnd)
This template method is called when the drag operation completes. This occurs on the pointerup event or perhaps a keypress event.

This method is always called, even if the drag is [aborted](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-aborted).

[onDragMouseDown](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-onDragMouseDown)
Grab draggable element on mouse down.

[onDragPointerDown](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-onDragPointerDown)
Grab draggable element on pointerdown.

[onDragTouchStart](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#function-onDragTouchStart)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dragCancel](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#event-dragCancel)
This event is fired when a drag gesture is completed due to the user aborting it (with the `ESC` key) or if the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method was called.

[drop](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#event-drop)
This event is fired when a drag gesture is completed successfully.

This event is **not** fired if the drag was aborted by the user pressing the `ESC` key or if the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method was called.

[drag](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#event-drag)
This event is fired as a drag gesture progresses due to cursor movement.

[beforeDragStart](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#event-beforeDragStart)
This event is fired prior to starting a drag gesture. This does not occur immediately after the user performs the pointer/mousedown/touchstart but only after the [dragThreshold](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragThreshold) amount of movement has taken place.

The drag is canceled if a listener returns `false`.

[dragStart](https://bryntum.com/docs/gantt/api/Core/mixin/Draggable#event-dragStart)
This event is fired when a drag gesture has started. This does not occur immediately after the user performs the pointer/mousedown/touchstart but only after the [dragThreshold](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable#config-dragThreshold) amount of movement has taken place.
