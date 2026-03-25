# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/data-storage-optimizer-configuration-troubleshooting.md

# Data Optimizer configuration troubleshooting

To troubleshoot Data Optimizer configuration issues, verify the following:

1. All required configuration parameters are defined, and the values are correct.
   * All parameter names and most values are case sensitive.
   * Make sure not to use Windows style new lines if you edited on Windows.
   * Verify the log for when the configuration file is loaded and confirm that there are no errors and that all loaded parameters are correct. Look for the string “`Found config key=`.”
2. Paths in the configuration file are correct and case matches the path on the local file system.
3. Ownership and permissions are correct for all required files and directories.
   * All files and directories are owned by the user matching UID in the configuration file.
   * Permissions = 770 for directories `CACHE_DIR`, `MD_STORE_DIR`, `MOUNT_POINT`, and `LOG_SDK` (if specified)
   * Permissions = 770 for parent folder of `METRICS_FILE` (if specified)
   * Permissions = 640 for the configuration file.
