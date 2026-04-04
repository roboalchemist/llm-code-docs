# Source: https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-redis-on-northflank.md

# Deploy Redis® on Northflank

This guide explains how to quickly and easily deploy and use [Redis®*](https://redis.io/) on Northflank.

| Available versions | Description | Backups | TLS |
| --- | --- | --- | --- |
| 8.4.0, 7.2.12, 7.2.4, 6.2.21, 6.2.14 | Redis® implements a distributed, in-memory key-value database with optional durability. | Disk | Yes |

## Deploy Redis

1. [Click here to create an addon](https://app.northflank.com/s/project/create/addon), or choose addon from the create new menu in the top right corner of the dashboard

2. Select Redis and enter a name

3. Choose a version or leave as default (most recent version)

4. Choose whether to [deploy with TLS](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#enable-tls). This can be changed later.

5. Choose whether to make the database publicly accessible. This will give your addon a URL and make it available online. TLS must be enabled to select this.

6. If you have [secret groups](https://northflank.com/docs/v1/application/secure/manage-secret-groups) in your project, choose ones to [link to the addon](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#link-database-secrets-to-a-secret-group) so that the database can be used in services and jobs that inherit variables from the secret group. To link the database to a secret group:
  
  
  
  - Show secret groups and configure the secret groups you wish to use
  
  - Select suggested secrets from the database to link, or select all
  
  - Set any required aliases for specific secrets to make them accessible by that name within your application

7. Select the required [resources](https://northflank.com/docs/v1/application/databases-and-persistence/scale-a-database) for your database. You can scale the database after creation, but available storage and replicas cannot be decreased once increased.

8. Create addon and Redis will begin provisioning, this may take a few minutes.

## Advanced options

Redis has the following advanced options available when creating your addon.

### Redis Sentinel

[Deploy Redis with an additional Sentinel process](https://northflank.com/docs/v1/application/databases-and-persistence/configure-addons-for-high-availability#redis). Sentinel monitors Redis instance health and triggers automated failover in case of an instance failure. Client library needs to support Sentinel for master discovery.

This cannot be changed after creation.

### Maxmemory policy

You can select an [eviction policy](https://redis.io/docs/reference/eviction/), which determines how Redis will behave when the `maxmemory` limit is reached. The maximum memory is determined by the memory assigned to the replica [according to the addon's plan](https://northflank.com/docs/v1/application/databases-and-persistence/scale-a-database). The `maxmemory` limit will be redefined when you change the addon's plan.

The policy cannot be changed after creation. By default, a Redis addon will use the `noeviction` policy, which will not remove existing values, nor save new ones if the memory limit is reached.

| Policy | Effect |
| --- | --- |
| `noeviction` | New values aren’t saved when memory limit is reached. When a database uses replication, this applies to the primary database |
| `allkeys-lru` | Keeps most recently used keys; removes least recently used (LRU) key |
| `allkeys-lfu` | Keeps frequently used keys; removes least frequently used (LFU) key |
| `volatile-lru` | Removes least recently used keys with the expire field set to true |
| `volatile-lfu` | Removes least frequently used keys with the expire field set to true |
| `allkeys-random` | Randomly removes keys to make space for the new data added |
| `volatile-random` | Randomly removes keys with expire field set to true |
| `volatile-ttl` | Removes keys with expire field set to true and the shortest remaining time-to-live (TTL) value |

### Deploy with zonal redundancy

Your addon will be deployed to your [project's region](https://northflank.com/docs/v1/application/run/deploy-to-a-region). Each region may have multiple availability zones, which are data centers with independent infrastructure such as networking, power supply and cooling within the region. Some regions, however, do not have more than one availability zone.

Normally your addon replicas will be provisioned in the same availability zone, but you can enable zonal redundancy to provision replicas across multiple availability zones.

This will ensure that your addon remains available in the event that one zone fails, however networking between replicas in different zones will be slightly slower compared to replicas provisioned in the same availability zone. Replicas will be bound to the zone they are deployed in.

### Backup schedules

You can [add backup schedules](https://northflank.com/docs/v1/application/databases-and-persistence/backup-restore-and-import-data#schedule-backups) when creating your addon. Backups of the addon will be taken according to the schedules.

## Connect to Redis

You can manually copy the connection secrets for your Redis database from the connection details page into runtime variables or build arguments of your workloads on Northflank.

However, it is much easier to link your database's connection details to a new or existing [secret group](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#link-database-secrets-to-a-secret-group).

The necessary secrets to connect your workload will vary depending on the application in your workload.

[Some clients may use a connection string](https://redis.io/docs/latest/develop/connect/), while some clients may not support the connection string format.

The connection string `REDIS_MASTER_URL` takes the format `[redis|rediss]://[user:password@][host][:port]`. There is also `REDIS_CONNECT_COMMAND` for command-line clients.

You can supply connections details and secrets such as `host`, `password`, and `port`  to your workload if your application is configured to use these instead of a connection string.

### Available ports

| Port | Protocol | URI prefix |
| --- | --- | --- |
| 6379 | RESP | `redis[s]://` |

### Automatically inherit database connection details into your workload

1. Create a new [secret group](https://northflank.com/docs/v1/application/secure/manage-secret-groups) of runtime variables to connect in the running workload

2. Show addons and configure your addon with either `REDIS_MASTER_URL` or select connection details and secrets

3. Set the aliases required in your workload to access the secrets

4. Enable apply secrets to specific services/jobs and select the workloads you want to access the database

5. Create secret group

6. Go to one of the workloads that inherits from the group and check the environment page, you should see the inherited variables from the secret group

The connection string or secrets will now be available in your workload under the configured aliases, and your application will be able to connect to the database using them.

## Access Redis

You can use the connect command to access Redis using the Redis CLI, or connect a [GUI tool](https://redis.io/resources/tools/) using the `HOST` secret. The addon must be forwarded to connect using the host name.

### Secure local access

To forward Redis for local access using the [Northflank CLI](https://northflank.com/docs/v1/api/use-the-cli), copy and execute the forward addon command from the local access section of the overview.

You can then use the `REDIS_CONNECT_COMMAND` from the connection details page to access your Redis deployment using the command-line client, or use the connection details in your local development environment.

### External access

To access your Redis database externally, ensure deploy with TLS and publicly accessible are enabled on the settings page under networking. The connection details will be updated to include an external connect command, and the host will now resolve externally.

## Redis specifications

### Connection limits

By default, a maximum of 10,000 concurrent connections are allowed on a Redis addon.

Your addon will be able to handle more concurrent connections by increasing the available CPU and memory available. You can do this by selecting the compute plan on the [addon's resources page](https://northflank.com/docs/v1/application/databases-and-persistence/scale-a-database).

### Redis persistence

Redis is run with [AOF (Append Only File) persistence](https://redis.io/docs/management/persistence/) on Northflank. This may have implications for Redis instances with very high write workloads:

- Memory: AOF rewrites lead to elevated memory requirements. Redis is configured to reserve 20% of the available plan memory as a buffer for processes such as AOF rewrites.

- Disk: Running Redis with AOF persistence means that all write operations are persisted to disk. This can temporarily lead to higher storage requirements than the minimally recommended disk size, which is equal to the memory size.

- vCPU: AOF rewrites create a fork process which can temporarily require vCPU resources. The performance impact should be minimal and is usually not noticeable.

For custom requirements or configurations, please contact [[support@northflank.com](mailto:support@northflank.com)](mailto:support@northflank.com).

## Next steps

- [Configure Redis® for high availability: Use primary and read replicas, and Redis Sentinel for high availability Redis on Northflank.](/v1/application/databases-and-persistence/configure-addons-for-high-availability#redis)
- [Use the Northflank CLI: Learn how to create and manage projects on Northflank using the command line client.](/v1/api/use-the-cli)
- [Scale a database: Increase the storage size, number of replicas, and the available CPU and memory to improve availability and performance.](/v1/application/databases-and-persistence/scale-a-database)

* Redis is a registered trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Northflank is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Northflank.
