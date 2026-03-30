# Source: https://uptrace.dev/raw/features/querying/logs-grouping.md

# Logs grouping

> Create pattern based log grouping rules that normalize noisy messages and generate consistent fingerprints for recurring issues.

Grouping rules allow to change how Uptrace groups logs and exceptions together. It works by specifying grouping patterns and a unique fingerprint.

For example, you can configure Uptrace to create a separate error group for each unknown PostgreSQL column:

```text
# Error messages
ERROR: column "event.created_at" does not exist (SQLSTATE=42703)
ERROR: column "updated_at" does not exist (SQLSTATE=42703)
ERROR: column "name" does not exist (SQLSTATE=42703)

# Pattern
log.severity=ERROR column column_name=<quoted,fingerprint> does not exist sqlstate=<kv>
```

## Patterns

A grouping pattern is a string that is used to match log and exception messages, for example, the following pattern:

```text
<time> unknown column column=<word,fingerprint> on node node_id=<number>
```

Matches the following log messages:

```text
02 Jan 06 15:04 MST unknown column foo on node 10
2006-01-02T15:04:05Z07:00 unknown column bar on node 199
Jan 2 15:04:05 unknown column hello on node 0
```

The pattern consists of matchers separated with a space. Uptrace supports the following matchers:

<table>
<thead>
  <tr>
    <th>
      Matcher
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
        word
      </code>
    </td>
    
    <td>
      Matches the word literally and case-sensitively, for example,<code>
        foo
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <number>
      </code>
    </td>
    
    <td>
      Matches ints and floats, e.g. <code>
        123.456
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <severity>
      </code>
    </td>
    
    <td>
      Matches log severity levels, e.g. <code>
        INFO
      </code>
      
      , <code>
        WARN
      </code>
      
      , <code>
        ERROR
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <http_method>
      </code>
    </td>
    
    <td>
      Matches HTTP request methods, e.g. <code>
        GET
      </code>
      
      , <code>
        POST
      </code>
      
      , <code>
        PUT
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <month>
      </code>
    </td>
    
    <td>
      Matches month names, e.g. <code>
        Jan
      </code>
      
      , <code>
        JAN
      </code>
      
      , <code>
        January
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <day>
      </code>
    </td>
    
    <td>
      Matches day names, e.g. <code>
        Mon
      </code>
      
      , <code>
        MON
      </code>
      
      , <code>
        Monday
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <word>
      </code>
    </td>
    
    <td>
      Matches words except <code>
        <severity>
      </code>
      
      , <code>
        <month>
      </code>
      
      , <code>
        <day>
      </code>
      
      : <code>
        ^[a-zA-Z]$
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <ident>
      </code>
    </td>
    
    <td>
      Matches identifiers including <code>
        <word>
      </code>
      
      : <code>
        ^[a-zA-Z0-9\.-]$
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <hex32>
      </code>
    </td>
    
    <td>
      Matches 32-bytes hex strings such as used for trace ids.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <uuid>
      </code>
    </td>
    
    <td>
      Matches UUIDs, e.g. <code>
        88da75f6-a07e-40b3-8c62-f2b28c505ff2
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <time>
      </code>
    </td>
    
    <td>
      Matches time in one of the formats supported by Uptrace.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <quoted>
      </code>
    </td>
    
    <td>
      Matches any text in single or double quotes, e.g. <code>
        "foo"
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <path>
      </code>
    </td>
    
    <td>
      Matches Unix absolute paths, e.g. <code>
        /var/log/syslog
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <url>
      </code>
    </td>
    
    <td>
      Matches HTTP URLs, e.g. <code>
        http://mydomain.com/foo/bar
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <ip>
      </code>
    </td>
    
    <td>
      Matches IP addresses, e.g. <code>
        127.0.0.1
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <email>
      </code>
    </td>
    
    <td>
      Matches email addresses, e.g. <code>
        admin@localhost
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <hashtag>
      </code>
    </td>
    
    <td>
      Matches hashtags, e.g. <code>
        #uptrace
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <kv>
      </code>
    </td>
    
    <td>
      Matches key-value pair, e.g. <code>
        foo=bar
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <json>
      </code>
    </td>
    
    <td>
      Matches valid JSON objects, e.g. <code>
        {"foo": "bar"}
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        <any>
      </code>
    </td>
    
    <td>
      Matches anything.
    </td>
  </tr>
