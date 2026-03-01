# Source: https://docs.curator.interworks.com/upgrading_migration/backups/manual_restoration_of_curator_backup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual Restoration of Curator Backup

> Step-by-step guide for manually restoring Curator from a full backup when automated restoration fails.

If you haven't attempted to use the Curator interface to restore from a full backup, go do that now
(Backend> Settings > Curator > Import/Export > Full Backup tab).
This guide is only needed if that fails for some hard-to-fix reason and it's an emergency to restore from a full backup.

It's also worth noting that, by default, Curator's full backups are stored on the same server as Curator.  If
something were to happen to the server, these could potentially disappear at the same time that Curator
does.  Please take steps to set up a server-level backup and/or store Curator's full backups in a safe, external location.

## Preface

Curator's full backups are a zip archive containing the following files:

* MySQL/MariaDB database dump (as a SQL script)
* The contents of Curator's web root directory, which contains all of the code, configuration, and uploads (as a zip archive)

The restoration process essentially overwrites all of the files on the server with the contents of the web
root directory and runs the SQL script to overwrite the database.  These are the steps you'll need to perform
when manually restoring from a full backup.

## Handling Different Database Connections

Curator stores the database connection details in `<web root>/config/database.php`.  The zip archive of the
web root within a full backup also contains these connection details.  If the database connection differs
from the system the backup originated from to the system being restored over, you'll need to perform these
steps prior to restoring:

1. Unzip the full backup zip archive to a temporary location (i.e. not inside either Curator portal’s actual web root).
2. Unzip the web root zip archive.
3. Modify the `config/database.php` file as needed in the extracted web root folder to match the connection
   details of the database you'll be restoring over.
4. Re-zip the extracted web root folder (use the same file name for the resulting zip archive).  DO NOT zip
   up the folder itself, just the contents (you should have a list of folders including plugins, storage, and vendor).
5. If the MySQL/MariaDB database name (not to be confused with host or username) differs, rename that part
   of the database dump SQL script.  Be sure to retain the date-stamp and file extension portions of the file
   name.  Also, open the file and update any references to the database name in the first \~30 lines.
6. Re-zip the web root zip archive (not to be confused with the extracted web root directory) and the
   database dump SQL script as the full backup (use the same file name for the resulting zip archive).
7. Transfer the updated full backup zip archive to the system you wish to restore over and place it in the
   directory where full backups are stored (default is `<web root>/storage/temp/`).

## Manually Restoring the Database

If you haven't already, unzip the full backup zip archive to extract the database dump and transfer that SQL
script to the system you'll be restoring over.

Make the following replacements in the commands below.  If you don't know the values, look at the
`<web root>/config/database.php` file on the system you'll be restoring over.

* `$host`: The database host.  This is normally localhost unless you have an external database.
* `$user`: The database username.
* `$port`: This is almost always 3306, unless you've customized your database configuration to run on a different port.
* `$name`: This is the database name.  Each MySQL/MariaDB host can store many different databases, usually
  this is Curator, but it could be different.
* `$dbDumpFilename`: This is the file name to the database dump file.  Include the full file path if running
  the command from a different directory that where the SQL script lives.

*NOTE: You will be prompted for the database password while the command runs.*

```MySQL  theme={null}
mysql -h $host -u $user -p --port=$port --database $name < $dbDumpFilename
```

## Manually Restoring the File System

### Step 0 for Linux Systems

Before beginning on Linux systems, run the following commands to determine which system user and group owns
Curator's web root.  It will be needed during the process.

```Linux  theme={null}
cd /var/www/html
ls -l
```

The user and group should either be `apache` or `www-data` and should be listed next to all of the files.
The commands below will assume apache, but replace it with www-data if your system lists it here instead.

### Restoration Process

1. If you haven't already, unzip the full backup zip archive to extract the web root directory backup and
   transfer that zip archive to the system you'll be restoring over.
2. In a temporary location on the Curator server outside of Curator's web root directory (make note of the
   location), unzip the web root directory backup (i.e. the file that matches the pattern: `webroot_YYYYMMDD_HHMMSS.zip`).
   * Linux Command:
     `sudo -u apache unzip webroot_YYYYMMDD_HHMM.zip`
   * On Windows systems, you should be able to utilize the built-in zip extract function, though
     alternatives like 7-zip may be faster.
3. In the web root directory, delete directories as follows:
   * Linux Command:
     `sudo rm -Rf /var/www/html/modules /var/www/html/plugins /var/www/html/themes /var/www/html/vendor`
   * On Windows systems, delete these folders using Windows Explorer:
     * modules
     * plugins
     * themes
     * vendor
4. Copy the contents of the extracted web root backup to the actual web root directory.
   * Linux Command:
     `sudo -u apache cp -a /path/to/extracted/webroot/backup/* /var/www/html/`
   * On Windows systems, use a copy/paste or select/drag operation within Windows Explorer.
5. Fix file permissions as needed.  See this document for details:
   [Filesystem Permissions](/server_management/system_administration/filesystem_permissions)
