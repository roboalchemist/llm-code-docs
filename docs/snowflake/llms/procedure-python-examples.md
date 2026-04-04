# Source: https://docs.snowflake.com/en/developer-guide/stored-procedure/python/procedure-python-examples.md

# Python handler examples for stored procedures

## Running concurrent tasks with worker processes

You can run concurrent tasks using Python worker processes. You might find this useful when you need to run parallel tasks that take
advantage of multiple CPU cores on warehouse nodes.

> **Note:**
>
> Snowflake recommends that you not use the built-in Python multiprocessing module.

To work around cases where the [Python Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) prevents a
multi-tasking approach from scaling across all CPU cores, you can execute concurrent tasks using separate worker processes, rather than threads.

You can do this on Snowflake warehouses by using the `joblib` library’s `Parallel` class, as in the following example.

```sqlexample-python
CREATE OR REPLACE PROCEDURE joblib_multiprocessing_proc(i INT)
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION = 3.12
  HANDLER = 'joblib_multiprocessing'
  PACKAGES = ('snowflake-snowpark-python', 'joblib')
AS $$
import joblib
from math import sqrt

def joblib_multiprocessing(session, i):
  result = joblib.Parallel(n_jobs=-1)(joblib.delayed(sqrt)(i ** 2) for i in range(10))
  return str(result)
$$;
```

> **Note:**
>
> The default backend used for `joblib.Parallel` differs between Snowflake standard and Snowpark-optimized warehouses.
>
> * Standard warehouse default: `threading`
> * Snowpark-optimized warehouse default: `loky` (multiprocessing)
>
> You can override the default backend setting by calling the `joblib.parallel_backend` function, as in the following example.
>
> ```python
> import joblib
> joblib.parallel_backend('loky')
> ```

## Using Snowpark APIs for asynchrononous processing

The following examples illustrate how you can use Snowpark APIs to begin asynchronous child jobs, as well as how those jobs behave under
different conditions.

### Checking the status of an asynchronous child job

In the following example, the `checkStatus` procedure executes an asynchronous child job that waits 60 seconds. The procedure then
checks on the status of the job before it can have finished, so the check returns `False`.

```sqlexample-python
CREATE OR REPLACE PROCEDURE checkStatus()
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = 3.12
PACKAGES = ('snowflake-snowpark-python')
HANDLER='async_handler'
EXECUTE AS CALLER
AS $$
def async_handler(session):
    async_job = session.sql("select system$wait(60)").collect_nowait()
    return async_job.is_done()
$$;
```

The following code calls the procedure.

```sqlexample
CALL checkStatus();
```

```output
+-------------+
| checkStatus |
|-------------|
| False       |
+-------------+
```

### Cancelling an asynchronous child job

In the following example, the `cancelJob` procedure uses SQL to insert data into the `test_tb` table with an asynchronous
child job that would take 10 seconds to finish. It then cancels the child job before it finishes and the data has been inserted.

```sqlexample
CREATE OR REPLACE TABLE test_tb(c1 STRING);
```

```sqlexample-python
CREATE OR REPLACE PROCEDURE cancelJob()
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = 3.12
PACKAGES = ('snowflake-snowpark-python')
HANDLER = 'async_handler'
EXECUTE AS OWNER
AS $$
def async_handler(session):
    async_job = session.sql("insert into test_tb (select system$wait(10))").collect_nowait()
    return async_job.cancel()
$$;

CALL cancelJob();
```

The following code queries the `test_tb` table, but returns no results because no data has been inserted.

```sqlexample
SELECT * FROM test_tb;
```

```output
+----+
| C1 |
|----|
+----+
```

### Waiting and blocking while an asynchronous child job runs

In the following example, the `blockUntilDone` procedure executes an asynchronous child job that takes 5 seconds to finish. Using
the `snowflake.snowpark.AsyncJob.result` method, the procedure waits and returns when the job has finished.

```sqlexample-python
CREATE OR REPLACE PROCEDURE blockUntilDone()
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = 3.12
PACKAGES = ('snowflake-snowpark-python')
HANDLER='async_handler'
EXECUTE AS CALLER
AS $$
def async_handler(session):
    async_job = session.sql("select system$wait(5)").collect_nowait()
    return async_job.result()
$$;
```

The following code calls the `blockUntilDone` procedure, which returns after waiting 5 seconds.

```sqlexample
CALL blockUntilDone();
```

```output
+------------------------------------------+
| blockUntilDone                               |
|------------------------------------------|
| [Row(SYSTEM$WAIT(5)='waited 5 seconds')] |
+------------------------------------------+
```

### Returning an error after requesting results from an unfinished asynchronous child job

In the following example, the `earlyReturn` procedure executes an asynchronous child job that takes 60 seconds to finish. The
procedure then attempts to return a `DataFrame` from the job’s result before it can have finished. The result is an error.

```sqlexample-python
CREATE OR REPLACE PROCEDURE earlyReturn()
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = 3.12
PACKAGES = ('snowflake-snowpark-python')
HANDLER='async_handler'
EXECUTE AS CALLER
AS $$
def async_handler(session):
    async_job = session.sql("select system$wait(60)").collect_nowait()
    df = async_job.to_df()
    try:
        df.collect()
    except Exception as ex:
        return 'Error: (02000): Result for query <UUID> has expired'
$$;
```

The following code calls the `earlyReturn` procedure, returning the error.

```sqlexample
CALL earlyReturn();
```

```output
+------------------------------------------------------------+
| earlyReturn                                                 |
|------------------------------------------------------------|
| Error: (02000): Result for query <UUID> has expired        |
+------------------------------------------------------------+
```

### Finishing a parent job before a child job finishes, canceling the child job

In the following example, the `earlyCancelJob` procedure executes an asynchronous child job to insert data into a table and takes 10
seconds to finish. However, the parent job — `async_handler` — returns before the child job finishes, which cancels the child job.

```sqlexample-python
CREATE OR REPLACE PROCEDURE earlyCancelJob()
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = 3.12
PACKAGES = ('snowflake-snowpark-python')
HANDLER='async_handler'
EXECUTE AS OWNER
AS $$
def async_handler(session):
    async_job = session.sql("insert into test_tb (select system$wait(10))").collect_nowait()
$$;
```

The following code calls the `earlyCancelJob` procedure. It then queries the `test_tb` table, which returns no result because
no data was inserted by the canceled child job.

```sqlexample
CALL earlyCancelJob();
SELECT * FROM test_tb;
```

```output
+----+
| C1 |
|----|
+----+
```