</tbody>
</table>

Matchers can be capturing (`id=<number>`) and non-capturing (`<number>`). A capturing matcher records the matched value in an attribute.

You can have multiple patterns in a single grouping rule, for example:

```text
can't find item item_id=<number>
can not find item item_id=<number>
item_id=<number> not found
```

## Fingerprints

Uptrace groups similar logs and exceptions together by hashing certain parts of the message. By default, Uptrace only hashes words, but you can use the `fingerprint` option to hash other values as well.

For example:

```text
unknown column: column=<word,fingerprint>
```

The pattern above will create a separate group for each column which can be useful for [alerting](/features/alerting) purposes:

```text
# Group 1
unknown column: foo
unknown column: foo
unknown column: foo

# Group 2
unknown column: bar
unknown column: bar
unknown column: bar
```

Note that you can also specify fingerprints in the `grouping.fingerprint` attribute when creating logs and exceptions:

```go
span := trace.SpanFromContext(ctx)

span.AddEvent("exception", trace.WithAttributes(
    attribute.String("exception.type", "*exec.ExitError"),
    attribute.String("exception.message", "exit status 1"),
    attribute.String("grouping.fingerprint", "exec.ExitError"),
))
```

When present, such fingerprints will override fingerprints automatically derived by Uptrace.

## Span duration

If your logs contain durations, you can convert them to spans to get percentiles and heatmaps. To achieve that, you need to capture the duration in the `.duration` attribute and specify the duration unit.

For example, the example below uses `.duration=<number,unit=seconds>` to capture requests duration:

```text
# Logs
Serving POST /booper/bopper/mooper/mopper took 0.123
Serving GET /ping took 0.567
Serving DELETE /wp-admin took 1.12

# Pattern
Serving http.request.method=<http_method> url.path=<path> took .duration=<number,unit=seconds>
```

## Examples

Go-style error messages:

```text
# Messages
strconv.ParseInt failed
SendEmail failed
mypkg.MyFunc failed

# Pattern
code.function=<ident,fingerprint> failed
```

PostgreSQL unknown column errors:

```text
# Error messages
ERROR: column "event.created_at" does not exist (SQLSTATE=42703)
ERROR: column "updated_at" does not exist (SQLSTATE=42703)
ERROR: column "name" does not exist (SQLSTATE=42703)

# Pattern
log.severity=ERROR column column_name=<quoted,fingerprint> does not exist sqlstate=<kv>
```

AWS CloudWatch JSON logs:

```text
# Log messages
api_version=2022-09-13 http_version=1.1 ip=84.45.193.139 method=GET request=/foo/bar request_id=Root=1-6529223f-17f6868713d13299499b8b9d request_time=0.099 status=200
api_version=2022-09-13 http_version=1.1 ip=73.59.95.40 method=POST request=/bar/baz request_id=1-6529223a-0aa4e4020b9258631cdffb45 request_time=0.123 status=200
api_version=2022-09-13 http_version=1.1 ip=58.39.250.34 method=GET request=/ping/pong request_id=1-65292232-5444ab28585cf86c208fbb1b request_time=1.234 status=200

# Pattern
api_version=<kv> http_version=<kv> ip=<kv> method=<kv> request=<kv> request_id=<kv> .duration=<kv,unit=seconds> http.response.status_code=<kv>
```

## Conclusion

Grouping rules work best with [structured logs](/glossary/structured-logging) and don't try to replace log parsers provided by [OpenTelemetry Logs](/opentelemetry/logs) and [Vector](/ingest/logs/vector).
