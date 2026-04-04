# Source: https://uptrace.dev/raw/guides/opentelemetry-pyramid.md

# OpenTelemetry Pyramid: Instrumentation and Monitoring Guide

> Instrument and monitor Pyramid applications with OpenTelemetry. Setup auto-instrumentation, manual tracing, SQLAlchemy integration, and production deployment for Python web apps.

OpenTelemetry Pyramid instrumentation provides automatic tracing for HTTP requests, route handling, and template rendering in Pyramid web applications. With `opentelemetry-instrumentation-pyramid`, you can add observability to your Python web services and track request latencies, database queries, and errors across distributed systems.

## Quick Reference

<table>
<thead>
  <tr>
    <th>
      Component
    </th>
    
    <th>
      Package
    </th>
    
    <th>
      Purpose
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Pyramid Instrumentation
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-pyramid
      </code>
    </td>
    
    <td>
      Auto-trace HTTP requests
    </td>
  </tr>
  
  <tr>
    <td>
      SQLAlchemy Instrumentation
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-sqlalchemy
      </code>
    </td>
    
    <td>
      Trace database queries
    </td>
  </tr>
  
  <tr>
    <td>
      Requests Instrumentation
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-requests
      </code>
    </td>
    
    <td>
      Trace outgoing HTTP calls
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-instrumentation
    </td>
    
    <td>
      <code>
        opentelemetry-bootstrap
      </code>
    </td>
    
    <td>
      Detect and install plugins
    </td>
  </tr>
</tbody>
</table>

## What is OpenTelemetry?

[OpenTelemetry](/opentelemetry) is an open-source observability framework that standardizes the collection of telemetry data from applications. It provides three pillars of observability:

- **Distributed Traces**: Track requests across services and components
- **Metrics**: Collect quantitative measurements of application performance
- **Logs**: Capture structured application logs with trace correlation

OpenTelemetry is vendor-neutral, meaning you can export data to any compatible [OpenTelemetry backend](/blog/opentelemetry-backend) such as Uptrace, Jaeger, or Grafana.

## Prerequisites

- **Python 3.8+**
- **Pyramid 1.7+**
- **pip** package manager

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Python zero-code instrumentation guide](/get/opentelemetry-python/zero-code).

</alert>

## Installation

Install the core packages for Pyramid instrumentation. For comprehensive Python instrumentation, see the [OpenTelemetry Python guide](/get/opentelemetry-python).

```shell
# Core OpenTelemetry SDK
pip install opentelemetry-api opentelemetry-sdk

# Pyramid instrumentation
pip install opentelemetry-instrumentation-pyramid

# OTLP exporter
pip install opentelemetry-exporter-otlp
```

Optional packages depending on your stack:

```shell
# Database instrumentation
pip install opentelemetry-instrumentation-sqlalchemy

# HTTP client instrumentation
pip install opentelemetry-instrumentation-requests
pip install opentelemetry-instrumentation-urllib3
```

## Basic Setup

### Using Uptrace SDK

The simplest way to get started is with the [Uptrace Python SDK](/get/opentelemetry-python), which bundles the OpenTelemetry SDK with sensible defaults:

```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from opentelemetry.instrumentation.pyramid import PyramidInstrumentor
import uptrace

# Configure OpenTelemetry with Uptrace
uptrace.configure_opentelemetry(
    # Set dsn or UPTRACE_DSN env var.
    # dsn="<FIXME>",
    service_name="pyramid-app",
    service_version="1.0.0",
)

# Instrument Pyramid before creating the app
PyramidInstrumentor().instrument()

def home(request):
    return Response("Hello, World!")

def health(request):
    return Response("OK")

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("home", "/")
        config.add_view(home, route_name="home")
        config.add_route("health", "/health")
        config.add_view(health, route_name="health")

        app = config.make_wsgi_app()

    print("Listening on http://localhost:6543")
    server = make_server("0.0.0.0", 6543, app)
    server.serve_forever()
```

