# Source: https://docs.datadoghq.com/actions/app_builder/components/tables.md

---
title: Tables
description: >-
  Advanced table component features including client-side filtering, server-side
  filtering, loading indicators, and dynamic values.
breadcrumbs: Docs > App Builder > Components > Tables
source_url: https://docs.datadoghq.com/app_builder/components/tables/index.html
---

# Tables

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

This page describes advanced features you can use to manipulate table components in your App Builder apps.

## Client-side filtering{% #client-side-filtering %}

When you have a full list of items already and you want to filter them, there are multiple methods to do so on the client side.

### Column filtering{% #column-filtering %}

Under **Columns**, expand a column and enable the **Filterable** option to allow users to filter by entries in that column. When enabled, a drop-down menu appears in the table header which allows the user to select an item from that column to filter on.

### Filter by date range{% #filter-by-date-range %}

To allow date range filtering, under **Appearance**, enable the **Has Date Range Filter** option and select a data path to filter by. When enabled, a drop-down menu appears in the table header which allows the user to select a time span to filter by.

### Filter with search{% #filter-with-search %}

To add a search bar to your table, under **Appearance**, enable the **Is Searchable** option.

### Filter a table with a text input or search component{% #filter-a-table-with-a-text-input-or-search-component %}

One common use case is filtering a table component using the value in a text input component.

For example, if you want to list your dashboards in a table that you can filter using a text input component, you could do the following:

1. Add a new query using the **+** button.

1. Search for "list dashboards" and click the **List Dashboards** action. Name your query `listDashboards0`.

1. Add a text input or search component to your app. Name it `searchInput`.

1. Add a table component.

1. Set the table's **data source** property to your data filtered by the text input or search component that you created. In this example, set the **data source** to the following expression:

   ```
   ${listDashboards0?.outputs.dashboards.filter(row => row.title.includes(searchInput.value))}
   ```

You can type text into the text input component and the rows of table are filtered by that text.

### Filter a table with a select component{% #filter-a-table-with-a-select-component %}

Another common use case is filtering a table using a select component.

For example, if you want to list your dashboards in a table that you can filter using a select component, you could do the following:

1. Add a new query using the **+** button.

1. Search for "list dashboards" and click the **List Dashboards** action. Name your query `listDashboards0`.

1. Add a select component to your app. Name it `selectInput`.

1. Add a table component.

1. Set the table's **data source** property to your data filtered by the select component. In this example, set **data source** to the following expression:

   ```
   ${listDashboards0?.outputs.dashboards.filter(row => row.title.includes(selectInput.value))}
   ```

You can select a value from the select component and the rows of table are filtered by that value.

### Filter query results using a post-query transformation{% #filter-query-results-using-a-post-query-transformation %}

If you want to filter the results of a query itself, then use those results in your table, perform the following steps:

1. Add a new query using the **+** button.

1. Search for "list dashboards" and click the **List Dashboards** action. Name your query `listDashboards0`.

1. Add a text input or search component to your app. Name it `searchInput`.

1. Add a table component and set its **data source** property to the query that you added.

1. Expand the **Advanced** section of the query and find **Post-query Transformation**.

1. Replace `return outputs` with the following line:

   ```
   outputs.dashboards.filter(row => row.title.includes(searchInput.value))
   ```

You can type text into the text input component and the rows of table are filtered by that text.

If you need the original, untransformed query result, you can reference it as `${listDashboards0.rawOutputs}`.

## Server-side filtering{% #server-side-filtering %}

In some cases, you might want to filter values server-side and issue new requests when the user enters a value in an input such as a text input component.

In this case, you can enable server-side filtering by editing the query directly.

For example, in the [GitHub PR pipeline](https://app.datadoghq.com/app-builder/apps/edit?activeTab=queries&showActionCatalog=false&template=github-pr-dashboard&viewMode=preview) blueprint, the `listOpenedPulls` query has an input that gets the following URL:

```
https://api.github.com/search/issues?q=org:${organizationInput.value}+author:${userNameInput.value}+type:pr+state:open
```

The GitHub API accepts query parameters for filtering based on organization, author, or pull request type. The preceding query input URL contains template expressions for `organizationInput.value`, which is the value of the "Organization" text input component, and `userNameInput.value`, which is the value of the "Username" text input component. If you set the query run settings to auto, the query automatically refreshes when these template expression values change, and the table values update.

## Showing a loading indicator{% #showing-a-loading-indicator %}

If you want to show a loading indicator on a table while the data is being fetched, you can set the *table's* `isLoading` value equal to the *query's* `isLoading` property. For example:

1. Follow the steps in [filtering with a text input](https://docs.datadoghq.com/service_management/app_builder/components/tables/#filtering-with-a-text-input).

1. In the properties of your table, under **Appearance**, click the **</>** next to **Is Loading** to open the code editor.

1. Set the table's `isLoading` value to the following expression:

   ```
   ${listDashboards0.isLoading}
   ```

The table shows a loading indicator when you type new text into the text input component.

## Dynamic table values{% #dynamic-table-values %}

You can use the **data source** property of a table component to dynamically fill table values and constrain which objects are pulled into the table as columns.

For example, the [GitHub PR Summarizer](https://app.datadoghq.com/app-builder/apps/edit?viewMode=edit&template=github-pr-summarizer) blueprint uses a series of GitHub queries to summarize a list of pull requests in a repository. The query uses the data source entry below to constrain the table to 6 columns: `title`,`Summary`,`updated_at`,`user`,`html_url`, and `state`. The highlighted code dynamically populates the user column for each pull request with the author's avatar and GitHub username.

```js
${(() => {
    const summaryById = Object.fromEntries(
        summarizePulls.outputs.map(({id, summary}) => [id, summary])
    );
    return listPulls.outputs.map(result => {
        const {title, updated_at, user, state, html_url} = result;
        const updatedAt = new Date(result.updated_at);
        let summary;
        if (summarizePulls.isLoading) {
            summary = 'Summarizing';
        } else {
            summary = summaryById[result.id] ?? 'N/A';
        }
        return {
            title: `**${title}**`,
            updated_at: updatedAt.toLocaleString(),
            user: {label: user.login, src: user.avatar_url},
            summary,
            state, html_url};
    })
})()}
```

In the table, the **User** column fills with an avatar and GitHub username for each PR author.

## Further reading{% #further-reading %}

- [Components](https://docs.datadoghq.com/service_management/app_builder/components/)
- [Build Apps](https://docs.datadoghq.com/service_management/app_builder/build/)

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
