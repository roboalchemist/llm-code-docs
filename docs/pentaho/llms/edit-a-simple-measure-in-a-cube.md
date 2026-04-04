# Source: https://docs.pentaho.com/pba/semantic-model-editor/editing-a-semantic-model/edit-a-cube/edit-a-simple-measure-in-a-cube.md

# Edit a simple measure in a cube

Edit a simple measure to change the properties that describe the measure, control its visibility and availability, or define which data is pulled from the cube’s fact table.&#x20;

Complete the following steps to edit a simple measure in a cube:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the cube with a simple measure you want to edit by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. On the canvas, locate the cube, measures node, and measure you want to edit.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> To locate an element in a large semantic model, you can click the <strong>Model Structure</strong> tab and then navigate to the element by searching or scrolling through the list. </p></div>
5. Next to the measure's name, click the **More Actions** icon and select **Edit**. The **Edit Measure** window opens.&#x20;
6. Edit options in one or more of the following sections:&#x20;
   1. In the **Mandatory Information** section, edit one or more of the following options:&#x20;

      <table><thead><tr><th width="181.5555419921875">Option</th><th>Description </th></tr></thead><tbody><tr><td>Measure Name*</td><td>A unique name for the simple measure. </td></tr><tr><td>Source Column* </td><td>Column that is the source of the simple measure's values. If not specified, you must enter a measure expression for the name of an existent column in the Facts table of the cube. </td></tr><tr><td>Default Aggregation* </td><td>Default method used in reports of grouping and calculating data for the simple measure. </td></tr></tbody></table>

      \*Required&#x20;
   2. Expand the **Optional Information** section, and then edit one or more of the following options: &#x20;

      <table><thead><tr><th width="180.6666259765625">Option </th><th>Description</th></tr></thead><tbody><tr><td>Format </td><td>Option that determines how the value for the simple measure is displayed (example: 0.00 or #, ###). </td></tr><tr><td>Visible </td><td>Value indicating whether the simple measure element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Data Type </td><td>The type of data used for the simple measure. Types include String, Numeric, and Integer. </td></tr></tbody></table>
   3. Expand the **Describe Measure** section, and then edit one or more of the following options: &#x20;

      <table><thead><tr><th width="183.3331298828125">Option </th><th>Description</th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the simple measure’s name. You can use captions to provide a user-friendly label for reports or for localization so that the simple measure’s name appears in the local language. </td></tr><tr><td>Description </td><td>A description of the simple measure. </td></tr></tbody></table>
7. Click **Apply**. Edits to the measure are applied.&#x20;
8. In the **Semantic Model Editor**, click **Save** to save changes to the model.&#x20;
