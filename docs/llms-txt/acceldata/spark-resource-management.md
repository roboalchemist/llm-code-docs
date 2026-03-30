# Source: https://docs.acceldata.io/documentation/spark-resource-management.md

# Spark Resource Management

## Sizing Spark Clusters for Performance and Efficiency

This page builds on the Resource Recommendations guidance by focusing specifically on Apache Spark—a distributed, in-memory data processing engine used in many ADOC workloads.

While the [Resource Recommendations and Auto-Sizing](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/resource-recommendations-and-auto-sizing) page outlines high-level strategies for allocating memory, CPU, and retry settings, Spark jobs require additional tuning due to their dynamic execution model, in-memory operations, and sensitivity to partitioning and data skew.

This guide will help you configure Spark clusters more effectively by covering:

- Spark driver and executor sizing
- Resource allocation strategies
- Practical examples and baseline configurations
- How to handle memory pressure and disk spill
- Best practices for tuning and monitoring jobs over time

## Prerequisites

Before proceeding, make sure you’ve reviewed the [Resource Recommendations and Auto-Sizing](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/resource-recommendations-and-auto-sizing) page to understand how ADOC determines baseline resource needs, auto-retry logic, and default sizing strategies. This page assumes you are familiar with:

- Data Plane-level resource strategies
- T-shirt sizing (Small, Medium, Large)
- Node-specific resource inputs (cores, memory, disk)

## Understanding Spark Cluster Sizing

A Spark cluster consists of two key components:

- **Driver** – Orchestrates the job, handles coordination.
- **Executors** – Perform the actual data processing in parallel.

Properly sizing a Spark cluster ensures jobs run efficiently—avoiding excessive retries, out-of-memory (OOM) errors, or wasted (idle) resources.

Note Sizing is not just about a single job.

In real-world ADOC environments, multiple jobs—such as **profiling**, **anomaly detection**, and **rule-based validations**—may run at the same time on the same Data Plane (shared Spark infrastructure). So while the sizing factors below apply to each job individually, you should also account for job concurrency and total available resources across the cluster.

When sizing, consider:

| Factor | Why It Matters | 
| ---- | ---- | 
| Data size (uncompressed) | Spark expands compressed data in memory | 
| Partitioning strategy | Determines parallelism and performance | 
| Memory and CPU availability | Defines scalability and execution time | 
| Disk size | Needed for data spill when memory is insufficient | 
| Job type (ETL, ML, aggregation) | Some require more CPU or memory | 
| Retry strategy | Influences how Spark responds to failures | 


### Planning for Multiple Jobs

If you're running several jobs on the same Data Plane, **cluster sizing becomes a capacity planning exercise**:

- Estimate the resource needs of each job.
- Factor in the **maximum number of jobs that may run concurrently**.
- Ensure the total cluster size (CPUs, memory, disk) can support that load.

#### Example

If your cluster has:

- 64 CPUs
- 256 GB RAM

And you expect 3 concurrent jobs:

- Profiling: 16 CPUs / 64 GB
- Anomaly Detection: 24 CPUs / 96 GB
- Validation: 16 CPUs / 64 GB

You’re using 56 CPUs and 224 GB RAM—which fits, but adding another job might push the cluster over its limit.

Currently, ADOC does not include a built-in resource estimation calculator.

However:

- You can use historical job data (Job Details &gt; Resource section) to estimate resource usage for similar jobs.
- The Node Details section in the UI helps refine recommendations by providing expected data sizes and available hardware.
- Teams often create simple internal sizing templates (e.g., spreadsheet models) based on past runs and job types.

## Sizing the Driver

The driver coordinates execution plans and stores lightweight intermediate results. It typically requires less memory and fewer cores than executors.

Recommended starting point:

- Cores: 1–2
- Memory: 2–4 GB
- Overhead memory: 20–30% of total

## Sizing Executors

Executors are the workers that process your data. You need to decide how many executors to use and how much power each one gets.

Suggested settings:

- Cores per executor: 3–5 (to balance speed and stability)
- Memory per executor: 14–20 GB (enough for most tasks)
- Add 20-30% more memory for safety
- Use up to 80–90% of available memory and CPU per node to avoid overloading it
- Plan for 2 to 3 times the memory size for each executor, in case data spills to disk.

