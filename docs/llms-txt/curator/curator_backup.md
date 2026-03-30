# Source: https://docs.curator.interworks.com/upgrading_migration/backups/curator_backup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Curator Backup

> Learn about Curators comprehensive backup options beyond basic Import/Export functionality.

The Import / Export is a great way to backup your Curator data but sometimes a more complete backup is
needed. The Full Backup will export an entire snapshot of all your Curator data (it's a full database and
filesystem backup of the Curator webroot directory). Curator will even show you up-to-date stats on how much
free space you have available on your server to ensure you have room.

***Modifying the Full Backup Settings***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Backups** in the left -hand menu.
3. Click on the gear icon to display a popup.  From here you can modify the location/frequency and retention options.

***To Manually Create a new Curator Backup:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Backups** in the left-hand menu.
3. Click the "Take New Backup" button to start a backup.  If you would like to check the status of the backup
   while it is running, you can view the active status under the
   **Settings** > **Curator** > **Queued Processes** in the left navigation.

***To Restore From a Full Backup:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Backups** in the left navigation.
3. Find the backup from the list view (NOTE: They are all appended with a timestamp from when they were
   taken), and click the "Restore Backup" icon (counter clockwise arrow) to restore Curator to exactly mirror
   the time the backup was taken.
