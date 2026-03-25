# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/open-the-connection-dialog-box/open-the-database-connection-dialog-box-from-pdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/open-the-connection-dialog-box/open-the-database-connection-dialog-box-from-pdi.md

# Open the Database Connection dialog box from PDI

Perform the following steps to open a new database connection in PDI:

1. Start the PDI client (Spoon) and create a new transformation or job.
2. In the **View** tab of the **Explorer** pane, double-click on the **Database connections** folder.

   The Database Connection dialog box appears, as shown below:![Database Connection dialog box](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-0b36ee4d927e030f0ff79f281fe32f337792b2a7%2FssPDIDataConnectionFromViewTabInExplorerPane.png?alt=media)
3. Enter your data connection information and test.

   See [Enter database connection information](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information) for further details.

In PDI, you can define connections to multiple databases provided by multiple database vendors such as MySQL and Oracle. PDI ships with the most suitable JDBC drivers for PostgreSQL, our default database.

Pentaho recommends avoiding ODBC connections. The ODBC to JDBC bridge driver does not always provide an exact match and adds another level of complexity, which affects performance. The only time you may have to use ODBC is if no JDBC driver is available. For details, see the [Pentaho Community article on why you should avoid ODBC](http://wiki.pentaho.com/pages/viewpage.action?pageId=14850644).

When you define a database connection in PDI, the connection information (such as the user name, password, and port number) is stored in the Pentaho Repository and is available to other users when they connect to the repository. If you are not using the Pentaho Repository, the database connection information is stored in the XML file associated with your transformation or job. See the **Pentaho Data Integration** document for details on the Pentaho Repository.

You must have information about your database (such as your database type, port number, user name and password) before you define a JDBC connection. In PDI, you can also set connection properties as variables. Through such variables, your transformations and jobs can access data from multiple database types.

Make sure to use clean ANSI SQL that works on all the database types used.
