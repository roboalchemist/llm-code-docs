# Source: https://docs.snowflake.com/en/developer-guide/udf/python/profiling-udf-handlers.md

# Profiling Snowpark Python user-defined function handlers

You can discover how much time or memory was spent executing your handler code by using the built-in code profiler. The profiler generates
information describing how much time or memory was spent executing each line of the handler.

Using the profiler, you can generate reports that focus on one of the following at a time:

* **Amount of time per line**, which shows the number of times a line was executed, how long the execution took, and so on.
* **Amount of memory usage per line**, which shows the amount of memory consumed per line.

The profiler saves the generated report to an internal [event table](../../logging-tracing/event-table-columns.md). You can
retrieve the results by using a function designed to access the table.

> **Note:**
>
> Profiling introduces performance overhead to Python execution and can affect the performance of the query.
> It’s intended for development and testing and should not be enabled on continuous production workloads.

## Required privileges

To manage and use the profiler results data, which is stored in the `SNOWFLAKE.LOCAL.PROFILER_EVENTS_RAW` event table, you must
use the following roles:

| Application Role | Notes |
| --- | --- |
| PROFILER_EVENTS_ADMIN | Required to manage data in the event table where profiler data is stored, including to select, truncate, or drop records. |
| PROFILER_USER | Required to read profiler results from the event table. |

For more information on granting an application role, see [GRANT APPLICATION ROLE](../../../sql-reference/sql/grant-application-role.md). The following example uses the `ACCOUNTADMIN` role to grant the application role `PROFILER_USER` to a user.

```sqlexample
USE ROLE ACCOUNTADMIN;
CREATE ROLE PROFILER_ROLE;
GRANT APPLICATION ROLE SNOWFLAKE.PROFILER_USER TO ROLE PROFILER_ROLE;
GRANT ROLE PROFILER_ROLE TO USER some_user;
```

## Limitations

* It can take 15-20 seconds after query execution for results from the profiler to be ready.
* Profiler output is not saved if the UDF execution fails.
* Recursive profiling is not supported. Only top-level functions of the specified modules are profiled. Functions defined inside
  functions are not profiled.
* Profiling third party modules is not supported.
* Support for profiling UDFs created on the client side via the `snowflake.snowpark` API is not available.
* Python functions running in parallel through `joblib` are not profiled.
* UDTFs are not supported.
* Time is measured in wall-clock time, not CPU time.

## Usage

Once you’ve set up the profiler, you can use it simply by executing the UDF to generate profiler output. After the
UDF finishes executing, the profiler’s output is written to an internal event table. You can
fetch the profiler output using a system function.

Follow these steps in your code to set up and use the profiler:

1. Enable the profiler and set what the profile report should focus on.
2. Execute the UDF.
3. View profiling output.

## Enable the profiler by specifying its focus

To enable the profiler set one of the following session parameters:

```sqlexample
-- To enable profiling that focuses on activity per line
ALTER SESSION SET ACTIVE_PYTHON_PROFILER = 'LINE';

-- To enable profiling that focuses on memory usage
ALTER SESSION SET ACTIVE_PYTHON_PROFILER = 'MEMORY';
```

> **Note:**
>
> Profiling introduces performance overhead on Python execution. You should profile your code during development and testing.
> Do not enable profiling on continuous production workloads.

## Specifying the code to be profiled

By default, the profiler profiles methods defined inline with the UDF declaration. In other words, the profiler will profile all the
methods defined in the handler.

For the following UDF example, the profiler will profile the `handler` method and `helper` method.

```sqlexample-python
CREATE OR REPLACE function my_udf()
  RETURNS VARIANT
  LANGUAGE PYTHON
  RUNTIME_VERSION = 3.11
  PACKAGES = ('other_package')
  HANDLER = 'handler'
  AS $$
from other_package import some_method

def helper():
...

def handler():
...
$$;
```

### Specify external code to profile

You can specify that the profiler should profile handler code defined outside the UDF declaration, such as code imported from a stage.

