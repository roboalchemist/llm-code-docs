# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/edit-configuration-files-for-users-cp-gdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/edit-configuration-files-for-users-cp-gdp.md

# Edit configuration files for users

Your cluster administrator must download configuration files from the cluster for the applications your teams are using, and then edit them to include Pentaho-specific and user-specific parameters. When edited, provide these modified files to the applicable users who must copy the files into the their directory: `<*username*>/.pentaho/metastore/pentaho/NamedCluster/Configs/<*user-defined connection name*>`.

When creating a named connection, the `<*user-defined connection name*>` directory is also created. When you set up the named connection, PDI copies these configuration files into that directory. The cluster administrator must provide users with the name to assign the named connection, so that PDI can copy these modified files into that directory. See the **Pentaho Data Integration** document for details about named connections.

The following files must be provided to your users:

* `core-site.xml`
* `hdfs-site.xml`
* `mapred-site.xml`
* `yarn-site.xml`
* `hive-site.xml`

**Note:** You can obtain the site files from the Dataproc cluster by using SCP (Secure Copy Protocol) to copy them locally.
