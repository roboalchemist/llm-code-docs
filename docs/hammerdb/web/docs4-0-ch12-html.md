# Source: https://www.hammerdb.com/docs4.0/ch12.html

Title: Chapter 12. How to Run an Analytic Workload

URL Source: https://www.hammerdb.com/docs4.0/ch12.html

Markdown Content:
Chapter 12.How to Run an Analytic Workload
===============

| Chapter 12.How to Run an Analytic Workload |
| :---: |
| [Prev](https://www.hammerdb.com/docs4.0/ch11s04.html) |  | [Next](https://www.hammerdb.com/docs4.0/ch12s01.html) |

* * *

[](https://www.hammerdb.com/docs4.0/ch12.html)Chapter 12.How to Run an Analytic Workload
========================================================================================

**Table of Contents**

[1. SUT Database Server Configuration](https://www.hammerdb.com/docs4.0/ch12s01.html)[2. Installation and Configuration](https://www.hammerdb.com/docs4.0/ch12s02.html)[2.1. Oracle](https://www.hammerdb.com/docs4.0/ch12s02.html#d0e3140)[2.2. SQL Server](https://www.hammerdb.com/docs4.0/ch12s02.html#d0e3170)[2.3. Db2](https://www.hammerdb.com/docs4.0/ch12s02.html#d0e3181)[2.4. PostgreSQL](https://www.hammerdb.com/docs4.0/ch12s02.html#d0e3196)[2.5. MySQL / MariaDB](https://www.hammerdb.com/docs4.0/ch12s02.html#d0e3203)[3. Configuring Schema Build Options](https://www.hammerdb.com/docs4.0/ch12s03.html)[3.1. Oracle Schema Build Options](https://www.hammerdb.com/docs4.0/ch12s03.html#d0e3233)[3.2. SQL Server Schema Build Options](https://www.hammerdb.com/docs4.0/ch12s03.html#d0e3304)[3.3. Db2 Schema Build Options](https://www.hammerdb.com/docs4.0/ch12s03.html#d0e3390)[3.4. MySQL Schema Build Options](https://www.hammerdb.com/docs4.0/ch12s03.html#d0e3446)[3.5. PostgreSQL Schema Build Options](https://www.hammerdb.com/docs4.0/ch12s03.html#d0e3508)[4. Creating the Schema](https://www.hammerdb.com/docs4.0/ch12s04.html)[4.1. Verifying and Backing-Up the Oracle Schema](https://www.hammerdb.com/docs4.0/ch12s04.html#d0e3624)[4.2. Verifying and Backing Up the SQL Server Schema](https://www.hammerdb.com/docs4.0/ch12s04.html#d0e3655)[4.3. Verifying and Backing up the Db2 Schema](https://www.hammerdb.com/docs4.0/ch12s04.html#d0e3694)[4.4. Verifying and Backing up the MySQL Schema](https://www.hammerdb.com/docs4.0/ch12s04.html#d0e3713)[4.5. Verifying and Backing up the PostgreSQL Schema](https://www.hammerdb.com/docs4.0/ch12s04.html#d0e3724)[5. Configuring Driver Script Options](https://www.hammerdb.com/docs4.0/ch12s05.html)[6. Loading the Driver Script](https://www.hammerdb.com/docs4.0/ch12s06.html)[7. Configure Virtual Users](https://www.hammerdb.com/docs4.0/ch12s07.html)[8. Run a Single Virtual User Test](https://www.hammerdb.com/docs4.0/ch12s08.html)[8.1. Changing the Query Order](https://www.hammerdb.com/docs4.0/ch12s08.html#d0e3931)[9. Run a Power Test](https://www.hammerdb.com/docs4.0/ch12s09.html)[10. Run a Throughput Test](https://www.hammerdb.com/docs4.0/ch12s10.html)[10.1. SQL Server Snapshot Isolation](https://www.hammerdb.com/docs4.0/ch12s10.html#d0e3998)[11. Calculate the Geometric Mean](https://www.hammerdb.com/docs4.0/ch12s11.html)

The basis of Analytic or Decision Support Systems is the ability to process complex ad-hoc queries on large volumes of data. Processing this amount of data within a single process or thread on traditional row-oriented database is time consuming. Consequently it is beneficial Parallel Query to break down such queries into multiple sub tasks to complex the query more quickly. Additional features such as compression and partitioning are also used with Parallel Query to improve performance. As a consequence when planning analytic workloads for optimal performance you should consider the database features for in-memory and parallel execution configuration. In similarity to the HammerDB OLTP workload, HammerDB implements a fair usage of a TPC workload however the results should not be compared to official published TPC-H results in any way.

* * *

[Prev](https://www.hammerdb.com/docs4.0/ch11s04.html)[Next](https://www.hammerdb.com/docs4.0/ch12s01.html)
4.Benchmarking Database Cloud Services[Home](https://www.hammerdb.com/docs4.0/index.html)1.SUT Database Server Configuration
