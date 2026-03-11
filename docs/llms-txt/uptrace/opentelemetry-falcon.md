# Source: https://uptrace.dev/raw/guides/opentelemetry-falcon.md

# OpenTelemetry Falcon Instrumentation and Monitoring

> Instrument and monitor Falcon applications with OpenTelemetry. Setup FalconInstrumentor for automatic tracing, performance monitoring, and error tracking.

OpenTelemetry Falcon instrumentation provides automatic tracing for HTTP requests and application performance monitoring. Using FalconInstrumentor, you can add observability to Falcon applications, enabling distributed tracing and error tracking across your Python API services.

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
      Install OpenTelemetry Falcon instrumentation
    </td>
    
    <td>
      <code>
        pip install opentelemetry-instrumentation-falcon
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      2. Import
    </td>
    
    <td>
      Import FalconInstrumentor
    </td>
    
    <td>
      <code>
        from opentelemetry.instrumentation.falcon import FalconInstrumentor
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
        FalconInstrumentor().instrument()
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      4. Run
    </td>
    
    <td>
      Start your Falcon application
    </td>
    
    <td>
      Traces collected automatically
    </td>
  </tr>
</tbody>
</table>

**Minimal working example:**

```python
import falcon
from opentelemetry.instrumentation.falcon import FalconInstrumentor

# Instrument Falcon before creating the app
FalconInstrumentor().instrument()

class HelloResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello World'}

app = falcon.App()
app.add_route('/hello', HelloResource())
```

This single `FalconInstrumentor().instrument()` call automatically captures all incoming HTTP requests, traces request flow, and exports telemetry data to your configured backend.

## What is Falcon?

Falcon is a minimalist, high-performance web framework for building RESTful APIs and microservices in Python. Known for its speed and low overhead, Falcon is designed for building fast, scalable backend services.

Key features of Falcon include:

- High performance with minimal overhead (one of the fastest Python frameworks)
- WSGI and ASGI support for flexible deployment
- Request and response objects with intuitive APIs
- Middleware support for cross-cutting concerns
- Built-in support for URI templates and routing
- Minimal dependencies for lightweight deployments

Falcon's focus on performance makes it ideal for building APIs that handle high request volumes.

## What is OpenTelemetry?

[OpenTelemetry](/opentelemetry) is an open-source observability framework that provides a standardized way to collect, process, and export telemetry data from applications. It combines three pillars of observability: [traces](/opentelemetry/distributed-tracing), [metrics](/opentelemetry/metrics), and [logs](/opentelemetry/logs).

OpenTelemetry supports multiple programming languages and platforms, making it suitable for a wide range of applications and environments.

OpenTelemetry enables developers to instrument their code and collect telemetry data, which can then be exported to various [OpenTelemetry backends](/blog/opentelemetry-backend) or observability platforms for analysis and visualization. The [OpenTelemetry Operator](/opentelemetry/operator) can automatically inject instrumentation into your applications when running in Kubernetes.

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Python zero-code instrumentation guide](/get/opentelemetry-python/zero-code).

</alert>

## Prerequisites and Installation

### System Requirements

- Python 3.8 or higher
- pip package manager
- A Falcon application (existing or new)

### Core Dependencies

Install the essential OpenTelemetry packages for Falcon. For comprehensive Python instrumentation, see the [OpenTelemetry Python guide](/get/opentelemetry-python).

```shell
# Core OpenTelemetry packages
pip install opentelemetry-api opentelemetry-sdk

# Falcon-specific instrumentation
pip install opentelemetry-instrumentation-falcon

# OTLP exporter for sending data to backends
pip install opentelemetry-exporter-otlp
```

## Basic Setup

Configure OpenTelemetry and instrument your Falcon application:

```python
import falcon
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.instrumentation.falcon import FalconInstrumentor

# Configure OpenTelemetry
resource = Resource.create({SERVICE_NAME: "my-falcon-api"})
trace_provider = TracerProvider(resource=resource)
trace_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
trace.set_tracer_provider(trace_provider)

# Instrument Falcon before creating the app
FalconInstrumentor().instrument()

# Create Falcon application
class HelloWorldResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello World'}

app = falcon.App()
app.add_route('/hello', HelloWorldResource())
```

