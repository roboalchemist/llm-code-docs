# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/pdso-does-not-start.md

# Data Optimizer does not start

If Data Optimizer does not start, verify the following:

1. Verify the log for an indication of failure.

   If not, try starting in **DEBUG** logging mode.
2. Make sure that the mount folder is empty.

   You will get an error starting the software if the mount point is not empty.
3. Verify the file and folder ownership permissions.

   In some cases, if a mount point is started manually, and particularly if it is started as the root user, certain files and directories might end up being inaccessible to the HDFS user who is supposed to own these assets. Verify that the following files and directories are owned by the correct user (Hortonworks - hdfs:hadoop, Cloudera - hdfs:hdfs). Including hidden files:

   `/tmp/ldo_*`

   `/tmp/ldo_*/*`

   All directories specified in the Data Optimizer configuration, including the Data Optimizer Mount Point and the Data Optimizer Cache Directory.
