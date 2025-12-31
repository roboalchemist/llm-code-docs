# Source: https://grafbase.com/docs/gateway/telemetry/metrics-attributes.md

# Metrics and Attributes

The Grafbase Gateway delivers metrics for requests and operations to an OpenTelemetry endpoint. Metrics include counters, histograms, and gauges at various points in the system.

The exponential histograms include a `Count` field, which doubles any histogram as a counter metric. If you can't find a specific counter, check if any of the histograms can serve that purpose.

## HTTP Request Duration

**Metric Name:** `http.server.request.duration`

This exponential histogram measures the time in milliseconds for each HTTP request and helps you track the final response time for those requests. It includes the following attributes:

- `http.response.status_code`: The HTTP status code.
- `http.request.method`: The HTTP request method.
- `http.route`: The request path.
- `network.protocol.version`: The HTTP version of the request.
- `server.address`: The server's listen address.
- `server.port`: The server's listen port.
- `url.scheme`: Either `http` or `https`, depending on whether TLS is enabled in the gateway.
- `http.headers.x-grafbase-client-name`: The name of the client that triggered this request, if available.
- `http.headers.x-grafbase-client-version`: The version of the client that triggered this request, if available.
- `graphql.response.status`: Indicates whether the underlying GraphQL operation succeeded, if available.

## Connected Clients

**Metric Name:** `http.server.connected.clients`

This up/down counter tracks currently connected clients, incrementing on an incoming request and decrementing upon any response.

## Request Body Sizes

**Metric Name:** `http.server.request.body.size`

This exponential histogram measures request body sizes.

## Response Body Sizes

**Metric Name:** `http.server.response.body.size`

This exponential histogram measures response body sizes.

## GraphQL Operation Duration

**Metric Name:** `graphql.operation.duration`

This exponential histogram measures the time in milliseconds for every valid operation in the GraphQL engine. The metric includes the following attributes:

- `graphql.document`: The normalized query of this operation, stripped of all variables. This value cannot contain any private data.
- `graphql.operation.type`: The type of the operation (either `query`, `mutation`, or `subscription`).
- `graphql.operation.name`: The name of the operation, if provided.
- `graphql.response.status`: Indicates if the response succeeded.
- `http.headers.x-grafbase-client-name`: The name of the client that triggered this request, if available.
- `http.headers.x-grafbase-client-version`: The version of the client that triggered this request, if available.

## GraphQL Operation Errors

**Metric Name:** `graphql.operation.errors`

This counter tracks distinct GraphQL errors per request. The metric contains the following attributes:

- `graphql.response.error.code`: The error code returned to the user.
- `graphql.operation.name`: The name of the operation, if present.
- `http.headers.x-grafbase-client-name`: The name of the client, if present.
- `http.headers.x-grafbase-client-version`: The version of the client, if present.

## Request Batch Sizes

**Metric Name:** `graphql.operation.batch.size`

This exponential histogram measures the number of batched requests sent to the engine. It counts the total number of batched requests while measuring the number of requests in the batch.

## Subgraph Request Duration

**Metric Name:** `graphql.subgraph.request.duration`

This exponential histogram measures the time in milliseconds for every subgraph request. It helps track execution time and includes the following attributes:

- `graphql.subgraph.name`: The requested subgraph's name.
- `graphql.subgraph.response.status`: Indicates if the response succeeded.
- `http.response.status_code`: The HTTP status code.

## Subgraph Retries

**Metric Name:** `graphql.subgraph.request.retries`

