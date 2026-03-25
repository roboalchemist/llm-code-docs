# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/add-drivers/driver-for-microsoft-sql-server.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-native-jdbc-or-oci-data-connections-for-the-pentaho-server/add-drivers/driver-for-microsoft-sql-server.md

# Driver for Microsoft SQL Server

If you are using a Microsoft SQL Server (MSSQL), you might need to use an alternative, non-vendor-supported driver called JTDS. Contact [Pentaho Support](https://support.pentaho.com) to ensure that you are adding the correct driver.

For Microsoft Windows, most JDBC drivers support Type 2 integrated authentication through the **integratedSecurity** connection string property. To use integrated authentication, copy the `sqljdbc_auth.dll` file to all machines and directories to which you copied the JDBC driver. You can find this file in the following location: `*&lt;installation directory&gt;*\sqljdbc_*&lt;version&gt;*\*&lt;language&gt;*\auth\`

| If running:                        | Use the sqljdbc\_auth.dll file here: |
| ---------------------------------- | ------------------------------------ |
| 64-bit JVM on a x64 processor      | x64 folder                           |
| 64-bit JVM on an Itanium processor | IA64 folder                          |
