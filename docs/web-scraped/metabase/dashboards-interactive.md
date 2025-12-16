# Source: https://www.metabase.com/docs/latest/dashboards/interactive

<div>

1.  [Home](/docs/latest/)
2.  [Dashboards](/docs/latest/dashboards/start)

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

# Dashboard interactivity

You can customize what happens when people click on questions in your dashboard.

By default, when you create charts using Metabase's graphical query builder, your charts automatically come with [drill-through capabilities](/learn/metabase-basics/querying-and-dashboards/questions/drill-through), which let folks click on a chart to explore further. But if you have a more customized click path in mind, Metabase allows you to customize what happens when a user clicks on a chart or table in your dashboard.

You can set up a dashboard card to:

-   Send the user to a [custom destination](#custom-destinations): a dashboard, question, or custom URL.
-   [Update a dashboard filter](#use-a-chart-to-filter-a-dashboard).

To configure this interactivity, you'll use the **click behavior** option on a dashboard card.

## Customizing click behavior

From your dashboard, first click on the **pencil** icon to enter dashboard edit mode.

If you hover over the card that contains question you want to customize, Metabase will display a menu at the top right of that card containing these options, from left to right:

-   **Visualization options**: This icon looks like a painter's palette.
-   **Click behavior**: This is the icon with the mouse cursor clicking on a card.
-   **Add series**: If your question has a visualization to which you can add an [additional series](./multiple-series) (like a line or bar chart), you'll see this icon as a **+** next to a small representation of that chart type. Not all cards will show this option.
-   **Remove**: This icon is an **X**. Selecting this will remove your question from the dashboard.

Select the **Click behavior** option.

![Click behavior icon](./images/click-behavior-icon.png)

Metabase will slide out the **Click behavior sidebar**:

![Click behavior menu](./images/click-behavior-menu.png)

For questions composed using the query builder, you can select from three options:

-   Open the Metabase drill-through menu.
-   Go to a custom destination.
-   Update a dashboard filter (if the dashboard has a filter).

SQL questions will only have the option to **Go to a custom destination**, and **Update a dashboard filter**.

If your dashboard has a filter, you'll also see an option to [update the filter](#use-a-chart-to-filter-a-dashboard).

## Open the drill-through menu

For questions composed using the query builder, the default click behavior is to open the **drill-through menu**, which presents people with the option to [drill through the data](/learn/metabase-basics/querying-and-dashboards/questions/drill-through):

![Drill-through menu](./images/drill-through-menu.png)

## Custom destinations

You can set custom destinations for all questions, including SQL questions.

![Custom destinations](./images/custom-destination.png)

Possible destinations include:

-   Dashboards
-   Saved questions
-   URLs

Internal Metabase destinations (dashboards or saved questions) will load in the same browser tab or window. External URLs will open in a new tab or window.

## Passing values to the destination

If you're linking to a dashboard or a SQL question that has filters, you can pass values from the current dashboard to filters in the destination.

For example, if you link to a dashboard that has a filter for `Category`, you can pass a value for `Category` from the origin question to the destination dashboard:

![Pass value to dashboard](./images/pass-value.png)

Once you select the column that contains the value you want to pass, the sidebar will display the column used to pass the value, as well as the target filter at the destination that Metabase will pass the value to:

![Pass category to filter](./images/pass-category-to-filter.png)

In the example above, when a user clicks on the **Orders by product category** card, Metabase will pass the clicked `Product -> Category` to the destination dashboard ("Interactive Dashboard"), which will then filter its cards by that `Category`.

You can also send the currently selected value of a dashboard filter on the current dashboard to the destination. In [some plans](/pricing/), you can pass a user attribute provided by SSO to the destination, too. Those user attributes will show up as options when you click on one of the destination's filters (provided the values are compatible with that filter).

When displaying questions as tables, you can select different click behaviors for different columns in the table. You can also modify the contents of the cells in a given column, replacing the value with custom text. For example, if you had a column that listed categories, you could change the text in the cell to read: "Click for details about }", where `Category` is the name of your column.

You can also use values to construct URLs to external resources.

![Enter a URL](./images/enter-a-url.png)

From the **Click behavior** sidebar, select **Go to a custom destination** and link to **URL**. The **Enter a URL to link to** modal will pop up, allowing you to specify a URL, as well as a column or dashboard filter.

What we need to do here is to type in the full URL of where a user should go when they click on a value in a card. But the really powerful thing we can do is to include variables in the URL. These variables will insert the value that the user clicks on into the URL.

For example, we could type a URL like this:

``` highlight
https://www.metabase.com/search.html?query=}
```

The important part is the `}` bit. What we're doing here is referring to the `Category` that the user clicked on. So if someone clicks on the `Widget` bar in our chart, the value of the `Category` column for that bar (`Widget`) would be inserted into our URL: `https://www.metabase.com/search.html?query=Widget`. Your URL can use as many column variables as you want - you can even refer to the same column multiple times in different parts of the URL. To see which variables you can include in the URL, click on the dropdown menu **Values you can reference**.

Next we'll click **Done**, then **Save** our dashboard. Now when we click our chart, we'll be taken to the URL that we entered above, with the value of the clicked bar inserted into the URL.

To learn more, check out [Custom destinations: choose what happens when people click on charts in your dashboard](/learn/metabase-basics/querying-and-dashboards/dashboards/custom-destinations).

## Use a chart to filter a dashboard

If your dashboard contains at least one filter, you can set things up so that clicking on a chart in the dashboard will update a filter.

When a user clicks on, say, a bar in a bar chart, you could send the value of the clicked bar to the filter, and update cards across the dashboard. We call this functionality **cross-filtering**. You can use this cross-filtering to make a chart behave as kind of "navigation question" that filters data across other cards.

For example, clicking on the `Widget` bar will update the current dashboard's **category** filter to filter for `Widget`:

![Cross-filtering](./images/cross-filter.png)

To set up cross-filtering, choose a dashboard filter that you'd like to update on click, and a question to use to update that filter. You can think of this question as your "navigation question." Instead of wiring this navigation question up to the filter, you'll [wire up every other question on the dashboard to the filter](./filters).

Below, we'll use the **Orders by product category question** as our navigation question, so we'll leave this question disconnected from the filter, and connect all the other questions to the **Category** filter.

![Wiring up filter](./images/wiring-up-filter.png)

With your filter wired up, stay in dashboard edit mode, and hover over the question you want to use as your navigation question to filter the dashboard. Click on the **click behavior** icon, then select the **Update a dashboard filter**.

Metabase will list the filters you can update. Here we select the **Category** filter, and supply the value to that filter from the question's `Product -> Category` column.

![Update a dashboard filter](./images/update-a-dashboard-filter.png)

Click **Done** in the sidebar, then **Save** your dashboard.

Now we can use our navigation question (Orders by product category) to interactively filter the data across your dashboard. When people click on a value in the navigation question, Metabase will send the clicked value to the filter, and update every card on the dashboard by filtering them for the clicked value - every card except for the navigation question: Orders by product category. The reason we don't want the navigation question to update is so that we can click on other bars to update the filter with a different value.

To learn more, check out [Cross-filtering: using a chart to update a dashboard filter](/learn/metabase-basics/querying-and-dashboards/dashboards/cross-filtering).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/dashboards/interactive.md) ]