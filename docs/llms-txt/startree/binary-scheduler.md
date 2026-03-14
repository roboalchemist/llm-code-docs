# Source: https://docs.startree.ai/corecapabilities/query_data/advanced_operations/workload-isolation/binary-scheduler.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Binary scheduler for workload isolation

<Warning>
  Binary scheduler feature has not been certified for production use in Startree Cloud. This is an experimental feature.
</Warning>

## **How Does Binary Scheduler Work?**

The Binary Workload Scheduler is designed to handle two distinct types of workloads: primary workloads (regular application queries) and secondary workloads (adhoc queries, testing, etc.)

**Primary Workload Processing:**

* Primary workload queries are executed with priority and submitted to runner threads immediately upon arrival
* Resources used by primary workload queries are not capped

**Secondary Workload Processing:**

* Secondary workload queries are identified using the query option

  `SET isSecondaryWorkload=true`
* These queries are processed through a constrained system with restrictions on runner threads, worker threads per query, and total worker threads for all in-progress secondary queries

The key benefit is to provide workload isolation: this scheduler can help to prevent expensive adhoc queries from impacting production workloads. Secondary workload can be used for adhoc triaging, testing and other non critical use cases on the same datasets.

## **How to Enable**

1. **Configure the Scheduler**: Set the query scheduler algorithm to `binary_workload` in your Pinot cluster configuration:

   ```
   pinot.query.scheduler.name=binary_workload  
   ```

2. **Mark Secondary Workload Queries**: Use the query option to identify secondary workload queries

   ```
   SET isSecondaryWorkload=true
   ```

3. **Optional Configuration**: Configure the maximum number of pending secondary queries

   ```
   pinot.query.scheduler.binarywlm.maxPendingSecondaryQueries = <>
   ```

## **Limitations**

* Only works for Single Stage Engine queries
* If primary workload queries end up occupying all threads - this will block any secondary workload queries
* Secondary workload queries can be rejected with "OutOfCapacityException" when the system cannot accommodate them

## Relevant Metrics

* numSecondaryQueries\_Count

Built with [Mintlify](https://mintlify.com).
