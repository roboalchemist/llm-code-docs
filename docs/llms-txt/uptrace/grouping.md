# Source: https://uptrace.dev/raw/features/querying/grouping.md

# Grouping similar spans and events together

> Optimize grouping by choosing stable span names, leveraging display.name, and providing custom fingerprints when needed.

Uptrace automatically groups similar spans and events together to help you identify patterns and anomalies in your application. This page explains how grouping works, how to optimize span names for effective grouping, and how to use OpenTelemetry semantic conventions for different types of operations.

## How grouping works

Uptrace computes a hash for each span based on its type and key attributes. Spans with the same hash are grouped together. The hash always includes:

- **Project ID** - spans from different projects are never grouped together
- **System** - the detected span type (e.g., `http`, `db:postgresql`, `messaging:rabbitmq`)
- **Span name** (for spans) or **Event name** (for events)
- **Span kind** (for spans) - `client`, `server`, `producer`, `consumer`, or `internal`

Additionally, each span type includes type-specific attributes in the hash:

<table>
<thead>
  <tr>
    <th>
      Span Type
    </th>
    
    <th>
      Grouping Attributes
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      HTTP
    </td>
    
    <td>
      <code>
        http.request.method
      </code>
      
      , <code>
        http.route
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Database
    </td>
    
    <td>
      <code>
        db.system.name
      </code>
      
      , <code>
        db.namespace
      </code>
      
      , <code>
        db.collection.name
      </code>
      
      , <code>
        db.operation.name
      </code>
      
      , <code>
        db.query.summary
      </code>
      
      , <code>
        db.stored_procedure.name
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      RPC
    </td>
    
    <td>
      <code>
        rpc.system
      </code>
      
      , <code>
        rpc.service
      </code>
      
      , <code>
        rpc.method
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Messaging
    </td>
    
    <td>
      <code>
        messaging.system
      </code>
      
      , <code>
        messaging.operation.name
      </code>
      
      , <code>
        messaging.operation.type
      </code>
      
      , <code>
        messaging.destination.name
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      FaaS
    </td>
    
    <td>
      <code>
        faas.name
      </code>
      
      , <code>
        faas.document.collection
      </code>
      
      , <code>
        faas.document.operation
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Logs
    </td>
    
    <td>
      <code>
        log.severity
      </code>
      
      , <code>
        log.message_format
      </code>
      
      , <code>
        exception.type
      </code>
      
      , <code>
        error.type
      </code>
      
      , <code>
        telemetry.sdk.language
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Exceptions
    </td>
    
    <td>
      <code>
        exception.type
      </code>
    </td>
  </tr>
</tbody>
</table>

Uptrace supports both stable and legacy OpenTelemetry semantic convention attribute names. For example, both `db.system.name` (stable) and `db.system` (legacy) are recognized.

## Span names

Uptrace uses span names and some attributes to group similar spans together. To group spans properly, give them short and concise names. The total number of unique span names should be less than 1000. Otherwise, you will have too many span groups and your experience may suffer.

The following names are **good** because they are short, distinctive, and help grouping similar spans together:

<table>
<thead>
  <tr>
    <th>
      Span name
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
        GET /projects/:id
      </code>
    </td>
    
    <td>
      Good. A route name with param names.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        select_project
      </code>
    </td>
    
    <td>
      Good. A function name without arguments.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT * FROM projects WHERE id = ?
      </code>
    </td>
    
    <td>
      Good. A database query with placeholders.
    </td>
  </tr>
</tbody>
</table>

The following names are **bad** because they contain variable params and args:

<table>
<thead>
  <tr>
    <th>
      Span name
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
        GET /projects/42
      </code>
    </td>
    
    <td>
      Bad. Contains a variable param <code>
        42
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        select_project(42)
      </code>
    </td>
    
    <td>
      Bad. Contains a variable <code>
        42
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT * FROM projects WHERE id = 42
      </code>
    </td>
    
    <td>
      Bad. Contains a variable arg <code>
        42
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

## Display name

Because OpenTelemetry uses span and event names to group similar spans together, such names end up being not very descriptive, for example, SQL spans often have names like `SELECT` or `INSERT`.

