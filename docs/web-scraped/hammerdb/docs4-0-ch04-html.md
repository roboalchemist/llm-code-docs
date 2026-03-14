# Source: https://www.hammerdb.com/docs4.0/ch04.html

Title: Chapter 4. How to Run a TPROC-C Workload

URL Source: https://www.hammerdb.com/docs4.0/ch04.html

Markdown Content:
Chapter 4.How to Run a TPROC-C Workload
===============

| Chapter 4.How to Run a TPROC-C Workload |
| :---: |
| [Prev](https://www.hammerdb.com/docs4.0/ch03s08.html) |  | [Next](https://www.hammerdb.com/docs4.0/ch04s01.html) |

* * *

[](https://www.hammerdb.com/docs4.0/ch04.html)Chapter 4.How to Run a TPROC-C Workload
=====================================================================================

**Table of Contents**

[1. Test Network Configuration](https://www.hammerdb.com/docs4.0/ch04s01.html)[1.1. SUT Database Server Configuration](https://www.hammerdb.com/docs4.0/ch04s01.html#d0e847)[1.2. Load Generation Server Configuration](https://www.hammerdb.com/docs4.0/ch04s01.html#d0e852)[1.3. CPU Single-Threaded Performance Calibration](https://www.hammerdb.com/docs4.0/ch04s01.html#d0e857)[1.4. Administrator PC Configuration](https://www.hammerdb.com/docs4.0/ch04s01.html#d0e886)[2. Installation and Configuration](https://www.hammerdb.com/docs4.0/ch04s02.html)[2.1. Oracle](https://www.hammerdb.com/docs4.0/ch04s02.html#d0e896)[2.2. Microsoft SQL Server](https://www.hammerdb.com/docs4.0/ch04s02.html#d0e913)[2.3. Db2](https://www.hammerdb.com/docs4.0/ch04s02.html#d0e924)[2.4. MySQL](https://www.hammerdb.com/docs4.0/ch04s02.html#d0e943)[2.5. PostgreSQL](https://www.hammerdb.com/docs4.0/ch04s02.html#d0e966)[3. Configuring Schema Build Options](https://www.hammerdb.com/docs4.0/ch04s03.html)[3.1. Oracle Schema Build Options](https://www.hammerdb.com/docs4.0/ch04s03.html#d0e996)[3.2. Microsoft SQL Server Schema Build Options](https://www.hammerdb.com/docs4.0/ch04s03.html#d0e1082)[3.2.1. In-Memory Optimized Tables](https://www.hammerdb.com/docs4.0/ch04s03.html#d0e1087)[3.2.2. Build Options](https://www.hammerdb.com/docs4.0/ch04s03.html#d0e1114)[3.3. Db2 Schema Build Options](https://www.hammerdb.com/docs4.0/ch04s03.html#d0e1206)[3.4. MySQL Schema Build Options](https://www.hammerdb.com/docs4.0/ch04s03.html#d0e1269)[3.5. PostgreSQL Schema Build Options](https://www.hammerdb.com/docs4.0/ch04s03.html#d0e1340)[4. Creating the Schema](https://www.hammerdb.com/docs4.0/ch04s04.html)[4.1. Deleting or Verifying the Oracle Schema](https://www.hammerdb.com/docs4.0/ch04s04.html#d0e1464)[4.2. Deleting or Verifying the SQL Server Schema and In-memory Schema](https://www.hammerdb.com/docs4.0/ch04s04.html#d0e1480)[4.3. Deleting or Verifying the Db2 Schema](https://www.hammerdb.com/docs4.0/ch04s04.html#d0e1509)[4.4. Deleting or Verifying the MySQL Schema](https://www.hammerdb.com/docs4.0/ch04s04.html#d0e1520)[4.5. Deleting or Verifying the PostgreSQL Schema](https://www.hammerdb.com/docs4.0/ch04s04.html#d0e1531)[5. Configuring Driver Script options](https://www.hammerdb.com/docs4.0/ch04s05.html)[6. Advanced Driver Script Options](https://www.hammerdb.com/docs4.0/ch04s06.html)[6.1. Use All Warehouses for increased I/O](https://www.hammerdb.com/docs4.0/ch04s06.html#d0e1653)[6.2. Time Profile for measuring Response Times](https://www.hammerdb.com/docs4.0/ch04s06.html#d0e1676)[6.3. Event Driven Scaling for Keying and Thinking Times](https://www.hammerdb.com/docs4.0/ch04s06.html#d0e1716)[6.4. XML Connect Pool for Cluster Testing](https://www.hammerdb.com/docs4.0/ch04s06.html#d0e1777)[7. Additional Driver Script Options for Stored Procedures and Server Side Reports: PostgreSQL, MySQL, Oracle, Db2 and EnterpriseDB PostgreSQL](https://www.hammerdb.com/docs4.0/ch04s07.html)[7.1. PostgreSQL Stored Procedures](https://www.hammerdb.com/docs4.0/ch04s07.html#d0e1829)[7.2. MySQL Prepare Statements](https://www.hammerdb.com/docs4.0/ch04s07.html#d0e1834)[7.3. Oracle AWR Reports](https://www.hammerdb.com/docs4.0/ch04s07.html#d0e1839)[7.4. Db2 MONREPORT](https://www.hammerdb.com/docs4.0/ch04s07.html#d0e1844)[7.5. EnterpriseDB PostgreSQL DRITA](https://www.hammerdb.com/docs4.0/ch04s07.html#d0e1849)[8. Loading the Driver Script](https://www.hammerdb.com/docs4.0/ch04s08.html)[9. Configure Virtual Users](https://www.hammerdb.com/docs4.0/ch04s09.html)[10. Create and Run Virtual Users](https://www.hammerdb.com/docs4.0/ch04s10.html)

This Chapter provides a general overview on the HammerDB TPROC-C workload and gives you an introduction to conducting OLTP (Online Transaction Processing) workloads on all of the supported databases. This will equip you with the essentials for assessing the ability of any system for processing transactional workloads.

* * *

[Prev](https://www.hammerdb.com/docs4.0/ch03s08.html)[Next](https://www.hammerdb.com/docs4.0/ch04s01.html)
8.Publishing database performance results[Home](https://www.hammerdb.com/docs4.0/index.html)1.Test Network Configuration
