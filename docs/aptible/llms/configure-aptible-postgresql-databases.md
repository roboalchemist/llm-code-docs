# Source: https://www.aptible.com/docs/how-to-guides/database-guides/configure-aptible-postgresql-databases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to configure Aptible PostgreSQL Databases

> Learn how to configure PostgreSQL Databases on Aptible

## Overview

This guide will walk you through the steps of changing, applying, and checking settings, in addition to configuring access control, for an [Aptible PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql) database.

## Changing Settings

As described in Aptible’s [PostgreSQL Configuration](/core-concepts/managed-databases/supported-databases/postgresql#configuration) documentation, the [`ALTER SYSTEM`](https://www.postgresql.org/docs/current/sql-altersystem.html)command can be used to make persistent, global changes to [`pg_settings`](https://www.postgresql.org/docs/current/view-pg-settings.html).

* `ALTER SYSTEM SET` changes a setting to a specified value. For example, `ALTER SYSTEM SET max_connections = 500;`.

* `ALTER SYSTEM RESET` resets a setting to the default value set in [`postgresql.conf`](https://github.com/aptible/docker-postgresql/blob/master/templates/etc/postgresql/PG_VERSION/main/postgresql.conf.template) i.e. the Aptible default setting. For example, `ALTER SYSTEM RESET max_connections`.

## Applying Settings

Changes to settings are not necessarily applied immediately. The setting’s `context` determines when the change is applied. The current contexts for settings that can be changed with `ALTER SYSTEM` are:

* `postmaster` - Server settings that cannot be changed after the Database starts. Restarting the Database is required to apply these settings.

* `backend` and `superuser-backend` - Connection settings that cannot be changed after the connection is established. New connections will use the updated settings.

* `sighup` - Server settings that can be changed at runtime. The Database’s configuration must be reloaded in order to apply these settings.

* `user` and `superuser` - Session settings that can be changed with `SET` . New sessions will use the updated settings by default and reloading the configuration will apply it to all existing sessions that have not changed the setting.

Any time the Database container restarts including when it crashes or when the [`aptible db:reload`](/reference/aptible-cli/cli-commands/cli-db-reload) or [`aptible db:restart`](/reference/aptible-cli/cli-commands/cli-db-restart) CLI commands are run will apply any pending changes. `aptible db:reload` is recommended as it incurs the least amount of downtime. Restarting the Database is the only way to apply `postmaster` settings. It will also ensure that all `backend` and `superuser-backend` settings are being used by all open connections since restarting the Database will terminate all connections, forcing clients to establish new connections.

For settings that can be changed at runtime, the `pg_reload_conf` function (i.e. running `SELECT pg_reload_conf();`) will apply the changes to the Database and existing sessions. This is required to apply `sighup` settings without restarting the Database. `user` and `superuser` settings don’t require the configuration to be reloaded but, if it isn’t, the changes will only apply to new sessions so it’s recommended in order to ensure all sessions are using the same default configuration.

## Checking Setting Values and Contexts

### Show pg\_settings

The `pg_settings` view contains information on the current settings being used by the Database. The following query selects the relevant columns from `pg_settings` for a single setting:

```js  theme={null}
SELECT name, setting, context, pending_restart
FROM pg_settings
WHERE name = 'max_connections';

```

Note that `setting` is the current value for the session and does not reflect changes that have not yet been applied. The `pending_restart` column indicates if a setting has been changed that cannot be applied until the Database is restarted. Running `SELECT pg_reload_conf();`, will update this column and if it’s `TRUE` (`t`) you know that the Database needs to be restarted.

### Show pending restarts

Using this, you can reload the config and then query if any settings have been changed that require the Database to be restarted.

```js  theme={null}
SELECT name, setting, context, pending_restart
FROM pg_settings
WHERE pending_restart IS TRUE;

```

### Show non-default Settings:

Using this, you can show all non-default settings:

```js  theme={null}
SELECT name, current_setting(name), source, sourcefile, sourceline
FROM pg_settings
WHERE(source <> 'default' OR name = 'server_version') 
AND name NOT IN('config_file', 'data_directory', 'hba_file', 'ident_file');
```

### Show all settings

Using this, you can show all non-default settings:

```js  theme={null}
SHOW ALL;
```

## Configuring Access Control

The [`pg_hba.conf` file](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html) (host-based authentication) controls where the PostgreSQL database can be accessed from and is traditionally the way you would restrict access. However, Aptible PostgreSQL Databases configure [`pg_hba.conf`](https://github.com/aptible/docker-postgresql/blob/master/templates/etc/postgresql/PG_VERSION/main/pg_hba.conf.template) to allow access from any source and it cannot be modified. Instead, access is controlled by the Aptible infrastructure. By default, Databases are only accessible from within the Stack that they run on but they can be exposed to external sources via [Database Endpoints](/core-concepts/managed-databases/connecting-databases/database-endpoints) or [Network Integrations](/core-concepts/integrations/network-integrations).
