# Source: https://docs.oxla.com/introduction/what-is-oxla-and-why-use-it.md

# What is Oxla and why use it

Oxla is a highly resource-efficient, self-hosted, column-oriented OLAP database and query engine. It’s available under a proprietary license with [capacity-based pricing](https://www.oxla.com/pricing), and also comes in a forever-free, single-node [Developer Edition](/quickstart) for POCs and non-commercial use.

## Key Characteristics

### Vectorized Query Execution

Oxla uses a massively parallel processing (MPP) architecture at the core of its compute engine for high-performance processing. While MPP has been the standard in analytics systems for over a decade, Oxla takes a modern approach: it’s a new system built from the ground up, without relying on third-party components. This clean-slate design lets us apply recent advancements in computer science to a fresh codebase, with a focus on [low-level optimizations that improve resource efficiency](#optimized-data-transfer-between-cpu-and-ram), both in the query engine and across the system.

### Columnar Storage Optimization

Transactional (OLTP) databases like PostgreSQL or MS SQL Server use a row-oriented design, optimized for high-frequency writes. Columnar storage, by contrast, is designed for analytical workloads, allowing for faster scans, better compression, and more efficient aggregations.

Oxla supports high-speed ingestion of .csv, ORC, Parquet, and JSON files. For example, you can easily feed large volumes of transactional data from OLTP sources into Oxla at scale.

### Decoupled Storage & Compute

While Oxla isn’t currently capable of querying external data in place at the source (though this is a high-priority item on our immediate [roadmap](/product-roadmap)), it benefits from a decoupled storage & compute architecture. This means compute resources can be scaled independently of storage, allowing for more efficient resource allocation, easier deployment, and better cost control.

### Efficient Data Compression

Depending on the structure and contents of the data, Oxla achieves up to 95% compression. This enables cost-effective long-term storage, and the ultra-efficient query engine supports fast historical analytics over large datasets (up to 400 terabytes).

### Distributed, Multi-node Architecture

Oxla is a distributed database, meaning it can run across multiple CPUs (nodes) in parallel for horizontal scaling, characteristic of cloud-native systems. Adaptive query pipelines efficiently handle all types of operations across nodes.

At the same time, thanks to its unique resource efficiency, Oxla delivers strong performance even in single-node deployments and can scale vertically by adding more CPU cores.

Execution strategies are selected at runtime based on workload characteristics, ensuring optimal performance in both single-node and multi-node setups.

### SQL Support

Like many modern OLAP systems, Oxla uses its own declarative query language under the hood, but provides [SQL support](/sql-reference/overview) to users. Oxla aims for close compatibility with PostgreSQL, including support for core SQL constructs such as `FROM`, `JOIN`, `GROUP BY`, `ORDER BY`, and window functions.

### Optimized Data Transfer Between CPU and RAM

Over the past decade, CPUs have scaled from 4–8 cores to over 100, but memory bandwidth hasn’t kept pace. This hardware limitation creates a critical bottleneck for analytical compute engines.

Oxla introduces a set of low-level memory access and caching optimizations to address this issue and achieve high resource efficiency.

* **Compressed data** reduces the volume transferred between storage, memory, and CPU
* **User-space storage caches** minimize overhead from kernel-level memory operations
* **A custom data format** enhances data locality
* **Hybrid row/column formats** allow better alignment with CPU cache lines and vectorized execution
* **Temporal access patterns** help retain frequently used data in memory longer, reducing cache misses

## Why choose Oxla

### Scalability through resource-efficiency

A common reason to move to a fully-managed cloud data warehouse is the promise of “infinite scalability,” made possible by on-demand infrastructure in the cloud.

At Oxla, we believe systems should scale through smarter, more efficient use of hardware—not by simply throwing more resources at the problem. This principle is baked into how Oxla is designed and built.

By maximizing resource efficiency, Oxla lets you continue self-hosting your data warehouse while handling growing datasets. This approach reduces total cost of ownership by squeezing more out of your existing infra, helping you delay expensive upgrades and maximize ROI.

### Straightforward self-hosting

Oxla runs on x86-64 CPUs (Intel/AMD/ARM) and is deployed via Docker on Linux, accessed
through PostgreSQL Client 14. The same Docker image can be run in a traditional client-server
setup (either single-node or multi-node) or locally.

Oxla’s [configuration file](/configuration-deployment/configuration/oxla-configuration-file) is designed with simplicity in mind. It employs a streamlined, human-readable YAML format that covers essential settings without the verbosity or complexity seen in some other systems.

This way, Oxla is simple to integrate into existing environments with minimal operational overhead.

### Unified support for batch, low-latency, time-series, and multi-dimensional analytics

Oxla supports a wide range of analytical workloads in a single system. You can power real-time BI dashboards, process log data, run time-series analytics, and perform exploratory queries over terabyte-scale datasets without switching tools or maintaining separate systems. Combined with scalable and easy-to-manage self-hosting, this makes Oxla particularly suitable for unified analytics in critical infrastructure such as the telco, energy, and defense sectors.
