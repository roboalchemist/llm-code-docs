# Source: https://uptrace.dev/raw/features/querying/traces.md

# Querying Traces

> Query distributed traces by filtering spans, logs, and events across services using the multi-row trace query syntax.

While the [span query language](/features/querying/spans) operates on individual spans and logs, **trace queries** allow you to select entire traces based on the spans, logs, and events they contain. This is useful for finding traces that match complex criteria across multiple services and operations.

For example, you can find all traces that contain a slow database query, have an error in a specific service, or involve a particular combination of microservices.

![Querying Traces UI](/features/querying-traces/ui.png)

## Query Structure

A trace query consists of multiple rows, where each row targets a different part of the trace. The first row is always the **root** row, and subsequent rows define conditions on child spans, logs, or events.

```text
root: <query for the root span>
<system> as <alias>: <query for matching spans>
```

Each row accepts the full [span query language](/features/querying/spans) including filters, aggregations, and groupings. A typical root row query looks like:

```text
root: perMin(count()) | quantiles(_dur_ms) | group by _group_id
```

<table>
<thead>
  <tr>
    <th>
      Component
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        root
      </code>
    </td>
    
    <td>
      Selects the root span of the trace. Use <code>
        <empty>
      </code>
      
       to match all root spans.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <system>
      </code>
    </td>
    
    <td>
      A <a href="/features/querying/grouping#span-systems">
        span system
      </a>
      
       like <code>
        db:postgresql
      </code>
      
      , <code>
        rpc:all
      </code>
      
      , or <code>
        log:error
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        as <alias>
      </code>
    </td>
    
    <td>
      An optional alias for readability.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <query>
      </code>
    </td>
    
    <td>
      Full query with <a href="/features/querying/spans#filters">
        where
      </a>
      
      , <a href="/features/querying/spans#groupings">
        group by
      </a>
      
      , and <a href="/features/querying/spans#aggregations">
        aggregate
      </a>
      
       clauses.
    </td>
  </tr>
</tbody>
</table>

## Filtering by System

Each non-root row targets spans belonging to a specific [system](/features/querying/grouping#span-systems). You can use exact systems or wildcard systems with `:all`:

<table>
<thead>
  <tr>
    <th>
      System
    </th>
    
    <th>
      Matches
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        db:postgresql
      </code>
    </td>
    
    <td>
      PostgreSQL database spans only
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        db:mysql
      </code>
    </td>
    
    <td>
      MySQL database spans only
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        db:all
      </code>
    </td>
    
    <td>
      All database spans (PostgreSQL, MySQL, etc)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rpc:grpc
      </code>
    </td>
    
    <td>
      gRPC spans only
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rpc:all
      </code>
    </td>
    
    <td>
      All RPC spans
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http:service1
      </code>
    </td>
    
    <td>
      HTTP spans for <code>
        service1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpserver:all
      </code>
    </td>
    
    <td>
      All HTTP server spans
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        messaging:kafka
      </code>
    </td>
    
    <td>
      Kafka messaging spans only
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        messaging:all
      </code>
    </td>
    
    <td>
      All messaging spans
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        log:error
      </code>
    </td>
    
    <td>
      Error-level logs
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        log:warn
      </code>
    </td>
    
    <td>
      Warning-level logs
    </td>
  </tr>
</tbody>
</table>

## Examples

### Traces with the Number of Database Queries

Return traces along with how many database queries each trace contains:

```text
root: perMin(count()) | quantiles(_dur_ms) | _error_rate | group by _group_id
db:all as db: count()
```

### Traces with Multiple Database Queries

Find traces that contain at least 2 PostgreSQL queries:

```text
root: perMin(count()) | quantiles(_dur_ms) | _error_rate | group by _group_id
db:postgresql as pg: having count() >= 2
```

This is useful for identifying N+1 query problems or traces with excessive database calls.

### Traces with Slow Service Calls

Find traces where a specific service takes longer than 1 second to respond:

```text
root: perMin(count()) | quantiles(_dur_ms) | _error_rate | group by _group_id
rpc:all as rpc: where service_name = "foo" | where _kind = "server" | where _dur_ms >= 1000
```

### Traces with Error Logs

Find traces that contain error logs mentioning "timeout":

```text
root: perMin(count()) | quantiles(_dur_ms) | _error_rate | group by _group_id
log:error as err: _display_name contains "timeout"
```

### Traces with Errors in a Specific Service

Find traces where a particular service returned an error:

```text
root: perMin(count()) | quantiles(_dur_ms) | _error_rate | group by _group_id
rpc:all as rpc: where service_name = "payment-service" | where _status_code = "error"
```

### Traces with Slow Root Spans

Find traces where the root span exceeds 5 seconds:

```text
root: where _dur_ms >= 5000
```

### Combining Multiple Conditions

Find traces that are slow **and** contain database errors:

```text
root: where _dur_ms >= 3000
db:all as db: where _status_code = "error"
```

This selects traces where the overall duration exceeds 3 seconds and at least one database span has an error status.

## Available Clauses

Each row â both root and child â supports the full [span query language](/features/querying/spans) including filters, aggregations, and groupings:

<table>
<thead>
  <tr>
    <th>
      Clause
    </th>
    
    <th>
      Example
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        where
      </code>
    </td>
    
    <td>
      <code>
        where service_name = "foo"
      </code>
    </td>
    
    <td>
      Filter spans by attribute values
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where
      </code>
    </td>
    
    <td>
      <code>
        where _dur_ms >= 1000
      </code>
    </td>
    
    <td>
      Filter by span duration
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where
      </code>
    </td>
    
    <td>
      <code>
        where _status_code = "error"
      </code>
    </td>
    
    <td>
      Filter by status code
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where
      </code>
    </td>
    
    <td>
      <code>
        where _kind = "server"
      </code>
    </td>
    
    <td>
      Filter by span kind
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where
      </code>
    </td>
    
    <td>
      <code>
        where _display_name contains "text"
      </code>
    </td>
    
    <td>
      Filter by display name
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        group by
      </code>
    </td>
    
    <td>
      <code>
        group by _group_id
      </code>
    </td>
    
    <td>
      Group spans by attribute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        group by
      </code>
    </td>
    
    <td>
      <code>
        group by service_name
      </code>
    </td>
    
    <td>
      Group by service
    </td>
  </tr>
  
  <tr>
    <td>
      Aggregates
    </td>
    
    <td>
      <code>
        count()
      </code>
      
      , <code>
        perMin(count())
      </code>
    </td>
    
    <td>
      Count and rate aggregations
    </td>
  </tr>
  
  <tr>
    <td>
      Aggregates
    </td>
    
    <td>
      <code>
        p50(_dur_ms)
      </code>
      
      , <code>
        quantiles(_dur_ms)
      </code>
    </td>
    
    <td>
      Duration percentiles
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        having
      </code>
    </td>
    
    <td>
      <code>
        having count() >= 2
      </code>
    </td>
    
    <td>
      Filter by aggregated span count
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        having
      </code>
    </td>
    
    <td>
      <code>
        having p99(_dur_ms) >= 500
      </code>
    </td>
    
    <td>
      Filter by percentile duration
    </td>
  </tr>
</tbody>
</table>

Multiple clauses can be chained with the pipe `|` operator:

```text
rpc:all as rpc: where service_name = "foo" | where _kind = "server" | where _dur_ms >= 1000
```

## See Also

- [Querying spans and logs](/features/querying/spans) - Query language fundamentals
- [Searching spans and logs](/features/querying/searching) - Simpler search syntax
- [Grouping and systems](/features/querying/grouping) - How span systems work
