# Source: https://uptrace.dev/raw/guides/opentelemetry-fastapi.md

# OpenTelemetry FastAPI Instrumentation and Monitoring

> Add OpenTelemetry instrumentation to FastAPI apps using FastAPIInstrumentor.instrument_app(). Get automatic distributed tracing, metrics and performance monitoring.

By integrating OpenTelemetry with FastAPI, you can gain valuable insight into the performance, behavior and dependencies of your API. You can monitor and troubleshoot issues, optimize performance, and ensure the reliability of your FastAPI applications.

## Quick Setup

<table>
<thead>
  <tr>
    <th>
      Step
    </th>
    
    <th>
      Action
    </th>
    
    <th>
      Code/Command
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      1. Install
    </td>
    
    <td>
      Install OpenTelemetry FastAPI instrumentation
    </td>
    
    <td>
      <code>
        pip install opentelemetry-instrumentation-fastapi
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      2. Import
    </td>
    
    <td>
      Import FastAPIInstrumentor
    </td>
    
    <td>
      <code>
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      3. Instrument
    </td>
    
    <td>
      Apply automatic instrumentation
    </td>
    
    <td>
      <code>
        FastAPIInstrumentor.instrument_app(app)
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      4. Run
    </td>
    
    <td>
      Start your FastAPI application
    </td>
    
    <td>
      Traces collected automatically
    </td>
  </tr>
</tbody>
</table>

**Minimal working example:**

```python
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

# Instrument your FastAPI app
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

This single line `FastAPIInstrumentor.instrument_app(app)` automatically captures all incoming HTTP requests, traces request flow through your application, and exports telemetry data to your configured OpenTelemetry backend.

## What is FastAPI?

FastAPI is a modern, high-performance web framework for building APIs with Python. It is designed to be easy to use, highly efficient, and able to handle high loads.

FastAPI's combination of performance, productivity, and modern features has made it popular among developers building APIs with Python.

## What is OpenTelemetry?

OpenTelemetry is an open-source observability framework that aims to standardize and simplify the collection, processing, and export of telemetry data from applications and systems.

OpenTelemetry supports multiple programming languages and platforms, making it suitable for a wide range of applications and environments.

OpenTelemetry enables developers to instrument their code and collect telemetry data, which can then be exported to various [backends](/opentelemetry/backend-comparison) or [observability platforms](/tools/top-observability-tools) for analysis and visualization. Configuration can be easily managed through [OpenTelemetry environment variables](/opentelemetry/env-vars), providing a standardized way to configure exporters, resource attributes, and sampling behavior.

OpenTelemetry provides detailed instrumentation, enabling you to monitor and measure the performance of your FastAPI applications in real-time. You can identify bottlenecks, optimize code, and ensure your application runs smoothly even under heavy traffic.

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Python zero-code instrumentation guide](/get/opentelemetry-python/zero-code).

</alert>

## FastAPI instrumentation

To install OpenTelemetry instrumentation for FastAPI:

```shell
pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-fastapi
```

## OpenTelemetry SDK

To initialize OpenTelemetry in your Flask application, add the following to your application's startup code, for example, in your `app.py` or `wsgi.py` file:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")
```

## Usage

To instrument FastAPI application:

```python
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)
```

