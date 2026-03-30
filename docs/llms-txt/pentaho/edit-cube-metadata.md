# Source: https://docs.pentaho.com/pba/semantic-model-editor/editing-a-semantic-model/edit-a-cube/edit-cube-metadata.md

# Edit cube metadata

You can edit cube metadata that describes the cube and controls its visibility and availability.&#x20;

Complete the following steps to edit the metadata for a cube in a semantic model:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the cube you want to edit by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. On the canvas, locate the cube you want to edit. &#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> To locate an element in a large semantic model, you can click the <strong>Model Structure</strong> tab and then navigate to the element by searching or scrolling through the list. </p></div>
5. Click the **More Actions** icon and select **Edit**. The **Cube Editor** window opens.&#x20;
6. Edit options in one or more of the following sections:&#x20;
   1. In the **Mandatory Information** section, enter a new **Cube Name**.&#x20;

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note</strong>: By changing the name of the cube, previous existing reports built using this cube from this model will no longer work, be cautious doing this action.</p></div>
   2. In the **Optional Information** section, edit one or more of the following options: &#x20;

      <table><thead><tr><th width="158.4444580078125">Option </th><th>Description </th></tr></thead><tbody><tr><td>Default Measure </td><td>The measure used by default when the cube is queried to aggregate or visualize data for analysis or in a report. </td></tr><tr><td>Cache </td><td>Value indicating whether the fact table data for the cube is stored in memory by the Mondrian engine. Caching fact table data for a cube can improve query performance by reducing how often the engine must fetch data from the data connection. The default value is <strong>true</strong>. </td></tr><tr><td>Visible </td><td>Value indicating whether the cube element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Enabled </td><td>Value indicating whether the cube is active and available for use in the semantic model. You can temporarily disable a cube without deleting it from the model. The default value is <strong>true</strong>. </td></tr></tbody></table>
   3. In the **Describe Cube** section, edit one or more of the following options:

      <table><thead><tr><th width="154.8887939453125">Option</th><th>Description</th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the cube’s name. You can use captions to provide a user-friendly label for reports or for localization so that the cube's name appears in the local language. </td></tr><tr><td>Description </td><td>Description of the cube to help users understand the purpose or contents of the cube. </td></tr></tbody></table>
7. Click **Apply**. Edits to the cube’s metadata are applied.&#x20;
8. In the **Semantic Model Editor**, click **Save** to save changes to the model.&#x20;
