# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/kettle-cluster-on-yarn-will-not-start.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/kettle-cluster-on-yarn-will-not-start.md

# Kettle cluster on YARN will not start

When you are using the Start a PDI Cluster on YARN job entry, the Kettle cluster may not start.

Verify in the **File System Path** (in the **Files** tab) that the **Default FS** setting matches the configured hostname for the HDFS Name node, then try starting the kettle cluster again.
