# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/oci-protocol-information-pdi-only.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/oci-protocol-information-pdi-only.md

# OCI protocol information (PDI only)

Perform the following steps to create an OCI connection in the PDI Database Connection dialog box:

1. In the **Connection Name** field, enter a name that uniquely describes this connection.

   The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Database Type** list, select **Oracle**.
3. In the **Access** list, select **OCI**. The access protocol which appears depends on the database type you select.
4. In the **Settings** section, enter the following information as directed by the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm).

   | Field                  | Description                                                              |
   | ---------------------- | ------------------------------------------------------------------------ |
   | SID                    | The Oracle system ID that uniquely identifies the database on the system |
   | Tablespace for Data    | The name of the tablespace where the data is stored                      |
   | Tablespace for Indices | The name of the tablespace where the indices is stored                   |
   | User Name              | The user name used to connect to the database                            |
   | Password               | The password used to connect to the database                             |
5. Click **Test**.

   A success message appears if the connection is established.
6. Click **OK** to close the connection test dialog box.
7. To save the connection, click **OK** to close the Database Connection dialog box.

If you want to use **Advanced**, **Options**, or **Pooling** for your OCI connection, refer to the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm) to understand how to specify these settings.
