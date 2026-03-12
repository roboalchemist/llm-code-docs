# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-a-measure-created-with-sql-to-a-cube.md

# Add a measure created with SQL to a cube

Add a measure created with SQL to a cube when you want to calculate the values for the data you are measuring in a cube by using an SQL expression that references data from multiple tables or views in the cube. &#x20;

Complete the following steps to add a measure created with SQL:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens. &#x20;
3. In the **Semantic Models** list, navigate to the model that has the cube to which you want to add a measure. You can find the model by searching or scrolling through the list.&#x20;
4. Select the model and click **Open**. The model opens in the canvas.&#x20;
5. Locate the cube you want to edit, and then click the **Add a Measure** icon. The **Add a Measure** dialog opens.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Notes:</strong> </p><ul><li>If the <strong>Add a Measure</strong> icon is not visible, click the <strong>More Actions</strong> icon, and then select <strong>Add a Measure</strong>. </li><li>To locate an element in a large semantic model, you can click the <strong>Model Structure</strong> tab and then navigate to the element by searching or scrolling through the list. </li></ul></div>
6. Select **Add with SQL**, and then click **Confirm**. The **Add with SQL** dialog opens.&#x20;
7. In the **Mandatory Information** section, enter the following, required information:

   <table><thead><tr><th width="179.5555419921875">Option </th><th>Description </th></tr></thead><tbody><tr><td>Measure Name </td><td>Name for the measure that is unique in the cube for all measures. </td></tr><tr><td>Default Aggregation </td><td>Default aggregation to use for the measure in reports. </td></tr><tr><td>SQL Expression </td><td><p>SQL expression used to calculate the measure's value. </p><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> Autocomplete options are available for generic SQL functions, keywords, and table columns within the cube's scope. </p></div></td></tr></tbody></table>
8. (Optional) Expand the **Optional Information** section and edit one or more of the following options:&#x20;

   <table><thead><tr><th width="143.99993896484375">Option </th><th>Description </th></tr></thead><tbody><tr><td>Format </td><td>Option that determines how the value for the measure is displayed (example: 0.00 or #, ###). </td></tr><tr><td>Visible </td><td>Value indicating whether the measure element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Dialect </td><td>SQL dialect that corresponds to the SQL expression that you wrote for the measure. In Advanced mode, you can write multiple expressions for the same measure by using a different dialect for each expression. For details, see <a href="../../../advanced-mode">Advanced mode</a>.</td></tr><tr><td>Data Type </td><td>The type of data resulting from the SQL expression used for the measure. </td></tr></tbody></table>

   &#x20;
9. (Optional) Expand the **Describe Measure** section and edit one or more of the following options: &#x20;

   <table><thead><tr><th width="143.11114501953125">Option </th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the measure's name. You can use captions to provide a user-friendly label for reports or for localization so that the measure's name appears in the local language. </td></tr><tr><td>Description </td><td>A description of the measure. </td></tr></tbody></table>
10. Click **Create**. The measure is created with SQL and added to the **Measures** node inside the cube.&#x20;
11. Click **Save** to save changes to the model.&#x20;
