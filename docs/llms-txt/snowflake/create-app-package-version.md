# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/native-apps/create-app-package-version.md

# Creating an application package with a version (or patch)

## Prerequisites

* You must have an existing connection in your `config.toml` file.
* You must have a `snowflake.yml` file in your native app project.

## How to create an application package with a version (or patch)

The [snow app version create](../command-reference/native-apps-commands/version/app-version-create.md) command brings all the different code files together, creates an application package, uploads code to a Snowflake stage in this application package, and creates a version for that application package. If a version already exists, it adds a custom or an auto-incremented patch to it. This command uses the values specified in your resolved project definition to determine the stage to which it upload files, which files to upload, and the name of the application package to create.

To create an application package and create a version for it, do the following:

1. [Create a connection](../connecting/connect.md), if necessary.
2. Make relevant changes to your code files, including `snowflake.yml`, `manifest.yml`, addition any setup scripts and extension code files.
3. Execute the `snow app version create` command from within your project, similar to the following:

   ```snowcli
   snow app version create V1 --connection="dev"
   ```

   ```output
   Version V1 created for application package my_app_pkg.
   Version create is now complete.
   ```

> This command creates a version **V1** and a default patch **0** for application package `my_app_pkg`.

For more information about adding a version definition to an application package, see the [snow app version create](../command-reference/native-apps-commands/version/app-version-create.md) command.
