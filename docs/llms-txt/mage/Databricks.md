# Source: https://docs.mage.ai/integrations/databases/Databricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Databricks

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

<ProOnly source="databricks" />

## Add credentials

1. Create a new pipeline or open an existing pipeline.
2. Expand the left side of your screen to view the file browser.
3. Scroll down and click on a file named `io_config.yaml`.
4. Enter the following keys and values under the key named `default` (you can
   have multiple profiles, add it under whichever is relevant to you)

```yaml  theme={"system"}
version: 0.1.1
default:
  DATABRICKS_ACCESS_TOKEN: access_token
  DATABRICKS_DATABASE: database  # Databricks Catalog
  DATABRICKS_HOST: dbc-123456-abcd.cloud.databricks.com
  DATABRICKS_HTTP_PATH: "/sql/1.0/warehouses/abcd1234"
  DATABRICKS_SCHEMA: schema
```

## Using SQL Block with Databricks

Follow these steps to use a **SQL block** connected to **Databricks** in your pipeline.

1. **Create or open a pipeline**\
   Create a new pipeline or open an existing one.

2. **Add a block**\
   Add a **Data loader**, **Transformer**, **Data exporter**, or **Custom** block.

3. **Select block type**\
   Set the block type to `SQL`.

4. **Configure the data provider**\
   In the `Data provider` dropdown, select `Databricks`.

5. **Choose a profile**\
   In the `Profile` dropdown, select `default` (or the profile you configured your Databricks credentials under).

6. **Configure output saving (optional)**\
   By default, the SQL block saves query results to a table in your Databricks database.

   * **Schema** (optional): Enter the schema where the block’s output should be saved, default to the schema in `io_config.yaml`.
   * **Table** (optional): Enter the table where the block’s output should be saved, default table is generated based on block uuid.
   * **Write policy**: Choose either `Replace` or `Append`. See the [SQL blocks guide](/guides/blocks/sql-blocks) for more details on write policies.
   * If you **don’t want to save results** to an intermediate table, enable the **Use raw SQL** option. See the [Raw SQL documentation](/guides/blocks/sql-blocks#using-raw-sql) for more information.

7. **Enter a test query**\
   Add a simple test query to confirm the connection works:
   ```
   SELECT 1
   ```

8. **Run the block**\
   Click **Run** to execute the query and verify the block works as expected.

<br />

## Using Python block

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader, transformer, or data exporter block (the code snippet
   below is for a data loader).
3. Select the `Data lakes -> Databricks SQL` template or `Generic (no template)`.
4. Enter this code snippet (note: change the `config_profile` from `default` if
   you have a different profile):

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.databricks_sql import DatabricksSQL
from os import path
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data_from_databricks(*args, **kwargs):
    """
    Template for loading data from Databricks with SQL.
    Specify your configuration settings in 'io_config.yaml'.
    """
    query = 'SELECT 1'  # Specify your SQL query here
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with DatabricksSQL.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        return loader.load(query)
```

5. Run the block.

### Export a dataframe

Here is an example code snippet to export a dataframe to Databricks:

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.databricks_sql import DatabricksSQL
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_databricks(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to Databricks.
    Specify your configuration settings in 'io_config.yaml'.
    """
    schema_name = 'your_schema_name'  # Specify the name of the schema to export data to
    table_name = 'your_table_name'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with DatabricksSQL.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name=schema_name,
            table_name=table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )
```

<br />

### Method arguments

| Field name               | Description                                                                                                                                   | Example values                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| allow\_reserved\_words   | Whether to allow using reserved words as column names.                                                                                        | True/False (default: False)                    |
| auto\_clean\_name        | Whether to automatically clean the column name (replace the empty space with underscore, avoid using number as the prefix of the column name) | True/False (default: True)                     |
| case\_sensitive          | Whether to support case sensitive columns                                                                                                     | True/False (default: False)                    |
| drop\_table\_on\_replace | Whether to drop the table when "if\_exists" param is set to "replace".                                                                        | True/False (default: False)                    |
| if\_exists               | Specify resolution policy if table name already exists                                                                                        | "fail"/"replace"/"append" (default: "replace") |

<br />


Built with [Mintlify](https://mintlify.com).