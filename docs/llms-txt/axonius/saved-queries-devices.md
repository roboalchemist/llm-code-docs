# Source: https://docs.axonius.com/docs/saved-queries-devices.md

# Saved Queries

Any query created on one of the asset pages, with either the Query Wizard or in [Basic mode](/docs/basic-query-mode), or by updating an existing query, can be saved. After you save it, it is added to the **Saved Queries** list and can be selected anywhere a query is used, such as in [Enforcement Sets](/docs/create-ec-set), [Dashboard Charts](/docs/working-with-custom-panels), [Reports](/docs/report-configuration-page), [Data Analytics](/docs/analyzing-query-data), and more.

## Saving a New Query

The Asset pages display the query name above the search bar along with the query status. The query status indicates whether this is a new query that is unsaved, or a saved query that has been edited.

When you save a query, the following information is saved:

* **Query filter** –  The collected assets together with their details according to the filter set.
* **Query view** – The columns that are displayed when you save the query are saved as part of the query and used to display the same “view” of selected fields in the table every time you use this query. Set the columns in **Edit Columns**.

<Callout icon="📘" theme="info">
  Note

  The “view” is saved as part of the saved query. It doesn’t impact the filtered asset data; only the data that is visible in the query results table.
</Callout>

**To save a query:**

1. After you create a query with either the Query Wizard or in [Basic mode](/docs/basic-query-mode), above the left-upper corner of the asset list, click **Save As**.

   ![QuerySaveAs.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QuerySaveAs.png)

   The **Save as a New Query** dialog opens.

2. In **Query name**, enter a unique name for the query.

3. In **Query description**, enter a description (optional).

   <Callout icon="❗️" theme="error">
     **Attention**

     HTML sanitization validation was added to saved query names and descriptions to prevent XSS attacks.

     Therefore, query names and descriptions can't contain `<` and `>` characters, or various patterns that contain URLs and some HTML tags.
   </Callout>

4. In **Tags**, choose a tag from the drop down list of tags available in the system or start typing to add a new tag. You can add as many tags as you need. When you add a new tag, click **Add  New** to add the tag to the system. Use **Clear All** to remove a tag you selected. Tags help organize your queries. You can add a tag to a query when you create the query, as well as  from the **Saved Queries** page. The list of tags used in queries is the same across the whole system. Tags are optional.

5. To create an Asset Scope query, enable **Asset scope query**. The query will be saved in the **Asset Scope Queries** folder and it can be used to create Data Scopes. If this option is enabled, the **Access** section is not displayed.

6. In [**Who has access**](/docs/who-has-access), configure the access privileges for the query.

7. In **Folder name**, select the folder where you want to save the query. The folders available depend on whether the query is private or public.
   * By default, public queries are saved in the folder of the current Data Scope.
   * Queries accessible to all Data Scopes are saved in the **Shared Queries** folder.
   * Private queries are saved in the **My Private Queries** folder.

8. Click **Save**.

<Callout icon="📘" theme="info">
  Note

  If you have written a query in AQL using terms or expressions not supported in the Query Wizard, when you save the query the system informs you that the system will save the query as an AQL expression.
</Callout>

## Running a Saved Query

Once a query is saved you can run it from the **<Anchor label="Queries" target="_blank" href="https://docs.axonius.com/docs/managing-queries">Queries</Anchor>** page, from the **Saved Query** drawer or  from the Saved Queries list in the Query Search Bar.

### Saved Queries List in the Query Search Bar

In an Asset page, click the Query Search bar. The drop-down list displays a list of saved queries and history of the queries run in Axonius.
To run a saved query, use the vertical scroll to select the saved query you want. Then click it to run the query.

![Search Saved Queries](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/SearchSavedQueries.png)

### Updating an Existing Saved Query

After you select a saved query, you can do the following:

* **Save As** - Save the query results as a new saved query.
  * **Update Query** - Select from the Saved As drop-down to update the saved query you are working on.
  * **Copy Query Link** - Select from the Saved As drop-down to copy the link to the query and then share it with others.
* **Reset** - Reset the page to its default column view and with no filtering, resulted in all devices/users being displayed.
* **Copy Query** - Generate a query URL. See [Sharing a Query Wizard Expression (URL)](#sharing-a-query-wizard-expression-url) below for more information.
* **EC Actions** - Use a quick Enforcement Action to add tags or custom fields to all assets returned by a query. In addition, you can create a case set from the EC Actions drop-down. See <Anchor label="Adding Tags to Query or Filter Results with a Quick Enforcement Action" target="_blank" href="https://docs.axonius.com/docs/working-with-tags#/adding-tags-to-query-or-filter-results-with-a-quick-enforcement-action">Adding Tags to Query or Filter Results with a Quick Enforcement Action</Anchor> and <Anchor label="Adding Custom Fields to Query or Filter Results with a Quick Enforcement Action" target="_blank" href="https://docs.axonius.com/docs/working-with-custom-data#/adding-custom-fields-to-query-or-filter-results-with-a-quick-enforcement-action">Adding Custom Fields to Query or Filter Results with a Quick Enforcement Action</Anchor> for more information.

![Update Saved Query screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/UpdateSavedQuery.png)

## Sharing a Query Wizard Expression (URL)

Another way to save a query is to generate a query URL. The generated link opens the Query Wizard with all the query details populated - assets, fields, data refinement, etc. The link acts as a temporary saved query and is available for 30 days.

**To generate a query URL**

1. Define a query using the Query Wizard and click **Search** to run it.
2. Click the **Copy Query** button above the asset table.

<Image align="left" alt="Copy Query Button" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/CopyQueryButton.png" />

3. A "Query Link copied to clipboard" message pops up.
4. To open the query URL, paste the copied link into the address bar and press **Enter**.
5. The Asset page that opens shows the results of the copied query.

## Accessing Saved Queries from the Assets Page

From each Assets page, you can access information regarding the saved queries run on this asset type. To get started, click the **Queries** button, located above the Assets page's search bar.

![QueriesButtonOnAssetsPage](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/queries%20direct%20access_1.png)

The **Queries** pane opens on the right and displays the **Recently Used Saved Queries**. Use the search bar to search for saved queries. You can also add a saved query to your Favorites for quick access.

Click a saved query to instantly run it on the Assets page.

![QueriesMenu](https://files.readme.io/47bc2c651d877c3d7b2645966fdc636e389cda896369a6f83ec2f867bf624993-image.png)