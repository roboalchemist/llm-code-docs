# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/row/RowManager.md

# [RowManager](https://bryntum.com/docs/gantt/api/Grid/row/RowManager)

Virtual representation of the grid, using [Row](https://bryntum.com/docs/gantt/api/#Grid/row/Row) to represent rows. Plugs into [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) and exposes the following functions on grid itself:

* [getRecordCoords()](https://bryntum.com/docs/gantt/api/#Grid/row/RowManager#function-getRecordCoords)
* [getRowById()](https://bryntum.com/docs/gantt/api/#Grid/row/RowManager#function-getRowById)
* [getRow()](https://bryntum.com/docs/gantt/api/#Grid/row/RowManager#function-getRow)
* [getRowFor()](https://bryntum.com/docs/gantt/api/#Grid/row/RowManager#function-getRowFor)
* [getRowFromElement()](https://bryntum.com/docs/gantt/api/#Grid/row/RowManager#function-getRowFromElement)

```
let row = grid.getRowById(1);
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[prependRowBuffer](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#config-prependRowBuffer)
Number of rows to render above current viewport

[appendRowBuffer](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#config-appendRowBuffer)
Number of rows to render below current viewport

[rowHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#config-rowHeight)
Default row height, assigned from Grid at construction (either from config [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#config-rowHeight) or CSS). Can be set from renderers

[fixedRowHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#config-fixedRowHeight)
Set to `true` to get a small performance boost in applications that uses fixed row height

## Properties

Properties are getters/setters or publicly accessible variables on this class

[rows](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-rows)
Get all Rows

[topRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-topRow)
Get the Row that is currently displayed at top.

[bottomRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-bottomRow)
Get the Row currently displayed furthest down.

[firstVisibleRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-firstVisibleRow)
Get the topmost visible Row

[lastVisibleRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-lastVisibleRow)
Get the last visible Row

[rowHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-rowHeight)
Set a fixed row height (can still be overridden by renderers) or get configured row height. Setting refreshes all rows

[rowOffsetHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-rowOffsetHeight)
Get actually used row height, which includes any border and might be an average if using variable row height.

[allHeightsKnown](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-allHeightsKnown)
Returns `true` if all rows have a known height. They do if all rows are visited, or if RowManager is configured with `fixedRowHeight`. If so, all tops can be calculated exactly, no guessing needed

[totalHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#property-totalHeight)
Total estimated grid height (used for scroller)

## Functions

Functions are methods available for calling on the class

[initWithHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-initWithHeight)
Initializes the RowManager with Rows to fit specified height.

[reinitialize](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-reinitialize)
Releases all elements (not from dom), calculates how many are needed, creates those and renders

[matchRowCount](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-matchRowCount)
Add or remove rows to fit row count

[calculateRowCount](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-calculateRowCount)
Calculates how many rows fit in the available height (view height)

[insert](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-insert)
Animate adding or removing rows to/from the rows array.

[getRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getRow)
Get the Row at a specified store index. Returns `undefined` if the row index is not rendered.

[getRowById](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getRowById)
Get Row for specified record id

[getRowFromElement](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getRowFromElement)
Get a Row from an HTMLElement

[getRowAt](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getRowAt)
Get the row at the specified Y coordinate, which is by default viewport-based.

[getRowFor](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getRowFor)
Get a Row for either a record, a record id or an HTMLElement

[getNextRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getNextRow)
Gets the Row following the specified Row (by index or object). Wraps around the end.

[offsetRows](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-offsetRows)
Calls offset() for each Row passing along offset parameter

[storeKnownHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-storeKnownHeight)
Store supplied `height` using `id` as key in the height map. Called by `Row` when it gets its height. Keeps `averageRowHeight` and `totalKnownHeight` up to date. Ignored when configured with `fixedRowHeight`

[getOffsetHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getOffsetHeight)
Get the known or estimated offset height for the specified record id

[invalidateKnownHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-invalidateKnownHeight)
Invalidate cached height for a record. Removing it from `totalKnownHeight` and factoring it out of `averageRowHeight`.

[clearKnownHeights](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-clearKnownHeights)
Invalidates all cached height and resets `averageRowHeight` and `totalKnownHeight`

[onRecordIdChange](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-onRecordIdChange)
Handles record id changes by updating the heightMap key and the Row's id.

[calculateTop](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-calculateTop)
Calculates a row top from its data index. Uses known values from the height map, unknown are substituted with the average row height. When configured with `fixedRowHeight`, it will always calculate a correct value

[getRecordCoords](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getRecordCoords)
Returns top and bottom for rendered row or estimated coordinates for unrendered.

[getRecordCoordsByIndex](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-getRecordCoordsByIndex)
Returns top and bottom coordinates for specified row. If all heights are known, by for example using fixed row height, the top is calculated exactly. If not, the top is estimated based on the closest known row.

[forEach](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-forEach)
Calls a function for each Row

[refreshCell](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-refreshCell)
Refresh a single cell.

[returnToTop](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-returnToTop)
Renders from the top of the grid, also resetting scroll to top. Used for example when collapsing all groups.

[renderFromRecord](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-renderFromRecord)
Renders from specified records row and down (used for example when collapsing a group, does not affect rows above).

[renderFromRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-renderFromRow)
Renders from specified row and down (used for example when collapsing a group, does not affect rows above).

[renderRows](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-renderRows)
Renders the passed array (or [Set](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)) of [rows](https://bryntum.com/docs/gantt/api/#Grid/row/Row)

[translateFromRow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-translateFromRow)
Translates all rows after the specified row. Used when a single rows height is changed and the others should rearrange. (Called from Row#render)

[refresh](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-refresh)
Rerender all rows

[jumpToPosition](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-jumpToPosition)
Makes sure that specified record is displayed in view

[warpIfNeeded](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-warpIfNeeded)
Jumps to a position if it is far enough from current position. Otherwise does nothing.

[updateRenderedRows](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-updateRenderedRows)
Handles virtual rendering (only visible rows + buffer are in dom) for rows

[fillAbove](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-fillAbove)
Moves as many rows from the bottom to the top that are needed to fill to current scroll pos.

[fillBelow](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-fillBelow)
Moves as many rows from the top to the bottom that are needed to fill to current scroll pos.

[estimateTotalHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-estimateTotalHeight)
Estimates height needed to fit all rows, based on average row height. Also offsets rows if needed to not be above the reachable area of the view.

[displayRecordAtTop](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-displayRecordAtTop)
Moves a row from bottom to top and renders the corresponding record to it.

[displayRecordAtBottom](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#function-displayRecordAtBottom)
Moves a row from top to bottom and renders the corresponding record to it.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[rowRowHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#event-rowRowHeight)
Triggered when an individual rendered [Row](https://bryntum.com/docs/gantt/api/#Grid/row/Row) has its height changed.

[rowHeight](https://bryntum.com/docs/gantt/api/Grid/row/RowManager#event-rowHeight)
Triggered when the owning Grid's [rowHeight](https://bryntum.com/docs/gantt/api/#Grid/view/Grid#property-rowHeight) is changed.
