# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/pdso-maintain-data-optimizer-metadata-cp/pdso-recovering-from-loss-or-corruption-of-the-local-metadata-store.md

# Recovering from local metadata store failure or corruption

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
