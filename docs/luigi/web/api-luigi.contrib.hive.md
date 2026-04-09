# luigi.contrib.hive

Functions

`get_default_client`()

`get_hive_syntax`()

`get_hive_warehouse_location`()

`get_ignored_file_masks`()

`load_hive_cmd`()

`run_hive`(args[, check_return_code])

Runs the hive from the command line, passing in the given args, and returning stdout.

`run_hive_cmd`(hivecmd[, check_return_code])

Runs the given hive query and returns stdout.

`run_hive_script`(script)

Runs the contents of the given script in hive and returns stdout.

Classes

`ApacheHiveCommandClient`()

A subclass for the HiveCommandClient to (in some cases) ignore the return code from the hive command so that we can just parse the output.

`ExternalHiveTask`(*args, **kwargs)

External task that depends on a Hive table/partition.

`HiveClient`()

`HiveCommandClient`()

Uses hive invocations to find information.

`HivePartitionTarget`(table, partition[, ...])

Target representing Hive table or Hive partition

`HiveQueryRunner`()

Runs a HiveQueryTask by shelling out to hive.

`HiveQueryTask`(*args, **kwargs)

Task to run a hive query.

`HiveTableTarget`(table[, database, client])

Target representing non-partitioned table

`HiveThriftContext`()

Context manager for hive metastore client.

`MetastoreClient`()

`WarehouseHiveClient`([hdfs_client, ...])

Client for managed tables that makes decision based on presence of directory in hdfs

Exceptions

`HiveCommandError`(message[, out, err])

exception luigi.contrib.hive.HiveCommandError(*message*, *out=None*, *err=None*)

luigi.contrib.hive.load_hive_cmd()

luigi.contrib.hive.get_hive_syntax()

luigi.contrib.hive.get_hive_warehouse_location()

luigi.contrib.hive.get_ignored_file_masks()

luigi.contrib.hive.run_hive(*args*, *check_return_code=True*)

Runs the hive from the command line, passing in the given args, and
returning stdout.

