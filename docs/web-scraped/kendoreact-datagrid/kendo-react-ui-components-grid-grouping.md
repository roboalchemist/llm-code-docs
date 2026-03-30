# Source: https://www.telerik.com/kendo-react-ui/components/grid/grouping

Title: React Data Grid Grouping Basics - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/grouping

Published Time: Fri, 27 Feb 2026 12:51:43 GMT

Markdown Content:
[Grouping Basics Premium](https://www.telerik.com/kendo-react-ui/components/grid/grouping#grouping-basics)
----------------------------------------------------------------------------------------------------------

Updated

on Dec 19, 2025

The KendoReact Data Grid lets you display grouped table data.

![Image 1: ninja-icon](https://www.telerik.com/kendo-react-ui/components/static/d2ecd6c1a01f6b1598a481623b8f4389/start-free-trial-icon.inline.svg)The Grouping feature of the Grid is part of [KendoReact](https://www.telerik.com/kendo-react-ui) premium, an enterprise-grade UI library with 120+ [free](https://www.telerik.com/kendo-react-ui/components/free) and premium components for building polished, performant apps. Test-drive all features with a free 30-day trial.[Start Free Trial](https://www.telerik.com/try/kendo-react-ui)

[Enabling Grouping](https://www.telerik.com/kendo-react-ui/components/grid/grouping#enabling-grouping)
------------------------------------------------------------------------------------------------------

The KendoReact Grid supports grouping in two modes:

*   [Built-in State Management](https://www.telerik.com/kendo-react-ui/components/grid/grouping#using-the-built-in-state-management-for-grouping): The Grid manages its own grouping state internally.

*   [Controlled Mode](https://www.telerik.com/kendo-react-ui/components/grid/grouping#using-the-grouping-in-controlled-mode): You manage the grouping state externally by handling events and updating the state.

### [Using the Built-in State Management for Grouping](https://www.telerik.com/kendo-react-ui/components/grid/grouping#using-the-built-in-state-management-for-grouping)

To use grouping with the built-in state management, follow these steps:

1.   Enable the [`autoProcessData`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#autoprocessdata) prop to let the Grid handle grouping automatically.

2.   Set the [`groupable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#groupable) prop of the Grid to enable grouping features.

3.   Set the `dataItemKey` prop to a unique value field from the data in the Grid.

4.   (Optional) Set the [`defaultGroup`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#defaultgroup) prop to add initial grouping for the Grid.

The following example shows how to use grouping with the built-in state management of the KendoReact Grid.

Loading ...

### [Using the Grouping in Controlled Mode](https://www.telerik.com/kendo-react-ui/components/grid/grouping#using-the-grouping-in-controlled-mode)

To use grouping in the KendoReact Grid with controlled mode, follow these steps:

1.   Set the [`groupable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#groupable) and [`group`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#group) options of the Grid.
2.   Handle the [`onGroupChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ongroupchange) or the [`onDataStateChange`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ondatastatechange) event. The `onDataStateChange` event works best when the Grid has other data operations because it provides the complete [`dataState`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/state) in a single event.
3.   Group the data on the client by using the [`groupBy`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/groupby) or [`process`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/process) methods. You can also group data on the server by making a request using the event parameters. The Grid needs the grouped data as a collection of [`GroupResults`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/groupresult).

> Use the [`groupBy`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/groupby) method with the `onGroupChange` event, and the [`process`](https://www.telerik.com/kendo-react-ui/components/dataquery/api/process) method with the `onDataStateChange` event.

For more information, see the article on the [process helpers for bulk data operations](https://www.telerik.com/kendo-react-ui/components/dataquery#grouping).

Loading ...

[Grouping Columns Dynamically](https://www.telerik.com/kendo-react-ui/components/grid/grouping#grouping-columns-dynamically)
----------------------------------------------------------------------------------------------------------------------------

By default, you can group all columns of the Grid multiple times. To enable grouping of specific Grid columns and add dynamic grouping to a column, use a function or a variable for the [`groupable`](https://www.telerik.com/kendo-react-ui/components/grid/api/gridcolumnprops#groupable) property.

jsx

`<Column field="ProductID" filterable={false} title="ID" width="50px" groupable={isGroupable("ProductID")} />`

jsx

```
const [group, setGroup] = React.useState<GroupDescriptor[]>(initialGroup);

const isGroupable = (field) => {
    return !((group || []).find((g) => g.field === field));
}
```

[Persist Groups Collapsed State](https://www.telerik.com/kendo-react-ui/components/grid/grouping#persist-groups-collapsed-state)
--------------------------------------------------------------------------------------------------------------------------------

The `data-tools` package gives you utility methods to create unique group item IDs. You can use these IDs to save the group collapsed state.

Loading ...

[Expand and Collapse All Groups](https://www.telerik.com/kendo-react-ui/components/grid/grouping#expand-and-collapse-all-groups)
--------------------------------------------------------------------------------------------------------------------------------

The example below shows how to add a button that expands or collapses all groups in the Grid.

Loading ...

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/grouping#suggested-links)
--------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [GroupDescriptor](https://www.telerik.com/kendo-react-ui/components/dataquery/api/groupdescriptor)
*   [dataStateChange](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops#ondatastatechange)
*   [API Reference of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops)
*   [React Data Grid High-Level Overview](https://www.telerik.com/kendo-react-ui/grid)
