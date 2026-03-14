# Source: https://docs.snowflake.com/en/sql-reference/sql/execute-notebook-project.md

# EXECUTE NOTEBOOK PROJECT

Executes a notebook stored in a notebook project (NPO). This command runs the notebook in a non-interactive (headless) mode and is useful for CI/CD
pipelines and other orchestrated workflows where you want to pass parameters or lock dependency versions for repeatable runs. The command can be run from:

* SQL files.
* Other Snowflake executables (Tasks).
* External orchestrators that issue SQL (for example, Airflow, Prefect, Dagster, CI/CD systems).

The command runs the notebook file you specify as `MAIN_FILE` using the runtime, compute pool, warehouse, and external access integrations you
configure.

> **Important:**
>
> Before triggering a non-interactive run, ensure that your notebook sets its execution context (database and schema) or uses fully qualified
> object names. For more information, see [Editing and running notebooks in Workspaces](../../user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-edit-run.md).

See also:
[CREATE NOTEBOOK PROJECT](create-notebook-project.md), [CREATE TASK](create-task.md), [CI/CD workflow scenario](../../user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-workflow-scenarios.md),
[Observability and logging for Notebooks in Workspaces](../../user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-observability-logging.md), [Running notebooks with parameters](../../user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-parameters.md)

## Syntax

```sqlsyntax
EXECUTE NOTEBOOK PROJECT <database_name>.<schema_name>.<project_name>
  MAIN_FILE = 'notebook.ipynb'
  COMPUTE_POOL = '<compute_pool_name>'
  QUERY_WAREHOUSE = '<warehouse_name>'
  RUNTIME = '<runtime_version>'
  [ ARGUMENTS = '<parameter_string>' ]
  [ REQUIREMENTS_FILE = '<path/to/requirements.txt>' ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = ( <integration_name> [ , ... ] ) ];
```

## Required parameters

`database_name.schema_name.project_name`
:   Fully qualified identifier of the notebook project to execute.

    Must reference an existing notebook project created with [CREATE NOTEBOOK PROJECT](create-notebook-project.md).

    Must be fully qualified unless it resides in the current DATABASE and SCHEMA.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`MAIN_FILE = 'notebook_file_name.ipynb'`
:   Specifies the main notebook file within the workspace to execute (`path/to/notebook.ipynb`).

    Must be an `.ipynb` notebook file located in the workspace referenced by the project.

    The path is relative to the workspace root.

`COMPUTE_POOL = 'compute_pool_name'`
:   Specifies the compute pool used when executing the notebook on a Container Runtime.

    Required when the notebook runtime uses Snowpark Container Services.

`QUERY_WAREHOUSE = 'warehouse_name'`
:   Specifies the virtual warehouse used for executing SQL and Snowpark queries from the notebook.

    Required if the notebook performs SQL or Snowpark operations and no warehouse is otherwise configured.

    When using container runtimes, the warehouse handles query pushdown; Python executes on the compute pool.

`RUNTIME = 'runtime_version'`
:   Specifies the runtime image/version for executing the notebook (for example, `'1.0' or '2.2-CPU-PY3.11'`).

    Determines the Python version and execution environment used for the notebook execution.

    Corresponds to a Container Runtime image (CPU or GPU) or warehouse runtime variant.

## Optional parameters

Depending on how the project and runtime are configured, you may need to set the following parameters. The descriptions below define their
purpose and typical usage.

`ARGUMENTS = 'parameter_string'`
:   Optionally passes one or more string arguments to the notebook at runtime, which appear as command-line arguments in the `sys.argv` list.
    Arguments are useful for making notebook logic dynamic (for example, selecting an environment such as `env prod`).

    To pass multiple arguments, specify them in a single string separated by spaces. The arguments are parsed into `sys.argv` using
    whitespace as the delimiter. In a Python cell, access the arguments using `sys.argv[0]` for the notebook name, `sys.argv[1]` for
    the first argument, and so on.

    Only strings are supported; other data types (such as integers or Booleans) are interpreted as NULL.

    Examples:

    ```sqlexample
    ARGUMENTS = 'env prod';
    ```

    ```python
    import sys
    print(sys.argv)
    ```

`REQUIREMENTS_FILE = '<path/to/requirements.txt>'`
:   Optionally specifies a `requirements.txt` file in a workspace or on a stage to pre-install exact versions of libraries (such as pandas
    or scikit-learn) and other Python dependencies before notebook execution. Pinning dependencies is critical for idempotency and helps
    make notebook runs more repeatable, reducing errors caused by changes in library versions. The file must be accessible to the executing role.

`EXTERNAL_ACCESS_INTEGRATIONS = ( integration_name [ , ... ] )`
:   Specifies one or more external access integrations that the notebook can use during execution.

    Required when the notebook makes outbound network calls (for example, to external APIs).

    Each integration name must reference an existing external access integration.

    Multiple external access integrations can be specified in a comma-separated list inside the parentheses.

    Example:

    ```sqlexample
    EXTERNAL_ACCESS_INTEGRATIONS = (http_eai, s3_eai);
    ```

    > **Note:**
    >
    > The Snowflake-managed PyPI network rule `SNOWFLAKE.EXTERNAL_ACCESS.PYPI_RULE` is only accessible to the ACCOUNTADMIN role.
    > Consequently, using this rule in an External Access Integration (EAI) for notebook objects or scheduled tasks may cause them to fail.
    > To avoid this, create a user-defined network rule for PyPI and reference it in your external access integration. For more information,
    > see [Snowflake-managed egress network rules](../../user-guide/network-rules.md).

## Access control requirements

The role executing `EXECUTE NOTEBOOK PROJECT` must have sufficient privileges on the notebook project.

In addition, the executing role must have USAGE and MONITOR on the query warehouse, and USAGE or OWNERSHIP on:

* The compute pool.
* The database and schema containing the notebook project.
* Tasks and external access integrations referenced by the command.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* It is not possible to use the EXECUTE NOTEBOOK PROJECT command from a notebook.
* You can call `EXECUTE NOTEBOOK PROJECT` from tasks, thus enabling notebook runs as part of larger workflows.
* Snowflake doesn’t support embedding the `EXECUTE NOTEBOOK PROJECT` command in a task that is configured to run using the [EXECUTE AS USER](../../user-guide/tasks-intro.md) clause.
  You will not see an error message when creating such a task, but when the task is executed, it will fail.
* When you run a notebook using the `EXECUTE NOTEBOOK PROJECT` command:
* Notebook code is executed on the compute pool specified by the COMPUTE_POOL parameter using the runtime specified by the RUNTIME parameter.
* SQL and Snowpark queries are executed using the warehouse specified by the QUERY_WAREHOUSE parameter.

## Examples

Execute a notebook project:

```sqlexample
EXECUTE NOTEBOOK PROJECT "sales_detection_db"."schema"."DEFAULT_PROJ_B32BCFD4"
  MAIN_FILE = 'notebook_file.ipynb'
  COMPUTE_POOL = 'test_X_CPU'
  QUERY_WAREHOUSE = 'ENG_INFRA_WH'
  RUNTIME = 'V2.2-CPU-PY3.10'
  ARGUMENTS = 'env prod'
  REQUIREMENTS_FILE = 'path/to/requirements.txt'
  EXTERNAL_ACCESS_INTEGRATIONS = ('test_EAI');
```
