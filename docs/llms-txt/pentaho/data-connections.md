# Source: https://docs.pentaho.com/pba/pentaho-user-console/modern-design/data-connections.md

# Data Connections

Use the Data Connections component to connect Pentaho to third-party services that store your data. While connected, you can use that data to create analysis reports, interactive reports, and dashboards.

## Add a data connection

To add a data connection, complete the following steps:&#x20;

1. Log into the Pentaho User Console.
2. Open **Data Connections** by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click **Data Connections**.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Data Connections.**

   **Data Connections** opens with a list of connections shown in a table.&#x20;
3. Click **+ Add Connection**. The **Where is your data?** window opens.
4. For the database to which you want to connect, click **Connect**. You can connect to the following options:&#x20;
   * Generic database
   * Hypersonic
   * MonetDB
   * PostgreSQL
   * Snowflake
5. In the configuration window that opens, enter database connection information for your new connection. The type of database connection information entered depends on your access protocol. Refer to the examples in the following sections of this topic for Native (JDBC) protocols:
   * [Native (JDBC) protocol information](#native-jdbc-protocol-information)
   * [JNDI protocol information](#jndi-protocol-information)
6. (Optional) To test the connect, in the Connection information section, click **Test connection**.
7. Click **Connect**. The connection is established and saved in the Modern Design of PUC.

### Native (JDBC) protocol information

Create a Native (JDBC) connection in the Database Connection dialog box by completing the following steps:

1. In the **Connection Name** field, enter a name that uniquely describes this connection.

   The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Connection Type** list, select the database you want to use (for example, MySQL or Oracle).
3. In the **Access** **Type** list, select **Native (JDBC)**. The access protocol which appears depends on the database type you select.
4. In the **Settings** section, enter the following information:

   <table><thead><tr><th width="159">Field</th><th>Description</th></tr></thead><tbody><tr><td>Host Name</td><td>The name of the server that hosts the database to which you are connecting. Alternatively, you can specify the host by IP address.</td></tr><tr><td>Database Name</td><td>The name of the database to which you are connecting. If you are using an ODBC connection, enter the Data Source Name (DSN) in this field.</td></tr><tr><td>Port Number</td><td>The TCP/IP port number (if it is different from the default)</td></tr><tr><td>Username</td><td>Optional user name used to connect to the database</td></tr><tr><td>Password</td><td>Optional password used to connect to the database</td></tr></tbody></table>
5. Click **Test Connection**. A success message appears if the connection is established.
6. Click **OK** to close the connection test dialog box.
7. To save the connection, click **Save**. The database connection is saved and appears in the **Database Connections** list.

### JNDI protocol information

If you are publishing to the Pentaho Server from the Modern Design of the Pentaho User Console, edit your connection information to match the JNDI connection information of your application server data sources.

By configuring a JNDI connection in the Modern Design of PUC, your application server will not be continuously running during the development and testing of transformations.&#x20;

## Edit a data connection

1. Log into the Pentaho User Console.
2. Open **Data Connections** by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click **Data Connections**.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Data Connections.**

   **Data Connections** opens with a list of connections shown in a table.
3. Browse or search for the connection you want to edit.&#x20;
4. In the rightmost column of the Connections table, for the connection you want to edit, click the **More Actions** icon, and then select **Open**.
5. In the connection page that opens, click **Edit**.
6. In the configuration window that opens, edit database connection information.&#x20;

## Edit data connections

To delete one or more connections, complete the following steps:

1. Log into the Pentaho User Console.
2. Open **Data Connections** by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click **Data Connections**.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Data Connections.**

   **Data Connections** opens with a list of connections shown in a table.
3. Browse or search for the connections you want to delete.
4. Select one or more connections to delete.

   **Note:** You can select all connections by clicking the checkbox at the top of the page that shows that selected versus available values.&#x20;
5. Click **Delete**.
