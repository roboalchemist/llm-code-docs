# Source: https://uptrace.dev/raw/features/querying/spans.md

# Querying Spans and Logs

> Master the Uptrace span query language including identifiers, filters, grouping, and aggregates for traces, logs, and events.

Uptrace provides a powerful querying language that enables you to filter, group, and aggregate your observability data effectively. The query language supports filters (`where _status_code = "error"`), grouping (`group by _group_id`), and aggregates (`p50(_dur_ms)`).

![Filters](/features/querying-spans/filtering.png)

## Prerequisites for Effective Querying

To write useful and performant queries, you need to pre-process raw data to ensure it has a well-defined structure. You can achieve this by:

- Recording contextual information in span [attributes](/opentelemetry/distributed-tracing#attributes) and [events](/opentelemetry/distributed-tracing#events)
- Using [structured logging](/glossary/structured-logging) for logs

For *searching* over spans and logs (as opposed to complex querying), Uptrace supports a more concise syntax described in the [searching documentation](/features/querying/searching).

## Query Language Components

### Identifiers

Identifiers are unquoted strings that reference span fields, attributes, and extract values from JSON. Examples include `_name`, `_display_name`, and `_dur_ms`.

**Important:** Span fields start with an underscore to distinguish them from attributes.

#### Built-in Span Fields

The following table lists all built-in span fields available for querying:

<table>
<thead>
  <tr>
    <th>
      Span Field
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
        _id
      </code>
    </td>
    
    <td>
      Unique span identifier
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _parent_id
      </code>
    </td>
    
    <td>
      Parent span identifier
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _trace_id
      </code>
    </td>
    
    <td>
      Trace identifier
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _name
      </code>
    </td>
    
    <td>
      Span operation name (used for grouping)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _event_name
      </code>
    </td>
    
    <td>
      Event name (for span events)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _display_name
      </code>
    </td>
    
    <td>
      Display name when <code>
        _name
      </code>
      
       is not enough.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _kind
      </code>
    </td>
    
    <td>
      Span kind (client, server, etc.)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _dur_ms
      </code>
    </td>
    
    <td>
      Span duration in milliseconds (float64)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _time
      </code>
    </td>
    
    <td>
      Span start time (microseconds accuracy)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _status_code
      </code>
    </td>
    
    <td>
      Span status code (ok, error, unset)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _status_message
      </code>
    </td>
    
    <td>
      Span status message
    </td>
  </tr>
</tbody>
</table>

#### Attribute Names

Attribute names are normalized by replacing dots with underscores. Common examples include:

<table>
<thead>
  <tr>
    <th>
      Attribute Name
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
        display_name
      </code>
    </td>
    
    <td>
      <a href="grouping#display-name">
        display.name
      </a>
      
       attribute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service_name
      </code>
    </td>
    
    <td>
      OpenTelemetry <code>
        service.name
      </code>
      
       attribute
    </td>
  </tr>
</tbody>
</table>

### Data Types

Uptrace supports the following attribute types, each with specific comparison operators:

<table>
<thead>
  <tr>
    <th>
      Attribute Type
    </th>
    
    <th>
      Supported Comparison Operators
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        str
      </code>
    </td>
    
    <td>
      <code>
        =
      </code>
      
      , <code>
        in
      </code>
      
      , <code>
        like
      </code>
      
      , <code>
        contains
      </code>
      
      , <code>
        ~
      </code>
      
       (regexp), <code>
        exists
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        int
      </code>
      
       and <code>
        float
      </code>
    </td>
    
    <td>
      <code>
        =
      </code>
      
      , <code>
        <
      </code>
      
      , <code>
        <=
      </code>
      
      , <code>
        >
      </code>
      
      , <code>
        >=
      </code>
      
      , <code>
        exists
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        bool
      </code>
    </td>
    
    <td>
      <code>
        =
      </code>
      
      , <code>
        !=
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        []str
      </code>
    </td>
    
    <td>
      <code>
        contains
      </code>
      
      , <code>
        exists
      </code>
    </td>
  </tr>
</tbody>
</table>

#### Type Specification

While type discovery is automatic, you can explicitly specify types when needed:

```sql
foo::string | bar::int | baz::float
```

For attributes with mixed types across spans (not recommended), you can query multiple types:

```sql
foo::string | foo::int
```

**Note:** Uptrace uses type information as a hint for reading columnar data, not for type conversion.

### Units

Specify attribute units by adding the unit name as a suffix to improve data interpretation and readability:

<table>
<thead>
  <tr>
    <th>
      Attribute
    </th>
    
    <th>
      Unit
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        http_read_bytes
      </code>
    </td>
    
    <td>
      <code>
        bytes
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        request_dur_ms_seconds
      </code>
    </td>
    
    <td>
      <code>
        seconds
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        elapsed_milliseconds
      </code>
    </td>
    
    <td>
      <code>
        milliseconds
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        memory_utilization
      </code>
    </td>
    
    <td>
      <code>
        utilization
      </code>
    </td>
  </tr>
</tbody>
</table>

If you cannot modify the attribute name, use aliases in queries:

```sql
sum(heap_size) as heap_size_bytes
```

### String Literals

Strings can be defined using single quotes, double quotes, or backticks:

```sql
"I'm a string\n"           -- Double quotes with escape sequences
'I\'m a string\n'          -- Single quotes with escape sequences
`^some-prefix-(\w+)$`      -- Backticks (no escape sequences, useful for regex)
```

## Query Clauses

### Filtering with WHERE

Use `where` clauses to filter spans and events by their attributes. The following examples demonstrate common filtering patterns:

<table>
<thead>
  <tr>
    <th>
      Filter Example
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
        where _status_code = "error"
      </code>
    </td>
    
    <td>
      Filter spans with error status (case-sensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where _display_name like "hello%"
      </code>
    </td>
    
    <td>
      Filter span names starting with "hello" (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where _display_name like "%hello"
      </code>
    </td>
    
    <td>
      Filter span names ending with "hello" (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where _display_name contains "hello"
      </code>
    </td>
    
    <td>
      Filter span names containing "hello" (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where _display_name contains "foo|bar"
      </code>
    </td>
    
    <td>
      Same as <code>
        _display_name contains "foo" OR _display_name contains "bar"
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where _dur_ms > 1ms
      </code>
    </td>
    
    <td>
      Duration greater than 1 millisecond (equivalent to <code>
        _dur_ms > 1000
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where http_request_content_length > 1kb
      </code>
    </td>
    
    <td>
      Content length greater than 1 kilobyte (equivalent to <code>
        http_request_content_length > 1024
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        where foo exists
      </code>
    </td>
    
    <td>
      Filter spans that have the <code>
        foo
      </code>
      
       attribute
    </td>
  </tr>
</tbody>
</table>

#### Supported Units in Filters

- **Time units:** `Î¼s` (microseconds), `ms` (milliseconds), `s` (seconds)
- **Size units:** `kb` (kilobytes), `mb` (megabytes), `gb` (gigabytes), `tb` (terabytes)

### Filtering Results with HAVING

Use `having` to filter aggregated query results after grouping:

```sql
group by service_name | having p50(_dur_ms) > 100ms
```

### Searching

You can use [search](/features/querying/searching) to filter query results using a simpler syntax:

```sql
search foo|bar -hello
```

This approach is more concise than complex `where` clauses for basic text matching.

### Grouping with GROUP BY

Group spans using `group by` clauses, similar to SQL. The following examples show common grouping patterns:

<table>
<thead>
  <tr>
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
        group by _group_id
      </code>
    </td>
    
    <td>
      Groups similar spans together
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        group by host_name
      </code>
    </td>
    
    <td>
      Groups spans by the <code>
        host_name
      </code>
      
       attribute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        group by service_name, service_version
      </code>
    </td>
    
    <td>
      Groups spans by combination of <code>
        service_name
      </code>
      
       and <code>
        service_version
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        group by lower(attribute)
      </code>
    </td>
    
    <td>
      Groups by lowercase value of <code>
        attribute
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extract(host_name, `^server-(\w+)$`) as host
      </code>
    </td>
    
    <td>
      Extracts and groups by a fragment from <code>
        host_name
      </code>
    </td>
  </tr>
</tbody>
</table>

You can use any [transformation function](#transform-functions) in the `group by` clause to modify values before grouping.

## Functions

### Aggregate Functions

Aggregate functions perform calculations on sets of values and return single values. They are commonly used with grouping to summarize data.

<table>
<thead>
  <tr>
    <th>
      Function
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
        count
      </code>
    </td>
    
    <td>
      <code>
        count()
      </code>
    </td>
    
    <td>
      Number of matched spans/logs/events
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        any
      </code>
    </td>
    
    <td>
      <code>
        any(_name)
      </code>
    </td>
    
    <td>
      Any (random) span name
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        anyLast
      </code>
    </td>
    
    <td>
      <code>
        anyLast(_name)
      </code>
    </td>
    
    <td>
      Any last span name
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        avg
      </code>
    </td>
    
    <td>
      <code>
        avg(_dur_ms)
      </code>
    </td>
    
    <td>
      Average span duration
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min
      </code>
      
      , <code>
        max
      </code>
    </td>
    
    <td>
      <code>
        max(_dur_ms)
      </code>
    </td>
    
    <td>
      Minimum/maximum span duration
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        sum
      </code>
    </td>
    
    <td>
      <code>
        sum(http_request_content_length)
      </code>
    </td>
    
    <td>
      Total sum of values
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        p50
      </code>
      
      , <code>
        p75
      </code>
      
      , <code>
        p90
      </code>
      
      , <code>
        p99
      </code>
    </td>
    
    <td>
      <code>
        p50(_dur_ms)
      </code>
    </td>
    
    <td>
      Span duration percentiles
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        top3
      </code>
      
      , <code>
        top10
      </code>
    </td>
    
    <td>
      <code>
        top3(code_function)
      </code>
    </td>
    
    <td>
      Top N most popular values
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        uniq
      </code>
    </td>
    
    <td>
      <code>
        uniq(http_client_ip)
      </code>
    </td>
    
    <td>
      Number of unique values
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        apdex
      </code>
    </td>
    
    <td>
      <code>
        apdex(500ms, 3s)
      </code>
    </td>
    
    <td>
      <a href="https://en.wikipedia.org/wiki/Apdex" rel="nofollow">
        Apdex
      </a>
      
       score
    </td>
  </tr>
</tbody>
</table>

#### Conditional Aggregates

Uptrace supports ClickHouse [if](https://clickhouse.com/docs/en/sql-reference/aggregate-functions/combinators#-if) combinator on aggregate functions for conditional calculations:

- `countIf(_status_code = "error")` - Count spans with error status
- `p50If(_dur_ms, service_name = "service1")` - P50 duration for specific service

#### Virtual Columns

Uptrace provides shortcuts for common aggregations to simplify queries:

<table>
<thead>
  <tr>
    <th>
      Virtual Column
    </th>
    
    <th>
      Equivalent Expression
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        _error_rate
      </code>
    </td>
    
    <td>
      <code>
        countIf(_status_code = "error") / count()
      </code>
    </td>
  </tr>
</tbody>
</table>

### Transform Functions

Transform functions accept a value and return a new value for each matched span/log/event. These functions are useful for data manipulation and formatting.

<table>
<thead>
  <tr>
    <th>
      Function
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
        lower
      </code>
    </td>
    
    <td>
      <code>
        lower(log_severity)
      </code>
    </td>
    
    <td>
      Converts string to lowercase
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        upper
      </code>
    </td>
    
    <td>
      <code>
        upper(log_severity)
      </code>
    </td>
    
    <td>
      Converts string to uppercase
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        perMin
      </code>
    </td>
    
    <td>
      <code>
        perMin(count())
      </code>
    </td>
    
    <td>
      Divides value by the number of minutes in the time interval
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        perSec
      </code>
    </td>
    
    <td>
      <code>
        perSec(count())
      </code>
    </td>
    
    <td>
      Divides value by the number of seconds in the time interval
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        trimPrefix(str, prefix)
      </code>
    </td>
    
    <td>
      <code>
        trimPrefix(str, "prefix")
      </code>
    </td>
    
    <td>
      Removes the specified leading prefix string
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        trimSuffix(str, suffix)
      </code>
    </td>
    
    <td>
      <code>
        trimSuffix(str, "suffix")
      </code>
    </td>
    
    <td>
      Removes the specified trailing suffix string
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extract(haystack, pattern)
      </code>
    </td>
    
    <td>
      <code>
        extract(host_name,
      </code>
      
      ^uptrace-prod-(\w+)$<code>
        )
      </code>
    </td>
    
    <td>
      Extracts a fragment using regular expression
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        replace(haystack, substring, replacement)
      </code>
    </td>
    
    <td>
      <code>
        replace(host_name, 'uptrace-prod-', '')
      </code>
    </td>
    
    <td>
      Replaces all occurrences of substring
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        replaceRegexp(haystack, pattern, replacement)
      </code>
    </td>
    
    <td>
      <code>
        replaceRegexp(host, `^`, 'prefix ')
      </code>
    </td>
    
    <td>
      Replaces all occurrences matching regular expression pattern
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        arrayJoin
      </code>
    </td>
    
    <td>
      <code>
        arrayJoin(db_sql_tables)
      </code>
    </td>
    
    <td>
      See ClickHouse <a href="https://clickhouse.com/docs/en/sql-reference/functions/array-join" rel="nofollow">
        arrayJoin
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseInt64
      </code>
    </td>
    
    <td>
      <code>
        parseInt64(str_with_int)
      </code>
    </td>
    
    <td>
      Parses string as 64-bit integer
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseFloat64
      </code>
    </td>
    
    <td>
      <code>
        parseFloat64(str_with_float)
      </code>
    </td>
    
    <td>
      Parses string as 64-bit float
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseDateTime
      </code>
    </td>
    
    <td>
      <code>
        parseDateTime(str_with_time)
      </code>
    </td>
    
    <td>
      Parses string as date with time
    </td>
  </tr>
</tbody>
</table>

#### Time Rounding Functions

Time rounding functions are particularly useful for time-series analysis and creating time-based aggregations:

<table>
<thead>
  <tr>
    <th>
      Function
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
        toStartOfDay
      </code>
    </td>
    
    <td>
      Rounds down to start of day
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        toStartOfHour
      </code>
    </td>
    
    <td>
      Rounds down to start of hour
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        toStartOfMinute
      </code>
    </td>
    
    <td>
      Rounds down to start of minute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        toStartOfSecond
      </code>
    </td>
    
    <td>
      Rounds down to start of second
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        toStartOfFiveMinutes
      </code>
    </td>
    
    <td>
      Rounds down to start of 5-minute interval
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        toStartOfTenMinutes
      </code>
    </td>
    
    <td>
      Rounds down to start of 10-minute interval
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        toStartOfFifteenMinutes
      </code>
    </td>
    
    <td>
      Rounds down to start of 15-minute interval
    </td>
  </tr>
</tbody>
</table>

## Complete Query Examples

You can combine filters, grouping, and aggregates to create powerful queries for comprehensive observability analysis.

### Daily Unique Visitors (Excluding Bots)

```sql
where user_agent_is_bot not exists | uniq(client_address) | group by toStartOfDay(_time)
```

This query identifies unique visitors per day while excluding bot traffic.

### Error Rate by Service

```sql
group by service_name | having count() > 100 | select service_name, _error_rate
```

This query calculates error rates for services with significant traffic (more than 100 requests).

### Top 10 Slowest Operations

```sql
where _dur_ms > 100ms | group by _name | top10(_name)
```

This query identifies the slowest operations based on 99th percentile duration.

![Querying](/features/querying-spans/querying.png)

## Query Performance Optimization

If your queries are taking too long to complete, apply these optimization strategies to improve performance:

### Narrow the Time Range

- Select shorter time periods when possible (e.g., "Last 1 hour" instead of "Last 24 hours")
- Consider the data volume when selecting time ranges

### Use System Filters

- Select specific systems when analyzing particular types of requests
- Example: Select `httpserver:all` system for HTTP request analysis
- This reduces the data scope significantly

### Add Group Filters

- Further narrow scope with `_group_id` filters
- Example: `where _group_id = 123456789`
- Group filters are highly efficient for targeted analysis

### Leverage Indexed Attributes

- Use [OpenTelemetry semantic conventions](/features/querying/semconv) for attribute names
- Uptrace optimizes [certain attributes](/features/querying/semconv#indexed-attributes) better than others
- Indexed attributes provide faster query performance

### Query Structure Best Practices

- Apply filters before grouping when possible to reduce data volume
- Use specific filters rather than broad pattern matching
- Limit the number of groups in `group by` clauses
- Consider using `having` clauses to filter aggregated results

## Common Query Patterns

### Error Analysis

```sql
-- Find error patterns by service
where _status_code = "error" | group by service_name, _name |
select service_name, _name, count(), p50(_dur_ms)
```

### Performance Monitoring

```sql
-- Monitor slow requests across services
where _dur_ms > 1s | group by service_name |
select service_name, count(), p95(_dur_ms), p99(_dur_ms)
```

### Traffic Analysis

```sql
-- Analyze request volume over time
group by toStartOfHour(_time), service_name |
select _time, service_name, count() as request_count
```

## See Also

- [Searching spans and logs](/features/querying/searching) - For simpler search syntax
- [OpenTelemetry Semantic Conventions](/features/querying/semconv) - For optimized attribute naming
- [Grouping Strategies](grouping) - Advanced grouping techniques
