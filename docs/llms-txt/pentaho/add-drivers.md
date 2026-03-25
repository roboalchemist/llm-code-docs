# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-jndi-connections-for-the-pentaho-server/add-drivers.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server/jdbc-database-connections/set-up-native-jdbc-or-oci-data-connections-for-the-pentaho-server/add-drivers.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor/add-drivers.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jdbc-or-oci-connections-for-ba-design-tools/add-drivers.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor/add-drivers.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jdbc-or-oci-connections-for-ba-design-tools/add-drivers.md

# Add drivers

The driver enables design tools to connect to the Pentaho Server and verify that the model is correct. Your database administrator, Chief Intelligence Officer, or IT manager should be able to provide the appropriate driver. If not, you can download drivers from your database vendor's website.

When you have the correct driver, copy it to these directories on all machines that run the design tools that you chose to install. Design tools should not be running when you copying the driver to the correct directories. Once the driver is in place, you can start the design tools:

* Aggregation Designer: `/pentaho/design-tools/agg-designer/drivers/`
* Metadata Editor: `/pentaho/design-tools/metadata-editor/libext/JDBC/`
* Report Designer: `/pentaho/design-tools/report-designer/lib/jdbc/`
* Schema Workbench: `/pentaho/design-tools/schema-workbench/drivers/`

There should be only one driver for your database in this directory. Ensure that there are no other versions of the same vendor's driver in this directory. If there are, back up the old driver files and remove them to avoid version conflicts. If you have any concerns about how to proceed, contact [Pentaho Support](https://support.pentaho.com).

## Driver for Microsoft SQL Server

If you are using a Microsoft SQL Server (MSSQL), you might need to use an alternative, non-vendor-supported driver called JTDS. Contact [Pentaho Support](https://support.pentaho.com) to ensure that you are adding the correct driver.

For Microsoft Windows, most JDBC drivers support Type 2 integrated authentication through the **integratedSecurity** connection string property. To use integrated authentication, copy the `sqljdbc_auth.dll` file to all machines and directories to which you copied the JDBC driver. You can find this file in this location:`<installation directory>\sqljdbc_<version>\<language>\auth\`

* Use the `sqljdbc_auth.dll` file in the x64 folder, if you are running a 64-bit JVM on a x64 processor.
* Use the `sqljdbc_auth.dll` file in the IA64 folder, you are running a 64-bit JVM on an Itanium processor.
