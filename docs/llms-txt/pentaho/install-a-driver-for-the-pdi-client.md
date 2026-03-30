# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/install-a-driver-for-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/install-a-driver-for-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/install-a-driver-for-the-pdi-client.md

# Install a driver for the PDI client

Before you can add a named connection to a cluster, you must install a driver for the vendor and version of the Hadoop cluster for which you are trying to connect.

If you are connected to the Pentaho Repository when you install a driver, it is placed into Pentaho Server directory and is available to all users. Otherwise, if you are not connected to the Pentaho Repository, the driver is placed into the PDI directory, registered exclusively by the local file system, and can only be used by you.

**Note:** This task assumes that you are not using the default Hadoop driver and that you have downloaded the vendor-specific driver from the [Support Portal](https://support.pentaho.com).

Perform the following steps to install a driver for the PDI client:

1. In the PDI client, select the **View** tab of the transformation or job.
2. Right-click the **Hadoop clusters** folder and click **Add driver**.

   The Add driver dialog box appears.
3. Click **Browse**.

   The Choose File to Upload dialog box appears.
4. Navigate to the location where you downloaded the driver file.
5. Select the driver (`.kar` file) you want to add, click **Open**, and then click **Next**.

   The selected file name appears in the **Browse** text field. The vendor distribution files contain their abbreviations in the `.kar` file names as shown below:

   * Amazon EMR (emr)
   * Apache Vanilla Hadoop (apachevanilla)
   * Azure HDInsight (hdi)
   * Cloudera Data Platform (cdp)
   * Google Dataproc (dataproc)
6. Click **Next**.

   The Congratulations dialog box appears, notifying you that you must restart the Pentaho Server or the PDI client.

The **Driver** field in the New cluster and Import cluster dialog boxes now display the driver you added.
