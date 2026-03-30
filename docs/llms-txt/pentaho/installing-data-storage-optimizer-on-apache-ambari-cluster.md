# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster.md

# Installing Pentaho Data Optimizer on an Apache Ambari Cluster

To install Pentaho Data Optimizer on an Apache Ambari cluster, use the following workflow:

[Step 1: Download the Pentaho Data Optimizer Management Pack](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-1-download-the-pdso-management-pack-hadoop-installation)

[Step 2: Install the Pentaho Data Optimizer Management Pack for Apache Ambari](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-2-install-the-pentaho-data-storage-optimizer-management-packfor-apache-ambari)

[Step 3: Install the mpack on the Apache Ambari server](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-3-install-the-mpack-on-the-apache-ambari-server)

[Step 4: Link the mpack on the Apache Ambari server](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-4-link-the-mpack-on-the-apache-ambari-server)

[Step 5: Add the Pentaho Data Optimizer service to the cluster](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-5-add-the-pentaho-data-storage-optimizer-service-to-the-cluster)

[Step 6: Configure Pentaho Data Optimizer volumes to start automatically](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-6-configure-pdso-volumes-to-auto-start)

[Step 7: Configure HDFS to use the Pentaho Data Optimizer volume](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-7-configure-hdfs-to-use-the-pdso-volume)

[Step 8: Restart HDFS datanodes after adding volumes](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-8-restart-hdfs-datanodes-after-adding-pentaho-data-storageoptimizer-volumes)

[Step 9: Restart data nodes in Apache Ambari](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-9-restart-data-nodes-in-apache-ambari)

## Step 1: Download the Pentaho Data Optimizer Management Pack

Follow the steps below to download the Data Optimizer mpack for Apache Ambari and verify the integrity of the files. This task assumes you know how to calculate an MD5 checksum.

