# Source: https://docs.pentaho.com/pba/semantic-model-editor/editing-a-semantic-model/edit-data-connection-details-in-a-semantic-model.md

# Edit data connection details in a semantic model

You can edit the data connection that connects the semantic model to a physical source of data by selecting a new connection from the list or by entering details for a new connection.&#x20;

Complete the following steps to edit data connection details in a semantic model:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;
3. Open the semantic model that you want to edit by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. Click the **More Actions** icon and select **Edit Connection**. The **Edit Connection** window opens.&#x20;
5. Edit your data connection by taking one or more of the following actions: &#x20;
   * To use a different, existing data connection, select that connection from the **Data Connection** list.&#x20;
   * To add a new data connection, click **New Data Connection** and enter the following information about the data connection:&#x20;

     <table><thead><tr><th width="115.77783203125">Option </th><th>Description </th></tr></thead><tbody><tr><td>URL* </td><td>URL of the data connection. </td></tr><tr><td>Driver </td><td>Driver needed to access the data connection. </td></tr><tr><td>User* </td><td>Name used to access the data connection. </td></tr><tr><td>Password </td><td>Password used to access the data connection. </td></tr></tbody></table>

     \*Required &#x20;
   * To disable all parameters for the data connection, turn off the **Add parameters?** toggle.&#x20;
   * To delete a parameter, navigate to the parameter by searching or scrolling through the **Parameters** list, and then click the trash icon next to the parameter you want to delete.&#x20;
   * To add one or more parameters to the data connection, turn on the **Add parameters?** toggle, click **Add+** to add a new row for each parameter to the Parameters table, and then enter a **Name** and **Value** for each parameter.

     Use parameters to fine-tune the Mondrian engine's model processing, set up the JDBC connection, or support dynamic user-specific information in the model content. You can enter a custom parameter name or select a parameter name from the list. The following names are reserved by the system and cannot be used as a parameter: `Provider`, `Jdbc`, `JdbcDrivers`, `JdbcUser`, `JdbcPassword`, `Catalog`, `CatalogContent`, `CatalogName`, `DataSource`, and `DataAccessNotListedCatalog`. &#x20;
6. Click **Save**. Changes to the data connection details for the semantic model are saved.&#x20;
