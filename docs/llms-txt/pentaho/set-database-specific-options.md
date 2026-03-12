# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/set-database-specific-options.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/set-database-specific-options.md

# Set database-specific options

Use the **Advanced** option in the Database Connection dialog box to configure properties associated with how SQL is generated. With these properties, you can set a standard across all your SQL tools, ETL tools, and design tools.

1. Open the Database Connection dialog box in [PUC](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Install/Pentaho%20configuration/Pentaho%20Configuration%20-%20Config%20Overview%20\(article%20cp\)/Tasks%20to%20be%20Performed%20by%20a%20Pentaho%20Administrator%20-%20Config%20Overview/Define%20Data%20Connections%20\(article%20cp\)/Open%20the%20Connection%20Dialog%20Box%20-%20Database%20Connections/Open%20the%20Database%20Connection%20dialog%20box%20from%20PUC=GUID-16E92667-FDF1-45F6-AC98-15C69E978DB2=2=en=.md) or [PDI](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/open-the-connection-dialog-box/open-the-database-connection-dialog-box-from-pdi).
2. Click **Options** in the left pane.

   The **Parameters** table appears as shown as shown below:![Options tab in the PUC (left) and PDI (right) Database Connection dialog boxes](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-91a9c0378490ed57d671309d99980a571afe99d1%2FssPUCanPDIDataConnectionOptions.png?alt=media)
3. In the next available row of the **Parameters** table, enter a valid parameter name and its corresponding value. For JDBC database-specific configuration help, click **Help**.

   A new browser window opens and displays additional information about configuring the JDBC connection for the database type that is currently selected in the **General** pane.
4. Click **Test**.

   A success message appears if the connection is established.
5. Click **OK** to close the connection test dialog box.
6. To save the connection, click **OK** to close the Database Connection dialog box.