This counter tracks retried subgraph requests. To enable this counter, you must [enable retries](https://grafbase.com/docs/gateway/configuration.md). The counter increments when a subgraph request fails and the engine retries it. The metric includes the following attributes:

- `graphql.subgraph.name`: The requested subgraph's name.
- `graphql.subgraph.aborted`: Indicates if the retries stopped and if the request became an error.

## Subgraph Request Sizes

**Metric Name:** `graphql.subgraph.request.body.size`

This exponential histogram measures subgraph request body sizes in bytes. The metric includes the following attribute:

- `graphql.subgraph.name`: The requested subgraph's name.

## Subgraph Response Sizes

**Metric Name:** `graphql.subgraph.response.body.size`

This exponential histogram measures successful subgraph response body sizes in bytes. The metric includes the following attribute:

- `graphql.subgraph.name`: The requested subgraph's name.

## Subgraph In-Flight Requests

**Metric Name:** `graphql.subgraph.request.inflight`

This up/down counter tracks in-flight subgraph requests. It increments when requesting a subgraph and decrements upon any response. The metric includes the following attribute:

- `graphql.subgraph.name`: The requested subgraph's name.

## Subgraph Cache Hits

**Metric Name:** `graphql.subgraph.request.cache.hit`

This counter tracks hits of subgraph entity caches. Enable this counter by [activating entity caching](https://grafbase.com/docs/gateway/performance/entity-caching.md). The metric includes the following attribute:

- `graphql.subgraph.name`: The requested subgraph's name.

## Subgraph Cache Misses

**Metric Name:** `graphql.subgraph.request.cache.miss`

This counter tracks misses of subgraph entity caches. Enable this counter by [activating entity caching](https://grafbase.com/docs/gateway/performance/entity-caching.md). The metric includes the following attribute:

- `graphql.subgraph.name`: The requested subgraph's name.

## Operation Cache Hits

**Metric Name:** `graphql.operation.cache.hit`

This counter tracks hits for operation plan caches.

## Operation Cache Misses

**Metric Name:** `graphql.operation.cache.miss`

This counter tracks misses for operation plan caches.

## Operation Preparation Duration

**Metric Name:** `graphql.operation.prepare.duration`

This exponential histogram measures the time in milliseconds taken to prepare an operation. This includes:

- Fetching a trusted document, if enabled and available.
- Fetching a query plan from the in-memory cache.
- If the plan is not cached, parsing the query into an AST and then determining the plan.

The metric includes the following attributes:

- `graphql.operation.name`: The name of the operation, if present.
- `graphql.document`: The normalized operation if parsing succeeds.
- `graphql.operation.success`: Indicates if the preparation finished successfully.

## Hook Duration

**Metric Name:** `grafbase.hook.duration`

This exponential histogram measures the time in milliseconds taken to execute a [hook](/guides/implementing-gateway-hooks). The metric includes the following attributes:

- `grafbase.name.hook`: The name of the hook function.
- `grafbase.hook.status`: Indicates if the hook call succeeded (`SUCCESS`), or if it failed due to errors from Grafbase code (`HOST_ERROR`), or from user code (`GUEST_ERROR`).

## Hook Pool Busy Instances

**Metric Name:** `grafbase.hook.pool.instances.busy`

This counter counts the number of active instances in the hook instance pool. Each instance processes one request at a time, which is why the gateway utilizes a pool to handle multiple requests concurrently.

## Hook Pool Instances Size

**Metric Name:** `grafbase.hook.pool.instances.size`

This counter tracks the total number of instances in the hook instance pool. [Configure the maximum pool size in the gateway configuration](https://grafbase.com/docs/gateway/configuration/hooks.md). The gateway adjusts the pool size automatically based on the current load.

## Pending Access Logs

**Metric Name:** `grafbase.gateway.access_log.pending`

This counter measures the amount of access log events not yet written to the access log file. [Read more](/guides/implementing-gateway-hooks#access-logs-with-response-hooks) on access logs.

## Rate-Limit Duration

**Metric Name:** `grafbase.gateway.rate_limit.duration`

This exponential histogram measures the time in milliseconds taken to query the current request rate from Redis. This metric requires enabling the [Redis-based rate-limiting](https://grafbase.com/docs/gateway/security/rate-limiting.md).

## Object Storage Fetch Duration

**Metric Name:** `object_storage.request.duration`

This exponential histogram measures the time in milliseconds to fetch a graph from object storage. This metric only activates in [hybrid mode](https://grafbase.com/docs/self-hosted-gateway.md). The metric includes the following attributes:

- `server.address`: The Graph Delivery Network endpoint URL.
- `object_storage.response.kind`: The response status kind, either `new`, `unchanged`, `http_error`, or `object_storage_error`.
- `http.response.status_code`: The status code of the request.