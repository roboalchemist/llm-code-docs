# Source: https://northflank.com/docs/v1/application/databases-and-persistence/migrate-data-to-northflank/migrate-your-rabbitmq-deployment-to-northflank.md

# Migrate your RabbitMQ deployment to Northflank

You can import your existing RabbitMQ instance's definitions to Northflank, so you can begin running your RabbitMQ instance on Northflank with the same configuration.

You should first [create a Northflank RabbitMQ addon](https://app.northflank.com/s/project/create/addon) to import to, and [connect to it](https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-rabbitmq-on-northflank#connect-to-rabbitmq) with your preferred administration tool. If you require your Northflank deployment to remain private you can [forward it](https://northflank.com/docs/v1/api/forwarding) to your local machine and use the non-external endpoints and commands to connect.

## Permissions

The user you use to import and export from RabbitMQ instances should have the [administrator tag](https://www.rabbitmq.com/access-control.html#user-tags) tag (enabled by the management plugin).

Your RabbitMQ instances require the [RabbitMQ management plugin](https://www.rabbitmq.com/management.html) to be enabled, this is enabled by default for your Northflank addon.

## Import definitions using the RabbitMQ web interface

You can export and import definitions using the RabbitMQ web interface (`MANAGEMENT_ENDPOINT` in your Northflank addon's connection details page).

![The RabbitMQ management web interface showing definition export and import](https://assets.northflank.com/documentation/v1/application/databases-and-persistence/migrate-your-data-to-northflank/migrate-your-rabbitmq-deployment-to-northflank/rabbitmq-definitions-gui.jpg)

### Export definitions

From the overview page expand the export definitions section. You can use the generated file name, or enter your own. Choose to export definitions for all virtual hosts, or export definitions from a specific virtual host and click download broker definitions to save the `.json` file.

### Import definitions

From the overview page expand the import definitions section. Select the `.json` file containing your definitions, and specify which virtual host to export the definitions to, or all, and click upload broker definitions.

You can now publish and consume messages using the same configuration as your existing RabbitMQ service, using the endpoints for the Northflank addon.

## Import definitions using the CLI

You can use the [rabbitmqadmin](https://www.rabbitmq.com/management-cli.html) command-line tool to export and import definitions for your RabbitMQ instances, you must [install RabbitMQ](https://www.rabbitmq.com/download.html) locally to use `rabbitmqadmin` commands.

### Export definitions

You can export your current RabbitMQ instance's definitions (users, vhosts, queues, exchanges, bindings, runtime parameters) using the following command:

```shell
rabbitmqadmin --host=<SOURCE_RABBITMQ_HOST> --port=<SOURCE_RABBITMQ_HOST> -u <SOURCE_ADMIN_USERNAME> -p <SOURCE_ADMIN_PASSWORD> export <FILE_PATH>/<FILE_NAME>.json
```

This will export your current definitions to a file in your working directory (or to a specified path). You may need to use [other options](https://www.rabbitmq.com/management-cli.html) in your command, such as `-s` if your RabbitMQ instance requires TLS to connect.

### Import definitions

You can import your definitions to your Northflank addon using the following command, with the definitions file in the working directory or by providing the full path. The necessary parameters can be found on your addon's connection details page.

```shell
rabbitmqadmin --host=<NORTHFLANK_RABBITMQ_HOST> --port=<NORTHFLANK_RABBITMQ_HOST> -s -u <ADMIN_USERNAME> -p <ADMIN_PASSWORD> import_definitions <FILE_PATH>/<FILE_NAME>.json
```

You can now publish and consume messages using the same configuration as your existing RabbitMQ service, using the endpoints for the Northflank addon.

## Next steps

- [Deploy RabbitMQ on Northflank: RabbitMQ is a lightweight, easy to deploy, open-source message broker that supports multiple messaging protocols.](/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-rabbitmq-on-northflank)
- [Access a database: Securely access your database locally or make it available online.](/v1/application/databases-and-persistence/access-a-database)
- [Backup, restore, and import your data: Create and import backups of your database, or restore from an existing backup.](/v1/application/databases-and-persistence/backup-restore-and-import-data)
- [Use a database with your applications: Securely access your database in your project's applications and services.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)
