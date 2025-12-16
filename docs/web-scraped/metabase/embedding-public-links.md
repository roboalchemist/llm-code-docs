# Source: https://www.metabase.com/docs/latest/embedding/public-links

<div>

1.  [Home](/docs/latest/)
2.  [Embedding](/docs/latest/embedding/start)

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

# Public sharing

> Only admins can create public links and iframes.

Admins can create and share public links (URLs) for questions, dashboards, and documents. People can view them as standalone destinations (URLs) or as embedded iframes in another page or app. Public items display view-only results of your question, dashboard, or document, so visitors won't be able to drill down into the underlying data on their own.

## Create a public link for a question

![Create a public link for a question](./images/create-a-public-link.png)

To create a public link for a question, admins can click on the **Sharing** icon at the top right of a question and select **Create a public link**. Copy the link and test it out by viewing the link in a private/incognito browser session.

## Public link to export question results in CSV, XLSX, JSON

This export option is only available for questions, not dashboards.

To create a public link that people can use to download the results of a question:

1.  Click on the **Sharing** icon for the question.
2.  Select **Create a public link**.
3.  Click on the file format you want (below the **Public link** URL): CSV, XLSX, or JSON.

![Public export](./images/public-export.png)

Open the public link in a new tab to test the download.

## Create a public link for a dashboard

To share a dashboard via a public link, admins can click on the **Sharing** button in the top right menu.

![Sharing a dashboard](./images/dashboard-sharing.png)

To embed a dashboard, see [static embedding](./static-embedding).

## Create a public link for a document

To share a document via a public link, admins can click on the **Sharing** button in the top right menu and select **Create a public link**.

Public documents are read-only: viewers cannot edit the content or add comments. For charts embedded in the document, viewers can download the results in CSV, XLSX, or JSON format using the **Download results** option in the chart menu.

## Exporting raw, unformatted question results

To export the raw, unformatted rows, you'll need to append `?format_rows=false` to the URL Metabase generates. For example, if you create a public link for a CSV download, the URL would look like:

``` highlight
https://www.example.com/public/question/cf347ce0-90bb-4669-b73b-56c73edd10cb.csv?format_rows=false
```

By default, Metabase will export the results of a question that include any formatting you added (for example, if you formatted a column with floats to display as a percentage (0.42 -\> 42%)).

See docs for the [export format endpoint](/docs/latest/api#tag/public/GET/public/card/%7Buuid%7D/query/%7Bexport-format%7D).

## Simulating drill-through with public links

Metabase's automatic [drill-through](/learn/metabase-basics/querying-and-dashboards/questions/drill-through) won't work on public dashboards because public links don't give people access to your raw data.

You can simulate drill-through on a public dashboard by setting up a [custom click behavior](../dashboards/interactive) that sends people from one public link to another public link.

1.  Create a second dashboard to act as the destination dashboard.
2.  [Create a public link](#create-a-public-link-for-a-dashboard) for the destination dashboard.
3.  Copy the destination dashboard's public link.
4.  On your primary dashboard, create a [custom destination](../dashboards/interactive#custom-destinations) with type "URL".
5.  Set the custom destination to the destination dashboard's public link.
6.  Optional: pass a filter value from the primary dashboard to the destination dashboard by adding a query parameter to the end of the destination URL:

``` highlight
/public/dashboard/?child_filter_name=}
```

For example, if you have a primary public dashboard that displays **Invoices** data, you can pass the **Plan** name (on click) to a destination public dashboard that displays **Accounts** data:

![Public link with custom destination](./images/public-link-custom-destination.png)

## Public embeds

![Public embed](./images/public-embed.png)

If you want to embed your question or dashboard as an iframe in a simple web page or app:

1.  Click on the **Sharing** icon for your question or dashboard.
2.  Click **Embed**.
3.  In the bottom of the embedding popup, click on **Get embedding code**.
4.  Copy the iframe snippet Metabase generates for you.
5.  Paste the iframe snippet in your destination of choice.

To customize the appearance of your question or dashboard, you can update the link in the `src` attribute with [public embed parameters](#public-embed-parameters).

## Public embed parameters

To apply appearance or filter settings to your public embed, you can add parameters to the end of the link in your iframe's `src` attribute.

Note that it's possible to find the public link URL behind a public embed. If someone gets access to the public link URL, they can remove the parameters from the URL to view the original question or dashboard (that is, without any appearance or filter settings).

If you'd like to create a secure embed that prevents people from changing filter names or values, check out [static embedding](./static-embedding).

## Appearance parameters

To toggle appearance settings, add *hash* parameters to the end of the public link in your iframe's `src` attribute.

See [appearance parameters](./static-embedding-parameters#customizing-the-appearance-of-a-static-embed).

## Filter parameters

You can display a filtered view of your question or dashboard in a public embed. Make sure you've set up a [question filter](../questions/query-builder/filters) or [dashboard filter](../dashboards/filters) first.

To apply a filter to your embedded question or dashboard, add a *query* parameter to the end of the link in your iframe's `src` attribute, like this:

``` highlight
/dashboard/42?filter_name=value
```

For example, say that we have a dashboard with an "ID" filter. We can give this filter a value of 7:

``` highlight
/dashboard/42?id=7
```

To set the "ID" filter to a value of 7 *and* hide the "ID" filter widget from the public embed:

``` highlight
/dashboard/42?id=7#hide_parameters=id
```

To specify multiple values for filters, separate the values with ampersands (&), like this:

``` highlight
/dashboard/42?id=7&name=janet
```

You can hide multiple filter widgets by separating the filter names with commas, like this:

``` highlight
/dashboard/42#hide_parameters=id,customer_name
```

Note that the name of the filter in the URL should be specified in lower case, and with underscores instead of spaces. If your filter is called "Filter for User ZIP Code", you'd write:

``` highlight
/dashboard/42?filter_for_user_zip_code=02116
```

## Disable public sharing

Public sharing is enabled by default.

![Enable public sharing](./images/enable-public-sharing.png)

To disable public sharing:

1.  Click on the **Gear** icon in the upper right.
2.  Select **Admin settings**.
3.  In the **Settings** tab, select **Public sharing**.
4.  Toggle off **Public sharing**.

Once toggled on, the **Public sharing** section will display Metabase questions, dashboards, documents, and actions with active public links.

If you disable public sharing, then re-enable public sharing, all your previously generated public links will still work (as long as you didn't deactivate them).

## Deactivating public links and embeds

### Individual question or dashboard links and embeds

1.  Visit the question or dashboard.
2.  Click on **Sharing** icon.
3.  Select **Public link** or **Embed**.
4.  Click **Remove public link**.

## Deactivating multiple public links and embeds

Admins can view and deactivate all public links for a Metabase.

1.  Click on the **gear** icon in the upper right.
2.  Select **Admin settings**.
3.  Go to the **Settings** tab.
4.  Go to the **Public sharing** tab in the left sidebar.
5.  For each item you want to deactivate, click on the **X** to revoke its public link.

## See all publicly shared content

Admins can see all publicly shared questions, dashboards, documents, and actions in **Admin Settings \> Public Sharing**.

![See shared content](./images/see-shared-content.png)

## Further reading

-   [Publishing data visualizations to the web](/learn/metabase-basics/embedding/charts-and-dashboards).
-   [Customizing Metabase's appearance](../configuring-metabase/appearance).
-   [Embedding introduction](../embedding/start).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/embedding/public-links.md) ]