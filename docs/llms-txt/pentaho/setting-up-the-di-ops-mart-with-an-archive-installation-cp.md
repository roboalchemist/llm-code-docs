# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/setting-up-the-di-ops-mart-with-an-archive-installation-cp.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pentaho-operations-mart/data-integration-operations-mart/setting-up-the-di-ops-mart-with-an-archive-installation-cp.md

# Setting up DI Operations Mart with an archive installation

Follow these instructions for setting up the Data Integration Operations Mart if you installed Pentaho with the Archive installation method. See the **Install Pentaho Data Integration and Analytics** document for details on Archive installation.

## Before you begin

Installation of the Data Integration Operations Mart depends on the following conditions and prerequisites.

### Archive installation of the Pentaho Server

The Data Integration Operations Mart installation instructions assume that you have installed the Pentaho Server with the archive installation method. If you need to review the installation instructions, see the **Install Pentaho Data Integration and Analytics** document.

### Required database

Before proceeding with the Data Integration Operations Mart installation steps, ensure that your Pentaho Server and Pentaho Repository are configured with one of the following database types:

* PostgreSQL
* MySQL or MariaDB
* Oracle
* MS SQL Server

### Data Integration Operations Mart scripts

To install the Data Integration Operations Mart, you must have the following two scripts:

* `pentaho_logging_*databasename*.sql`
* `pentaho_mart_*databasename*.sql`

**Note:** In the file name, *databasename* is the name of your Pentaho Server Repository database type:

* `postgresql`
* `mysql15` (MariaDB only)
* `oracle10g` or `oracle12c`
* `sqlserver`

## Process overview

To install the Data Integration Operations Mart, perform the following steps:

