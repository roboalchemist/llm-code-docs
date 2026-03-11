# Source: https://www.hammerdb.com/docs4.0/ch11s01.html

Title: 1. What is TPROC-H derived from TPC-H?

URL Source: https://www.hammerdb.com/docs4.0/ch11s01.html

Markdown Content:
To complement the OLTP type TPROC-C workload HammerDB also contains a Fair Use derivation of the decision support based TPC-H Benchmark Standard. The HammerDB TPROC-H workload is an open source workload derived from the TPC-H Benchmark Standard and as such is not comparable to published TPC-H results, as the results do not comply with the TPC-H Benchmark Standard. TPROC-H in simple terms can be thought of as complementing the workload implemented in TPROC-C related to the activities of a wholesale supplier. However, whereas TPROC-C simulates an online ordering system TPROC-H represents the typical workload of a retailer running analytical queries about their operations. To do this TPROC-H is represented by a set of business focused ad-hoc queries (in addition to concurrent data updates and deletes) and is measured upon the time it takes to complete these queries. In particular the focus is upon highly complex queries that require the processing of large volumes of data. Also in similarity to TPROC-C the schema size is not fixed and is dependent upon a Scale Factor and therefore your schema can also be as small or large as you wish with a larger schema requiring a more powerful computer system to process the increased data volume for queries. However, in contrast to TPROC-C it is not valid to compare the test results of query load tests taken at different Scale Factors shown as SF in the Schema diagram.

**Figure 11.1.TPROC-H Schema.**

![Image 1: TPROC-H Schema.](https://www.hammerdb.com/docs4.0/resources/ch9-1.png)

The workload is represented by users executing a stream of 22 ad-hocs queries against the database with an example query as follows:

-- using 647655760 as a seed to the RNG
 select
        l_returnflag,
        l_linestatus,
        sum(l_quantity) as sum_qty,
        sum(l_extendedprice) as sum_base_price,
        sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
        sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
        avg(l_quantity) as avg_qty,
        avg(l_extendedprice) as avg_price,
        avg(l_discount) as avg_disc,
        count(*) as count_order 
from
        lineitem 
where
        l_shipdate <= date '1998-12-01' – interval '69' day (3)
group by
        l_returnflag,
        l_linestatus 
order by
        l_returnflag,
        l_linestatus;

In measuring the results the key aspect is the time the queries take to complete and it is recommended to use the geometric mean of the query times for comparison. A typical performance profile is represented by the time it takes the system to process a query set from Q1 to Q22 (run in a pre-determined random order).

**Figure 11.2.Power Query**

![Image 2: Power Query](https://www.hammerdb.com/docs4.0/resources/ch9-2.PNG)
