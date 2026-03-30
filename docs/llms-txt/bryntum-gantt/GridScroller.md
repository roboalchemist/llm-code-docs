# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/util/GridScroller.md

# [GridScroller](https://bryntum.com/docs/gantt/api/Grid/util/GridScroller)

A Scroller subclass which handles scrolling in a grid.

If the grid has no parallel scrolling grids (No locked columns), then this functions transparently as a Scroller.

If there are locked columns, then scrolling to an _element_ will invoke the scroller of the subgrid which contains that element.

## Functions

Functions are methods available for calling on the class

[onPartnerOverflowChange](https://bryntum.com/docs/gantt/api/Grid/util/GridScroller#function-onPartnerOverflowChange)
Called when a partner GridScroller that we are sharing X position with changes its overflowing state.

This will mean the addition or removal of a vertical scrollbar.

All partners must stay in sync. If another parter has a vertical scrollbar and we do not, we must set our overflowY to 'scroll' so that we show an empty scrollbar to keep widths synchronized.
