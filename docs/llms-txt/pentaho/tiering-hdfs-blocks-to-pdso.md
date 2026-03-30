# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/tiering-hdfs-blocks-to-pdso.md

# Tiering HDFS Blocks to Data Optimizer

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

![](https://github.com/pentaho/documentation/blob/main/PDC/10.2/Data%20Optimizer/PDO%20Installing%20Data%20Optimizer%20Volumes/LDO%20Install/PDSO%20Install%20in%20Hadoop%20Cluster/PDSO%20Maintain%20\(Landing%20page\)/Troubleshoot%20Data%20Storage%20Optimizer%20FS/Tiering%20HDFS=GUID-3C9C821E-A533-422B-9CE8-771B961DA0B4=1=en=Low.png)

If using the mover service, you should first identify the locations of the blocks you will be tiering to Data Optimizer. To do this use the `hdfs fsck` command with the `-blocks -files -locations` arguments. This will provide a list of the current block replicas and their datanode location.

For more information on HDFS storage types, storage policies, and the mover service, see HDFS Heterogeneous Storage documentation for your Hadoop distribution.
