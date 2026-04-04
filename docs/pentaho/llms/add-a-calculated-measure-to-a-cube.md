# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-a-calculated-measure-to-a-cube.md

# Add a calculated measure to a cube

Add a calculated view when you want to calculate values for the data you are measuring in a cube by using a multidimensional (MDX) expression. &#x20;

Complete the following steps to add a calculated measure:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens. &#x20;
3. In the **Semantic Models** list, navigate to the model that contains the cube to which you want to add a measure. You can find the model by searching or scrolling through the list.&#x20;
4. Select the model and click **Open**. The model opens in the canvas.&#x20;
5. Locate the cube you want to edit, and then click the **Add a Measure** icon.  The **Add a Measure** dialog opens.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Notes</strong>: </p><ul><li>If the <strong>Add a Measure</strong> icon is not visible, click the <strong>More Actions</strong> icon, and then select <strong>Add a Measure</strong>. </li><li>To locate an element in a large semantic model, you can click the <strong>Model Structure</strong> tab and then navigate to the element by searching or scrolling through the list. </li></ul></div>
6. Select **Add Calculated Measure**, and then click **Confirm**. The **Add Calculated Measure** dialog opens.&#x20;
7. In the **Mandatory Information** section, enter the required information for the following options:  &#x20;

   <table><thead><tr><th width="144.00006103515625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Measure Name </td><td>Name for the measure that is unique for all measures in the cube. </td></tr><tr><td>Formula </td><td>MDX formula used to calculate the value for the measure. </td></tr></tbody></table>
8. (Optional) Expand the **Optional Information** section and edit one or more of the following options:&#x20;

   <table><thead><tr><th width="116.44439697265625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Format </td><td>Option that determines how the value for the measure is displayed (example: 0.00 or #, ###). </td></tr><tr><td>Visible </td><td>Value indicating whether the measure element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Parent </td><td>Fully-qualified MDX identifier of the parent member.  If not specified, the member will be at the lowest level in the hierarchy.</td></tr></tbody></table>
9. (Optional) Expand the **Describe Measure** section and edit one or more of the following options:&#x20;

   <table><thead><tr><th width="136">Option </th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the calculated measure's name. You can use captions to provide a user-friendly label for reports or for localization so that the measure's name appears in the local language. </td></tr><tr><td>Description </td><td>A description of the measure. </td></tr></tbody></table>
10. Click **Create**. The calculated measure is created and added to the **Measures** node inside the cube.&#x20;
11. Click **Save** to save changes to the model.&#x20;
