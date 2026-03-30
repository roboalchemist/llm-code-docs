# Source: https://docs.pentaho.com/pba/semantic-model-editor/editing-a-semantic-model/edit-a-cube/edit-a-measure-created-with-sql-in-a-cube.md

# Edit a measure created with SQL in a cube

Edit a measure created with SQL to change the properties that describe the measure; control its visibility and availability; and specify the SQL expression, format, and default aggregation used to calculate the measure.&#x20;

Complete the following steps to edit a measure created with SQL in a cube:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the cube with a measure you want to edit by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. On the canvas, locate the cube, measures node, and measure you want to edit.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> To locate an element in a large semantic model, you can click the <strong>Model Structure</strong> tab and then navigate to the element by searching or scrolling through the list. </p></div>
5. Next to the measure's name, click the **More Actions** icon and select **Edit**. The **Edit SQL Measure** window opens.&#x20;
6. Edit options in one or more of the following sections:&#x20;
   1. In the **Mandatory Information** section, edit one or more of the following options:&#x20;

      <table><thead><tr><th width="182.4444580078125">Option </th><th>Description </th></tr></thead><tbody><tr><td>Measure Name* </td><td>A unique name for the measure created with SQL. </td></tr><tr><td>Default Aggregation* </td><td>Default aggregation to use for the measure in reports. </td></tr><tr><td>SQL Expression* </td><td><p>SQL expression used to calculate the measure's value.  </p><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note</strong>: Autocomplete options are available for standard SQL functions, keywords, and table columns within the cube's scope. </p></div></td></tr></tbody></table>

      \*Required&#x20;
   2. Expand the **Optional Information** section, and then edit one or more of the following options:

      <table><thead><tr><th width="143.99993896484375">Option </th><th>Description </th></tr></thead><tbody><tr><td>Format </td><td>Option that determines how the value for the measure is displayed (example: 0.00 or #, ###). </td></tr><tr><td>Visible </td><td>Value indicating whether the dimension element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Dialect </td><td>SQL dialect that corresponds to the SQL expression that you wrote for the measure. In Advanced mode, you can write multiple expressions for the same measure by using a different dialect for each expression. For details, see <a href="../../advanced-mode">Advanced mode</a>.</td></tr><tr><td>Data Type </td><td>The type of data resulting from the SQL expression used for the measure. </td></tr></tbody></table>
   3. Expand the **Describe Measure** section, and then edit one or more of the following options: &#x20;

      <table><thead><tr><th width="128.22216796875">Option </th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the measure’s name. You can use captions to provide a user-friendly label for reports or for localization so that the measure’s name appears in the local language. </td></tr><tr><td>Description </td><td>A description of the measure created with SQL. </td></tr></tbody></table>
7. Click **Apply**. Edits to the measure created with SQL are applied.&#x20;
8. In the **Semantic Model Editor**, click **Save** to save changes to the model.&#x20;
