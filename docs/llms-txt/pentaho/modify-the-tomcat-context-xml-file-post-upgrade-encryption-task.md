# Source: https://docs.pentaho.com/install/9.3-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/modify-the-tomcat-context-xml-file-post-upgrade-encryption-task.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/setting-up-password-encryption-after-upgrading-pentaho-upgrade-cp/modify-the-tomcat-context-xml-file-post-upgrade-encryption-task.md

# Modify the Tomcat context XML file

Database connection and network information for your Pentaho Repository database are stored in the `context.xml` file.

Perform the following steps to modify the `context.xml` file to reflect encryption password changes for your database connection and network information.

1. If you had any previous customizations to the `context.xml` file before upgrading and you have not already applied these customizations to the 10.2 version of the file, merge your customizations into the `context.xml` file. See [Apply customizations](https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/post-upgrade-tasks-pentaho-ugrade-cp/apply-customizations-post-upgrade-tasks) for instructions.

   **Note:** Password encryption requires the 9.1 or later version of the `context.xml` file.
2. Stop the Pentaho Server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
3. Navigate to the `pentaho/server/pentaho-server/tomcat/webapps/pentaho/META-INF` directory and open the `context.xml` file with any file editor.
4. Locate all occurrences of the following `factory` setting:

   ```xml
   factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
   ```
5. Replace every occurrence of the `factory` setting with the following value:

   ```xml
   factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
   ```
6. Locate the type of database you are using as the Pentaho Repository and add the following lines of code to the end of the `Resource` block to include Jackrabbit, which handles password encryption:
   * **Postgres**

     ```xml
     <Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource" factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0" maxWait="10000" username="jcr_user" password="password" driverClassName="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/jackrabbit" validationQuery="select 1"/>
     ```
   * **MySQL**

     ```xml
     <Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource" factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0" maxWait="10000" username="jcr_user" password="password" driverClassName="com.mysql.jdbc.Driver" url="jdbc:mysql://localhost:3306/jackrabbit" validationQuery="select 1"/>
     ```
   * **Oracle**

     Be sure to also replace `XE` in the URL setting to reflect the name of your schema:

     ```xml
     <Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource" factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0" maxWait="10000" username="jcr_user" password="password" driverClassName="oracle.jdbc.OracleDriver" url="jdbc:oracle:thin:@localhost:1521/XE" validationQuery="select 1 from dual"/>
     ```
   * **MS SQL Server**

     ```xml
     <Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource" factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0" maxWait="10000" username="jcr_user" password="password" driverClassName="com.microsoft.sqlserver.jdbc.SQLServerDriver" url="jdbc:sqlserver://localhost:1433;DatabaseName=jackrabbit" validationQuery="select 1"/>
     ```
7. Save and close the `context.xml` file.
8. Restart the server and confirm no errors occurred.

   For instructions on starting the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).

   Depending on the error, you may need to contact your customer support representative for help.

The `context.xml` is now modified to reflect encryption password changes for your database connection and network information.