This is where the `display.name` attribute comes in handy. The `display.name` is a human-readable string that provides a short summary of the operation that the span or event represents.

Uptrace doesn't use display names for grouping so they don't have the same limitations as span names. For example, a span representing a SQL query might have the following name and attributes:

```toml
SpanName = "SELECT"

display.name = "pg_select_items_from_group(123)"
db.system.name = "postgresql"
db.query.text = "SELECT * FROM items WHERE group_id = 123 ORDER BY id LIMIT 100"
```

You can use `display.name` attribute with events too.

## Custom grouping

You can customize how Uptrace groups spans and events together by specifying the `grouping.fingerprint` attribute which can be a string or a number (hash). Uptrace will group spans/events with the same fingerprint together.

```toml
SpanName = "SELECT"

display.name = "pg_select_items_from_group(123)"
db.system.name = "postgresql"
db.query.text = "SELECT * FROM items WHERE group_id = 123 ORDER BY id LIMIT 100"
grouping.fingerprint = "select group items"
```

## Grouping settings

On the Project Settings page, there are several options that control how Uptrace groups spans together:

- **Group by environment** - Group spans with different `deployment.environment.name` (or legacy `deployment.environment`) attribute separately. After enabling this setting, there will be separate groups for spans with the same name but different environments.
- **Group functions by service** - Group spans with `funcs` system and different `service.name` attribute separately. After enabling this setting, there will be a separate system for each service such as `funcs:service1` and `funcs:service2`.

## Span systems

Depending on the presence of some semantic attributes, Uptrace assigns each span a **system**, for example:

- `http:service_name` system for HTTP spans.
- `db:postgresql` for PostgreSQL queries.
- `log:error` for log messages with `ERROR` severity.

