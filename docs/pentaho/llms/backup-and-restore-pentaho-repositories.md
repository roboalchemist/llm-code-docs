# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-repository/backup-and-restore-pentaho-repositories.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-repository/backup-and-restore-pentaho-repositories.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-repository/backup-and-restore-pentaho-repositories.md

# Backup and restore Pentaho repositories

A complete backup and restore of your Pentaho repositories can be done through either the command (cmd) window or with the `File Resource` service in the Pentaho Rest APIs.

**Note:** If you are on Pentaho version 8.0 or earlier, as a best practice to avoid errors when exporting and importing repository contents, select specific content and not the entire repository. For more information, see [Importing and exporting PDI content with Pentaho 8.0 and earlier](https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-repository-issues/importing-and-exporting-8.0-and-earlier).

The backup process exports all content from the Pentaho Repository and creates a ZIP file, which includes:

* Users and roles
* All files (dashboards, reports, etc.)
* Schedules
* Data connections
* Mondrian schemas
* Metadata entries
* A manifest file

All of your content is pulled from this ZIP file when you restore the Pentaho Repository.

You must have appropriate administrator permissions on the server in order to perform a repository backup or restore.

## Step 1: Backup the Pentaho Repository

Backing up your Pentaho Repository is done through the use of command line arguments. You can customize the provided examples for your server.

If an argument is required for successful backup and has not been provided, the missing requirement is displayed in the cmd window. Backup results are also displayed in the window.

1. Open a cmd window and point the directory to the install location of your running Pentaho Server.
2. Use the `import-export` script with your arguments for backing up the repository.
3. Press Enter.

For example,

* **Windows**

  `import-export.bat --backup --url=http://localhost:8080/pentaho --username=admin --password=password --file-path=c:/home/Downloads/backup.zip --logfile=c:/temp/logfile.log --logLevel=DEBUG`
* **Linux**

  `./import-export.sh --backup --url=http://localhost:8080/pentaho --username=admin --password=password --file-path=/home/Downloads/backup.zip --logfile=/temp/logfile.log`

## Step 2: Restore the Pentaho Repository

Restoring your Pentaho Repository is also done through the use of command line arguments. The process for restoring both repositories is similar to the backup process, except for the differences shown in the provided examples. These examples can be customized for your particular server.

If an argument is required for successful restore and has not been provided, the missing requirement is displayed in the cmd window. Restore results are also displayed in the window.

1. Open a cmd window and point the directory to the install location of your running Pentaho Server.
2. Use the `import-export` script with your arguments for backing up the repository.
3. Press Enter.

For example,

* **Windows**

  `import-export.bat --restore --url=http://localhost:8080/pentaho --username=admin --password=password --file-path=c:/home/Downloads/backup.zip --overwrite=true --logfile=c:/temp/logfile.log --logLevel=DEBUG`
* **Linux**

  `./import-export.sh --restore --url=http://localhost:8080/pentaho --username=admin --password=password --file-path=/home/Downloads/backup.zip --overwrite=true --logfile=/temp/logfile.log`
