# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Droppable.md

# [Droppable](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable)

Mix this into another class to enable drop support and receive drops from [draggables](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable).

There are 4 basic methods that a droppable implements. These methods are called as drag operations occur:

```
 class MyDroppable extends Base.mixin(Droppable) {
     dragEnter(drag) {
         // a drag has entered the drop zone... create some type of drop indicator perhaps
     }

     dragMove(drag) {
         // a drag has changed position... update drop indicators
     }

     dragDrop(drag) {
         // drop has occurred... process data from the drag context
     }

     dragLeave(drag) {
         // the drag has left the drop zone... cleanup indicators
     }
 }
```

Instances of `Droppable` are associated with an element to receive drag operations:

```
 let target = new MyDroppable({
     dropRootElement : someElement
 });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[droppableSelector](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#config-droppableSelector)
A selector, which, if specified, narrows the dropability to child elements of the [dropRootElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#config-dropRootElement) which match this selector.

[dropRootElement](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#config-dropRootElement)
Set this config to the element where drops should be received. When set, the `b-droppable` CSS class is added to the element and the `Droppable` instance is associated with that element so that it can be found by [draggables](https://bryntum.com/docs/gantt/api/#Core/mixin/Draggable).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDroppable](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#property-isDroppable)
Identifies an object as an instance of [Droppable](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable) class, or subclass thereof.

[isDroppable](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#property-isDroppable-static)
Identifies an object as an instance of [Droppable](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable) class, or subclass thereof.

[dropping](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#property-dropping)
The current `DragContext`. This is set when a drag enters this target. Changing this config causes the [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragEnter) and [dragLeave](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragLeave) methods to be called. If `dragEnter` returns `false` for a drag, this value will be set to `null`.

[dropEventer](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#property-dropEventer)
Return the `Events` instance from which drop events are fired.

[droppableCls](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#property-droppableCls)
Returns the CSS class that is added to the [dropRootElement](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#config-dropRootElement), i.e., `'b-droppable'`.

## Functions

Functions are methods available for calling on the class

[dragEnter](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#function-dragEnter)
This method is called when a drag enters this droppable's `dropRootElement`. In many cases, this method is used to create some sort of drop indicator to provide user feedback.

If this method does not return `false`, the [dropping](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#property-dropping) config will retain the given `drag` context which was set prior to this method being called.

If this method returns `false`, the drop will not be accepted. Neither [dragDrop](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragDrop) nor [dragLeave](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragLeave) will be called for this drop. If the drag leaves this target and re-enters, this method will be called again. While `dropping` will already be updated before this method is called, it will be reset to `null` in this case.

The base class implementation of this method fires the [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#event-dragEnter) event.

[dragMove](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#function-dragMove)
This method is called when the drag that was previously announced via [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragEnter) moves to a new position. This is typically where drop indicators are updated to reflect the new position.

The base class implementation of this method fires the [dragMove](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#event-dragMove) event.

[dragDrop](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#function-dragDrop)
This method is called when the drag that was previously announced via [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragEnter) has ended with a drop. In addition to any cleanup (since [dragLeave](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragLeave) will not be called), this method handles any updates associated with the data from the drag context and the position of the drop.

The base class implementation of this method fires the [drop](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#event-drop) event.

[dragLeave](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#function-dragLeave)
This method is called when the drag that was previously announced via [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragEnter) leaves this droppable's `dropRootElement`, or the drag is [aborted](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#property-aborted) by the user pressing the `ESC` key, or the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method is called.

This is the time to cleanup anything created by `dragEnter`.

The base class implementation of this method fires the [dragLeave](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#event-dragLeave) event.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dragEnter](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#event-dragEnter)
This event is fired when a drag enters this droppable's `dropRootElement`. It is fired by the droppable's [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragEnter) method.

[dragMove](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#event-dragMove)
This event is fired when the drag that was previously announced via [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#event-dragEnter) moves to a new position. It is fired by the droppable's [dragMove](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragMove) method.

[drop](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#event-drop)
This event is fired when the drag that was previously announced via [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#event-dragEnter) has ended with a drop. It is fired by the droppable's [dragDrop](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragDrop) method.

This event is **not** fired when a drag gesture is aborted by the user pressing the `ESC` key or if the [abort](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragContext#function-abort) method is called.

[dragLeave](https://bryntum.com/docs/gantt/api/Core/mixin/Droppable#event-dragLeave)
This event is fired when the drag that was previously announced via [dragEnter](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#event-dragEnter) leaves this droppable's `dropRootElement`. It is fired by the droppable's [dragLeave](https://bryntum.com/docs/gantt/api/#Core/mixin/Droppable#function-dragLeave) method.
