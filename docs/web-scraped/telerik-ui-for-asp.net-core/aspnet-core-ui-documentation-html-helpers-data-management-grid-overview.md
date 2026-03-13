# Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/overview

Title: ASP.NET Core Data Management Grid Overview - Telerik UI for ASP.NET Core

URL Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/overview

Markdown Content:
New to Telerik UI for ASP.NET Core?[Start a free 30-day trial](https://www.telerik.com/try/aspnet-core-ui)

Updated

on Dec 10, 2025

The Telerik UI Grid TagHelper and HtmlHelper for ASP.NET Core are server-side wrappers for the Kendo UI Grid widget. To add the component to your ASP.NET Core app, you can use either.

The Grid is a powerful control for displaying data in a tabular format. It provides options for executing data operations, such as paging, sorting, filtering, grouping, and editing, which determine the way the data is presented and manipulated. The Grid supports data binding to local and remote sets of data by using the Kendo UI for jQuery DataSource component.

* [Demo page for the Grid HtmlHelper](https://demos.telerik.com/aspnet-core/grid/index)

* [Demo page for the Grid TagHelper](https://demos.telerik.com/aspnet-core/grid/tag-helper)

[Initializing the Grid](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/overview#initializing-the-grid)
----------------------------------------------------------------------------------------------------------------------------------------------

The following example demonstrates how to define the Grid.

Razor

```
@(Html.Kendo().Grid<Kendo.Mvc.Examples.Models.Customer>()
  .Name("grid")
  .Columns(columns =>
  {
   columns.Bound(c => c.ContactName).Width(140);
   columns.Bound(c => c.ContactTitle).Width(190);
   columns.Bound(c => c.CompanyName);
   columns.Bound(c => c.Country).Width(110);
  })
  .DataSource(dataSource => dataSource
   .Ajax()
   .Read(read => read.Action("Customers_Read", "Grid"))
  )
    )
```

> The default casing for JSON strings in ASP.NET Core is camelCase. The Telerik UI components that are data-bound depend on PascalCase formatted response from the server. If the JSON serialization isn't configured properly, the UI components will display wrong data. To find out how to configure the application to return the data in Pascal-case, refer to the [JSON Serialization](https://www.telerik.com/aspnet-core-ui/documentation/installation/json-serialization) article.

[Basic Configuration](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/overview#basic-configuration)
------------------------------------------------------------------------------------------------------------------------------------------

The Grid configuration options are passed as attributes of the helper. The Grid uses the [DataSource component](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/datasource/overview) to bind its data.

> To parse the value to a proper data type, set a `type` field in the DataSource schema model of the Grid HtmlHelper or TagHelper.

Razor

```
@(Html.Kendo().Grid<TelerikAspNetCoreApp4.Models.OrderViewModel>()
        .Name("grid")
        .Columns(columns =>
        {
            columns.Bound(p => p.OrderID).Width(120);
            columns.Bound(p => p.OrderDate).Format("{0:MM/dd/yyyy}");
            columns.Bound(p => p.ShipName).Width(300);
            columns.Bound(p => p.ShipCity).Width(250);
        })
        .Scrollable()
        .Groupable()
        .Sortable()
        .Filterable()
        .Pageable(pageable => pageable
        .ButtonCount(5)
        .Refresh(true)
        .PageSizes(new[] { 5, 10, 20 }))
        .HtmlAttributes(new { style = "height: 550px;" })
        .DataSource(dataSource => dataSource
            .Ajax()
            .PageSize(20)
            .Read(read => read.Action("Orders_Read", "Grid"))
        )
    )
```

> You can accelerate your Grid journey with the [Telerik ASP.NET Core AI Coding Assistant](https://www.telerik.com/aspnet-core-ui/documentation/ai/overview) and the available [Grid-related prompts](https://www.telerik.com/aspnet-core-ui/documentation/ai/prompt-library#grid).

[Functionality and Features](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/overview#functionality-and-features)
--------------------------------------------------------------------------------------------------------------------------------------------------------

| Feature | Description |
| --- | --- |
| [Data binding](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/binding/overview) | You can bind the Grid to remote data or to local arrays of data. Additionally, you can use [SignalR](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/binding/signalr-binding) or configure your [custom binding](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/binding/custom-binding). |
| [Editing](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/editing/overview) | The Grid supports various editing modes that allow you to control the way the data is represented. |
| [Filtering](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/filtering) | To filter the displayed data, you can use row, checkbox, and menu filtering. |
| [Grouping](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/grouping/overview) | The Grid provides built-in aggregates for a grand total row and column values. Additionally, you can use group paging to load groups on demand and page through the groups at the same time. |
| [Paging](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/paging) | Use the built-in paging functionality to paginate the data. For optimal performance, perform the paging operations on the server. |
| [Sorting](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/sorting) | The single-, multi-, and mixed-sort modes allow you to address various sorting requirements. |
| [Search panel](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/search-panel) | The Grid comes with a search panel out-of-the-box and allows the users to quickly find the needed data. |
| [Export to Excel](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/export/excel-export) | The Grid enables you to export its content to Excel. |
| [Export to PDF](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/export/pdf-export) | You can use the built-in PDF export functionality. |
| [Printing](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/export/print-export) | If desired, you can print only the content of the Grid and ignore the rest of the page. |
| Column enhancements | The built-in Grid features like [locked](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/columns/locked) and [sticky](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/columns/sticky) columns, [column templates](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/columns/templates), [multi-column headers](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/columns/multicolumn-headers), [column resizing](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/columns/resizing) and [reordering](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/columns/reordering) allow you to take complete control over the behavior of the columns. |
| [State persistence](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/persist-state) | The Grid allows you to save the custom settings of the users and restore them after they log in again. |
| [Hierarchy](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/hierarchy) | The Grid provides options for visualizing the relations between parent and child records by displaying its table data in a hierarchical manner. |
| [Templates](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/templates/client-detail-template) | The abundance of templates allows you to customize the way the data is visualized in the table. |
| [Scroll modes](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/scrolling/overview) | The virtual scrolling and endless scrolling modes allow you to further enhance the user experience. |
| [Selection](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/selection) | The selection functionality and its various options allow the users to quickly manipulate the desired data. |
| [Stacked display mode](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/stacked-display-mode) | Displays Grid rows in a compact, card-like stacked arrangement with configurable column widths, ideal for limited horizontal space or mobile-friendly layouts. |
|  |  |
| [Toolbar](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/toolbar) | You can add command buttons to the toolbar and even define custom commands. |
| Rendering and styling | You can customize the appearance of the Grid by [configuring its rows](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/appearance/rows), initializing the Grid from a [hidden container](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/appearance/hidden-containers), using [adaptive rendering](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/appearance/adaptive), and setting its [height](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/appearance/height) and [width](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/appearance/width). |
| [Globalization](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/globalization/overview) | The Grid provides globalization through the combination of [localization](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/globalization/localization) with [internationalization](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/globalization/intl) and [right-to-left support](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/globalization/rtl-support). |
| [Accessibility](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/accessibility/overview) | The Grid is accessible for screen readers, supports WAI-ARIA attributes, and delivers [keyboard shortcuts](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/accessibility/keyboard-navigation) for faster navigation. |
| [AI Toolbar Assistant](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/smart-grid/ai-toolbar-tool) | The Grid provides a built-in AI Assistant toolbar tool that allows users to interact with the Grid using natural language prompts. |
| [Custom AI Column](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/smart-grid/custom-column-ai) | The Grid can be enhanced with a custom AI-powered column that provides personalized insights, summaries, and explanations for individual rows. |

[Next Steps](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/overview#next-steps)
------------------------------------------------------------------------------------------------------------------------

* [Getting Started with the Grid](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/getting-started-grid)

* [Basic Usage of the Grid HtmlHelper for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/grid/index)

* [Basic Usage of the Grid TagHelper for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/grid/tag-helper)

* [Grid in Razor Pages](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/binding/razor-page)

* [Using the API of the Grid for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/grid/api)

[See Also](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/grid/overview#see-also)
--------------------------------------------------------------------------------------------------------------------

* [ASP.NET Core DataGrid Homepage](https://www.telerik.com/aspnet-core-ui/grid)

* [Knowledge Base Section](https://www.telerik.com/aspnet-core-ui/documentation/knowledge-base)

* [Server-Side API](https://www.telerik.com/aspnet-core-ui/documentation/api/grid)

* [ASP.NET Core Grid example](https://demos.telerik.com/aspnet-core/grid)

* [Forum Discussions](https://www.telerik.com/forums/aspnet-core-ui?tagId=753)

* [How-To Examples](https://github.com/telerik/ui-for-aspnet-mvc-examples/tree/master/Telerik.Examples.Mvc/Telerik.Examples.Mvc/Areas)