With the apache release of Hive, so of the table existence checks
(which are done using DESCRIBE do not exit with a return code of 0
so we need an option to ignore the return code and just return stdout for parsing

luigi.contrib.hive.run_hive_cmd(*hivecmd*, *check_return_code=True*)

Runs the given hive query and returns stdout.

luigi.contrib.hive.run_hive_script(*script*)

Runs the contents of the given script in hive and returns stdout.

class luigi.contrib.hive.HiveClient

abstractmethod table_location(*table*, *database='default'*, *partition=None*)

Returns location of db.table (or db.table.partition). partition is a dict of partition key to
value.

abstractmethod table_schema(*table*, *database='default'*)

Returns list of [(name, type)] for each column in database.table.

abstractmethod table_exists(*table*, *database='default'*, *partition=None*)

Returns true if db.table (or db.table.partition) exists. partition is a dict of partition key to
value.

abstractmethod partition_spec(*partition*)

Turn a dict into a string partition specification

class luigi.contrib.hive.HiveCommandClient

Uses hive invocations to find information.

table_location(*table*, *database='default'*, *partition=None*)

Returns location of db.table (or db.table.partition). partition is a dict of partition key to
value.

table_exists(*table*, *database='default'*, *partition=None*)

Returns true if db.table (or db.table.partition) exists. partition is a dict of partition key to
value.

table_schema(*table*, *database='default'*)

Returns list of [(name, type)] for each column in database.table.

partition_spec(*partition*)

Turns a dict into the a Hive partition specification string.

class luigi.contrib.hive.ApacheHiveCommandClient

A subclass for the HiveCommandClient to (in some cases) ignore the return code from
the hive command so that we can just parse the output.

table_schema(*table*, *database='default'*)

Returns list of [(name, type)] for each column in database.table.

class luigi.contrib.hive.MetastoreClient

table_location(*table*, *database='default'*, *partition=None*)

Returns location of db.table (or db.table.partition). partition is a dict of partition key to
value.

table_exists(*table*, *database='default'*, *partition=None*)

Returns true if db.table (or db.table.partition) exists. partition is a dict of partition key to
value.

table_schema(*table*, *database='default'*)

Returns list of [(name, type)] for each column in database.table.

partition_spec(*partition*)

Turn a dict into a string partition specification

class luigi.contrib.hive.HiveThriftContext

Context manager for hive metastore client.

class luigi.contrib.hive.WarehouseHiveClient(*hdfs_client=None*, *warehouse_location=None*)

Client for managed tables that makes decision based on presence of directory in hdfs

table_schema(*table*, *database='default'*)

Returns list of [(name, type)] for each column in database.table.

table_location(*table*, *database='default'*, *partition=None*)

Returns location of db.table (or db.table.partition). partition is a dict of partition key to
value.

table_exists(*table*, *database='default'*, *partition=None*)

The table/partition is considered existing if corresponding path in hdfs exists
and contains file except those which match pattern set in  ignored_file_masks

partition_spec(*partition*)

Turn a dict into a string partition specification

luigi.contrib.hive.get_default_client()

class luigi.contrib.hive.HiveQueryTask(**args*, ***kwargs*)

Task to run a hive query.

n_reduce_tasks = None

bytes_per_reducer = None

reducers_max = None

abstractmethod query()

Text of query to run in hive

hiverc()

Location of an rc file to run before the query
if hiverc-location key is specified in luigi.cfg, will default to the value there
otherwise returns None.

Returning a list of rc files will load all of them in order.

hivevars()

Returns a dict of key=value settings to be passed along
to the hive command line via –hivevar.
This option can be used as a separated namespace for script local variables.
See https://cwiki.apache.org/confluence/display/Hive/LanguageManual+VariableSubstitution

hiveconfs()

Returns a dict of key=value settings to be passed along
to the hive command line via –hiveconf. By default, sets
mapred.job.name to task_id and if not None, sets:

- 

mapred.reduce.tasks (n_reduce_tasks)

- 

mapred.fairscheduler.pool (pool) or mapred.job.queue.name (pool)

- 

hive.exec.reducers.bytes.per.reducer (bytes_per_reducer)

- 

hive.exec.reducers.max (reducers_max)

job_runner()

class luigi.contrib.hive.HiveQueryRunner

Runs a HiveQueryTask by shelling out to hive.

prepare_outputs(*job*)

Called before job is started.

If output is a FileSystemTarget, create parent directories so the hive command won’t fail

get_arglist(*f_name*, *job*)

run_job(*job*, *tracking_url_callback=None*)

The type of the NotImplemented singleton.

class luigi.contrib.hive.HivePartitionTarget(*table*, *partition*, *database='default'*, *fail_missing_table=True*, *client=None*)

Target representing Hive table or Hive partition

@param table: Table name
@type table: str
@param partition: partition specificaton in form of
dict of {“partition_column_1”: “partition_value_1”, “partition_column_2”: “partition_value_2”, … }
If partition is None or {} then target is Hive nonpartitioned table
@param database: Database name
@param fail_missing_table: flag to ignore errors raised due to table nonexistence
@param client: HiveCommandClient instance. Default if client is None

exists()

returns True if the partition/table exists

property path

Returns the path for this HiveTablePartitionTarget’s data.

class luigi.contrib.hive.HiveTableTarget(*table*, *database='default'*, *client=None*)

Target representing non-partitioned table

@param table: Table name
@type table: str
@param partition: partition specificaton in form of
dict of {“partition_column_1”: “partition_value_1”, “partition_column_2”: “partition_value_2”, … }
If partition is None or {} then target is Hive nonpartitioned table
@param database: Database name
@param fail_missing_table: flag to ignore errors raised due to table nonexistence
@param client: HiveCommandClient instance. Default if client is None

class luigi.contrib.hive.ExternalHiveTask(**args*, ***kwargs*)

External task that depends on a Hive table/partition.

database

Parameter whose value is a `str`, and a base class for other parameter types.

Parameters are objects set on the Task class level to make it possible to parameterize tasks.
For instance:

```
class MyTask(luigi.Task):
    foo = luigi.Parameter()

class RequiringTask(luigi.Task):
    def requires(self):
        return MyTask(foo="hello")

    def run(self):
        print(self.requires().foo)  # prints "hello"

```