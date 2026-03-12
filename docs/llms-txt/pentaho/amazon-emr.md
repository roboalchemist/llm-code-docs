# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/amazon-emr.md

# Amazon EMR

If you plan to use AEL with Amazon EMR, note the following conditions:

* To use Amazon EMR with AEL, you must install the Linux LZO compression library, see [LZO support](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/amazon-emr/lzo-support) for more information.
* To use Amazon EMR with AEL and Hive, you must [Configure the AEL daemon for a Hive service](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive/configure-the-ael-daemon-for-a-hive-service).
* To use the HBase Input and HBase Output steps with AEL and Amazon EMR, see **Using HBase steps with Amazon EMR 5.21** in the **Pentaho Data Integration** document.
* Because of limitations in Amazon EMR 4.0 and later, Impala is not supported on Spark.

  **Note:** Impala is not available as a download on the EMR Cluster configuration menu.
