# Source: https://docs.mage.ai/integrations/databases/MicrosoftSQLServer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft SQL Server

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

![](https://www.commvault.com/wp-content/uploads/2019/08/sql-server_logo.jpg)

## Add credentials

1. Create a new pipeline or open an existing pipeline.
2. Expand the left side of your screen to view the file browser.
3. Scroll down and click on a file named `io_config.yaml`.
4. Enter the following keys and values under the key named `default` (you can
   have multiple profiles, add it under whichever is relevant to you)

```yaml  theme={"system"}
version: 0.1.1
default:
  MSSQL_DATABASE: database
  MSSQL_SCHEMA: schema
  MSSQL_DRIVER: "ODBC Driver 18 for SQL Server"
  MSSQL_HOST: host
  MSSQL_PASSWORD: password
  MSSQL_PORT: 1433
  MSSQL_USER: SA

  # (Optional) SSH tunnel config
  MSSQL_CONNECTION_METHOD: direct
  MSSQL_SSH_HOST:
  MSSQL_SSH_PORT: 22
  MSSQL_SSH_USERNAME:
  MSSQL_SSH_PASSWORD:
  MSSQL_SSH_PKEY:
```

### SSH tunneling

<Note>
  SSH tunneling is a Mage Pro only feature.
</Note>

<ProOnly source="mssql" />

If you want to connect to SQL Server with SSH tunnel, update the value of `MSSQL_CONNECTION_METHOD` to `ssh_tunnel`, and enter the values for keys with prefix `MSSQL_SSH`.

| Key                  | Description                                                                                                                                                  | Sample value           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| `MSSQL_SSH_HOST`     | The host of the intermediate bastion server.                                                                                                                 | `123.45.67.89`         |
| `MSSQL_SSH_PORT`     | The port of the intermediate bastion server. Default value: 22                                                                                               | `22`                   |
| `MSSQL_SSH_USERNAME` | The username used to connect to the bastion server.                                                                                                          | `username`             |
| `MSSQL_SSH_PASSWORD` | (Optional) The password used to connect to the bastion server. It should be set if you authenticate with the bastion server with password.                   | `password`             |
| `MSSQL_SSH_PKEY`     | (Optional) The path to the private key used to connect to the bastion server. It should be set if you authenticate with the bastion server with private key. | `/path/to/private/key` |

<Note>
  When using SSH tunnel, the `fast_execute` option will automatically be disabled to ensure reliable connections through the tunnel.
</Note>

## Dependencies

To connect to the Microsoft SQL Server, you'll need to make sure the driver is installed.
By default, ODBC Driver 18 is installed in the docker image.
If you want to use other ODBC Driver versions, you'll need to build a custom docker image (use Mage image as the base image) and install the drivers.
Here is the doc for installing ODBC drivers for SQL Server: [https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server)

***

## Using SQL block

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader, transformer, or data exporter block.
3. Select `SQL`.
4. Under the `Data provider`/`Connection` dropdown, select `Microsoft SQL Server`.
5. Under the `Profile` dropdown, select `default` (or the profile you added
   credentials underneath).
6. Enter the schema and optional table name of the table to write to.
7. Under the `Write policy` dropdown, select `Replace` or `Append` (please see
   [SQL blocks guide](/guides/blocks/sql-blocks) for more information on write policies).
8. Enter in this test query: `SELECT 1`.
9. Run the block.

<br />

## Using Python block

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader, transformer, or data exporter block (the code snippet
   below is for a data loader).
3. Select `Generic (no template)`.
4. Enter this code snippet (note: change the `config_profile` from `default` if
   you have a different profile):

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.mssql import MSSQL
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_mssql(*args, **kwargs):
    """
    Template for loading data from a MSSQL database.
    Specify your configuration settings in 'io_config.yaml'.
    Set the following in your io_config:

    Docs: /integrations/databases/MicrosoftSQLServer
    """
    query = 'Your MSSQL query'  # Specify your SQL query here
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with MSSQL.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        return loader.load(query)
```

5. Run the block.

### Export a dataframe

Here is an example code snippet to export a dataframe to MSSQL:

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.mssql import MSSQL
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_mssql(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a MSSQL database.
    Specify your configuration settings in 'io_config.yaml'.
    Set the following in your io_config:

    Docs: /integrations/databases/MicrosoftSQLServer
    """
    schema_name = 'dbo'  # Specify the name of the schema to export data to
    table_name = 'your_table_name'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with MSSQL.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
            fast_execute=True,  # Use fast_executemany option to speed up bulk inserting rows
            unique_conflict_method='UPDATE',  # Specify method to resolve row conflicts
            unique_constraints=['col'],
        )
```

<br />

6. Custom types

To overwrite a column type when running a python export block, simply specify the column name and type in the `overwrite_types` dict in data exporter config

Here is an example code snippet:

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.mssql import MSSQL
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_mssql(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a MSSQL database.
    Specify your configuration settings in 'io_config.yaml'.
    Set the following in your io_config:

    Docs: /integrations/databases/MicrosoftSQLServer
    """
    schema_name = 'dbo'  # Specify the name of the schema to export data to
    table_name = 'your_table_name'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    overwrite_types = {'column_name': 'VARCHAR(255)'}

    with MSSQL.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
            overwrite_types=overwrite_types,
        )
```

<br />

## Troubleshooting errors

### `error: ODBC SQL type -155 is not yet supported.`

<Check>
  *“I changed the datetime with timezone data type to a datetime and it starting working”*
</Check>

* [Windy Martin](https://mageai.slack.com/archives/C068SHY6YG6/p1705874712639659?thread_ts=1705668895.141169\&cid=C068SHY6YG6)


Built with [Mintlify](https://mintlify.com).