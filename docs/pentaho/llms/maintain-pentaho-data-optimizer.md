# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-pentaho-data-optimizer-in-hadoop-cluster/maintain-pentaho-data-optimizer.md

# Maintain Pentaho Data Optimizer

Use the following tools to maintain Data Optimizer:

* [Maintain Data Optimizer metadata](#maintain-data-optimizer-metadata)
* [The ldoctl command line utility](#the-ldoctl-command-line-utility)
* [Troubleshoot Data Optimizer](#monitor-data-optimizer)
* [Monitor Data Optimizer](#monitor-data-optimizer)

## Maintain Data Optimizer metadata

Each Pentaho Data Optimizer volume maintains an authoritative local data store that contains the metadata of all files and directories stored by the instance. The term “authoritative” means that the metadata in the store is complete, current, and trusted. The authoritative local metadata store gives significant performance benefits, allowing the Data Optimizer volume to handle metadata inquiries internally without making external API calls to the S3 storage device.

If the local metadata store for a Data Optimizer volume becomes lost or corrupted, you need to recover the metadata store. For example, corruption might occur if the metadata is stored on a failed disk drive. Recovering the store involves relocating the store, putting the Data Optimizer volume in recovery mode, and running the recovery procedure.

### Data Optimizer recovery mode

In recovery mode, the Pentaho Data Optimizer volume operates with its metadata store in non-authoritative mode while recovering file system metadata. The term “non-authoritative” means that the contents of the local metadata store might be incomplete. As a result, certain metadata inquiries can only be serviced by making external API calls to the S3 storage device. The metadata retrieved from the S3 storage device is cached to the local metadata store, reducing the need for future external API calls. Data Optimizer volumes are fully functional while in recovery mode, though performance might be affected.

#### Authoritative vs non-authoritative

When authoritative (`RECOVERY_MODE=false`), the store is considered complete, that means if a file or folder is not in the store, it does not exist. In authoritative mode, all metadata requests are serviced from the local metadata store.

When non-authoritative (`RECOVERY_MODE=true`), the store is considered incomplete. The absence of a file or folder in the store can indicate that the entity does not exist, or it mean that the file or directory has not been accessed since recovery began. In non-authoritative mode, directory listings and metadata requests for records not previously cached in the local metadata store must be serviced by querying the S3 bucket.

### Recovering from local metadata store failure or corruption

If the local metadata store fails, perform the following steps on the affected DataNode:

1. Put the DataNode in maintenance mode.
2. Stop the HDFS DataNode software.
3. Shut down Data Optimizer.
4. Choose one of the following actions:
   * If the metadata store is corrupted, delete all metadata store files (`metadata.db3*`) stored in the folder identified by the `CACHE_DIR` or `MD_STORE_DIR` (if present) configuration parameter.
   * If the drive hosting the folder identified by the `CACHE_DIR` or `MD_STORE_DIR` (if present) configuration parameter has failed, then change the parameter to point to a folder on a healthy drive.
5. Edit the Data Optimizer configuration file for the DataNode and add or edit the property `RECOVERY_MODE`, to set the value to `true`.
6. Restart Data Optimizer.
7. Restart the HDFS DataNode software.
8. Take the HDFS DataNode out of maintenance mode.

After completing the these steps, the Data Optimizer software runs in a passive, opportunistic recovery mode and is fully functional. As file system operations are performed, Data Optimizer rebuilds its local metadata store opportunistically.

**Note:** Passive recovery does not fully restore the local metadata store to an authoritative state; active recovery is required for that purpose.

### Restoring the metadata store to its authoritative state

To force an active recovery, perform the following steps:

1. SSH to the DataNode in question.
2. Turn logging for the Data Optimizer instance up to DEBUG. See **Adjusting log level at run time** in **Log levels**.
3. Put the DataNode in maintenance mode.

   **Note:** To ensure that all metadata has been recovered, run the `du` command at least twice while no other processes are modifying the contents of the *mount\_point* folder. After you have had two concurrent successful `du` passes, with the number of records in the metadata store (`md_cache_size`) being the same after the last two successful passes, you can be confident that all metadata has been recovered.
4. Run the following commands:

   ```
   `ldoctl metrics collect sudo -u *user* du -s *mount\_point*; [ $? == 0 ] && (echo "Success") || (echo "Failure") `
   `ldoctl metrics collect sudo -u *user* du -s *mount\_point*; [ $? == 0 ] && (echo "Success") || (echo "Failure") `
   `ldoctl metrics collect journalctl -et ldo -g '"md_cache_size"' `
   ```

   * *user* is the username of the user matching the `UID` parameter in the configuration file, that is the user with access to the file system.
   * *mount\_point* is the folder matching the `MOUNT_POINT` parameter in the configuration file, that is where Data Optimizer is mounted.
   * The `du` command attempts a recursive folder listing and metadata poll of the entire file system.
   * The `ldoctl` command emits metrics to the systemd journal. Run this command before and after each `du` command.
   * The `journalctl` command grabs the metrics you are interested in from the journal. If the `du` command finishes successfully it prints "Success" on the window upon completion; otherwise, it prints "Failure."

   The following example shows the command with two successful results:

   ```
   $ `ldoctl metrics collect`
   $ `sudo -u <user> du -s <mount_point>; [ $? == 0 ] && (echo "Success") || (echo "Failure")`
   321577600 /mnt/ldo/data/
   Success
   $ `ldoctl metrics collect` 
   $ `sudo -u <user> du -s <mount_point>; [ $? == 0 ] && (echo "Success") || (echo "Failure")`
   321577600 /mnt/ldo/data/
   Success
   $ `ldoctl metrics collect`
   $ `journalctl -et ldo -g '"md_cache_size"'`
   … [t:3892][metrics.c:231] {"type": "counter", "event": "md_cache_size", "total": 1},
   … [t:3892][metrics.c:231] {"type": "counter", "event": "md_cache_size", "total": 2512325},
   … [t:3892][metrics.c:231] {"type": "counter", "event": "md_cache_size", "total": 2512325},

   ```
5. If the `du` command completes successfully twice in a row, compare the last two totals for md\_cache\_size metrics.

   If the numbers match, all metadata from the S3 bucket has been recovered locally in the metadata store.
6. Perform the following steps based on the success or failure of the previous command and the comparisons of md\_cache\_size metrics:
   * If the result of the previous command is "Failure," or the last two md\_cache\_size totals do not match:
     1. Repeat the process, running the `du`, `ldoctl`, and `journalct` commands until you have two concurrent successful results with matching totals.

        ```
        `sudo -u *user* du -s *mount\_point*; [ $? == 0 ] && (echo "Success") || (echo "Failure") 
        ldoctl metrics collect 
        journalctl -et ldo -g '"md_cache_size"' `
        ```
     2. If the `du` command fails, it reports a list of the failed files or folders. If the list of failed resources is shrinking or changing, or the totals reported by the metrics are increasing, then the active recovery is making progress.
     3. If over several passes the `du` command reports “Failure,” and the list of failing resources does not change, that might indicate the active recovery is not making progress and additional troubleshooting is required. See the [Pentaho Customer Portal.](https://support.pentaho.com/hc/en-us)
   * If the result of the previous command is "Success" and the last two md\_cache\_size totals match:
     1. Edit the Data Optimizer configuration file for the DataNode and find the property `RECOVERY_MODE`. Remove the property or set the value to `false`.
     2. Use the `ldoctl` command line tool to reload the configuration file and take the software out of recovery mode as follows:

        `ldoctl config reload`
     3. Take the DataNode out of maintenance mode.

### Data Optimizer alerts

Pentaho Data Optimizer gives the alerts for Ambari. In addition to standard service alerts that Ambari gives for all services, the Data Optimizer installation delivers an alert called **PDO metadata store verification**. This alert monitors the volume’s metadata database and alerts users if there is evidence of corruption. In the event of corruption see: [Maintain Data Optimizer metadata](#maintain-data-optimizer-metadata) for possible solutions.

## The ldoctl command line utility

You can access the following `ldoctl` command line utility functions to help maintain and monitor Data Optimizer:

* Reloading the configuration file at run time to apply new configurations without restarting the software.
* Collecting and marking logs to identify specific events and tracking the performance or issues.
* Collecting performance metrics.

You can find the `ldoctl` utility documention in `man` pages and inline help. You can also find examples of how to use this utility throughout the guide.

## Troubleshoot Data Optimizer

Use the following best practices when troubleshooting:

* [Access the Data Optimizer volumes directly](#access-the-data-optimizer-volumes-directly)
* [Tiering HDFS Blocks to Data Optimizer](#tiering-hdfs-blocks-to-data-optimizer)
* [Data Optimizer logging](#data-optimizer-logging)
* [Data Optimizer configuration troubleshooting](#troubleshoot-data-optimizer)
* [Hitachi Content Platform (HCP) configuration troubleshooting](#hitachi-content-platform-hcp-configuration-troubleshooting)
* [Data Optimizer does not start](#data-optimizer-does-not-start)

### Access the Data Optimizer volumes directly

When necessary, you can access the Data Optimizer volume directly for troubleshooting. This might include performing directory listings, checking file status, or running the `df` command to report file system usage. In all these cases, access the volume as either the root user or as the **System User** specified in the Data Optimizer configuration. The following examples show how to directly access the volumes:

1. Attempt to access as `svcusr` user (Permission denied): Attempting to access the Data Optimizer mount as the `svcusr` user might result in a "permission denied" error.

   ```
   [svccusr]# ls -l /ldo/mnt
   ls: cannot access /ldo/mnt: Permission denied
   d????????? ? ?    ?    ?            ? mnt

   ```
2. Successful access as `root` and `hdfs` users:

   * Using the `root` or `hdfs` users for the `ls` operation succeeds.
   * The mount is owned by the `hdfs` user and `hdfs` group, with the `hdfs` user having full `rwx` (read, write, execute) permissions, and other users in the `hdfs` group having `rx` (read, execute) permissions.

   ```
   [svccusr]# sudo ls -l /ldo/mnt
   drwxr-x--- 1 hdfs hdfs 0 Aug  8  1995 dn

   [svccusr]# sudo -u hdfs ls -l /ldo/mnt
   drwxr-x--- 1 hdfs hdfs 0 Aug  8  1995 dn

   ```
3. Failed access using `sudo` to the `hdfs` group:

   * Sudoing to the `hdfs` group might still result in a "permission denied" error when accessing the LDO mount.
   * Ensure you use either the root user or the owner to access Data Storage Optimizer mounted volumes.

   ```
   [svccusr]# sudo -g hdfs ls -l /ldo/mnt
   ls: cannot access /ldo/mnt: Permission denied

   ```

#### Troubleshooting using direct access

Perform the following steps to use `sudo` for basic file operations in the Data Optimizer volume to troubleshoot through direct access:

1. Create and work in your own folder.
   1. Do not write to or modify folders created by HDFS.
   2. Create your own folder in the Data Optimizer volume.
   3. Write or copy files into your folder.
2. Verify with an S3 client:
   1. Verify that the folders and files are in the bucket as expected using an S3 client.
   2. Read the files back and compute checksums to verify the content.
3. Refer to logs for issues:
   1. Refer to the Data Optimizer logs if you encounter any issues.
   2. Increase the log level to DEBUG if necessary.
4. Enable AWS SDK logging for network issues:
   1. If the error message indicates the issue might be between the Data Optimizer instance and the S3 bucket (S3 SDK, Network, HCP, and so on.), enable AWS SDK logging to gain further insights.

### Tiering HDFS Blocks to Data Optimizer

Once you have verified that the Data Storage Optimizer is functioning correctly with the direct access method, the next step is to ensure that the datanode can tier block replicas to Data Optimizer. To test HDFS tiering to Data Optimizer, you need to set storage policies in HDFS and write to COLD folders or tier COLD files using the mover service.

Perform the following steps to verify block storage:

1. Use the `hdfs fsck` command with the

   ```
   --blocks --files
           --locations
   ```

   arguments to confirm that the blocks for all files set to the COLD storage policy are on ARCHIVE storage.
2. Perform recursive directory listings of the Data Optimizer mount points on the datanodes using the `find` or `tree` command.
3. Compare these listings with similar listings from the Data Optimizer bucket using the AWS CLI or other S3 clients. Ensure that everything HDFS wrote to the Data Optimizer mount was also written to the Data Optimizer bucket.

To get Instance ID:

1. Use the command `journalctl -t ldo | grep "instance id"` to retrieve the ID for the Data Optimizer volume on a node and match it to the top-level folder in the S3 bucket.
2. You can also find the instance ID in the `.lock.chillfs` file in the Data Optimizer instance’s cache directory.

Once you have validated that the Data Optimizer instance is functioning properly with the direct access method, and HDFS is configured to use Data Optimizer volumes as ARCHIVE storage, you can verify that HDFS files are properly tiering to Data Optimizer.

You can cause HDFS blocks to be written to Data Optimizer volumes in two ways. The first is to create a folder in HDFS, set the storage policy on the folder to COLD/WARM, and then to write files to that folder. The second is to set the storage policy for existing HDFS files and folders to COLD or WARM and then run the mover service, targeting those files and folders with the required storage policy.

To write directly to a COLD directory, create the directory in HDFS, set the policy on the directory to cold, and write files to the cold directory:

<figure><img src="https://1897852526-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNjj4joO63OgOTabje2xP%2Fuploads%2FFrxYIp4llTbDiPH2cdoL%2Fimage.png?alt=media&#x26;token=a67c048d-8269-4f73-b932-72c6b66ec722" alt=""><figcaption></figcaption></figure>

If using the mover service, you should first identify the locations of the blocks you will be tiering to Data Optimizer. To do this use the `hdfs fsck` command with the `-blocks -files -locations` arguments. This will provide a list of the current block replicas and their datanode location.

For more information on HDFS storage types, storage policies, and the mover service, see HDFS Heterogeneous Storage documentation for your Hadoop distribution.

### Data Optimizer logging

You can acquire Data Optimizer logs through Cloudera's and Ambari's log collectors or by directly accessing the log files.

#### Viewing logs on Cloudera

To view logs through Cloudera, go to **Diagnostics** > **Logs**. All logs collected by Cloudera will be present here. To filter out logs specific to Data Optimizer, enter `Data Storage Optimizer` in the **Services** filter. You can view and download specific log files through Cloudera’s log viewer.

#### Viewing logs on Ambari

Depending on the version of Ambari you are using, the **Log Search** service, and other services it depends on, you might first need to install and configure it. If the **Log Search** service was installed before installing Data Optimizer, restart the Log Search service to begin indexing the logs in Data Optimizer. Without this service, Data Optimizer still logs; however, logs will not be integrated into Ambari, and you should access them natively.

To view logs through Ambari, use the **Log Search UI** link in the **Quick Links** drop-down menu in the **Log Search** service.

<figure><img src="https://1897852526-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNjj4joO63OgOTabje2xP%2Fuploads%2FDk1g34c1kZvVN2bVRI5k%2Fimage.png?alt=media&#x26;token=da3208ed-9324-40cd-a54f-ca0149d933f3" alt=""><figcaption></figcaption></figure>

To isolate only Data Optimizer logs, in the **Troubleshooting** and **Service Logs** tabs, include the **ldo\_volume** as part of the component. This is the default component for Data Optimizer, but can be changed in `Advanced ldo-logsearch-conf` configurations.

#### Viewing logs natively

You can access logs, located at `/var/log/ldo`, with the latest logs located at `/var/log/ldo/ldo.log` with logs rotating when it reaches 128 MB.

**Note:** Configurations for Data Optimizer cannot be changed.

#### Marking logs

Inserting entries into the logs can help mark the beginning or end of a test or series of tests. The `ldoctl` command line utility gives a command to easily insert entries into the log. Use the following command to insert a custom message into the log:

```
ldoctl logs mark "Message to put in the log."
```

#### Log format

The Data Optimizer log format is as follows:

`<date> <LOG_LEVEL> ldo.<component>:<line>: [p:<pid>][t:<thread>] <message>`

**Note:** The date format is `YYYY-mm-dd HH:MM:ss,ms`.

#### Log levels

By default, the Data Optimizer logs events at the INFO level. This level logs rare events such as startup and shutdown, and events that should not occur, such as errors or warnings. You can adjust the logging level as necessary based on the following levels:

* `ALERT`: Internal API Violated, Possibly a Bug.
* `ERROR`: An Error Occurred, Immediate Action Required.
* `WARNING`: A Significant Event, No Immediate Action Required.
* `INFO`: Notable Events in Normal Product Flow, No Action Required.
* `DEBUG`: Verbose Logging, Useful for Troubleshooting.

Each log level includes itself and all the levels above it in the list. For example, WARNING includes ALERT, ERROR, and WARNING messages. DEBUG includes all levels.

The desired logging level is specified by setting the `LOG_LEVEL` parameter in the configuration file. When Data Optimizer starts up it reads this parameter and sets its logging level accordingly. Typically, you would not want to set this level to anything more than WARNING or INFO, as that might result in unnecessarily verbose logging to your systemd journal.

#### Adjusting log level at run time

In order to troubleshoot an issue, you might want to increase the logging level without restarting the software, as a restart might resolve the issue before you have an opportunity to determine the cause. In this case, the `ldoctl` can be used to get and set the log level of a live running instance:

```
ldoctl -m <mount_pont> get
ldoctl -m <mount_point> set <log_level>
```

**Note:** Setting the logl level through ldoctl will not persist if ldo is restarted.

#### AWS S3 SDK logging

In some cases, particularly when troubleshooting issues between the Data Optimizer instance and the Hitachi Content Platform,you may want to see the detailed AWS SDK logs. These logs include many client-side details as to the content of the requests being sent to the HCP and the detailed content of the responses received. To enable this logging the `LOG_SDK` configuration parameter must be properly set, and the `LOG_LEVEL` parameter set to DEBUG. This logging is enabled only at start time and cannot be enabled by reloading the configuration file. When enabled, details about the communication between the Data Optimizer instance and the HCP are logged to a file called `ldo_aws_sdk_*datestamp*.log` in the specified folder, where *datestamp* represents the day and hour logging began.

As a best practice, it is recommended to keep SDK logging disabled unless actively troubleshooting. The logs can get quite large, and Data Optimizer does not manage or rotate these logs. It is up to the user to delete these files when done with troubleshooting exercises.

### **Data** **Optimizer configuration troubleshooting**

To troubleshoot Data Optimizer configuration issues, verify the following:

1. All required configuration parameters are defined, and the values are correct.
   * All parameter names and most values are case sensitive.
   * Make sure not to use Windows style new lines if you edited on Windows.
   * Verify the log for when the configuration file is loaded and confirm that there are no errors and that all loaded parameters are correct. Look for the string “Found config key=.”
2. Paths in the configuration file are correct and case matches the path on the local file system.
3. Ownership and permissions are correct for all required files and directories.
   * All files and directories are owned by the user matching UID in the configuration file.
   * Permissions = 770 for directories CACHE\_DIR, MD\_STORE\_DIR, MOUNT\_POINT, and LOG\_SDK (if specified)
   * Permissions = 770 for parent folder of METRICS\_FILE (if specified)
   * Permissions = 640 for the configuration file.

### **Hitachi Content Platform (HCP) configuration troubleshooting**

To troubleshoot Hitachi Content Platform (HCP) configuration issues, verify the following:

1. HCP is reachable over the network at ports 80/443 from the DataNode.
2. HCP is properly configured according to the instructions in this guide and the HCP documentation.
   * Your user credentials are correct, and your user has Namespace Management permission selected.
3. HCP Hard Quotas and Namespace Quotas have not been exceeded.

### **Data** **Optimizer does not start**

If Data Optimizer does not start, verify the following:

1. Verify the log for an indication of failure.If not, try starting in DEBUG logging mode.
2. Make sure that the mount folder is empty.You will get an error starting the software if the mount point is not empty.
3. Verify the file and folder ownership permissions.

In some cases, if a mount point is started manually, and particularly if it is started as the root user, certain files and directories might end up being inaccessible to the HDFS user who is supposed to own these assets. Verify that the following files and directories are owned by the correct user (Hortonworks - hdfs:hadoop, Cloudera - hdfs:hdfs). Including hidden files:

`/tmp/ldo_*`

`/tmp/ldo_*/*`

All directories specified in the Data Optimizer configuration, including the Data Optimizer Mount Point and the Data Optimizer Cache Directory.

## Monitor Data Optimizer

Data Optimizer maintains operation and performance metrics that are useful for ongoing monitoring of the software. To instruct Data Optimizer to emit these metrics use the `ldoctl` command line utility as follows:

```
ldoctl metrics collect
```

The command causes Data Optimizer to emit a JSON string containing the metrics to the `systemd` journal log, or to the file specified in the `METRICS_FILE` parameter in the configuration file, if specified and permissions are properly set on the target folder.

`ldoctl metrics collect`

The command causes Data Optimizer to emit a JSON string containing the metrics to the `systemd` journal log, or to the file specified in the `METRICS_FILE` parameter in the configuration file, if specified and permissions are properly set on the target folder.

The format of the JSON string is as follows:

```
{
    "date": "2019 10 25 13:48:00 +0000",
    "metrics": [
        {
            "event": "*event\_name*",
            "max": *max\_value*,
            "mean": *mean\_value*,
            "min": *min\_value*,
            "stddev": *stddev*,
            "total": *event\_count*,
            "type": "timer"
        },
        {
            "event": "*event\_name*",
            "total": *event\_count*,
            "type": "counter"
        }
        
    ]
}

```

### Types of metrics events

There are two types of metrics events: `timer` and `counter`. Both `timer` and `counter` metrics events have an event name in the `event` field.

* **Timer events**

  Report the maximum (`max`), mean (`mean`), minimum (`min`), and standard deviation (`stddev`) of the amount of time it takes to complete certain measured internal operations. The `total` field for timer events is always a count of the number of times the event has occurred. Following is a list of the `timer` events:

  * `get_attr`: Filesystem request for file attributes, that is, `stat`
  * `readdir`: Directory listing, includes S3 listing if applicable
  * `md_cache_add_entry`: Adding an entry to the local metadata store
  * `md_cache_update_entry`: Updating an entry in the local metadata store
  * `md_cache_evict_entry`: Removing an entry in the local metadata store
  * `md_cache_get_entry`: Getting an entry from the local metadata store
  * `md_cache_copy_entry_new_path`: Copying an entry in the local metadata store
  * `md_cache_get_size`: Counting the entries in the local metadata store
  * `md_cache_readdir_root`: Listing the root directory from the local metadata store
  * `md_cache_readdir`: Listing a directory from the local metadata store
  * `*_prepare_stmt`: Preparing a DB operation for the local metadata store
  * `*_exec_stmt`: Executing a DB operation on the local metadata store
* **Counter Events**

  The `total` field can be a count of occurrences or some other count. Following is a list of the `counter` events:

  * `md_cache_size`: The number of entries in the local metadata store
  * `md_cache_size`: The number of entries in the local metadata store
  * `open_file_size`: The number of currently open file handles in the Data Optimizer volume
  * `s3_op_put`: The count of S3 PUT requests to the HCP
  * `s3_op_get`: The count of S3 GET requests to the HCP
  * `s3_op_list`: The count of bucket listing requests to the HCP
  * `s3_op_delete`: The count of S3 DELETE requests to the HCP
  * `s3_op_copy`: The count of S3 put-copy requests to the HCP
  * `s3_op_error`: The count of S3 error responses from the HCP
  * `warnings`: The count of logged warnings
  * `errors`: The count of logged errors

**Note:** All values reported in the metrics are cumulative and reset only when Data Optimizer restarts.
