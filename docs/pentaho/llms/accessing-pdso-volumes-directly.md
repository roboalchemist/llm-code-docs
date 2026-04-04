# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/accessing-pdso-volumes-directly.md

# Access the Data Optimizer volumes directly

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
