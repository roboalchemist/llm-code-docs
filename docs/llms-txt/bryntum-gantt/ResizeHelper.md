# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/ResizeHelper.md

# [ResizeHelper](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper)

Handles resizing of elements using handles. Handles can be actual elements or virtual handles specified as a border area on elements left and right edges.

```
// enable resizing all elements with class 'resizable'
let resizer = new ResizeHelper({
  targetSelector: '.resizable'
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resizingCls](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-resizingCls)
CSS class added when resizing

[dragThreshold](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-dragThreshold)
The amount of pixels to move mouse before it counts as a drag operation

[handleSize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-handleSize)
Resizing handle size

[dynamicHandleSize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-dynamicHandleSize)
Automatically shrink virtual handles when available space < handleSize. The virtual handles will decrease towards width/height 1, reserving space between opposite handles to for example leave room for dragging. To configure reserved space, see [reservedSpace](https://bryntum.com/docs/gantt/api/#Core/helper/ResizeHelper#config-reservedSpace).

[reservedSpace](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-reservedSpace)
Room in px to leave unoccupied by handles when shrinking them dynamically (see [dynamicHandleSize](https://bryntum.com/docs/gantt/api/#Core/helper/ResizeHelper#config-dynamicHandleSize)).

[touchHandleSize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-touchHandleSize)
Resizing handle size on touch devices

[minWidth](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-minWidth)
Minimum width when resizing

[maxWidth](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-maxWidth)
Max width when resizing.

[minHeight](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-minHeight)
Minimum height when resizing

[maxHeight](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-maxHeight)
Max height when resizing

[scroller](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-scroller)
Optional scroller used to read scroll position. If unspecified, the outer element will be used.

[allowResize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-allowResize)
Assign a function to determine if a hovered element can be resized or not. Return `true` to allow resizing or `false` to prevent.

[dragWithin](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-dragWithin)
Outer element that limits where element can be dragged

[isElementResizable](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-isElementResizable)
A function that determines if dragging an element is allowed. Gets called with the element as argument, return `true` to allow dragging or `false` to prevent.

[targetSelector](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-targetSelector)
A CSS selector used to determine if resizing an element is allowed.

[leftHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-leftHandle)
Use left handle when resizing. Only applies when `direction` is 'horizontal'

[rightHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-rightHandle)
Use right handle when resizing. Only applies when `direction` is 'horizontal'

[topHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-topHandle)
Use top handle when resizing. Only applies when `direction` is 'vertical'

[bottomHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-bottomHandle)
Use bottom handle when resizing. Only applies when `direction` is 'vertical'

[handleSelector](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-handleSelector)
A CSS selector used to determine where handles should be "displayed" when resizing. Defaults to targetSelector if unspecified

[handleContainerSelector](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-handleContainerSelector)
A CSS selector used to determine which inner element contains handles.

[invalidCls](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-invalidCls)
CSS class added when the resize state is invalid

[direction](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#config-direction)
Direction to resize in, either 'horizontal' or 'vertical'

## Functions

Functions are methods available for calling on the class

[initResize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-initResize)
Initializes resizing

[initListeners](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-initListeners)
Initialize listeners

[onMouseDown](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-onMouseDown)
Grab draggable element on mouse down.

[onMouseMove](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-onMouseMove)
Move grabbed element with mouse.

[onMouseUp](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-onMouseUp)
Drop on mouse up (if dropped on valid target).

[onDocumentClick](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-onDocumentClick)
This is a capture listener, only added during drag, which prevents a click gesture propagating from the terminating mouseup gesture

[onKeyDown](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-onKeyDown)
Cancel on ESC key

[update](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-update)
Updates resize, called when an element is grabbed and mouse moves

[abort](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-abort)
Abort dragging

[grabResizeHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-grabResizeHandle)
Starts resizing, updates ResizeHelper#context with relevant info.

[checkResizeHandles](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-checkResizeHandles)
Check if mouse is over a resize handle (virtual). If so, highlight.

[updateResize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-updateResize)
Updates size of target (on mouse move).

[finishResize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-finishResize)
Finalizes resize, fires drop.

[abortResize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-abortResize)
Abort resizing

[highlightHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-highlightHandle)
Highlights handles (applies css that changes cursor).

[unHighlightHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-unHighlightHandle)
Unhighlight handles (removes css).

[overLeftHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-overLeftHandle)
Check if over left handle (virtual).

[overRightHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-overRightHandle)
Check if over right handle (virtual).

[overTopHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-overTopHandle)
Check if over top handle (virtual).

[overBottomHandle](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#function-overBottomHandle)
Check if over bottom handle (virtual).

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[resizing](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#event-resizing)
Fired while dragging

[resizeStart](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#event-resizeStart)
Fired when dragging starts.

[resize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#event-resize)
Fires after resize, and allows for asynchronous finalization by setting 'async' to `true` on the context object.

[cancel](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#event-cancel)
Fires when a resize is canceled (width & height are reverted)

## Typedefs

Typedefs are type definitions for the class

[ResizeContext](https://bryntum.com/docs/gantt/api/Core/helper/ResizeHelper#typedef-ResizeContext)
Contextual information available during a resize.
