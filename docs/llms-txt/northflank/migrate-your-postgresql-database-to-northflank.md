# Source: https://northflank.com/docs/v1/application/databases-and-persistence/migrate-data-to-northflank/migrate-your-postgresql-database-to-northflank.md

# Migrate your PostgreSQL database to Northflank

You can import your existing PostgreSQL database to Northflank by creating and uploading a dump of your database, or providing a connection string to your existing database.

Imports will be more reliable if the database you are importing to is the same, or a newer, version of PostgreSQL as the source database you are exporting from.

If you have more than one database to import from the same PostgreSQL service you should use the connection string method, which will import all the databases the given user has access to.

> [!warning] 
> Both methods of importing a database will erase all existing user databases in the Northflank addon, if there are any.

You should first [create a Northflank PostgreSQL addon](https://app.northflank.com/s/project/create/addon) to import to, and [connect to it](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-postgresql-on-northflank#connect-to-postgresql) with your preferred administration tool. If you require your Northflank deployment to remain private you can [forward it](https://northflank.com/docs/v1/api/forwarding) to your local machine and use the non-external endpoints and commands to connect.

## Permissions

The user for the database you are exporting from must have the following permissions:

- `Connect` on the database(s) you want to export

- `Select` on all the tables in the database schema you want to export

- `Select` on all sequences in the database schema you want to export

You can grant permissions via a PostgreSQL administration tool such as pgAdmin, or via an SQL query, replacing `<DATABASE>`, `<SCHEMA>`, and `<USER>` with the relevant values for your database:

```postgresql
GRANT CONNECT ON DATABASE <DATABASE> to <USER>;
GRANT SELECT ON ALL TABLES IN SCHEMA <SCHEMA> TO <USER>;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA <SCHEMA> TO <USER>;
```

## Import from dump

Importing from a dump of a database will erase all existing user databases on the target PostgreSQL addon, and your dump will be imported as the default database on the Northflank addon (specified in your addon’s connection details as `DATABASE`). You can only import one database using this method, if you have more than one database to import you should use the [connection string method](#import-from-connection-string).

To start, you will need to generate a dump of your existing database, either using an administration tool such as [pgAdmin](https://www.pgadmin.org) or via the terminal using [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) . The exact method will depend on your current service provider.

### Create a dump in pgAdmin

To create a dump in pgAdmin, right click on a database and select backup…. Give your dump a recognisable name, and select `plain` or `compressed` as the format.

Open the Data/Objects settings and select `owner` and `privilege` under `do not save`.

Click on tools and open storage manager, then select your newly-created dump and download it by clicking the download button .

### Create a dump using pg_dump

You can create a dump using the `pg_dump` tool in your terminal. This can be run either on your server and then downloaded, or run locally, with the publicly accessible database URI:

`pg_dump "<DB_URI>" "--no-owner" "--no-privileges" "--no-password" "--no-tablespaces" > dumpfile`

The database URI should take the format:

```
postgresql://<USERNAME>:<PASSWORD>@<HOST><:PORT>/<DATABASE>?sslmode=require
```

Note: you may need to surround the URI with quotes for the command to work.

### Import dump to Northflank

Navigate to your Northflank PostgreSQL addon’s backups page and click import backup. Enter a recognisable name and select either upload, if your dump is stored locally, or URL if your dump is hosted online and accessible. You can upload the dump as plain text or as a gzipped file (`.gz`).

After selecting your file, or entering the URL, click upload import. All backups stored on Northflank are encrypted at rest, to keep your data private and secure.

Select the uploaded import from the backups list and click restore  to begin importing the database to your Northflank PostgreSQL addon. All user data in the existing PostgreSQL database on Northflank will be erased, except for the `postgres` system database, before importing the contents of the dump file.

You can click on a restore listed in a backup to view the logs of the restoration, and you will be able to see in the backups list and the list of restores whether the restoration was successful.

You can now double-check that the import has run as you expected it to by accessing the addon using your preferred administration tool.

> [!note] 
> Northflank will import to the default database if your dump doesn't include an explicit `\connect` statement. You can find the name of the default database in your Northflank addon's connection details as `DATABASE`.

## Import from connection string

You can import one or more databases from your source PostgreSQL database by [providing a connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING). Navigate to your Northflank PostgreSQL addon and select import backup from the backups page.

Enter a recognisable name and select connection string as the import method, and provide the connection string for your source database. The source database must be publicly available and the connection string must take the format:

```
postgresql://username:password@host:port/database?sslmode=require
```

Only databases that the supplied credentials have permission to access will be imported. When you start the import, Northflank will create dumps of all the available databases.

After importing, select the uploaded import from the backups list and click restore  to begin importing the dump to your Northflank PostgreSQL addon. All user data in the existing PostgreSQL database on Northflank will be erased, except for the `postgres` system database, before restoring from the imported dump.

Each database will be imported with its existing name, the default Northflank database will be recreated as an empty database.

You can now double-check that the import has run as you expected it to by accessing the addon via pgAdmin, or [forward it using the Northflank CLI](https://northflank.com/docs/v1/api/forwarding) to connect locally. If you need to make any changes you can connect to your Northflank PostgreSQL addon using the admin URI connection strings, or by using the `ADMIN_USERNAME` and `ADMIN_PASSWORD` login details.

## Next steps

- [Deploy PostgreSQL on Northflank: PostgreSQL, also known as Postgres, is a free and open-source relational database management system.](/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-postgresql-on-northflank)
- [Access a database: Securely access your database locally or make it available online.](/v1/application/databases-and-persistence/access-a-database)
- [Backup, restore, and import your data: Create and import backups of your database, or restore from an existing backup.](/v1/application/databases-and-persistence/backup-restore-and-import-data)
- [Use a database with your applications: Securely access your database in your project's applications and services.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)
