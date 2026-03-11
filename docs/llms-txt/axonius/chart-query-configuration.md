# Source: https://docs.axonius.com/docs/chart-query-configuration.md

# Chart Query Configuration

You can select an existing query, edit a query or create a new query directly from the chart. The actions you can do, depend on the permissions you have.

After selecting an asset module from the Module drop down, click in the Query field. In some of the charts this might have a slightly different name.

![SelectChartQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SelectChartQuery.png)

## Viewing and Editing a Query

When you choose a query, hover over the query list and click the View or Edit Query icon ![EditQueryIcon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditQueryIcon.png) to view the query details in a drawer. In this way you can make sure what it displays. If a query is based on one or more saved queries you can see the details of the saved query.

![QueryDrawerin chart.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryDrawerin%20chart.png)

Close the query drawer if you do not want to make any changes. If you click **Run Query**, the system opens the relevant asset page and runs the query.

You can edit queries which are not predefined. Click the Edit icon on the toolbar to edit the query. See [Query Wizard and Query Filter Bar](/docs/query-wizard-and-query-filter) to learn how to edit queries.

![EditQuery.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditQuery.png)

Click Duplicate ![DuplicateButton.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DuplicateButton.png) to duplicate a query and then edit it.
When you finish editing a query select **Save**.

## Creating a New Query

You can create a new query instead of using an existing saved query. This new query will be saved in the folder selected and can be accessed from the Folders pane of the [Queries page](/docs/managing-queries).

<Image align="center" border={false} width="400px" src="https://files.readme.io/04cb6a0dcd13f007e93a986638d46884e630a2801907548c236f15891ba1832c-New_query_screen-2025.png" />

<br />

<br />

**To create a new query**

1. At the bottom of the query list, click **+ Add Query**. The query drawer opens.

2. In **Name**, enter a name for the new query.

3. In **Description**, enter a description that includes what assets the query returns.

4. In **Tags**, add tags if necessary.

5. In **Cache Settings**, select whether to **Always keep cached** or deselect to not keep cached. When selected, query results are updated and stored in cache. This makes the query run faster.

<Callout icon="📘" theme="info">
  Note:

  This option only appears when the **Enable caching on recently used queries** option is enabled in the [Cache and Performance settings](https://docs.axonius.com/docs/configuring-cache-and-performance#cache-settings).
</Callout>

<br />

6. In **Query Expression**, select the query parameters. For more about using the Query Wizard, see [Creating Queries with the Query Wizard](/docs/query-wizard-and-query-filter).
7. In **Field Refinement**, click **Refine Data** to refine the query results, if required. This customizes the asset data displayed in the final table. Refer to <Anchor label="Refining the data displayed in table columns and rows" target="_blank" href="https://docs.axonius.com/docs/setting-page-columns-display#/refining-the-data-displayed-in-table-columns-and-rows">Refining the data displayed in table columns and rows</Anchor> for detailed instructions.
8. In [**Who has access**](/docs/who-has-access), configure the access privileges for the query.
9. In **Folder**, select the folder where the new query will be saved. Depending on the access configuration, the folder may be selected automatically.
10. To save the query, click **Save**. Click **Cancel** to close the Query Wizard page without saving any changes.

<br />