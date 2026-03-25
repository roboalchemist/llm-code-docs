# Source: https://docs.axonius.com/docs/searching-for-assets.md

# Global Search

**Axonius Global Search** is a quick, direct way to allocate assets and run queries, without the need to navigate to their dedicated pages first.

To get started, click the search bar at the top of each Axonius page, or type Ctrl + Y for shortcut.

<Image border={false} src="https://files.readme.io/ed7ee6d58ba60b21320f992738c21129dacdeda45df07a0fe75efa7590adc341-image.png" />

Upon entering some free text (at least three characters) into the search bar, the search runs on all asset types and queries, and a list of results appears instantly.

The **Search Axonius** dialog contains two sections: **Recently Searched** results and **Recently Viewed** results. If this is your first search ever, those sections are empty.

<Image align="center" alt="SearchAxoniusDialog" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ESMRMED8.png" />

The search results are displayed in two tabs: **Assets** and **Queries**.

### Searching for Assets

The **Assets** tab shows which asset types were found by the string you typed and how many assets were found in total. Use the **Asset type** dropdown to filter results by a specific asset type.

<Callout icon="📘" theme="info">
  **Note**

  Only fields defined as **searchable fields** appear in the search results.

  For the default list of searchable fields per asset type, see [Fields Available for Search](https://docs.axonius.com/axonius-help-docs/docs/fields-available-for-search).

  To learn how to define specific searchable fields for each asset type, see [Customizing Global Search Settings](https://docs.axonius.com/axonius-help-docs/docs/customizing-global-search-settings).
</Callout>

Under each result, the fields where the search criteria was found in are listed. Hover over a result to see the values of these fields.

Here's a demonstration of the full Assets search flow:

<Image align="center" border={false} width="700px" src="https://files.readme.io/86f1f9970561adb88b2c0ebe7c7fbdb56eb05f79a9865c735d4172af75f237e5-AWSSearchFlow.gif" />

Click **Clear** to view results from all asset types again.

### Searching for Queries

The **Queries** tab shows queries that have the search criteria included in their query name, and the asset types they are associated with. Use the **Asset type** dropdown to filter results by a specific asset type.

<Callout icon="📘" theme="info">
  **Note**

  You can also view results found in [**Adapter Fetch History**](https://docs.axonius.com/docs/adapters-fetch-history) under the **Other Modules** section.

  <Image align="center" border={false} width="200px" src="https://files.readme.io/b9da6f4b9132c45b9e153f492a047d3ec54f85361c90c2c91dc5c2cb5da618c0-image.png" />
</Callout>

Hover over a result to view the query details such as its Folder Path and Tags, or open the query drawer.

Click on the result to automatically run the query.

Here's a demonstration of the full Queries search flow:

<Image align="center" border={false} width="700px" src="https://files.readme.io/55e24e9ee2a391602395456a411c01e270a6b47bffd842da7664cea79bd2ffef-QueriesSearchFlow.gif" />

Click **Clear** to view results from all asset types again.

## Viewing Search Results

Click **View all Results** to explore the full list of results returned by your search criteria.

### Results from Assets

Use the left navigation pane to select a specific Assets page to view results in.

* In each Assets page, your search is translated to an AQL and a Query Wizard expression. The query includes all the fields that were searched with OR conditions between them.

  * For example, if we type the string 'weblb' into the search bar, and proceed to view the results in the Devices page, the results are filtered by the following Query Wizard expression:

    <Image align="center" alt="SearchQuery" border={false} width="700px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-Z5OJ6LPJ.png" />
* All default fields are added automatically to the query even if they did not return results.
* If results were found in fields that **do not** exist in your default table view, those fields are automatically added to the table. For example: if the default view of the Devices page does not include the **Device Manufacturer Serial** field, and you run a search that finds a relevant result in that field - the results table on the Devices page will include the Device Manufacturer Serial field as well.

  <Callout icon="📘" theme="info">
    **Note**

    The field will be added to the table only if it's defined as a searchable field for Devices by the [Global Search settings](https://docs.axonius.com/axonius-help-docs/docs/customizing-global-search-settings).
  </Callout>
* See the [Assets Page documentation](/docs/assets-page) for additional information on actions you can perform on each Assets page to manage the assets found: create queries, edit the table columns, refine data, export data, and more.

### Results from Queries

View all queries that contains your search criteria in their name.

## Exiting and Resuming the Search

To exit the search results view and reset the current Assets or Queries page to their default views, click the **Reset** button of the Assets or Queries table.

To resume a search, if it appears in the **Recently Searched** section, click on it to run it again.