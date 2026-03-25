# Source: https://docs.pentaho.com/pba/semantic-model-editor/delete-elements-in-a-semantic-model.md

# Delete elements in a semantic model

Delete elements from a semantic model that you no longer need.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* Deleting an element might impact model consistency because elements reference other elements. When you delete an element, the system displays a warning message with a list of elements that might be affected by the deletion.
* To locate an element in a large semantic model, you can click the **Model Structure** tab and then navigate to the element by searching or scrolling through the list.&#x20;
  {% endhint %}

## Delete a cube

Delete a cube from a semantic model when you no longer need that cube.&#x20;

Complete the following steps to delete a cube from a semantic model.&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the cube you want to delete by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. On the canvas, locate the cube you want to delete.&#x20;
5. In the cube, click the **More Actions** icon and select **Delete**. The **Delete Cube** confirmation window opens.&#x20;
6. Click **Delete**. The cube is deleted.&#x20;

## Delete cube elements

Delete elements from a cube that you no longer need in the cube.&#x20;

{% hint style="info" %}
**Note:** Some elements cannot be deleted. For example, a dimension must have at least one hierarchy. If a dimension has only one hierarchy, that hierarchy cannot be deleted. If an element cannot be deleted, the **Delete** option is not available and cannot be selected.
{% endhint %}

Complete the following steps to delete an element from a cube.&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the element you want to delete by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. On the canvas, locate the cube that contains the element you want to delete.&#x20;
5. In the cube, locate the element you want to delete. You can delete one or more of the following cube elements: &#x20;
   * Fact table&#x20;
   * Dimensions&#x20;
   * Hierarchies in a dimension&#x20;
   * Levels in the hierarchy of a dimension&#x20;
   * Measures&#x20;
   * Degenerate dimensions&#x20;
   * Hierarchies in a degenerate dimension&#x20;
   * Levels in the hierarchy of a degenerate dimension&#x20;
6. Next to the element’s name, click the **More Actions** icon and select **Delete**. A confirmation window to delete the element opens.&#x20;
7. Click **Delete**. The element is deleted.&#x20;

## Delete shared dimensions

Delete shared dimensions that you no longer need for any cubes in the semantic model. &#x20;

Complete the following steps to delete a shared dimension from a semantic model.&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that contains the shared dimension you want to delete by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. On the canvas, locate the shared dimension you want to delete.&#x20;
5. Next to the shared dimension's name, click the **More Actions** icon and select **Delete**. The **Delete Shared Dimension** confirmation window opens.&#x20;
6. Click **Delete**. The shared dimension is deleted.&#x20;
