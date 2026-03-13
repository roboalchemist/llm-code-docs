# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/drag/DragProxy.md

# [DragProxy](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy)

Drag proxies are helper classes that represent the object being dragged in some visual way. This is an abstract base with which particular drag proxy classes (such as, [DragTipProxy](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragTipProxy) are registered.

Derived classes the various template methods of this class to manage their particular form of visual feedback.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[dragging](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#config-dragging)
The currently active `DragContext`. This context will be active prior to be passed to the proxy. This config is set by [dragStart](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#function-dragStart) and cleared by [dragEnd](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#function-dragEnd).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDragProxy](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#property-isDragProxy)
Identifies an object as an instance of [DragProxy](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy) class, or subclass thereof.

[isDragProxy](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#property-isDragProxy-static)
Identifies an object as an instance of [DragProxy](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy) class, or subclass thereof.

[owner](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#property-owner)
The `Draggable` instance that owns this drag proxy.

## Functions

Functions are methods available for calling on the class

[close](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#function-close)
This template method is called when [dragging](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#config-dragging) is reset to `null`.

[open](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#function-open)
This template method is called when [dragging](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#config-dragging) is set to a non-`null` value.

[dragStart](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#function-dragStart)
This template method is called by the `Draggable` instance when the drag officially starts. This sets the [dragging](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#config-dragging) config to `drag`, which triggers the call to [open](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#function-open).

[dragMove](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#function-dragMove)
This template method is called by the `Draggable` instance as drag movement occurs.

[dragEnd](https://bryntum.com/docs/gantt/api/Core/util/drag/DragProxy#function-dragEnd)
This template method is called by the `Draggable` instance when the drag completes.

This sets the [dragging](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#config-dragging) config to `null`, which triggers the call to [close](https://bryntum.com/docs/gantt/api/#Core/util/drag/DragProxy#function-close).
