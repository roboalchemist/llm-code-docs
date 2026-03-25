# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/set-up-a-cluster.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/set-up-a-cluster.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/set-up-a-cluster.md

# Set up a cluster

A Pentaho node consists of a Tomcat Web App server and the Pentaho Server. Multiple nodes that are joined make up a cluster. You can create a cluster using any version of Pentaho Suite 6.x or later.

The following topics explain how to cluster the application server:

* [Step 1: Address prerequisites for clustering](#step-1-address-prerequisites-for-clustering)
* [Step 2: Initialize and configure repository](#step-2-initialize-and-configure-repository)
* [Step 3: Configure Jackrabbit Journal](#step-3-configure-jackrabbit-journal)
* [Step 4: Configure Quartz](#step-4-configure-quartz)
* [Step 5: Start and test the cluster](#step-5-start-and-test-the-cluster)

## Step 1: Address prerequisites for clustering

Before you begin the process of clustering your servers, a few tasks need to be preformed and some specific requirements must be met to successfully implement a Pentaho deployment on a Tomcat cluster. The following table describes these tasks and requirements:

| Requirement                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Make sure that all of your application nodes are set up with identical configurations and Pentaho deployments.                                                                                                                   | Your application nodes all need the same configurations and Pentaho deployments installed already in order for clustering to work.                                                                                                                                                                                                            |
| Establish a load balancer.                                                                                                                                                                                                       | This will make sure that computing resources are spread evenly among the nodes.                                                                                                                                                                                                                                                               |
| Each node and the load balancer must be time-synchronized via NTP.                                                                                                                                                               | All machines that make up the cluster have to have the same system time. If they do not, execution times of objects will be effected.                                                                                                                                                                                                         |
| You must run only one node per machine (or NIC).                                                                                                                                                                                 | It is possible to run multiple application servers on each node with a modified configuration, but this scenario does not offer any benefit for load balancing (performance) or hardware failover (redundancy), and therefore is not covered in this guide. Refer to your application server's clustering documentation for more information. |
| You must use the supported version of Tomcat (either default archive installation or manual installation). See the **Components reference** in the **Try Pentaho Data Integration and Analytics** document for more information. | You may be able to use this guide as a basic blueprint for configuring other application servers or versions of Tomcat for a clustered environment, but Pentaho support will not be able to assist you if you run into any problems with the Pentaho Server.                                                                                  |
| You must have permission to install software and modify service configurations.                                                                                                                                                  | If you do not have permissions, you must have access to someone at your company who does have the correct permission levels, typically root access.                                                                                                                                                                                           |
| Only the Pentaho Server will be deployed to the cluster.                                                                                                                                                                         | It is possible to modify the configuration to deploy other WARs or EARs. However, for ease of testing and support, Pentaho only supports deployment of the `pentaho` and `pentaho-style` WARs to the cluster.                                                                                                                                 |
| You must use a single repository location.                                                                                                                                                                                       | Most people use a database-based solution repository. Keep in mind that you are not clustering the database server in this procedure, only the application server.                                                                                                                                                                            |
| You must have sticky sessions enabled.                                                                                                                                                                                           | This will tie your session to a single node.                                                                                                                                                                                                                                                                                                  |

## Step 2: Initialize and configure repository

After you have determined that your systems meet all of the requirements listed in the checklist, you need to first initialize and then configure the repository for clustering. Finally, you need to verify your clustering setup, before you move on to setting up the Jackrabbit journal:

1. Initialize your database using the appliable steps for your type of installation and database found in the **Install Pentaho Data Integration and Analytics** document.
2. After you have initialized your database, configure the data connections to the Pentaho Repository. **Define data connections** in the **Install Pentaho Data Integration and Analytics** document walks you through the steps for JDBC and JNDI connections for PostgreSQL, MySQL, and Oracle.
3. Configure your repository using the appliable steps for your type of installation and database found in the **Install Pentaho Data Integration and Analytics** document.
4. After you have initialized and configured your repository, you should clean up these files by following these steps.
   * Locate the `pentaho-server/tomcat` directory and remove all files and folders from the `temp` folder.
   * Locate the `pentaho-server/tomcat` directory and remove all files and folders from the `work` folder.
   * Locate the `pentaho-server/pentaho-solutions/system/jackrabbit/repository` directory and remove all files and folders from the final `repository` folder.
   * Locate the `pentaho-server/pentaho-solutions/system/jackrabbit/repository` directory and remove all files and folders from the `workspaces` folder.

You now have a configured repository and are ready to move to the next step for clustering.

## Step 3: Configure Jackrabbit Journal

These following steps show how to set up the Jackrabbit journal for your cluster (make sure that each node has a unique ID):

1. Locate the `repository.xml` file in the `pentaho-server/pentaho-solutions/system/jackrabbit` directory and open it with any text editor.
2. Scroll to the bottom of the file and replace the section that begins with `<!-- Run with a cluster journal -->` with the correct code for your type of database repository.

   For PostgreSQL only:

   ```xml
   <!--
   Run with a cluster journal
   -->
   <Cluster id="Unique_ID">
       <Journal class="org.apache.jackrabbit.core.journal.DatabaseJournal">
         <param name="revision" value="${rep.home}/revision.log"/>
         <param name="url" value="jdbc:postgresql://HOSTNAME:PORT/jackrabbit"/>
         <param name="driver" value="org.postgresql.Driver"/>
         <param name="user" value="jcr_user"/>
         <param name="password" value="password"/>
         <param name="databaseType" value="postgresql"/>
         <param name="janitorEnabled" value="true"/>
         <param name="janitorSleep" value="86400"/>
         <param name="janitorFirstRunHourOfDay" value="3"/>
       </Journal>
   </Cluster>
   ```

   For MySQL only:

   ```xml
   <!--
   Run with a cluster journal
   -->
   <Cluster id="Unique_ID">
       <Journal class="org.apache.jackrabbit.core.journal.DatabaseJournal">
         <param name="revision" value="${rep.home}/revision.log"/>
         <param name="url" value="jdbc:mysql://HOSTNAME:PORT/jackrabbit"/>
         <param name="driver" value="com.mysql.jdbc.Driver"/>
         <param name="user" value="jcr_user"/>
         <param name="password" value="password"/>
         <param name="schema" value="mysql"/>
         <param name="databaseType" value="mysql"/>
         <param name="janitorEnabled" value="true"/>
         <param name="janitorSleep" value="86400"/>
         <param name="janitorFirstRunHourOfDay" value="3"/>
       </Journal>
   </Cluster>

   ```

   For Oracle only:

   ```xml
   <!--
   Run with a cluster journal
   -->  

   <Cluster id="Unique_ID">
       <Journal class="org.apache.jackrabbit.core.journal.OracleDatabaseJournal">
           <param name="revision" value="${rep.home}/revision.log" />
           <param name="url" value="jdbc:oracle:thin://localhost:1521/jackrabbit"/>
           <param name="driver" value="oracle.jdbc.OracleDriver"/>
           <param name="user" value="jcr_user"/>
           <param name="password" value="password"/>
           <param name="schema" value="oracle"/>
           <param name="janitorEnabled" value="true"/>
           <param name="janitorSleep" value="86400"/>
           <param name="janitorFirstRunHourOfDay" value="3"/> 
        </Journal>
   </Cluster>"
   ```

   For MS SQL Server only:

   ```xml
   <!--
   Run with a cluster journal
   -->
   <Cluster id="Unique_ID">
       <Journal class="org.apache.jackrabbit.core.journal.MSSqlDatabaseJournal">
         <param name="revision" value="${rep.home}/revision.log"/>
         <param name="url" value="jdbc:sqlserver://localhost:1433;databaseName=jackrabbit"/>
         <param name="driver" value="com.microsoft.sqlserver.jdbc.SQLServerDriver"/>
         <param name="user" value="jcr_user"/>
         <param name="password" value="password"/>
         <param name="schema" value="mssql"/>
         <param name="janitorEnabled" value="true"/>
         <param name="janitorSleep" value="86400"/>
         <param name="janitorFirstRunHourOfDay" value="3"/>
       </Journal>
   </Cluster>
   ```
3. Save and close the file.

Jackrabbit journaling is now set up for your cluster. The [Jackrabbit Wiki](http://wiki.apache.org/jackrabbit/Clustering) has additional information about journaling.

Next, you need to cluster the quartz tables to avoid duplicate scheduling on each node.

## Step 4: Configure Quartz

You now need to make a few edits in the `quartz.properties` file to configure Quartz to work with your cluster.

1. Locate the `quartz.properties` file in the `pentaho-server/pentaho-solutions/system/scheduler-plugin/quartz` directory and open it with any text editor.
2. Find the **org.quartz.scheduler.instanceId** = INSTANCE\_ID line and change INSTANCE\_ID to `AUTO`.

   ```xml
   org.quartz.scheduler.instanceId = AUTO
   ```
3. Find the `#_replace_jobstore_properties` section and change the default value of **org.quartz.jobStore.isClustered** to `true` as shown:

   ```xml
   #_replace_jobstore_properties

   org.quartz.jobStore.misfireThreshold = 60000
   org.quartz.jobStore.driverDelegateClass = org.quartz.impl.jdbcjobstore.PostgreSQLDelegate
   org.quartz.jobStore.useProperties = false
   org.quartz.jobStore.dataSource = myDS
   org.quartz.jobStore.tablePrefix = QRTZ5_
   org.quartz.jobStore.isClustered = true
   ```
4. Add this line just after the **org.quartz.jobStore.isClustered** = `true` line:

   ```xml
   org.quartz.jobStore.clusterCheckinInterval = 20000
   ```

Quartz is now configured for your cluster. The [Quartz Configuration Reference](http://quartz-scheduler.org/documentation/quartz-2.x/configuration/ConfigJDBCJobStoreClustering) has additional information about clustering with Quartz.

## Step 5: Start and test the cluster

Start the cluster and verify that it is working properly with the following steps:

1. Start the solution database.
2. Start the application server on each node.
3. Make sure that the load balancer is able to ping each node.
4. Repeat for each node that you have set up.
5. Test the cluster by accessing the Pentaho Server through the load balancer's IP address, hostname, or domain name.

Begin whatever test procedure you have designed for this scenario.
