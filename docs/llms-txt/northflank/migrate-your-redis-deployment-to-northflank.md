# Source: https://northflank.com/docs/v1/application/databases-and-persistence/migrate-data-to-northflank/migrate-your-redis-deployment-to-northflank.md

# Migrate your Redis® deployment to Northflank

You can import your existing Redis®* data to Northflank either as a snapshot of the database or by using live replication to transfer existing and new keys to your Northflank Redis addon.

You should first [create a Northflank Redis addon](https://app.northflank.com/s/project/create/addon) to import to.

> [!note] 
> There is currently an issue with RIOT which means URI handling is not working. Please specify the host, port, and password (and username if required) separately when running commands.

## Import a snapshot using RIOT

You can import your current Redis instance's keys and values using [RIOT](https://developer.redis.com/riot/). Download and install the tool on your local machine, or on the server with your existing Redis instance.

It is recommended that you make both the source Redis instance and the Northflank Redis addon [publicly accessible](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-redis-on-northflank#access-redis) over the internet. Alternatively, you can [forward the Northflank addon](https://northflank.com/docs/v1/api/forwarding) to your local machine or existing Redis deployment and use the non-external command to connect securely.

The exact command you will need to run depends on your existing Redis provider and your Redis usage. You may need to configure [reader options](https://developer.redis.com/riot/#_file_export_reader_options) if you store a lot of keys, or big sets.

### From managed service to Northflank

You can migrate from an existing service provider using the connection details for your existing Redis instance, and the connection details for your Northflank Redis addon, found on the connection details page.

```shell
## without TLS (forwarded Northflank addon)
riot -h <SOURCE_REDIS_HOST> -p <SOURCE_REDIS_PORT> -a <SOURCE_REDIS_PASSWORD> replicate -h <NORTHFLANK_REDIS_HOST> -p <NORTHFLANK_REDIS_PORT> -a <NORTHFLANK_REDIS_PASSWORD>

## with TLS enabled on Redis source and Northflank addon
riot -h <SOURCE_REDIS_HOST> -p <SOURCE_REDIS_PORT> -a <SOURCE_REDIS_PASSWORD> --tls --tls-verify=NONE replicate -h <NORTHFLANK_REDIS_HOST> -p <NORTHFLANK_REDIS_PORT> -a <NORTHFLANK_REDIS_PASSWORD> --tls --tls-verify=NONE
```

If you are not using the default user on your source Redis instance, you can also specify the user by including the `--user` flag.

### From local machine to Northflank

You can migrate from your local machine, or via the terminal on your server, by specifying the hostname, port, and password for the local instance, and the connection details for your Northflank Redis addon as the target, found on the connection details page.

```shell
riot -h <LOCAL_REDIS_HOST> -p <LOCAL_REDIS_PORT> -a <LOCAL_REDIS_PASSWORD> -a  replicate -h <NORTHFLANK_REDIS_HOST> -p <NORTHFLANK_REDIS_PORT> -a <NORTHFLANK_REDIS_PASSWORD> --tls --tls-verify=NONE
```

If you are not using the default user on your local Redis instance, you can also specify the user by including the `--user` flag.

RIOT should import all keys and values from the source Redis instance to your Northflank addon, you can double-check that the import has run as you expected it to by [accessing the addon](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-redis-on-northflank#access-redis) and comparing keys and values.

## Live replication using RIOT

You can configure live replication between your existing and Northflank Redis instances using [RIOT's live replication mode](https://developer.redis.com/explore/riot).

This method will allow you to seamlessly migrate a Redis instance, as new keys created on the source will be transferred to your new Northflank Redis instance. This method uses pub/sub which means delivery is not guaranteed, and it may also fail if trying to copy big sets repeatedly. You should evaluate your Redis store for big sets before using these methods to migrate.

Before using live replication you will need to enable keyspace notifications in each Redis instance. You can do this by logging into each instance using redis-cli and entering the command `CONFIG SET notify-keyspace-events KA`.

You can use the same commands as to [import a snapshot](#import-a-snapshot-using-riot-redis), adding the required mode flag at the end of the command:

### Live only `--mode liveonly`

Live only mode will only replicate keys added or updated in your source Redis instance after the process has started, and not keys that currently exist in your source Redis.

### Initial and live `--mode live`

Live mode will copy your current keys from your source Redis instance, as well as replicate any new keys and updates to keys from your source Redis while the process is running.

### Verification and migration

You can double-check that replication is working as expected by [accessing the addon](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-redis-on-northflank#access-redis) manually, or running RIOT's [compare command](https://developer.redis.com/explore/riot/#step-5-verification).

You can now configure your applications and infrastructure to use the Northflank Redis addon. Once your changes are live, you can terminate the RIOT replicate process and shut down your original source Redis instance.

## Next steps

- [Deploy Redis® on Northflank: Redis implements a distributed, in-memory key-value database with optional durability.](/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-redis-on-northflank)
- [Access a database: Securely access your database locally or make it available online.](/v1/application/databases-and-persistence/access-a-database)
- [Backup, restore, and import your data: Create and import backups of your database, or restore from an existing backup.](/v1/application/databases-and-persistence/backup-restore-and-import-data)
- [Use a database with your applications: Securely access your database in your project's applications and services.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)

* Redis is a registered trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Northflank is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Northflank.
