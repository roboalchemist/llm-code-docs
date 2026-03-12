# Source: https://docs.snowflake.com/en/sql-reference/sql/create-streamlit.md

# CREATE STREAMLIT

Creates a new Streamlit object in Snowflake or replaces an existing Streamlit
object in the same schema.

See also:
:   [SHOW STREAMLITS](show-streamlits.md), [DESCRIBE STREAMLIT](desc-streamlit.md), [ALTER STREAMLIT](alter-streamlit.md),
    [DROP STREAMLIT](drop-streamlit.md), [UNDROP STREAMLIT](undrop-streamlit.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] STREAMLIT [ IF NOT EXISTS ] <name>
  [ FROM <source_location> ]
  [ MAIN_FILE = '<filename>' ]
  [ QUERY_WAREHOUSE = <warehouse_name> ]
  [ RUNTIME_NAME = '<runtime_name>' ]
  [ COMPUTE_POOL = <compute_pool_name> ]
  [ COMMENT = '<string_literal>' ]
  [ TITLE = '<app_title>' ]
  [ IMPORTS = ( '<stage_path_and_file_name_to_read>' [ , ... ] ) ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = ( <integration_name> [ , ... ] ) ]
  [ SECRETS = ( '<snowflake_secret_name>' = <snowflake_secret> [ , ... ] ) ]
```

**The following syntax is legacy:**

> **Important:**
>
> * ROOT_LOCATION is a legacy parameter and may be deprecated in a future release.
> * For container runtimes, ROOT_LOCATION is not supported.
> * For Streamlit apps created using ROOT_LOCATION, multi-file editing and Git integration are not supported.

```sqlsyntax
CREATE [ OR REPLACE ] STREAMLIT [ IF NOT EXISTS ] <name>
  ROOT_LOCATION = '<stage_path_and_root_directory>'
  MAIN_FILE = '<path_to_main_file_in_root_directory>'
  [ QUERY_WAREHOUSE = <warehouse_name> ]
  [ COMMENT = '<string_literal>' ]
  [ TITLE = '<app_title>' ]
  [ IMPORTS = ( '<stage_path_and_file_name_to_read>' [ , ... ] ) ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = ( <integration_name> [ , ... ] ) ]
