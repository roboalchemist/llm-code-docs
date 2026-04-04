# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-cloudera-cluster/edit-the-configuration-files-for-users-cloudera/edit-hive-site-xml-file.md

# Edit Hive site XML file

If you are using Hive, follow these instructions to set the location of the hive metastore in the `hive-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `hive-site.xml` file.
2. Add the following value:

   | Parameter               | Value                                                                                      |
   | ----------------------- | ------------------------------------------------------------------------------------------ |
   | **hive.metastore.uris** | Set this to the location of your hive metastore if it differs from what is on the cluster. |
3. Save and close the file.

See [Hive](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive) for further configuration information when using Hive with Spark on AEL.
