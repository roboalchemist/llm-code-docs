# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/use-a-shared-dimension-in-a-cube.md

# Use a shared dimension in a cube

Use a shared dimension in a cube when you want the aggregated data to be consistent with other cubes in the same semantic model. For example, you might use a shared time dimension for all cubes that are used in time-based analysis. The shared dimension must be created before it can be used in a cube. See [Create a shared dimension](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-shared-dimension).&#x20;

Complete the following steps to use a shared dimension in a cube:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model to which you are using a shared dimension by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. In the canvas, locate the shared dimension you want to use and the cube in which you want to use the shared dimension. &#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> To locate an element in a large semantic model, you can click the <strong>Model Structure</strong> tab and then navigate to the element by searching or scrolling through the list. </p></div>
5. Drag and hold the shared dimension over the cube until the **Do you want to:** dialog opens and then drop the shared dimension onto the **Use as Dimension** option. The **Dimension Usage Editor** opens.&#x20;
6. In the **Dimension Name** section, enter a **Name** that is unique in the context of the cube. The name can be the same name used for the shared dimension if it is unique in the context of the cube.&#x20;
7. In the **Mandatory Data** section, enter information for the following options:

   <table><thead><tr><th width="180.44439697265625">Option</th><th>Description</th></tr></thead><tbody><tr><td>Source* </td><td>Table used as the source of data for the dimension. This is not editable in the Dimension Usage as it is defined in the Shared Dimension.</td></tr><tr><td>Fact Table Column* </td><td>Fact table column used to connect the cube's fact table to the usage of the shared dimension in that cube. </td></tr></tbody></table>

   \*Required field&#x20;
8. (Optional) Expand the **Optional Information** section and edit one or more of the following options:&#x20;

   <table><thead><tr><th width="181.33331298828125">Option</th><th>Description</th></tr></thead><tbody><tr><td>Level to Join </td><td>Level of the hierarchy in the shared dimension to connect to the cube's fact table. When not specified, joins to the lowest level of the dimension.</td></tr><tr><td>Visible </td><td>Value indicating whether the hierarchy element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Usage Prefix </td><td>String of text added to the beginning of the column name when building collapsed dimension aggregates to indicate how the dimension is used. Usage prefixes enable the system to accurately recognize and associate columns during aggregate table matching. </td></tr></tbody></table>
9. (Optional) Expand the **Describe Hierarchy** section and edit one or more of the following options:

   <table><thead><tr><th width="182.22222900390625">Option</th><th>Description</th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the hierarchy’s name. You can use captions to provide a user-friendly label for hierarchies or for localization so that the hierarchy’s name appears in the local language. </td></tr><tr><td>Description </td><td>Description of the hierarchy. </td></tr></tbody></table>

   &#x20;
10. Click **Apply**. The dimension is used as a **Shared Dimension** node in the cube.&#x20;
11. Click **Save** to save changes to the model.&#x20;
