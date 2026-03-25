# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/install-a-driver-for-the-pentaho-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/install-a-driver-for-the-pentaho-server.md

# Install a driver for the Pentaho Server

Before you can add a named connection to a cluster, you must install a driver for the vendor and version of the Hadoop cluster that you are connecting to. Perform the following steps to install a driver for the Pentaho Server.

This task assumes that you have downloaded your driver from the [Support Portal](https://support.pentaho.com/hc/en-us) or that you are using the Apache Hadoop driver that is shipped with Pentaho.

1. Verify that you are connected to a repository.
2. In the PDI client, select the **View** tab of your transformation or job.
3. Right-click the **Hadoop clusters** folder and click **Add driver**.

   The Add driver dialog box appears.

   ![Add driver dialog box](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-3b472e150b60b8ff6fe2a52b211a58b25c3095f6%2FPDI_Hadoop_Clusters_Add_Driver.png?alt=media)
4. Click **Browse**

   The Choose File to Upload dialog box appears.
5. Navigate to the directory where you downloaded your `.kar` file from the [Support Portal](https://support.pentaho.com/hc/en-us).
6. Select the driver (`.kar` file) you want to add, click **Open**, and then click **Next**.

   The selected file name appears in the **Browse** text field. The vendor distribution files contain their abbreviations in the `.kar` file names as shown below:

   * Amazon EMR (emr)
   * Azure HDInsight (hdi)
   * Cloudera Data Platform (cdp)
   * Google Dataproc (dataproc)
7. Click **Next**.

   The Congratulations dialog box appears, notifying you that you must restart the Pentaho Server and the PDI client. The installed driver is now available for selection in the **Driver** field in the New cluster and Import cluster dialog boxes.