See the [example](https://github.com/uptrace/uptrace-python/tree/master/example/pyramid) on GitHub for more details.

### Using OpenTelemetry SDK Directly

For a vendor-neutral setup, configure the OpenTelemetry SDK directly:

```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.instrumentation.pyramid import PyramidInstrumentor

# Configure resource attributes
resource = Resource.create({
    SERVICE_NAME: "pyramid-app",
    "service.version": "1.0.0",
})

# Set up tracing
provider = TracerProvider(resource=resource)
provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter())
)
trace.set_tracer_provider(provider)

# Instrument Pyramid
PyramidInstrumentor().instrument()

def home(request):
    return Response("Hello, World!")

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("home", "/")
        config.add_view(home, route_name="home")
        app = config.make_wsgi_app()

    server = make_server("0.0.0.0", 6543, app)
    server.serve_forever()
```

## Auto-Instrumentation with Bootstrap

As an alternative to programmatic setup, you can use `opentelemetry-instrument` to run your application with automatic instrumentation:

```shell
# Install the distro package (includes opentelemetry-bootstrap CLI)
pip install opentelemetry-distro opentelemetry-instrumentation

# Detect and install instrumentation for installed libraries
opentelemetry-bootstrap -a install

# Run with auto-instrumentation
opentelemetry-instrument \
  --service_name pyramid-app \
  --traces_exporter otlp \
  --metrics_exporter otlp \
  --exporter_otlp_endpoint https://api.uptrace.dev:4317 \
  --exporter_otlp_headers "uptrace-dsn=<FIXME>" \
  python app.py
```

This approach requires no code changes at all. The agent detects Pyramid and other installed libraries automatically.

## Custom Instrumentation

Add custom spans to trace specific business logic:

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def create_order(request):
    with tracer.start_as_current_span("create-order") as span:
        order_data = request.json_body
        span.set_attribute("order.customer_id", order_data.get("customer_id"))
        span.set_attribute("order.item_count", len(order_data.get("items", [])))

        try:
            # Validate order
            with tracer.start_as_current_span("validate-order"):
                validate_order(order_data)

            # Save to database
            with tracer.start_as_current_span("save-order") as db_span:
                db_span.set_attribute("db.operation", "INSERT")
                db_span.set_attribute("db.table", "orders")
                order_id = save_order(order_data)

            span.set_attribute("order.id", order_id)
            return Response(json={"order_id": order_id})

        except Exception as e:
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            return Response(json={"error": str(e)}, status=500)
```

## Database Instrumentation

Pyramid applications commonly use SQLAlchemy for database access. Add automatic tracing for all database queries:

```shell
pip install opentelemetry-instrumentation-sqlalchemy
```

```python
from sqlalchemy import create_engine
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

engine = create_engine("postgresql://user:password@localhost/mydb")

# Instrument SQLAlchemy engine
SQLAlchemyInstrumentor().instrument(
    engine=engine,
    enable_commenter=True,  # Add trace context to SQL comments
)
```

This captures all queries executed through the instrumented engine, including query text, execution time, and connection metadata.

For a detailed guide, see [SQLAlchemy instrumentation](/guides/opentelemetry-sqlalchemy).

## Excluding URLs

Disable tracing on specific routes by setting an environment variable with URL patterns:

```shell
export OTEL_PYTHON_PYRAMID_EXCLUDED_URLS="client/.*/info,healthcheck,metrics"
```

This is useful for excluding health check endpoints and other high-frequency, low-value routes from tracing.

## Capturing HTTP Headers

### Request Headers

Capture incoming HTTP request headers as span attributes:

```shell
# Specific headers
export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_REQUEST="content-type,custom_request_header"

# Pattern matching
export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_REQUEST="Accept.*,X-.*"

# All headers
export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_REQUEST=".*"
```

### Response Headers

Capture outgoing HTTP response headers:

```shell
# Specific headers
export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_RESPONSE="content-type,custom_response_header"

# Pattern matching
export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_RESPONSE="Content.*,X-.*"
```

### Sanitizing Sensitive Headers

Prevent storing sensitive data from captured headers:

```shell
export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SANITIZE_FIELDS=".*session.*,set-cookie,authorization"
```

See [documentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/pyramid/pyramid.html) for details.

## Environment Variables Configuration

Configure OpenTelemetry through environment variables for production deployments:

```shell
# Service identification
export OTEL_SERVICE_NAME="pyramid-app"
export OTEL_RESOURCE_ATTRIBUTES="service.version=1.0.0,deployment.environment=production"

# Exporter configuration
export OTEL_TRACES_EXPORTER="otlp"
export OTEL_METRICS_EXPORTER="otlp"
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.uptrace.dev:4317"
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>"
export OTEL_EXPORTER_OTLP_COMPRESSION="gzip"

# Sampling (optional - reduce volume in production)
export OTEL_TRACES_SAMPLER="parentbased_traceidratio"
export OTEL_TRACES_SAMPLER_ARG="0.1"
```

For the full list, see the [OpenTelemetry environment variables reference](/opentelemetry/env-vars).

## Production Deployment

### Using Gunicorn

Deploy with Gunicorn for production:

```shell
pip install gunicorn

gunicorn --bind 0.0.0.0:6543 --workers 4 "app:main()"
```

OpenTelemetry automatically instruments Gunicorn workers when `PyramidInstrumentor` is configured in your application.

### Using Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 6543

CMD ["gunicorn", "--bind", "0.0.0.0:6543", "--workers", "4", "app:main()"]
```

Run with environment variables:

```shell
docker run -p 6543:6543 \
  -e OTEL_SERVICE_NAME=pyramid-app \
  -e OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317 \
  -e OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>" \
  pyramid-app
```

## Troubleshooting

**No traces appearing**: Verify the OTLP endpoint is reachable and check that `PyramidInstrumentor().instrument()` is called before the WSGI app is created.

**Missing spans for specific routes**: Check if the route is excluded via `OTEL_PYTHON_PYRAMID_EXCLUDED_URLS`.

**High memory usage**: Reduce the batch processor queue size:

```python
from opentelemetry.sdk.trace.export import BatchSpanProcessor

processor = BatchSpanProcessor(
    exporter,
    max_queue_size=512,
    max_export_batch_size=128,
)
```

**Debug logging**: Enable verbose OpenTelemetry logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("opentelemetry").setLevel(logging.DEBUG)
```

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's next?

Your Pyramid application is now instrumented with OpenTelemetry for comprehensive monitoring. Next steps:

- [Flask instrumentation](/guides/opentelemetry-flask) for an alternative Python web framework
- [Django instrumentation](/guides/opentelemetry-django) for full-featured Python web applications
- [SQLAlchemy instrumentation](/guides/opentelemetry-sqlalchemy) for database monitoring
- [OpenTelemetry Python guide](/get/opentelemetry-python) for deeper instrumentation options
