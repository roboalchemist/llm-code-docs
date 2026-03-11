# Source: https://uptrace.dev/raw/features/transformations.md

# Transformations

> Use YAML based transformations and Expr filters to rename attributes, parse payloads, and drop or sample telemetry before it reaches Uptrace.

Uptrace allows to transform the ingested data using a YAML-based language. You can use it to rename/delete attribute keys, parse/change attribute values, sample/drop spans, etc.

## Example

For example, to rename an attribute:

```yaml
name: Rename service to service_name
scope: [spans, logs, events, datapoints]
type: rename_attr
old_key: service
new_key: service_name
```

You can use the YAML above to create an operation by following these steps:

1. In the navigation menu on the left, click "Project" -> "Transformations".
2. Click "New Operation" -> "New operation from YAML".
3. Paste the YAML and click "Create".

## Scope

Each operation must have a `scope` field that limits the operation to a particular data type (aka signal). The scope is an array and must contain one of the following values:

- spans
- logs
- events
- datapoints

## Conditions

You can further narrow down the telemetry data to be transformed using `if` expression:

```yaml
name: Rename service to service_name
scope: [spans, logs, events, datapoints]
type: rename_attr
old_key: service
new_key: service_name
if: attr("deployment_environment") == "prod"
```

Uptrace uses [Expr](https://expr-lang.org/docs/language-definition) language for writing expressions. In addition to built-in functions provided by Expr, Uptrace also supports the following functions:

<table>
<thead>
  <tr>
    <th>
      Function
    </th>
    
    <th>
      Scope
    </th>
    
    <th>
      Comment
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        spanName()
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Returns the span name or an empty string.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        eventName()
      </code>
    </td>
    
    <td>
      events
    </td>
    
    <td>
      Returns the event name or an empty string.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        spanKind()
      </code>
    </td>
    
    <td>
      spans
    </td>
    
    <td>
      Returns the span kind.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        spanDuration()
      </code>
    </td>
    
    <td>
      spans
    </td>
    
    <td>
      Returns the span duration in nanoseconds.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        spanStatusCode()
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Returns the span status code.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        spanStatusMessage()
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Returns the span status message.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        metricName()
      </code>
    </td>
    
    <td>
      datapoints
    </td>
    
    <td>
      Returns the metric name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        metricUnit()
      </code>
    </td>
    
    <td>
      datapoints
    </td>
    
    <td>
      Returns the metric unit.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        metricInstrument()
      </code>
    </td>
    
    <td>
      datapoints
    </td>
    
    <td>
      Returns the metric instrument.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        libraryName()
      </code>
    </td>
    
    <td>
      datapoints
    </td>
    
    <td>
      Returns the instrumentation library name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        libraryVersion()
      </code>
    </td>
    
    <td>
      datapoints
    </td>
    
    <td>
      Returns the instrumentation library version.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        attr(key string)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Returns the attribute value by key.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        hasAttr(key string)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Returns <code>
        true
      </code>
      
       if the attribute exists.
    </td>
  </tr>
</tbody>
</table>

Note that `spanName()` and `eventName()` return the original value as reported by OpenTelemetry, e.g. `eventName()` usually contains only a single word like `message`, `log`, etc.

## Execution

Uptrace executes operations one by one after normalising attribute names, i.e. `service.name` is normalised to `service_name` so you should use the normalised name.

Execution will stop if the signal is dropped by a `drop` operation, but otherwise Uptrace will execute all operations regardless of errors.

To change the execution order, use the `priority` field.

```yaml
name: Rename service to service_name
scope: [spans, logs, events, datapoints]
priority: 100
type: rename_attr
old_key: service
new_key: service_name
```

Uptrace executes transformations before it processes the data so you can't use certain attributes set by Uptrace, for example, the `_display_name` column is not available and instead you should use `spanName()`, `eventName()`, `logName()`, and `log_message`.

For the same reason, you also can't use attributes extracted from structured logs and SQL queries, such as `db_arg_*` attributes.

<table>
<thead>
  <tr>
    <th>
      Uptrace Column
    </th>
    
    <th>
      Replacement
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        _display_name
      </code>
    </td>
    
    <td>
      <code>
        spanName()
      </code>
      
      , <code>
        eventName()
      </code>
      
      , and <code>
        attr("log_message")
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        db_arg_*
      </code>
    </td>
    
    <td>
      <code>
        attr("db_statement") contains "something"
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http_response_status_class
      </code>
    </td>
    
    <td>
      <code>
        http_response_status_code
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        user_agent_*
      </code>
    </td>
    
    <td>
      <code>
        user_agent_original
      </code>
    </td>
  </tr>
</tbody>
</table>

## Operations

### Rename attribute

To rename attr from `service` to `service_name`:

```yaml
name: Rename service to service_name
scope: [spans, logs, events]
type: rename_attr
old_key: service
new_key: service_name
```

### Delete attributes

To delete attrs:

```yaml
name: Delete foo and bar
scope: [spans, logs, events, datapoints]
type: delete_attrs
keys:
  - foo
  - bar
```

To delete attrs using a regular expression:

```yaml
name: Delete foo and bar
scope: [spans, logs, events, datapoints]
type: delete_attrs
regexp: ^(foo|bar)$
```

To delete attrs in the specific metric:

```yaml
name: Delete foo and bar
scope: [datapoints]
type: delete_attrs
keys:
  - foo
  - bar
if: metricName() == "my_metric_name"
```

### Keep attributes

To keep some attributes and delete others:

```yaml
name: Keep foo and bar
scope: [spans, logs, events, datapoints]
type: keep_attrs
keys:
  - foo
  - bar
```

To keep attributes matching a regular expression:

```yaml
name: Keep foo and bar
scope: [spans, logs, events, datapoints]
type: keep_attrs
regexp: ^(foo|bar)$
```

### Drop

To drop logs that match `if` expression:

```yaml
name: Drop hello logs
scope: [logs]
type: drop
if: attr("log_message") contains "hello"
```

To drop spans that match `if` expression:

```yaml
name: Drop Redis evalsha
scope: [spans]
type: drop
if: spanName() == "evalsha" && spanStatusCode() != "error"
```

### Sample

To sample 50% of logs that match `if` expression:

```yaml
name: Sample 50% hello logs
scope: [logs]
type: sample
fraction: 0.5
if: attr("log_message") startsWith "hello"
```

### Index Map

By default, Uptrace does not index attributes that contain maps. For example, the following attribute cannot be queried using the `object.nested.foo` path:

```json
{
  "object": {
    "nested": {
      "foo": "bar",
      "hello": "world"
    }
  }
}
```

To index such attributes, use the `index_map` operation:

```yaml
name: Index the object attribute
scope: [spans]
type: index_map

# Map attributes to index.
maps: ['object']

# Map paths to include.
include_paths: ['object.nested.foo']
include_regexp: '^object.nested\.'

# Map paths to exclude.
exclude_paths: ['object.nested.hello']
exclude_regexp: 'secret'
```

If you don't specify any paths, the operation will index the entire map but will stop after 16 paths. This limit exists to keep the number of indexed attributes low and improve performance.

### Script

Uptrace allows to write simple scripts that can modify telemetry data, for example:

```yaml
name: Update status code if span has exception* attributes
scope: [spans]
type: script
if: hasAttr("exception_type") && hasAttr("exception_message")
then:
  - setSpanStatusCode("error")
  - setSpanStatusMessage(attr("exception_message"))
else:
  - setSpanStatusCode("ok")
```

You can use the following functions to change the telemetry data:

<table>
<thead>
  <tr>
    <th>
      Function
    </th>
    
    <th>
      Scope
    </th>
    
    <th>
      Comment
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        setSpanName(string)
      </code>
    </td>
    
    <td>
      spans
    </td>
    
    <td>
      Sets the span name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setLogName(string)
      </code>
    </td>
    
    <td>
      logs
    </td>
    
    <td>
      Sets the log name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setEventName(string)
      </code>
    </td>
    
    <td>
      events
    </td>
    
    <td>
      Sets the event name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setSpanKind(string)
      </code>
    </td>
    
    <td>
      spans
    </td>
    
    <td>
      Sets the span kind.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setSpanDuration(nanoseconds)
      </code>
    </td>
    
    <td>
      spans
    </td>
    
    <td>
      Sets the span duration in nanoseconds.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setSpanStatusCode(string)
      </code>
    </td>
    
    <td>
      spans
    </td>
    
    <td>
      Sets the span status code.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setSpanStatusMessage(string)
      </code>
    </td>
    
    <td>
      spans
    </td>
    
    <td>
      Sets the span status message.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setMetricName(string)
      </code>
    </td>
    
    <td>
      datapoints
    </td>
    
    <td>
      Sets the datapoint metric name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setMetricUnit(string)
      </code>
    </td>
    
    <td>
      datapoints
    </td>
    
    <td>
      Sets the datapoint metric unit.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setAttr(key, value)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Sets the attribute value.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        deleteAttr(key)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Deletes the attribute.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        renameAttr(oldKey, newKey)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Renames the attribute.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseInt(value)
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Parses the value as <code>
        int
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseUint(value)
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Parses the value as <code>
        uint
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseFloat(value)
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Parses the value as <code>
        float
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseBool(value)
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Parses the value as <code>
        bool
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseDuration(string)
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Parses the string value as <code>
        time.Duration
      </code>
      
      , e.g. <code>
        parseDuration("1s")
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parseBytes(string)
      </code>
    </td>
    
    <td>
      spans, logs, events
    </td>
    
    <td>
      Parses the string value as <code>
        int64
      </code>
      
       bytes , e.g. <code>
        parseBytes("1mb")
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        replaceGlob(src, pattern, repl)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Replaces <code>
        src
      </code>
      
       with <code>
        repl
      </code>
      
       if src matches glob <code>
        pattern
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        replaceAllRegexp(src, pattern, repl)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Replaces <code>
        src
      </code>
      
       with <code>
        repl
      </code>
      
       if src matches regexp <code>
        pattern
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extractAllRegexp(src, pattern, repl)
      </code>
    </td>
    
    <td>
      all
    </td>
    
    <td>
      Extracts <code>
        repl
      </code>
      
       if src matches regexp <code>
        pattern
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

To parse a string attribute value as a float:

```yaml
name: Parse elapsed_ms
scope: [spans]
type: script
if: hasAttr("elapsed_ms")
then:
  - setAttr("elapsed_ms", parseFloat(attr("elapsed_ms")))
```

To reduce cardinality of an attribute:

```yaml
name: Reduce http_target cardinality
scope: [spans]
type: script
if: metricName() startsWith "http_server_" && hasAttr("http_target")
then:
  - setAttr("http_target", replaceGlob(attr("http_target"), "/user/*/list/*", "/user/{userId}/list/{listId}"))
```

To replace all numbers in a string attribute using a regular expression:

```yaml
name: Replace numbers in foo
scope: [spans]
type: script
if: hasAttr("foo")
then:
  - setAttr("foo", replaceAllRegexp(attr("foo"), "(\\d+)", "<number>"))
```

To extract all numbers from a string attribute using a regular expression:

```text
name: Extract numbers from foo
scope: [spans]
type: script
if: hasAttr("foo")
then:
  - setAttr("foo", extractAllRegexp(attr("foo"), "(\\d+)", "$1"))
```

To convert a log into a span:

```yaml
name: Convert logs with elapsed_ms to spans
scope: [logs]
type: script
if: hasAttr("elapsed_ms")
then:
  - setSpanName("operation-name")
  - setLogName("") # must zero the log name
  - setSpanDuration(parseFloat(attr("elapsed_ms")) * 1e6)
  - setSpanStatusCode("ok")
```

## Related links

- [Expr Language Definition](https://expr-lang.org/docs/language-definition)
