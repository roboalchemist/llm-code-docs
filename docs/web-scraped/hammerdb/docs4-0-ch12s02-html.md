# Source: https://www.hammerdb.com/docs4.0/ch12s02.html

Title: 2. Installation and Configuration

URL Source: https://www.hammerdb.com/docs4.0/ch12s02.html

Markdown Content:
Before creating a test schema you should ensure that your database is configured to process analytic workloads instead of transactional.

### [](https://www.hammerdb.com/docs4.0/ch12s02.html)2.1.Oracle

When your database server is installed you should create a tablespace into which the test data will be installed allowing disk space according to the guide previously given in this document.

SQL> create tablespace tpchtab datafile size 20g;

Tablespace created.

When using parallel query ensure that the instance is configured for parallel execution, noting in particular the value for parallel_max_servers.

SQL> show parameter parallel
NAME                      TYPE        VALUE
------------------------------------ -----------
parallel_max_servers      integer    160
…
parallel_min_servers      integer    16
…
parallel_servers_target   integer    64
parallel_threads_per_cpu  integer    2

For testing purposes you can disable parallel execution in a particular environment by setting parallel_max_servers to a value of zero. An additional parameter that can provide significant benefit to the performance of parallel query workloads is optimizer_dynamic_sampling. By default this value is set to 2. Increasing this value to 4 has been shown to benefit query performance however testing the impact of changing this parameter should always be done during pre-testing as it may change between Oracle releases.

SQL> alter system set optimizer_dynamic_sampling=4;

System altered.

SQL> show parameter optimizer_dynamic

NAME                       TYPE       VALUE
------------------------------------ ----------- 
optimizer_dynamic_sampling integer    4

If using the In-Memory option ensure that the parameter inmemory_size has been configured and the database restarted.

SQL> show parameter inmemory

NAME                             TYPE        VALUE
-------------------------------------------- --------
inmemory_clause_defaultstring
inmemory_force                   string      DEFAULT
inmemory_max_populate_servers    integer     2
inmemory_query                   string      ENABLE
inmemory_size                    big integer 1500M
inmemory_trickle_repopulate      integer     1
_servers_percent    
optimizer_inmemory_aware         boolean     TRUE

Then alter the new tablespace containing the schema to be in-memory.

SQL> alter tablespace TPCHTAB default inmemory;
Tablespace altered.

As shown the objects created within the tablespace will now be configured to be in-memory.

SQL> select tablespace_name, def_inmemory from dba_tablespaces;

TABLESPACE_NAME           DEF_INME
------------------------- --------
SYSTEM                    DISABLED
SYSAUX                    DISABLED
TEMP                      DISABLED
USER                      DISABLED
TPCCTAB                   DISABLED
TPCHTAB                   ENABLED

For larger schemas both partitioning and compression settings (both standard and in-memory) should be considered for query tuning.

### [](https://www.hammerdb.com/docs4.0/ch12s02.html)2.2.SQL Server

For SQL Server ensure that the Max Degree of Parallelism is set to the maximum number of cores that you wish to process the queries.

**Figure 12.1.Max Degree of Parallelism**

![Image 1: Max Degree of Parallelism](https://www.hammerdb.com/docs4.0/resources/ch13-1.PNG)

### [](https://www.hammerdb.com/docs4.0/ch12s02.html)2.3.Db2

If using DB2 BLU use db2set to set the parameter DB2_WORKLOAD to ANALYTICS.

[db2inst1 ~]$ db2set DB2_WORKLOAD=ANALYTICS
[db2inst1 ~]$ db2stop force
25/05/2016 10:08:22     0   0   SQL1064N  DB2STOP processing was successful.
SQL1064N  DB2STOP processing was successful.
[db2inst1 ~]$ db2start
05/25/2016 10:08:27     0   0   SQL1063N  DB2START processing was successful.
SQL1063N  DB2START processing was successful.

In your db2cli.ini set the following parameter for each of the databases that you plan to create to test the TPROC-H workload, this will prevent failure due to SQLSTATE 01003 “Null values were eliminated from the argument of a column function” when running the workload thereby preventing the query set from completing.

[db2inst1 cfg]$ more db2cli.ini 
[TPCH]
IgnoreWarnList="'01003'"
[TPCH1]
IgnoreWarnList="'01003'"

When your database server is installed you should create a database into which the test data will be installed, for TPROC-H workloads a large pagesize is recommended.

[db2inst1 ~]$ db2 create database tpch pagesize 32 k
DB20000I  The CREATE DATABASE command completed successfully.

### [](https://www.hammerdb.com/docs4.0/ch12s02.html)2.4.PostgreSQL

The PostgreSQL Server should be at a minimum level of 9.6 that supports Parallel Query. The postgresql.conf file should include parallelism specific parameters such as follows:

work_mem = 1000MB                              
max_worker_processes = 16
max_parallel_workers_per_gather = 16
force_parallel_mode = on

### [](https://www.hammerdb.com/docs4.0/ch12s02.html)2.5.MySQL / MariaDB

To test analytic workloads on a MySQL compatible databases MariaDB columnstore is the solution that should be used. Note that this is a separate installation from a MySQL or MariaDB installation rather than a pluggable storage engine. As MariaDB columnstore is based on a columnstore solution called InfiniDB the relevant parameters start with infinidb, for example:

# Enable compression by default on create, set to 0 to turn off
infinidb_compression_type=2
# Default for string table threshhold
infinidb_stringtable_threshold=20
# infinidb local query flag
# infinidb_local_query=1
infinidb_diskjoin_smallsidelimit=0
infinidb_diskjoin_largesidelimit=0
infinidb_diskjoin_bucketsize=100
infinidb_um_mem_limit=64000
infinidb_use_import_for_batchinsert=1
infinidb_import_for_batchinsert_delimiter=7
