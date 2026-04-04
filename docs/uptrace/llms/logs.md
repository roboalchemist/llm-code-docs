# Source: https://uptrace.dev/raw/get/opentelemetry-swift/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-rust/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-ruby/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-python/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-php/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-js/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-java/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-go/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-erlang/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-dotnet/logs.md

# Source: https://uptrace.dev/raw/get/opentelemetry-cpp/logs.md

# Source: https://uptrace.dev/raw/get/logs.md

# Monitoring logs with Uptrace

> Collect infrastructure and application logs with Vector, Fluent Bit, or OpenTelemetry events, enrich them with attributes, and group records inside Uptrace.

<alert type="info">

To receive notifications about specific logs and errors, see [Alerts and notifications](/features/alerting).

</alert>

## Infrastructure logs

To monitor infrastructure logs, you can use [Vector](/ingest/logs/vector) (Heroku, Fly) and [FluentBit](/ingest/logs/fluentbit) integrations.

If you are using AWS, you can also send [CloudWatch Logs](/ingest/cloudwatch#cloudwatch-logs) directly to Uptrace.

## Application logs

There are two approaches to recording application logs with OpenTelemetry:

1. **OpenTelemetry Logging Libraries** - Use bridges for popular logging libraries (recommended)
2. **Span Events** - Add log events directly to spans

### Using logging libraries

The recommended approach is to use OpenTelemetry bridges for your existing logging library. This provides automatic trace correlation and a familiar logging API.

<code-group>

```go [Go (Zap)]
import (
    "go.uber.org/zap"
    "github.com/uptrace/opentelemetry-go-extra/otelzap"
)

// Wrap zap logger with otelzap
log := otelzap.New(zap.NewExample())

// Pass context to correlate with traces
log.Ctx(ctx).Error("request failed",
    zap.Error(err),
    zap.String("user_id", "12345"),
)
```

```go [Go (slog)]
import (
    "log/slog"
    "go.opentelemetry.io/contrib/bridges/otelslog"
)

// Set otelslog as the default logger
slog.SetDefault(otelslog.NewLogger("my-service"))

// Logs automatically include trace context
slog.ErrorContext(ctx, "request failed",
    "error", err.Error(),
    "user_id", "12345",
)
```

```python [Python]
import logging
from opentelemetry import trace
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

# Set up OpenTelemetry logging
logger_provider = LoggerProvider()
logger_provider.add_log_record_processor(
    BatchLogRecordProcessor(exporter)
)

# Attach to Python logging
handler = LoggingHandler(logger_provider=logger_provider)
logging.getLogger().addHandler(handler)

# Use standard logging API - trace context is automatically included
logger = logging.getLogger(__name__)
logger.error("request failed", extra={"user_id": "12345"})
```

```java [Java (Logback)]
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import io.opentelemetry.api.trace.Span;

Logger logger = LoggerFactory.getLogger(MyClass.class);

// OpenTelemetry Java agent auto-injects trace context to MDC
// Or manually inject:
Span span = Span.current();
SpanContext spanCtx = span.getSpanContext();
MDC.put("trace_id", spanCtx.getTraceId());
MDC.put("span_id", spanCtx.getSpanId());

logger.error("Request failed user_id={}", "12345");
MDC.clear();
```

```js [Node.js (winston)]
const winston = require('winston');
const { trace } = require('@opentelemetry/api');

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format((info) => {
      const span = trace.getActiveSpan();
      if (span) {
        const ctx = span.spanContext();
        info.trace_id = ctx.traceId;
        info.span_id = ctx.spanId;
      }
      return info;
    })(),
    winston.format.json()
  ),
  transports: [new winston.transports.Console()]
});

logger.error('request failed', { user_id: '12345' });
```

</code-group>

**Language-specific guides:**

<home-distro-list page="logs">



</home-distro-list>

**Library-specific guides:**

- [OpenTelemetry Zap](/guides/opentelemetry-zap) - Go Zap logging integration
- [OpenTelemetry Slog](/guides/opentelemetry-slog) - Go standard library slog
- [OpenTelemetry Logrus](/guides/opentelemetry-logrus) - Go Logrus integration
- [OpenTelemetry Log4j](/guides/opentelemetry-log4j) - Java Log4j logging integration
- [OpenTelemetry Logback](/guides/opentelemetry-logback) - Java Logback logging integration

### Using span events

You can also record logs as [OpenTelemetry span events](/opentelemetry/distributed-tracing#event). Set the event name to `log` and use [semantic attributes](/opentelemetry/distributed-tracing#attributes) for context:

<table>
<thead>
  <tr>
    <th>
      Attribute
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
        log.severity
      </code>
    </td>
    
    <td>
      Log level: <code>
        TRACE
      </code>
      
      , <code>
        DEBUG
      </code>
      
      , <code>
        INFO
      </code>
      
      , <code>
        WARN
      </code>
      
      , <code>
        ERROR
      </code>
      
      , <code>
        FATAL
      </code>
      
      , <code>
        PANIC
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        log.message
      </code>
    </td>
    
    <td>
      The log message
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        code.function
      </code>
    </td>
    
    <td>
      Function name (optional)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        code.filepath
      </code>
    </td>
    
    <td>
      File path (optional)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        code.lineno
      </code>
    </td>
    
    <td>
      Line number (optional)
    </td>
  </tr>
</tbody>
</table>

<code-group>

```go [Go]
span := trace.SpanFromContext(ctx)

span.AddEvent("log", trace.WithAttributes(
    attribute.String("log.severity", "ERROR"),
    attribute.String("log.message", "request failed"),
    attribute.String("code.function", "org.FetchUser"),
    attribute.String("code.filepath", "org/user.go"),
    attribute.Int("code.lineno", 123),
    attribute.String("user_id", "12345"),
))
```

```python [Python]
from opentelemetry import trace

span = trace.get_current_span()

span.add_event("log", attributes={
    "log.severity": "ERROR",
    "log.message": "request failed",
    "code.function": "fetch_user",
    "code.filepath": "org/user.py",
    "code.lineno": 123,
    "user_id": "12345",
})
```

```java [Java]
Span span = Span.current();

span.addEvent("log", Attributes.builder()
    .put("log.severity", "ERROR")
    .put("log.message", "request failed")
    .put("code.function", "fetchUser")
    .put("code.filepath", "org/User.java")
    .put("code.lineno", 123)
    .put("user_id", "12345")
    .build());
```

```js [JavaScript]
const { trace } = require('@opentelemetry/api');

const span = trace.getActiveSpan();

span.addEvent('log', {
  'log.severity': 'ERROR',
  'log.message': 'request failed',
  'code.function': 'fetchUser',
  'code.filepath': 'org/user.js',
  'code.lineno': 123,
  'user_id': '12345',
});
```

</code-group>

For more information on [OpenTelemetry Logs](/opentelemetry/logs) and open-source tools for log management, see [Open-Source Log Management Tools](/blog/open-source-log-management).

## Grouping logs together

You can control how Uptrace groups logs together by providing `grouping.fingerprint` attribute which can be a string or a number (hash/id):

```toml
log.severity = "info"
log.message = "unstructured log message 123 456 789"
grouping.fingerprint = "unstructured log message"
```

You can further customize [logs grouping](/features/querying/logs-grouping) using grouping rules.

## Propagating trace context

When collecting third-party logs with Vector or FluentBit, trace context is not automatically [propagated](/opentelemetry/distributed-tracing#context) and logs can't be linked with spans.

To propagate context and associate a log record with a span, include these attributes in your log messages:

<table>
<thead>
  <tr>
    <th>
      Attribute
    </th>
    
    <th>
      Format
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
        trace_id
      </code>
    </td>
    
    <td>
      32 hex characters
    </td>
    
    <td>
      Links log to a distributed trace
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        span_id
      </code>
    </td>
    
    <td>
      16 hex characters
    </td>
    
    <td>
      Links log to a specific span
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        trace_flags
      </code>
    </td>
    
    <td>
      W3C format
    </td>
    
    <td>
      Indicates if trace is sampled (optional)
    </td>
  </tr>
</tbody>
</table>

**Example log message:**

```text
request failed trace_id=958180131ddde684c1dbda1aeacf51d3 span_id=0cf859e4f7510204
```

**Example JSON log:**

```json
{
  "message": "request failed",
  "level": "error",
  "trace_id": "958180131ddde684c1dbda1aeacf51d3",
  "span_id": "0cf859e4f7510204",
  "user_id": "12345"
}
```

## See also

- [OpenTelemetry Logs](/opentelemetry/logs) - Complete logs specification guide
- [Structured logging](/glossary/structured-logging) - What is structured logging
- [OpenTelemetry Slog](/guides/opentelemetry-slog) - Go standard library logging
- [OpenTelemetry Zap](/guides/opentelemetry-zap) - Go Zap logging integration
- [Vector](/ingest/logs/vector) - Collect logs with Vector
- [FluentBit](/ingest/logs/fluentbit) - Collect logs with FluentBit
