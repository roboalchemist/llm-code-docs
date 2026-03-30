# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-hbase-site-xml-file-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi/edit-hbase-site-xml-file-hdi.md

# Edit HBase site XML file

If you are using HBase, edit the location of the temporary directory in the `hbase-site.xml` file to create an HBase local storage directory.

Perform the following steps to edit the `hbase-site.xml` file:

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `hbase-site.xml` file.
2. Add the following value:

   | Parameter         | Value               |
   | ----------------- | ------------------- |
   | **hbase.tmp.dir** | `/tmp/hadoop/hbase` |
3. Save and close the file.
