# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/SubGrid.md

# [SubGrid](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid)

A SubGrid is a part of the grid (it has at least one and normally no more than two, called locked and normal). It has its own header, which holds the columns to display rows for in the SubGrid. SubGrids are created by Grid, but you can configure your SubGrids with the [subGridConfigs](https://bryntum.com/docs/gantt/api/#Grid/view/GridBase#config-subGridConfigs) object.

```
const grid = new Grid({
    appendTo : 'container',

    features : {
        regionResize : true
    },

    subGridConfigs : {
        locked : {
            width : 360
        },
        normal : {
            flex : 1
        }
    }
});
```

If you use multiple regions in your grid, you can enable the [RegionResize](https://bryntum.com/docs/gantt/api/#Grid/feature/RegionResize) feature to let users resize and collapse/expand grid sections.

If not configured with a width or flex, the SubGrid will be sized to fit its columns. In this case, if all columns have a fixed width (not using flex) then toggling columns will also affect the width of the SubGrid.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[region](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#config-region)
Region (name) for this SubGrid

[columns](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#config-columns)
Column store, a store containing the columns for this SubGrid

[weight](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#config-weight)
The subgrid "weight" determines its position among its SubGrid siblings. Higher weights go further right.

[sealedColumns](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#config-sealedColumns)
Set `true` to disable moving columns into or out of this SubGrid.

[collapsed](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#config-collapsed)
Set `true` to start subgrid collapsed. To operate collapsed state on subgrid use [collapse](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid#function-collapse)/[expand](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid#function-expand) methods.

[resizable](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#config-resizable)
Set to `false` to prevent this subgrid being resized with the [RegionResize](https://bryntum.com/docs/gantt/api/#Grid/feature/RegionResize) feature

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSubGrid](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#property-isSubGrid)
Identifies an object as an instance of [SubGrid](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid) class, or subclass thereof.

[isSubGrid](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#property-isSubGrid-static)
Identifies an object as an instance of [SubGrid](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid) class, or subclass thereof.

[collapsed](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#property-collapsed)
Set `true` to start subgrid collapsed. To operate collapsed state on subgrid use [collapse](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid#function-collapse)/[expand](https://bryntum.com/docs/gantt/api/#Grid/view/SubGrid#function-expand) methods.

[width](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#property-width)
Get/set SubGrid width, which also sets header and footer width (if available).

[flex](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#property-flex)
Get/set SubGrid flex, which also sets header and footer flex (if available).

[viewRectangle](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#property-viewRectangle)
Get the "viewport" for the SubGrid as a Rectangle

[rowElements](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#property-rowElements)
Get all row elements for this SubGrid.

## Functions

Functions are methods available for calling on the class

[construct](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-construct)
SubGrid constructor

[toggleSplitterCls](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-toggleSplitterCls)
Toggle (add/remove) class for splitters

[fixWidths](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-fixWidths)
Sets header width and scroller width (if needed, depending on if using flex). Might also change the subgrids width, if it uses a width calculated from its columns.

[onInternalResize](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-onInternalResize)
Called when grid changes size. SubGrid determines if it has changed size and triggers scroll (for virtual rendering in cells to work when resizing etc.)

[syncParallelSplitters](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-syncParallelSplitters)
Keeps the parallel splitters in the header, footer and fake scroller synced in terms of being collapsed or not.

[updateHasFlex](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-updateHasFlex)
Called when updating column widths to apply 'b-has-flex' which is used when fillLastColumn is configured.

[resizeColumnsToFitContent](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-resizeColumnsToFitContent)
Resize all columns in the SubGrid to fit their width, according to their configured [fitMode](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-fitMode)

[refreshFakeScroll](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-refreshFakeScroll)
Fixes widths of fake scrollers

[initScroll](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-initScroll)
Init scroll syncing for header and footer (if available).

[handleHorizontalScroll](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-handleHorizontalScroll)
Triggers the 'horizontalScroll' event + makes sure overlay scrollbar is reachable with pointer for a substantial amount of time after scrolling starts

[scrollColumnIntoView](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-scrollColumnIntoView)
Scrolls a column into view (if it is not already). Called by Grid#scrollColumnIntoView, use it instead to not have to care about which SubGrid contains a column.

[onAddRow](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-onAddRow)
Creates elements for the new rows when RowManager has determined that more rows are needed

[clearRows](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-clearRows)
Removes all row elements from the subgrids body and empties cache

[collapse](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-collapse)
Collapses subgrid. If collapsing subgrid is the only one expanded, next subgrid to the right (or previous) will be expanded.

```
let locked = grid.getSubGrid('locked');
locked.collapse().then(() => {
    console.log(locked.collapsed); // Logs 'True'
});

let normal = grid.getSubGrid('normal');
normal.collapse().then(() => {
    console.log(locked.collapsed); // Logs 'False'
    console.log(normal.collapsed); // Logs 'True'
});
```

[expand](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-expand)
Expands subgrid.

```
grid.getSubGrid('locked').expand().then(() => console.log('locked grid expanded'));
```

[toggleCollapse](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#function-toggleCollapse)
Toggles this subgrid `collapsed` state.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[horizontalScrollEnd](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#event-horizontalScrollEnd)
Fires after the Grid is done scrolling horizontally in one of its SubGrids

[horizontalScroll](https://bryntum.com/docs/gantt/api/Grid/view/SubGrid#event-horizontalScroll)
Fires when the Grid is scrolling horizontally in one of its SubGrids
