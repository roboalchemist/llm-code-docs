# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/edit-configuration-files-for-users-emr.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/edit-configuration-files-for-users-emr.md

# Edit configuration files for users

Your cluster administrator must download configuration files from the cluster for the applications your teams are using, and then edit them to include Pentaho-specific and user-specific parameters. These modified files must be provided to the users and must be copied to the user's directory: `<username>/.pentaho/metastore/pentaho/NamedCluster/Configs/<user-defined connection name>`.

When the user creates a named connection, this `<user-defined connection name>` directory is created. When the user sets up the named connection, PDI copies these configuration files into that directory. The cluster administrator must provide the user with the name to assign the named connection, so that PDI can copy these modified files into that directory. See the **Pentaho Data Integration** document for details about named connections.

The following files must be provided to your users:

* `core-site.xml`
* `mapred-site.xml`
* `hdfs-site.xml`
