# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-native-jdbc-or-oci-data-connections-for-the-pentaho-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-native-jdbc-or-oci-data-connections-for-the-pentaho-server.md

# Set up native (JDBC) or OCI data connections for the Pentaho Server

Once you have [Set up native (JDBC) or OCI data connections for the Pentaho Server](#GUID-31E63101-6538-4630-8730-8938D85F05A1), there are configuration and maintenance tasks that you need to perform.

## Add drivers

The Pentaho Server needs the appropriate driver to connect to the database that stores your data. Your database administrator, Chief Intelligence Officer, or IT manager should be able to provide the appropriate driver. If not, you can download drivers from your database vendor's website. The [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference) contains a list of drivers.

Once you have the correct driver, copy it to the following directories:

* Pentaho Server: `/pentaho/server/pentaho-server/tomcat/lib/`
* PDI client: `data-integration/lib`

**Note:** You must restart the PDI client for the driver to take effect.

There should be only one driver for your database in the directory. Ensure that there are no other versions of the same vendor's driver in this directory. If there are, back up the old driver files and remove them to avoid version conflicts. This is a concern when you are adding a driver for the same database type as your Pentaho Repository. If you have any concerns about how to proceed, contact [Pentaho Support](https://support.pentaho.com).

When the driver files are in place, restart the server.

### Driver for Microsoft SQL Server

If you are using a Microsoft SQL Server (MSSQL), you might need to use an alternative, non-vendor-supported driver called JTDS. Contact [Pentaho Support](https://support.pentaho.com) to ensure that you are adding the correct driver.

For Microsoft Windows, most JDBC drivers support Type 2 integrated authentication through the **integratedSecurity** connection string property. To use integrated authentication, copy the `sqljdbc_auth.dll` file to all machines and directories to which you copied the JDBC driver. You can find this file in the following location: `*&lt;installation directory&gt;*\sqljdbc_*&lt;version&gt;*\*&lt;language&gt;*\auth\`

| If running:                        | Use the sqljdbc\_auth.dll file here: |
| ---------------------------------- | ------------------------------------ |
| 64-bit JVM on a x64 processor      | x64 folder                           |
| 64-bit JVM on an Itanium processor | IA64 folder                          |