```

## Required parameters

`name`
:   Specifies the identifier (i.e. name) for the Streamlit object. This identifier
    must be unique for the schema where the object is created.

    In addition, the identifier must start with an alphabetic character and can’t
    contain spaces or special characters unless the entire identifier string is
    enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in
    double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`FROM source_location`
:   Copies the app source files from the specified location. The location must be
    within an internal named stage. The path can be relative or fully qualified.
    For example, if the stage is named
    `@streamlit_db.streamlit_schema.streamlit_stage`, valid source locations can
    include:

    * A fully qualified path to the root of the stage:
      `FROM '@streamlit_db.streamlit_schema.streamlit_stage'`
    * A relative path to the root of the stage:
      `FROM '@streamlit_stage'`
    * A fully qualified or relative path to a subdirectory within the stage:
      `FROM '@streamlit_db.streamlit_schema.streamlit_stage/subdir'`

    Files are copied only one time when the CREATE command is executed; future
    changes to the source location don’t automatically update the Streamlit app.

    If this parameter isn’t specified, Snowflake copies the source files for a
    default app with a `streamlit_app.py` entrypoint file.

`MAIN_FILE = 'filename'`
:   Specifies the Streamlit entrypoint file. The requirements depend on the runtime type:

    * **Warehouse runtimes**: The file must be in the root of the source directory specified in FROM.
      Only a filename is allowed, not a path.
    * **Container runtimes**: The file can be in the root or a subdirectory. You can specify a relative
      path from the root of the source directory, like `'subdir/my_app.py'`.

    If you are using ROOT_LOCATION instead of FROM, then MAIN_FILE can be a path relative to ROOT_LOCATION
    even though ROOT_LOCATION only supports warehouse runtimes.

    DEFAULT: `'streamlit_app.py'`

`QUERY_WAREHOUSE = warehouse_name`
:   Specifies the warehouse used by the Streamlit app. The behavior depends on the runtime type:

    * **Warehouse runtimes**: Specifies the warehouse to run the app code and execute SQL queries.
      This is the code warehouse. It’s recommended to manually switch to a different warehouse within your app code for queries.
    * **Container runtimes**: Specifies the warehouse to execute SQL queries issued by the app.
      The app code runs on the compute pool specified by COMPUTE_POOL.

    DEFAULT: No value

    > **Note:**
    >
    > Although you can create a Streamlit object without this parameter, the app
    > won’t run until you specify a query warehouse.

`RUNTIME_NAME = 'runtime_name'`
:   Specifies the runtime environment for the Streamlit app. The runtime determines where and how
    the app executes. Runtime names follow the pattern `SYSTEM$ST_<type>_RUNTIME_PY<version>`.

    * **Warehouse runtimes**: Run the app in a virtual warehouse. Each viewer gets a personal instance
      of the app. The following warehouse runtimes are valid:

      + `SYSTEM$ST_WAREHOUSE_RUNTIME_PY3_9`
      + `SYSTEM$ST_WAREHOUSE_RUNTIME_PY3_10`
      + `SYSTEM$ST_WAREHOUSE_RUNTIME_PY3_11`
    * **Container runtimes**: Run the app in a Snowpark Container Services compute pool. All viewers
      share a single, long-running instance of the app. The following container runtimes are valid:

      + `SYSTEM$ST_CONTAINER_RUNTIME_PY3_11`

      [Preview Feature](../../release-notes/preview-features.md) — Open

      Available to all accounts.

    The runtime defaults to the latest warehouse runtime.

    DEFAULT: `SYSTEM$ST_WAREHOUSE_RUNTIME_PY3_11`

`COMPUTE_POOL = compute_pool_name`
:   Specifies the compute pool where the Streamlit app runs. This parameter is required when using
    a container runtime and is ignored for warehouse runtimes.

    [Preview Feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    DEFAULT: No value

`COMMENT = 'string_literal'`
:   Specifies a comment for the Streamlit object.

    DEFAULT: No value

`TITLE = 'app_title'`
:   Specifies a title for the Streamlit object to display in Snowsight.

    DEFAULT: The name of the Streamlit object passed to CREATE STREAMLIT.

`IMPORTS = ( 'stage_path_and_file_name_to_read' [ , ... ] )`
:   The location (stage), path, and name of the file(s) to import. This only applies to warehouse runtimes and
    is ignored for container runtimes.

    DEFAULT: No value

`EXTERNAL_ACCESS_INTEGRATIONS = ( integration_name [ , ... ] )`
:   The names of [external access integrations](create-external-access-integration.md) needed in order for the
    Streamlit app code to access external networks.

    For container runtimes, external access integrations are required to install packages from external package indexes
    like PyPI. For all runtime types, external access integrations enable the app to make outbound network requests.

    DEFAULT: No value

`SECRETS = ( 'snowflake_secret_name' = snowflake_secret [ , ... ] )`
:   Maps Snowflake secrets to secret names that can be referenced in the Streamlit app code. The secret name (left side)
    is how you reference the secret in your code, and the secret object (right side) is the identifier of the Snowflake secret.

    For example: `SECRETS = ('api_key' = my_database.my_schema.my_secret)`

    Secrets are only available in warehouse runtimes through the `_snowflake` module and must be associated with an external
    access integration in EXTERNAL_ACCESS_INTEGRATIONS. In container runtimes, this parameter
    isn’t supported and you must create SQL functions to access secrets instead. For more information, see
    [Manage secrets and configure your Streamlit app](../../developer-guide/streamlit/app-development/secrets-and-configuration.md).

    DEFAULT: No value

`ROOT_LOCATION = 'stage_path_and_root_directory'`
:   Specifies the path to the named stage containing the Streamlit Python files, media files, and the
    `environment.yml` file, for example:

    ```sqlexample
    ROOT_LOCATION = '@streamlit_db.streamlit_schema.streamlit_stage'
    ```

    In this example, the Streamlit files are located on a named stage named `streamlit_stage` within a database named
    `streamlit_db` and schema named `streamlit_schema`.

    > **Note:**
    >
    > * This parameter must point to a single directory inside a named internal stage.
    > * External stages are not supported for Streamlit in Snowflake.
    > * If you’re creating or replacing a Streamlit application object within the Snowflake Native App Framework, use `FROM 'relative_path_from_stage_root_directory'` and not `ROOT_LOCATION = 'stage_path_and_root_directory'`.

## Access control requirements

If your role does not own the objects in the following table, then your role
must have the listed
[privileges](../../user-guide/security-access-control-overview.md) on those objects:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE STREAMLIT | Schema where you create the Streamlit object |  |
| READ | Stage from which you copy the Streamlit app source files |  |
| USAGE | Warehouse used by the Streamlit app |  |
| USAGE | Compute pool used by the Streamlit app | This privilege is only required if your app uses a container runtime. |
| USAGE | External access integrations used by the Streamlit app | This privilege is only required if your app uses external access integrations. For container runtimes, this privilege is required to install packages from external package indexes like PyPI. |
| USAGE | Secrets used by the Streamlit app | This privilege is only required if your app uses secrets and only applies to warehouse runtimes. |
| CREATE STAGE | Schema where you create the Streamlit object | This privilege is only required to create Streamlit objects with the ROOT_LOCATION parameter. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* You must initialize the app after creating it.

  > **Important:**
  >
  > After you use CREATE STREAMLIT, the Streamlit app isn’t live until you do one of the
  > following actions:
  >
  > * Execute ALTER STREAMLIT … ADD LIVE VERSION FROM LAST on the new
  >   Streamlit object.
  > * Visit the app in Snowsight with the role that owns the app.
* When you clone a schema or database containing a Streamlit object, the Streamlit object is not cloned.
* To specify the packages used by the Streamlit application, include a dependency file in the source files.
  The format of the dependency file depends on the runtime type:

  * **Warehouse runtime**: Use an `environment.yml` file.
  * **Container runtime**: Use a `pyproject.toml` or `requirements.txt` file.

  For more information, see [Manage dependencies for your Streamlit app](../../developer-guide/streamlit/app-development/dependency-management.md).
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

### Create a Streamlit app with default source files

To create a container-runtime Streamlit app from built-in default files, run the CREATE STREAMLIT
command as shown in the following example:

```sqlexample
CREATE STREAMLIT hello_streamlit
  RUNTIME_NAME = 'SYSTEM$ST_CONTAINER_RUNTIME_PY3_11'
  COMPUTE_POOL = my_compute_pool
  QUERY_WAREHOUSE = my_warehouse;
