# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/notes-hdp-cluster-connection/simba-spark-sql-driver-support.md

# Simba Spark SQL driver support

If you are using Pentaho 7.0 or later, the Pentaho HDP drivers support the Simba Spark SQL driver. You need to download, install, and configure the Simba Spark SQL driver to use Simba Spark SQL with PDI.

1. Download the [Simba Spark SQL driver](http://www.simba.com/drivers/spark-jdbc-odbc/).
2. Extract the ZIP file, and then copy the following 3 files into the `lib/` directory of the Pentaho HDP driver:
   * `SparkJDBC41.jar`
   * `TCLIServiceClient.jar`
   * `QI.jar`
3. In the Database Connection window, select **SparkSQL** option.

   The default port for the Spark thrift server is 10015.
4. For secure connections, set the following additional parameters on the JDBC URL through the **Options** tab:
   * **KrbServiceName**
   * **KrbHostFQDN**
   * **KrbRealm**
5. For unsecure connections, if your Spark SQL configuration specifies **hive.server2.authentication**=`NONE`, then include an appropriate **User Name** in the Database Connection window.

   Otherwise, the connection is assumed to be NOSASL authentication, which causes a connection failure after timeout.
6. Stop and restart the component.
