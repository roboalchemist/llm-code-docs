# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/accessing-pdso-volumes-directly/pdso-troubleshooting-using-direct-access.md

# Troubleshooting using direct access

Perform the following steps to use `sudo` for basic file operations in the Data Optimizer volume to troubleshot through direct access:

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
