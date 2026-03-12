# Source: https://docs.snowflake.com/en/user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-parameters.md

# Running notebooks with parameters

Currently, parameters passed in the `ARGUMENTS` string are parsed into the `sys.argv` list using whitespace as the delimiter.

## Example: Execute a notebook project with parameters

The following example passes two arguments (env and prod) using ARGUMENTS = ‘env prod’.

The first element (`sys.argv[0]`) is the notebook filename, followed by the space-separated arguments.

```sqlexample
EXECUTE NOTEBOOK PROJECT "<database_name>"."<schema_name>"."<project_name>"
  MAIN_FILE = 'snow://workspace/<workspace_hash>/path/to/notebook.ipynb' -- Notebook name with full file path
  COMPUTE_POOL = '<compute_pool_name>'
  RUNTIME = '<runtime_version>'    -- For example, V2.2-CPU-PY3.11
  QUERY_WAREHOUSE = '<warehouse_name>'
  ARGUMENTS = 'env prod' -- Can pass in a single string, which can be parsed in the notebook code. Point to the environment configuration.
  REQUIREMENTS_FILE = 'path/to/requirements.txt';
```

## View all arguments

To inspect the full list of parameters passed to the session, use the `sys` module.

```python
import sys
print(sys.argv)
```

Output example:

```text
['exampletestSCOS.ipynb', 'env', 'prod']
```

## Print each argument

To process or log each parameter individually, loop through the `sys.argv` list.

```python
import sys
for arg in sys.argv:
    print(arg)
```

Output example:

```text
exampletestSCOS.ipynb
env
prod
```

## Access a specific argument

Parameters are accessed by their index in the list. Because `sys.argv[0]` is the notebook name, the first user parameter starts at `index[1]`.

```python
import sys

# Access the first user parameter
first_param = sys.argv[1]
print(first_param)
```

Output example:

```text
env
```

For full syntax and parameter details, see [EXECUTE NOTEBOOK PROJECT](../../../sql-reference/sql/execute-notebook-project.md).
