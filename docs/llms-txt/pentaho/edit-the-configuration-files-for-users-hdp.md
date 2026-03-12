# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/edit-the-configuration-files-for-users-hdp.md

# Edit the configuration files for users

Your cluster administrators must download the configuration files from the cluster for the applications your teams are using, and then edit the files to include Pentaho-specific and user-specific parameters. These files must be copied to the user's directory: `<username>/.pentaho/metastore/pentaho/NamedCluster/Configs/<user-defined connection name>`. This directory and the `config.properties` file are created when you set up a named connection. See the **Pentaho Data Integration** document for details about named connections.

The following files must be modified and provided to your users:

* `config.properties`
* `hbase-site.xml`
* `hive-site.xml`
* `mapred-site.xml`
* `yarn-site.xml`
