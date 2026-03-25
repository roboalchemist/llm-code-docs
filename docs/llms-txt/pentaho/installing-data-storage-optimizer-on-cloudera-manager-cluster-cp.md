# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp.md

# Installing Pentaho Data Optimizer on a Cloudera Manager cluster

To install Data Optimizer on a Cloudera Manager cluster, use the following workflow:

Step 1: [Download the Pentaho Data Optimizer software](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/download-the-pentaho-data-storage-optimizer-software)

Step 2: [Add the Pentaho Data Optimizer parcel to a parcel repository](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/add-data-storage-optimizer-parcel-to-a-parcel-repository)

Step 3: [Download the parcel to Cloudera Manager](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/download-the-parcel-to-cloudera-manager-pdso-install-in-hadoop)

Step 4: [Install the custom service descriptor on the Cloudera Manager server](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/install-the-custom-service-descriptor-on-the-cloudera-manager-server-pdso-install-in-hadoop)

Step 5: [Distribute and activate the parcel](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/distribute-and-activate-the-parcel-pdso-install-in-hadoop)

Step 6: [Add the Pentaho Data Optimizer service to the cluster](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/add-data-storage-optimizer-service-to-the-cluster)

Step 7: [Configure Data Optimizer volumes to restart automatically](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/configure-data-storage-optimizer-volumes-to-auto-restart)

Step 8: [Configure HDFS to use the Data Optimizer volume](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/configure-hdfs-to-use-the-data-storage-optimizer-volume)

Step 9: [Refresh HDFS Datanodes after adding Data Optimizer volumes](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/refresh-hdfs-datanodes-after-adding-data-storage-optimizervolumes)

Step 10: [Data Optimizer extension for Cloudera Manager](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/data-storage-optimizer-extension-for-cloudera-manager)

## Step 1: Download the Pentaho Data Optimizer software

Follow the steps below to download the Data Optimizer install files and verify the integrity of the files. This task assumes you know how to calculate an MD5 checksum.

