# Source: https://docs.upsun.com/learn/tutorials/exporting.md

# Exporting data

As an Upsun user, your code and data belong to you.
At any time, you can download your site's data for local development, to back up your data, or to change provider.

## Before you begin

You need:

- [Git](https://git-scm.com/downloads)
- An Upsun account
- Code in your project
- Optional: the [Upsun CLI](https://docs.upsun.com/administration/cli.md)

## 1. Download your app's code

Your app's code is maintained through the Git version control system.

To download your entire app's code history:

 - Retrieve the project you want to back up by running the following command:

```bash {}
upsun get <PROJECT_ID>
```

 - In the [Console](https://console.upsun.com/), open your project and click **Code **.

 - Click **Git**.

 - To copy the command, click ** Copy**.
The command is similar to the following:

```text {}
git clone abcdefgh1234567@git.eu.upsun.com:abcdefgh1234567.git project-name
```

## 2. Download your files

Some files might not be stored in Git,
such as data your app writes [in mounts](https://docs.upsun.com/create-apps/image-properties/mounts.md).

You can download your files [using the CLI](https://docs.upsun.com/development/file-transfer.md#transfer-files-using-the-cli) or [using SSH](https://docs.upsun.com/development/file-transfer.md#transfer-files-using-an-ssh-client).

## 3. Download data from services

The mechanism for downloading from each service (such as your database) varies.

For services designed to hold non-persistent data, such as [Redis](https://docs.upsun.com/add-services/redis.md) or [Solr](https://docs.upsun.com/add-services/solr.md),
it's generally not necessary to download data as it can be rebuilt from the primary data store.

For services designed to hold persistent data, see each service's page for instructions:

- [MySQL](https://docs.upsun.com/add-services/mysql.md#exporting-data)
- [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md#exporting-data)
- [MongoDB](https://docs.upsun.com/add-services/mongodb.md#exporting-data)
- [InfluxDB](https://docs.upsun.com/add-services/influxdb.md#export-data)

## 4. Get environment variables

Environment variables can contain critical information such as tokens or additional configuration options for your app.

Environment variables can have different prefixes:

- Variables beginning with `env:` are exposed [as Unix environment variables](https://docs.upsun.com/development/variables.md#top-level-environment-variables).
- Variables beginning with `php:` are interpreted [as `php.ini` directives](https://docs.upsun.com/development/variables.md#php-specific-variables).

All other variables are [part of `$PLATFORM_VARIABLES`](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

To back up your environment variables:

Note that you can also get all the environment variable values by running the following command:

```bash {}
upsun ssh -- env
```

 - Store the data somewhere secure on your computer.

 - In the [Console](https://console.upsun.com/), open your project and click **Settings**.
 - Click **Project Settings **.
 - Click **Variables** and access your variable’s values and settings.
 - Store the data somewhere secure on your computer.

Note that in the Console, you can’t access the value of variables that have been [marked as sensitive](https://docs.upsun.com/development/variables/set-variables.md#variable-options).
Use the CLI to retrieve these values.

## What's next

- Migrate data from elsewhere [into Upsun](https://docs.upsun.com/learn/tutorials/migrating.md).
- Migrate to [another region](https://docs.upsun.com/projects/region-migration.md).
- To use data from an environment locally, export your data and set up your [local development environment](https://docs.upsun.com/development/local.md).

