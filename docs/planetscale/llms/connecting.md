# Source: https://planetscale.com/docs/postgres/connecting.md

# Connections overview

> There are several ways to connect to Postgres databases, each with their advantages and tradeoffs.

## Connecting to your PlanetScale Postgres database

Connecting to your PlanetScale Postgres database involves understanding several key components. This page provides an overview of connection options — for detailed instructions, see the linked documentation below.

### Roles and credentials

PlanetScale provides two types of roles for database access:

* **Default postgres role** — A near-superuser role with extensive permissions, ideal for administrative tasks and initial database setup. This role should not be used for application connections.
* **User-defined roles** — Custom roles with specific permission sets that follow the principle of least privilege. These are recommended for all application connections and allow credential rotation without downtime.

Connection credentials include a hostname, username (formatted as `{role}.{branch_id}`), password (prefixed with `pscale_pw_`), and database name. Learn more about [managing roles and creating credentials](/docs/postgres/connecting/roles).

### Connection strings

PlanetScale databases require SSL/TLS encryption for all connections. Connection strings include parameters for the host, port, username, password, database name, and SSL configuration. The port determines the connection method:

* **Port 5432** — Direct connections to Postgres, bypassing PgBouncer
* **Port 6432** — Connections through PgBouncer for connection pooling

The [connections quickstart](/docs/postgres/connecting/quickstart) provides detailed connection string examples and explains when to use each connection method.

### Private connectivity

For enhanced security and reduced latency, PlanetScale supports private connectivity that keeps traffic within cloud provider networks:

* **AWS PrivateLink** — Establishes private connections from your AWS VPC to PlanetScale databases without exposing traffic to the public internet. See the [AWS PrivateLink documentation](/docs/postgres/connecting/private-connections/aws-privatelink).
* **GCP Private Service Connect** — Provides private connectivity from your Google Cloud VPC to PlanetScale databases. See the [GCP Private Service Connect documentation](/docs/postgres/connecting/private-connections/gcp-private-service-connect).

### Neon Serverless Driver

For serverless and edge environments, PlanetScale supports connections via the [Neon serverless driver](/docs/postgres/connecting/neon-serverless-driver). This driver is optimized for platforms like Vercel Functions, AWS Lambda, and edge runtimes like Cloudflare Workers. Both HTTP and WebSocket modes are supported, HTTP mode for simple one-shot queries, and WebSocket mode for transactions and session-based features.

## Understanding Postgres connections

