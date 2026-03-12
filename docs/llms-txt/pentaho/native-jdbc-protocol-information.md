# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/native-jdbc-protocol-information.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/native-jdbc-protocol-information.md

# Native (JDBC) protocol information

Perform the following steps to create a Native (JDBC) connection in the Database Connection dialog box:

1. In the **Connection Name** field, enter a name that uniquely describes this connection.

   The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Database Type** list, select the database you want to use (for example, MySQL or Oracle).
3. In the **Access** list, select **Native (JDBC)**. The access protocol which appears depends on the database type you select.
4. In the **Settings** section, enter the following information:

   | Field         | Description                                                                                                                               |
   | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
   | Host Name     | The name of the server that hosts the database to which you are connecting. Alternatively, you can specify the host by IP address.        |
   | Database Name | The name of the database to which you are connecting. If you are using a ODBC connection, enter the Data Source Name (DSN) in this field. |
   | Port Number   | The TCP/IP port number (if it is different from the default)                                                                              |
   | User Name     | Optional user name used to connect to the database                                                                                        |
   | Password      | Optional password used to connect to the database                                                                                         |
5. Click **Test**.

   A success message appears if the connection is established.
6. Click **OK** to close the connection test dialog box.
7. To save the connection, click **OK** to close the Database Connection dialog box.
   * In PUC, your connection name appears in the list of available data sources in the Manage Data Sources dialog box.
   * In PDI, your connection name appears under the **Database connections** folder in the **View** tab.