## Resource Allocation Strategies

Spark jobs can follow different execution patterns depending on memory and disk availability. Below are three common scenarios.

**Case 1: In-Memory, Single-Pass Execution**

- Entire data fits into memory
- No spill to disk

Example (1 TB uncompressed data):

- Required executor memory: 1 TB + 30% overhead = 1.3 TB
- Required cores: Equal to number of partitions (e.g., 1000)

**Case 2: In-Memory with Disk Spill, Single-Pass**

- Not enough RAM to hold all data
- Data partially spills to disk

Strategy:

- Reduce executor RAM
- Increase disk size (e.g., 3x memory)
- Keep total core count equal to number of partitions

**Case 3: Disk Spill + Multi-Pass (Most Common)**

- Data processed in multiple iterations
- Reduces RAM needs
- Relies on Spark to spill to disk during each pass

Example:

- 1 TB data split into 1000 partitions
- Process over 20 iterations using 100 cores
- Each executor uses 3–5 cores and 14–20 GB RAM
- Memory spill writes to disk; execution is slower but more efficient

## Example Cluster Configuration

For a 1 TB dataset with quality checks and transformations:

- Node pool: 20 nodes (each 8 cores, 32 GB RAM)
- Total cores: ~160
- Executors: 48 executors, ~144 cores total

Executor config:

- 3–5 cores each
- 14–20 GB RAM
- 20–30% overhead
- Disk: 2–3x RAM

Driver config:

- 2 cores
- 2– 4 GB RAM

## Understanding Why Data Expands in Spark

Data stored in compressed formats (like ZIP files) gets much larger when Spark processes it:

1. A 1TB compressed CSV file might need up to 10 TB of memory
2. Other formats (like JSON or Parquet) might need 3-6 times more space.
3. Poorly organized data can increase memory needs even more.

| Scenario | Typical Expansion | 
| ---- | ---- | 
| 1 TB GZIP CSV | Up to 10 TB in memory | 
| JSON or Parquet | 3–6x expansion | 
| Poorly partitioned data | Higher memory overhead due to skew | 


Always size based on decompressed data volume, not file size on disk.

## Tracking Job Performance with Spark History Server

ADOC integrates with the Apache Spark History Server for persistent job monitoring and performance analysis.

### Benefits

- Review completed jobs beyond the live Spark UI
- Debug long-running or failed jobs
- Analyze memory use, executor allocation, and shuffles
- Track retry behavior and job evolution over time

### Configuration Steps

1. **Storage setup**: Create a cloud directory (e.g., S3, GCS, GCP)
2. **Permissions**: Ensure service account has read/write access
3. **Retention and refresh**: Tune how many jobs to store and how often to refresh history
4. **Data Plane-level setup**: Customize history server for each Data Plane’s needs

Different Data Planes may handle different data types (e.g., sales vs. behavioral data)—configure history storage accordingly.

---

## Best Practices

1. **Start with a balanced setup**
Use 3 to 5 CPU cores and about 14–20 GB of memory per executor. This works well for most jobs.
2. **Make sure you have enough disk space**
If your data might not fit in memory, keep 2 to 3 times more disk space than memory.
3. **Add a safety buffer**
Always add 20–30% extra memory to avoid out-of-memory errors during processing.
4. **Align cores with your data**
Use one core per data chunk, or one core for every 3–5 chunks if the job has many steps.
5. **Keep an eye on job performance**
Check job stats regularly (in the history server). Adjust your settings if the data size or job behavior changes.

### Troubleshooting: Out-of-Memory (OOM) Errors

**What if I get an OOM error?**

Try reducing executor cores (less parallelism → less memory pressure) or increasing executor memory if available.

**Can I avoid increasing memory?**

Yes—reduce executor cores to lower memory demand per node.

**What if I have more memory available?**

Increase executor memory and overhead, but keep core count constant.

**Will reducing cores affect performance?**

Yes, but it may be necessary to complete the job reliably.

**How can I prevent OOM in the future?**

Monitor memory usage and adjust configurations. Use T-shirt sizing with auto-retries as a fallback.