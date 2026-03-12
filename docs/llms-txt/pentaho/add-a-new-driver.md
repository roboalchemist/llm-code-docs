# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/before-you-begin-pentaho-server-to-hadoop-cluster-connection/adding-a-new-driver-to-pentaho/add-a-new-driver.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/adding-a-new-driver-to-pentaho/add-a-new-driver.md

# Add a new driver

To add a new driver, first download the driver file from the [Support Portal](https://support.pentaho.com/hc/en-us) then add it to Pentaho using the PDI client. If you are connected to a repository, the driver is copied to the Pentaho Server driver directory. Otherwise, the driver is copied locally to the PDI client driver directory.

Perform the following steps to add a new driver.

1. Download the new driver from the [Support Portal](https://support.pentaho.com/hc/en-us).
   1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
   2. In the Pentaho card, click **Download**.

      The Downloads page opens.
   3. In the **10.x** list, click **See all \<number> articles** to see the full list of **10.x** downloads.
   4. On the **10.x** page, click **Pentaho 10.2 GA Release**.
   5. Scroll to the bottom of the Pentaho 10.2 GA Release page.
   6. In the file component section, browse to the `Big Data Shims` folder and download the driver file that you need.

      The following table lists the driver files that are available in the `Big Data Shims` folder.

      | Cluster connected to PDI | File                                                                      |
      | ------------------------ | ------------------------------------------------------------------------- |
      | Apache Vanilla           | pentaho-hadoop-shims-ee- apachevanilla-kar-10.2.0.0-*\<build number>*.kar |
      | Cloudera Data Platform   | pentaho-hadoop-shims-ee- cdpdc71-kar-10.2.0.0-*\<build number>*.kar       |
      | Google Dataproc          | pentaho-hadoop-shims-ee- dataproc1421-kar-10.2.0.0- *\<build number>*.kar |
      | Amazon Elastic MapReduce | pentaho-hadoop-shims-ee- emr700-kar-10.2.0.0-*\<build number>*.kar        |
      | Azure HDInsight          | pentaho-hadoop-shims-ee- hdi40-kar-10.2.0.0-*\<build number>*.kar         |
2. Unpack the Zip file that contains the driver to a temporary directory.
3. In the PDI client, select the **View** tab of your transformation or job.
4. Right-click the **Hadoop clusters** folder and click **Add driver**.

   The Add driver dialog box appears.
5. Click **Browse** and navigate to the temporary directory that contains the new driver `.kar` file that you downloaded from the [Support Portal](https://support.pentaho.com/hc/en-us).
6. Select the new driver `.kar` file, click **Open**, and then click **Next**.

   The Congratulations dialog box appears, notifying you that you must restart the PDI client and the Pentaho Server.

   * If you are connected to a repository, the driver is copied to the Pentaho Server driver directory.
   * If you are not connected to a repository, the driver is copied to the PDI client driver directory.