1. Download the Pentaho Data Optimizer mpack for Ambari from the [Support Portal](https://support.pentaho.com/hc/en-us):

   `pdso-mpack-1.0.0.0.tar.gz`
2. As a best practice, verify the downloaded content.
   1. Calculate the MD5 checksum of the downloaded file.
   2. Compare it to the MD5 checksum provided on the software download page.
   3. Ensure the two values are the same. If the two values are not the same, check your download or contact [Support Portal](https://support.pentaho.com/hc/en-us) to ensure you have the correct file.

## Step 2: Install the Pentaho Data Optimizer Management Pack for Apache Ambari

To add the Data Optimizer service to a cluster, you must first install the management pack (mpack) on the Apache Ambari server. Apache Ambari provides a framework for deploying and managing third-party services like Data Optimizer in an Apache or Hadoop cluster. The mpack for Apache Ambari defines the Data Optimizer service and its roles for Apache Ambari.

The Data Optimizer mpack contains metadata files that communicate to Apache Ambari what the Data Optimizer service is, the roles the service provides, and how the service is managed. For example, the mpack tells Apache Ambari which scripts to call to start or stop the roles associated with the service.

The mpack also contains the Data Optimizer code in the form of executable binaries and scripts. Apache Ambari executes Data Optimizer code according to the instructions provided in the mpack whenever you:

* start or stop the service or roles
* change log levels
* run instance recovery
* enable or disable recovery mode

Each host on a cluster has roles. Roles help determine the service that is installed and the location. The Data Optimizer mpack for Apache Ambari contains only a single role called **Volume. Instances** of this role are added to HDFS data nodes and enable the Data Optimizer tiering capability on those data nodes. For more information on the Volume role, see: [Access the Data Optimizer volumes directly](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/accessing-pdso-volumes-directly).

To prepare Apache Ambari for the Data Optimizer installation, first download the Pentaho Data Optimizer mpack and then install it on the Apache Ambari server.

## Step 3: Install the mpack on the Apache Ambari server

Follow the steps below to put the Data Optimizer software in Apache Ambari’s extension cache.

**Note:** As a best practice, perform the following steps with the same user credentials as the Ambari administrator.

1. Copy the mpack file to a temporary directory on the Ambari server, for example `/tmp/pdso-mpack-1.0.0.0.tar.gz`
2. Connect to the Ambari server using a Secure Shell (SSH) protocol.
3. Install the mpack with the following command, updated for your mpack location: `ambari-server install-mpack --verbose --mpack=/tmp/pdso-mpack-1.0.0.0.tar.gz`
4. Restart the Ambari server.

   This step refreshes Ambari server’s stale memory cache so it recognizes the Data Optimizer extension.

## Step 4: Link the mpack on the Apache Ambari server

Once linked to the HDP stack, you can add the Data Optimizer file service to the cluster as if Data Optimizer is contained in the stack, using the Linux `curl` utility to create the link. You can perform this step on any Linux host with `curl` and network access to the Apache Ambari REST API.

1. Create the mpack link with the following `curl` command:

   ```
   curl -u <user>:<password> \
   http://<server>:<port>/api/v1/links/ \
   -H 'X-Requested-By: ambari' -X POST \
   -d '
   {
     "ExtensionLink": {
       "stack_name": "HDP", 
       "stack_version":"<hdp_stack_version>", 
       "extension_name": "ldo", 
       "extension_version": "1.0.0.0"
     }
   }'
   ```

   Where:

   * **`<user>:<password>`**

     Username and password for the Ambari administrator.
   * **`<server>:<port>`**

     Ambari server’s host name or IP, and the Ambari server’s port.
   * **`<hdp_stack_version>`**

     HDP stack version running on the cluster you are deploying Data Optimizer to. Typically, this is just the `major.minor version number`, for example, `3.1`. You can query this value from Ambari using the following command:

     ```
     curl -u <user>:<password> \
     http://<server>:<port>/api/v1/clusters/<cluster_name>/stack_versions
     ```
2. Verify the links were properly created by querying the Apache Ambari API as follows:

   ```
   curl -u
           <user>:<password> \ http://<server>:<port>/api/v1/links/
   ```

   You should get a response such as the following:

   ```
   {
     "href" : "http://<server>:<port>/api/v1/links/",
     "items" : [
       {
         "href" : "http://<server>:<port>/api/v1/links/1",
         "ExtensionLink" : {
           "extension_name" : "ldo",
           "extension_version" : "1.0.0.0",
           "link_id" : 1,
           "stack_name" : "HDP",
           "stack_version" : "3.1"
         }
       }
     ]
   }
   ```
3. Restart the Apache Ambari server.

   This refreshes Apache Ambari server’s stale memory cache so it recognizes the Data Optimizer extension.

## Step 5: Add the Pentaho Data Optimizer service to the cluster

To add Data Optimizer to your cluster, log in to the Ambari dashboard and perform the following steps:

1. In the Ambari dashboard, click the more actions button for **Services** in the left sidebar and select **Add Service**.

   A list of available services appears.
2. Select Pentaho Data Optimizer and click **Next**.

   Because Data Optimizer has no master component, the Add Service Wizard will skip over the page.
3. On the Assign Slaves and Clients page, select the Data Optimizer volume checkbox for each of the data node hosts for which you want to add a Data Optimizer volume.
4. On the Customize Services page, enter the configuration parameters for your environment. While you must complete the configuration of the Advanced `ldo-config` section, the other configuration sections may be left at their default settings. To configure the Data Optimizer volumes, see [Configure Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-configure-data-storage-optimizer).

   **Note:** Remember the Data Optimizer mount point. You need this value when configuring HDFS to use the Data Optimizer volume.
5. After you have entered and confirmed all your Data Optimizer configuration values, click **Next** to proceed to the Review page.

   The Review page appears.
6. Click **Deploy**.

   The Install, Start and Test page opens. From here you can monitor the installation progress as well as the initial startup of Data Optimizer volumes on the data nodes.
7. (Optional) If you encounter errors when starting your volumes, view the following troubleshooting steps for possible solutions.
   1. Examine the `stdout` and `stderr` logs.

      You can access these logs by clicking through the links on the Install, Start and Test page in the Add Service Wizard. See [Troubleshoot Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs) for guidance.
   2. If the installation or first service run fails because of improper configuration, you may need to delete the Data Optimizer service from the cluster and to add the service as described in this article.

      **Note:** You can only edit some Data Optimizer configuration parameters during installation.

After all the Data Optimizer volumes have started, click through the remaining pages in the Add Service Wizard to return to the Apache Ambari dashboard.

## Step 6: Configure Pentaho Data Optimizer volumes to start automatically

After you complete the **Add Service** wizard, you can configure Data Optimizer volumes to automatically start when the data nodes are rebooted. If **Auto Start** is enabled for the HDFS Datanode component, then this configuration change is required.

1. In the Ambari dashboard, in the left pane, navigate to **Cluster Admin** > **Service** > **Auto Start** > **Pentaho Data Optimizer**
2. Locate the **Auto Start** status for the Data Optimizer volume component and change it to **Enabled**.
3. Save your changes.

The Data Optimizer volumes automatically start when the data nodes are rebooted.

## Step 7: Configure HDFS to use the Pentaho Data Optimizer volume

Before you can tier HDFS datanodes to the Data Optimizer volume, you must configure the HDFS datanodes to see the volume and to recognize Data Optimizer as an **ARCHIVE** type volume. If you deployed Data Optimizer to some, but not all datanodes, you must create a new configuration group for the datanodes running Data Optimizer volumes.

1. In the Ambari dashboard, navigate to **HDFS** > **Configs**
2. If you configured a subset of data nodes with Data Optimizer, create a new HDFS configuration group with the following steps:
   1. In the top of the HDFS Configs window, open the **Config Group** menu and click **Manage Config Groups**.

      The Manage HDFS Configuration Groups dialog box opens.
   2. Select the HDFS configuration group you want to copy from the list of existing configuration groups.

      Although this selection is typically the **Default** group, your selected group may differ if you are already using configuration groups to manage your data nodes.
   3. Open the menu on the form and select **Duplicate** to create a copy of the selected configuration group.
   4. Fill in the Create New Configuration Group form as follows:

      ValueEntry

      **Name**

      Datanode PDSO Volume Group

      **Description**

      Configuration Group for Datanodes with Data Optimizer volumes
   5. Click **OK**.
   6. In the Manage HDFS Configuration Groups dialog box, select **Datanode PDSO Volume Group** from the list of configuration groups in the left pane.
   7. Click the **+** (plus) icon, on the right side of the dialog box, to add hosts to the selected configuration group.

      The Select Configuration Group Hosts dialog box opens.
   8. Select the checkbox next to each of the datanodes with a Data Optimizer volume.
   9. Click **OK**.

      The Manage HDFS Configuration Groups dialog box appears.
   10. Click **Save**.

       The HDFS Configs page appears.
3. On the HDFS Configs page, locate the **Datanode directories** property (`dfs.datanode.data.dir`)
4. If you did not create a configuration group, then proceed to the next step. If you created a new HDFS configuration group because Data Optimizer is deployed to a subset of datanodes, then:
   1. Point over the **Datanode directories** field.

      The **+** (override) icon appears to the right of the field.
   2. Click the **+** icon to override the current entry.
   3. When prompted, choose the **HDFS Configuration Group** and select the**Datanode PDSO Volume Group** you created previously in this task.

      The new override value prepopulates with the value from the current configuration.
5. Place your cursor at the end of the current text in the **Datanode directories** field and add the `[ARCHIVE]<pdso_mount_point>/data` value, where `<pdso_mount_point>` is the value associated with the **Pentaho Data Optimizer Mount Point** property in the Data Optimizer configuration.

   For example, if the mount point is `/mnt/pdso`, then the value of the new entry would be `[ARCHIVE]/mnt/pdso/data`.

   The property requires a comma delimited list so be sure to separate the new entry from the existing entries with a comma.

   As a best practice, create a subdirectory under the Pentaho Data Optimizer Mount Point for the HDFS Datanode directory and assign it a name. In this example, the subdirectory name is `data`, but the name can be whatever you choose.
6. Save your work.
7. Refresh or restart your datanodes. See [Step 8: Restart HDFS datanodes after adding volumes](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-8-restart-hdfs-datanodes-after-adding-pentaho-data-storageoptimizer-volumes).
8. Verify Pentaho Data Optimizer is working properly. See [Tiering HDFS Blocks to Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/tiering-hdfs-blocks-to-pdso).

## Step 8: Restart HDFS datanodes after adding volumes

After you have configured HDFS data nodes to use Pentaho Data Optimizer volumes, you need to perform additional steps so Ambari operates properly.

Ambari cannot detect the components that are impacted by a configuration change. In addition, it does not support refreshing configurations on a running service instance. Therefore, Ambari prompts you to restart all HDFS components, even though only the data node component is impacted, and the changed property is classified as a “refreshable” property.

Use the **Restart data nodes** method to trigger the data nodes to detect the configuration change. Restarting data nodes is performed entirely in the user interface, but the data nodes restart in a rolling fashion.

As a best practice, restart only data node components in a rolling restart fashion to minimize disruption and to avoid data availability issues. This process does not resolve the notifications in the Ambari UI indicating that all HDFS services need to be restarted.

## Step 9: Restart data nodes in Apache Ambari

In the Apache Ambari dashboard, perform the following steps:

1. Navigate to the HDFS Summary page.
2. At the top of the page, select either **Restart**, **Restart DataNodes**, or **Service Actions**.
3. Select the configuration settings that are consistent with your normal best practices for data node rolling restarts in this environment.
4. Select **Only restart DataNodes with stale configs**.
5. Select **Trigger Rolling Restart**.

After the rolling restart is complete, the data nodes start tiering to Data Optimizer.

For help verifying that tiering is occurring, see [Tiering HDFS Blocks to Pentaho Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/tiering-hdfs-blocks-to-pdso).

[<br>](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-apache-ambari-cluster/step-2-install-the-pentaho-data-storage-optimizer-management-packfor-apache-ambari)