```

By default, apps use the latest warehouse runtime if RUNTIME_NAME isn’t specified. To create a warehouse-runtime
Streamlit app from built-in default files, run the CREATE STREAMLIT command as shown in the following example:

```sqlexample
CREATE STREAMLIT hello_streamlit
  QUERY_WAREHOUSE = my_warehouse;
```

### Create a Streamlit app from a custom source files

To create a container-runtime Streamlit app from custom source files, run the CREATE STREAMLIT
command as shown in the following example:

```sqlexample
CREATE STREAMLIT hello_streamlit
  FROM @streamlit_db.streamlit_schema.streamlit_stage
  MAIN_FILE = 'streamlit_main.py'
  QUERY_WAREHOUSE = my_warehouse
  RUNTIME_NAME = 'SYSTEM$ST_CONTAINER_RUNTIME_PY3_11'
  COMPUTE_POOL = my_compute_pool;
```

To create a warehouse-runtime Streamlit app from custom source files, run the CREATE STREAMLIT
command as shown in the following example:

```sqlexample
CREATE STREAMLIT hello_streamlit
  FROM @streamlit_db.streamlit_schema.streamlit_stage
  MAIN_FILE = 'streamlit_main.py'
  QUERY_WAREHOUSE = my_warehouse;
```

### Create a warehouse-runtime Streamlit app with secrets

To create a warehouse-runtime Streamlit app with secrets, run the CREATE STREAMLIT command as shown in the following example:

```sqlexample
CREATE STREAMLIT hello_streamlit
  FROM @streamlit_db.streamlit_schema.streamlit_stage
  MAIN_FILE = 'streamlit_main.py'
  QUERY_WAREHOUSE = my_warehouse
  SECRETS = ('api_key' = streamlit_db.streamlit_schema.my_api_secret);
```

Container-runtime Streamlit apps must use SQL functions to access secrets. For more information, see
[Manage secrets and configure your Streamlit app](../../developer-guide/streamlit/app-development/secrets-and-configuration.md).

### Create a Streamlit app from a Git repository

To create a Streamlit app from a Git repository, run the CREATE STREAMLIT command as shown in the following example:

```sqlexample
CREATE STREAMLIT hello_streamlit
  FROM @streamlit_db.streamlit_schema.streamlit_repo/branches/streamlit_branch/
  MAIN_FILE = 'streamlit_main.py'
  QUERY_WAREHOUSE = my_warehouse;
```