1. Download both the `TAR` file containing the custom service descriptor (CSD) file and the parcel for Pentaho Data Optimizer from the [Support Portal](https://support.pentaho.com/hc/en-us). The file is named `pdso-1.3.x.x-el7.tar`.
2. Verify the downloaded content.
   1. Calculate the MD5 checksum of the downloaded file.
   2. Compare it to the MD5 checksum provided on the software download page.
   3. Ensure the two values match.
3. Extract the contents of the `pdso-1.3.x.x-el7.tar` file to a directory.

The contents of the directory are extracted.

<table><thead><tr><th width="253">File name</th><th>Description</th></tr></thead><tbody><tr><td><code>pdso-1.3.x.x-el7.parcel</code></td><td>The Pentaho Data Optimizer parcel.</td></tr><tr><td><code>pdso-1.3.x.xel7.parcel.sha</code></td><td>A SHA-1 checksum of the parcel file, used for the local parcel repository.</td></tr><tr><td><code>manifest.json</code></td><td>A manifest for the hosted parcel repository.</td></tr><tr><td><code>pdso-1.3.x.x-el7.jar</code></td><td>The file containing the custom service descriptor.</td></tr></tbody></table>

## Step 2: Add the Pentaho Data Optimizer parcel to a parcel repository

To install Pentaho Data Optimizer with Cloudera Manager (CM), you must place the parcel in a repository accessible to your CM server.

* **Internally hosted remote parcel repository**

  For users with an existing parcel repository hosted on their own webserver in their network, which is network accessible from the Cloudera Manager server:

  1. In the `/<parcel_dir>/` directory on your parcel repository webserver, create a subdirectory called `pdso/1.3.0/`.
  2. Copy the `pdso-1.3.0.x-el7.parcel` and `manifest.json` files to the `/<parcel_dir>/pdso/1.3.0/` directory.
  3. Change the file ownership and permissions as necessary on `/<parcel_dir>/pdso/`, `/<parcel_dir>/pdso/1.3.0/` and their contents, so the webserver can serve these files.
* **No internally hosted parcel repository**

  If you do not have a private, internally-hosted parcel repository, see **Configuring a Local Parcel Repository** in the Cloudera documentation for more information on configuring a parcel repository.

## Step 3: Download the parcel to Cloudera Manager

If you are using a local parcel repository, skip this section and proceed to [Distribute and activate the parcel](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/distribute-and-activate-the-parcel-pdso-install-in-hadoop).

This task assumes you have an internally-hosted remote parcel repository.

1. Log into Cloudera Manager Admin Console and click **HostsParcels** in the top navigation bar.

   The Parcels page opens.
2. Click **Configuration**.

   The Parcel Configurations dialog box opens.
3. Locate the **Remote Parcel Repository URLs** setting and add the location of the Data Optimizer parcel on your internally-hosted remote repository server as your new entry.

   The value of the new entry is the location of the Data Optimizer parcel on your internally hosted remote repository server. For example, if your remote repository is located at `https://myrepo.example.com/parcel-repo/`, then the value would be `https://myrepo.example.com/parcel-repo/pdso/1.2.0/`.
4. Save your changes to return to the Parcels page.
5. Click **Check for New Parcels**.

   The `pdso` parcel entry displays in the parcel list with a status of **Available Remotely**.
6. Click **Download** for the `pdso` parcel.

When the process is complete, the status of the parcel changes to **Downloaded**.

## Step 4: Install the custom service descriptor on the Cloudera Manager server

The Data Optimizer Custom Service Descriptor (CSD) file describes the service to Cloudera Manager (CM). This file is required so that CM is aware of the service and its roles.

1. Copy the CSD file to the `/opt/cloudera/csd/` directory on the Cloudera Manager server.
2. Change the file ownership to the `cloudera-scm` user and group.
   1. `chown cloudera-scm:cloudera-scm`
   2. `/opt/cloudera/csd/pdso-1.3.0.<x>-el7.jar`
3. Change the file permissions to 640: `chmod 640 /opt/cloudera/csd/pdso-1.3.0.<x>-el7.jar`
4. Restart the Cloudera Manager server.

   If you are running the Cloudera Manager Management Service, you must restart it on the Cloudera Manager dashboard.

## Step 5: Distribute and activate the parcel

Before you can add the Data Optimizer service to your cluster, you must first distribute the `pdso` parcel to all the nodes in the cluster and then activate the parcel.

1. Log into Cloudera Manager Admin Console and navigate to **Hosts** > **Parcels**.
2. Find the `pdso` parcel.

   The status of the parcel should be **Downloaded**.
3. If you do not see the `pdso` parcel, click **Check for New Parcels** at the top of the Parcels page.
4. Click **Distribute** for the `pdso` parcel.

   The distribution process starts immediately. Depending on the size of the cluster, this process may take several minutes or more. Allow it to complete.

   The parcel status changes to **Distributed**.
5. Click **Activate** for the `pdso` parcel.

   The activation process starts immediately. Depending on the size of the cluster, this process may take several minutes or more. Allow it to complete.

   The parcel status changes to **Activated**.

The Data Optimizer service is ready to be added to your Cloudera cluster.

## Step 6: Add the Pentaho Data Optimizer service to the cluster

To add Data Optimizer to your cluster, perform the following steps:

1. Log in to the Cloudera Manager dashboard.
2. Navigate to the cluster and open the action menu dropdown for the cluster then select **Add Service**.
3. Select Pentaho Data Optimizer from the list of available services and click **Continue**.
4. Assign hosts for the **Volume** role.
   1. On the Assign Roles page, locate the **Volume** role for the Data Optimizer service and click the Volume dialog box.
   2. Select the hosts to assign to the **Volume** role and click **OK**.

      Only hosts that have the HDFS Datanode role are valid candidates to add the Data Optimizer **Volume** role.
5. Assign hosts for the **Volume Monitor** role:
   1. Navigate back to the Assign Roles page and locate the named **Volume Monitor** for the Data Optimizer service.
   2. Click the **Volume Monitor** dialog box then assign hosts in your cluster to the **Volume Monitor** role.
   3. If prompted, select **Custom**.
   4. Select each of the hosts to which you added the **Volume** role and click **OK**.

      **Note:** Each host with a **Volume** instance must have a **Volume Monitor** instance as well. Do not select hosts without a **Volume** instance.
6. Click **Continue**.
7. Proceed to the Review Changes page. then enter the Data Optimizer volume configuration parameters for your environment.

   See the [Data Optimizer configuration parameters](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-configure-data-storage-optimizer/pdso-configuration-parameters) section for information about how to configure Data Optimizer volumes.

   **Note:** Remember the value of the `MOUNT_POINT` parameter. You will need this value when configuring HDFS to use the Data Optimizer volume.
8. After you have entered and confirmed all your Data Optimizer configuration values, click **Continue**.

   The Command Details page opens. From here, you can monitor the **First Run Command**.

   At this point in the process, Cloudera Manager attempts to start the service and launch the **Volume** instances for the initial time.
9. Monitor the start commands as they run in the background. Verify that all **Volume** and **Volume Monitor** instances start without error.
10. (Optional) If you encounter errors, you may need to troubleshoot.
    1. Look at the `stdout`, `stderr`, and role logs in the Cloudera Manager UI.
    2. If necessary, see [Troubleshoot Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs).
11. After all Data Optimizer volumes have started, you can click through the remaining pages in the Add Service wizard to return to the Cloudera Manager dashboard.

## Step 7: Configure Data Optimizer volumes to restart automatically

After you complete the **Add Service** wizard, you can configure Data Optimizer volumes to automatically start when the data nodes are rebooted.

**Note:** If **Auto Start** is enabled for the HDFS Datanode component, then this configuration change is required.

1. In the Cloudera dashboard, navigate to **Cluster Admin** > **Service** > **Auto Start** > **Pentaho Data Optimizer**
2. Locate the **Auto Start** status for the Data Optimizer volume component and change it to **Enabled**.
3. Save your changes.

The Data Optimizer volumes start automatically when the data nodes are rebooted.

## Step 8: Configure HDFS to use the Data Optimizer volume

Before HDFS datanodes can begin tiering blocks to the Data Optimizer volume, you must configure the HDFS datanodes to see the Data Optimizer volume and to recognize Data Optimizer as an **ARCHIVE** volume type. If you deployed Data Optimizer to some but not all datanodes, then you will need to create a new configuration group for the datanodes running Data Optimizer volumes.

1. From the Cloudera dashboard, navigate to **HDFS** > **Configuration**.
2. If you configured a subset of data nodes with Data Optimizer, create a new HDFS configuration group with the following steps:
   1. In the top of the HDFS Configs window, open the **Config Group** drop-down menu and click **Manage Config Groups**.

      The Manage HDFS Configuration Groups dialog box opens.
   2. From the list of existing configuration groups, select the HDFS configuration group you want to copy.

      Although this selection is typically the **Default** group, your selected group may differ if you are already using configuration groups to manage your data nodes.
   3. Open the dropdown menu on the form and select **Duplicate** to create a copy of the selected configuration group.
   4. Fill in the **Create New Configuration Group** form as follows:

      | Value           | Entry                                                         |
      | --------------- | ------------------------------------------------------------- |
      | **Name**        | Datanode PDSO Volume Group                                    |
      | **Description** | Configuration Group for Datanodes with Data Optimizer volumes |
   5. Click **OK**.
   6. In the Manage HDFS Configuration Groups dialog box, select the **Datanode PDSO Volume Group** from the list of configuration groups in the left pane.
   7. On the right side of the dialog box, click the **+** (plus) icon to add hosts to the selected configuration group.

      The **Select Configuration Group Hosts** dialog box opens.
   8. In the Select Configuration Group Hosts dialog box, select the checkbox next to each of the datanodes with a Data Optimizer Volume.
   9. Click **OK**.

      The **Manage HDFS Configuration Groups** dialog box opens.
   10. Click **Save**.

       The HDFS Configs page appears.
3. Locate the **Datanode directories** property (`dfs.datanode.data.dir`).
4. (Optional) If you did not create a configuration group, proceed to the next step. If you created a new HDFS configuration group because Data Optimizer is deployed to a subset of datanodes, perform the following steps:

   1. Place your cursor over the **Datanode directories** field.

      The **+** (override) icon appears to the right of the field.
   2. Click the **+** icon to override the current entry.
   3. When prompted, choose the **HDFS Configuration Group** and select the **Datanode PDSO Volume Group** you created previously in this task.

   The new override value prepopulates with the value from the current configuration.
5. Place your cursor after the end of the current text in the **Datanode directories** text box and add the `[ARCHIVE]<pdso_mount_point>/data` value.

   The `<pdso_mount_point>` value is associated with the **Pentaho Data Optimizer Mount Point** property in the Data Optimizer Configuration.

   For example, if the PDSO mount point is `/mnt/pdso`, then the value of the new entry would be `[ARCHIVE]/mnt/pdso/data`.

   The property requires a comma delimited list, so be sure to separate the new entry from the existing entries with a comma.

   **Note:** As a best practice, create a subdirectory under the Data Optimizer mount point for the HDFS Datanode directory and assign it a name. In this example, the subdirectory name is `data`, but the name can be whatever you choose.
6. Save your work.
7. Refresh or restart your datanodes. See [Refresh HDFS Datanodes after adding Data Optimizer volumes](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/refresh-hdfs-datanodes-after-adding-data-storage-optimizervolumes).

Verify Data Optimizer is working properly. See [Tiering HDFS Blocks to Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/tiering-hdfs-blocks-to-pdso).

## Step 9: Refresh HDFS Datanodes after adding Data Optimizer volumes

After you have configured HDFS data nodes to use Data Optimizer volumes, refresh or restart the data nodes so they can register the configuration change and use the volumes. The data node property that was modified is a refreshable configuration, so the data nodes can pick up new data directories without restarting, which can be disruptive.

Typically, Cloudera Manager prompts you to refresh your data nodes because Cloudera Manager detects that the configuration change is refreshable. Click the refresh icon when it appears at the top of the HDFS configuration page to refresh your data nodes. After the refresh, the data nodes can start tiering to Data Optimizer.

In some cases, such as if you created a new configuration role group, Cloudera Manager may prompt for a restart. In this case, contact the Data Optimizer implementation team and your Cluster Administrator to determine how best to proceed and resolve the required restart notifications. You still might be able to perform a refresh by executing the **Refresh Cluster** action. After the refresh, data nodes are ready to begin tiering as described in the previous paragraph.

{% hint style="warning" %}
After HDFS has been configured to use Data Optimizer Volumes, do not stop the Volume on a node when the Datanode service is still running. Doing so can result in unpredictable behavior, including HDFS marking a volume as failed.
{% endhint %}

To verify Data Optimizer is tiering properly, see [Tiering HDFS Blocks to Data Optimizer](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/tiering-hdfs-blocks-to-pdso).

## Step 10: Data Optimizer extension for Cloudera Manager

Cloudera Manager extensions allow you to deploy and manage third party services like Data Optimizer on a Cloudera cluster. The Data Optimizer extension for Cloudera Manager (CM) defines the Data Optimizer service and its roles for Cloudera Manager. This extension is compatible only with parcel-deployed Cloudera clusters.

The Data Optimizer extension contains a Custom Service Descriptor (CSD) file that defines the Data Optimizer service, the roles it provides, and how the service is managed. For example, the CSD file tells CM which scripts to call to start or stop the roles associated with the service.

You must deploy this CSD file directly to the CM server with `root` or `sudo` permissions.

The Data Optimizer extension also includes a parcel file that contains the Data Optimizer code in the form of executable binaries and scripts. Cloudera Manager executes the Data Optimizer code according to the instructions provided in the CSD file whenever the service or roles are started and stopped, or when changing log levels, collecting logs, or enabling/disabling the recovery mode. Deploy the parcel directly to the CM server or download it from a privately-hosted parcel repository.

The Data Optimizer extension for Cloudera Manager contains the following roles:

* **Volume**

  Instances of the Volume role are added to HDFS datanodes and enable the Data Optimizer tiering capability on those data nodes.
* **Volume Monitor**

  Instances of the Volume Monitor role are deployed alongside Volume instances and provide proactive monitoring capabilities to ensure that the Volume is healthy, and to generate alerts when necessary.

[<br>](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-install-landing-page-hadoop-installation/installing-data-storage-optimizer-on-cloudera-manager-cluster-cp/download-the-parcel-to-cloudera-manager-pdso-install-in-hadoop)
