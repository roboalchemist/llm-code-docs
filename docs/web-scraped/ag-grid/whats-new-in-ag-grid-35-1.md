# Source: https://blog.ag-grid.com/whats-new-in-ag-grid-35-1/

Title: What's New in AG Grid 35.1

URL Source: https://blog.ag-grid.com/whats-new-in-ag-grid-35-1/

Published Time: 2026-02-11T12:20:48.000Z

Markdown Content:
*   [![Image 1: James Swinton-Bland](https://blog.ag-grid.com/content/images/size/w100/2024/08/me.jpeg)James Swinton-Bland](https://blog.ag-grid.com/author/james/)
*   [![Image 2: Kiril Matev](https://blog.ag-grid.com/content/images/size/w100/2024/12/Kiril-Matev-2.jpg)Kiril Matev](https://blog.ag-grid.com/author/kiril/)

11 February 2026|[Releases](https://blog.ag-grid.com/tag/version-release/)

![Image 3](https://blog.ag-grid.com/content/images/2026/02/AG-Grid-35.1-1.png)
AG Grid 35.1 includes named range date filtering, a powerful formula editor, native support for large integers, and new controls for managing themes and protecting exported Excel data:

### Key features

1.   [Formula Editor](https://ag-grid.com/data-grid/formula-editor-component/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35.1-release-blog) - Auto-complete for formula functions, click to select cells and ranges, and drag to fill capabilities. 
2.   [Named Date Range Filters](https://ag-grid.com/data-grid/filter-date/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35.1-release-blog#built-in-named--relative-date-ranges) - Filter by named and relative date ranges to make common filtering tasks easier, e.g. filter by "yesterday" or "last month". 
3.   [BigInt Support](https://ag-grid.com/data-grid/cell-data-types/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35.1-release-blog#bigint) - A new `BigInt` cell data type that enables exact, precision-safe handling of large integers across core grid features. 
4.   [Theme Builder Imports](https://www.ag-grid.com/theme-builder/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35.1-release-blog) - Import, preview and edit existing themes within our [Theme Builder](https://www.ag-grid.com/theme-builder/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog). 
5.   [Excel Export Data Protection](https://ag-grid.com/data-grid/excel-export-data-protection/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35.1-release-blog) - protect the exported worksheet so that users can only edit specific cells. 

Formula editor
--------------

With the new formula editor, users can now create formulas more efficiently and accurately with support for auto-complete, cell & range selection, and drag to fill functionality:

0:00

/0:27

![Image 4](https://storage.ghost.io/c/b0/00/b000c74b-bdbf-4c17-a6cb-0b11b3965a82/content/media/2026/02/Formula-Editor---Light---Final_thumb.jpg)

The Formula Cell Editor is the default editor for columns with`allowFormula: true` - You can override the default functionality by supplying your own Cell Renderer.

Visit the [formula editor](https://www.ag-grid.com/data-grid/formula-editor-component/?ref=blog.ag-grid.com) docs for more information.

Named date range filters
------------------------

With [named date range filters](https://www.ag-grid.com/data-grid/filter-date/?ref=blog.ag-grid.com#enabling-built-in-date-ranges), users can now filter their data with more intuitive, pre-defined date ranges. For example, instead of manually filtering dates between `01/01/2026` and `31/01/2026`, users can simply select "last month":

0:00

/0:16

![Image 5](https://storage.ghost.io/c/b0/00/b000c74b-bdbf-4c17-a6cb-0b11b3965a82/content/media/2026/02/Date-Range-Filters_thumb.jpg)
We provide [22 pre-defined filters](https://ag-grid.com/data-grid/filter-date/?ref=blog.ag-grid.com#available-built-in-date-filter-options), and developers can choose which ones to expose to users by adding them to the`filterOptions`array in the date filter configuration:

```
// Enable built-in date ranges
const columnDefs: ColDef[] = [
  {
    filter: 'agDateColumnFilter',
    filterParams: {
      // Enable built-in named & relative date ranges
      filterOptions: [
        'empty', // optional: show 'Choose one' option first
        'yesterday',
        'today',
        'tomorrow',
        'last7Days',
        'lastWeek',
        'thisWeek',
        'nextWeek',
        'last30Days',
        'lastMonth',
        // ... All other preset ranges
      ],
      // Other filter settings...
    },
  },
];
```

Visit the [Built-in Named & Relative Date Ranges](https://www.ag-grid.com/data-grid/filter-date/?ref=blog.ag-grid.com#built-in-named--relative-date-ranges) docs for more information.

BigInt support
--------------

AG Grid 35.1 adds a new `BigInt` cell data type, which is a numeric type used to represent integers larger than the fixed-size limits of standard integer types. BigInts enable more efficient and accurate calculations, filtering, and sorting when working with large numbers, e.g, values greater than 2⁵³−1.

The `BigInt` cell data type will be inferred automatically based on your data. You can also manually define the cell data type on specific columns if needed:

```
const gridOptions = {
    columnDefs: [
        {
            field: 'transactions',
            // enables cell data type `bigint`
            cellDataType: 'bigint'
        }
    ],

    // other grid options ...
}
```

The BigInt data type works with the Text Cell Editor, Set Filter and Absolute Sorting features.

Visit the [BigInt](https://www.ag-grid.com/data-grid/cell-data-types/?ref=blog.ag-grid.com#bigint) docs for more information.

Theme builder imports
---------------------

Our Theme Builder, a UI for creating and customising themes, now supports theme imports, allowing you to visualise, test, and edit your existing themes within the Theme Builder:

0:00

/0:11

![Image 6](https://storage.ghost.io/c/b0/00/b000c74b-bdbf-4c17-a6cb-0b11b3965a82/content/media/2026/02/Theme-Builder-Import---Light---Simple_thumb.jpg)
Visit the [Theme Builder](https://www.ag-grid.com/theme-builder?ref=blog.ag-grid.com) to try it out.

Excel export data protection
----------------------------

The new data protection capability in Excel exports allows developers to protect the exported worksheet, to prevent users from editing specific cells.

Worksheet protection is enabled by setting`protectSheet`in the[Excel Export Params](https://www.ag-grid.com/react-data-grid/excel-export-api/?ref=blog.ag-grid.com#excelexportparams), which will lock editing of all cells:

```
const excelExportParams = useMemo(() => {
  return {
    protectSheet: true,
  };
}, []);

<AgGridReact excelExportParams={excelExportParams} />;
```

You can also override the default worksheet protection options by supplying a config object to `protectSheet`:

```
const excelExportParams = useMemo(() => {
  return {
    protectSheet: true,
    password: "secret",
    autoFilter: true,
    formatCells: true,
    deleteRows: true,
  };
}, []);
```

Visit the [Excel Export - Data Protection](https://www.ag-grid.com/data-grid/excel-export-data-protection/?ref=blog.ag-grid.com) docs for more information on worksheet protection defaults and unlocking specific cells.

Summary
-------

AG Grid 35.1 focuses on improving everyday grid workflows by reducing configuration overhead, increasing precision, and expanding control over presentation and output. This release:

*   Introduces a new Formula Editor to streamline formula creation and editing.
*   Exposes 22 pre-defined named date ranges to simplify common date filtering scenarios.
*   Adds a BigInt cell data type for safe and accurate handling of large integers.
*   Enables importing existing themes into the Theme Builder for faster iteration and testing.
*   Adds worksheet protection to Excel exports for greater control over shared data.

As always, we welcome feedback. Enterprise customers can contact us via [Zendesk](https://ag-grid.zendesk.com/hc/en-us?ref=blog.ag-grid.com); Alternatively, please submit a [GitHub issue](https://github.com/ag-grid/ag-grid/issues?ref=blog.ag-grid.com) or complete our [contact form](https://ag-grid.com/license-pricing/?ref=blog.ag-grid.com#request-trial-licence).

Next steps
----------

**New to AG Grid?** Get started in minutes, for free, with your favourite framework:

[![Image 7: React Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg)](https://www.ag-grid.com/react-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)[![Image 8: Angular Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Angular_gradient_logo.png/500px-Angular_gradient_logo.png)](https://www.ag-grid.com/angular-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)[![Image 9: Vue Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg)](https://www.ag-grid.com/vue-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)[![Image 10: Javascript Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png)](https://www.ag-grid.com/javascript-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog)

**Considering AG Grid Enterprise?**[Request a free 30-day trial licence](https://www.ag-grid.com/data-grid/community-vs-enterprise/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-35-release-blog#request-a-30-day-enterprise-bundle-trial-licence) to test your application in production and get direct access to our support team.

Happy coding!

Read more posts about...
