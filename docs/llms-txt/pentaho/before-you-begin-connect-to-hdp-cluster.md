# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/before-you-begin-connect-to-hdp-cluster.md

# Before you begin

Before you begin to set up Pentaho to connect to a HDP cluster, you must perform the following tasks: .

1. Check the [Components Reference](https://docs.pentaho.com/install/9.3-install/components-reference) to verify that your Pentaho version supports your version of the HDP cluster.
2. Prepare your HDP cluster by performing the following tasks;
   1. Configure a HDP cluster.

      See [Hortonwork's documentation](http://docs.hortonworks.com/) if you need help.
   2. Install any required services and service client tools.
   3. Test the cluster.
3. From your Hadoop administrator, get the connection information for the cluster and services that you intend to use. Some of this information may be from Ambari or other cluster management tools.
4. Add the YARN user on the cluster to the group defined by the **dfs.permissions.superusergroup** property. The **dfs.permissions.superusergroup** property can be found in `hdfs-site.xml` file on your cluster or in the cluster management application.
5. Read the [Notes](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/notes-hdp-cluster-connection) section to review special configuration instructions for your version of HDP.
6. [Set up Pentaho to connect to a Hadoop cluster](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster). You need to install the driver for your version of HDP.
