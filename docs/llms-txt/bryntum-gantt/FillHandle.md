# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/FillHandle.md

# [FillHandle](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle)

This feature adds a fill handle to a Grid range selection, which when dragged, fills the cells being dragged over with values based on the values in the original selected range. This is similar to functionality normally seen in various spreadsheet applications.

Requires [selectionMode.cell](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-selectionMode) to be activated.

This feature is **disabled** by default

```
const grid = new Grid({
    features : {
        fillHandle : true
    }
});
```

This feature will not work properly when Store uses [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[calculateFillValue](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#config-calculateFillValue)
Implement this function to be able to customize the value that cells will be filled with. Return `undefined` to use default calculations.

```
new Grid({
   features : {
       fillHandle : {
          calculateFillValue({cell, column, range, record}) {
             if(column.field === 'number') {
                return range.reduce(
                   (sum, location) => sum + location.record[location.column.field]
                );
             }
          }
       }
   }
});
```

[allowCropping](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#config-allowCropping)
Set to `true` to enable the fill range to crop the original selected range. This clears the cells which were a part of the original selected range, but are no longer a part of the smaller range.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFillHandle](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#property-isFillHandle)
Identifies an object as an instance of [FillHandle](https://bryntum.com/docs/gantt/api/#Grid/feature/FillHandle) class, or subclass thereof.

[isFillHandle](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#property-isFillHandle-static)
Identifies an object as an instance of [FillHandle](https://bryntum.com/docs/gantt/api/#Grid/feature/FillHandle) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[handleSelection](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#function-handleSelection)
Checks selection and sees to it that fill handle and border is drawn. Runs on next animation frame

[abort](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#function-abort)
Aborts an ongoing FillHandle drag operation

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeFillHandleDragStart](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#event-beforeFillHandleDragStart)
Fired before dragging of the FillHandle starts, return `false` to prevent the drag operation.

[fillHandleDragStart](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#event-fillHandleDragStart)
Fired when dragging of the FillHandle starts.

[fillHandleDrag](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#event-fillHandleDrag)
Fired while dragging the FillHandle.

[fillHandleBeforeDragFinalize](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#event-fillHandleBeforeDragFinalize)
Fired before the FillHandle dragging is finalized and values are applied to cells, return `false` to prevent the drag operation from applying data changes.

[fillHandleDragEnd](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#event-fillHandleDragEnd)
Fired after a FillHandle drag operation.

[fillHandleDragAbort](https://bryntum.com/docs/gantt/api/Grid/feature/FillHandle#event-fillHandleDragAbort)
Fired when a FillHandle drag operation is aborted.
