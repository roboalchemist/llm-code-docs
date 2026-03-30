# Source: https://northflank.com/docs/v1/application/databases-and-persistence/migrate-data-to-northflank/migrate-your-mongodb-database-to-northflank.md

# Migrate your MongoDB® database to Northflank

You can import your existing MongoDB® database to Northflank by creating and uploading a dump of your database, or providing a connection string to your existing database.

Imports will be more reliable if the database you are importing to is the same, or a newer, version of MongoDB as the source database you are exporting from.

> [!warning] 
> Both methods of importing a database will erase all existing user databases in the Northflank addon, if there are any.

You should first [create a Northflank MongoDB addon](https://app.northflank.com/s/project/create/addon) to import to, and [connect to it](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-mongodb-on-northflank#connect-to-mongodb) with your preferred administration tool. If you require your Northflank deployment to remain private you can [forward it](https://northflank.com/docs/v1/api/forwarding) to your local machine and use the non-external endpoints and commands to connect.

## Permissions

To run mongodump you must have `find` [privileges](https://www.mongodb.com/docs/database-tools/mongodump/#required-access) on the databases you want to back up, or the `backup` role.

## Import from dump

Importing from a dump of a database will erase all existing user databases on the target MongoDB addon, and your dump will be imported as the default database on the Northflank addon (specified in your addon’s connection details as `DATABASE`).

To start, you will need to generate a dump of your existing database using [mongodump](https://www.mongodb.com/docs/database-tools/mongodump/#mongodb-binary-bin.mongodump).

### Create a dump using mongodump

You must run mongodump from the system command line, not the mongo shell. You must have the [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/installation/installation/) installed.

You can use either a [connection string](https://www.mongodb.com/docs/manual/reference/connection-string/) or provide your connection details as parameters to the mongodump command. The exact connection string or details you use to connect will depend on your provider or MongoDB configuration. The following commands create a compressed archive file in the working directory where the command is run, you can omit the `--gzip` flag and `.gz` extension to produce an uncompressed file.

#### With connection string

```shell
## Standalone
mongodump --uri="mongodb://<USER><:PASSWORD>@<HOST><:PORT></DATABASE_TO_EXPORT>?authSource=<AUTH_DB>" --gzip --archive=<DUMP_NAME>.archive.gz

## Replica set using DNS seed list
mongodump --uri="mongodb+srv://<USER><:PASSWORD>@<HOST><:PORT></DATABASE_TO_EXPORT>?replicaSet=<REPLICA_SET>&authSource=<AUTH_DB>" --gzip --archive=<DUMP_NAME>.archive.gz
```

#### With parameters

```shell
mongodump --host=<HOST> --port=<PORT> --username=<USER> --authenticationDatabase=<AUTH_DB> --db=<DATABASE_TO_EXPORT> --gzip --archive=<DUMP_NAME>.archive.gz
```

See the [mongodump](https://www.mongodb.com/docs/database-tools/mongodump/#options) documentation for more information.

### Import dump to Northflank

Navigate to your MongoDB addon’s backups page and click import backup. Enter a recognisable name and select either upload, if your dump is stored locally, or URL if your dump is hosted online and accessible. You can upload the dump as plain text, or as a gzipped file (`.gz`).

After selecting your file, or entering the URL, click upload import. All backups stored on Northflank are encrypted at rest, to keep your data private and secure.

Select the uploaded import from the backups list and click restore  to begin importing the database to your Northflank MongoDB addon. All user data in the existing MongoDB database on Northflank will be erased before importing the contents of the dump file.

You can click on a restore listed in a backup to view the logs of the restoration, and you will be able to see in the backups list and the list of restores whether or not the restoration was successful.

You can now double-check that the import has run as you expected it to by accessing the addon via the mongo shell or a GUI tool.

> [!note] 
> Northflank will copy your collections to the default Northflank-generated database when importing from a dump. You can find the name of the default database in your Northflank addon's connection details as `DATABASE`.

## Import from connection string

You can import a database from your source MongoDB instance by [providing a connection string](https://www.mongodb.com/docs/manual/reference/connection-string/). Navigate to the backups page of your Northflank MongoDB addon and select import backup.

Enter a recognisable name and select connection string as the import method, and provide the connection string for your source database, which must be publicly available. The connection string will take the format:

```shell
## Standalone
mongodb://<USER><:PASSWORD>@<HOST><:PORT>/<DATABASE>

## Replica set using DNS seed list
mongodb+srv://<USER><:PASSWORD>@<HOST><:PORT></DATABASE>?replicaSet=<REPLICA_SET>
```

When you start the import, Northflank will create a dump of the specified database. After importing, select the new import from the backups list and click restore  to begin importing the database to your Northflank MongoDB addon. Your database will be imported to the default Northflank-generated database, the database name can be found in your addon's connection details as `DATABASE`.

You can now double-check that the import has run as you expected it to by accessing the addon via a GUI, or [forward it using the Northflank CLI](https://northflank.com/docs/v1/api/forwarding) to connect locally. If you need to make any changes you can connect to your Northflank MongoDB addon using the admin URI connection strings, or by using the `ADMIN_USERNAME` and `ADMIN_PASSWORD` login details.

## Next steps

- [Deploy MongoDB® on Northflank: MongoDB is a document-oriented database program that uses JSON-like documents with schema.](/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-mongodb-on-northflank)
- [Access a database: Securely access your database locally or make it available online.](/v1/application/databases-and-persistence/access-a-database)
- [Backup, restore, and import your data: Create and import backups of your database, or restore from an existing backup.](/v1/application/databases-and-persistence/backup-restore-and-import-data)
- [Use a database with your applications: Securely access your database in your project's applications and services.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)
