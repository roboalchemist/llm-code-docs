# Source: https://www.hammerdb.com/docs4.0/ch11s02.html

Title: 2. Running the Power and Throughput Test and Calculating the Geometric Mean

URL Source: https://www.hammerdb.com/docs4.0/ch11s02.html

Markdown Content:
The audited metric for TPC-H workloads is called QphH, however because of the differences in how these workloads are run, in particular using bulk operations for data loads it is not recommended that the QphH be calculated for HammerDB workloads. Instead it is recommended to measure and compare the geometric mean of the power and throughput test query times. For the audited results the following 3 aspects of the capability of the system to process queries are considered:

1.   Database size.

2.   Query processing power of queries in a single stream.

3.   Total query throughput of queries from multiple concurrent users.

For the multiple concurrent user tests the throughput test always follows the power test and the number of Virtual Users is based upon the following table where each Stream is processed by a Virtual User in HammerDB. This can also serve as a guide when running throughput tests with HammerDB taking the metric as the geomean of the query times of the slowest virtual user to complete the query set.

**Table 11.1.Query Streams and Scale Factors**

| SF ( Scale Factor ) | S (Streams) |
| --- | --- |
| 100000 | 11 |
| 30000 | 10 |
| 10000 | 9 |
| 3000 | 8 |
| 1000 | 7 |
| 300 | 6 |
| 100 | 5 |
| 30 | 4 |
| 10 | 3 |
| 1 | 2 |

There is also the availability for a simultaneous data refresh set. HammerDB provides full capabilities to run this refresh set both automatically as part of a Power test and concurrently with a Throughput test. Note however that once a refresh set is run the schema is required to be refreshed and it is prudent to backup and restore a HammerDB TPROC-H based schema where running a refresh set is planned.
