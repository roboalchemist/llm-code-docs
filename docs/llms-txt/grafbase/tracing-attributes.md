# Source: https://grafbase.com/docs/gateway/telemetry/tracing-attributes.md

# Tracing Spans and Attributes

The Grafbase Gateway sends spans in certain points in the request execution. These spans are used to measure the time taken by the Gateway to execute a request and to provide insights into the request execution.

The following default attributes apply to all spans:

- `busy_ns`: Time the span remained active in nanoseconds.
- `code.filepath`: Code file path.
- `code.lineno`: Line number in the code where this span originated.
- `code.namespace`: Module name.
- `idle_ns`: Time the span remained idle in nanoseconds.
- `thread.id`: Runtime thread ID.
- `thread.name`: Runtime thread name.

## HTTP Request

**Span name**: `<VERB> <PATH>`.

The root span monitors the complete request lifecycle. Additional spans descend from this root span.

**Attributes**:

- `grafbase.kind`: The span kind, which is always `http-request` for the root span.
- `graphql.operations.name`: The name or names of the executed operation(s).
- `graphql.operations.type`: The type or types of the executed operation(s).
- `graphql.response.errors.count`: The number of errors in the response.
- `graphql.response.errors.count_by_code.codes`: Distinct error codes in the response.
- `graphql.response.errors.count_by_code.counts`: The number of errors for each distinct error code.
- `http.request.body.size`: The size of the request body.
- `http.request.header.x-forwarded-for`: The client IP address.
- `http.request.header.x-grafbase-client-name`: The name of the client.
- `http.request.header.x-grafbase-client-version`: The version of the client.
- `http.request.method`: The HTTP method.
- `http.response.body.size`: The size of the response body.
- `server.address`: The server address.
- `url.path`: The URL path.
- `user_agent.original`: The user agent.

## Authenticate

**Span name**: `authenticate`.

You'll only see this span if you enable authentication.

## Global Rate Limit

**Span name**: `rate limit`.

You'll only see this span if you enable global rate limiting with Redis storage.

## Operation Execution

**Span name**: `<OPERATION_NAME>`.

Operation execution spans are created for each operation in the request.

**Attributes**;

- `grafbase.kind`: The span kind, which is always `graphql-operation` for operation execution spans.
- `grafbase.operation.computed_name`: The name of the operation. For named operations, this shows the operation name. For unnamed operations, this shows a name derived from the query.
- `graphql.operation.document`: The normalized query that hides all possible data.
- `graphql.operation.type`: The type of the operation: `query`, `mutation` or `subscription`.
- `graphql.response_data.is_present`: Whether the response data is present.
- `graphql.response.errors.count_by_code`: Distinct error codes in the response with their counts.

## Operation Preparation

**Span name**: `prepare operation`.

This span plans the operation execution and operates as a child of the operation execution span.

## Subgraph Execution

**Span name**: `<SUBGRAPH_NAME>`.

The gateway creates subgraph execution spans for each subgraph in the request. These spans become children of the operation execution span.

**Attributes**:

- `subgraph.name`: The name of the subgraph.
- `grafbase.kind`: The span kind, which is always `subgraph-graphql-request` for subgraph execution spans.
- `graphql.operation.document`: The subgraph receives this query. The system replaces all data with variables to prevent exposure of sensitive data.
- `graphql.operation.type`: The type of the operation: `query`, `mutation` or `subscription`.
- `graphql.response_data.is_present`: Whether the response data is present.

## Subgraph Rate Limit

**Span name**: `rate limit`.

This span appears when you enable rate limiting to the subgraph with Redis storage.

**Attributes**:

- `subgraph.name`: The name of the subgraph.

## HTTP Request

**Span name**: `POST <PATH>`.

This span tracks HTTP requests to the subgraph. When you enable retries and requests fail, the gateway creates multiple spans. All spans act as children of the subgraph execution span.

**Attributes**:

- `http.request.method`: The HTTP method.
- `http.response.status_code`: The HTTP status code.
- `server.address`: The server address.
- `server.port`: The server port.