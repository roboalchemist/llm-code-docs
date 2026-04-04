# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-postgresql-as-your-repository-database-manual-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-postgresql-as-your-repository-database-archive-installation/perform-tomcat-specific-connection-tasks/step-2-modify-jdbc-connection-information-in-the-tomcat-context.xml-file-postgresql-archive.md

# Step 2: Modify JDBC connection information in the Tomcat XML file

Database connection and network information, such as the username, password, driver class information, IP address or domain name, and port numbers for your Pentaho Repository database are stored in the `context.xml` file. Modify this file to reflect the database connection and network information for your operating environment. in this file.

**CAUTION:**

If you have a different port, password, user, driver class information, or IP address, make sure that you change the password and port number in these examples to match the ones in your configuration environment.

1. Consult your database documentation to determine the JDBC class name and the connection string for your Pentaho Repository database.
2. Navigate to the `server/pentaho-server/tomcat/webapps/pentaho/META-INF` directory and open the `context.xml` file with any text editor.
3. Add the following code to the file if it does not already exist.

   ```xml
   <Resource name="jdbc/Hibernate" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
           maxWait="10000" username="hibuser" password="password"
           driverClassName="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/hibernate"
           validationQuery="select 1" jdbcInterceptors="ConnectionState" defaultAutoCommit="true"/>
   <Resource name="jdbc/Audit" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
           maxWait="10000" username="hibuser" password="password"
           driverClassName="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/hibernate"
           validationQuery="select 1" />
   <Resource name="jdbc/Quartz" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0" maxWait="10000"
           username="pentaho_user" password="password" testOnBorrow="true"
           driverClassName="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/quartz"
           validationQuery="select 1"/>
   <Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
           maxWait="10000" username="hibuser" password="password"
           driverClassName="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/hibernate"
           validationQuery="select 1"/>
   <Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
           maxWait="10000" username="hibuser" password="password"
           driverClassName="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/hibernate"
           validationQuery="select 1"/>
   <Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0" maxWait="10000"
           username="hibuser" password="password" driverClassName="org.postgresql.Driver"
           url="jdbc:postgresql://localhost:5432/hibernate?searchpath=pentaho_dilogs"
           validationQuery="select 1"/>
   <Resource name="jdbc/SampleData" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
           maxWait="10000" username="pentaho_user" password="password"
           driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
           validationQuery="select 1"/>
   <Resource name="jdbc/SampleDataAdmin" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
           maxWait="10000" username="pentaho_admin" password="password"
           driverClassName="org.hsqldb.jdbcDriver" url="jdbc:hsqldb:hsql://localhost/sampledata"
           validationQuery="select 1"/>
   <Resource name="jdbc/jackrabbit" auth="Container" type="javax.sql.DataSource"
           factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory"
           maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
           maxWait="10000" username="jcr_user" password="password"
           driverClassName="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/jackrabbit"
           validationQuery="select 1" jdbcInterceptors="ConnectionState" defaultAutoCommit="true"/>
   ```
4. Modify the username, password, driver class information, IP address (or domain name), and port numbers to match the correct values for your environment.
5. Comment out any resource references that refer to other databases.
6. Verify that the **validationQuery** variable for your database is set to this: `validationQuery="select 1"`
7. Save the `context.xml` file and close it.
