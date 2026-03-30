# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/native-apps/drop-objects.md

# Dropping Snowflake Native App objects

## Prerequisites

* You must have an existing connection in your `config.toml` file.
* You must have a `snowflake.yml` file in your Snowflake Native App project.

## How to drop Snowflake Native App application packages and application objects

The `snow app teardown` drops both the application object and the application package defined in the resolved project definition.
This command succeeds even if one or both of these objects do not exist.

1. [Create a connection](../connecting/connect.md), if necessary.
2. Execute the `snow app teardown` command from within your project, similar to the following:

   > ```snowcli
   > snow app teardown --connection="dev"
   > ```
   >
   > When successful, the command returns the following message:
   >
   > ```output
   > Teardown is now complete.
   > ```

> **Note:**
>
> When dropping applications that own objects outside of the application object, such as compute pools, Snowflake CLI shows a list of these dependent objects and asks whether you would like to drop them in addition to the application object and package.
>
> > You can choose this option non-interactively by passing in the `--cascade` option.

If Snowflake CLI is unable to drop the application, it does note drop the application package either.
For more information about dropping Snowflake Native App objects, see the [snow app teardown](../command-reference/native-apps-commands/teardown-app.md) command.
