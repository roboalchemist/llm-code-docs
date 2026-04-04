# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor/edit-the-properties-file-for-report-designer.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor/edit-the-properties-file-for-report-designer.md

# Edit the properties file for Report Designer

1. On the workstation where you want to run Report Designer, [stop Report Designer](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/ba-design-tools/start-and-stop-ba-design-tools) and the Pentaho Server if it is running on the same workstation.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Navigate to the `.pentaho` directory in the user directory. For example, if the user name is `username` for Microsoft Windows, the Pentaho directory is`C:\Users\username\.pentaho\`, and for Linux or Solaris the directory is `/home/username/.pentaho/`.
3. Switch to the `~/.pentaho/simple-jndi/` subdirectory. If it does not exist, create it.
4. Edit the `default.properties` file found there.

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
5. Save and close the file.
6. In order for this change to take effect, restart the design tools and the server if the server and design tools are running on the same workstation.

You now have a properties file that defines a JNDI connection for Report Designer. Remember, if you run this tool on more than one workstation, repeat this process on all of the other workstations.
