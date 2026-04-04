# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/pdso-maintain-data-optimizer-metadata-cp/pdso-restoring-the-metadata-store-to-its-authoritative-state.md

# Restoring the metadata store to its authoritative state

To force an active recovery, perform the following steps:

1. SSH to the DataNode in question.
2. Turn logging for the Data Optimizer instance up to DEBUG. See [Adjusting log level at runtime](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/data-storage-optimizer-logging/pdso-log-levels).
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
   * The `journalctl` command grabs the metrics you are interested in from the journal.\
     If the `du` command finishes successfully it prints "Success" on the window upon completion; otherwise, it prints "Failure."

   Here is an example showing the command with two successful results:

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
     3. If over several passes the `du` command reports “Failure,” and the list of failing resources does not change, that might indicate the active recovery is not making progress and additional troubleshooting is required. Contact [Pentaho Customer Portal.](https://support.pentaho.com/hc/en-us)
   * If the result of the previous command is "Success" and the last two md\_cache\_size totals match:
     1. Edit the Data Optimizer configuration file for the DataNode and find the property `RECOVERY_MODE`. Remove the property or set the value to `false`.
     2. Use the `ldoctl` command line tool to reload the configuration file and take the software out of recovery mode as follows:

        `ldoctl config reload`
     3. Take the DataNode out of maintenance mode.
