# Source: https://www.hammerdb.com/docs4.0/ch06s01.html

Title: 1. Oracle Transaction Counter

URL Source: https://www.hammerdb.com/docs4.0/ch06s01.html

Markdown Content:
For Oracle the connection parameters are the same as the schema options. There is also an option to query a TimesTen database instead of an Oracle one and to select transactions from an Oracle RAC cluster. The refresh rate determines the sampling interval.

**Figure 6.2.Oracle TX Counter Options**

![Image 1: Oracle TX Counter Options](https://www.hammerdb.com/docs4.0/resources/ch6-2.PNG)

For single instance Oracle, transactions are sampled with the following statement. This displays transactions with the same value as used in Oracle Enterprise Manager and in Oracle AWR reports.

select sum(value) from v$sysstat where name = 'user commits' or name = 'user rollbacks'
For Oracle RAC gv$sysstat is queried for global transactions.

select sum(value) from gv$sysstat where name = 'user commits' or name = 'user rollbacks'
for TimesTen the following SQL is used.

select (xact_commits + xact_rollbacks) from sys.monitor
