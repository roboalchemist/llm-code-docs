# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-fact-table-to-a-cube.md

# Add a fact table to a cube

Add a fact table that contains the data from a semantic model’s physical connection that you want aggregated in a cube. You can either create a new cube while adding the fact table or add the fact table to an existing cube.

{% hint style="info" %}
**Notes:**&#x20;

* A cube can have only one fact table.&#x20;
* Using an inline table as a fact table is supported only in Advanced mode. For details, see [Advanced mode](https://docs.pentaho.com/pba/semantic-model-editor/advanced-mode).
  {% endhint %}

Complete the following steps to add a table or view as a fact table for a cube:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model to which you are adding a cube or editing a cube by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. In the **Data Source** tab, navigate to the table or view that you want to use as a fact table.&#x20;
5. (Optional) To preview data in the table or view, click the **Preview** icon next to the table or view. The **Preview Data** panel opens. You can take one or more of the following additional actions while previewing the data:&#x20;
   * Hover over a column header to see metadata information for that column.
   * Click a column header to sort the table by the data in that column.&#x20;
   * Click the **Preview** icon again to close the **Preview Data** panel.

     <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You can preview one table or view at a time. By default, the maximum number of rows shown is 100. The administrator can change the maximum value by editing the <code>row-limit</code> property in the <code>application.properties</code> file, located in: <code>\Pentaho\server\pentaho-server\pentaho-solutions\system\semantic-model-editor</code>. The administrator must restart the Server for the new row value maximum to take effect.</p></div>
6. Use one of the following options to add the table or view as a fact table:&#x20;

   1. For an existing cube that does not already have a fact table, drag and hold the table or view over the cube until the **Do you want to:** dialog opens, and then drop the table or view onto the **Use as Fact Table** option.&#x20;
   2. To create a new cube, drag and hold the table or view over a blank area of the canvas until the **Do you want to:** dialog opens, and then drop the table or view onto the **Use as Fact Table** option.

   The table or view is added to the cube as a fact table. &#x20;
7. (Optional) If you created a new cube, change the name of the cube by clicking the name to make it editable and then enter a new, unique name for the cube.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> The default name of a cube is “Cube” plus a number that represents the order in which the cube was created (example: Cube 3). </p></div>
8. Click **Save** to save changes to the model.&#x20;
