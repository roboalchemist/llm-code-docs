# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/using-pan-and-kitchen-with-a-hadoop-cluster.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/using-pan-and-kitchen-with-a-hadoop-cluster.md

# Using Pan and Kitchen with a Hadoop cluster

To use [Pan or Kitchen](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Advanced%20Pentaho%20Data%20Integration%20topics/Advanced%20topics%20\(Pentaho%20Data%20Integration%20overview\)/Use%20Command%20Line%20Tools%20to%20Run%20Transformations%20and%20Jobs=GUID-8F752993-2BB0-4609-995D-E7E473B380FD=3=en=.md) on a Hadoop cluster, you must configure Pentaho to run transformations and jobs with either the PDI client or the Pentaho Server. However, these configurations are not needed if your PDI client is connected to the Pentaho Repository. To use Pan and Kitchen from a repository directly on the Pentaho Server, you must create the named cluster definition in the server's repository. See [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article) for information on creating that connection.

**Note:** If a user starts the PDI client and the Pentaho Server on the same platform, the cluster configuration files in the `/home/<user>/.pentaho/metastore` directory are overwritten. To avoid this issue, use the same cluster connection names on both the PDI client host and the Pentaho Server host.
