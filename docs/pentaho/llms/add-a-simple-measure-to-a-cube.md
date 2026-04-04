# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-a-simple-measure-to-a-cube.md

# Add a simple measure to a cube

Add a simple measure to use values pulled directly from a column in the cube’s fact table as a measure. &#x20;

Complete the following steps to add a simple measure to a cube:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the cube to which you want to add a measure by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.
4. Select the cube you want to edit, and then click the **Add a Measure** icon. The **Add a Measure** dialog opens.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> If the <strong>Add a Measure</strong> icon is not visible, click the <strong>More Actions</strong> icon, and then select <strong>Add a Measure</strong>. </p></div>
5. Select **Add Simple Measure**, and then click **Confirm**. The Add a **Simple Measure** dialog opens.&#x20;
6. In the **Mandatory Information** section, enter the required information for the following options: &#x20;

   <table><thead><tr><th width="179.55548095703125">Option </th><th>Description </th></tr></thead><tbody><tr><td>Measure Name </td><td>A unique name for the simple measure. </td></tr><tr><td>Source Column </td><td>Column that is the source of the measure's values. If not specified, you must enter a measure expression for the name of an existent column in the Facts table of the cube. </td></tr><tr><td>Default Aggregation </td><td>Default method used in reports for grouping and calculating data for the measure. </td></tr></tbody></table>
7. &#x20;(Optional) Expand the **Optional Information** section and edit one or more of the following options: &#x20;

   <table><thead><tr><th width="126.22222900390625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Format </td><td>Option that determines how the value for the measure is displayed (example: 0.00 or #, ###).  </td></tr><tr><td>Visible </td><td>Value indicating whether the measure element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Data Type </td><td>The type of data used for the measure. Types include String, Numeric, and Integer. </td></tr></tbody></table>
8. (Optional) Expand the **Describe Measure** section and edit one or more of the following options:

   <table><thead><tr><th width="127.11114501953125">Option </th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the measure's name. You can use captions to provide a user-friendly label for reports or for localization so that the measure's name appears in the local language. </td></tr><tr><td>Description </td><td>A description of the measure. </td></tr></tbody></table>

   &#x20;
9. Click **Create**. The measure is created and added to the **Measures** node inside the cube.&#x20;
10. Click **Save** to save changes to the model.&#x20;
