# Source: https://northflank.com/docs/v1/application/databases-and-persistence/migrate-data-to-northflank/migrate-your-mysql-database-to-northflank.md

# Migrate your MySQL database to Northflank

You can import your existing MySQL database to Northflank by creating and uploading a dump of your database, or providing a connection string to your existing database.

Imports will be more reliable if the database you are importing to is the same, or a newer, version of MySQL as the source database you are exporting from.

If you have more than one database to import from the same MySQL instance you should use the connection string method, which will import all the databases the given user has access to.

> [!warning] 
> Both methods of importing a database will erase all existing user databases in the Northflank addon, if there are any.

You should first [create a Northflank MySQL addon](https://app.northflank.com/s/project/create/addon) to import to, and [connect to it](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-mysql-on-northflank#connect-to-mysql) with your preferred administration tool. If you require your Northflank deployment to remain private you can [forward it](https://northflank.com/docs/v1/api/forwarding) to your local machine and use the non-external endpoints and commands to connect.

## Permissions

The user for the database you are exporting from may need the following permissions: `SELECT`, `SHOW_VIEW`, `TRIGGER`, `LOCK TABLES`, and `PROCESS`. You can grant permissions to a user with the following SQL query:

```sql
GRANT <PRIVILEGE> ON <DATABASE>.* TO <USER>@'localhost';
```

Replace the values with the required privilege, the database you're trying to export, and the user.

## Import from dump

Importing from a dump of a database will erase all existing user databases on the target MySQL addon, and your dump will be imported as the default database on the Northflank addon (specified in your addon’s connection details as `DATABASE`). You can only import one database using this method, if you have more than one database to import you should use the [connection string method](#import-from-connection-string).

To start, you will need to generate a dump of your existing database using either a GUI or command line tool. The exact method to access your existing database will depend on your current service provider.

### Create a dump using MySQL Workbench

You can create a dump of your source database using [MySQL Workbench](https://www.mysql.com/products/workbench/). Connect to your source MySQL server and select data export from the server menu.

Select the database and tables you want to export. Ensure `dump structure and data` is selected, `include create schema` is not selected, and choose to export the dump to a self-contained file. In advanced options enter `OFF` in the `set-gtid-purged` field and create your dump.

### Create a dump using mysqldump

You can create a dump in your terminal using the [mysqldump tool](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html), part of the [mysql client](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install.html).

You should only dump a single database and you are recommended to use the following command to generate your dump:

```shell
mysqldump "--host=<HOST>" "--port=<PORT>" "--user=<USER>" -p "--skip-comments" "--no-set-names" "--no-create-db" "--set-gtid-purged=OFF" "<DATABASE>" > database.sql
```

Replace the values for `HOST`, `PORT`, `USER`, and `DATABASE` with the details for your current MySQL instance, providing a user with sufficient permissions to dump the database. You must include the `--no-create-db` and `--set-gtid-purged=OFF` options in your command, or you will not be able to restore from the dump in your Northflank addon.

The file will be generated at the given path, or in the working directory if no path is specified for the output.

### Import dump to Northflank

Navigate to your MySQL addon’s backups page and click import backup. Enter a recognisable name and select either upload, if your dump is stored locally, or URL if your dump is hosted online and accessible. You can upload the dump as plain text or as a gzipped file (`.gz`).

After selecting your file, or entering the URL, click upload import. All backups stored on Northflank are encrypted at rest, to keep your data private and secure.

Select the uploaded import from the backups list and click restore  to begin importing the database to your Northflank MySQL addon. All user data in the existing MySQL database on Northflank will be erased, excluding the system databases `information_schema` and `performance_schema`, before importing the contents of the dump file.

You can click on a restore listed in a backup to view the logs of the restoration, and you will be able to see in the backups list and the list of restores whether the restoration was successful.

You can now double-check that the import has run as you expected it to by accessing the addon using your preferred administration tool.

> [!note] 
> Northflank will import to the default database if your dump doesn't include an explicit `USE` statement. You can find the name of the default database in your Northflank addon's connection details as `DATABASE`.

## Import from connection string

You can import one or more databases from your source MySQL database by [providing a JDBC connection string](https://dev.mysql.com/doc/connector-j/en/connector-j-reference-jdbc-url-format.html). Create a new MySQL addon in Northflank, or navigate to an existing one, and select import backup from the backups page.

Enter a recognisable name and select connection string as the import method, and provide the connection string for your source database. The source database must be publicly available and the connection string must take the format:

```
jdbc:mysql://username:password@host:port/database
```

Only databases that the supplied credentials have permission to access will be imported. When you start the import, Northflank will create dumps of all the databases available.

After importing, select the import from the backups list and click restore  to begin importing to your Northflank MySQL addon. All user data in the existing MySQL database on Northflank will be erased, excluding the system databases `information_schema` and `performance_schema`, before restoring from the import.

Each database will be imported with its existing name, the default Northflank database will be recreated as an empty database.

You can now double-check that the import has run as you expected it to by accessing the addon via pgAdmin, or [forward it using the Northflank CLI](https://northflank.com/docs/v1/api/forwarding) to connect locally. If you need to make any changes you can connect to your Northflank MySQL addon using the admin URI connection strings, or by using the `ADMIN_USERNAME` and `ADMIN_PASSWORD` login details.

## Next steps

- [Deploy MySQL on Northflank: MySQL is a fast, reliable, scalable, and easy to use open-source relational database system.](/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-mysql-on-northflank)
- [Access a database: Securely access your database locally or make it available online.](/v1/application/databases-and-persistence/access-a-database)
- [Backup, restore, and import your data: Create and import backups of your database, or restore from an existing backup.](/v1/application/databases-and-persistence/backup-restore-and-import-data)
- [Use a database with your applications: Securely access your database in your project's applications and services.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)
