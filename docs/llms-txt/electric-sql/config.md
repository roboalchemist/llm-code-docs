# Source: https://electric-sql.com/docs/api/config.md

---
url: /docs/api/config.md
description: Configuration options for the Electric sync engine.
---

# Sync service configuration

This page documents the config options for [self-hosting](/docs/guides/deployment) the [Electric sync engine](/product/electric).

> \[!Warning] Advanced only
> You don't need to worry about this if you're using [Electric Cloud](/product/cloud).
>
> Also, the only required configuration options are `DATABASE_URL` and `ELECTRIC_SECRET`.

## Configuration

The sync engine is an [Elixir](https://elixir-lang.org) application developed at [packages/sync-service](https://github.com/electric-sql/electric/tree/main/packages/sync-service) and published as a [Docker](https://docs.docker.com/get-started/docker-overview) image at [electricsql/electric](https://hub.docker.com/r/electricsql/electric).

Configuration options can be provided as environment variables, e.g.:

```shell
docker run \
    -e "DATABASE_URL=postgresql://..." \
    -e "ELECTRIC_DB_POOL_SIZE=10" \
    -p 3000:3000 \
    electricsql/electric
```

These are passed into the application via [config/runtime.exs](https://github.com/electric-sql/electric/blob/main/packages/sync-service/config/runtime.exs).

## Database

### DATABASE\_URL

Postgres connection string. Used to connect to the Postgres database.

The connection string must be in the [libpg Connection URI format](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS) of `postgresql://[userspec@][hostspec][/dbname][?sslmode=<sslmode>]`.

The `userspec` section of the connection string specifies the database user that Electric connects to Postgres as. They must have the `REPLICATION` role.

For a secure connection, set the `sslmode` query parameter to `require`.

### ELECTRIC\_POOLED\_DATABASE\_URL

Postgres connection string. Used to connect to the Postgres database for anything but the replication, will default to the same as `DATABASE_URL` if not provided.

The connection string must be in the [libpg Connection URI format](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS) of `postgresql://[userspec@][hostspec][/dbname][?sslmode=<sslmode>]`.

The `userspec` section of the connection string specifies the database user that Electric connects to Postgres as. This can point to a connection pooler and does not need a `REPLICATION` role as it does not handle the replication.

This should point to the same instance as the main database URL, as Electric relies on transaction information for consistency reasons.

For a secure connection, set the `sslmode` query parameter to `require`.

This used to be called `ELECTRIC_QUERY_DATABASE_URL`, but that name is deprecated and will be removed in a future release.

### ELECTRIC\_DATABASE\_USE\_IPV6

Set to `true` to prioritise connecting to the database over IPv6. Electric will fall back to an IPv4 DNS lookup if the IPv6 lookup fails.

### ELECTRIC\_DB\_POOL\_SIZE

How many connections Electric opens as a pool for handling shape queries.

### ELECTRIC\_DATABASE\_CA\_CERTIFICATE\_FILE

The path on local disk to a file containing trusted certificate(s) that Electric will use to verify the database server identity.

Trusted certificates are those that have been signed by trusted certificate authorities (CA); they are also known as root certificates. Every operating system and most web browsers include a bundle of well-known root certificates (aka CA store). You can instruct Electric to use the default bundle provided by your OS by specifying an absolute path to it. [This page](https://neon.com/docs/connect/connect-securely#location-of-system-root-certificates) from Neon lists the typical locations for different operating systems.

Some managed Postgres providers such as Supabase and DigitalOcean use a self-signed root certificate that won't be found in OS-specific CA stores. If you're using one of those, download the trusted certificate from the provider's website and put it somewhere on your local disk where Electric can access it.

**Certificate verification and `sslmode`**

Electric doesn't support `sslmode=verify-ca` or `sslmode=verify-full` query params in `DATABASE_URL`. Those values are specific to `psql`. When you configure Electric with a trusted certificate file, it will always try to verify the server identity and will refuse to open a database connection if the verification does not succeed.

Note, however, that setting `sslmode=disable` in `DATABASE_URL` and enabling certificate verification at the same time will result in a startup error.

### ELECTRIC\_REPLICATION\_STREAM\_ID

Suffix for the logical replication publication and slot name.

### ELECTRIC\_REPLICATION\_IDLE\_TIMEOUT

After seeing no activity on the logical replication stream for this long, Electric will close all of its database connections. This allows the database server to scale-to-zero on supported providers.

While Electric is in the scaled-down mode, an incoming shape request will cause it to reopen database connections and restart the logical replication stream. The request itself will be held until it can be processed as usual to return a proper response.

The default value is 0, meaning the connection scaling down is disabled and Electric will keep its database connections open permanently.

**Important note on WAL growth**

Avoid setting this timeout if your database sees constant or frequent writes.

When Electric isn't streaming from the database, its replication slot is inactive. Postgres will continue to retain WAL files needed for the slot, since they are required to resume replication later. Over time, this can cause storage growth proportional to the volume of writes on the primary database, regardless of whether those writes target tables for which Electric has active shapes or not.

Once Electric reconnects and replication catches up, Postgres will automatically discard the no-longer-needed WAL segments. However, if the inactivity period is too long, the accumulated WAL may exceed available disk space, potentially interrupting database operations.

### ELECTRIC\_MANUAL\_TABLE\_PUBLISHING

Set to `true` to disable automatic addition/removal of database tables from the publication in Postgres.

In order to receive realtime updates as soon as they are committed in Postgres, Electric maintains a [publication](https://www.postgresql.org/docs/current/logical-replication-publication.html) inside the database and automatically adds tables to it for which shape subscriptions are established. This only works if Electric's database role owns the table or is granted the [group role](https://www.postgresql.org/docs/current/role-membership.html#ROLE-MEMBERSHIP) that owns the table.

If your permissions policies prevent Electric from using a role that can alter application tables, set this setting to `true` and manually add each table to the publication by executing

```sql
BEGIN;
ALTER PUBLICATION electric_publication_default ADD TABLE <my table>;
ALTER TABLE <my table> REPLICA IDENTITY FULL;
COMMIT;
```

before requesting a new shape for that table.

## Electric

### ELECTRIC\_SECRET

Secret for shape requests to the [HTTP API](/docs/api/http). This is required unless `ELECTRIC_INSECURE` is set to `true`.
By default, the Electric API is public and authorises all shape requests against this secret.
More details are available in the [security guide](/docs/guides/security).

### ELECTRIC\_INSECURE

When set to `true`, runs Electric in insecure mode and does not require an `ELECTRIC_SECRET`.
Use with caution.
API requests are unprotected and may risk exposing your database.
Good for development environments.
If used in production, make sure to [lock down access](/docs/guides/security#network-security) to Electric.

### ELECTRIC\_INSTANCE\_ID

A unique identifier for the Electric instance. Defaults to a randomly generated UUID.

### ELECTRIC\_SERVICE\_NAME

Name of the electric service. Used as a resource name in OTEL traces and metrics.

### ELECTRIC\_LISTEN\_ON\_IPV6

By default, Electric binds to IPv4. Enable this to listen on IPv6 addresses as well.

### ELECTRIC\_TCP\_SEND\_TIMEOUT


Timeout for sending a response chunk back to the client. Defaults to 30 seconds.

Slow response processing on the client or bandwidth restristrictions can cause TCP backpressure leading to the error message:

```
Error while streaming response: :timeout
```

This environment variable increases this timeout.

### ELECTRIC\_SHAPE\_CHUNK\_BYTES\_THRESHOLD

Limit the maximum size of a shape log response, to ensure they are cached by
upstream caches. Defaults to 10MB (10 \_ 1024 \_ 1024).

See [#1581](https://github.com/electric-sql/electric/issues/1581) for context.

### ELECTRIC\_PORT

Port that the [HTTP API](/docs/api/http) is exposed on.

### ELECTRIC\_SHAPE\_SUSPEND\_CONSUMER

Whether to terminate idle shape consumer processes after `ELECTRIC_SHAPE_HIBERNATE_AFTER` seconds. This saves on memory at the cost of slightly higher CPU usage. When receiving a transaction that contains changes matching a given shape, a consumer process is started to handle the update. If more transactions matching the shape appear within the time defined by `ELECTRIC_SHAPE_HIBERNATE_AFTER` then the consumer will remain active, if not it will be terminated.

If set to `false` the consumer processes will [hibernate](https://www.erlang.org/doc/apps/erts/erlang#hibernate/3) instead of terminating, meaning they still occupy some memory but are inactive until passed transaction operations to process.

If you enable this feature then you should configure `ELECTRIC_SHAPE_HIBERNATE_AFTER` to match the usage patterns of your application to avoid unnecessary process churn.

### ELECTRIC\_SHAPE\_HIBERNATE\_AFTER

The amount of time a consumer process remains active without receiving transaction operations before either [hibernating](https://www.erlang.org/doc/apps/erts/erlang#hibernate/3) or terminating (if `ELECTRIC_SHAPE_SUSPEND_CONSUMER` is `true`).

## Caching

### ELECTRIC\_CACHE\_MAX\_AGE

Default `max-age` for the cache headers of the HTTP API.

### ELECTRIC\_CACHE\_STALE\_AGE

Default `stale-age` for the cache headers of the HTTP API.

## Storage

### ELECTRIC\_PERSISTENT\_STATE

Where to store shape metadata. Defaults to storing on the filesystem.
If provided must be one of `MEMORY` or `FILE`.

### ELECTRIC\_STORAGE

Where to store shape logs. Defaults to storing on the filesystem.
If provided must be one of `MEMORY` or `FAST_FILE`.

### ELECTRIC\_STORAGE\_DIR

Path to root folder for storing data on the filesystem.

## Telemetry

These environment variables allow configuration of metric and trace export for visibility into performance of the Electric instance.

### ELECTRIC\_OTLP\_ENDPOINT

Set an [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) endpoint URL
to enable telemetry.

### ELECTRIC\_OTEL\_DEBUG

Debug tracing by printing spans to stdout, without batching.

### ELECTRIC\_HNY\_API\_KEY

[Honeycomb.io](https://www.honeycomb.io) api key. Specify along with `HNY_DATASET` to
export traces directly to Honeycomb, without the need to run an OpenTelemetry Collector.

### ELECTRIC\_HNY\_DATASET

Name of your Honeycomb Dataset.

### ELECTRIC\_PROMETHEUS\_PORT

Expose a prometheus reporter for telemetry data on the specified port.

### ELECTRIC\_STATSD\_HOST

Enable sending telemetry data to a StatsD reporting endpoint.

## Logging

### ELECTRIC\_LOG\_LEVEL

Verbosity of Electric's log output.

Available levels, in the order of increasing verbosity:

* `error`
* `warning`
* `info`
* `debug`

### ELECTRIC\_LOG\_COLORS

Enable or disable ANSI coloring of Electric's log output.

By default, coloring is enabled when Electric's stdout is connected to a terminal. This may be undesirable in certain runtime environments, such as AWS which displays ANSI color codes using escape sequences and may incorrectly split log entries into multiple lines.

### ELECTRIC\_LOG\_OTP\_REPORTS

Enable [OTP SASL](https://www.erlang.org/doc/apps/sasl/sasl_app.html) reporting at runtime.

## Usage reporting

### ELECTRIC\_USAGE\_REPORTING

These environment variables allow configuration of anonymous usage data reporting back to https://electric-sql.com

Configure anonymous usage data about the instance being sent to a central checkpoint service. Collected information is anonymised and doesn't contain any information from the replicated data. You can read more about it in our [telemetry docs](../reference/telemetry.md#anonymous-usage-data).
