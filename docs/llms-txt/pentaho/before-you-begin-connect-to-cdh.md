# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-cloudera-cluster/before-you-begin-connect-to-cdh.md

# Before you begin

Before you begin to set up Pentaho to connect to a Cloudera cluster, you must perform the following tasks:

1. Check the [Components Reference](https://docs.pentaho.com/install/9.3-install/components-reference) to verify that your Pentaho version supports your version of the CDH cluster.
2. Prepare your Cloudera cluster by performing the following tasks:
   1. Configure a CDH cluster.

      See [Cloudera's documentation](http://www.cloudera.com/content/cloudera/en/documentation.html) if you need help.
   2. Install any required services and service client tools.
   3. Test the cluster.
3. From your Hadoop administrator, get the connection information for the cluster and services that you intend to use. Some of this information may be from Cloudera Manager or other cluster management tools. You also need to [supply some of this information to users](https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list) after you are finished.
4. Add the YARN user on the cluster to the group defined by **dfs.permissions.superusergroup** property. The **dfs.permissions.superusergroup** property can be found in `hdfs-site.xml` file on your cluster or in the Cloudera Manager.
5. [Set up Pentaho to connect to a Hadoop cluster](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster). You need to install the driver for your version of CDH.
