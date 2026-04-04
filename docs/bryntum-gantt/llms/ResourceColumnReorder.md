# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ResourceColumnReorder.md

# [ResourceColumnReorder](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder)

Allows user to reorder resource columns in vertical mode by dragging them. The feature fires various events during the drag operation (see events below). To get notified about the actual resource reorder, you can also listen to the `change` event on the scheduler [ResourceStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/ResourceStore).

This feature is **disabled** by default and only works when the scheduler is in vertical mode.

Basic usage
-----------

```
const scheduler = new Scheduler({
    mode     : 'vertical',
    features : {
        resourceColumnReorder : true
    }
});
```

Validation
----------

You can validate the drag drop flow by listening to the `resourceColumnDrag` event:

```
const scheduler = new Scheduler({
    mode     : 'vertical',
    features : {
        resourceColumnReorder : true
    },
    listeners : {
        resourceColumnDrag({ context }) {
            // Prevent dropping on certain resources
            if (context.insertBefore?.isSpecialResource) {
                context.valid = false;
            }
        }
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[targetSelector](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#config-targetSelector)
A CSS selector used to determine which elements can initiate a drag operation.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResourceColumnReorder](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#property-isResourceColumnReorder)
Identifies an object as an instance of [ResourceColumnReorder](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceColumnReorder) class, or subclass thereof.

[isResourceColumnReorder](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#property-isResourceColumnReorder-static)
Identifies an object as an instance of [ResourceColumnReorder](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceColumnReorder) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[init](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#function-init)
Initialize drag & drop (called on first paint)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[resourceColumnBeforeDragStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#event-resourceColumnBeforeDragStart)
Fired before dragging starts, return `false` to prevent the drag operation.

[resourceColumnDragStart](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#event-resourceColumnDragStart)
Fired when dragging starts.

[resourceColumnDrag](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#event-resourceColumnDrag)
Fired while the resource column is being dragged. You can signal that the drop position is valid or invalid by setting `context.valid = false;`

[resourceColumnBeforeDropFinalize](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#event-resourceColumnBeforeDropFinalize)
Fired before the drop is finalized. You can return `false` or a Promise that resolves to `false` to cancel the drop operation.

[resourceColumnDrop](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#event-resourceColumnDrop)
Fired after drop

[resourceColumnDragAbort](https://bryntum.com/docs/gantt/api/Scheduler/feature/ResourceColumnReorder#event-resourceColumnDragAbort)
Fired when drag is aborted
