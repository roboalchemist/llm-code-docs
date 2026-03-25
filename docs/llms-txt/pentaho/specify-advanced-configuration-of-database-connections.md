# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/specify-advanced-configuration-of-database-connections.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/specify-advanced-configuration-of-database-connections.md

# Specify advanced configuration of database connections

Use the **Advanced** option in the Database Connection dialog box to configure properties associated with how SQL is generated. With these properties, you can set a standard across all your SQL tools, ETL tools, and design tools.

1. Open the Database Connection dialog box in [PUC](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Install/Pentaho%20configuration/Pentaho%20Configuration%20-%20Config%20Overview%20\(article%20cp\)/Tasks%20to%20be%20Performed%20by%20a%20Pentaho%20Administrator%20-%20Config%20Overview/Define%20Data%20Connections%20\(article%20cp\)/Open%20the%20Connection%20Dialog%20Box%20-%20Database%20Connections/Open%20the%20Database%20Connection%20dialog%20box%20from%20PUC=GUID-16E92667-FDF1-45F6-AC98-15C69E978DB2=2=en=.md) or [PDI](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/open-the-connection-dialog-box/open-the-database-connection-dialog-box-from-pdi).
2. Click **Advanced** on the left pane.

   The available options depend on whether you are using PUC or PDI as shown below:![Advanced tab in the (left) and (right) Database Connection dialog boxes](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-222ab0e906cd9fc07fbfc3731d32a8549d48ccf9%2FssPUCandPDIDataConnectionAdvancedOption.png?alt=media)
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
