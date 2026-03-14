# Source: https://docs.snowflake.com/en/developer-guide/stored-procedure/python/procedure-python-profiler.md

# Profiling Python procedure handler code

You can discover how much time or memory was spent executing your handler code by using the built-in code profiler. The profiler generates
information describing how much time or memory was spent executing each line of the procedure handler.

Using the profiler, you can generate reports that focus on one of the following at a time:

* **Amount of time per line**, in which the report shows the number of times a line was executed, how long the execution took, and so on.
* **Amount of memory usage per line**, in which the report shows the amount of memory consumed per line.

The profiler saves the generated report to a Snowflake [internal user stage](../../../user-guide/data-load-overview.md) you specify.
You can read the profiler output using the [GET_PYTHON_PROFILER_OUTPUT (SNOWFLAKE.CORE)](../../../sql-reference/functions/get_python_profiler_output.md)
system function.

> **Note:**
>
> Profiling introduces performance overhead on Python execution and can affect the performance of the query.
> It’s intended for development, testing, and troubleshooting and should not be enabled on continuous production workloads.

## Required privileges

Setting the session-level parameter does not trigger privilege check, but when a stored procedure is executed with [ACTIVE_PYTHON_PROFILER](../../../sql-reference/parameters.md)
session parameter to either LINE or MEMORY, Snowflake will check the following privileges.

* You must have read/write privileges on the profiling output stage.
* You must have OWNERSHIP privilege on the stored procedure.

## Limitations

* Only stored procedures are supported. UDFs support is not available yet.
* Recursive profiling is not supported. Only top-level functions of the specified modules are profiled. Functions defined inside
  functions are not.
* Support for profiling stored procedures created on the client-side via the `snowflake.snowpark` API is not supported (for example,
  stored procedures created from `Session.sproc.register`).
* Python functions running in parallel through `joblib` will not be profiled.
* System defined stored procedures cannot be profiled. They will produce no output.

## Usage

Once you’ve set up the profiler for use, you can use it simply by calling the stored procedure to generate profiler output. After the
procedure finishes executing, the profiler’s output is written to a file on the stage you specify. You can fetch the profiler output
using a system function.

Follow these steps to set up and use the profiler:

1. Specify the Snowflake stage where profile output should be written.

   Set the parameter PYTHON_PROFILER_TARGET_STAGE to the stage’s fully-qualified name.
2. Enable the profiler and specify what the profile should focus on.

   Set the ACTIVE_PYTHON_PROFILER session parameter.
3. Call the stored procedure.

   After the profiler is enabled, call your stored procedure.
4. View profiling output.

   At the end of execution, the profiling output will be uploaded as a file to the output stage with the naming pattern of `<query_id>_<sproc_name>.lprof`
   or `<query_id>_<sproc_name>.mprof`.

### Specify the Snowflake stage where profile output should be written

Before running the profiler, you must specify a stage to which its report will be saved. To specify the stage, set the
[PYTHON_PROFILER_TARGET_STAGE](../../../sql-reference/parameters.md) parameter to the stage’s fully-qualified name.

* Use a temporary stage to store output only for the duration of the session.
* Use a permanent stage to preserve the profiler output outside of the scope of a session.

Code in the following example creates a temporary `profiler_output` stage to receive the profiler output.

```sqlexample
USE DATABASE my_database;
USE SCHEMA my_schema;

CREATE TEMPORARY STAGE profiler_output;
ALTER SESSION SET PYTHON_PROFILER_TARGET_STAGE = "my_database.my_schema.profiler_output";
```

### Enable the profiler and specify what the profile should focus on

Set the [ACTIVE_PYTHON_PROFILER](../../../sql-reference/parameters.md) session parameter to a value specifying which kind of profile report you want to generate.

* To have the profile focus on line use activity, set the parameter to the `LINE` value (case insensitive), as shown below:

  ```sqlexample
  ALTER SESSION SET ACTIVE_PYTHON_PROFILER = 'LINE';
  ```

* To have the profile focus on memory use activity, set the parameter to the `MEMORY` value (case insensitive), as shown below:

  ```sqlexample
  ALTER SESSION SET ACTIVE_PYTHON_PROFILER = 'MEMORY';
  ```

### Call the stored procedure

After the profiler is enabled, call your stored procedure.

```sqlexample
CALL YOUR_STORED_PROCEDURE();
```

By default, the profiler will profile methods that are defined in the user’s module. You can register other modules to profile as well. For more information,
see Profile Additional Modules.

