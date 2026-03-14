# Source: https://docs.snowflake.com/en/migrations/guides/teradata.md

# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/user-guide/snowconvert/command-line-interface/teradata.md

# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/considerations/teradata.md

# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/supported-languages/teradata.md

# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/code-extraction/teradata.md

# SnowConvert AI - Teradata

The first step for migration is getting the code that you need to migrate. There are many ways to extract the code from your database. However, we recommend using the extraction scripts provided by Snowflake.

All the source code for these scripts is open source and is available on [GitHub](https://github.com/Snowflake-Labs/SC.DDLExportScripts/).

## Prerequisites

* Access to a server with a Teradata database.
* Permission to run shell scripts with access to the server.
* Teradata utilities like`bteq / tpt`.

## Installing the scripts

Go to <https://github.com/Snowflake-Labs/SC.DDLExportScripts/>.

From the Code option, select the drop-down and use the **Download ZIP** option to download the code.

Decompress the ZIP file. The code for Teradata should be under the Teradata folder

Follow the [Usage instructions](https://github.com/Snowflake-Labs/SC.DDLExportScripts/blob/main/Teradata/README.md) to modify the files and run them on your system.

### Package the results

When the script is done, the output folder will contain all the DDLs for the migration. You can then compress this folder to use it with [SnowConvert AI](../../../overview.md).

E.g. run:

```none
zip -r output.zip ./output
```
