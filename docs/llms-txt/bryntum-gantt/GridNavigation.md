# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/mixin/GridNavigation.md

# [GridNavigation](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation)

Mixin for Grid that handles cell to cell navigation.

See [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) for more information on grid cell keyboard navigation.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridNavigation](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#property-isGridNavigation)
Identifies an object as an instance of [GridNavigation](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridNavigation) class, or subclass thereof.

[isGridNavigation](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#property-isGridNavigation-static)
Identifies an object as an instance of [GridNavigation](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridNavigation) class, or subclass thereof.

[focusedCell](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#property-focusedCell)
Grid GridLocation which encapsulates the currently focused cell. Set to focus a cell or use [focusCell](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridNavigation#function-focusCell).

[isActionableLocation](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#property-isActionableLocation)
This property is `true` if an element _within_ a cell is focused.

[cellCSSSelector](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#property-cellCSSSelector)
CSS selector for currently focused cell. Format is "\[data-index=index\] \[data-column-id=columnId\]".

## Functions

Functions are methods available for calling on the class

[onFocusedRowDerender](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-onFocusedRowDerender)
Called by the RowManager when the row which contains the focus location is derendered.

This keeps focus in a consistent place.

[isFocused](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-isFocused)
Checks whether a cell is focused.

[onGridBodyFocusIn](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-onGridBodyFocusIn)
This function handles focus moving into, or within the grid.

[restoreActiveItem](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-restoreActiveItem)
Sets the passed record as the current focused record for keyboard navigation and selection purposes. This API is used by Combo to activate items in its picker.

[focusCell](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-focusCell)
Navigates to a cell and/or its row (depending on selectionMode)

[internalNextPrevCell](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-internalNextPrevCell)
Selects the cell before or after currently focused cell.

[navigateRight](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-navigateRight)
Select the cell after the currently focused one.

[navigateLeft](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-navigateLeft)
Select the cell before the currently focused one.

[internalNextPrevRow](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-internalNextPrevRow)
Selects the next or previous record in relation to the current selection. Scrolls into view if outside.

[navigateDown](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-navigateDown)
Navigates to the cell below the currently focused cell

[navigateUp](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#function-navigateUp)
Navigates to the cell above the currently focused cell

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[navigate](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridNavigation#event-navigate)
Triggered when a user navigates to a grid cell
