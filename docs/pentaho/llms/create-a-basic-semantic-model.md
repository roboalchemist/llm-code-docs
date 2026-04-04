# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-basic-semantic-model.md

# Create a basic semantic model

Create a basic semantic model with the minimum information of the model's name and physical data connection details.&#x20;

Complete the following steps to create a basic semantic model:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Click **+ Add New Model**. The **New Model** window opens.&#x20;
4. Enter a unique **Model Nam**e.&#x20;
5. Select the data connection to use in the model by using one of the following options:&#x20;
   * Add an existing data connection by completing the following sub steps:&#x20;
     1. Click **Existing Data Connection** and then select the connection from the **Data Connection** list. &#x20;
     2. (Optional) To add one or more parameters to the data connection, turn on the **Add parameters?** toggle, click **Add+** to add a new row for each parameter to the **Parameters** table, and then enter a **Name** and **Value** for each parameter. &#x20;

        Use parameters to fine-tune the Mondrian engine's model processing, set up the JDBC connection, or support dynamic user-specific information in the model content. You can enter a custom parameter name or select a parameter name from the list. The following names are reserved by the system and cannot be used as a parameter: `Provider`, `Jdbc`, `JdbcDrivers`, `JdbcUser`, `JdbcPassword`, `Catalog`, `CatalogContent`, `CatalogName`, `DataSource`, and `DataAccessNotListedCatalog`.
   * Add a new data connection by completing the following sub steps:&#x20;

     <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>Important:</strong> A data connection added during semantic model creation is exclusive to that model and cannot be reused elsewhere in the product.</p></div>

     1. Select **New Data Connection**.
     2. Enter information about the data connection for the following options:

        <table><thead><tr><th width="99.11114501953125">Option </th><th>Description </th></tr></thead><tbody><tr><td>URL* </td><td>URL of the data connection. </td></tr><tr><td>Driver </td><td>Driver needed to access the data connection. </td></tr><tr><td>User* </td><td>Name used to access the data connection. </td></tr><tr><td>Password </td><td>Password used to access the data connection. </td></tr></tbody></table>

        &#x20;\*Required
     3. (Optional) To add one or more parameters to the data connection, turn on the **Add parameters?** toggle, click **Add+** to add a new row for each parameter to the **Parameters** table, and then enter a **Name** and **Value** for each parameter. &#x20;

        Use parameters to fine-tune the Mondrian engine's model processing, set up the JDBC connection, or support dynamic user-specific information in the model content. You can enter a custom parameter name or select a parameter name from the list. The following names are reserved by the system and cannot be used as a parameter: `Provider`, `Jdbc`, `JdbcDrivers`, `JdbcUser`, `JdbcPassword`, `Catalog`, `CatalogContent`, `CatalogName`, `DataSource`, and `DataAccessNotListedCatalog`.&#x20;
     4. (Optional) Click **Test Connection** to test the connection. &#x20;
6. Click **Create Model**. The semantic model is created and opened in the canvas.&#x20;

**What to do next:** Create a cube with fact tables, dimensions, and measures in the semantic model for the data that you want to analyze.