To specify external code for profiling, set the PYTHON_UDF_PROFILER_MODULES session parameter’s value to a comma-separated list of the
modules containing the code.

```sqlexample
ALTER SESSION SET PYTHON_UDF_PROFILER_MODULES = 'test_python_import_main, test_python_import_module';
```

The profiler will include the specified modules in its profiling output when you execute a UDF that imports them.

Code in the following example shows a UDF that imports code from the specified modules:

```sqlexample
CREATE OR REPLACE function test_udf_1()
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION = 3.11
  HANDLER = 'test_python_import_main.my_udf'
  IMPORTS = ('@stage1/test_python_import_main.py', '@stage2/test_python_import_module.py');
```

## Execute the user-defined function

After you’ve enabled the profiler, execute your user-defined function (UDF) to begin profiling.

By default, the profiler profiles methods that are defined in your module. For information on registering other modules from imported
files to profile, see Specifying the code to be profiled for more information.

```sqlexample
SELECT return_mean(my_col) FROM MY_TABLE;
```

## View profiling output

* To view profiling output, query an internal [event table](../../logging-tracing/event-table-columns.md).

Profiling results are typically available in the event table 15-20 seconds after the UDF execution finishes. You can access the output by using
the table system function, GET_PYTHON_UDF_PROFILER_OUTPUT.

Code in the following example shows a query of the event table for profiler results. The `query_id` specified as an argument is the
query ID of the UDF query for which profiling was enabled.

```sqlexample
SELECT * FROM TABLE(SNOWFLAKE.LOCAL.GET_PYTHON_UDF_PROFILER_OUTPUT(<query_id>));
```

### Profile results

When you view profiler results, you’ll see a report that differs depending on whether you specified profiling for a line report or
a memory report.

The memory profiler output will look like this:

```none
Handler Name: return_mean
Python Runtime Version: 3.12
Modules Profiled: ['return_mean_module']
Extension Function ID: 1

File: _udf_code.py
Function: return_mean at line 2

Line #    Mem usage    Increment  Occurrences    Line Contents
==============================================================
     2    107.0 MiB    107.0 MiB           1    def return_mean():
     3    144.6 MiB     37.6 MiB           1        import numpy as np
     4
     5                                              # Generate a numpy array with 10 random integers between 1 and 100
     6                                              # np.random.randint(low, high, size)
     7    147.3 MiB      2.7 MiB           1        random_array = np.random.randint(1, 101, 10)
     8
     9                                              # Use a numpy function to calculate the mean
    10    147.3 MiB      0.0 MiB           1        mean_value = np.mean(random_array)
    11
    12    147.3 MiB      0.0 MiB           1        count = 0
    13    147.3 MiB      0.0 MiB         101        for i in range(100):
    14    147.3 MiB      0.0 MiB         100            count = count + 1
    15
    16    147.3 MiB      0.0 MiB           1        return mean_value
```

The line profiler output will look like this:

```none
Handler Name: return_mean
Python Runtime Version: 3.12
Extension Function ID: 1
Modules Profiled: ['return_mean_module']
Timer Unit: 0.001 s

Total Time: 0.229063 s
File: _udf_code.py
Function: return_mean at line 2

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     2                                           def return_mean():
     3         1        206.1    206.1     90.0      import numpy as np
     4
     5                                               # Generate a numpy array with 10 random integers between 1 and 100
     6                                               # np.random.randint(low, high, size)
     7         1         22.8     22.8     10.0      random_array = np.random.randint(1, 101, 10)
     8
     9                                               # Use a numpy function to calculate the mean
    10         1          0.1      0.1      0.0      mean_value = np.mean(random_array)
    11
    12         1          0.0      0.0      0.0      count = 0
    13       101          0.0      0.0      0.0      for i in range(100):
    14       100          0.0      0.0      0.0          count = count + 1
    15
    16         1          0.0      0.0      0.0      return mean_value
```
