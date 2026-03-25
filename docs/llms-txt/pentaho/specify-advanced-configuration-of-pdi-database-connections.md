# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/specify-advanced-configuration-of-pdi-database-connections.md

# Specify advanced configuration of PDI database connections

Use the **Advanced** option in the Database Connection dialog box to configure properties associated with how SQL is generated. With these properties, you can set a standard across all your SQL tools, ETL tools, and design tools.

1. Open the Database Connection dialog box in [PUC](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/dbSFXbJFiObHB299lSSa/) or [PDI](https://docs.pentaho.com/pdia-data-integration/readme).
2. Click **Advanced** on the left pane.

   The available options depend on whether you are using PUC or PDI as shown below:![Advanced tab in the (left) and (right) Database Connection dialog boxes](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2FqPtd3RpLH2s9Y96vbT02%2FssPUCandPDIDataConnectionAdvancedOption.png?alt=media\&token=14161d03-fea2-4ea9-9b9a-01575dbd6910)
3. Check the appropriate boxes and enter the SQL statements as described in the following table:

   | Identifier                         | Description                                                                                                                                                                                                   |
   | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Supports the Boolean data type\*   | Instructs PDI to use native Boolean data types supported by the database.                                                                                                                                     |
   | Supports the timestamp data type\* | Instructs PDI to use the timestamp data type supported by the database.                                                                                                                                       |
   | Quote all in database              | Enables case-sensitive table names. For example, MySQL is case-sensitive on Linux, but not case-sensitive on Microsoft Windows. If you quote the identifiers, the databases uses a case-sensitive table name. |
   | Force all to lower-case            | Enables the system to change the case of all database to lower-case.                                                                                                                                          |
   | Force all to upper-case            | Enables the system to change the case of all identifiers to upper-case.                                                                                                                                       |
   | Preserve case of reserved words\*  | Instructs PDI to use a list of reserved words supported by the database.                                                                                                                                      |
   | Preferred schema name\*            | For PDI, enter the preferred schema name (for example, `MYSCHEMA`).                                                                                                                                           |
   | SQL statements                     | Enter the SQL statement used to initialize this connection.                                                                                                                                                   |

   **Note:** Which preferences appear depends on if you are accessing the dialog box from PUC or PDI. The additional fields available in PDI are indicated with an asterisk (\*).
4. Click **Test**. A success message appears if the connection is established. Click **OK** to close the connection test dialog box.
5. To save the connection, click **OK** to close the Database Connection dialog box.