### View profiling output

At the end of execution, the profiling output will be uploaded as a file to the output stage with the naming pattern of `<query_id>_<sproc_name>.lprof`
or `<query_id>_<sproc_name>.mprof`.

The output can be accessed via a system function [GET_PYTHON_PROFILER_OUTPUT](../../../sql-reference/functions/get_python_profiler_output.md)
in the [SNOWFLAKE database](../../../sql-reference/snowflake-db.md).

The format of the system function’s signature is as follows:

```sqlexample
SELECT SNOWFLAKE.CORE.GET_PYTHON_PROFILER_OUTPUT(<query_id>);
```

Replace `<query_id>` with the query ID of the stored procedure query for which profiling was enabled.

You can also directly access the output file on the output stage. For more information, see [Viewing staged files](../../../user-guide/data-load-local-file-system-stage-ui.md).

> **Note:**
>
> The system function looks for profiling output files from the stage specified with the PYTHON_PROFILER_TARGET_STAGE parameter.
>
> The profiling output for child stored procedures is not appended into the parent procedure output.
> To view the output for a child stored procedure, call the system function on the child procedure query ID explicitly.

## Including additional modules for profiling

You can include for profiling modules that aren’t included by default. To include additional modules for profiling, set the
PYTHON_PROFILER_MODULES parameter to the names of modules you want to include.

By default, methods defined in the your module will be profiled. These methods include the following:

* The handler method
* Methods defined in the module
* Methods imported from packages or other modules.

In the example below, `handler`, `helper` and `some_method` will all be profiled by default.

```sqlexample-python
CREATE OR REPLACE PROCEDURE my_sproc()
  RETURNS VARIANT
  LANGUAGE PYTHON
  RUNTIME_VERSION = 3.10
  PACKAGES = ('snowflake-snowpark-python', 'other_package')
  HANDLER='handler'
AS $$
from other_package import some_method

def helper():
...

def handler(session):
...
$$;
```

### Including modules with the PYTHON_PROFILER_MODULES parameter

You can use the [PYTHON_PROFILER_MODULES](../../../sql-reference/parameters.md) parameter to include for profiling modules that wouldn’t be included by default. When
you include a module in this way, all functions used from that module will be included in the profiler output. By default, the
PYTHON_PROFILER_MODULES parameter value is an empty string (`''`), in which the profile would profile only inline handler code, if
any.

To include modules for profiling, specify their names as the parameter’s value in a comma-separated list, as illustrated below.

```sqlexample
ALTER SESSION SET PYTHON_PROFILER_MODULES = 'module_a, my_module';
```

## Profiling staged handler code

To profile handler code that is staged rather than inline — including helper functions — you must explicitly specify the staged handler
for profiling using the [PYTHON_PROFILER_MODULES](../../../sql-reference/parameters.md) parameter.

By default, the profiler doesn’t profile handler code that is [staged, rather than inline](../../inline-or-staged.md) —
that is, when the handler module is specified with the IMPORTS clause.

For example, by default this procedure will generate no detailed profiling output.

```sqlexample
CREATE OR REPLACE PROCEDURE test_udf_1()
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION = '3.12'
  PACKAGES=('snowflake-snowpark-python')
  HANDLER = 'test_python_import_main.my_udf'
  IMPORTS = ('@stage1/test_python_import_main.py', '@stage2/test_python_import_module.py');
```

To include staged code for profiling, specify staged module names as the PYTHON_PROFILER_MODULES parameter’s value in a comma-separated
list, as illustrated below.

```sqlexample
ALTER SESSION SET PYTHON_PROFILER_MODULES = 'test_python_import_main, test_python_import_module';
```

## Example

Code in this example illustrates how to use the profiler to generate and retrieve a report of line usage.

