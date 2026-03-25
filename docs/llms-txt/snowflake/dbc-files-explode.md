# Source: https://docs.snowflake.com/en/migrations/sma-docs/support/frequently-asked-questions-faq/dbc-files-explode.md

# Snowpark Migration Accelerator: DBC files explode

Before migrating Databricks workloads, you need to complete two steps:

1. Extract the source code from your .dbc files using the explode process
2. Use SnowConvert AI to migrate the extracted source code

To run the explode process, you need Python installed on your computer. We recommend using [Python 3.7](https://www.python.org/downloads/release/python-370/).

## Run explode script

Run [dbcexplode.py](https://repo.bds.mobilize.net/snowflake/qualification-service-desk/-/blob/main/dbcexplode.py) and provide the path to your .dbc file as a command-line argument.

```bash
python dbcexplode.py <dbc_file_path>
```

The script creates a folder in the same directory as the **dbcexplode.py** script. The new folder’s name will be your DBC file’s name followed by **.dbc-exploded**.

This folder will contain a separate folder for each notebook found in the .dbc file. In this example, the .dbc file contains a single notebook named **SanFranciscoFireCallsAnalysis (1).python**.

Inside this folder, you will find separate files for each command from the processed notebook. Each file follows the naming pattern **<notebook_name>-<sequence_number>**. The **<sequence_number>** represents the order in which the commands appear in the notebook. For example, **SanFranciscoFireCallsAnalysis (1)-001.md** represents the first command found in the notebook.

Note: If a notebook code cell contains a magic string, the script will generate a file with a .magic extension.
