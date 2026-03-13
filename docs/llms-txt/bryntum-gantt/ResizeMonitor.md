# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/ResizeMonitor.md

# [ResizeMonitor](https://bryntum.com/docs/gantt/api/Core/helper/ResizeMonitor)

Allows size monitoring of elements (or optionally a Window instance).

```
ResizeMonitor.addResizeListener(
  myElement,
  element => {
     console.log(element, ' changed size');
  }
);
```

## Functions

Functions are methods available for calling on the class

[addResizeListener](https://bryntum.com/docs/gantt/api/Core/helper/ResizeMonitor#function-addResizeListener-static)
Adds a resize listener to the passed element which is called when the element is resized by layout.

[removeResizeListener](https://bryntum.com/docs/gantt/api/Core/helper/ResizeMonitor#function-removeResizeListener-static)
Removes a resize listener from the passed element.

[onElementResize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeMonitor#function-onElementResize-static)
Event handler for deferred processing of ResizeMonitor entries. Prevents recursive calls during the same microtask, that would cause multiple resize events for a single resize. Fix for https://github.com/bryntum/support/issues/7373

If it is necessary to execute a ResizeObserver entry immediately, e.g. when the ResizeMonitor needs to be set up with an initial Rectangle in a `paint` event listener with `firstPaint : true`, use `ResizeMonitor.processElementResize(entries)` directly.

[processElementResize](https://bryntum.com/docs/gantt/api/Core/helper/ResizeMonitor#function-processElementResize-static)
Undeferred processing of ResizeMonitor entries.

## Typedefs

Typedefs are type definitions for the class

[ResizeMonitorEventCallback](https://bryntum.com/docs/gantt/api/Core/helper/ResizeMonitor#typedef-ResizeMonitorEventCallback)
Resize event handing callback