```sqlexample-python
CREATE OR REPLACE PROCEDURE last_n_query_duration(last_n NUMBER, total NUMBER)
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION=3.12
  PACKAGES=('snowflake-snowpark-python')
  HANDLER='main'
AS $$
import snowflake.snowpark.functions as funcs

def main(session, last_n, total):
  # create sample dataset to emulate id + elapsed time
  session.sql('''
  CREATE OR REPLACE TABLE sample_query_history (query_id INT, elapsed_time FLOAT)
  ''').collect()
  session.sql('''
  INSERT INTO sample_query_history
  SELECT
  seq8() AS query_id,
  uniform(0::float, 100::float, random()) as elapsed_time
  FROM table(generator(rowCount => {0}));'''.format(total)).collect()

  # get the mean of the last n query elapsed time
  df = session.table('sample_query_history').select(
    funcs.col('query_id'),
    funcs.col('elapsed_time')).limit(last_n)

  pandas_df = df.to_pandas()
  mean_time = pandas_df.loc[:, 'ELAPSED_TIME'].mean()
  del pandas_df
  return mean_time
$$;

CREATE TEMPORARY STAGE profiler_output;
ALTER SESSION SET PYTHON_PROFILER_TARGET_STAGE = "my_database.my_schema.profiler_output";
ALTER SESSION SET ACTIVE_PYTHON_PROFILER = 'LINE';

-- Sample 1 million from 10 million records
CALL last_n_query_duration(1000000, 10000000);

SELECT SNOWFLAKE.CORE.GET_PYTHON_PROFILER_OUTPUT(last_query_id());
```

The line profiler output will look like this:

```output
Handler Name: main
Python Runtime Version: 3.12
Modules Profiled: ['main_module']
Timer Unit: 0.001 s

Total Time: 8.96127 s
File: _udf_code.py
Function: main at line 4

Line #      Hits        Time  Per Hit   % Time  Line Contents
==============================================================
    4                                           def main(session, last_n, total):
    5                                               # create sample dataset to emulate id + elapsed time
    6         1        122.3    122.3      1.4      session.sql('''
    7                                                   CREATE OR REPLACE TABLE sample_query_history (query_id INT, elapsed_time FLOAT)''').collect()
    8         2       7248.4   3624.2     80.9      session.sql('''
    9                                               INSERT INTO sample_query_history
    10                                               SELECT
    11                                               seq8() AS query_id,
    12                                               uniform(0::float, 100::float, random()) as elapsed_time
    13         1          0.0      0.0      0.0      FROM table(generator(rowCount => {0}));'''.format(total)).collect()
    14
    15                                               # get the mean of the last n query elapsed time
    16         3         58.6     19.5      0.7      df = session.table('sample_query_history').select(
    17         1          0.0      0.0      0.0          funcs.col('query_id'),
    18         2          0.0      0.0      0.0          funcs.col('elapsed_time')).limit(last_n)
    19
    20         1       1528.4   1528.4     17.1      pandas_df = df.to_pandas()
    21         1          3.2      3.2      0.0      mean_time = pandas_df.loc[:, 'ELAPSED_TIME'].mean()
    22         1          0.3      0.3      0.0      del pandas_df
    23         1          0.0      0.0      0.0      return mean_time
```

The memory profiler output will look like this:

```output
ALTER SESSION SET ACTIVE_PYTHON_PROFILER = 'MEMORY';

Handler Name: main
Python Runtime Version: 3.12
Modules Profiled: ['main_module']
File: _udf_code.py
Function: main at line 4

Line #   Mem usage    Increment  Occurrences  Line Contents
=============================================================
    4    245.3 MiB    245.3 MiB           1   def main(session, last_n, total):
    5                                             # create sample dataset to emulate id + elapsed time
    6    245.8 MiB      0.5 MiB           1       session.sql('''
    7                                                 CREATE OR REPLACE TABLE sample_query_history (query_id INT, elapsed_time FLOAT)''').collect()
    8    245.8 MiB      0.0 MiB           2       session.sql('''
    9                                             INSERT INTO sample_query_history
    10                                             SELECT
    11                                             seq8() AS query_id,
    12                                             uniform(0::float, 100::float, random()) as elapsed_time
    13    245.8 MiB      0.0 MiB           1       FROM table(generator(rowCount => {0}));'''.format(total)).collect()
    14
    15                                             # get the mean of the last n query elapsed time
    16    245.8 MiB      0.0 MiB           3       df = session.table('sample_query_history').select(
    17    245.8 MiB      0.0 MiB           1           funcs.col('query_id'),
    18    245.8 MiB      0.0 MiB           2           funcs.col('elapsed_time')).limit(last_n)
    19
    20    327.9 MiB     82.1 MiB           1       pandas_df = df.to_pandas()
    21    328.9 MiB      1.0 MiB           1       mean_time = pandas_df.loc[:, 'ELAPSED_TIME'].mean()
    22    320.9 MiB     -8.0 MiB           1       del pandas_df
    23    320.9 MiB      0.0 MiB           1       return mean_time
```
