# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive/configuring-the-ael-daemon-for-hive-warehouse-connector-on-your-hortonworks-cluster.md

# Configuring the AEL daemon for the Hive Warehouse Connector on your Hortonworks cluster

You can use PDI with the Hive Warehouse Connector (HWC) to access Hive managed tables in an ORC format or large unmanaged tables in Hive on secure supported HDP clusters. You can set the access controls and the LLAP queue by configuring the `application.properties` file of the AEL daemon.

**Note:** As a best practice, enable LLAP on HDP and follow the instructions outlined in [Apache Hive Performance Tuning](https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.0/performance-tuning/hive_performance_tuning.pdf).
