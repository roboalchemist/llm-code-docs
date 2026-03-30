# Source: https://www.hammerdb.com/docs4.0/ch11s03.html

Title: 3. Choosing a Database for running TPROC-H workloads

URL Source: https://www.hammerdb.com/docs4.0/ch11s03.html

Markdown Content:
TPROC-H workloads run complex queries scanning large volumes of data and therefore require the use of database features such as parallel query and in-memory column stores to maximise performance. With the available HammerDB TPROC-H based workloads the three databases that support these features are the Enterprise Editions of Oracle, SQL Server and Db2 and therefore these databases will deliver the best experience for building and running TPROC-H. Over time there has been improvement with open-source and open-source derived databases in the ability to run TPROC-H workloads. For example PostgreSQL supports Parallel Query and the PostgreSQL derived versions of Amazon Redshift and Greenplum offer further accelerated query solutions. MySQL does not support an analytic storage engine however the MariaDB column store storage is best suited for running analytic tests against MySQL. Nevertheless it is known that with some or all of the open source solutions a number of queries either fail or are extremely long running due to the limitations of the databases themselves (and not HammerDB) in optimizing the queries.

### [](https://www.hammerdb.com/docs4.0/ch11s03.html)3.1.Oracle

The Oracle database is fully featured for running TPROC-H based workloads and presents two options for configuring the database either row oriented parallel query or the In-Memory Column Store (IM column store). Both of these configurations are able to run a full TPROC-H workload and are configured on the database as opposed to configuring with HammerDB.

### [](https://www.hammerdb.com/docs4.0/ch11s03.html)3.2.Microsoft SQL Server

SQL Server is able to support a full TPROC-H workload and offers row oriented parallel query as well as in-memory column store configured. The clustered columnstore build is selected through the HammerDB Build Options.

**Figure 11.3.Clustered Columnstore**

![Image 1: Clustered Columnstore](https://www.hammerdb.com/docs4.0/resources/ch9-9.PNG)

### [](https://www.hammerdb.com/docs4.0/ch11s03.html)3.3.Db2

Db2 can support a full TPCH workload through row oriented parallel query and Db2 BLU in-memory column store. The column store is selected through the Db2 Organize by options.

**Figure 11.4.Db2 Organize By**

![Image 2: Db2 Organize By](https://www.hammerdb.com/docs4.0/resources/ch9-10.PNG)

### [](https://www.hammerdb.com/docs4.0/ch11s03.html)3.4.PostgreSQL

PostgreSQL supports standard row oriented parallel query. This offers significant performance improvement over single-threaded queries however not all queries at all schema sizes are expected to complete without database error and some run for a significant length of time. Options are also available to run the PostgreSQL queries against a Greenplum database. It is important to be aware that because of the Greenplum MPP architecture there is significant overhead in processing INSERT operations and therefore data should be loaded in bulk after generating with the HammerDB datagen operation.

**Figure 11.5.PostgreSQL TPROC-H**

![Image 3: PostgreSQL TPROC-H](https://www.hammerdb.com/docs4.0/resources/ch9-11.PNG)

### [](https://www.hammerdb.com/docs4.0/ch11s03.html)3.5.MySQL / MariaDB

MySQL does not support row oriented parallel query or a column store configuration and therefore queries run against a MySQL database are expected to be long-running. However the MySQL compatible MariaDB supports a separate installation of a column store based database which offers significantly improved query times. However some queries will result in database errors or long running queries. This option is selected with the Data Warehouse Storage Engine Option.

**Figure 11.6.MySQL MariaDB TPROC-H**

![Image 4: MySQL MariaDB TPROC-H](https://www.hammerdb.com/docs4.0/resources/ch9-12.PNG)
