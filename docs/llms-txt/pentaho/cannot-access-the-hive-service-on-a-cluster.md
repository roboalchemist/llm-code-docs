# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/cannot-access-the-hive-service-on-a-cluster.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/cannot-access-the-hive-service-on-a-cluster.md

# Cannot access the Hive service on a cluster

If you cannot use Kerberos impersonation to authenticate and access the Hive service on a cluster, review the steps in the **Pentaho Business Analytics** document.

If this issue persists, copy the `hive-site.xml` file on the Hive server to the configuration directory of the named cluster connection in these directories:

* **Pentaho Server**

  `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-big-data-plugin/hadoop-configurations/[cluster distribution]`
* **PDI client**

  `data-integration/plugins/pentaho-big-data-plugin/hadoop-configurations/[cluster distribution]`

If the problem continues to persist, disable pooled connections for Hive.
