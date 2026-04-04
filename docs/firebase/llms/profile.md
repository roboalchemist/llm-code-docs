# Source: https://firebase.google.com/docs/database/usage/profile.md.txt

<br />

Measure the performance of yourFirebase Realtime Databasewith the database profiler tool, built into the[FirebaseCLI](https://firebase.google.com/docs/cli). The profiler tool logs all the activity in your database over a given period of time, then generates a detailed report. Use the detailed report to troubleshoot issues with your database performance, spot problem areas, and reduce unindexed queries.
| **Note:** You can extend the analysis you perform using the database profiler with data captured by the[Cloud Audit Logging service](https://firebase.google.com/support/guides/cloud-audit-logging/firebase-realtime-database).

## Build a profile

1. Before you start profiling yourFirebase Realtime Database, make sure you're using the latest version of the[FirebaseCLI](https://firebase.google.com/docs/cli)and that you've initialized it for the database and project you want to profile. Note that you must be an editor or owner of that project to profile.

2. Start profiling your database with the following command:

   ```text
   firebase database:profile
   ```
   The profiler displays a status message as it records operations from your database and builds the profile.

   <br />

3. Press<kbd>Enter</kbd>to complete the profile and display the results.

## Interpret your results

The profiler tool aggregates the data it's collected about your database's operations and displays the results in three primary categories:[speed](https://firebase.google.com/docs/database/usage/profile#speed),[bandwidth](https://firebase.google.com/docs/database/usage/profile#bandwidth), and[unindexed queries](https://firebase.google.com/docs/database/usage/profile#unindexed_queries).

### Speed

The Speed Report measures the server's response time (in milliseconds) for each operation type. However, the speed measured in the Speed Report might not actually reflect the speed end-users experience. Different factors, including network conditions, can add latency on the client side.

The Speed Report includes the following properties:

- **Path:** The path in your database where the operations occurred. If there are more than 25 child nodes, the profiler tool collapses these into a parent path and adds a`$wildcard`marker. You might see your database's root directory in the report, represented by a forward slash**`/`**.
- **Count:**The number of operations that occurred at the given path.
- **Average Execution Speed:**The average time it takes the server to execute business logic needed to handle the particular operation type at that path. The time interval measured here starts after that measured by the "Average Pending Time" described below.
- **Average Pending Time:** The average time requests spend queued before getting executed. This delay is common to all client-initiated requests. The total server-side request latency is roughly the sum of that request's pending time and execution speed.If the average pending time is consistently high, overall performance will suffer. Common root causes of such degradation include (1) database overload due to request volume and (2) head-of-line blocking due to long-running reads or writes. Sharding data across multiple instances is the recommended remedy for (1). Solutions for (2) are case-specific, but client-side instrumentation of individual requests is a good first step towards finding them.
- **Permission Denied:** The number of operations at the given path that were blocked by[Firebase Database Rules](https://firebase.google.com/docs/database/security/core-syntax)on your database.

|                                                                                                                                                                                                                                                                                     Speed Report by Operation Type                                                                                                                                                                                                                                                                                     ||
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read Execution Speed      | The server response time for client requests to read data from the database. Read execution time generally scales with the amount of data being read, but even some small reads may also be delayed by cache prefetching.                                                                                                                                                                                                                                                                                                                                                   |
| Write Execution Speed     | The server response time for client requests to write data to the database. Write execution time scales with the amount of data being written.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Connect Execution Speed   | The server response time for requests to establish to database clients. Latency for connection requests is dominated by in-memory server-side bookkeeping related to connection management.                                                                                                                                                                                                                                                                                                                                                                                 |
| Broadcast Execution Speed | The amount of time the server takes to distribute data to clients listening to the given path for realtime updates. The**Count**property in the Broadcast Speed Report aggregates the number of broadcasts that happened, not the number of clients that received the information. For example, if 10 clients were listening at a given path, and the server broadcast an update to all 10 clients, the broadcast count only reflects 1 broadcast, even though 10 clients received the data. The**Permission Denied**property isn't included in the Broadcast Speed report. |

### Bandwidth

The Bandwidth Report provides insight on how much data your database consumes across incoming and outgoing operations. You shouldn't use the Bandwidth Report to estimate billing, however, because it doesn't include bandwidth used for other operations, like profiling your database. The Bandwidth Report roughly estimates the payload size of the data consumed by read, write, and broadcast operations to and from your database. It's a tool that measures performance, not one that forecasts billing.

The Bandwidth Report includes the following properties:

- **Path:**The path in your database where the operations occurred. If there are more than 25 child nodes, the profiler tool collapses these into a parent path.

  | **Operations at root:** If a write operation happened at your database's root directory, even though the read or broadcast operation happened at a different path, the report displays the root directory for the download operation. Your database's root directory is shown as a forward slash**`/`**in the report.
- **Total:**The total outgoing or incoming bytes used across all operations at the given path.

- **Count:**The number of operations that occurred at the given path.

- **Average:**The average number of downloaded or uploaded bytes across operations at the given path (bytes/write or bytes/read).

|                                                                Bandwidth Report                                                                ||
|------------------|------------------------------------------------------------------------------------------------------------------------------|
| Downloaded Bytes | Data consumed through read and broadcast operations sent out via the client SDKs and REST API.                               |
| Uploaded Bytes   | Data consumed through write requests coming into the database server. Deletes show up as writes with 0 bytes under incoming. |

### Unindexed Queries

Unindexed queries can be expensive, because clients download all of the data at a location and then perform queries on it. This uses up more bandwidth than necessary. Resolve as many unindexed queries as you can to optimize your database's performance.

The Unindexed Queries report displays the following properties:

- **Path:**The path in your database where the unindexed queries occurred.
- **Index:** The rule you should add to resolve the unindexed queries. Learn more about indexing in[Index your data](https://firebase.google.com/docs/database/security/indexing-data).
- **Count:**The number of unindexed queries that occurred at the given path.

## Advanced profiling

To see all the operations your database is handling, use the`--raw`flag when you profile your database, as follows:  

```text
firebase database:profile --raw
```

<br />

The raw output also includes client information for each operation, such as`userAgent`strings and IP addresses. Learn more about the different operations profiled in yourFirebase Realtime Databasein[Firebase Realtime DatabaseOperation Types](https://firebase.google.com/docs/cli/database-profile).

## The profiler tool: Not a billing tool

**Don't use the profiler tool to estimate bandwidth cost.**The profiler tool is intended to give you an overall picture of your database's performance, to help you monitor operations and troubleshoot issues, not to estimate billing. It doesn't account for network traffic, it only records an estimate of the application data sent in responses.

The following are some common examples of network traffic billed by Firebase that aren't covered in your database profile:

- **Protocol overhead:**Some additional traffic between the server and clients is necessary to establish and maintain a session. Depending on the underlying protocol, this traffic might include: Firebase Realtime Database's realtime protocol overhead, WebSocket overhead, and HTTP header overhead. Each time a connection is established, this overhead, combined with any SSL encryption overhead, contributes to the connection costs. Although this is typically not a large amount of bandwidth, it can be substantial if your payloads are tiny or you make frequent, short connections.
- **SSL encryption overhead:**There is a cost associated with the SSL encryption overhead necessary for secure connections. On average, this cost is approximately 3.5KB for the initial handshake, and approximately 40B for TLS record headers on each outgoing message. For most apps, this is a small percentage of your bill. However, this could become a large percentage if your specific case requires a lot of SSL handshakes. For example, devices that don't support TLS session tickets might require large numbers of SSL connection handshakes.

Read more about[understanding and estimating your bill](https://firebase.google.com/docs/database/usage/billing).