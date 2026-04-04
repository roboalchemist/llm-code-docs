# Source: https://www.telerik.com/kendo-react-ui/components/grid/sorting

Title: React Data Grid Sorting Overview - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/sorting

Markdown Content:
[KendoReact Data Grid Single-column Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting#kendoreact-data-grid-single-column-sorting)
-------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Dec 19, 2025

The KendoReact Data Grid provides powerful sorting capabilities that allow users to organize and analyze data effectively. Sorting can be applied to a single column or multiple columns simultaneously, depending on the application’s requirements.

Use React Sorting for Free You can use the free components from the React Sorting package in production—no sign-up or license required. Sorting is part of KendoReact, an enterprise-grade UI library with 120+ [free](https://www.telerik.com/kendo-react-ui/components/free) and premium components. To test-drive premium components, [start a 30-day trial](https://www.telerik.com/try/kendo-react-ui).

[Basics of Sorting in the KendoReact Data Grid](https://www.telerik.com/kendo-react-ui/components/grid/sorting#basics-of-sorting-in-the-kendoreact-data-grid)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Sorting in the Grid is enabled through the sortable property. When sorting is enabled, users can click on column headers to sort data in ascending or descending order. Additional customization options allow for multi-column sorting and custom sorting logic in either one of the following modes:

*   [Built-in State Management](https://www.telerik.com/kendo-react-ui/components/grid/sorting#using-the-built-in-state-management-for-sorting): The Grid manages its own sorting state internally.

*   [Controlled Mode](https://www.telerik.com/kendo-react-ui/components/grid/sorting#using-the-sorting-in-controlled-mode): The sorting state is externally managed by handling events and updating the state accordingly.

### [Features of Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting#features-of-sorting)

*   [Single-column Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting#single-column-sorting)—Users can sort data by one column at a time, with an option to unsort.
*   [Multiple-column Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting#multiple-solumn-sorting)—Allows sorting by multiple columns, defining sorting priorities.
*   **Custom Sorting Logic**—Developers can implement [custom compare functions](https://www.telerik.com/kendo-react-ui/components/grid/sorting#customizing-the-sort-compare-function)
*   [Reversing Sorting Order](https://www.telerik.com/kendo-react-ui/components/grid/sorting#reversing-sorting-order)—Allows you to prioritize the last sorted column.
*   **Client-side and Server-side Sorting**—allows you to handle the sorting on the client for fast updates or processed on the server for larger datasets.

You can also enable the unsorting of columns by utilizing the `sortable.allowUnsort` option.

Loading ...

[Using the Built-in State Management for Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting#using-the-built-in-state-management-for-sorting)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

To enable sorting in the KendoReact Grid and utilize its built-in state management, follow these steps:

1.   Enable the [`autoProcessData`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#autoprocessdata) prop to allow the Grid to handle the updated state automatically.
2.   Set the [`sortable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#sortable) prop of the Grid to enable sorting.
3.   Set the [`defaultSort`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultsort) prop to define the initial sorting.

The following example demonstrates how to use sorting handled by the built-in state management of the KendoReact Grid.

Loading ...

[Using the Sorting in Controlled Mode](https://www.telerik.com/kendo-react-ui/components/grid/sorting#using-the-sorting-in-controlled-mode)
-------------------------------------------------------------------------------------------------------------------------------------------

To enable sorting in the KendoReact Grid and use it in controlled mode, follow these steps:

1.   Set the [`sortable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#sortable) option of the Grid and set its `mode` prop to `single`.
2.   Set the [`field`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridcellprops#field) option of the Grid column.
3.   Utilize the [`sort`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#sort) option to apply the sorting styles and buttons to the affected columns.
4.   Handle the [`onSortChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#onsortchange) or the [`onDataStateChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ondatastatechange) event of the Grid. The `onDataStateChange` event is recommended when the Grid will have other data operations as it provides the complete [`dataState`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/state) in a single event.
5.   Sort the data on the client by using our built-in methods [`orderBy`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/orderby) or [`process`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/process). The data can also be sorted on the server by making a request using the event parameters.

> The [`orderBy`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/orderby) method is recommended when using the `onSortChange` event and the [`process`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/process) method is recommended when using the `onDataStateChange` event.

The following example demonstrates the minimum required configuration for single column sorting the Grid records.

Loading ...

[Single-column Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting#single-column-sorting)
-------------------------------------------------------------------------------------------------------------

Single-column sorting allows users to sort records by clicking on a column header. Clicking repeatedly cycles through ascending, descending, and unsorted states if enabled.

Learn more about enabling and customizing single-column sorting: [Single-column Sorting Guide](https://www.telerik.com/kendo-react-ui/components/grid/sorting/single-sorting)

[Multiple-column Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting#multiple-column-sorting)
-----------------------------------------------------------------------------------------------------------------

Multiple-column sorting lets users define a sorting hierarchy by sorting several columns at once. The order of sorting can be adjusted to prioritize certain columns.

Explore multiple-column sorting options: [Multiple-column Sorting Guide](https://www.telerik.com/kendo-react-ui/components/grid/sorting/multi-sorting)

[Customizing the Sort Compare Function](https://www.telerik.com/kendo-react-ui/components/grid/sorting#customizing-the-sort-compare-function)
---------------------------------------------------------------------------------------------------------------------------------------------

The `SortDescriptor` allows setting custom `compare` function for providing custom sorting logic. In the context of the Grid, the `onSortChange` or `onDataStateChange` events can be handled for finding the SortDescriptor for specific field and adding the custom sort compare function.

The following example demonstrates how to add custom compare function to `version` field within the `onDataStateChange` event of the Grid:

Loading ...

[Reversing Sorting Order](https://www.telerik.com/kendo-react-ui/components/grid/sorting#reversing-sorting-order)
-----------------------------------------------------------------------------------------------------------------

The Grid allows you to reverse the sorting order of its columns. To apply higher priority to the last sorted column, place it at the beginning of the sorting array before setting the new state. When a column is removed from the sorting state, you do not have to reverse the items.

jsx

```
sortChange(event: GridSortChangeEvent) {
    const sort = event.sort;
    if (sort.length >= state.sort.length) {
        sort.unshift(sort.pop());
    }
    setState({
        products: GetProducts(sort),
        sort: sort
    });
}
```

*   [API Reference of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops)
*   [API Index of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/api)

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/sorting#suggested-links)
-------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [Data Query Overview](https://www.telerik.com/kendo-react-ui/components/dataquery)
*   [React Data Grid High-Level Overview](https://www.telerik.com/kendo-react-ui/grid)
