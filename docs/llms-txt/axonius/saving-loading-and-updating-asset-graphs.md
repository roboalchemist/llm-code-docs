# Source: https://docs.axonius.com/docs/saving-loading-and-updating-asset-graphs.md

# Saving, Loading and Updating Asset Graphs

At any point in your investigation, you can save the current state of the Asset Graph and return to it later. Saved Asset Graphs can be loaded to continue working on them. New investigation steps performed on existing Asset Graphs can be added to the exising steps.

Before a graph is saved, it is called New Graph.

<Image align="center" alt="AssetGraph-NewGraph.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-NewGraph.png" />

**To save a new Asset Graph:**

1. Perform the investigation steps you want.
2. Click **Save As** at the top right of the Asset Graph. The Save as New Asset Graph dialog opens.
3. In the **Graph name** text box, give the Asset Graph a descriptive name.
4. (Optional) Click **Add description** to enter a full description of the graph.
5. Under **Tags**, add or search for tags to apply to the Asset Graph.
6. In [**Who has access**](/docs/who-has-access), configure the access privileges for the query.
7. Under **Folder name**, select the location where you want to save the new Asset Graph.
8. Click **Save**. The Asset Graph is saved and can be found on the [Asset Graph Manager](/docs/managing-asset-graphs) page.

**To load a previously saved Asset Graph:**

1. Navigate to the [Asset Graph Manager](/docs/managing-asset-graphs).
2. Click on the Asset Graph you want to load.
3. At the bottom of the drawer, click **Load Graph**.

<Callout icon="📘" theme="info">
  Note

  The access permissions of an asset graph that were configured when it was saved determine what changes you can make when it is subsequently loaded.
</Callout>

## Saving Changes to an Existing Asset Graph

Once an Asset Graph is saved it can be loaded again for further investigation. If subsequent investigation steps are taken in addition to the existing steps, you can save the additional steps to the already saved steps. This is useful when an investigation needs to be continued at another time.

**To save new steps to an existing Asset Graph:**

1. Save a new Asset Graph or load an existing Asset Graph.
2. Perform the new investigation steps.
3. From the **Save As** dropdown list, select **Save**. The new steps are added to the previously saved steps.
4. To discard the changes and revert to how the graph was before the new steps, click **Discard Changes**. Then click **Discard** to verify the action.

## Updating Asset Graph Details

You can update the details of saved Asset Graphs. The Asset Graph can be renamed, and the access permissions and folder location can be changed.

**To update Asset Graph details:**

1. Save a new Asset Graph or load an existing Asset Graph.
2. From the **Save As** dropdown list, select **Update Details**.
3. In the Update Details dialog, make the changes you want and click **Save**.