Also see [OpenTelemetry FastAPI example](https://github.com/uptrace/uptrace-python/tree/master/example/fastapi) at GitHub.

OpenTelemetry allows you to trace requests as they flow through your FastAPI application, providing a clear picture of how different components and services interact. This end-to-end tracing helps diagnose issues quickly and streamline troubleshooting.

Once your FastAPI application is instrumented with OpenTelemetry, you can use the observability data in a variety of ways. You can visualize distributed traces, analyze performance metrics, and gain insight into the behavior of your API.

## Instrumenting your code

OpenTelemetry can automatically trace incoming HTTP requests to your FastAPI application. You can also create custom spans to trace specific parts of your code. For example:

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

@app.get("/")
async def read_root():
    # Create a custom span
    with tracer.start_as_current_span("custom-span"):
        # Your code here
        return {"message": "Hello, World!"}
```

## FastAPI Monitoring with OpenTelemetry

OpenTelemetry FastAPI monitoring provides comprehensive visibility into your API's performance, request flows, and resource utilization. The `FastAPIInstrumentor` automatically captures critical monitoring data including request/response times, HTTP status codes, endpoint paths, and error rates.

### What FastAPIInstrumentor Monitors

When you call `FastAPIInstrumentor.instrument_app(app)`, OpenTelemetry automatically tracks:

- **Request Duration**: Time taken to process each API request
- **HTTP Methods**: GET, POST, PUT, DELETE, PATCH operations
- **Endpoint Paths**: Which routes are being accessed
- **Status Codes**: Success (2xx), redirects (3xx), client errors (4xx), server errors (5xx)
- **Request/Response Sizes**: Payload sizes for bandwidth monitoring
- **Concurrent Requests**: Number of simultaneous connections

### Monitoring FastAPI with Uptrace

OpenTelemetry backends like Uptrace provide real-time dashboards showing FastAPI performance metrics, request traces, and error analytics. You can identify slow endpoints, track API usage patterns, and receive alerts when error rates spike.

## OpenTelemetry FastAPI Metrics Collection

Beyond distributed tracing, OpenTelemetry collects metrics from your FastAPI application for performance analysis and capacity planning. These metrics include request rates, latency distributions, and resource consumption.

### HTTP Server Metrics

FastAPI instrumentation automatically generates standard HTTP server metrics:

```python
from opentelemetry import metrics
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Automatic metrics collection
FastAPIInstrumentor.instrument_app(app)

# Metrics collected:
# - http.server.duration (request latency histogram)
# - http.server.request.size (request body sizes)
# - http.server.response.size (response body sizes)
# - http.server.active_requests (concurrent requests gauge)
```

### Custom Metrics for FastAPI

Add custom business metrics to track application-specific KPIs:

```python
from opentelemetry import metrics

meter = metrics.get_meter(__name__)
request_counter = meter.create_counter(
    "api.requests.custom",
    description="Custom API request counter"
)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    request_counter.add(1, {"endpoint": "/items", "method": "GET"})
    return {"item_id": item_id}
```

## Performance Tracking and Optimization

OpenTelemetry FastAPI instrumentation enables detailed performance tracking, helping identify bottlenecks and optimize API response times.

### Distributed Tracing for FastAPI

[Distributed tracing](/opentelemetry/distributed-tracing) shows the complete request path through your FastAPI application, including database queries, external API calls, and background tasks. Each trace contains spans representing individual operations:

```python
from opentelemetry import trace
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

tracer = trace.get_tracer(__name__)

@app.get("/complex-operation")
async def complex_operation():
    with tracer.start_as_current_span("database-query") as span:
        # Simulate database query
        span.set_attribute("db.operation", "SELECT")
        result = await fetch_from_database()

    with tracer.start_as_current_span("external-api-call"):
        # Trace external API calls
        data = await call_external_api()

    return {"result": result, "data": data}
```

### Identifying Slow Endpoints

Use OpenTelemetry traces to identify which FastAPI endpoints have the highest latency. Backends like Uptrace automatically rank endpoints by response time, showing P50, P95, and P99 latencies.

## What is Uptrace?

Uptrace is an [open source APM](/get/hosted/open-source-apm) for OpenTelemetry that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues. For APM capabilities, compare with other [top APM tools](/tools/top-apm-tools).

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules, notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

### uvicorn

If you are using uvicorn with Gunicorn, you need to initialize OpenTelemetry in the post-fork hook:

```python
import uptrace

def post_fork(server, worker):
    uptrace.configure_opentelemetry(...)

workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
```

## Conclusion

With insights from OpenTelemetry, you can make informed decisions about scaling your FastAPI application. Load balancing strategies can be adjusted based on real-time data to handle traffic spikes effectively.

OpenTelemetry also allows you to instrument specific parts of your code for custom telemetry collection. You can use [OpenTelemetry Python APIs](/get/opentelemetry-python/tracing) to manually create spans and add custom attributes, events, or metrics to capture additional information.

For background task processing, consider instrumenting [Celery](/guides/opentelemetry-celery) workers. If you need alternative Python frameworks, explore [Flask](/guides/opentelemetry-flask) for traditional WSGI applications or [Django](/guides/opentelemetry-django) for full-featured web development.

## FAQ

**What is opentelemetry-instrumentation-fastapi?** The opentelemetry-instrumentation-fastapi package is the official OpenTelemetry library for automatically instrumenting FastAPI applications. It provides the `FastAPIInstrumentor` class that wraps your FastAPI app to collect traces, metrics, and telemetry data from all HTTP requests without manual instrumentation code.

**How to use FastAPIInstrumentor.instrument_app()?** To use FastAPIInstrumentor, first install the package with `pip install opentelemetry-instrumentation-fastapi`, then import and apply it to your FastAPI application: `from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor` followed by `FastAPIInstrumentor.instrument_app(app)`. This single line automatically instruments all endpoints and middleware in your FastAPI application.

**What does FastAPIInstrumentor monitor?** FastAPIInstrumentor automatically monitors HTTP request duration, endpoint paths, HTTP methods (GET/POST/PUT/DELETE), response status codes, request and response payload sizes, concurrent active requests, and exceptions. It creates distributed traces showing the complete request flow through your application and integrates with distributed tracing systems.

**How to collect metrics from FastAPI with OpenTelemetry?** OpenTelemetry FastAPI instrumentation automatically collects HTTP server metrics including `http.server.duration` (latency histogram), `http.server.request.size`, `http.server.response.size`, and `http.server.active_requests`. These metrics are exported to your configured OpenTelemetry backend for visualization and alerting.

**How to monitor FastAPI application performance?** Monitor FastAPI performance by instrumenting with `FastAPIInstrumentor.instrument_app(app)` and exporting telemetry to an [OpenTelemetry backend](/blog/opentelemetry-backend) like Uptrace, Jaeger, or Prometheus. These backends provide dashboards showing request rates, latency percentiles (P50, P95, P99), error rates, and endpoint-level performance breakdowns.

**Does FastAPIInstrumentor work with async endpoints?** Yes, FastAPIInstrumentor fully supports both synchronous and asynchronous FastAPI endpoints. It correctly traces async operations including `async def` route handlers, background tasks, and concurrent requests, maintaining trace context across asynchronous boundaries in your FastAPI application.

**How to add custom spans to FastAPI traces?** Add custom spans using OpenTelemetry's tracing API: `tracer = trace.get_tracer(__name__)`, then wrap code blocks with `with tracer.start_as_current_span("span-name")`. Custom spans appear nested within the automatic HTTP request spans created by FastAPIInstrumentor, providing detailed visibility into specific operations.

**What's the difference between FastAPI monitoring and instrumentation?** FastAPI instrumentation refers to adding OpenTelemetry code (`FastAPIInstrumentor.instrument_app()`) to collect telemetry data from your application. FastAPI monitoring refers to the ongoing process of observing collected telemetry data through dashboards, alerts, and analytics in your observability platform to track performance and troubleshoot issues.

**How to instrument FastAPI with uvicorn and Gunicorn?** When using uvicorn with Gunicorn workers, initialize OpenTelemetry in the post-fork hook to ensure each worker process is properly instrumented. See the [Application servers](/get/opentelemetry-python#application-servers) guide for detailed configuration. For single-process uvicorn deployments, standard `FastAPIInstrumentor.instrument_app(app)` works without additional setup.

**What Python version is required for opentelemetry-instrumentation-fastapi?** The opentelemetry-instrumentation-fastapi package requires Python 3.7 or higher, matching FastAPI's minimum Python version requirement. For complete Python instrumentation setup including SDK configuration and exporter setup, see the [OpenTelemetry Python guide](/get/opentelemetry-python).
