# Source: https://render.com/docs/metrics-streams.md

# Streaming Render Service Metrics — Push metrics for CPU, memory, and more to your OTel-compatible provider.

Workspaces with a *Professional* plan or higher can push a variety of service metrics (memory usage, disk capacity, etc.) to an [OpenTelemetry](https://opentelemetry.io/)-compatible observability provider, such as New Relic, Honeycomb, or Grafana.

[image: Example OpenTelemetry metrics in Grafana]

> *Render does not emit metrics for the following:*
>
> - [Static sites](static-sites)
> - [Cron jobs](cronjobs)
> - [One-off jobs](one-off-jobs)

## General setup

The following steps must be performed by a workspace [admin](team-members#member-roles):

1. From your workspace's home in the [Render Dashboard](https://dashboard.render.com), select *Integrations > Observability* in the left sidebar:

   [image: Selecting Integrations in the Render Dashboard]

2. Under *Metrics Stream*, click *+ Add destination*.

   The following dialog appears:

   [image: Setting a default metrics export in the Render Dashboard]

3. Select your observability provider from the dropdown. The dialog updates to display fields specific to your provider.

> If your provider isn't listed, select *Custom*. [Learn how to connect a custom provider.](#other-providers-custom)

4. Fill in the provider-specific fields.

   - See instructions for your provider [below](#provider-specific-config).

5. Click *Add destination*.

You're all set! Your provider will start receiving [reported metrics](#reported-metrics) from Render shortly.

## Provider-specific config

When creating a metrics stream for your workspace, you provide different information depending on your observability provider:

[image: Provider-specific metrics config in the Render Dashboard]

See details for each supported provider below, along with instructions for [other providers](#other-providers-custom). Please also consult your provider's documentation for additional information.

> If there’s a provider you’d like us to add to this list, please submit a [feature request](https://feedback.render.com).

### New Relic

For *Region*, select *US* or *EU* according to where your New Relic data is hosted.

For *License key*, create a new key with the following steps:

1. From your New Relic [API keys page](https://one.newrelic.com/api-keys), click *Create a key*.

   The following dialog appears:

   [image: Creating a New Relic API key]

2. For the *Key type*, select *Ingest - License*.
3. Add a descriptive *Name* (e.g., "Render Metrics Integration").
4. Click *Create Key*.

### Honeycomb

For *Region*, select *US* or *EU* according to where your Honeycomb data is hosted.

For *API key*, create a new key with the following steps:

1. In your Honeycomb dashboard, hover over *Manage Data* on the bottom left and click *Send Data*:

   [image: Clicking Send Data in Honeycomb]

2. Click *Manage API keys*.
3. Click *Create Ingest API Key*.

   The following dialog appears:

   [image: Creating a Honeycomb API key]

4. Add a descriptive *Name* (e.g., "Render Metrics Integration").
5. Make sure *Can create services/datasets* is enabled.
6. Click *Create*.

### Grafana

Obtain both your *Endpoint* and *API Token* with the following steps:

1. From your Grafana Cloud Portal (`grafana.com/orgs/[your-org-name]`), click *Details* for the Grafana stack you want to use:

   [image: Selecting a Grafana stack in the Grafana Cloud Portal]

2. Find the *OpenTelemetry* tile and click *Configure*.
3. Copy the value of *Endpoint for sending OTLP signals* (this is your *Endpoint*).
4. Under *Password / API Token*, click *Generate now*.
5. Add a token name (e.g., `render_metrics_integration`).
6. Click *Create Token*.
7. Copy the generated value starting with `glc_` (this is your *API Token*).

For more details, see the [Grafana documentation](https://grafana.com/docs/grafana-cloud/send-data/otlp/send-data-otlp/#manual-opentelemetry-setup-for-advanced-users).

### Datadog

> To simplify metrics ingestion with Datadog, Render pushes metrics in Datadog's native format instead of using OpenTelemetry.

Specify your *Datadog site*, according to where your Datadog data is hosted.

For *API key*, generate a new organization-level API key from your [organization settings page](https://app.datadoghq.com/organization-settings/api-keys). You _cannot_ use an application key or a user-scoped API key.

### Better Stack

Obtain both your *Ingesting host* and *Source token* with the following steps:

1. From your *Telemetry > Sources* page in Better Stack, click *Connect source*.

   The following page appears:

   [image: Creating a Better Stack source]

2. Add a descriptive *Name* (e.g., "Render Metrics Integration").
3. Select *OpenTelmetry* as the *Platform*.
4. Click *Connect source*.

   Better Stack creates the new source and redirects you to its details page.

5. Copy your source's *Ingesting host* URL and *Source token*.

### Signoz

Obtain both your Signoz *Endpoint* and *Ingestion key* with the following steps:

1. From your Signoz Cloud dashboard, select *Settings > Workspace Settings* in the left sidebar.
2. Switch to the *Ingestion* tab:

    [image: Ingestion keys in the Signoz Cloud dashboard]

3. Copy your *Ingestion URL* and provide it as your *Endpoint* in the Render Dashboard.

    Make sure to include `https://` at the beginning, for example:

    ```
    https://ingest.us.signoz.cloud
    ```

4. Create a *+ New ingestion key* or copy an existing one. Provide this value as your *Ingestion key* in the Render Dashboard.

After you save your changes, Render metrics start to appear in the *Metrics* tab of your Signoz Cloud dashboard within a few minutes:

[image: Render metrics in the Signoz Cloud dashboard]

### Groundcover

Obtain both your Groundcover *Endpoint* and *API key* with the following steps:

1. From your Groundcover dashboard, select *Settings > Access > Ingestion Keys* in the sidebar.
2. Click *Create key*.
3. For *Key type*, select *Third Party*.

> Each ingestion key should be dedicated to a single data source for better security and manageability.

4. Add a descriptive name (e.g., "Render Metrics Integration").
5. Click *Create*.
6. Copy your *Ingestion key* and provide it as your *API key* in the Render Dashboard.
7. Copy your *Managed OpenTelemetry endpoint* URL and provide it as your *Endpoint* in the Render Dashboard.

For more details, see the [Groundcover documentation](https://docs.groundcover.com/use-groundcover/remote-access-and-apis/ingestion-keys#creating-an-ingestion-key).

### Other providers (custom)

> Consult this section only if your observability provider isn't listed above.

Render can push service metrics to your OpenTelemetry-compatible endpoint, _if_ that endpoint authenticates requests via an API key provided as a bearer token in an `Authorization` header.

*If your provider's endpoint supports authentication via bearer token:*

1. Consult your provider's documentation to obtain your OpenTelemetry endpoint and API key.

2. Specify *Custom* as your provider in the metrics stream creation dialog, then provide your endpoint and API key in the corresponding fields.

*If your provider's endpoint requires a different authentication method:*

1. Please [submit a feature request](https://feedback.render.com) to let us know about your provider's requirements.

2. You can spin up your own OpenTelemetry collector (such as the official [vendor-agnostic implementation](https://github.com/open-telemetry/opentelemetry-collector)). Your collector's endpoint can receive metrics from Render, then transform and forward them to your provider using whatever authentication method it expects.

## Reported metrics

Render streams service metrics that pertain to the following categories:

- [CPU](#cpu)
- [Memory](#memory)
- [Network](#network)
- [HTTP requests](#http-requests)
- [Data storage](#data-storage)

All metrics use OpenTelemetry JSON format. The first component of each metric's name is `render` (e.g., `render.service.memory.usage`).

> *Some observability providers transform metric names to match their conventions.*
>
> For example, Grafana converts the metric `render.service.memory.usage` to `render_service_memory_usage_bytes`.
>
> After you set up your metrics stream, inspect incoming data in your provider's dashboard to verify how it identifies Render metrics.

See names, descriptions, and included properties for each reported metric below.

### Universal properties

All reported metrics include the following properties:

| Property | Description |
| --- | --- |
| `service.name` | The name of the service (e.g., `my-service`). Grafana displays this property as `job`. |
| `service.id` | The ID of the service (e.g., `srv-abc123`). |
| `service.instance.id` | For _most_ metrics, this is the ID of the metric's associated service instance (e.g., `srv-abc123-def456`). This is _not_ the case for [HTTP request metrics](#http-requests). Everything before the final hyphen is the service ID (`srv-abc123`), and the final component (`def456`) uniquely identifies the instance. This value enables you to segment metrics by individual instances of a [scaled service](scaling), and to identify when a service's instances are cycled as part of a redeploy. |

The following properties are also universal but optional:

| Property | Description |
| --- | --- |
| `service.project` | The name of the service's associated [project](projects), if it belongs to one (otherwise omitted). |
| `service.environment` | The name of the service's associated [environment](projects), if it belongs to one (otherwise omitted). |

### CPU

These metrics apply to all compute instances and datastores.

###### `render.service.cpu.limit`

The maximum amount of CPU available to a particular service instance (as determined by its instance type).

Includes [universal properties](#universal-properties) only.

###### `render.service.cpu.time`

The cumulative amount of CPU time used by a particular service instance, in seconds.

To visualize changes to CPU load over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

### Memory

These metrics apply to all compute instances and datastores.

###### `render.service.memory.limit`

The maximum amount of memory available to a particular service instance (as determined by its instance type), in bytes.

Includes [universal properties](#universal-properties) only.

###### `render.service.memory.usage`

The amount of memory that a particular service instance is currently using, in bytes.

Includes [universal properties](#universal-properties) only.

###### `render.service.memory.rss`

The amount of anonymous and swap cache memory that a particular service instance is currently using, in bytes.

Includes [universal properties](#universal-properties) only.

###### `render.service.memory.cache`

The amount of page cache memory that a particular service instance is currently using, in bytes.

Includes [universal properties](#universal-properties) only.

### Network

These metrics apply to all compute instances and datastores.

###### `render.service.network.transmit.bytes`

The cumulative number of bytes transmitted by a particular service instance.

To visualize changes to network traffic over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

###### `render.service.network.receive.bytes`

The cumulative number of bytes received by a particular service instance.

To visualize changes to network traffic over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

### HTTP requests

These metrics apply only to [web services](web-services).

> *HTTP request metrics are not reported per instance.*
>
> Render aggregates these metrics across all instances of a given web service. For these metrics, the value of [`service.instance.id`](#serviceinstanceid) matches that of [`service.id`](#serviceid).

###### `render.service.http.requests.total`

The cumulative number of HTTP requests that a given service has received _across all instances_, segmented by the properties below.

To visualize changes to request load over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `host` | The destination domain for incoming requests. This can be your service's `onrender.com` domain or any [custom domain](custom-domains) you've added. |
| `status_code` | The HTTP status code returned by the service (`200`, `404`, and so on). |

###### `render.service.http.requests.latency`

Provides a particular web service's p50, p95, or p99 response time, segmented by the properties below.

Includes [universal properties](#universal-properties), along with the following:

------

###### Property

`quantile`

###### Description

Indicates the percentile of the provided latency value. One of the following:

- `0.50` (p50)
- `0.95` (p95)
- `0.99` (p99)

---

###### Property

`host`

###### Description

The destination domain for incoming requests. This can be your service's `onrender.com` domain or any [custom domain](custom-domains) you've added.

---

###### Property

`status_code`

###### Description

The HTTP status code returned by the service instance (`200`, `404`, and so on).

------

### Data storage

Each of these metrics applies to one or more of [Render Postgres](postgresql), [Render Key Value](key-value), and [persistent disks](disks).

###### `render.service.disk.capacity`

The total capacity of a service's persistent storage, in bytes.

Applies to [Render Postgres](postgresql) databases and [persistent disks](disks).

Includes [universal properties](#universal-properties) only.

###### `render.service.disk.usage`

The amount of _occupied_ persistent storage for a service, in bytes.

Applies to [Render Postgres](postgresql) databases and [persistent disks](disks).

Includes [universal properties](#universal-properties) only.

#### Disk I/O

The following metrics apply to [Render Postgres](postgresql) and [Render Key Value](key-value) instances.

###### `render.service.disk.read.bytes`

The cumulative number of bytes read from disk by a particular service instance.

To visualize changes to disk read activity over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

###### `render.service.disk.read.count`

The cumulative number of read operations performed on disk by a particular service instance.

To visualize changes to disk read activity over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

###### `render.service.disk.write.bytes`

The cumulative number of bytes written to disk by a particular service instance.

To visualize changes to disk write activity over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

###### `render.service.disk.write.count`

The cumulative number of write operations performed on disk by a particular service instance.

To visualize changes to disk write activity over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

#### Render Key Value

The following metrics apply to [Render Key Value](key-value) instances.

###### `render.keyvalue.connections`

The number of active connections to a particular Render Key Value instance.

Includes [universal properties](#universal-properties) only.

###### `render.keyvalue.connection.limit`

The maximum number of concurrent connections supported for a particular Render Key Value instance (as determined by its instance type).

Includes [universal properties](#universal-properties) only.

#### Render Postgres

The following metrics apply to [Render Postgres](postgresql) instances.

###### `render.postgres.connections`

The number of active connections to a particular Render Postgres instance.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `database_name` | The name of the PostgreSQL database created in the instance (e.g., `my_db_abcd`). This value is helpful if your Render Postgres instance hosts [multiple databases](postgresql-creating-connecting#adding-multiple-databases-to-a-single-instance). This value usually does _not_ match the value of `service.name`. |

###### `render.postgres.connection.limit`

The maximum number of concurrent connections supported by a particular Render Postgres instance (as determined by its instance type).

Includes [universal properties](#universal-properties) only.

###### `render.postgres.database.size`

The size of a particular PostgreSQL database, in bytes.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `database_name` | The name of the PostgreSQL database created in the instance (e.g., `my_db_abcd`). |

###### `render.postgres.indexes.size`

The total size of all indexes in a particular PostgreSQL database, in bytes.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `database_name` | The name of the PostgreSQL database created in the instance (e.g., `my_db_abcd`). |

###### `render.postgres.replication.lag`

The delay between when a change occurs on the primary Render Postgres instance and when its [read replica](postgresql-read-replicas) (if it has any) _fully replicates_ that change, in milliseconds.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `replication_host` | The hostname or identifier of the read replica. |

###### `render.postgres.replication.apply.lag`

The delay between when a transaction commits on the primary Render Postgres instance and when its [read replica](postgresql-read-replicas) (if it has any) _applies_ those changes, in milliseconds.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `replication_host` | The hostname or identifier of the read replica. |

###### `render.postgres.slow.lock.count`

The total number of slow locks on a particular Render Postgres instance. A slow lock occurs when a query waits an extended period to acquire a database lock.

Includes [universal properties](#universal-properties) only.

###### `render.postgres.slow.lock.time`

The cumulative wait time for slow locks on a particular Render Postgres instance, in seconds.

Includes [universal properties](#universal-properties) only.

###### `render.postgres.table.scans`

The total number of sequential table scans performed on a particular database within a Render Postgres instance.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `database_name` | The name of the PostgreSQL database created in the instance (e.g., `my_db_abcd`). |

###### `render.postgres.transaction.exhaustion`

The percentage of available transaction IDs used by a particular PostgreSQL database. PostgreSQL databases have a maximum of approximately 2.1 billion transaction IDs before wraparound occurs.

Includes [universal properties](#universal-properties), along with the following:

| Property | Description |
| --- | --- |
| `database_name` | The name of the PostgreSQL database created in the instance (e.g., `my_db_abcd`). |

###### `render.postgres.transaction.volume`

The cumulative number of transactions (i.e., commits and rollbacks) on a particular Render Postgres instance.

To visualize changes to transaction activity over time, apply a `rate()` function or similar in your observability provider.

Includes [universal properties](#universal-properties) only.

### History of changes to reported metrics

------

###### Date

`2025-06-02`

###### Change

Added the following Render Postgres transaction metrics:

- [`render.postgres.transaction.exhaustion`](#render-postgres-transaction-exhaustion)
- [`render.postgres.transaction.volume`](#render-postgres-transaction-volume)

---

###### Date

`2025-05-13`

###### Change

Added the following Render Postgres metrics:

- [`render.postgres.table.scans`](#render-postgres-table-scans)
- [`render.postgres.replication.apply.lag`](#render-postgres-replication-apply-lag)

---

###### Date

`2025-04-30`

###### Change

Added the following Render Postgres metrics:

- [`render.postgres.database.size`](#render-postgres-database-size)
- [`render.postgres.indexes.size`](#render-postgres-indexes-size)
- [`render.postgres.slow.lock.count`](#render-postgres-slow-lock-count)
- [`render.postgres.slow.lock.time`](#render-postgres-slow-lock-time)

Added the following disk I/O metrics:

- [`render.service.disk.read.bytes`](#render-service-disk-read-bytes)
- [`render.service.disk.read.count`](#render-service-disk-read-count)
- [`render.service.disk.write.bytes`](#render-service-disk-write-bytes)
- [`render.service.disk.write.count`](#render-service-disk-write-count)

---

###### Date

`2025-04-17`

###### Change

Added the following datastore connection metrics:

- [`render.postgres.connections`](#render-postgres-connections)
- [`render.postgres.connection.limit`](#render-postgres-connection-limit)
- [`render.keyvalue.connections`](#render-keyvalue-connections)
- [`render.keyvalue.connection.limit`](#render-keyvalue-connection-limit)

Added the following memory metrics:

- [`render.service.memory.rss`](#render-service-memory-rss)
- [`render.service.memory.cache`](#render-service-memory-cache)

Added the following networking metrics:

- [`render.service.network.transmit.bytes`](#render-service-network-transmit-bytes)
- [`render.service.network.receive.bytes`](#render-service-network-receive-bytes)

---

###### Date

`2025-03-11`

###### Change

Added the following initial set of metrics:

- [`render.service.cpu.time`](#render-service-cpu-time)
- [`render.service.cpu.limit`](#render-service-cpu-limit)
- [`render.service.memory.usage`](#render-service-memory-usage)
- [`render.service.memory.limit`](#render-service-memory-limit)
- [`render.service.http.requests.latency`](#render-service-http-requests-latency)
- [`render.service.http.requests.total`](#render-service-http-requests-total)
- [`render.service.disk.capacity`](#render-service-disk-capacity)
- [`render.service.disk.usage`](#render-service-disk-usage)
- [`render.postgres.replication.lag`](#render-postgres-replication-lag)

------
