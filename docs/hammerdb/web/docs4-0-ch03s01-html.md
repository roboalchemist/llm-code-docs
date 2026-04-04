# Source: https://www.hammerdb.com/docs4.0/ch03s01.html

Title: 1. What is a Transactional Workload

URL Source: https://www.hammerdb.com/docs4.0/ch03s01.html

Markdown Content:
A transactional or OLTP (online transaction processing) workload is a workload typically identified by a database receiving both requests for data and multiple changes to this data from a number of users over time where these modifications are called transactions. Each database transaction has a defined beginning point, manipulates and modifies the data within the database and either commits the changes or rollbacks the changes to the starting point. A database must adhere to the ACID (Atomicity, Consistency, Isolation, Durability) properties to ensure that the database remains consistent whilst processing transactions. Database systems that process transactional workloads are inherently complex in order to manage the user sessions access to same data at the same time, processing the transactions in isolation whilst keeping the database consistent and recoverable. People will typically interact with OLTP systems on a regular basis with examples such as an online grocery ordering and delivery system or an airline reservation system. Performance and scalability are essential properties of systems designed to process transactional workloads. The TPC-C benchmark is a benchmark designed by the TPC to measure the performance of the software and hardware of a relational database system to process these workloads.
