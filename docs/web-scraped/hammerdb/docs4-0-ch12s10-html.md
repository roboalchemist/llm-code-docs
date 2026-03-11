# Source: https://www.hammerdb.com/docs4.0/ch12s10.html

Title: 10. Run a Throughput Test

URL Source: https://www.hammerdb.com/docs4.0/ch12s10.html

Markdown Content:
10.Run a Throughput Test
===============

| 10.Run a Throughput Test |
| :---: |
| [Prev](https://www.hammerdb.com/docs4.0/ch12s09.html) | Chapter 12.How to Run an Analytic Workload | [Next](https://www.hammerdb.com/docs4.0/ch12s11.html) |

* * *

[](https://www.hammerdb.com/docs4.0/ch12s10.html)10.Run a Throughput Test
-------------------------------------------------------------------------

After the power test you should run the throughput test (if the refresh function has been run it is necessary to refresh the schema). For the throughput test you need to also run the refresh function however this time the aim is to trickle the refresh function slowly while multiple query streams are run. Configure the options as for the Power Test and enable the refresh function, this time the update sets, trickle refresh and REFRESH_VERBOSE options will also be enabled when refresh_on is set to true. Configure the correct number of Virtual Users to enable the first Virtual User to run the Refresh Functions and additional Virtual Users to run the Query Streams as defined in the specification for the test. For the example below at Scale Factor 10 there are 3 Virtual Users to run the queries and 1 to run the refresh. Note that the Refresh Function will run more slowly as expected and all of the Virtual Users run the queries in a different order.

[](https://www.hammerdb.com/docs4.0/ch12s10.html)
**Figure 12.29.Throughput Test**

![Image 1: Throughput Test](https://www.hammerdb.com/docs4.0/resources/ch13-30.PNG)

### [](https://www.hammerdb.com/docs4.0/ch12s10.html)10.1.SQL Server Snapshot Isolation

Note that before running a long running query at the same time as the inserts of the refresh function you should enable snapshot isolation on the database. Failure to do so will mean the Query streams will hang under a shared lock (LCK_M_S) whilst the refresh function is running.

[](https://www.hammerdb.com/docs4.0/ch12s10.html)
**Figure 12.30.Enable Snapshot Isolation**

![Image 2: Enable Snapshot Isolation](https://www.hammerdb.com/docs4.0/resources/ch13-31.PNG)

Once set the refresh and queries will run as expected. If you observe foreign key or constraint violation errors after having restored a schema verify the scale factor in the driver script is set to the same value as the scale factor of the schema you have restored.

[](https://www.hammerdb.com/docs4.0/ch12s10.html)
**Figure 12.31.SQL Server with Snapshot Isolation**

![Image 3: SQL Server with Snapshot Isolation](https://www.hammerdb.com/docs4.0/resources/ch13-32.PNG)

When the Virtual Users running the Query sets have completed the throughput tests, note the longest (not the shortest) time taken for a full query set to complete. You do not need to wait for the trickled refresh function to complete, however must have configured enough update sets to ensure that the refresh function remains running whilst the throughput test completes.

[](https://www.hammerdb.com/docs4.0/ch12s10.html)
**Figure 12.32.Throughput test complete**

![Image 4: Throughput test complete](https://www.hammerdb.com/docs4.0/resources/ch13-33.PNG)

* * *

[Prev](https://www.hammerdb.com/docs4.0/ch12s09.html)[Up](https://www.hammerdb.com/docs4.0/ch12.html)[Next](https://www.hammerdb.com/docs4.0/ch12s11.html)
9.Run a Power Test[Home](https://www.hammerdb.com/docs4.0/index.html)11.Calculate the Geometric Mean