## Instrumentation Options

The FalconInstrumentor supports several configuration options:

<table>
<thead>
  <tr>
    <th>
      Option
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
        request_hook
      </code>
    </td>
    
    <td>
      Callback called when a span is created
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        response_hook
      </code>
    </td>
    
    <td>
      Callback called before the span is finished
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        tracer_provider
      </code>
    </td>
    
    <td>
      Use a custom TracerProvider
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        meter_provider
      </code>
    </td>
    
    <td>
      Use a custom MeterProvider
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        excluded_urls
      </code>
    </td>
    
    <td>
      Comma-separated URL patterns to exclude from tracing
    </td>
  </tr>
</tbody>
</table>

### Excluding URLs

Exclude certain URLs from being traced using environment variables:

```shell
# Excludes requests such as `https://site/client/123/info` and `https://site/xyz/healthcheck`
export OTEL_PYTHON_FALCON_EXCLUDED_URLS="client/.*/info,healthcheck"
```

Or configure programmatically:

```python
FalconInstrumentor().instrument(excluded_urls="health,metrics,ready")
```

### Traced Request Attributes

Extract specific attributes from Falcon's request object:

```shell
export OTEL_PYTHON_FALCON_TRACED_REQUEST_ATTRS='query_string,uri_template'
```

See [documentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/falcon/falcon.html) for more details.

## Request and Response Hooks

Use hooks to customize span attributes based on request and response data:

```python
from opentelemetry.instrumentation.falcon import FalconInstrumentor

def request_hook(span, req):
    """Called right after a span is created."""
    if span and span.is_recording():
        # Add custom attributes from the request
        span.set_attribute("http.user_agent", req.user_agent or "unknown")
        span.set_attribute("http.client_ip", req.remote_addr)

        # Add API version from header
        api_version = req.get_header("X-API-Version")
        if api_version:
            span.set_attribute("api.version", api_version)

def response_hook(span, req, resp):
    """Called right before the span is finished."""
    if span and span.is_recording():
        # Add response attributes
        span.set_attribute("http.response.content_type", resp.content_type or "unknown")

FalconInstrumentor().instrument(
    request_hook=request_hook,
    response_hook=response_hook
)
```

## Creating Custom Spans

Add custom spans to trace specific operations within your resources:

```python
import falcon
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class UserResource:
    def on_get(self, req, resp, user_id):
        # Create a custom span for database operation
        with tracer.start_as_current_span("fetch_user") as span:
            span.set_attribute("user.id", user_id)

            user = self.fetch_user_from_db(user_id)

            if user:
                span.set_attribute("user.found", True)
                resp.media = user
            else:
                span.set_attribute("user.found", False)
                resp.status = falcon.HTTP_404
                resp.media = {"error": "User not found"}

    def fetch_user_from_db(self, user_id):
        with tracer.start_as_current_span("database_query") as span:
            span.set_attribute("db.operation", "SELECT")
            span.set_attribute("db.table", "users")
            # Database logic here
            return {"id": user_id, "name": "John Doe"}
```

## Recording Errors

Record errors in your resources to mark spans as failed:

```python
import falcon
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

class ProcessResource:
    def on_post(self, req, resp):
        span = trace.get_current_span()

        try:
            data = req.media
            result = self.process_data(data)
            resp.media = {"result": result}
        except ValueError as e:
            # Record the error on the span
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR, str(e)))

            resp.status = falcon.HTTP_400
            resp.media = {"error": str(e)}
        except Exception as e:
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR, "Internal server error"))

            resp.status = falcon.HTTP_500
            resp.media = {"error": "Internal server error"}

    def process_data(self, data):
        if not data:
            raise ValueError("No data provided")
        return {"processed": True}
```

## Middleware Integration

Create custom middleware to add observability across all requests:

```python
import falcon
from opentelemetry import trace

