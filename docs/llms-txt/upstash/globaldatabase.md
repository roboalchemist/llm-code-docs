# Source: https://upstash.com/docs/redis/features/globaldatabase.md

# Global Database

In the global database, the replicas are distributed across multiple regions
around the world. The clients are routed to the nearest region. This helps with
minimizing latency for use cases where users can be anywhere in the world.

### Primary Region and Read Regions

The Upstash Global database is structured with a Primary Region and multiple
Read Regions. When a write command is issued, which can be initiated from any region, it is initially sent and processed
at the Primary Region. The write operation is then replicated to all the Read
Regions, ensuring data consistency across the database.

On the other hand, when a read command is executed, it is directed to the
nearest Read Region to optimize response time. By leveraging the Global
database's distributed architecture, read operations can be performed with
reduced latency, as data retrieval occurs from the closest available Read
Region.

The Global database's design thus aids in minimizing read operation latency by
efficiently distributing data across multiple regions and enabling requests to
be processed from the nearest Read Region.

User selects a single primary region and multiple read regions. For the best
performance, you should select the primary region in the same location where
your writes happen. Select the read regions where your clients that read the
Redis located. You may have your database with a single primary region but no
read regions which would be practically same with a single region (regional)
database. You can add or remove regions on a running Redis database.

Here the list of regions currently supported:

* AWS US-East-1 North Virginia
* AWS US-East-2 Ohio
* AWS US-West-1 North California
* AWS US-West-2 Oregon
* AWS EU-West-1 Ireland
* AWS EU-West-2 London
* AWS EU-Central-1 Frankfurt
* AWS AP-South-1 Mumbai
* AWS AP-SouthEast-1 Singapore
* AWS AP-SouthEast-2 Sydney
* AWS AP-NorthEast-1 Japan
* AWS SA-East-1 São Paulo

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/regionselect.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=c177261b7443aad5aab557f7ab312d8d" width="520" data-og-width="974" data-og-height="1603" data-path="img/globaldb/regionselect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/regionselect.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8dc3ffc3f04cb5aac64fb1d284467a92 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/regionselect.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=b413c448ee87a3578e0a70ef409dfe1d 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/regionselect.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=1b42b024e74fafd89a13e50c98e34fb3 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/regionselect.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=55a74b38c825de58ed043a063d226ebc 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/regionselect.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=cba8e82fee977b3c70e605be921a13ed 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/regionselect.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=6b6406fdcea9e681b23b2a81a0e19919 2500w" />
</Frame>

In our internal tests, we see the following latencies (99th percentile):

* Read latency from the same region \<1ms
* Write latency from the same region \<5ms
* Read/write latency from the same continent \<50ms

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/map2.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=6e744968e9185a825f52ee2986a23f7e" width="1000" data-og-width="1680" data-og-height="874" data-path="img/globaldb/map2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/map2.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=3f9b8524ff479b37266efe47da799185 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/map2.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=a47f9e8c867f53df998e390d09866fa9 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/map2.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=e5ea157ad2d54c6ce0ac0a2636861eae 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/map2.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=da93e8b5bdf527ee2e54ea6fcc32f8e5 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/map2.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=0218a1971423ae33cfc9500ae0aaa1dc 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/globaldb/map2.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=966b9f9e1835f38321b8c1c879b50df3 2500w" />
</Frame>

### Architecture

In the multi region architecture, each key is owned by a primary replica which
is located at the region that you choose as primary region. Read replicas become
the backups of the primary for the related keys. The primary replica processes
the writes, then propagates them to the read replicas. Read requests are
processed by all replicas, this means you can read a value from any of the
replicas. This model gives a better write consistency and read scalability.

Each replica employs a failure detector to track the liveness of the primary
replica. When the primary replica fails for a reason, read replicas start a new
leader election round and elect a new leader (primary). This is the only
unavailability window for the cluster where your requests can be blocked for a
short period of time.

<Note>
  Global Database is designed to optimize the latency of READ operations. It may
  not be a good choice if your use case is WRITE heavy.
</Note>

### Use Cases

* **Edge functions:** Edge computing (Cloudflare workers, Fastly Compute) is
  becoming a popular way of building globally fast applications. But there are
  limited data solutions accessible from edge functions. Upstash Global Database
  is accessible from Edge functions with the REST API. Low latency from all edge
  locations makes it a perfect solution for Edge functions

* Multi region serverless architectures: You can run your AWS Lambda function in
  multiple regions to lower global latency. Vercel/Netlify functions can be run
  in different regions. Upstash Global database provides low latency data
  wherever your serverless functions are.

* Web/mobile use cases where you need low latency globally. Thanks to the read
  only REST API, you can access Redis from your web/mobile application directly.
  In such a case, Global Database will help to lower the latency as you can
  expect the clients from anywhere.

### High Availability and Disaster Recovery

Although the main motivation behind the Global Database is to provide low
latency; it also makes your database resilient to region wide failures. When a
region is not available, your requests are routed to another region; so your
database remains available.

### Consistency

Global Database is an eventually consistent database. The write request returns
after the primary replica processes the operation. Write operation is replicated
to read replicas asynchronously. Read requests can be served by any replica,
which gives better horizontal scalability but also means a read request may
return a stale value while a write operation for the same key is being
propagated to read replicas.

In case of cluster wide failures like network partitioning (split brain);
periodically running anti entropy jobs resolve the conflicts using LWW
algorithms and converge the replicas to the same state.

### Upgrade from Regional to Global

Currently, we do not support auto-upgrade from regional to global database. You
can export data from your old database and import into the global database.

### Pricing

Global Database charges \$0.2 per 100K commands. The write commands are replicated to all read regions in addition to primary region so the replications are counted as commands. For example, if you have 1 primary 1 read region, 100K writes will cost \$0.4 (\$0.2 x 2). You can use Global Database in the free tier too. Free usage is limited with max one read region.
