# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/supported-languages/sybase-iq.md

# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/code-extraction/sybase-iq.md

# SnowConvert AI - Sybase IQ

The first step for migration is getting the code that you need to migrate. There are many ways to extract the code from your database. However, we recommend using the extraction scripts provided by Snowflake.

All the source code for these scripts is open source and is available on [GitHub](https://github.com/Snowflake-Labs/SC.DDLExportScripts/).

## Prerequisites

* Sybase IQ client utilities installed and accessible, specifically iqunload (or iqunload.bat on Windows).
* Sufficient privileges for the user in the target database to extract DDL.
* Disk space in the output directory for the consolidated SQL and split files.
* A valid Sybase IQ connection string (examples below).

## Installing the scripts

Go to <https://github.com/Snowflake-Labs/SC.DDLExportScripts/>

From the Code option, select the drop-down and use the **Download ZIP** option to download the code.

Decompress the ZIP file. The code for Sybase IQ should be under the “Sybase IQ” folder.

Follow the [Usage instructions](https://github.com/Snowflake-Labs/SC.DDLExportScripts/tree/main/Sybase%20IQ#readme) to modify the files and run them on your system.

Once the script execution finishes, the output folder will contain all the DDLs for the migration.
