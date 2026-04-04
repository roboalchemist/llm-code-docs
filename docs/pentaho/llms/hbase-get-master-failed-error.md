# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/hbase-get-master-failed-error.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/hbase-get-master-failed-error.md

# HBase Get Master Failed error

If the HBase cannot establish the authenticated portion of the connection, then copy the `hbase-site.xml` file from the HBase server to the configuration directory of the named cluster connection in these directories:

* Pentaho Server:

  `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-big-data-plugin/hadoop-configurations/[cluster distribution]`
* PDI client:

  `data-integration/plugins/pentaho-big-data-plugin/hadoop-configurations/[cluster distribution]`
