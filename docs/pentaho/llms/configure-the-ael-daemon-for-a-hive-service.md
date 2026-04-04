# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive/configure-the-ael-daemon-for-a-hive-service.md

# Configure the AEL daemon for a Hive service

You must configure the `application.properties` file of the AEL daemon if you want to:

* Use Hive tables on a secure supported HDP cluster.
* Use Hive managed and unmanaged tables in an ORC or Parquet format on your Amazon EMR cluster.
* Use Hive managed and unmanaged tables in an ORC or Parquet format on your Google Dataproc cluster.

To configure the properties file, perform the following steps.

1. Navigate to the `data-integration/adaptive-execution/config` directory and open the `application.properties` file with any text editor.
2. Set the values for your environment as shown in the following table.

   | Parameter                       | Value                                                                                                                                                                                                                                                                   |
   | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `enableHiveConnection`          | Enables AEL access to Hive tables. Set this value to `true`.                                                                                                                                                                                                            |
   | `spark.driver.extraClassPath`   | Specifies the path to the directory containing the `hive-site.xml` file on the driver node. It loads the `hive-site.xml` file as a resource in the driver. This resource defines the Hive endpoints and security setting required by AEL to access the Hive subsystem.  |
   | `spark.executor.extraClassPath` | Specifies the path to the directory containing the `hive-site.xml` on the executor nodes. It loads the `hive-site.xml` file as a resource on each executor. This resource defines the Hive endpoints and security setting required by AEL to access the Hive subsystem. |

   The following lines of code show sample values for these parameters:

   ```
   # AEL Spark Hive Property Settings
   enableHiveConnection=true
   enableHiveWarehouseConnector=false
   spark.driver.extraClassPath=/etc/spark/conf.dist/
   spark.executor.extraClassPath=/etc/spark/conf.dist/
   ```
3. Save and close the file.
4. Restart the AEL daemon.
5. [Stop, then start the Pentaho Server](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration).

You can now use PDI with a **Hadoop Hive 2/3** database connection.