Using a system, you can easily filter spans that have the same set of attributes, for example, [all database spans](https://app.uptrace.dev/explore/1/groups?system=db:all).

### HTTP

To monitor HTTP clients and servers, use the [HTTP semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/http/http-spans.md).

A minimal HTTP server example:

```toml
SpanName = "GET /users/:id"
SpanKind = "server"

http.request.method = "GET"
http.route = "/users/:id"
url.scheme = "https"
```

A minimal HTTP client example:

```toml
SpanName = "GET"
SpanKind = "client"

http.request.method = "GET"
url.full = "https://api.example.com/users/123"
server.address = "api.example.com"
```

### RPC

To monitor remote procedure calls, use the [RPC semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/rpc/rpc-spans.md).

A minimal RPC server example:

```toml
SpanName = "AuthService/Auth"
SpanKind = "server"

rpc.system = "grpc"
rpc.service = "AuthService"
rpc.method = "Auth"
```

### Database

To monitor database queries and Redis/memcached commands, use the [database semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/db/database-spans.md).

A minimal DB example:

```toml
SpanName = "SELECT users"
SpanKind = "client"

db.system.name = "postgresql"
db.query.text = "SELECT * FROM users WHERE id = $1"
db.collection.name = "users"
db.namespace = "mydb"
```

A minimal Redis command example:

```toml
SpanName = "GET"
SpanKind = "client"

db.system.name = "redis"
db.query.text = "GET foo"
```

### Messages

To monitor producers and consumers (queues), use the [messaging semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/messaging/messaging-spans.md).

A minimal producer example:

```toml
SpanName = "MyQueue send"
SpanKind = "producer"

messaging.system = "rabbitmq"
messaging.destination.name = "MyQueue"
messaging.operation.type = "send"
```

A minimal consumer example:

```toml
SpanName = "MyQueue process"
SpanKind = "consumer"

messaging.system = "rabbitmq"
messaging.destination.name = "MyQueue"
messaging.operation.type = "process"
```

### Functions

To monitor functions, use [source code attributes](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/general/attributes.md#source-code-attributes).

A minimal example:

```toml
SpanName = "org.FetchUser"

service.name = "myservice"
code.function.name = "FetchUser"
code.namespace = "org"
code.filepath = "org/user.go"
code.lineno = 123
```

### Functions as a Service

To monitor serverless functions, use the [FaaS semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/faas/faas-spans.md).

A minimal HTTP-triggered function:

```toml
SpanName = "my-lambda-function"
SpanKind = "server"

faas.trigger = "http"
faas.name = "my-lambda-function"
```

A datasource-triggered function (e.g., S3, DynamoDB):

```toml
SpanName = "my-lambda-function"
SpanKind = "server"

faas.trigger = "datasource"
faas.name = "my-lambda-function"
faas.document.collection = "my-bucket"
faas.document.operation = "insert"
```

A minimal client example (invoking a function):

```toml
SpanName = "my-lambda-function"
SpanKind = "client"

faas.invoked_name = "my-lambda-function"
faas.invoked_provider = "aws"
faas.invoked_region = "us-west-2"
```

### Exceptions

To monitor errors and exceptions, use the [exceptions semantic conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/exceptions/exceptions-logs.md) and **events** API.

A minimal example:

```toml
EventName = "exception"

exception.type = "*exec.ExitError"
exception.message = "exit status 1"
exception.stacktrace = "<exception stacktrace>"
```

<code-group>

```go [Go]
span := trace.SpanFromContext(ctx)

span.RecordError(err, trace.WithAttributes(
    attribute.String("exception.type", fmt.Sprintf("%T", err)),
))
// Or manually:
span.AddEvent("exception", trace.WithAttributes(
    attribute.String("exception.type", "*exec.ExitError"),
    attribute.String("exception.message", "exit status 1"),
    attribute.String("exception.stacktrace", string(debug.Stack())),
))
```

```python [Python]
from opentelemetry import trace

span = trace.get_current_span()
try:
    # your code
    pass
except Exception as e:
    span.record_exception(e)
    span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
```

```js [JavaScript]
const span = trace.getActiveSpan();
try {
  // your code
} catch (error) {
  span.recordException(error);
  span.setStatus({ code: SpanStatusCode.ERROR, message: error.message });
}
```

</code-group>

You can also control how Uptrace groups exceptions together by specifying the `grouping.fingerprint` attribute which can be a string or a number (hash). Uptrace will group exceptions with the same fingerprint together.

```toml
EventName = "exception"

exception.type = "*exec.ExitError"
exception.message = "exit status 1"
grouping.fingerprint = "*exec.ExitError"
```

### Logs

Uptrace groups logs by `log.severity` and `log.message_format`. The `log.message_format` attribute should contain the log message template (with placeholders), not the actual message with interpolated values. This ensures logs with the same pattern are grouped together.

A minimal example:

```toml
EventName = "log"

log.severity = "info"
log.message = "user 123 logged in from 192.168.1.1"
log.message_format = "user %d logged in from %s"
log.params.user_id = "123"
log.params.ip = "192.168.1.1"
```

<code-group>

```go [Go]
span := trace.SpanFromContext(ctx)

span.AddEvent("log", trace.WithAttributes(
    attribute.String("log.severity", "info"),
    attribute.String("log.message", fmt.Sprintf("user %d logged in from %s", userID, ip)),
    attribute.String("log.message_format", "user %d logged in from %s"),
    attribute.Int("log.params.user_id", userID),
    attribute.String("log.params.ip", ip),
))
```

```python [Python]
from opentelemetry import trace

span = trace.get_current_span()
span.add_event("log", attributes={
    "log.severity": "info",
    "log.message": f"user {user_id} logged in from {ip}",
    "log.message_format": "user %d logged in from %s",
    "log.params.user_id": user_id,
    "log.params.ip": ip,
})
```

```js [JavaScript]
const span = trace.getActiveSpan();
span.addEvent('log', {
  'log.severity': 'info',
  'log.message': `user ${userId} logged in from ${ip}`,
  'log.message_format': 'user %d logged in from %s',
  'log.params.user_id': userId,
  'log.params.ip': ip,
});
```

</code-group>

You can also control how Uptrace groups logs together by providing `grouping.fingerprint` attribute which can be a string or a number (hash). This is useful for unstructured logs where you can't easily extract a message format:

```toml
EventName = "log"

log.severity = "info"
log.message = "Connection to database failed after 3 retries"
grouping.fingerprint = "database connection failed"
```

See [Monitoring Logs](/get/logs) for details.
