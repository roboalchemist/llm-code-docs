# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/mixin/GridElementEvents.md

# [GridElementEvents](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents)

Mixin for Grid that handles dom events. Some listeners fire own events but all can be chained by features. None of the functions in this class are indented to be called directly.

See [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) for more information on grid keyboard interaction.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[longPressTime](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#config-longPressTime)
Time in ms until a longpress is triggered

[enableUndoRedoKeys](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#config-enableUndoRedoKeys)
Set to `true` to listen for CTRL-Z (CMD-Z on Mac OS) keyboard event and trigger undo (redo when SHIFT is pressed). Only applicable when using a [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager).

[hoverCls](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#config-hoverCls)
A CSS class to add to hovered row elements

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridElementEvents](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#property-isGridElementEvents)
Identifies an object as an instance of [GridElementEvents](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridElementEvents) class, or subclass thereof.

[isGridElementEvents](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#property-isGridElementEvents-static)
Identifies an object as an instance of [GridElementEvents](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridElementEvents) class, or subclass thereof.

[hoveredCell](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#property-hoveredCell)
The currently hovered grid cell

[longPressTime](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#property-longPressTime)
Time in ms until a longpress is triggered

[enableUndoRedoKeys](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#property-enableUndoRedoKeys)
Set to `true` to listen for CTRL-Z (CMD-Z on Mac OS) keyboard event and trigger undo (redo when SHIFT is pressed). Only applicable when using a [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager).

## Functions

Functions are methods available for calling on the class

[initInternalEvents](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-initInternalEvents)
Init listeners for a bunch of dom events. All events are handled by handleEvent().

[getCellDataFromEvent](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-getCellDataFromEvent)
This method finds the cell location of the passed event. It returns an object describing the cell.

[getCellDataFromElement](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-getCellDataFromElement)
This method finds the cell location of the passed element. It returns an object describing the cell.

[getHeaderDataFromEvent](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-getHeaderDataFromEvent)
This method finds the header location of the passed event. It returns an object describing the header.

[handleEvent](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-handleEvent)
Handles all dom events, routing them to correct functions (touchstart -> onElementTouchStart)

[onElementTouchStart](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementTouchStart)
Touch start, chain this function in features to handle the event.

[onElementTouchMove](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementTouchMove)
Touch move, chain this function in features to handle the event.

[onElementTouchEnd](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementTouchEnd)
Touch end, chain this function in features to handle the event.

[onElementMouseDown](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementMouseDown)
Mouse down, chain this function in features to handle the event.

[onElementMouseMove](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementMouseMove)
Mouse move, chain this function in features to handle the event.

[onElementMouseUp](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementMouseUp)
Mouse up, chain this function in features to handle the event.

[onElementPointerUp](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementPointerUp)
Pointer up, chain this function in features to handle the event.

[onHandleElementClick](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onHandleElementClick)
Called before [onElementClick](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridElementEvents#function-onElementClick). Fires 'beforeElementClick' event which can return false to cancel further onElementClick actions.

[onElementClick](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementClick)
Click, select cell on click and also fire 'cellClick' event. Chain this function in features to handle the dom event.

[onElementDblClick](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementDblClick)
Double click, fires 'cellDblClick' event. Chain this function in features to handle the dom event.

[onElementMouseOver](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementMouseOver)
Mouse over, adds 'hover' class to elements.

[onElementMouseOut](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementMouseOut)
Mouse out, removes 'hover' class from elements.

[onElementKeyDown](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementKeyDown)
To catch all keydowns. For more specific keydown actions, use keyMap.

[onElementKeyPress](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementKeyPress)
Key press, chain this function in features to handle the dom event.

[onElementKeyUp](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementKeyUp)
Key up, chain this function in features to handle the dom event.

[onElementContextMenu](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onElementContextMenu)
Context menu, chain this function in features to handle the dom event. In most cases, include ContextMenu feature instead.

[onInternalResize](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#function-onInternalResize)
Overrides empty base function in View, called when view is resized.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[cellClick](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-cellClick)
Fired when user clicks in a grid cell

[cellDblClick](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-cellDblClick)
Fired when user double clicks a grid cell

[cellContextMenu](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-cellContextMenu)
Fired when user activates contextmenu in a grid cell

[cellMouseOver](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-cellMouseOver)
Fired when user moves the mouse over a grid cell

[cellMouseOut](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-cellMouseOut)
Fired when a user moves the mouse out of a grid cell

[rowMouseEnter](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-rowMouseEnter)
Fired when the mouse enters a row

[rowMouseLeave](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-rowMouseLeave)
Fired when the mouse leaves a row

[cellMouseEnter](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-cellMouseEnter)
Fired when the mouse enters a cell

[cellMouseLeave](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-cellMouseLeave)
Fired when the mouse leaves a cell

[headerClick](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-headerClick)
Fired when a grid header is clicked on.

Returning `false` from a handler prevents any features (such as [Sort](https://bryntum.com/docs/gantt/api/#Grid/feature/Sort)) from recieving and processing the click event.

[mouseOver](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-mouseOver)
Mouse moved in over element in grid

[mouseOut](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridElementEvents#event-mouseOut)
Mouse moved out from element in grid
