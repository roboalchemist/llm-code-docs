# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/set-specific-options-for-pdi-database-connections.md

# Set specific options for PDI database connections

Use the **Advanced** option in the Database Connection dialog box to configure properties associated with how SQL is generated. With these properties, you can set a standard across all your SQL tools, ETL tools, and design tools.

1. Open the Database Connection dialog box in [PUC](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/dbSFXbJFiObHB299lSSa/) or [PDI](https://docs.pentaho.com/pdia-data-integration/readme).
2. Click **Options** in the left pane.

   The **Parameters** table appears as shown as shown below:

   ![Options tab in the PUC (left) and PDI (right) Database Connection dialog boxes](https://docs.pentaho.com/~gitbook/image?url=https%3A%2F%2F3897443520-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7HOrU4JuCmIFVNup2Gxd%252Fuploads%252Fgit-blob-91a9c0378490ed57d671309d99980a571afe99d1%252FssPUCanPDIDataConnectionOptions.png%3Falt%3Dmedia\&width=300\&dpr=4\&quality=100\&sign=e408939a\&sv=2)
3. In the next available row of the **Parameters** table, enter a valid parameter name and its corresponding value. For JDBC database-specific configuration help, click **Help**.

   A new browser window opens and displays additional information about configuring the JDBC connection for the database type that is currently selected in the **General** pane.
4. Click **Test**.

   A success message appears if the connection is established.
5. Click **OK** to close the connection test dialog box.
6. To save the connection, click **OK** to close the Database Connection dialog box.
