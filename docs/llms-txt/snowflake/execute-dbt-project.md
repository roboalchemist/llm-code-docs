# Source: https://docs.snowflake.com/en/sql-reference/sql/execute-dbt-project.md

# EXECUTE DBT PROJECT

Executes the specified [dbt project object](../../user-guide/data-engineering/dbt-projects-on-snowflake.md) or the dbt project in a Snowflake workspace using the dbt command and command-line options specified.

See also:
:   [CREATE DBT PROJECT](create-dbt-project.md), [ALTER DBT PROJECT](alter-dbt-project.md), [DESCRIBE DBT PROJECT](desc-dbt-project.md), [DROP DBT PROJECT](drop-dbt-project.md), [SHOW DBT PROJECTS](show-dbt-projects.md)

## Syntax

Executes the dbt project object with the specified name.

```sqlsyntax
EXECUTE DBT PROJECT [ IF EXISTS ] <name>
  [ ARGS = '[ <dbt_command> ] [ --<dbt_cli_option> <option_value_1> [ ... ] ] [ ... ]' ]
  [ DBT_VERSION = 'version_number' ]
```

## Variant syntax

Executes the dbt project that is saved in a workspace with the specified workspace name. The user who owns the workspace must be the user who runs this command variant.

```sqlsyntax
EXECUTE DBT PROJECT [ IF EXISTS ] [ FROM WORKSPACE <name> ]
  [ ARGS = '[ <dbt_command> ] [ --<dbt_cli_option> <option_value_1> [ ... ] [ ... ] ]' ]
  [ DBT_VERSION = 'version_number' ]
  [ PROJECT_ROOT = '<subdirectory_path>' ]
```

## Required parameters

`name`
:   When executing a dbt project object, specifies the name of the dbt project object to execute.

    When executing a dbt project by using the FROM WORKSPACE option, specifies the name of the workspace for dbt Projects on Snowflake. The workspace name is always specified in reference to the `public` schema in the user’s personal database, which is indicated by `user$`.

    We recommend enclosing the workspace name in double quotes because workspace names are case-sensitive and can contain special characters.

    The following example shows a workspace name reference:

    `user$.public."My dbt Project Workspace"`

## Optional parameters

