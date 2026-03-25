# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/edit-configuration-files-for-users-hdi.md

# Edit configuration files for users

Ask your Azure administrator to download the configuration files from the platform for the applications your teams are using, and then edit these files to include Pentaho-specific and user-specific parameters. Copy the files to the user's directory: `<username>/.pentaho/metastore/pentaho/NamedCluster/Configs/<user-defined connection name>`. This directory and the `config.properties` file are created when you create a named connection. See the **Pentaho Data Integration** document for details about named connections.

Modify the following files and provide them to your users:

* `core-site.xml` if you are using secured instance of HDI
* `hbase-site.xml`
* `hive-site.xml`
* `mapred-site.xml`
* `yarn-site.xml`
