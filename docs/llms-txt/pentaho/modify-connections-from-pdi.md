# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/modify-connections/modify-connections-from-pdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/modify-connections/modify-connections-from-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/modify-connections-from-pdi.md

# Modify connections from PDI

Access other database-related connection tasks in PDI by right-clicking on the connection name in the **View** tab of the **Explorer** pane, as shown below:

<figure><img src="https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2F77G69r1psHnxvnYDjltz%2Fimage.png?alt=media&#x26;token=d8269f89-b63c-4b54-b3aa-aef429191818" alt="Other database-related tasks. "><figcaption><p>Other database-related tasks</p></figcaption></figure>

The following table describes these tasks:

| Task                  | Description                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Duplicate**         | Duplicate the database connection. The duplicate will not be created unless you specify a different **Connection Name** in the Database Connection dialog box when it appears.                                                                    |
| **Copy to clipboard** | Copy the XML defining the step to the clipboard.                                                                                                                                                                                                  |
| **SQL Editor**        | Execute SQL commands against an existing connection within the SQL Editor. See the **Pentaho Data Integration** document for details on the SQL Editor.                                                                                           |
| **Clear DB Cache**    | Clear out the database cache used by PDI to speed up connections. This command is commonly used when databases tables have been changed, created, or deleted (when the information in the cache no longer represents the layout of the database). |
| **Share**             | Share the connection information among transformations and jobs.                                                                                                                                                                                  |
| **Explore**           | Use the Database Explorer to explore the schemas and tables of your connected database. See the **Pentaho Data Integration** document for details on the Database Explorer.                                                                       |
| **Show dependences**  | Show all of the transformations and jobs that use this database connection.                                                                                                                                                                       |

## Delete connections from PDI

Perform the following steps to delete a connection in PDI:

1. Expand the **Database connections** folder in the **View** tab of the **Explorer** pane.
2. Right-click on a connection name and select **Delete**.

   The data source no longer appears under the Database connections folder.