class TelemetryMiddleware:
    def process_request(self, req, resp):
        """Add custom attributes to the current span."""
        span = trace.get_current_span()
        if span and span.is_recording():
            # Add request ID for correlation
            request_id = req.get_header("X-Request-ID")
            if request_id:
                span.set_attribute("request.id", request_id)

            # Add tenant information for multi-tenant apps
            tenant_id = req.get_header("X-Tenant-ID")
            if tenant_id:
                span.set_attribute("tenant.id", tenant_id)

    def process_response(self, req, resp, resource, req_succeeded):
        """Add response information to the span."""
        span = trace.get_current_span()
        if span and span.is_recording():
            span.set_attribute("request.succeeded", req_succeeded)

app = falcon.App(middleware=[TelemetryMiddleware()])
```

## Captured Span Attributes

The Falcon instrumentation automatically captures attributes following the [OpenTelemetry semantic conventions](/opentelemetry/semconv):

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
        http.request.method
      </code>
    </td>
    
    <td>
      HTTP method (GET, POST, etc.)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        url.full
      </code>
    </td>
    
    <td>
      Full request URL
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        url.path
      </code>
    </td>
    
    <td>
      Request path
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.response.status_code
      </code>
    </td>
    
    <td>
      HTTP response status code
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        url.scheme
      </code>
    </td>
    
    <td>
      URL scheme (http/https)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server.address
      </code>
    </td>
    
    <td>
      Request host
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.route
      </code>
    </td>
    
    <td>
      Matched route template
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server.port
      </code>
    </td>
    
    <td>
      Server port
    </td>
  </tr>
</tbody>
</table>

<alert type="info">

Older versions of the instrumentation use legacy attribute names like `http.method` and `http.status_code`. Upgrade to the latest `opentelemetry-instrumentation-falcon` to get the stable [HTTP semantic conventions](/opentelemetry/semconv).

</alert>

## Configuration with Uptrace

To export telemetry data to Uptrace:

```python
import falcon
import uptrace
from opentelemetry.instrumentation.falcon import FalconInstrumentor

# Configure Uptrace
uptrace.configure_opentelemetry(
    dsn="https://<token>@api.uptrace.dev/<project_id>",
    service_name="my-falcon-api",
    service_version="1.0.0",
)

# Instrument Falcon
FalconInstrumentor().instrument()

# Create application
app = falcon.App()
```

## FAQ

**What version of Falcon is supported?** OpenTelemetry Falcon instrumentation supports Falcon 2.x and 3.x. The examples in this guide use Falcon 3.x syntax (`falcon.App()` instead of the deprecated `falcon.API()`).

**How do I instrument ASGI Falcon apps?** For ASGI applications, use `opentelemetry-instrumentation-asgi` alongside the Falcon instrumentation. The Falcon instrumentation works with both WSGI and ASGI apps.

**Why are my health check endpoints being traced?** Use `excluded_urls` to skip tracing for endpoints like `/health` or `/ready`. This reduces noise and telemetry costs.

**How do I correlate logs with traces?** Use OpenTelemetry's logging instrumentation (`opentelemetry-instrumentation-logging`) to automatically inject trace and span IDs into your log records.

**Can I use Falcon with auto-instrumentation?** Yes, you can use `opentelemetry-bootstrap -a install` to detect and install all available instrumentations, then run with `opentelemetry-instrument python app.py`.

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's next?

With OpenTelemetry Falcon instrumentation in place, you can monitor request latency, track error rates, and trace requests across your distributed systems.

Next steps to enhance your observability:

- Create custom spans using the [OpenTelemetry Python Tracing API](/get/opentelemetry-python/tracing)
- Add database instrumentation with [SQLAlchemy](/guides/opentelemetry-sqlalchemy)
- Explore other Python frameworks like [FastAPI](/guides/opentelemetry-fastapi) or [Django](/guides/opentelemetry-django)
- Set up the [OpenTelemetry Collector](/opentelemetry/collector) for production deployments
