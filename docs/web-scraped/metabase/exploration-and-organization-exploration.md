# Source: https://www.metabase.com/docs/latest/exploration-and-organization/exploration

<div>

1.  [Home](/docs/latest/)
2.  [Exploration and Organization](/docs/latest/exploration-and-organization/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Basic exploration

## See what your teammates have made

As long as you're not the first user in your team's Metabase, the easiest way to start exploring your data is by looking at dashboards, charts, and lists that your teammates have already created. The best place to start is by checking out any dashboards that might be pinned on your home page, or in [collections](./collections) you have access to.

## Command palette

The command palette lets you create new things, search your content, or jump to anywhere in your Metabase.

To bring up the command palette, hit cmd/ctrl + k. That's `cmd + k` for Macs, or `ctrl + k` for Windows PCs.

You can use the command palette to:

-   Create new things (like new questions and dashboards)
-   Find things (saved questions, dashboards, models, etc.)
-   Find and jump to Admin and account settings.

So anytime you want to do or find anything in Metabase, just hit `cmd/ctrl + k` and start typing what you want to do.

> The command palette is currently unavailable in [Embedded analytics JS](../embedding/embedded-analytics-js) and [interactive embedding](../embedding/interactive-embedding) contexts.

## Advanced search

To filter your search results, hit `cmd/ctrl + k` to bring up the command palette and enter your search term. The first result is a link to "Search and filter all X results".

![Search results](./images/search-results.png)

Searches consider items' titles, descriptions, and other metadata --- you can even search the contents of your SQL queries. For example, you can search for things like `SELECT escape_pod FROM mothership` and find that one question you worked on six months ago. The results will display which collection each item is saved in, what kind of object it is, and whether it's pinned. Note that you'll only ever see items in that are in collections you have permission to view.

You can search by:

-   **Content type**: dashboard, question, model, collection, database, table.
-   **Creator**: who made the thing.
-   **Last editor**: who made the last saved change on the thing.
-   **Creation date**: when the thing entered our universe.
-   **Last edit date**: when someone last cared enough to update the thing.
-   **Verified items only**. Only show items that [have been verified](./content-verification).
-   **Search the contents of native queries**: search through the SQL/native code in questions.
-   **Search items in trash**: include the depths of oblivion in your search.

## Browse your databases

> Whether a group has access to the database browser depends on the group's [Create queries permission](../permissions/data#create-queries-permissions).

![Browse databases](./images/browse-data.png)

The left sidebar lists your databases, [models](../data-modeling/models), and [metrics](../data-modeling/metrics).

[Pro](/product/pro) and [Enterprise](/product/enterprise) plans include the ability to filter for [verified models and metrics](./content-verification).

The database browser will list all the databases connected to your Metabase. Hover over a table and click on the **bolt** icon to [X-ray](x-rays) the table, or click on the **book** icon to view more info about the table: its fields and their descriptions (if any), what questions are based on that table, and more.

To learn more, see [Exploring data with Metabase's data browser](/learn/metabase-basics/querying-and-dashboards/data-browser).

## Exploring collections

[Collections](./collections) in Metabase are a lot like folders. They're where Metabase keeps all your team's dashboards and charts.

![A collection](./images/collection-detail.png)

Your teammates might have pinned some items to the top of your collection.

-   [dashboards](../dashboards/introduction)
-   [models](../data-modeling/models)
-   [metrics](../data-modeling/metrics)
-   [questions](../questions/start)

Collections have a list of any other items that are saved within them, and you can see what other collections are saved inside of the current one by checking out the navigation sidebar.

## Exploring dashboards

[Dashboards](../dashboards/start) are a set of questions and text cards that you want to be able to refer to regularly.

If you click on a part of a chart, such as a bar in a bar chart, or a dot on a line chart, you'll see the **Action menu**, with actions you can take to dive deeper into that result, branch off from it in a different direction, or see automatic insights to [X-ray](x-rays) the data.

![Drill-through menu](images/automatic-insights.png)

In this example of orders by product category per month, clicking on a data point on this line chart gives us the ability to:

-   **See these Orders**: See a list of the orders for a particular month.
-   **See this month by week**.
-   **Break out by ...**: See things like the Gizmo orders in June 2023 broken out by the status of the customer (e.g., `new` or `VIP`). Different charts will have different breakout options, such as **Location** and **Time**.
-   **Automatic insights**: See orders for a particular category over a shorter time range.
-   **Filter by this value**: update the chart based on the value you clicked: equal to, less than, greater than, or not equal to.

> Note that while charts created with SQL currently only have [limited drill-through menu](../questions/native-editor/writing-sql#drill-though-in-sql-questions), you can add SQL questions to a dashboard and customize their click behavior. You can send people to a [custom destination](/learn/metabase-basics/querying-and-dashboards/dashboards/custom-destinations) (like another dashboard or an external URL), or have the clicked value [update a dashboard filter](/learn/metabase-basics/querying-and-dashboards/dashboards/cross-filtering).

Clicking on a table cell will often allow you to filter the results using a comparison operator, like =, \>, or \<. For example, you can click on a table cell, and select the less than operator `<` to filter for values that are less than the selected value.

![Comparison operator filters](images/comparison-operator-filters.png)

Lastly, clicking on the ID of an item in a table gives you the option to go to a [detail view](#view-details-of-a-record) for that single record. For example, you can click on a customer's ID to see the profile view for that customer.

![Detail view](images/detail-view.png)

When you add questions to a dashboard, you can have even more control over what happens when people click on your chart. In addition to the default drill-through menu, you can add a [custom destination](/learn/metabase-basics/querying-and-dashboards/dashboards/custom-destinations) or [update a filter](/learn/metabase-basics/querying-and-dashboards/dashboards/cross-filtering). Check out [interactive dashboards](../dashboards/interactive).

## View details of a record

To see the details of an individual record when viewing unaggregated tables, click on a record and select "View details."

To expand the details sidebar to a full page, click "Open in full page". Every record has a dedicated details page which you can link to.

Admins and people with [table metadata permissions](../permissions/data#manage-table-metadata-permissions) can set specific fields to display only in this details view. See [Table metadata](../data-modeling/metadata-editing).

If your record has a field containing [an image link](../data-modeling/formatting), Metabase will show the image as the record's icon in the detail view. If the record has a field with the "Entity name" name semantic type, or a field called `Title` or `Name` , Metabase will show this field as the name of the record.

## Bookmarks

**Bookmarks** are a way to quickly get back to things you visit frequently (or have been working on recently). Bookmarked items show up in the main navigation sidebar above [collections](./collections).

To bookmark an item, look for the **ribbon** icon in the upper right corner of the item's page. You can bookmark:

-   Questions
-   Models
-   Dashboards
-   Collections

To add or remove a bookmark from an item, click on the three-dot menu (**...**) next to the item in the collection.

Some things to remember with bookmarks:

-   Bookmarks are personal; other people can't see your bookmarks. If you want to highlight something for everyone, you'll want to put it in an official collection and/or pin the item in the collection (see [collections](./collections)).
-   If you end up bookmarking a lot of items, you can collapse the bookmarks section in the sidebar (or remove the bookmarks that are just getting in your way).
-   Items that you bookmark will get a boost in your search results (but not the search results of other people).
-   To reorder bookmarks, simply drag and drop them in the sidebar.

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/exploration-and-organization/exploration.md) ]