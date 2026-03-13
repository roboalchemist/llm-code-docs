# Source: https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export

Title: React Data Grid Exporting Excel Export - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export

Markdown Content:
[KendoReact Data Grid Excel Export Overview Premium](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#kendoreact-data-grid-excel-export-overview)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Dec 19, 2025

The KendoReact Data Grid provides you the option to export its data to excel by utilizing the KendoReact [Excel Export library](https://www.telerik.com/kendo-react-ui/components/excelexport).

![Image 1: ninja-icon](https://www.telerik.com/kendo-react-ui/components/static/d2ecd6c1a01f6b1598a481623b8f4389/start-free-trial-icon.inline.svg)The Excel Export feature of the Grid is part of [KendoReact](https://www.telerik.com/kendo-react-ui) premium, an enterprise-grade UI library with 120+ [free](https://www.telerik.com/kendo-react-ui/components/free) and premium components for building polished, performant apps. Test-drive all features with a free 30-day trial.[Start Free Trial](https://www.telerik.com/try/kendo-react-ui)

[The KendoReact Data Grid Excel Export in Action](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#the-kendoreact-data-grid-excel-export-in-action)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following example demonstrates the basic implementation of the Excel export functionality of the Grid.

[Getting Started with the KendoReact Data Grid Excel Export](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#getting-started-with-the-kendoreact-data-grid-excel-export)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To enable the Excel export:

1.   Install `kendo-react-excel-export` package.

sh `npm i @progress/kendo-react-excel-export` 
2.   Import the ExcelExport component in your React Application.

jsx `import { ExcelExport } from '@progress/kendo-react-excel-export';` 
3.   Wrap the Grid in the ExcelExport component and use the ExcelExport `save` function to export the Grid and save it to excel file.

[Configuration](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#configuration)
---------------------------------------------------------------------------------------------------------

You can entirely control the Excel export configuration through the arguments that are passed to the [`save`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexport#save) function of the KendoReact Excel Export component.

The ExcelExport enables you to:

*   [Wrap the Grid in an ExcelExport component](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#wrapping-the-grid)
*   [Pass the Grid columns to the ExcelExport component](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#passing-the-grid-columns)
*   [Export specific data](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#exporting-specific-data)
*   [Customize the exported columns of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#customizing-exported-columns)

### [Wrapping the Grid](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#wrapping-the-grid)

If the Grid is passed as a child to the ExcelExport and its columns are defined declaratively by using the `GridColumn` components, they will be automatically detected. You still need to pass the data of the Grid to the [`save`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexport#save) function or as a [`data`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexportprops#data) property to the ExcelExport component.

Loading ...

### [Passing the Grid Columns](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#passing-the-grid-columns)

The Grid exposes its columns through its [`columns`](https://www.telerik.com/kendo-react-ui/components/grid/api/grid#columns) field. To pass the Grid columns, pass its data and columns to the [`save`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexport#save) function of the ExcelExport component.

Loading ...

### [Exporting Specific Data](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#exporting-specific-data)

To export specific data, pass the data to the [`save`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexport#save) function of the ExcelExport component. For example, if the Grid has its paging enabled but you need to export all pages, pass the unprocessed data to the `save` function.

Loading ...

### [Customizing Exported Columns](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#customizing-exported-columns)

You can use the same data as the Grid and customize the exported columns. To export columns that are different from the current Grid columns, include the [`ExcelExportColumn`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexportcolumn) and [`ExcelExportColumnGroup`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexportcolumngroup) components as children to the ExcelExport.

Loading ...

[Known Limitations](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#known-limitations)
-----------------------------------------------------------------------------------------------------------------

*   During the export to Excel, the Grid does not use column formats. Column formats are incompatible with Excel. For more information, refer to the page on the [Excel-supported formats](https://support.office.com/en-us/article/Create-or-delete-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US).
*   The maximum size of the exported file to Excel has a system-specific limit. For large data sets, it is highly recommended that you use a server-side solution.
*   When you use the ExcelExport in older browsers, such as Internet Explorer 9 and Safari, you have to implement a server proxy using the [`proxyUrl`](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexportprops#proxyurl) property of the ExcelExport component. You can refer to [this KB article](https://www.telerik.com/kendo-react-ui/components/knowledge-base/pdfexport-setup-proxy/) for an example.

*   [API Reference of the Grid Component](https://www.telerik.com/kendo-react-ui/components/grid/api/grid)
*   [API Reference of the Excel Export Component](https://www.telerik.com/kendo-react-ui/components/excelexport/api/excelexport)

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export#suggested-links)
-------------------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [ExcelExport Overview](https://www.telerik.com/kendo-react-ui/components/excelexport)
*   [Export to Excel Grid Reordered Columns](https://www.telerik.com/kendo-react-ui/components/knowledge-base/excel-export-with-column-reorder/)
*   [Export Multiple Grids to Excel](https://www.telerik.com/kendo-react-ui/components/knowledge-base/export-to-excel-multiple-grids/)
*   [Export to Excel Both Parent and Child Grid Data](https://www.telerik.com/kendo-react-ui/components/knowledge-base/excel-export-of-both-parent-and-child-grid-data/)
*   [Export Data to Excel with Custom Header and Footer](https://www.telerik.com/kendo-react-ui/components/knowledge-base/excel-export-with-custom-header-footer/)
*   [Export Grid Data With Watermark](https://www.telerik.com/kendo-react-ui/components/knowledge-base/grid-pdf-export-watermark/)
