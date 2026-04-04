# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-pentaho-data-optimizer-in-hadoop-cluster/installing-data-optimizer-on-the-cluster.md

# Installing Data Optimizer on the cluster

Depending on the type of cluster, use the following instructions to install Data Optimizer:

* [Installing Pentaho Data Optimizer on an Apache Ambari Cluster](#installing-pentaho-data-optimizer-on-an-apache-ambari-cluster)
* [Installing Pentaho Data Optimizer on a Cloudera Manager cluster](#installing-pentaho-data-optimizer-on-a-cloudera-manager-cluster)

## Installing Pentaho Data Optimizer on an Apache Ambari Cluster

To install Pentaho Data Optimizer on an Apache Ambari cluster, use the following workflow:

### Step 1: Download the Pentaho Data Optimizer Management Pack

The following steps outline how to download the Data Optimizer mpack for Apache Ambari and verify the integrity of the files. This task assumes you know how to calculate an MD5 checksum.

1. Download the Pentaho Data Optimizer mpack for Ambari from the [Support Portal](https://support.pentaho.com/hc/en-us):

   `pdso-ambari-extension-mpack-<version>.tar.gz`
2. As a best practice, verify the downloaded content.
   1. Calculate the MD5 checksum of the downloaded file.
   2. Compare it to the MD5 checksum provided on the software download page.
   3. Ensure the two values are the same. If the two values are not the same, verify your download or contact the [Support Portal](https://support.pentaho.com/hc/en-us) to ensure you have the correct file.

### Step 2: Install the Pentaho Data Optimizer Management Pack for Apache Ambari

To add the Data Optimizer service to a cluster, you must first install the management pack (mpack) on the Apache Ambari server. Apache Ambari gives a framework for deploying and managing third-party services like Data Optimizer in an Apache or Hadoop cluster. The mpack for Apache Ambari defines the Data Optimizer service and its roles for Apache Ambari.

The Data Optimizer mpack contains metadata files that communicate to Apache Ambari what the Data Optimizer service is, the roles the service provides, and how the service is managed. For example, the mpack tells Apache Ambari which scripts to call to start or stop the roles associated with the service.

The mpack also contains the Data Optimizer code in the form of executable binaries and scripts. Apache Ambari executes Data Optimizer code according to the instructions provided in the mpack whenever you:

* start or stop the service or roles
* change log levels
* run instance recovery
* enable or disable recovery mode

To prepare Apache Ambari for the Data Optimizer installation, first download the Pentaho Data Optimizer mpack and then install it on the Apache Ambari server.

### Step 3: Install the mpack on the Apache Ambari server

Perform the following steps to put the Data Optimizer software in Apache Ambari’s extension cache.

**Note:** As a best practice, perform the following steps with the same user credentials as the Ambari administrator.

1. Copy the mpack file to a temporary folder on the Ambari server, for example `/tmp/pdso-mpack-<version>.tar.gz`
2. Connect to the Ambari server using the Secure Shell (SSH) protocol.
3. Install the mpack with the following command, updated for the mpack location: `ambari-server install-mpack --verbose --mpack=/tmp/pdso-mpack-<version>.tar.gz`
4. Restart the Ambari server.

   It refreshes the Ambari server’s stale memory cache so it recognizes the Data Optimizer extension.

### Step 4: Link the mpack on the Apache Ambari server

After you linked to the Hortonworks Data Platform (HDP) stack, you can add the Data Optimizer file service to the cluster as if Data Optimizer is contained in the stack, using the Linux `curl` utility to create the link. You can perform this step on any Linux host with `curl` and network access to the Apache Ambari REST API.

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
       "extension_name": "pdso", 
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
           "extension_name" : "pdso",
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

### Step 5: Add the Data Optimizer service to the cluster

To add Data Optimizer to your cluster, log in to the Ambari dashboard and perform the following steps:

1. In the Ambari dashboard, click the more actions button for **Services** in the left sidebar and select **Add Service**.

   A list of available services appears.
2. Select Pentaho Data Optimizer and click **Next**.

   Because Data Optimizer has no master component, the Add Service Wizard will skip over the page.
3. On the Assign Slaves and Clients page, select the Data Optimizer volume checkbox for all DataNode hosts.
4. On the Customize Services page, enter the configuration parameters for your environment. While you must complete the configuration of the Advanced `ldo-config` section, the other configuration sections may be left at their default settings. To configure the Data Optimizer volumes, see [Configure Data Optimizer](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-pentaho-data-optimizer-in-hadoop-cluster/broken-reference).

   **Note:** Remember the Data Optimizer mount point. You need this value when configuring HDFS to use the Data Optimizer volume.
5. After you have entered and confirmed all your Data Optimizer configuration values, click **Next** to proceed to the Review page.

   The Review page appears.
6. Click **Deploy**.

   The Install, Start and Test page opens. From here you can monitor the installation progress as well as the initial startup of Data Optimizer volumes on the data nodes.
7. (Optional) If you encounter errors when starting your volumes, view the following troubleshooting steps for possible solutions.
   1. Examine the `stdout` and `stderr` logs.

      You can access these logs by clicking through the links on the Install, Start and Test page in the Add Service Wizard. See [Troubleshoot Data Optimizer](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-pentaho-data-optimizer-in-hadoop-cluster/broken-reference) for guidance.
   2. If the installation or first service run fails because of improper configuration, you may need to delete the Data Optimizer service from the cluster and to add the service as described in this article.

      **Note:** You can only edit some Data Optimizer configuration parameters during installation.

After all the Data Optimizer volumes have started, click through the remaining pages in the Add Service Wizard to return to the Apache Ambari dashboard.

### Step 6: Configure Pentaho Data Optimizer volumes to start automatically

After you complete the **Add Service** wizard, you can configure Data Optimizer volumes to automatically start when the data nodes are rebooted. If **Auto Start** is enabled for the HDFS Datanode component, then this configuration change is required.

1. In the Ambari dashboard, in the left pane, navigate to **Cluster Admin** > **Service** > **Auto Start** > **Pentaho Data Optimizer**
2. Locate the **Auto Start** status for the Data Optimizer volume component and change it to **Enabled**.
3. Save your changes.

The Data Optimizer volumes automatically start when the data nodes are rebooted.

### Step 7: Configure HDFS to use the Pentaho Data Optimizer volume

Before you can tier HDFS datanodes to the Data Optimizer volume, you must configure the HDFS datanodes to see the volume and to recognize Data Optimizer as an **ARCHIVE** type volume. If you deployed Data Optimizer to some, but not all datanodes, you must create a new configuration group for the datanodes running Data Optimizer volumes.

1. In the Ambari dashboard, navigate to **HDFS** > **Configs**
2. On the HDFS Configs page, locate the **Datanode directories** property (`dfs.datanode.data.dir`).
3. Place your cursor at the end of the current text in the **Datanode directories** field and add the `[ARCHIVE]<pdso_mount_point>/data` value, where `<pdso_mount_point>` is the value associated with the **Pentaho Data Optimizer Mount Point** property in the Data Optimizer configuration.

   For example, if the mount point is `/mnt/pdso`, then the value of the new entry would be `[ARCHIVE]/mnt/pdso/data`. The property requires a comma delimited list so be sure to separate the new entry from the existing entries with a comma.

   As a best practice, create a subdirectory under the Pentaho Data Optimizer Mount Point for the HDFS Datanode directory and assign it a name. In this example, the subdirectory name is `data`, but the name can be whatever you choose.
4. Save your work.
5. Refresh or restart your datanodes. See [Step 8: Restart HDFS datanodes after adding volumes](#step-8-restart-hdfs-datanodes-after-adding-volumes).
6. Verify Pentaho Data Optimizer is working properly. See [Tiering HDFS Blocks to Data Optimizer](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-pentaho-data-optimizer-in-hadoop-cluster/broken-reference).

### Step 8: Restart HDFS datanodes after adding volumes

After you have configured HDFS data nodes to use Pentaho Data Optimizer volumes, you need to perform additional steps so Ambari operates properly.

Ambari cannot detect the components that are impacted by a configuration change. In addition, it does not support refreshing configurations on a running service instance. Therefore, Ambari prompts you to restart all HDFS components, even though only the data node component is impacted, and the changed property is classified as a “refreshable” property.

Use the **Restart data nodes** method to trigger the data nodes to detect the configuration change. Restarting data nodes is performed entirely in the user interface, but the data nodes restart in a rolling fashion.

As a best practice, restart only data node components in a rolling restart fashion to minimize disruption and to avoid data availability issues. This process does not resolve the notifications in the Ambari UI indicating that all HDFS services need to be restarted.

### Step 9: Restart data nodes in Apache Ambari

In the Apache Ambari dashboard, perform the following steps:

1. Navigate to the HDFS Summary page.
2. At the top of the page, select either **Restart**, **Restart DataNodes**, or **Service Actions**.
3. Select the configuration settings that are consistent with your normal best practices for data node rolling restarts in this environment.
4. Select **Only restart DataNodes with stale configs**.
5. Select **Trigger Rolling Restart**.

After the rolling restart is complete, the data nodes start tiering to Data Optimizer.

For help verifying that tiering is occurring, see **Tiering HDFS Blocks to Data Optimizer**.

### Step 10: Start policy runner on a datanode

When the volumes are up, start the policy runner. This is an agent that runs on one of the DataNodes at scheduled intervals defined in the PDO configuration, facilitating migration jobs from Data Catalog.

Follow these steps to start PDO policy runner:

1. Go to **Hosts**.
2. Select any DataNode.
3. Click the **More** icon next to the PDO volume.
4. Click **Start Policy Runner**.

## Installing Pentaho Data Optimizer on a Cloudera Manager cluster

Pentaho Data Optimizer package for Cloudera Manager (CM) enables you to deploy and manage third party services like Data Optimizer on a Cloudera cluster. The Data Optimizer extension for Cloudera Manager defines the Data Optimizer service and its roles for Cloudera Manager. This extension is compatible only with parcel-deployed Cloudera clusters.

The Data Optimizer package contains a CSD file that defines the Data Optimizer service, the roles it provides, and how the service is managed. For example, the CSD file specifies CM which scripts to call to start or stop the roles associated with the service.

You must deploy this CSD file directly to the CM server with `root` or `sudo` permissions.

The Data Optimizer extension also includes a parcel file that contains the Data Optimizer code in the form of executable binaries and scripts. Cloudera Manager executes the Data Optimizer code according to the instructions provided in the CSD file whenever the service or roles are started and stopped, or when changing log levels, collecting logs, or enabling/disabling the recovery mode. Deploy the parcel directly to the CM server or download it from a privately-hosted parcel repository.

The Data Optimizer extension for Cloudera Manager contains the following roles:

* **Volume**: Instances of the Volume role are added to HDFS datanodes and enable the Data Optimizer tiering capability on those data nodes.
* **Volume Monitor**: Instances of the Volume Monitor role are deployed alongside Volume instances and provide proactive monitoring capabilities to ensure that the Volume is healthy, and to generate alerts when necessary.
* **Policy Runner**: A role that executes at scheduled intervals, as defined in the Data Optimizer configuration, to fetch migration jobs from the Pentaho Data Catalog system. It performs the migration or archiving of HDFS files and folders within the Hadoop cluster based on the scheduled jobs.

To install Data Optimizer on a Cloudera Manager cluster, use the following workflow:

### Step 1: Download the Pentaho Data Optimizer software

Perform the following steps to download the Data Optimizer install files and verify the integrity of the files. This task assumes you know how to calculate an MD5 checksum.

1. Download both the `TAR` file containing the custom service descriptor (CSD) file and the parcel for Pentaho Data Optimizer from the [Support Portal](https://support.pentaho.com/hc/en-us). The file is named `pdso-<version>.tar`.
2. Verify the downloaded content.
   1. Calculate the MD5 checksum of the downloaded file.
   2. Compare it to the MD5 checksum provided on the software download page.
   3. Ensure the two values match.
3. Extract the contents of the `pdso-<version>.tar` file to a folder.

The contents of the folder are extracted.

<table><thead><tr><th width="237.333251953125">File name</th><th>Description</th></tr></thead><tbody><tr><td><code>pdso-&#x3C;version>.parcel</code></td><td>The Pentaho Data Optimizer parcel.</td></tr><tr><td><code>pdso-&#x3C;version>.parcel.sha</code></td><td>A SHA-1 checksum of the parcel file, used for the local parcel repository.</td></tr><tr><td><code>manifest.json</code></td><td>A manifest for the hosted parcel repository.</td></tr><tr><td><code>pdso-&#x3C;version>.jar</code></td><td>The file containing the custom service descriptor.</td></tr></tbody></table>

### Step 2: Add the Pentaho Data Optimizer parcel to a parcel repository

To install Pentaho Data Optimizer with Cloudera Manager (CM), you must place the parcel in a repository accessible to your CM server.

* **Internally hosted remote parcel repository**

  For users with an existing parcel repository hosted on their own webserver in their network, which is network accessible from the Cloudera Manager server:

  1. In the `/<parcel_dir>/` directory on your parcel repository webserver, create a subdirectory called `pdso/1.3.0/`.
  2. Copy the `pdso-1.3.0.x-el7.parcel` and `manifest.json` files to the `/<parcel_dir>/pdso/1.3.0/` directory.
  3. Change the file ownership and permissions as necessary on `/<parcel_dir>/pdso/`, `/<parcel_dir>/pdso/1.3.0/` and their contents, so the webserver can serve these files.
* **No internally hosted parcel repository**

  If you do not have a private, internally-hosted parcel repository, see **Configuring a Local Parcel Repository** in the Cloudera documentation for more information on configuring a parcel repository.

### Step 3: Download the parcel to Cloudera Manager

If you are using a local parcel repository, skip this section and proceed to [#step-5-distribute-and-activate-the-parcel](#step-5-distribute-and-activate-the-parcel "mention").

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

### Step 4: Install the custom service descriptor on the Cloudera Manager server

The Data Optimizer Custom Service Descriptor (CSD) file describes the service to Cloudera Manager (CM). This file is required so that CM is aware of the service and its roles.

1. Copy the CSD file to the `/opt/cloudera/csd/` directory on the Cloudera Manager server.
2. Change the file ownership to the `cloudera-scm` user and group.
   1. `chown cloudera-scm:cloudera-scm`
   2. `/opt/cloudera/csd/pdso-1.3.0.<x>-el7.jar`
3. Change the file permissions to 640: `chmod 640 /opt/cloudera/csd/pdso-1.3.0.<x>-el7.jar`
4. Restart the Cloudera Manager server.

   If you are running the Cloudera Manager Management Service, you must restart it on the Cloudera Manager dashboard.

### Step 5: Distribute and activate the parcel

Before you can add the Data Optimizer service to your cluster, you must first distribute the `pdso` parcel to all the nodes in the cluster and then activate the parcel.

1. Log in to Cloudera Manager Admin Console and navigate to **Hosts** > **Parcels**.
2. Find the `pdso` parcel.

   The status of the parcel should be **Downloaded**.
3. If you do not see the `pdso` parcel, click **Check for New Parcels** at the top of the Parcels page.
4. Click **Distribute** for the `pdso` parcel.

   The distribution process starts immediately. Depending on the cluster size, this process may take several minutes or longer. Allow it to complete.

   The parcel status changes to **Distributed**.
5. Click **Activate** for the `pdso` parcel.

   The activation process starts immediately. Depending on the cluster size, this process may take several minutes or longer. Allow it to complete.

   The parcel status changes to **Activated**.

The Data Optimizer service is ready to be added to your Cloudera cluster.

### Step 6: Add the Pentaho Data Optimizer service to the cluster

To add Data Optimizer to the cluster, perform the following steps:

1. Log in to the Cloudera Manager dashboard.
2. Navigate to the cluster and open the action menu dropdown for the cluster then select **Add Service**.
3. Select Pentaho Data Optimizer from the list of available services and click **Continue**.
4. Assign hosts for the **Volume** role.
   1. On the Assign Roles page, locate the **Volume** role for the Data Optimizer service and click the Volume dialog box.
   2. Select all DataNodes for the **PDO Volume** to install and click **OK**.

      Only hosts that have the HDFS DataNode role are valid candidates to add the Data Optimizer **Volume** role.
5. Assign hosts for the **Volume Monitor** role:
   1. Navigate back to the Assign Roles page and locate the named **Volume Monitor** for the Data Optimizer service.
   2. Click the **Volume Monitor** dialog box then assign hosts in the cluster to the **Volume Monitor** role.
   3. If prompted, select **Custom**.
   4. Select each of the hosts to which you added the **Volume** role and click **OK**.

      **Note:** Each host with a **Volume** instance must have a **Volume Monitor** instance as well. Do not select hosts without a **Volume** instance.
6. Assign hosts for the **PDO Policy Runner** role.
   1. On the Assign Roles page, locate the **Volume** role for the Data Optimizer service and click the **PDO Policy Runner** dialog box.
   2. Select any one DataNode to install the **PDO Policy Runner** role.
7. Click **Continue**.
8. Proceed to the Review Changes page. then enter the Data Optimizer volume configuration parameters for the environment.

   See the [#data-optimizer-configuration-parameters](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/configure-data-optimizer#data-optimizer-configuration-parameters "mention")section for information about how to configure Data Optimizer volumes.

   **Note:** Remember the value of the `MOUNT_POINT` parameter. You will need this value when configuring HDFS to use the Data Optimizer volume.
9. After you have entered and confirmed all the Data Optimizer configuration values, click **Continue**.

   The Command Details page opens. From here, you can monitor the **First Run Command**.

   At this point in the process, Cloudera Manager attempts to start the service and start the **Volume** instances for the initial time.
10. Monitor the start commands as they run in the background. Verify that all **Volume** and **Volume Monitor** instances start without error.
11. (Optional) If you encounter errors, you might require to troubleshoot.
    1. Look at the `stdout`, `stderr`, and role logs in the Cloudera Manager UI.
    2. If necessary, see [Troubleshoot Data Optimizer](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/maintain-pentaho-data-optimizer#troubleshoot-data-optimizer).
12. After all Data Optimizer volumes have started, you can click through the remaining pages in the Add Service wizard to return to the Cloudera Manager dashboard.

### Step 7: Configure Data Optimizer volumes to restart automatically

After completing the Add Service wizard, you can configure Data Optimizer volumes to start automatically when the data nodes are rebooted.

**Note:** If **Auto Start** is enabled for the HDFS Datanode component, then this configuration change is required.

1. In the Cloudera dashboard, navigate to **Cluster Admin** > **Service** > **Auto Start** > **Pentaho Data Optimizer**
2. Locate the **Auto Start** status for the Data Optimizer volume component and change it to **Enabled**.
3. Save your changes.

The Data Optimizer volumes start automatically when the data nodes are rebooted.

### Step 8: Configure HDFS to use the Data Optimizer volume

Before HDFS DataNodes can begin tiering blocks to the Data Optimizer volume, you must configure the HDFS DataNodes to see the Data Optimizer volume and to recognize Data Optimizer as an **ARCHIVE** volume type. If you deployed Data Optimizer to some but not all DataNodes, then you must create a new configuration group for the DataNodes running Data Optimizer volumes.

1. From the Cloudera dashboard, navigate to **HDFS** > **Configuration**.
2. Locate the **DataNode directories** property (`dfs.datanode.data.dir`).
3. Place the cursor after the end of the current text in the **DataNode directories** text box and add the `[ARCHIVE]<pdso_mount_point>/data` value.

   The `<pdso_mount_point>` value is associated with the **Pentaho Data Optimizer Mount Point** property in the Data Optimizer Configuration.

   For example, if the PDSO mount point is `/mnt/pdso`, then the value of the new entry will be `[ARCHIVE]/mnt/pdso/data`.

   The property requires a comma delimited list, so make sure to separate the new entry from the existing entries with a comma.

   **Note:** As a best practice, create a subfolder under the Data Optimizer mount point for the HDFS DataNode folder and assign it a name. In this example, the subfolder name is `data`, but the name can be whatever you choose.
4. Save the work.
5. Refresh or restart the DataNodes. See [Refresh HDFS Datanodes after adding Data Optimizer volumes](#step-9-restart-data-nodes-in-apache-ambari).

Verify Data Optimizer is working properly. See [Tiering HDFS Blocks to Data Optimizer](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/maintain-pentaho-data-optimizer#tiering-hdfs-blocks-to-data-optimizer).

### Step 9: Refresh HDFS Datanodes after adding Data Optimizer volumes

After you have configured HDFS data nodes to use Data Optimizer volumes, refresh or restart the data nodes so they can register the configuration change and use the volumes. The data node property that was modified is a refreshable configuration, so the data nodes can pick up new data directories without restarting, which can be disruptive.

Typically, Cloudera Manager prompts you to refresh your data nodes because Cloudera Manager detects that the configuration change is refreshable. Click the refresh icon when it appears at the top of the HDFS configuration page to refresh your data nodes. After the refresh, the data nodes can start tiering to Data Optimizer.

In some cases, such as if you created a new configuration role group, Cloudera Manager may prompt for a restart. In this case, contact the Data Optimizer implementation team and your Cluster Administrator to determine how best to proceed and resolve the required restart notifications. You still might be able to perform a refresh by executing the **Refresh Cluster** action. After the refresh, data nodes are ready to begin tiering as described in the previous paragraph.

**CAUTION:** After HDFS has been configured to use Data Optimizer Volumes, do not stop the Volume on a node when the Datanode service is still running. Doing so can result in unpredictable behavior, including HDFS marking a volume as failed.

To verify Data Optimizer is tiering properly, see [Tiering HDFS Blocks to Data Optimizer](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/maintain-pentaho-data-optimizer#tiering-hdfs-blocks-to-data-optimizer).

### Step 10: Data Optimizer extension for Cloudera Manager

Cloudera Manager extensions allow you to deploy and manage third-party services like Data Optimizer on a Cloudera cluster. The Data Optimizer extension for Cloudera Manager (CM) defines the Data Optimizer service and its roles for Cloudera Manager. This extension is compatible only with parcel-deployed Cloudera clusters.

The Data Optimizer extension contains a Custom Service Descriptor (CSD) file that defines the Data Optimizer service, its roles, and how the service is managed. For example, the CSD file tells CM which scripts to call to start or stop the roles associated with the service.

You must deploy this CSD file directly to the CM server with `root` or `sudo` permissions.

The Data Optimizer extension also includes a parcel file that contains the Data Optimizer code in the form of executable binaries and scripts. Cloudera Manager executes the Data Optimizer code according to the instructions provided in the CSD file whenever the service or roles are started and stopped, or when changing log levels, collecting logs, or enabling or disabling recovery mode. Deploy the parcel directly to the CM server or download it from a privately hosted parcel repository.

The Data Optimizer extension for Cloudera Manager contains the following roles:

* **Volume**

  Instances of the Volume role are added to HDFS datanodes, enabling the Data Optimizer tiering capability on those data nodes.
* **Volume Monitor**

  Instances of the Volume Monitor role are deployed alongside Volume instances and provide proactive monitoring capabilities to ensure that the Volume is healthy and to generate alerts when necessary.
* **Policy Runner**

  A role that executes at scheduled intervals, as defined in the Data Optimizer configuration, to fetch migration jobs from the Pentaho Data Catalog system. It performs the migration or archiving of HDFS files and folders within the Hadoop cluster based on the scheduled jobs.
