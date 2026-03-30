# Source: https://docs.axonius.com/docs/asset-added-or-removed.md

# Asset Added or Removed

Axonius supports **Asset added or removed** as an event in a Workflow.
When a Workflow is configured with an **Asset added**/**Asset removed** event, the query results of the current Discovery cycle are compared to the results of the previous Discovery cycle. Each time an asset is added/removed from the query results between Discovery Cycles, an event occurs. The Workflow runs on those added/removed assets only.

<Callout icon="📘" theme="info">
  Note

  * The results of the first Discovery Cycle are compared to the query results at the time that the event was saved in the Workflow.

  * The **Asset removed** event only refers to assets removed from query results. These assets still exist in the Axonius database.
</Callout>

**To select Asset added or removed as an event**

1. In the Event pane, under **Axonius Utilities**, click ![AssetAddedorRemovedButton](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetAddedorRemovedButton.png)
   The **Asset added or removed** configuration opens.

* The following is an **Asset added or removed** non-triggering event.

![EventAssetAddedRemoved.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventAssetAddedRemoved.png)

2. Select the event trigger:
   * Click **Asset added** to create an event whenever an asset is added to the query results.
   * Click **Asset removed** to create an event whenever an asset is removed from the query results.

3. In **Select Query**, from the **Module** dropdown, select the asset type that you want to query. Then, from the **Query Name** dropdown, do one of the following:
   * Select a saved query from the list.
   * Click **Add Query** to create a new query using the query wizard. To learn more about creating a new query, see [Adding a New Query](/docs/query-wizard-and-query-filter).