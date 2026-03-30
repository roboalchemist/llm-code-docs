# Source: https://docs.curator.interworks.com/upgrading_migration/backups/taking_a_manual_full_backup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Taking a Manual Full Backup

> Instructions for manually creating comprehensive Curator backups when built-in backup functionality is insufficient.

While we highly recommend using the built-in Full Backup functionality within Curator, there are times where
that isn't possible or when implementing your own full backup process.  This guide will cover the steps and
commands that Curator uses to take a full backup.  You may need to customize these steps for your own
purposes.

There are 2 sets of data that will need to be included in a full backup:

1. Curator's Database
2. Curator's File System

## Database Dump

The way Curator backs up its database is by dumping the structure and data contained in that database to a
SQL file. This SQL file will include the actual SQL code needed to recreate the tables and insert all of the data.

The command Curator runs is:

`mysqldump -h $host -u $user -p --port=$port --databases $databaseName > $backupFilename`

Where:

* `$host` is the host name where the database lives.  This is almost always localhost or 127.0.0.1.
* `$user` is the database user.  Get this from your *\<web root>*/config/database.php configuration file.
* `$port` is the port the database runs on.  This is almost always 3306.  Get this from your *\<web root>*
  config/database.php configuration file if it's something other than 3306.
* `$databaseName` is the name of the database inside of MariaDB/MySQL that houses Curator's data.  Get this
  from your *\<web root>*/config/database.php configuration file.
* `$backupFilename` is the file to save the SQL dump into.  Curator names this file `$databaseName`\_`$currentTimestamp`.sql

You will be prompted for the password when running this command.  Get the password from your *\<web root>*
config/database.php configuration file.

## Filesystem Backup

To back up Curator's files, Curator just zips the entire web root directory (i.e. /var/www/html or
C:\InterWorks\Curator), excluding any other full backup files.  Curator stores its full backup files in the
*\<web root>*/storage/temp directory as `full_backup_$currentTimestamp.zip` by default, but this backup
location may be configured to be a different directory.

## Curator Compatible Backups

If you are trying to create a backup that's compatible with Curator's Full Backup functionality so that it
can be restored with the click of a button, here are the details that will be important:

1. The full backup zip archive must follow this naming convention, where the the middle part is replaced by
   an appropriate timestamp: `full_backup_YYYYMMDD_HHMMSS.zip`.
2. The full backup zip archive must consist of 2 files:
   1. The database dump with the name of the database as the prefix (e.g. `curator_`), a timestamp that
      matches the full backup timestamp, and a `.sql` file extension.
      The name should look something like: `curator_YYYYMMDD_HHMMSS.sql`.
   2. The backup of the file system as a zip archive that must follow this naming convention, where the
      middle part is replaced by the same timestamp as the full backup: `webroot_YYYYMMDD_HHMMSS.zip`.
3. In order to be restored by Curator, this file must be placed in *\<web root>*/storage/temp/.
