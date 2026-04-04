# Source: https://www.hammerdb.com/docs4.0/ch04s07.html

Title: 7. Additional Driver Script Options for Stored Procedures and Server Side Reports: PostgreSQL, MySQL, Oracle, Db2 and EnterpriseDB PostgreSQL

URL Source: https://www.hammerdb.com/docs4.0/ch04s07.html

Markdown Content:
### [](https://www.hammerdb.com/docs4.0/ch04s07.html)7.1.PostgreSQL Stored Procedures

With PostgreSQL by default the 5 TPROC-C transactions are implemented using PostgreSQL functions. From PostgreSQL v11.0 there is the option to use PostgreSQL stored procedures instead. However prepared statements are not supported by PostgreSQL for stored procedures only for functions and therefore if using the XML connect pool feature only PostgreSQL functions are supported.

### [](https://www.hammerdb.com/docs4.0/ch04s07.html)7.2.MySQL Prepare Statements

With MySQL there is the option to use server side prepared statements. This option is mandatory if using the XML connect pool feature.

### [](https://www.hammerdb.com/docs4.0/ch04s07.html)7.3.Oracle AWR Reports

The Generation of Oracle AWR reports is built-in functionality with the Oracle Timed Test. At the end of the test HammerDB will report the snapshot numbers between which the report corresponds to the test.

### [](https://www.hammerdb.com/docs4.0/ch04s07.html)7.4.Db2 MONREPORT

In the Db2 driver script options the Minutes for Test Duration is shown as monreportinterval in the Driver Script. This defines the period of time taken from the minutes for test duration that the monitoring user runs a monreport capture. The results are output at the end of the test and therefore selecting this option should be done in conjunction with the logfile enabled. While the MONREPORT is being captured the monitoring virtual user cannot bet terminated as control is handed over to the DB2 database and therefore shorter periods of report are optimal. In all cases in the MONREPORT interval specified is longer than the minutes for test duration then no MONREPORT will be captured.

### [](https://www.hammerdb.com/docs4.0/ch04s07.html)7.5.EnterpriseDB PostgreSQL DRITA

If you have Enterprise DB installed and DRITA functionality enabled, by selecting this option HammerDB will automatically take DRITA snapshots for performance analysis of the workload between tests. For DRITA functionality to work you need the parameter timed_statistics = on set in your postgresql.conf file. With the test complete and the values you recorded if you selected the DRITA option you should next generate the DRITA report that corresponds to the reported SNAPIDs to show the PostgreSQL wait events, in the example below snapshots 2 and 3.

edb=# select * from sys_rpt(2,3,1000);
                                   sys_rpt                                   
-----------------------------------------------------------------------------
 WAIT NAME                                COUNT      WAIT TIME       % WAIT
 ---------------------------------------------------------------------------
 wal insert lock acquire                  1054357    2.300713        88.25
 xid gen lock acquire                     83471      0.195263        7.49
 db file read                             5523       0.067953        2.61
 buffer free list lock acquire            11133      0.029317        1.12
 query plan                               205        0.013703        0.53
 freespace lock acquire                   3          0.000007        0.00
 rel cache init lock acquire              0          0.000000        0.00
(9 rows)

edb=#
