# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor/edit-the-properties-file-for-metadata-editor.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor/edit-the-properties-file-for-metadata-editor.md

# Edit the properties file for Metadata Editor

1. On the workstation where you want to run Metadata Editor, [stop Metadata Editor](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/ba-design-tools/start-and-stop-ba-design-tools) and the Pentaho Server if it is running on the same workstation.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Navigate to the `metadata-editor/simple_jndi` directory where you installed the Metadata Editor.
3. Edit the `JDBC.properties` file found there.

   If it does not exist, create it according to this example.

   ```xml
   SampleData/type=javax.sql.DataSource
   SampleData/driver=org.hsqldb.jdbcDriver
   SampleData/user=pentaho_user
   SampleData/password=password
   SampleData/url=jdbc:hsqldb:mem:SampleData

   ```

   In the example, `SampleData` is the name of the JNDI connection. Each line must begin with the JNDI connection name and a forward slash (/), followed by these required parameters.

   | Parameter    | Description                                                      |
   | ------------ | ---------------------------------------------------------------- |
   | **type**     | *javax.sql.DataSource* defines the JNDI data source type.        |
   | **driver**   | The driver class name provided by your database vendor.          |
   | **user**     | A user account that can connect to this database.                |
   | **password** | The password for the previously declared user.                   |
   | **url**      | The database connection string provided by your database vendor. |
4. Save and close the file.
5. For these changes to take effect, [restart the Metadata Editor](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/ba-design-tools/start-and-stop-ba-design-tools) and the Pentaho Server if it is running on the same workstation.

You now have a properties file that defines a JNDI connection for Metadata Editor. Remember, if you run this tool on more than one workstation, repeat this process on all the other workstations.
