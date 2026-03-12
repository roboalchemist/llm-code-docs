# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/before-you-begin-connect-to-emr-cluster.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-amazon-emr-cluster/before-you-begin-connect-to-emr-cluster.md

# Before you begin

Before you begin setting up Pentaho to connect to an Amazon EMR cluster, perform the following tasks.

1. Check the [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference) to verify that your Pentaho version supports your version of the Amazon EMR cluster.
2. Prepare your Amazon EMR cluster by performing the following tasks:
   1. Configure an Amazon EC2 cluster.

      View the [Amazon's documentation](https://aws.amazon.com/documentation/elastic-mapreduce/) if you need help.
   2. Install any required services and service client tools.
   3. Test the cluster.
3. Install PDI on an Amazon EC2 instance that is within the same Amazon Virtual Private Cloud (VPC) as the Amazon EMR cluster.

   **Note:** As a best practice, you should install PDI on your Amazon EC2 instance. Otherwise, you might not be able to write or read files to or from the cluster. To resolve this issue, see [Unable to read or write files to HDFS on the Amazon EMR cluster](https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/unable-to-read-or-write-files-to-hdfs-on-amazon-emr-cluster).
4. Get the connection information for the cluster and services that you intend to use from your Hadoop administrator. Some of this information may be available from a cluster management tool. You also need to [supply some of this information to users](https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list) after you are finished.
5. Add the YARN user on the cluster to the group defined by **dfs.permissions.superusergroup** property. The **dfs.permissions.superusergroup** property can be found in `hdfs-site.xml` file on your cluster or in the cluster management application.
