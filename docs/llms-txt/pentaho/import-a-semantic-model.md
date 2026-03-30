# Source: https://docs.pentaho.com/pba/semantic-model-editor/import-a-semantic-model.md

# Import a semantic model

You can import an existing data source that you published in the **Pentaho Server** as a semantic model. Data sources imported as semantic models are no longer available in the **Pentaho User Console**. &#x20;

{% hint style="danger" %}
**Cautions:** &#x20;

* If an Analysis Data Source with the same name as a Semantic Model is imported using the Pentaho User Console, the content of the Analysis Data Source completely overwrites the content in the Semantic Model, which cannot be restored.&#x20;
* If you change the structure or name of the semantic model, you must also update related reports, or the reports will no longer work. &#x20;
  {% endhint %}

Complete the following steps to create a basic semantic model:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Click **Import**. The **Please Select Data Source** window opens.&#x20;
4. Navigate to the data source that you want to import by searching or scrolling through the list.&#x20;
5. Click **Import**. The data source is imported as a semantic model with the same name and connection information, and the model is displayed on the canvas.&#x20;