* [Step 1: Get the Data Integration Operations Mart files](#step-1-get-the-data-integration-operations-mart-files)
* [Step 2: Run the setup scripts](#step-2-run-the-setup-scripts)
* [Step 3: Set the global Kettle logging variables](#step-3-set-the-global-kettle-logging-variables)
* [Step 4: Add the JNDI connections for logging](#step-4-add-the-jndi-connections-for-logging)
* [Step 5: Add a JDBC connection for the Pentaho Server](#step-5-add-a-jdbc-connection-for-the-pentaho-server)
* [Step 6: Add the Data Integration Operations Mart ETL solutions to the Pentaho Repository default content folder](#step-6-add-the-data-integration-operations-mart-etl-solutions-to-the-pentaho-repository-default-cont)
* [Step 7: Initialize the Data Integration Operations Mart](#step-7-initialize-the-data-integration-operations-mart)
* [Step 8: Verify the Data Integration Operations Mart is working](#step-8-verify-the-data-integration-operations-mart-is-working)

### Step 1: Get the Data Integration Operations Mart files

Download Data Integration Operations Mart files that you need for [Step 6: Add the Data Integration Operations Mart ETL solutions to the Pentaho Repository default content folder](#step-6-add-the-data-integration-operations-mart-etl-solutions-to-the-pentaho-repository-default-cont).

Verify the following information before proceeding:

* If you performed an archive installation with a PostgreSQL repository, skip to [Step 2: Run the setup scripts](#step-2-run-the-setup-scripts).
* If you performed an archive installation with a MySQL, MS SQL Server, or Oracle repository, and you do not have the `pentaho-operations-mart-10.2.0.0-<build number>.zip` file, then you must download it from the [Support Portal](https://support.pentaho.com/home).

Perform the following steps to get the Data Integration Operations Mart files:

1. Download the `pentaho-server-ee-10.2.0.0-<build number>.zip` file from the [Support Portal](https://support.pentaho.com/home).
   1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
   2. In the Pentaho card, click **Download**.

      The Downloads page opens.
   3. In the **10.x** list, click **Pentaho 10.2 GA Release**.
   4. Scroll to the bottom of the Pentaho 10.2 GA Release page.
   5. In the file component section, click the `Operations Mart` folder.
   6. Download the `pentaho-operations-mart-10.2.0.0-<build number>.zip` file.
2. Unpack the `pentaho-operations-mart-10.2.0.0-<build number>.zip` file to a temporary directory.
3. In the temporary directory, verify that you have the following files that are required for [Step 6: Add the Data Integration Operations Mart ETL solutions to the Pentaho Repository default content folder](#step-6-add-the-data-integration-operations-mart-etl-solutions-to-the-pentaho-repository-default-cont)
   * `pentaho-operations-mart-operations-di-10.2.0.0-<build number>.zip`
   * `pentaho-operations-mart-operations-bi-10.2.0.0-<build number>.zip`
4. Verify that you have the two files that are required for the repository database type.

   The following table lists the required files for each type of repository database.

| Repository database type | Required files                                                                                                                           |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Oracle                   | `pentaho-operations-mart-etl-oracle10g-10.2.0.0-<build number>.zip``pentaho-operations-mart-clean-oracle10g-10.2.0.0-<build number>.zip` |
| MySQL5                   | `pentaho-operations-mart-etl-mysql5-10.2.0.0-<build number>.zip``pentaho-operations-mart-clean-mysql5-10.2.0.0-<build number>.zip`       |
| MS SQL Server            | `pentaho-operations-mart-etl-mssql10.2.0.0-<build number>.zip``pentaho-operations-mart-clean-mssql-10.2.0.0-<build number>.zip`          |

### Step 2: Run the setup scripts

When you performed the Archive installation of the Pentaho Server, you downloaded the `pentaho-server-ee-10.2.0.0-<build number>.zip` file, which contains both the required Operations Mart setup scripts. The scripts are located in the `<install-directory>/pentaho-server/data/<databasename>` directory where`<database name>` is one of the following Pentaho Server Repository database types:

* `postgresql`
* `mysql5` (MariaDB only)
* `oracle10g` or `oracle12c`
* `sqlserver`

Depending on the database repository type, run the following scripts, in the order, to create the tables that log the activity for transformations and jobs.

1. `pentaho_logging_<database name>.sql`
2. `pentaho_mart_<database name>.sql`

### Step 3: Set the global Kettle logging variables

Perform this step on the computer where you have installed your Pentaho Data Integration (PDI) client and the Pentaho Server.

When you run PDI for the first time, the `kettle.properties` file is created and stored in the `$USER_HOME/.kettle.properties` directory.

1. In the PDI client, select **Edit** > **Edit the kettle.properties file**.
2. Add or edit the values for each of the logging variables shown in the following log tables:

   **Note:** If you customized the values for these logging variables in the following scripts, add the customized values for your site rather than the default values shown in the table.

   * `pentaho_logging_*databasename*.sql`
   * `pentaho_mart_*databasename*.sql`\
     where *databasename* is your database type.

   **Note:** For Oracle and Microsoft SQL Server, leave **Value** blank with **Variables** that contain '*SCHEMA*' in the name.

   | Variable                       | Value               |
   | ------------------------------ | ------------------- |
   | *KETTLE\_CHANNEL\_LOG\_DB*     | `live_logging_info` |
   | *KETTLE\_CHANNEL\_LOG\_TABLE*  | `channel_logs`      |
   | *KETTLE\_CHANNEL\_LOG\_SCHEMA* | `pentaho_dilogs`    |

   | Variable                        | Value               |
   | ------------------------------- | ------------------- |
   | *KETTLE\_JOBENTRY\_LOG\_DB*     | `live_logging_info` |
   | *KETTLE\_JOBENTRY\_LOG\_TABLE*  | `jobentry_logs`     |
   | *KETTLE\_JOBENTRY\_LOG\_SCHEMA* | `pentaho_dilogs`    |

   | Variable                   | Value               |
   | -------------------------- | ------------------- |
   | *KETTLE\_JOB\_LOG\_DB*     | `live_logging_info` |
   | *KETTLE\_JOB\_LOG\_TABLE*  | `job_logs`          |
   | *KETTLE\_JOB\_LOG\_SCHEMA* | `pentaho_dilogs`    |

   | Variable                       | Value               |
   | ------------------------------ | ------------------- |
   | *KETTLE\_METRICS\_LOG\_DB*     | `live_logging_info` |
   | *KETTLE\_METRICS\_LOG\_TABLE*  | `metrics_logs`      |
   | *KETTLE\_METRICS\_LOG\_SCHEMA* | `pentaho_dilogs`    |

   | Variable                    | Value               |
   | --------------------------- | ------------------- |
   | *KETTLE\_STEP\_LOG\_DB*     | `live_logging_info` |
   | *KETTLE\_STEP\_LOG\_TABLE*  | `step_logs`         |
   | *KETTLE\_STEP\_LOG\_SCHEMA* | `pentaho_dilogs`    |

   | Variable                     | Value               |
   | ---------------------------- | ------------------- |
   | *KETTLE\_TRANS\_LOG\_DB*     | `live_logging_info` |
   | *KETTLE\_TRANS\_LOG\_TABLE*  | `trans_logs`        |
   | *KETTLE\_TRANS\_LOG\_SCHEMA* | `pentaho_dilogs`    |

   | Variable                                  | Value               |
   | ----------------------------------------- | ------------------- |
   | *KETTLE\_TRANS\_PERFORMANCE\_LOG\_DB*     | `live_logging_info` |
   | *KETTLE\_TRANS\_PERFORMANCE\_LOG\_TABLE*  | `transperf_logs`    |
   | *KETTLE\_TRANS\_PERFORMANCE\_LOG\_SCHEMA* | `pentaho_dilogs`    |

### Step 4: Add the JNDI connections for logging

This section explains how to add the logging (**live\_logging\_info**) and Operations Mart (**PDI\_Operations\_Mart**) connections for a PDI client.

1. Navigate to the PDI client `<install directory>/data-integration/simple-jndi` directory.
2. Open the `jdbc.properties` file with a text editor.
3. Depending on your repository database type, update the values accordingly (URL, users, password) as shown in the following samples.

   PostgreSQL:

   ```xml
    PDI_Operations_Mart/type=javax.sql.DataSource
   PDI_Operations_Mart/driver=org.postgresql.Driver
   PDI_Operations_Mart/url=jdbc:postgresql://localhost:5432/hibernate?searchpath=pentaho_operations_mart
   PDI_Operations_Mart/user=hibuser
   PDI_Operations_Mart/password=password
   live_logging_info/type=javax.sql.DataSource
   live_logging_info/driver=org.postgresql.Driver
   live_logging_info/url=jdbc:postgresql://localhost:5432/hibernate?searchpath=pentaho_dilogs
   live_logging_info/user=hibuser
   live_logging_info/password=password
   ```

   MySQL:

   ```xml
   PDI_Operations_Mart/type=javax.sql.DataSource
   PDI_Operations_Mart/driver=com.mysql.jdbc.Driver
   PDI_Operations_Mart/url=jdbc:mysql://localhost:3306/pentaho_operations_mart
   PDI_Operations_Mart/user=hibuser
   PDI_Operations_Mart/password=password
   live_logging_info/type=javax.sql.DataSource
   live_logging_info/driver=com.mysql.jdbc.Driver
   live_logging_info/url=jdbc:mysql://localhost:3306/pentaho_dilogs
   live_logging_info/user=hibuser
   live_logging_info/password=password
   ```

   MariaDB:

   ```xml
   PDI_Operations_Mart/type=javax.sql.DataSource
   PDI_Operations_Mart/driver=com.mariadb.jdbc.Driver
   PDI_Operations_Mart/url=jdbc:mariadb://localhost:3306/pentaho_operations_mart
   PDI_Operations_Mart/user=hibuser
   PDI_Operations_Mart/password=password
   live_logging_info/type=javax.sql.DataSource
   live_logging_info/driver=com.mariadb.jdbc.Driver
   live_logging_info/url=jdbc:mariadb://localhost:3306/pentaho_dilogs
   live_logging_info/user=hibuser
   live_logging_info/password=password
   ```

   Oracle:

   ```xml
   PDI_Operations_Mart/type=javax.sql.DataSource
   PDI_Operations_Mart/driver=oracle.jdbc.OracleDriver
   PDI_Operations_Mart/url=jdbc:oracle:thin:@localhost:1521/XE
   PDI_Operations_Mart/user=pentaho_operations_mart
   PDI_Operations_Mart/password=password
   live_logging_info/type=javax.sql.DataSource
   live_logging_info/driver=oracle.jdbc.OracleDriver
   live_logging_info/url=jdbc:oracle:thin:@localhost:1521/XE
   live_logging_info/user=pentaho_dilogs
   live_logging_info/password=password
   ```

   Microsoft SQL Server:

   ```xml
   PDI_Operations_Mart/type=javax.sql.DataSource
   PDI_Operations_Mart/driver=com.microsoft.sqlserver.jdbc.SQLServerDriver
   PDI_Operations_Mart/url=jdbc:sqlserver://10.0.2.15:1433;DatabaseName=pentaho_operations_mart
   PDI_Operations_Mart/user=pentaho_operations_mart
   PDI_Operations_Mart/password=password
   live_logging_info/type=javax.sql.DataSource
   live_logging_info/driver=com.microsoft.sqlserver.jdbc.SQLServerDriver
   live_logging_info/url=jdbc:sqlserver://10.0.2.15:1433;DatabaseName=pentaho_dilogs
   live_logging_info/user=dilogs_user
   live_logging_info/password=password
   ```

### Step 5: Add a JDBC connection for the Pentaho Server

This section explains how to add a JDBC connection for the Pentaho Server. Perform this task on the machine where you have installed the Pentaho Server.

1. Navigate to the `<install directory>/server/pentaho-server/tomcat/webapps/Pentaho/META-INF/` folder.
2. Open the `context.xml` file with a text editor.
3. Depending on your database type, edit the file to reflect the values, as shown in the following examples.
4. (Optional) If you want to use encrypted passwords, locate all occurrences of the `factory` setting and replace them with the following value:

   `factory="org.pentaho.di.core.database.util.DecryptingDataSourceFactory`

   PostgreSQL:

   ```xml
    <Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax.sql.DataSource"
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" 
               url="jdbc:postgresql://localhost:5432/hibernate"
               validationQuery="select 1"/>
              
    <Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax.sql.DataSource"
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" 
               url="jdbc:postgresql://localhost:5432/hibernate"
               validationQuery="select 1"/>
              
    <Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql.DataSource"
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" minIdle="0" maxIdle="5" initialSize="0"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.postgresql.Driver" 
               url="jdbc:postgresql://localhost:5432/hibernate?searchpath=pentaho_dilogs"            
               validationQuery="select 1"/>
   ```

   MySQL:

   ```xml
     <Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax.sql.DataSource"
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" maxIdle="5"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="com.mysql.jdbc.Driver" url="jdbc:mysql://localhost:3306/pentaho_operations_mart"
               jdbcInterceptors="ConnectionState" defaultAutoCommit="true" validationQuery="select 1"/>
              
     <Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax.sql.DataSource"
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" maxIdle="5"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="com.mysql.jdbc.Driver" url="jdbc:mysql://localhost:3306/pentaho_operations_mart"
               jdbcInterceptors="ConnectionState" defaultAutoCommit="true" validationQuery="select 1"/>
               
     <Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql.DataSource"
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" maxIdle="5"
               maxWait="10000" username="hibuser" password="password"
               driverClassName="com.mysql.jdbc.Driver" url="jdbc:mysql://localhost:3306/pentaho_dilogs"            
               jdbcInterceptors="ConnectionState" defaultAutoCommit="true" validationQuery="select 1"/>
   ```

   MariaDB:

   ```xml
     <Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax. sql.DataSource" 
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" maxIdle="5" 
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.mariadb.jdbc.Driver" url="jdbc:mariadb://localhost:3306/pentaho_operations_mart" 
               jdbcInterceptors="ConnectionState" defaultAutoCommit="true" validationQuery="select 1"/> 

     <Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax. sql.DataSource" 
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" maxIdle="5" 
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.mariadb.jdbc.Driver" url="jdbc:mariadb://localhost:3306/pentaho_operations_mart" 
               jdbcInterceptors="ConnectionState" defaultAutoCommit="true" validationQuery="select 1"/> 

     <Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql. DataSource" 
               factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxActive="20" maxIdle="5" 
               maxWait="10000" username="hibuser" password="password"
               driverClassName="org.mariadb.jdbc.Driver" url="jdbc:mariadb://localhost:3306/pentaho_dilogs" 
               jdbcInterceptors="ConnectionState" defaultAutoCommit="true" validationQuery="select 1"/>
   ```

   Oracle:

   ```xml
   <Resource 
       validationQuery="select 1 from dual"
       url="jdbc:oracle:thin:@localhost:1521/orcl"
       driverClassName="oracle.jdbc.OracleDriver"
       password="password"
       username="pentaho_operations_mart"
       initialSize="0"
       maxActive="20"
       maxIdle="10"
       maxWait="10000"
       factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
       type="javax.sql.DataSource"
       auth="Container"
       connectionProperties="oracle.jdbc.J2EE13Compliant=true"
       name="jdbc/pentaho_operations_mart"/>

   <Resource 
       validationQuery="select 1 from dual"
       url="jdbc:oracle:thin:@localhost:1521/orcl"
       driverClassName="oracle.jdbc.OracleDriver"
       password="password"
       username="pentaho_operations_mart"
       initialSize="0"
       maxActive="20"
       maxIdle="10"
       maxWait="10000"
       factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
       type="javax.sql.DataSource"
       auth="Container"
       connectionProperties="oracle.jdbc.J2EE13Compliant=true"
       name="jdbc/PDI_Operations_Mart"/>

   <Resource validationQuery="select 1 from dual" url="jdbc:oracle:thin:@localhost:1521/XE" 
        driverClassName="oracle.jdbc.OracleDriver" password="password" 
        username="pentaho_dilogs" maxWaitMillis="10000" maxIdle="5" maxTotal="20" 
        jdbcInterceptors="ConnectionState" defaultAutoCommit="true" 
        factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" type="javax.sql.DataSource" 
        auth="Container" name="jdbc/live_logging_info"/>
   ```

   Microsoft SQL Server:

   ```xml
   <Resource name="jdbc/PDI_Operations_Mart" auth="Container" type="javax.sql.DataSource"
         factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxTotal="20" maxIdle="5"
         maxWaitMillis="10000" username="pentaho_operations_mart" password="password" 
         jdbcInterceptors="ConnectionState" defaultAutoCommit="true"
         driverClassName="com.microsoft.sqlserver.jdbc.SQLServerDriver" 
         url="jdbc:sqlserver://localhost:1433;DatabaseName=pentaho_operations_mart"
         validationQuery="select 1"/>
               
   <Resource name="jdbc/pentaho_operations_mart" auth="Container" type="javax.sql.DataSource"
          factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxTotal="20" maxIdle="5"
          maxWaitMillis="10000" username="pentaho_operations_mart" password="password" 
          jdbcInterceptors="ConnectionState" defaultAutoCommit="true"
          driverClassName="com.microsoft.sqlserver.jdbc.SQLServerDriver" 
          url="jdbc:sqlserver://localhost:1433;DatabaseName=pentaho_operations_mart"
          validationQuery="select 1"/>
    
   <Resource name="jdbc/live_logging_info" auth="Container" type="javax.sql.DataSource"
           factory="org.apache.tomcat.jdbc.pool.DataSourceFactory" maxTotal="20" maxIdle="5"
           maxWaitMillis="10000" username="dilogs_user" password="password" 
           jdbcInterceptors="ConnectionState" defaultAutoCommit="true"
           driverClassName="com.microsoft.sqlserver.jdbc.SQLServerDriver" 
           url="jdbc:sqlserver://localhost:1433;DatabaseName=pentaho_dilogs"            
           validationQuery="select 1"/>
   ```

### Step 6: Add the Data Integration Operations Mart ETL solutions to the Pentaho Repository default content folder

If you are using PostgreSQL as your repository database, you can skip to [Step 7: Initialize the Data Integration Operations Mart](#step-7-initialize-the-data-integration-operations-mart).

Perform the following steps to add Data Integration Operations Mart ETL solutions to the Pentaho Repository default content folder:

1. Stop the Pentaho Server.
2. Depending on your repository database type, locate the ZIP files containing the ETL solution and sample reports.

   You downloaded and unpacked these files in [Step 1: Get the Data Integration Operations Mart files](#step-1-get-the-data-integration-operations-mart-files).

   * `pentaho-operations-mart-operations-di-9.3.0.zip`
   * `pentaho-operations-mart-operations-bi-9.3.0.zip`\
     Additionally, locate the two ZIP files that are specific to your repository type:

| Directory              | File names                                                                                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/oracle (10g or 12c)` | <ul><li><code>pentaho-operations-mart-etl-oracle10g-9.3.0.zip</code></li><li><code>pentaho-operations-mart-clean-oracle10g-9.3.0.zip</code></li></ul> |
| `/mysql5`              | <ul><li><code>pentaho-operations-mart-etl-mysql5-9.3.0.zip</code></li><li><code>pentaho-operations-mart-clean-mysql5-9.3.0.zip</code></li></ul>       |
| `/sqlserver`           | <ul><li><code>pentaho-operations-mart-etl-mssql-9.3.0.zip</code></li><li><code>pentaho-operations-mart-clean-mssql-9.3.0.zip</code></li></ul>         |

3\. Copy all four ZIP files \\(di, bi, mart-etl, mart-clean\\) for your database to this directory:

```
`$PENTAHO_HOME/pentaho-server/pentaho-solution/system/default-content`

-   DI Operations Mart sample reports: pentaho-operations-mart-operations-di-9.3.0-dist.zip
-   BA Operations Mart sample reports: pentaho-operations-mart-operations-bi-9.3.0-dist.zip
```

4\. Start the Pentaho Server.

```
When you restart the Pentaho Server, the startup process unpacks the content in the ZIP files to generate the Pentaho User Console \(PUC\) reports, sample transformations, and sample jobs needed to use the Data Integration Operations Mart.

**Note:** After these files are processed by the Pentaho Server, they are renamed with a timestamp so that each subsequent time you start the Pentaho Server, it does not unzip them again. You must keep these files in this directory, even though the date/timestamp is the installation date.
```

See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

### Step 7: Initialize the Data Integration Operations Mart

Perform these steps for the Operations Mart to start creating and collecting log file content.

1. Launch the PDI client (Spoon).
2. Connect to the Pentaho Repository through the Pentaho Server.
3. At the main menu, select **File** > **Open**.
4. Select **Browse Files** > **Public** > **Pentaho Operations Mart** > **DI Ops Mart ETL**.

   ![List of DI Ops Mart files in PDI Client folder](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-7b1ab03789be7a89a9bd02995d954059ec37b25e%2FPUC_Browse_Ops_Mart_folder_list_of_jobs_transforms_500.png?alt=media)
5. To initiate the transformation and job logging processes, open each transformation and job.
6. In each transformation or job, open the associated Job Properties or Transformation Properties window and click the **Logging** tab.
   * For logging to occur, you must at a minimum add a value to each individual **Log Connection** field shown in the tables below for jobs and transformations. A best practice tip for these fields is to use the global variables, as shown in the tables. You can also use the values you customized for your site and defined in the `kettle.properties` file during [Step 3: Set the global Kettle logging variables](#step-3-set-the-global-kettle-logging-variables).
   * If you leave all three fields shown in each table as empty values, then no logging occurs.
   * Logging also occurs if you add a value to all three fields, as shown in each table.
   * For job logging, add values to the **Log connection**, **Log table schema**, and **Log table name** fields as shown in the tables below for the **Job log table**, **Job entry log table**, and **Logging channel log table** in the **Log** tab. You can also use any values you have customized for your site.

     ![Job properties window, Logging tab](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-8a0990e7fbc65046ed967a4d314e28903bc13e89%2FPDI_TransJob_JobPropScreen_LoggingTab_500.png?alt=media)

     | Field                | Value                           |
     | -------------------- | ------------------------------- |
     | **Log connection**   | **${KETTLE\_JOB\_LOG\_DB**}     |
     | **Log table schema** | **${KETTLE\_JOB\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_JOB\_LOG\_TABLE}**  |

     | Field                | Value                                |
     | -------------------- | ------------------------------------ |
     | **Log connection**   | **${KETTLE\_JOBENTRY\_LOG\_DB}**     |
     | **Log table schema** | **${KETTLE\_JOBENTRY\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_JOBENTRY\_LOG\_TABLE}**  |

     | Field                | Value                               |
     | -------------------- | ----------------------------------- |
     | **Log connection**   | **${KETTLE\_CHANNEL\_LOG\_DB}**     |
     | **Log table schema** | **${KETTLE\_CHANNEL\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_CHANNEL\_LOG\_TABLE}**  |
   * For transformation logging, add values to the **Log connection**, **Log table schema**, and **Log table name** fields as shown in the following tables for the **Transformation**, **Step**, **Performance**, **Logging channels**, and **Metrics** in the **Logging** tab. You can also use a value you have customized for your site.

     ![Transformation properties window, Logging tab](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-6223ef10ef4c4c25b5b71ecad5a5a4bb3ad36141%2FPDI_TransStep_TransPropScreen_LoggingTab_500.png?alt=media)

     | Field                | Value                             |
     | -------------------- | --------------------------------- |
     | **Log connection**   | **${KETTLE\_TRANS\_LOG\_DB}**     |
     | **Log table schema** | **${KETTLE\_TRANS\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_TRANS\_LOG\_TABLE}**  |

     | Field                | Value                            |
     | -------------------- | -------------------------------- |
     | **Log connection**   | **${KETTLE\_STEP\_LOG\_DB}**     |
     | **Log table schema** | **${KETTLE\_STEP\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_STEP\_LOG\_TABLE}**  |

     | Field                | Value                                          |
     | -------------------- | ---------------------------------------------- |
     | **Log connection**   | **${KETTLE\_TRANS\_PERFORMANCE\_LOG\_DB}**     |
     | **Log table schema** | **${KETTLE\_TRANS\_PERFORMANCE\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_TRANS\_PERFORMANCE\_LOG\_TABLE}**  |

     | Field                | Value                               |
     | -------------------- | ----------------------------------- |
     | **Log connection**   | **${KETTLE\_CHANNEL \_LOG\_DB}**    |
     | **Log table schema** | **${KETTLE\_CHANNEL\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_CHANNEL\_LOG\_TABLE}**  |

     | Field                | Value                               |
     | -------------------- | ----------------------------------- |
     | **Log connection**   | **${KETTLE\_METRICS\_LOG\_DB}**     |
     | **Log table schema** | **${KETTLE\_METRICS\_LOG\_SCHEMA}** |
     | **Log table name**   | **${KETTLE\_METRICS\_LOG\_TABLE}**  |
7. In the main menu, select **File** > **Open**.
8. Select **Browse Files** > **Public** > **Pentaho Operations Mart** > **DI Ops Mart ETL** > **Fill\_in\_DIM\_DATE\_and\_DIM\_TIME** job file and run it.
9. Run a few of the sample KTRs, to generate logging activities for [Step 8: Verify the Data Integration Operations Mart is working](#step-8-verify-the-data-integration-operations-mart-is-working). You can also use or create your own sample KTRs.
10. At the main menu, select **File** > **Open**.
11. Select **Public Pentaho Operations Mart DI Ops Mart ETL** > **Update\_Dimensions\_then\_Logging\_Data** job file and run it.

    All the transformations and jobs are placed in the Pentaho Repository, then the data mart is populated. You can then set your transformations and jobs to run on a schedule, based on how often you want this data refreshed.

### Step 8: Verify the Data Integration Operations Mart is working

* From the Pentaho User Console, select **Browse Files** > **Public** > **Pentaho Operations Mart** > **DI Audit Reports** > **Last\_Run** and open it.
* Verify that the jobs and transformations in [Step 7: Initialize the Data Integration Operations Mart](#step-7-initialize-the-data-integration-operations-mart) were run.
