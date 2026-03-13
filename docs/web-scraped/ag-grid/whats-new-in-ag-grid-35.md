# Source: https://blog.ag-grid.com/whats-new-in-ag-grid-35/

Title: What's New in AG Grid 35

URL Source: https://blog.ag-grid.com/whats-new-in-ag-grid-35/

Published Time: 2025-12-10T10:20:58.000Z

Markdown Content:
*   [![Image 1: James Swinton-Bland](https://blog.ag-grid.com/content/images/size/w100/2024/08/me.jpeg)James Swinton-Bland](https://blog.ag-grid.com/author/james/)
*   [![Image 2: Kiril Matev](https://blog.ag-grid.com/content/images/size/w100/2024/12/Kiril-Matev-2.jpg)Kiril Matev](https://blog.ag-grid.com/author/kiril/)

10 December 2025|[Releases](https://blog.ag-grid.com/tag/version-release/)

![Image 3: Whats New in Version 35 of AG Grid's Data Grid: Formulas](https://blog.ag-grid.com/content/images/2025/12/AG-Grid-39.png)
AG Grid 35 now allows users to create spreadsheet-style formulas directly within cells, in addition to support for dragging row groups, absolute sorting and column selection.

### Key Features

1.   [Formulas](https://ag-grid.com/data-grid/formulas/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog) - Enable spreadsheet-style formulas within cells that can reference other cells, functions, and operators, to allow users to create their own custom calculations. 
2.   [Row Group Dragging](https://ag-grid.com/data-grid/grouping-row-dragging/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog) - Move rows within or across groups using drag-and-drop, whilst the grid takes care of any necessary data updates. 
3.   [Absolute Sorting](https://ag-grid.com/data-grid/row-sorting/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog#absolute-sorting) - Sort numeric values by magnitude, disregarding sign (e.g. positive/negative) to measure deviations, anomalies, or variances. 
4.   [Column Selection](https://ag-grid.com/data-grid/cell-selection/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog#selecting-cells-via-column-headers) - Select an entire column with a single click or key press, ready for further processing, analysis, or visualisation. 
5.   [Filtering & Export Overlays](https://ag-grid.com/data-grid/overlays-overview/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog) - Display full-customisable overlays to users when performing long-running filter or export operations. 

Formulas
--------

AG Grid 35 now supports formulas, allowing users to create dynamic calculations by typing them directly into a cell. Formulas can reference other [cells](https://ag-grid.com/data-grid/formulas/?ref=blog.ag-grid.com#cell-references), [functions](https://ag-grid.com/data-grid/formulas/?ref=blog.ag-grid.com#functions), [mathematical operators](https://ag-grid.com/data-grid/formulas/?ref=blog.ag-grid.com#mathematical-operations), and [constants](https://ag-grid.com/data-grid/formulas/?ref=blog.ag-grid.com#constants), just like in Excel:

0:00

/0:19

![Image 4](https://blog.ag-grid.com/content/media/2025/12/Formulas_thumb.jpg)
To enable formulas, set`allowFormula` to `true`on the desired columns and implement the `getRowId` callback:

```
// Assign rowIds
const getRowId = (params) => String(params.data.rid);

// Enable Formulas
const columnDefs = [
  { 
    field: 'subtotal',
    allowFormula: true
  },
  // ... other columns
];
```

If the functions provided out of the box don't meet your requirements, [custom functions](https://ag-grid.com/data-grid/formulas/?ref=blog.ag-grid.com#custom-functions) can be defined via the [`formulaFuncs`](https://ag-grid.com/data-grid/grid-options/?ref=blog.ag-grid.com#reference-formulas-formulaFuncs) grid option to perform any kind of calculation:

```
const gridOptions = {
  formulaFuncs: {
    foo: {
        func: (params) => {
            return bar;
        },
    },
  }
  // ... other grid options 
}
```

Formulas provide users with ultimate control over their data, allowing them to manipulate and interrogate their data however they like, without needing to go back to their developers for updates to the grid configuration.

Visit the [Formulas](https://ag-grid.com/data-grid/formulas/?ref=blog.ag-grid.com) documentation for more information.

Row Group Dragging
------------------

Row dragging can now be combined with[Row Grouping](https://ag-grid.com/data-grid/grouping/?ref=blog.ag-grid.com), allowing users to move rows within or between groups:

0:00

/0:21

![Image 5](https://blog.ag-grid.com/content/media/2025/12/Managed-Row-Dragging---Row-Grouping_thumb.jpg)
To enable row dragging with row groups, set the `rowDrag`, `suppressMoveWhenRowDragging`, `refreshAfterGroupEdit`, and `rowDragManaged` properties to `true`, and implement the `getRowId` callback:

```
const gridOptions = {
  columnDefs: [
    { field: "country", width: 120, rowGroup: true, editable: true },
    { field: "year", width: 90, rowGroup: true, editable: true },
    ...
  ],
  // Enable Row Dragging
  autoGroupColumnDef: {
    rowDrag: true,
    width: 250,
  },
  // Configure Row Dragging w/ Groups
  suppressMoveWhenRowDragging: true,
  refreshAfterGroupEdit: true,
  rowDragManaged: true,
  getRowId: ({ data }) => data.id,
};
```

Row group dragging is perfect for data that needs to be flexible, such as adjusting line-items in financial reports, reordering tasks within a sprint, or moving accounts between regions.

Visit the [Row Grouping - Row Dragging](https://ag-grid.com/data-grid/grouping-row-dragging/?ref=blog.ag-grid.com) documentation for more information.

Absolute Sorting
----------------

Absolute Sorting sorts numeric values by magnitude, ignoring their sign - ordering values by their size, regardless of whether it is positive or negative:

0:00

/0:10

![Image 6](https://blog.ag-grid.com/content/media/2025/12/Absolute-Sorting_thumb.jpg)
To enable absolute sorting, simply add the `type: 'absolute'` property to the `colDef.sort` property:

```
const gridOptions = {
    columnDefs: [
        {
            field: 'rankingChange',
            sort: { direction: 'asc', type: 'absolute' },
            sortingOrder: [
                { direction: 'asc', type: 'absolute' }, 
                { direction: 'desc', type: 'absolute' },
                null, 
            ],
        },
        // ... other columns 
    ],
}
```

Absolute sorting is ideal for ranking deviations, anomalies, variances, and error deltas where size is more important than direction.

Visit the [Absolute Sorting](https://ag-grid.com/data-grid/row-sorting/?ref=blog.ag-grid.com#absolute-sorting) documentation for more information.

Column Selection
----------------

Columns now support selection, allowing users to easily select entire columns of data.

Columns are selected by clicking the column header or pressing the enter ↵ key when the column header is focused. The ctrl ⌃ and shift ⇧ keys also allow multiple columns to be selected:

0:00

/0:19

![Image 7](https://blog.ag-grid.com/content/media/2025/12/Column-Selection_thumb.jpg)
To enable column selection, set the`enableColumnSelection` property to `true`on the desired columns:

```
const columnDefs = [
  { 
    field: 'subtotal', 
    enableColumnSelection: true 
  },
  // ... other columns 
]);
```

Column selection is particularly useful when users want to do something with a large range of data, such as creating an [integrated chart](https://ag-grid.com/data-grid/integrated-charts/?ref=blog.ag-grid.com), avoiding the need to manually select all of the cells themselves.

Visit the [Column Selection](https://ag-grid.com/data-grid/cell-selection/?ref=blog.ag-grid.com#selecting-cells-via-column-headers) documentation for more information.

Filtering & Export Overlays
---------------------------

Overlays are used to display messages over the grid to indicate the grid state. AG Grid 35 introduces two new overlays - a no matching rows overlay, which is shown when there are no matching rows to a column filter, and an exporting overlay, shown during exporting operations:

0:00

/0:06

![Image 8](https://blog.ag-grid.com/content/media/2025/12/Exporting-Overlay_thumb.jpg)
The loading, exporting, no rows and no matching rows overlays are enabled by default, and custom overlays can be provided via the `gridOptions.components.{overlayKey}` property:

```
const gridOptions = {
    components: {
        agLoadingOverlay: CustomLoadingOverlay,
        agNoRowsOverlay: CustomNoRowsOverlay,
        agNoMatchingRowsOverlay: CustomNoMatchingRows,
        agExportingOverlay: CustomExportingOverlay
    },
}
```

Overlays help provide clearer feedback to users when performing long-running actions on large datasets or applying specific filters.

Visit our [Overlays](https://ag-grid.com/data-grid/overlays-overview/?ref=blog.ag-grid.com) documentation for more information.

Summary
-------

AG Grid 35 is one of our most significant releases yet, focused on user interactivity and experience:

*   Formulas enable users to create dynamic calculations directly from the UI,
*   Row group dragging simplifies the reorganisation of grouped datasets,
*   Absolute sorting provides new ways to rank data,
*   Column selection accelerates bulk operations, and
*   Filtering and export overlays improve clarity for users working with large datasets and long-running processes.

As always, we're here to help, and we're keen to hear your feedback. Enterprise customers can contact us via [Zendesk](https://ag-grid.zendesk.com/hc/en-us?ref=blog.ag-grid.com); Alternatively, please submit a [GitHub issue](https://github.com/ag-grid/ag-grid/issues?ref=blog.ag-grid.com), or complete our [contact form](https://ag-grid.com/license-pricing/?ref=blog.ag-grid.com#request-trial-licence).

Next Steps
----------

New to AG Grid? Get started in minutes, for free:

[![Image 9: React Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg)](https://www.ag-grid.com/react-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)[![Image 10: Angular Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Angular_gradient_logo.png/500px-Angular_gradient_logo.png)](https://www.ag-grid.com/angular-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)[![Image 11: Vue Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg)](https://www.ag-grid.com/vue-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)[![Image 12: Javascript Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png)](https://www.ag-grid.com/javascript-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)

Considering AG Grid Enterprise? [Request a free 30-day trial licence](https://www.ag-grid.com/data-grid/community-vs-enterprise/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog#request-a-30-day-enterprise-bundle-trial-licence) to test your application in production and get direct access to our support team.

Happy coding!

Read more posts about...
