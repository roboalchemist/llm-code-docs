# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-client.md

# FiddlerClient

The main client for instrumenting Generative AI applications with Fiddler observability.

This client configures and manages the OpenTelemetry tracer that sends telemetry data to the Fiddler platform for monitoring, analysis, and debugging of your AI agents and workflows.

Flush on exit: A shutdown handler is registered via `atexit()` so that pending spans are flushed and the tracer is shut down when the process exits. For short scripts or critical workloads, call [`force_flush()`](#force_flush) and [`shutdown()`](#shutdown) explicitly (e.g. in a `try`/`finally` or signal handler) since `atexit` may not run in all environments (e.g. SIGKILL, fork).

Asyncio: Tracing works in asyncio (context vars propagate across `await`). When shutting down from async code, use [`aflush()`](#aflush) and [`ashutdown()`](#ashutdown) so the event loop is not blocked; the sync [`force_flush()`](#force_flush) and [`shutdown()`](#shutdown) can block for up to the flush timeout.

Context manager: Use `with FiddlerClient(...) as client:` to ensure [`shutdown()`](#shutdown) is called on exit (flush then shutdown; atexit is unregistered).

## Parameters

| Parameter               | Type               | Required | Default                    | Description                                                                                                                                                                                                          |
| ----------------------- | ------------------ | -------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`               | `str`              | ✓        | `-`                        | The `API` key for authenticating with the Fiddler backend.                                                                                                                                                           |
| `application_id`        | `str`              | ✓        | `-`                        | The unique identifier (UUID4) for the application.                                                                                                                                                                   |
| `url`                   | `str`              | ✓        | `-`                        | The base `URL` for your Fiddler instance. This is specific to your deployment, whether hosted, `VPC`-deployed, on-premise, or local development (e.g., <https://your-instance.fiddler.ai>, <http://localhost:4318>). |
| `console_tracer`        | `bool`             | ✗        | `False`                    | If True, traces will be printed to the console instead of being sent to the Fiddler backend. Useful for debugging                                                                                                    |
| `span_limits`           | \`SpanLimits       | None\`   | ✗                          | `None`                                                                                                                                                                                                               |
| `sampler`               | \`sampling.Sampler | None\`   | ✗                          | `None`                                                                                                                                                                                                               |
| `compression`           | `Compression`      | ✗        | `Compression.Gzip`         | The compression for exporting traces. Can be Compression.Gzip, Compression.Deflate, or Compression.NoCompression                                                                                                     |
| `jsonl_capture_enabled` | `bool`             | ✗        | `False`                    | Whether to enable `JSONL` capture of trace data. When enabled, all span data will be captured and saved to a `JSONL` file in OpenTelemetry format for offline analysis                                               |
| `jsonl_file_path`       | `str`              | ✗        | `fiddler_trace_data.jsonl` | Path to the `JSONL` file where trace data will be saved. Only used when jsonl\_capture\_enabled is True                                                                                                              |

## Raises

**ValueError** -- If application\_id is not a valid UUID4 or if the url is not a valid HTTP/HTTPS URL.

## Examples

Basic connection to your Fiddler instance:

```python
client = FiddlerClient(
    api_key='YOUR_API_KEY',
    application_id='YOUR_APPLICATION_ID',
    url='https://your-instance.fiddler.ai',
)
```

High-volume applications with custom configuration:

```python
from opentelemetry.sdk.trace import SpanLimits, sampling
from opentelemetry.exporter.otlp.proto.http.trace_exporter import Compression

# Example: add custom limits
client = FiddlerClient(
    api_key='YOUR_API_KEY',
    application_id='YOUR_APPLICATION_ID',
    url='https://your-instance.fiddler.ai',
    span_limits=SpanLimits(
        max_span_attributes=64,           # Reduce from default 128
        max_span_attribute_length=2048,   # Limit from default None (unlimited)
    ),
    sampler=sampling.TraceIdRatioBased(0.1),  # Sample 10% of traces
    compression=Compression.Gzip,
)
```

Local development with console output:

```python
client = FiddlerClient(
    api_key='dev-key',
    application_id='00000000-0000-0000-0000-000000000000',
    url='http://localhost:4318',
    console_tracer=True,  # Print traces to console for debugging
)
```

## **enter**()

Context manager entry. Returns this client.

**Return type:** [*FiddlerClient*](#fiddlerclient)

## **exit**(exc\_type, exc\_val, exc\_tb)

Context manager exit. Flushes and shuts down the tracer provider.

**Return type:** None

## force\_flush()

Flushes pending spans to the exporter.

Call this before process exit (e.g. in signal handlers or atexit) to reduce intermittent span loss. BatchSpanProcessor buffers spans in memory and exports on a schedule; without flush, buffered spans can be lost on exit.

This method is blocking (up to `timeout_millis`). From async code, use [`aflush()`](#aflush) to avoid blocking the event loop.

## Parameters

| Parameter        | Type  | Required | Default | Description                                                    |
| ---------------- | ----- | -------- | ------- | -------------------------------------------------------------- |
| `timeout_millis` | `int` | ✗        | `30000` | Maximum time to wait for flush in milliseconds. Default 30000. |

## Returns

True if flush completed within the timeout, False otherwise.

**Return type:** bool

## *async* aflush(timeout\_millis=30000)

Async version of [`force_flush()`](#force_flush).

Runs the flush in a thread pool so the event loop is not blocked. Use this when shutting down an asyncio application.

**Return type:** bool

## shutdown()

Shuts down the tracer provider after flushing pending spans.

Call this when the application is exiting to ensure all spans are exported. Safe to call multiple times. Registered automatically via atexit when the client is created. The atexit handler is unregistered so it will not run again at process exit.

This method is blocking (flush can take up to 30 seconds). From async code, use [`ashutdown()`](#ashutdown) to avoid blocking the event loop.

**Return type:** None

## *async* ashutdown()

Async version of [`shutdown()`](#shutdown).

Runs flush and shutdown in a thread pool so the event loop is not blocked. Use this when shutting down an asyncio application, e.g. in an `async with` cleanup or before closing the event loop.

**Return type:** None

## get\_tracer\_provider()

Gets the OpenTelemetry TracerProvider instance.

Initializes the provider on the first call.

## Returns

The configured OpenTelemetry TracerProvider.

**Return type:** TracerProvider

## Raises

**RuntimeError** -- If tracer provider initialization fails.

## update\_resource()

Updates the OpenTelemetry resource with additional attributes.

Use this to add metadata that applies to all spans, such as version numbers or environment names.

{% hint style="warning" %}
Must be called before get\_tracer() is invoked.
{% endhint %}

## Parameters

| Parameter    | Type             | Required | Default | Description                             |
| ------------ | ---------------- | -------- | ------- | --------------------------------------- |
| `attributes` | `dict[str, Any]` | ✓        | `-`     | Key-value pairs to add to the resource. |

## Raises

**ValueError** -- If the tracer has already been initialized. **Return type:** None

## Examples

```python
from fiddler_langgraph import FiddlerClient
client = FiddlerClient(api_key='...', application_id='...', url='https://your-instance.fiddler.ai')
client.update_resource({'service.version': '1.2.3'})
```

## get\_tracer()

Returns an OpenTelemetry tracer instance for creating spans.

Initializes the tracer on the first call. This is the primary method for developers to get a tracer for custom instrumentation.

## Returns

OpenTelemetry tracer instance.

**Return type:** trace.Tracer

## Raises

**RuntimeError** -- If tracer initialization fails.

## Examples

```python
from fiddler_langgraph import FiddlerClient
client = FiddlerClient(api_key='...', application_id='...', url='https://your-instance.fiddler.ai')
tracer = client.get_tracer()
with tracer.start_as_current_span('my-operation'):
    print('Doing some work...')
```

## start\_as\_current\_span()

Create a span using context manager (automatic lifecycle).

## Parameters

| Parameter | Type                                             | Required | Default | Description                                              |
| --------- | ------------------------------------------------ | -------- | ------- | -------------------------------------------------------- |
| `name`    | `str`                                            | ✗        | `None`  | Name for the span.                                       |
| `as_type` | `Literal['span', 'generation', 'chain', 'tool']` | ✗        | `span`  | Type of span - "span", "generation", "chain", or "tool". |

## Returns

Wrapper with context manager support.

**Return type:** *FiddlerSpan* | *FiddlerGeneration* | *FiddlerChain* | *FiddlerTool*

## start\_span()

Create a span with manual control. User must call span.end().

## Parameters

| Parameter | Type                                             | Required | Default | Description                                              |
| --------- | ------------------------------------------------ | -------- | ------- | -------------------------------------------------------- |
| `name`    | `str`                                            | ✗        | `None`  | Name for the span.                                       |
| `as_type` | `Literal['span', 'generation', 'chain', 'tool']` | ✗        | `span`  | Type of span - "span", "generation", "chain", or "tool". |

## Returns

Wrapper requiring explicit end() call.

**Return type:** *FiddlerSpan* | *FiddlerGeneration* | *FiddlerChain* | *FiddlerTool*
