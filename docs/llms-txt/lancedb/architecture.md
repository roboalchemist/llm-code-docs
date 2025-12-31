# Source: https://docs.lancedb.com/enterprise/architecture.md

# Architecture

> Learn about LanceDB Enterprise architecture and system design.

LanceDB Enterprise consists of the following key components:

* Query Fleet
* Plan Execution Fleet
* Indexer Fleet

<img src="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/enterprise/architecture.png?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=4e1a6b83e1db3d0f4c9d3f6d2392abbf" alt="architecture" data-og-width="2341" width="2341" data-og-height="1324" height="1324" data-path="static/assets/images/enterprise/architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/enterprise/architecture.png?w=280&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=54c07bb506ac57c21681226e728e9378 280w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/enterprise/architecture.png?w=560&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=1fea3676e06b167106237fd48708c18a 560w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/enterprise/architecture.png?w=840&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=0bd26507e3b7f3226aee64350b7b7c73 840w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/enterprise/architecture.png?w=1100&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=75cc958fb7938ea405b41e7654ea88b8 1100w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/enterprise/architecture.png?w=1650&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=09fe1a4cdc28590153c766a22b640311 1650w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/enterprise/architecture.png?w=2500&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=94891e92536f0b04e3efd49a56fee8f4 2500w" />

### Query Execution

The LanceDB stateless query fleet is capable of managing **tens of thousands** of queries per second (QPS) per table with minimal latency.
This level of throughput satisfies the requirements of even the most demanding production environments.

Each query is compiled into a distributed query plan and executed on the Plan Execution Fleet in parallel.
Additionally, each query is auto-vectorized for recent generations of `x86_64` and `ARM`
CPUs for enhanced hardware efficiency.

### Plan Execution Fleet

Each plan execution node is equipped with high-performance NVMe SSDs that act as
a hybrid cache for cloud object storage systems like AWS S3,
Google Cloud Storage, and Azure Blob Storage.

The distributed query plan enforces cache locality for both data and indices using a variant of
the **consistent hashing** algorithm with a low cache miss rate.
LanceDB can serve warm queries with latency in **the single-digit to low double-digit milliseconds** range.

### Write Path

LanceDB Enterprise is engineered for high-throughput data ingestion and indexing.
The system ensures data persistence on durable object storage before confirming any write request.

An extensive indexing fleet, enhanced with hardware acceleration, operates asynchronously to
perform partial or full indexing, data compaction, and cleanup.
Furthermore, we achieve high-throughput indexing operations without compromising query performance.

<Note>
  Customer data does not go through the event queue. The queue sends events such as
  "create an index" to the indexers to trigger actions.
</Note>

<Info>
  Indexing scales down to zero when there is no activity on the table.
</Info>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt