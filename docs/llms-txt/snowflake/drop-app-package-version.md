# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/native-apps/drop-app-package-version.md

# Dropping an existing version of an app in an application package

## Prerequisites

* You must have an existing connection in your `config.toml` file.
* You must have a `snowflake.yml` file in your Snowflake Native App project.

## How to drop a version definition of an app

The [snow app version drop](../command-reference/native-apps-commands/version/app-version-drop.md) drops the specified app version of an application package, if it exists, and is not referenced by a release directive. If you want to drop a version referenced by a release directive, you must first set that release directive to a different version. This command uses the resolved project definition to determine the name of the application package version to drop.

This command does not allow dropping patches, because Snowflake does not currently support that functionality for a Snowflake Native App.

To drop a version of an existing application package, do the following:

1. [Create a connection](../connecting/connect.md), if necessary.
2. Set the release directive to a different version, if not already done.
3. Execute the `snow app version drop` command from within your project, as shown:

   ```snowcli
   snow app version drop v1 --connection="dev"
   ```

   ```output
   Version v1 of application package my_app_pkg dropped successfully.
   Version drop is now complete.
   ```

> **Note:**
>
> If the version of the application is replicated to other regions, the version won’t be dropped until the next replication is complete.
>
> For information about updating the replication schedule, see
> [Set the refresh schedule for a listing](../../../collaboration/provider-listings-auto-fulfillment-configure-cron-refresh-schedule.md).
>
> To start replication manually, use the [SYSTEM$TRIGGER_LISTING_REFRESH](../../../sql-reference/functions/system_trigger_listing_refresh.md) system function.

For more information about dropping a version of an application package, see the [snow app version drop](../command-reference/native-apps-commands/version/app-version-drop.md) command.
