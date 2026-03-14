# Source: https://docs.mage.ai/integrations/databases/SQLite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# SQLite

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

![](https://user-images.githubusercontent.com/78053898/198754399-3b594af0-cf84-41d3-8faf-e1f6e4c5182d.png)

## Add credentials

1. Create a new pipeline or open an existing pipeline.
2. Expand the left side of your screen to view the file browser.
3. Scroll down and click on a file named `io_config.yaml`.
4. Enter the following keys and values under the key named `default` (you can
   have multiple profiles, add it under whichever is relevant to you)

```yaml  theme={"system"}
version: 0.1.1
default:
  sqlite:
    database: /path/to/your/sqlite.db
```

**Notes:**

* `database` should be the absolute path to your SQLite database file
* The database file will be created automatically if it doesn't exist
* Make sure the directory containing the database file has proper write permissions

<br />

## Using SQL block

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader, transformer, or data exporter block.
3. Select `SQL`.
4. Under the `Data provider` dropdown, select `SQLite`.
5. Under the `Profile` dropdown, select `default` (or the profile you added
   credentials underneath).
6. Next to the `Save to schema` label, enter the schema name you want this block
   to save data to.
7. Under the `Write policy` dropdown, select `Replace` or `Append` (please see
   [SQL blocks guide](/guides/blocks/sql-blocks) for more
   information on write policies).
8. Enter in this test query: `SELECT 1`.
9. Run the block.

### Using raw SQL

You can also use raw SQL with SQLite by enabling the "Use raw SQL" option in the SQL block configuration. This allows you to write complete SQL statements including `CREATE TABLE`, `INSERT`, `UPDATE`, and `DELETE` statements.

**Example raw SQL:**

```sql  theme={"system"}
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

INSERT INTO users (name, email) VALUES 
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com');

SELECT * FROM users;
```

**Note:** When using raw SQL, you're responsible for writing the complete SQL statements. Mage won't automatically create tables or handle data insertion.

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
from mage_ai.io.sqlite import SQLite
from os import path
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_sqlite(**kwargs) -> DataFrame:
    query = 'SELECT 1'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with SQLite.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        return loader.load(query)
```

5. Run the block.

### Export a dataframe

Here is an example code snippet to export a dataframe to SQLite:

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.sqlite import SQLite
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_sqlite(df: DataFrame, **kwargs) -> None:
    schema_name = 'your_schema_name'  # Specify the name of the schema to export data to
    table_name = 'your_table_name'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with SQLite.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
            drop_table_on_replace=False,   # Whether to drop the table when "if_exists" param is set to "replace"
        )

```

<br />

### Custom types

To overwrite a column type when running a python export block, simply specify the column name and type in the `overwrite_types` dict in data exporter config

Here is an example code snippet:

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.sqlite import SQLite
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_sqlite(df: DataFrame, **kwargs) -> None:
    schema_name = 'your_schema_name'  # Specify the name of the schema to export data to
    table_name = 'your_table_name'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    overwrite_types = {'column_name': 'TEXT'}

    with SQLite.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
            overwrite_types=overwrite_types,
        )

```

### Method arguments

| Field name               | Description                                                                                                                                       | Example values                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| auto\_clean\_name        | Whether to automatically clean the column name (replace the empty space with underscore, avoid using number as the prefix of the column name)     | True/False (default: True)                     |
| case\_sensitive          | Whether to support case sensitive columns                                                                                                         | True/False (default: False)                    |
| drop\_table\_on\_replace | Whether to drop the table when "if\_exists" param is set to "replace".                                                                            | True/False (default: False)                    |
| if\_exists               | Specify resolution policy if table name already exists                                                                                            | "fail"/"replace"/"append" (default: "replace") |
| overwrite\_types         | Overwrite the column types                                                                                                                        | `{'column1': 'INTEGER', 'column2': 'TEXT'}`    |
| unique\_conflict\_method | How to handle the conflict on unique constraints. Use 'UPDATE' for UPSERT (update existing rows, insert new ones) or 'IGNORE' to skip duplicates. | 'UPDATE' or 'IGNORE' (default: None)           |
| unique\_constraints      | The unique constraints of the table. Used with unique\_conflict\_method for UPSERT operations.                                                    | \['col1', 'col2'] (default: None)              |

**Example: Using UPSERT (UPDATE or INSERT)**

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.sqlite import SQLite
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_sqlite(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to SQLite with UPSERT support.
    Specify your configuration settings in 'io_config.yaml'.
    """
    schema_name = 'your_schema_name'
    table_name = 'your_table_name'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with SQLite.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,
            if_exists='append',  # Use 'append' with UPSERT
            unique_constraints=['user_id', 'email'],  # Columns that form unique constraint
            unique_conflict_method='UPDATE',  # Update existing rows, insert new ones
        )
```

<br />

## SQLite-specific considerations

### Database file location

* SQLite databases are stored as single files on disk
* Ensure the file path is accessible and has proper read/write permissions
* Use absolute paths to avoid issues with working directory changes

### Schema support

* SQLite doesn't have true schema support like PostgreSQL
* The "schema" parameter in Mage is used for table naming conventions
* Tables are created in the main database without schema prefixes

### Data types

* SQLite uses dynamic typing (type affinity)
* Common types: `INTEGER`, `REAL`, `TEXT`, `BLOB`, `NULL`
* Mage will map pandas data types to appropriate SQLite types

### Performance tips

* SQLite performs best with smaller datasets (\< 1GB)
* Consider using `PRAGMA` statements for performance tuning
* Use transactions for bulk operations


Built with [Mintlify](https://mintlify.com).