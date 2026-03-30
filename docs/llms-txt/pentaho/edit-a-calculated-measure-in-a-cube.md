# Source: https://docs.pentaho.com/pba/semantic-model-editor/editing-a-semantic-model/edit-a-cube/edit-a-calculated-measure-in-a-cube.md

# Edit a calculated measure in a cube

Edit a calculated measure to change the properties that describe the measure, control its visibility and availability, and specify the formula and parent used to calculate the measure.&#x20;

{% hint style="info" %}
**Note:** If you edit a semantic model externally in Pentaho Analyzer and create a calculated measure for the semantic model, the following changes occur in the semantic model:&#x20;
{% endhint %}

* Pentaho Analyzer saves the calculated measure in the semantic model's XML as a read-only structure. Read-only structures are visible in Semantic Model Editor but cannot be edited or deleted. Semantic Model Editor displays a read-only structure in the following locations:&#x20;
  * **Canvas mode:** Displays read-only structure as grayed-out element. &#x20;
  * **Advanced mode:** Displays read-only structure as gray text with grey highlighting. &#x20;
  * **Model Structure tab:** Displays read-only structure as grey text with a grey lock icon next to the name. &#x20;
* When the semantic model is imported back into the Semantic Model Editor, comments in the XML are discarded from the semantic model.&#x20;

Complete the following steps to edit a calculated measure in a cube:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the cube with a calculated measure you want to edit by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.
4. On the canvas, locate the cube, measures node, and measure you want to edit.&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> To locate an element in a large semantic model, you can click the <strong>Model Structure</strong> tab and then navigate to the element by searching or scrolling through the list. </p></div>
5. Next to the measure's name, click the **More Actions** icon and select **Edit**. The **Edit Calculated Measure** window opens.&#x20;
6. Edit options in one or more of the following sections:&#x20;
   1. In the **Mandatory Information** section, edit one or more of the following options:&#x20;

      <table><thead><tr><th width="154">Option </th><th>Description </th></tr></thead><tbody><tr><td>Measure Name* </td><td>Name for the measure that is unique for all measures in the cube. </td></tr><tr><td>Formula* </td><td>MDX formula used to calculate the value for the measure. </td></tr></tbody></table>

      \*Required&#x20;
   2. Expand the **Optional Information** section, and then edit one or more of the following options: &#x20;

      <table><thead><tr><th width="155.777587890625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Format </td><td>Option that determines how the value for the calculated measure is displayed (example: 0.00 or #, ###). </td></tr><tr><td>Visible </td><td>Value indicating whether the calculated measure element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Parent </td><td>Fully-qualified MDX identifier of the parent member.  If not specified, the member will be at the lowest level in the hierarchy. </td></tr></tbody></table>
   3. Expand the **Describe Measure** section, and then edit one or more of the following options: &#x20;

      <table><thead><tr><th width="162.22216796875">Option </th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the calculated measure’s name. You can use captions to provide a user-friendly label for reports or for localization so that the calculated measure’s name appears in the local language. </td></tr><tr><td>Description </td><td>A description of the calculated measure. </td></tr></tbody></table>
7. Click **Apply**. Edits to the calculated measure are applied.&#x20;
8. In the **Semantic Model Editor**, click **Save** to save changes to the model.&#x20;
