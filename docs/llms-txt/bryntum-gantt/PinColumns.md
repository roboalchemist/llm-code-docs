# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/PinColumns.md

# [PinColumns](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns)

Allows pinning columns to the start or end region of the grid without any additional subGrid configurations. When pinning to a region that does not yet exist, the feature creates the required subGrid on the fly.

This feature is **disabled** by default. To enable it:

```
new Grid({
    features : {
        pinColumns : true
    },
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPinColumns](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#property-isPinColumns)
Identifies an object as an instance of [PinColumns](https://bryntum.com/docs/gantt/api/#Grid/feature/PinColumns) class, or subclass thereof.

[isPinColumns](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#property-isPinColumns-static)
Identifies an object as an instance of [PinColumns](https://bryntum.com/docs/gantt/api/#Grid/feature/PinColumns) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[populateHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#function-populateHeaderMenu)
Populates the header context menu items.

[populateCellMenu](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#function-populateCellMenu)
Populates the cell context menu items.

[isPinningColumnDisabled](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#function-isPinningColumnDisabled)
Returns `true` if the pin/unpin action should be disabled for the given column. Disables when the column is already in the target region or when moving out of the normal region would leave it empty.

[pinColumn](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#function-pinColumn)
Pins the given column to the requested region. Creates the subgrid if needed.

[pinColumnToStart](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#function-pinColumnToStart)
Pins the given column to the `start` region. Creates the subgrid if needed.

[pinColumnToEnd](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#function-pinColumnToEnd)
Pins the given column to the `end` region. Creates the subgrid if needed.

[unpinColumn](https://bryntum.com/docs/gantt/api/Grid/feature/PinColumns#function-unpinColumn)
Unpins the given column from the requested region. Creates the subgrid if needed.
