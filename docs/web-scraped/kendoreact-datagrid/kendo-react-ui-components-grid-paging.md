# Source: https://www.telerik.com/kendo-react-ui/components/grid/paging

Title: React Data Grid Paging Overview - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/paging

Markdown Content:
New to KendoReact?[Learn about KendoReact Free.](https://www.telerik.com/kendo-react-ui/components/free)

Updated

on Dec 19, 2025

The KendoReact Data Grid provides a flexible paging mechanism that enables users to navigate large datasets efficiently. The built-in pager allows for numeric and input-based navigation, as well as customizable paging components.

[Getting Started with the KendoReact Data Grid Paging](https://www.telerik.com/kendo-react-ui/components/grid/paging#getting-started-with-the-kendoreact-data-grid-paging)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pagination is enabled in the Grid by setting the `pageable` property. This adds navigation controls to the bottom of the Grid, allowing users to move between pages.

[Enabling Paging](https://www.telerik.com/kendo-react-ui/components/grid/paging#enabling-paging)
------------------------------------------------------------------------------------------------

The KendoReact Grid supports paging in two modes:

*   [Built-in State Management](https://www.telerik.com/kendo-react-ui/components/grid/paging#using-the-built-in-state-management-for-paging): The Grid manages its own paging state internally.

*   [Controlled Mode](https://www.telerik.com/kendo-react-ui/components/grid/paging#using-the-paging-in-controlled-mode): The paging state is externally managed by handling events and updating the state accordingly.

[Using the Built-in State Management for Paging](https://www.telerik.com/kendo-react-ui/components/grid/paging#using-the-built-in-state-management-for-paging)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

To enable basic numeric paging using the built-in state management mechanism, follow these steps:

1.   Enable the [`autoProcessData`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#autoprocessdata) prop to allow the Grid to handle paging automatically.
2.   Set the [`pageable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable) prop of the Grid to enable pagination.
3.   Set the [`defaultTake`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaulttake) prop to define the number of items rendered initially.
4.   Use the [`defaultSkip`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultskip) prop to specify the number of items to be skipped initially, determining the starting page.

The following example demonstrates how to implement numeric paging using the built-in state management of the KendoReact Grid.

Loading ...

[Using the Paging in Controlled Mode](https://www.telerik.com/kendo-react-ui/components/grid/paging#using-the-paging-in-controlled-mode)
----------------------------------------------------------------------------------------------------------------------------------------

To enable numeric paging in the KendoReact Grid and use it in controlled mode, follow these steps:

1.   Set the [`pageable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable) prop of the Grid to enable paging.
2.   Use the [`skip`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#skip) prop used to track the current page.
3.   Set the [`pageSize`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pagesize) or the [`take`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#take) options of the Grid to specify how many items will be rendered on the page.
4.   Use the [`total`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#total) prop to notify the Grid how many records are in total, which is needed to calculate the correct total pages.
5.   Handle the [`onPageChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onpagechange) or the [`onDataStateChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ondatastatechange) event of the Gridfor managing the paging [`state`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/state).
6.   Use the [`slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) method or the built-in [`process`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/process) method to manage paging logic.

The following example demonstrates how to implement basic numeric paging in controlled mode.

Loading ...

The Grid supports different pager types:

*   [Numeric](https://www.telerik.com/kendo-react-ui/components/grid/paging/basic-paging)—Renders buttons with numbers.
*   [Input (responsive)](https://www.telerik.com/kendo-react-ui/components/grid/paging/basic-paging#responsive-pager)—Renders an input field for typing the page number.
*   [Custom Pager](https://www.telerik.com/kendo-react-ui/components/grid/paging/custom-paging)—Allows you to change entirely the Pager rendering.

The `PagerSettings` object has the following fields:

*   [`buttonCount`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable)—Sets the maximum numeric buttons count before the buttons are collapsed.
*   [`info`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable)—Toggles the information about the current page and the total number of records.
*   [`type`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable)—Accepts the `numeric` (buttons with numbers) and `input` (input for typing the page number) values.
*   [`pageSizes`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable)—Shows a menu for selecting the page size.
*   [`previousNext`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable)—Toggles the **Previous** and **Next** buttons.

To set the pager types, pass the [`PagerSettings`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridpagersettings) object to the [`pageable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#pageable) option of the Grid.

Loading ...

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/paging#suggested-links)
------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [React Data Grid High-Level Overview](https://www.telerik.com/kendo-react-ui/grid)
*   [Numeric Paging](https://www.telerik.com/kendo-react-ui/components/grid/paging/basic-paging)
*   [Custom Paging](https://www.telerik.com/kendo-react-ui/components/grid/paging/custom-paging)