`ARGS = '[ dbt_command ] [ --dbt_cli_option option_value_1 [ ... ] [ ... ] ]'`
:   Specifies the [dbt command](https://docs.getdbt.com/reference/dbt-commands) and supported [command-line options](https://docs.getdbt.com/reference/global-configs/about-global-configs#available-flags) to run when the dbt project executes. This is a literal string that must conform to the syntax and requirements of dbt CLI commands.

    If no value is specified, the dbt project executes with the [dbt command](https://docs.getdbt.com/reference/dbt-commands) and [command-line options](https://docs.getdbt.com/reference/global-configs/about-global-configs#available-flags) specified in the [dbt project object definition](create-dbt-project.md). If you specify dbt CLI options without specifying a dbt command, the dbt `run` command executes by default.

    Default: No value

`DBT_VERSION = 'version_number'`
:   Specifies a version for the dbt Project.

    Default: When you execute a dbt project, the system uses the default version you specified when creating the dbt project. If none was specified, the system uses `1.9.4` by default.

    For more information, see [Supported dbt Core versions for dbt Projects on Snowflake](../../user-guide/data-engineering/dbt-projects-on-snowflake-dbt-core-versions.md).

`PROJECT_ROOT = 'subdirectory_path'`
:   Specifies the subdirectory path to the `dbt_project.yml` file within the dbt project object or workspace. This parameter is only supported when executing a dbt project by using the FROM WORKSPACE option.

    If no value is specified, the dbt project executes with the `dbt_project.yml` file in the root directory of the dbt project object.

    If no `dbt_project.yml` file exists in the root directory or in the PROJECT_ROOT subdirectory, an error occurs.

    Default: No value

## Output

| Column | Description |
| --- | --- |
| `0|1 Success` | `TRUE` if the dbt project executed successfully; otherwise, `FALSE`. If the dbt project fails to execute, an exception message is returned. |
| `EXCEPTION` | Any exception message returned by the dbt project execution. If the dbt project executes successfully, the string `None` is returned. |
| `STDOUT` | The standard output returned by the dbt project execution. |
| `OUTPUT_ARCHIVE_URL` | The URL of the output archive that contains output files of the dbt project execution. This includes log files and artifacts that dbt writes to the `/target` directory. For more information, see [About dbt artifacts](https://docs.getdbt.com/reference/artifacts/dbt-artifacts) in dbt documentation. Selecting this link directly results in an error; however, you can use this URL to retrieve dbt project files and output. For more information, see [Access dbt artifacts and logs programmatically](../../user-guide/data-engineering/dbt-projects-on-snowflake-monitoring-observability.md). |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object |
| --- | --- |
| USAGE | dbt project |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

> **Note:**
>
> The dbt command specified in EXECUTE DBT PROJECT runs with the privileges of the `role` specified in the `outputs` block of the projects `profiles.yml` file. Operations are further restricted to only those privileges granted to the Snowflake user calling EXECUTE DBT PROJECT. Both the user and the role specified must have the required privileges to use the `warehouse`, perform operations on the `database` and `schema` specified in the project’s `profiles.yml` file, and perform operations on any other Snowflake objects that the dbt model specifies.

## Examples

* Default run command with target and models specified
* Explicit test command with target and models specified
* Explicit run command with downstream models specified
* Run and test dbt projects using production tasks

### Default run command with target and models specified

Execute a dbt `run` targeting the `dev` profile in the `dbt_project.yml` file in the root directory of the dbt project object and selecting three models from the project DAG. No `run` command is explicitly specified and is executed by default.

```sqlexample
EXECUTE DBT PROJECT my_database.my_schema.my_dbt_project
  ARGS = '--select simple_customers combined_bookings prepped_data --target dev';
```

### Explicit test command with target and models specified

Execute a dbt `test` command targeting the `prod` profile in the `dbt_project.yml` file in the root directory of the dbt project object and selecting three models from the project DAG.

```sqlexample
EXECUTE DBT PROJECT my_database.my_schema.my_dbt_project
  ARGS = '--select simple_customers combined_bookings prepped_data --target prod';
```

### Explicit run command with downstream models specified

Execute a dbt `run` command targeting the `dev` profile in the `dbt_project.yml` file and selecting all models downstream of the `simple_customers` model using the dbt `+` notation.

```sqlexample
EXECUTE DBT PROJECT my_database.my_schema.my_dbt_project
  ARGS = 'run --select simple_customers+ --target dev';
```

### Run and test dbt projects using production tasks

Create a task for a production dbt target that executes a dbt `run` command on a six-hour interval. Then create a task that executes the dbt `test` command after each dbt `run` task completes. The EXECUTE DBT PROJECT command for each task targets the `prod` profile in the `dbt_project.yml` file in the root directory of the dbt project object.

```sqlexample
CREATE OR ALTER TASK my_database.my_schema.run_dbt_project
  WAREHOUSE = my_warehouse
  SCHEDULE = '6 hours'
AS
  EXECUTE DBT PROJECT my_database.my_schema.my_dbt_project args='run --target prod';

CREATE OR ALTER TASK change_this.public.test_dbt_project
        WAREHOUSE = my_warehouse
        AFTER run_dbt_project
AS
  EXECUTE DBT PROJECT my_database.my_schema.my_dbt_project args='test --target prod';
```

### Override the project’s pinned version at execution time for testing or temporary needs

`my_dbt_project` is pinned to 1.9.4. This execution overrides the dbt project’s default 1.9.4 version:

```sqlexample
EXECUTE DBT PROJECT finance_analytics
  DBT_VERSION = '1.10.15'
```