Postgres uses a connection-per-process architecture. Each connection made to a Postgres server [spawns a new process](https://planetscale.com/blog/processes-and-threads), which consumes system resources including memory and CPU. For this reason, it's important to manage the number of direct connections to keep the system performant.

Connection pooling is the primary solution to this challenge. In the Postgres ecosystem, [PgBouncer](https://www.pgbouncer.org/) is the most widely-used connection pooler. PgBouncer instances sit between clients and the Postgres server, maintaining a small pool of connections to Postgres while accepting a much larger number of client connections. PgBouncer routes client requests through these pooled connections efficiently.

## Connection options

PlanetScale provides several ways to connect to your Postgres database:

1. **Direct primary connections** - Connect directly to your Postgres primary server on port `5432`. This provides the lowest latency and full Postgres session capabilities. Use this for administrative tasks, long-running operations, and data imports.

2. **Direct replica connections** - Connect directly to read-only replicas on port `5432` by appending `|replica` to your username. Use this for read-only queries that can tolerate replication lag.

3. **Local PgBouncer (primary only)** - All Postgres databases include a local PgBouncer running on the same host as the primary. Connect via port `6432`. This is recommended for all application connections to the primary.

4. **Dedicated replica PgBouncer** - Create dedicated PgBouncer instances that pool connections to your replicas. These run on separate nodes and are useful for read-heavy workloads. Connect via port `6432` with the PgBouncer name appended to your username.

5. **Dedicated primary PgBouncer** - Create dedicated PgBouncer instances that pool connections to your primary database. These run on separate nodes and provide improved high availability, with connections persisting through cluster resizes, upgrades, and most failover scenarios. Connect via port `6432` with the PgBouncer name appended to your username.

The following sections describe each option in detail to help you choose the right connection method for your use case.

## Direct primary connections

Direct connections provide the lowest-latency access to your Postgres primary instance.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png?fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=2a840a2f0a8dbbfe08873fd00218c8d4" alt="Direct connections" style={{ maxHeight: '250px', width: 'auto' }} data-og-width="1436" width="1436" data-og-height="720" height="720" data-path="docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png?w=280&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=6dd2b702b047c27dacbbfd2d99bce6f1 280w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png?w=560&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=80a242d1e349f0e90ee37a2d0821e11b 560w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png?w=840&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=4adf3f093c0bb4f6bc512891b054ff25 840w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png?w=1100&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=b79c78392a2a69b5d40b90a4dfb1daa0 1100w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png?w=1650&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=b75c3302150748c6ab8207e2b6b2b967 1650w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-direct-connect.png?w=2500&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=8177d33c936d06052fd88a0b2dd73d2c 2500w" />
</Frame>

However, these connections are considered *heavy-weight* since each one consumes significant resources. Direct connections are recommended only for specific scenarios:

1. Administrative tasks, like creating new databases/schemas, manual DDL commands, and installing extensions.
2. Long-running operations like `VACUUM`s and large analytical queries that are executed infrequently.
3. Importing data during a migration or other bulk-loading operations.
4. When you need features like `SET`, pub/sub, and other features not provided by PgBouncer pooled connections.

Because having too many direct connections degrades performance, PlanetScale sets `max_connections` to a conservative default value that varies depending on cluster size. To find this value, navigate to the "Clusters" page and select the "Parameters" tab.

<img src="https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png?fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=801d2653e9765b82900038d0edb026c1" alt="Navigate to the Cluster Parameters page" data-og-width="3006" width="3006" data-og-height="1296" height="1296" data-path="docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png?w=280&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=587b35c7f9093dc942071a74a7c4318b 280w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png?w=560&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=2ff3a7914d60fdafc5316ff1fe1c7979 560w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png?w=840&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=89566c8bdc5fdb0d2415d7a704f0ee3b 840w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png?w=1100&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=8421ca38f515b4cffeba734a98ca3294 1100w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png?w=1650&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=40015cd621076a730ae41ef365f2045a 1650w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/cluster-configuration-parameters-darkmode.png?w=2500&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=89370dd542ae0ec4767916edc3ec3cda 2500w" />

Search for `max_connections` to view the current configured value. This can be increased if necessary, though doing so requires careful consideration as increasing direct connections can negatively impact performance.

When the `max_connections` limit is reached, error messages like the following will appear:

```
FATAL: sorry, too many clients already
```

Or variations such as:

```
FATAL: remaining connection slots are reserved for non-replication superuser connections
```

For application connections outside of the specific use cases listed above, PgBouncer should be used instead.

## Direct replica connections

The main purpose for the default [Replicas](/docs/postgres/scaling/replicas) in a cluster is to maintain [high-availability](/docs/postgres/operations-philosophy), but they can also be used to handle read traffic. Since replicas are read-only, they are only capable of serving `SELECT` queries. All write traffic (`INSERT`, `UPDATE`, etc) must be sent to the primary.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png?fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=2b0958ff6f84878f6eb093924a4c939e" alt="Direct replica connections" style={{ maxHeight: '250px', width: 'auto' }} data-og-width="1936" width="1936" data-og-height="792" height="792" data-path="docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png?w=280&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=e7ee06700c9b07b64fa79d4d4757a72f 280w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png?w=560&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=1f743b850238e0792c719a82deed2954 560w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png?w=840&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=22ca449fae8cd0b53fda8008882df0c5 840w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png?w=1100&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=f916e538b8d42743a581078f58eb77f7 1100w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png?w=1650&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=12f78a1e567e1269acd46722b915d38a 1650w, https://mintcdn.com/planetscale-cad1a68a/-ubEebx1La8vHdTj/docs/images/assets/docs/postgres/connecting/diagram-replica-direct-connect.png?w=2500&fit=max&auto=format&n=-ubEebx1La8vHdTj&q=85&s=1bcea6276dc2373953a3833958cd9602 2500w" />
</Frame>

Replicas always experience some level of replication lag — the delay between data arriving at the primary and being replicated to a replica. Frequently, replication lag is measured in milliseconds, but it can grow to multiple seconds, especially when the server is experiencing high write traffic or network issues.

Because of these factors, queries should only be sent to replicas if they meet the following criteria: (A) they are read-only and (B) they can tolerate being slightly out-of-sync with the data on the primary. For reads that cannot tolerate this lag, send them to the primary.

To connect to a replica, append `|replica` to your credential username and use port `5432`. For example:

```bash  theme={null}
psql 'host=xxxxxxxxxx-useast1-1.horizon.psdb.cloud \
      port=5432 \
      user=postgres.xxxxxxxxxx|replica \
      password=pscale_pw_xxxxxxxxxxxxxxxxxx \
      dbname=my_database \
      sslnegotiation=direct \
      sslmode=verify-full \
      sslrootcert=system'
```

Learn more about replicas and when to use them in the [database replicas documentation](/docs/postgres/scaling/replicas).

## PgBouncer connections

PgBouncer provides connection pooling for your Postgres database, allowing applications to scale beyond the constraints of direct connections. Connections from application servers should be made via PgBouncer whenever possible. PlanetScale provides three types of PgBouncer instances:

### Local PgBouncer

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png?fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=9b9065fc891bd115df330a3e81ce3a89" alt="Local PgBouncer connections" style={{ maxHeight: '250px', width: 'auto' }} data-og-width="1992" width="1992" data-og-height="880" height="880" data-path="docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png?w=280&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=31db0ac4dc51e5b8c51f70b9bffebf6c 280w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png?w=560&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=2fb9e10eb2dec1afdaf9bd629586c07e 560w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png?w=840&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=50db56be8f8a93ac95c391c67888cae1 840w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png?w=1100&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=c8bcbf9763a6452e6bf1369cb6fe958d 1100w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png?w=1650&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=c3e7e4a499d051ec34013abc046342fd 1650w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-local-pgbouncer.png?w=2500&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=ff83356fd4a4d750702eeb0bea02c9b3 2500w" />
</Frame>

All PlanetScale Postgres databases include a local PgBouncer instance running on the same host node as the Postgres primary. This is recommended for all application connections to the primary. To connect via the local PgBouncer, use the same credentials as a direct connection but change the port from `5432` to `6432`.

<Note>
  The local PgBouncer only routes connections to the primary. To pool connections to replicas, use a [dedicated replica PgBouncer](#dedicated-replica-pgbouncers).
</Note>

### Dedicated replica PgBouncer

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png?fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=88b54024b5a322863603a313a4c638be" alt="Dedicated replica PgBouncer connections" style={{ maxHeight: '250px', width: 'auto' }} data-og-width="2656" width="2656" data-og-height="792" height="792" data-path="docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png?w=280&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=78ccf92159aff36d2a4a2dcf41a2394e 280w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png?w=560&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=b33f3bc676fc132157718499c9227714 560w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png?w=840&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=ec61ba42b30aa02d1f34996ab72a8392 840w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png?w=1100&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=43f6f6e7b04af1ce2731c4a9c786ecd7 1100w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png?w=1650&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=b1f879cb3f994eb9319f80e7e1985e76 1650w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-replica-pgbouncer.png?w=2500&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=ed626514b403d3fa46506295c9812018 2500w" />
</Frame>

[Dedicated replica PgBouncers](/docs/postgres/connecting/pgbouncer#dedicated-replica-pgbouncers) run on nodes separate from the Postgres instances and pool connections to your replicas. These are useful for read-heavy workloads that send significant read traffic to replicas.

### Dedicated primary PgBouncers

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png?fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=93af653242cfb44619b8596fc0836f20" alt="Dedicated primary PgBouncer connections" style={{ maxHeight: '250px', width: 'auto' }} data-og-width="2196" width="2196" data-og-height="880" height="880" data-path="docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png?w=280&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=5168a497d5221a954e0bee88309c4af3 280w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png?w=560&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=624fcb98078b2ec2cb0473938fc5c58d 560w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png?w=840&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=d7fe587d470147685011ca0ba0e4eec0 840w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png?w=1100&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=302054516a9b896ef9a6889884980a7f 1100w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png?w=1650&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=0dad20bce3db2f3c4fa648a6a66321a1 1650w, https://mintcdn.com/planetscale-cad1a68a/qlTxKzpSogl0IGN-/docs/images/assets/docs/postgres/connecting/diagram-dedicated-primary-pgbouncer.png?w=2500&fit=max&auto=format&n=qlTxKzpSogl0IGN-&q=85&s=ca399d7e3e61e9c055c2acbda263499e 2500w" />
</Frame>

[Dedicated primary PgBouncers](/docs/postgres/connecting/pgbouncer#dedicated-primary-pgbouncers) provide connection pooling for your primary database on nodes separate from the Postgres servers. Connections through dedicated PgBouncers persist through cluster resizes, upgrades, and most failover scenarios, providing improved high availability.

## Connecting to dedicated PgBouncers

Connect to replica or primary PgBouncers via port `6432` and append the name of the PgBouncer to your username. For example, if your PgBouncer is named `read-bouncer`, the connection username should be `postgres.xxxxxxxxxx|read-bouncer`.

```bash  theme={null}
psql 'host=xxxxxxxxxx-useast1-1.horizon.psdb.cloud \
      port=6432 \
      user=postgres.xxxxxxxxxx|read-bouncer \
      password=pscale_pw_xxxxxxxxxxxxxxxxxx \
      dbname=my_database \
      sslnegotiation=direct \
      sslmode=verify-full \
      sslrootcert=system'
```

Learn more about [creating, configuring, and connecting to PgBouncers](/docs/postgres/connecting/pgbouncer).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt