# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/legacy-mode-activated-if-named-cluster-configuration-cannot-be-located.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/legacy-mode-activated-if-named-cluster-configuration-cannot-be-located.md

# Legacy mode activated when named cluster configuration cannot be located

If you run a transformation or job for which PDI cannot locate and load a named configuration cluster, then PDI activates a legacy mode. This legacy, or fallback, mode is only available in Pentaho 9.0 and later.

When the legacy mode is activated, PDI attempts to run the transformation by finding any existing cluster configuration you have set up in the PDI Big Data plugin. PDI then migrates the existing configuration to the latest PDI instance that you are currently running.

**Note:** You cannot connect to more than one cluster.

The legacy mode is helpful for transformations built with previous versions of PDI and includes individual steps that are not associated to a named cluster. You can run the transformation in legacy mode without revising the cluster configuration in each individual step. For information about setting up a named connection, see the **Pentaho Data Integration** document.

When legacy mode is active, the transformation log displays the following message:

`Could not find cluster configuration file {0} for cluster {1} in expected metastore locations or a legacy shim configuration.`

If the Big Data plugin is present and PDI accesses it to successfully activate legacy mode, the transfomation log displays the following message:

`Cluster configuration not found in expected location; trying legacy configuration location.`

For more information about working with clusters, see [Get started with Hadoop and PDI](https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi).
