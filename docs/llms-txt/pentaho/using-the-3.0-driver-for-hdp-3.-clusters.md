# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/notes-hdp-cluster-connection/hdp-3.1-notes/using-the-3.0-driver-for-hdp-3.-clusters.md

# Using the 3.0 driver for HDP 3.1 clusters

You can use the HDP 3.0 driver to connect to your HDP 3.1 cluster by updating the PDI `config.properties` file.

Perform the following steps to update your **java.syste.hdp.version** driver configuration parameter to HDP 3.1:

1. On your HDP cluster, use the `hdp-select` command to determine the full version of your cluster, such as '`3.1.0.0-78`'.
2. In the Pentaho distribution, open the `config.properties` file located in the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory.
3. Change the **java.system.hdp.version** parameter from the existing version to the full version of your cluster, which you obtained by running the `hdp-select` command in Step 1. For example, the existing version of '`3.0.0.0-1634`' might be changed to '`3.1.0.0-78`'.
4. Save and close the `config.properties` file.

Your HDP 3.0 driver now works with your 3.1 HDP cluster after you restart your PDI client.
