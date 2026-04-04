# Source: https://electric-sql.com/blog/posts/2025-08-13-electricsql-v1.1-released.md

---
url: /blog/posts/2025-08-13-electricsql-v1.1-released.md
description: >-
  How we built a new storage engine for Electric, why we did it now, and how it
  delivers lower latency, higher throughput, and zero‑downtime deploys.
---

Electric is a [Postgres](https://www.postgresql.org/) sync engine that [streams database changes to millions of concurrent users in real time](https://electric-sql.com/blog/2024/12/10/electric-beta-release#scalable). Our mission is simple: be faster than Postgres.

After a year of progress, rapid growth exposed our limits. The storage engine had become a critical bottleneck — replication lag climbing, CPUs maxing out, and the system was having trouble keeping pace with the largest deployments. We made a bold decision: build our own storage engine from scratch.

The result? 102X faster writes and 73X faster reads on SSD. This is the story of how we made it.

## How Electric works

The core primitive for controlling sync in Electric is the [**shape**](/docs/guides/shapes). A shape is a partial replica of a table that includes the subset of rows matching a user-defined WHERE clause. Electric continuously tails Postgres's logical replication stream for changes, matches them against registered shapes, appends them to the corresponding **[shape logs](/docs/api/http#shape-log)**, and sends them to clients using HTTP long polling.

:::info Why this architecture is different

**CDN-native fan-out**: CDNs de-duplicate shape requests and collapse load, moving it out of your infrastructure.

**Cost physics**: There's no persistent socket tax—you pay only for actual data transfer, which means lower egress costs and fewer hot servers at scale.

**Operational simplicity**: Shape log persistence means zero-downtime deploys without managing stateful socket fleets.

:::

Electric's job sounds simple, until you have hundreds of thousands of shapes to match and millions of clients hitting the system at once. At that scale, every microsecond counts. Fall behind Postgres throughput and real-time becomes sluggish and Postgres's [WAL](https://www.postgresql.org/docs/current/wal-intro.html) starts to pile up. It's not pretty.

## Storage is the beating heart of Electric

One [difference](https://expertofobsolescence.substack.com/p/the-hard-things-about-sync) between sync engines and other types of real‑time systems is that sync engines don't miss changes. Real‑time systems typically offer at‑most‑once delivery or temporal buffering windows. If you lose connection, you're done. In Electric, users can resume shapes at any point in history. This makes the sync engine dramatically simpler to use but storage becomes the beating heart of the system.

### Picking an off-the-shelf solution

When we decided to [rebuild Electric](/blog/2024/07/17/electric-next), we focused on shipping a working system that users could trust, and fine-tune performance later. As Kyle Mathews says: "make it work, make it right, make it fast".

Writes in Electric are append‑only, while reads are mostly range scans. Since logs can grow indefinitely, we compact them periodically. Compaction in Electric is unique in that it must preserve the temporal ordering of creation and deletion of keys in the log. We looked at the available options.

[Apache Kafka](https://kafka.apache.org/) is the production system that is closest to our needs. However, it's too complex and would be hard to integrate.
[LSM‑tree](https://www.cs.umb.edu/~poneil/lsmtree.pdf)‑based stores like [RocksDB](https://rocksdb.org/) are good for append‑only writes but not ideal for range scans. We also looked into [SQLite](https://sqlite.org/) because it is heavily optimized. It was fast, but not always faster, and we were worried about hitting issues with a non‑customizable system.

None of the off‑the‑shelf solutions were a perfect fit for Electric's requirements. So, we ended up picking [CubDB](https://github.com/lucaong/cubdb) as a pragmatic starting point — a tiny and mighty Elixir key‑value store that would get the job done. Our team has lots of experience with Elixir, so we would get good development speed by keeping the storage engine in the same language. We knew this was not the best solution, but it was one that didn't require a lot of initial engineering investment.

### Reaching the limits

CubDB was performing well enough and we didn't come across any bugs. We were able to get huge performance gains by optimizing other parts of the system before even thinking of storage. We [launched v1.0](/blog/2025/03/17/electricsql-1.0-released) and later [Cloud Beta](/blog/2025/04/07/electric-cloud-public-beta-release) with it. As Electric scaled to production traffic with customers like [Trigger.dev](https://trigger.dev/) pushing [20,000 changes per second](https://x.com/triggerdotdev/status/1945876425225171173), the limitations started to emerge.

**CPU usage**: Writing to storage consumed excessive CPU time. This was due to frequent updates to CubDB's internal structures.

**Latency**: P95 latency was too high. Large transactions blocked reads for extended periods.

**Technical limitations:** CubDB's architecture made zero-downtime deployments impossible in our Cloud, because it wasn't possible to have shared access to logs across instances.

The challenges we encountered weren’t due to CubDB being poorly designed — it simply wasn’t the right fit for Electric’s use case. We knew this day would come, and we were grateful for how far our initial storage solution with CubDB had taken us.

## Building our own storage engine

Following the lessons from [CockroachDB](https://www.cockroachlabs.com/) when they [replaced RocksDB with Pebble](https://www.cockroachlabs.com/blog/pebble-rocksdb-kv-store/), we chose to build our storage engine from scratch and own this layer of the system. The scope of our needs was small enough to make this feasible. We could more easily adapt it to our needs over time. Here's what we needed from our storage:

**Performance**: With our initial prototype, we learned about bottlenecks and the parts of the system that were hard to scale. Reducing CPU usage and the number of system calls were two top priorities.

**Optimize read path**: We've designed Electric to do all the hard work at write time to make the read path extremely efficient. Parsing any data in the read path is prohibitively expensive.

**Fast recovery**: Electric implements the Postgres's logical replication [protocol](https://www.postgresql.org/docs/current/logical-replication.html). When it crashes, we want to resume replication from a safe checkpoint and recover quickly.

**Cloud native**: In our [Cloud](https://dashboard.electric-sql.cloud/sources), we ship patches constantly. Zero-downtime deployments are a non-negotiable. At some point we also want to start moving shape logs to object store.

**Observability**: By owning the storage engine, we gain deep visibility into its behavior and performance. This lets us optimize hot paths, resolve issues faster, and respond quickly as requirements evolve.

## Implementation overview

Our new storage architecture is elegantly simple. For each shape, we maintain two files: the **shape log**, which contains the raw data for the shape, and the **offset index**, which is a list of pointers into the shape log for fast lookup of offsets. Addressing shape logs by offset matches how [clients request shapes](/docs/api/http#shape-log).

### Shape log

The shape log contains pre‑serialized JSON lines of the shape data (the row change from Postgres's logical replication) and their corresponding offset. Shape logs are divided into fixed‑size **chunks**. The first entry of the log is the **chunk boundary** and is used for indexing. Changes matching the shape are appended to the end of the log.

**Immutable chunks**: Once a chunk reaches its max size, it is marked as complete and becomes immutable. Readers can safely access completed chunks.

**Shape‑log scanning**: To find the right offset for a user request, we use the shape index to locate the chunk that contains the requested offset and then scan the chunk to find the first JSON line for that offset. We use a [read‑ahead](https://man7.org/linux/man-pages/man2/readahead.2.html) technique to reduce the number of system calls while scanning the file.

**Buffering writes**: Calling [`fsync()`](https://man7.org/linux/man-pages/man2/fsync.2.html) on every write is prohibitively slow, but not calling `fsync()` immediately is giving away durability. Any high‑performance storage system needs to address this dilemma in some way. In Electric, we deeply integrate shape‑log recovery with logical replication. If Electric crashes without some changes being flushed to disk, we can resume logical replication from the last persisted position and replay missing transactions.

### Shape index

The shape index provides fast shape offset lookup through a sparse indexing strategy. The index is simply a list of pointers to chunk boundaries in the shape log. We add a new pointer to the sparse index for every finalized chunk.

**Finding a chunk**: When a client requests data starting from a specific offset, we do a binary search on the index to locate the appropriate chunk pointer, retrieve that chunk, and scan it from there, as explained above.

**Lock‑free**: Because shape logs are append‑only, offset pointers are always added to the end of the index. This means that the index can be read and written without any locking. We keep a number of chunk pointers in memory to avoid reading the index from disk for [live requests](/docs/api/http#live-mode).

### Read-only mode

The new architecture decouples readers and writers, allowing the Electric server connected to Postgres to share access with other Electric servers accessing the shape logs in read-only mode. This unlocks new capabilities.

**Horizontal read scaling**: Electric is already quite scalable [behind a CDN](/blog/2024/12/10/electric-beta-release), but read-only mode allows horizontal scaling of the read path. Electric can scale to any read workload.

**Zero‑downtime deployments**: Keeping the system available during deploys is critical for our Cloud infrastructure. We achieve zero-downtime deployments by allowing servers to continue serving data from shape logs, while the old and new server switchover the connection to Postgres.

## Performance evaluation

Enough talk — show me the numbers! To validate our new storage engine, we ran a series of performance tests.

Microbenchmarks ran on a local SSD (MacBook Air M4), and end‑to‑end benchmarks ran on AWS t2.medium instances with network-attached storage (EFS).

### Micro-benchmarks

We conducted a series of microbenchmarks to evaluate the new storage engine against CubDB. We saw strong speedups on both SSDs and EFS, with 102x and 7x faster writes and 73x and 172x faster reads, respectively.

#### Write performance

This benchmark consists of appending a fixed number of rows to a shape log. With CubDB, every insertion needs to update the index to locate the right chunk to write to. With the new engine, we simply append to the latest chunk and only modify the index when we reach the chunk‑size limit.

On local SSDs, the new engine wrote 102x faster when appending 1,000 rows.

With network‑attached storage, the network latency slows both storage engines down but we still see the same sort of speedup, but now with a 5x to 7x performance improvement.

#### Read performance

This benchmark consists of reading a fixed number of chunks starting from an arbitrary offset in a shape log and measuring the total time to retrieve all chunks.

In this case, the baseline latency for CubDB is quite high due to the number of system calls required to find the requested offset in the initial chunk. The new storage engine uses a read‑ahead optimization to reduce the number of system calls.

### End-to-End benchmarks

The following [benchmarks](/docs/reference/benchmarks) run the full Electric stack end-to-end and report application‑level latency. The results give a clearer picture of potential improvements at runtime. We ran these experiments in AWS in the same setting as the micro-benchmarks (t2.medium instances with EFS).

#### Shape creation

In this benchmark, we create an increasing number of concurrent shapes until the system saturates. This is a fairly expensive operation, as we need to query Postgres and write a new file to disk with each request.
This is a scenario we had optimized for CubDB, so it performs reasonably well; however, the new engine is still significantly faster overall — about 1.63x on average across the run.

#### Write throughput

This benchmark drives writes to arbitrary shapes and measures the end‑to‑end latency for a client to receive the data. This is the critical path for Electric: the longer writes take, the greater the replication lag becomes. We had a significant speedup for the new storage — 5x at 1,500 shapes — which means that the new storage is able to keep replication lag lower.

#### Reads fan‑out

This benchmark measures read latency when streaming changes from one shape to a large number of connected clients. It stresses the concurrency of the read path until resources saturate. In practice, most Electric deployments will run behind a CDN (or an HTTP cache), which will de‑duplicate requests for the same shape. But benchmarks show that Electric can go pretty far without any caching in front of it.

Across the range, the new engine delivers consistently lower end‑to‑end latency — roughly 3.5–4.5x faster, and about 3.8x faster at 1,000 concurrent clients. Lower read‑path latency keeps live clients closer to real time.

## Lessons learned

Starting with CubDB was a good choice. It got us to v1.0 with minimal issues, giving us time to ship software that just works. Before addressing storage performance, [we've fixed tons of bugs, made Electric a reliable system](https://electric-sql.com/blog/2025/08/04/reliability-sprint) and learned a great deal about how it behaves under real‑world workloads, surfacing bottlenecks in many other places that were far more important to our core proposition. Had we chosen to build our own storage system from day one, we would have made some wrong assumptions and done lots of premature optimizations. Instead, our production experience gave us the insight we needed to design the right solution in the right moment.

This isn't a universal playbook. It worked well for us because the scope of what we had to build was relatively small, and it was one of our team's core areas of expertise.

## What's next

We've taken a big step toward our ambitious goal: being **faster than Postgres**. The new storage engine has delivered significant performance gains with 102x faster writes on SSD.

Beyond making Electric faster, we're laying the groundwork to continue building better open-source and cloud products. In Cloud, we're already seeing benefits with rolling deployments, horizontal scalability but it doesn't end there. There is an exciting roadmap ahead!

None of this would've been possible without our incredible engineering team. Huge thanks to the Electric [team](/about/team) for their insight, code reviews, and relentless focus on making Electric better.

Ready to experience the sync? [Sign up for Electric Cloud](https://electric-sql.com/cloud)—it's free.
