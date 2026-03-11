# Source: https://uptrace.dev/raw/guides/opentelemetry-django.md

# Django OpenTelemetry Instrumentation and Monitoring

> Instrument and monitor Django applications with OpenTelemetry. Setup DjangoInstrumentor, auto/manual tracing, metrics collection, database monitoring, async tasks, and Docker deployment.

OpenTelemetry enables comprehensive monitoring of Django applications by automatically collecting telemetry data including request and response times, database query performance, and custom metrics. By integrating OpenTelemetry, you can capture distributed traces and metrics, then export this data to various observability backends for analysis and visualization.

## What is Django?

Django is an open-source, high-level web framework written in Python. It follows the Model-View-Template (MVT) architectural pattern and provides a robust set of tools and features that simplify and accelerate web application development.

Django is designed to promote clean, maintainable code and follows the "Don't Repeat Yourself" (DRY) principle, emphasizing code reusability and reducing redundancy.

## What is OpenTelemetry?

OpenTelemetry is an open-source observability framework that provides a standardized way to collect, process, and export telemetry data from applications and infrastructure. It combines metrics, logs, and [distributed traces](/opentelemetry/distributed-tracing) into a unified toolkit that helps developers understand how their systems are performing.

The framework solves vendor lock-in by providing consistent instrumentation across different technology stacks. Teams can instrument their applications once with OpenTelemetry and send that data to any compatible observability platform, making it easier to monitor complex, distributed systems without being tied to specific monitoring vendors. The [OpenTelemetry architecture](/opentelemetry/architecture) is designed with modularity in mind, consisting of APIs, SDKs, and the Collector that work together seamlessly.

## Monitoring Options Comparison

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      OpenTelemetry
    </th>
    
    <th>
      Django Debug Toolbar
    </th>
    
    <th>
      Prometheus
    </th>
    
    <th>
      Sentry
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Primary Use Case
      </strong>
    </td>
    
    <td>
      Production observability
    </td>
    
    <td>
      Development debugging
    </td>
    
    <td>
      Metrics collection
    </td>
    
    <td>
      Error tracking
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Traces
      </strong>
    </td>
    
    <td>
      Yes (distributed)
    </td>
    
    <td>
      No
    </td>
    
    <td>
      No
    </td>
    
    <td>
      Limited
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Metrics
      </strong>
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      No
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      No
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Logs
      </strong>
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes (dev only)
    </td>
    
    <td>
      No
    </td>
    
    <td>
      Limited
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Vendor Lock-in
      </strong>
    </td>
    
    <td>
      None
    </td>
    
    <td>
      N/A
    </td>
    
    <td>
      None
    </td>
    
    <td>
      Vendor-specific
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Production Ready
      </strong>
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      No (dev only)
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Best For
      </strong>
    </td>
    
    <td>
      Full-stack observability
    </td>
    
    <td>
      Local development
    </td>
    
    <td>
      Infrastructure metrics
    </td>
    
    <td>
      Error monitoring
    </td>
  </tr>
</tbody>
</table>

OpenTelemetry provides comprehensive observability suitable for production environments, while other tools serve specific purposes like development debugging or focused monitoring needs.

## Installation

To instrument a Django application with OpenTelemetry, install the required packages. For comprehensive Python instrumentation details, see the [OpenTelemetry Python guide](/get/opentelemetry-python).

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Python zero-code instrumentation guide](/get/opentelemetry-python/zero-code).

</alert>

```shell
pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-django
```

### Additional Database-Specific Instrumentation

Depending on your database backend, you may also need to install additional instrumentation packages:

```shell
# For PostgreSQL
pip install opentelemetry-instrumentation-psycopg2

# For MySQL
pip install opentelemetry-instrumentation-dbapi

# For SQLite
pip install opentelemetry-instrumentation-sqlite3
```

### Exporter Installation

To export telemetry data to observability backends, install an appropriate exporter:

```shell
# For OTLP (recommended)
pip install opentelemetry-exporter-otlp

# For console output (development/testing)
pip install opentelemetry-exporter-otlp-proto-http
```

## OpenTelemetry SDK Configuration

Initialize OpenTelemetry in your Django application by adding the following configuration to your application's startup code. This should be placed in your `manage.py`, `wsgi.py`, or a dedicated configuration module:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create resource with service information
resource = Resource(attributes={
    SERVICE_NAME: "your-django-app"
})

# Create and configure the tracer provider
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Set the global default tracer provider
trace.set_tracer_provider(provider)

# Create a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")
```

## Basic Usage

### Manual Instrumentation

Django instrumentation relies on the `DJANGO_SETTINGS_MODULE` environment variable to locate your settings file. Since Django defines this variable in the `manage.py` file, you should instrument your Django application from that file:

```python
# manage.py
import os
import sys
from opentelemetry.instrumentation.django import DjangoInstrumentor

def main():
    # Ensure DJANGO_SETTINGS_MODULE is set before instrumenting
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    # Initialize Django instrumentation
    DjangoInstrumentor().instrument()

    # Your existing Django management code here
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

### Auto-Instrumentation

For a simpler setup without code modifications, you can use OpenTelemetry's auto-instrumentation:

```shell
# First, install the auto-instrumentation packages
pip install opentelemetry-distro

# Bootstrap to install all relevant instrumentation packages
opentelemetry-bootstrap -a install

# Run your Django application with auto-instrumentation
opentelemetry-instrument python manage.py runserver --noreload
```

**Note:** Use the `--noreload` flag to prevent Django from running the initialization twice.

## Creating Custom Spans

OpenTelemetry automatically traces incoming HTTP requests to your Django application. You can also create custom spans to trace specific parts of your code:

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def my_view(request):
    # Create a custom span for specific business logic
    with tracer.start_as_current_span("custom-business-logic"):
        # Your application code here
        result = perform_complex_operation()

        # Add attributes to the span for better observability
        span = trace.get_current_span()
        span.set_attribute("operation.result", str(result))
        span.set_attribute("user.id", request.user.id if request.user.is_authenticated else "anonymous")

    return HttpResponse("Hello, World!")
```

## Collecting Metrics

OpenTelemetry enables you to collect custom metrics alongside traces to monitor application performance, track business KPIs, and measure resource utilization. Django applications can benefit from metrics like request counts, response times, database query durations, and custom business metrics.

### Setting Up Metrics

First, configure the metrics provider in your application startup:

```python
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME

# Create resource with service information
resource = Resource(attributes={
    SERVICE_NAME: "your-django-app"
})

# Create metrics reader and provider
reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)

# Get a meter for creating instruments
meter = metrics.get_meter("django.metrics")
```

### Creating Metric Instruments

OpenTelemetry provides three main types of metrics instruments:

**Counter** - For monotonically increasing values:

```python
from opentelemetry import metrics

meter = metrics.get_meter(__name__)
request_counter = meter.create_counter(
    name="http.server.requests",
    description="Total number of HTTP requests",
    unit="1"
)

def my_view(request):
    # Increment counter for each request
    request_counter.add(1, {
        "http.method": request.method,
        "http.route": request.path
    })
    return HttpResponse("Hello, World!")
```

**Histogram** - For recording distributions of values:

```python
response_time_histogram = meter.create_histogram(
    name="http.server.duration",
    description="HTTP request duration",
    unit="ms"
)

import time

def my_view(request):
    start_time = time.time()

    # Your business logic here
    result = process_request(request)

    # Record duration
    duration_ms = (time.time() - start_time) * 1000
    response_time_histogram.record(duration_ms, {
        "http.method": request.method,
        "http.status_code": 200
    })

    return HttpResponse(result)
```

**UpDownCounter** - For values that can increase or decrease:

```python
active_users = meter.create_up_down_counter(
    name="active.users",
    description="Number of currently active users",
    unit="1"
)

def user_login(request):
    active_users.add(1)
    # Login logic here

def user_logout(request):
    active_users.add(-1)
    # Logout logic here
```

### Django Middleware for Request Metrics

Create custom middleware to automatically collect metrics for all requests:

```python
# middleware.py
from opentelemetry import metrics
import time

class MetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        meter = metrics.get_meter(__name__)

        self.request_counter = meter.create_counter(
            "django.requests.total",
            description="Total HTTP requests"
        )
        self.request_duration = meter.create_histogram(
            "django.requests.duration",
            description="HTTP request duration",
            unit="ms"
        )

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = (time.time() - start_time) * 1000

        attributes = {
            "http.method": request.method,
            "http.route": request.path,
            "http.status_code": response.status_code
        }

        self.request_counter.add(1, attributes)
        self.request_duration.record(duration, attributes)

        return response
```

Add the middleware to your `settings.py`:

```python
MIDDLEWARE = [
    'myapp.middleware.MetricsMiddleware',
    # ... other middleware
]
```

## Context Propagation for Background Tasks

Django applications often use background task queues like Celery for asynchronous processing. OpenTelemetry supports distributed tracing across these boundaries through context propagation, allowing you to trace requests from the initial web request through background task execution.

### Celery Integration

For comprehensive Celery task monitoring, see the [OpenTelemetry Celery guide](/guides/opentelemetry-celery). Here's a basic example of context propagation:

```python
from opentelemetry import trace
from opentelemetry.propagate import inject, extract
from celery import shared_task

# Django view that triggers a background task
def my_view(request):
    # Create carrier for context propagation
    carrier = {}
    inject(carrier)

    # Send task with propagated context
    process_data.delay(data=request.POST, context=carrier)

    return HttpResponse("Task queued")

# Celery task that receives propagated context
@shared_task
def process_data(data, context):
    # Extract context from carrier
    ctx = extract(context)
    tracer = trace.get_tracer(__name__)

    # Continue the trace in background task
    with tracer.start_as_current_span("celery.process_data", context=ctx):
        # Your background processing logic
        result = perform_expensive_operation(data)
        return result
```

### Manual Context Propagation

For custom async patterns or other task queues:

```python
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry import trace

def enqueue_task(task_data):
    # Create carrier dictionary
    carrier = {}

    # Inject current trace context
    propagator = TraceContextTextMapPropagator()
    propagator.inject(carrier)

    # Add carrier to task data
    task_data['trace_context'] = carrier

    # Send to queue
    queue.send(task_data)

def process_task(task_data):
    # Extract trace context
    carrier = task_data.get('trace_context', {})
    propagator = TraceContextTextMapPropagator()
    ctx = propagator.extract(carrier)

    tracer = trace.get_tracer(__name__)

    # Continue trace in task processor
    with tracer.start_as_current_span("task.processing", context=ctx):
        # Process the task
        result = handle_task(task_data)
```

## Deployment Configuration

### uWSGI

When using Django with uWSGI, initialize OpenTelemetry using the post-fork hook to ensure proper instrumentation in worker processes. Add this to your application startup file:

```python
from uwsgidecorators import postfork
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor

@postfork
def init_tracing():
    # Initialize OpenTelemetry
    provider = TracerProvider()
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Instrument Django
    DjangoInstrumentor().instrument()
```

### Gunicorn

For Django with Gunicorn, use the post-fork hook in your `gunicorn.conf.py`:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    # Initialize OpenTelemetry
    provider = TracerProvider()
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Instrument Django
    DjangoInstrumentor().instrument()
```

### Docker

Django applications commonly run in Docker containers for production deployments. For comprehensive Docker observability patterns, see the [OpenTelemetry Docker guide](/guides/opentelemetry-docker).

Here's how to configure OpenTelemetry in a containerized Django application:

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenTelemetry packages
RUN pip install opentelemetry-api \
                opentelemetry-sdk \
                opentelemetry-instrumentation-django \
                opentelemetry-exporter-otlp

# Copy application code
COPY . .

# Expose Django port
EXPOSE 8000

# Use Gunicorn with OpenTelemetry
CMD ["gunicorn", "--config", "gunicorn.conf.py", "myproject.wsgi:application"]
```

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  django:
    build: .
    ports:
      - "8000:8000"
    environment:
      # Django settings
      - DJANGO_SETTINGS_MODULE=myproject.settings

      # OpenTelemetry configuration
      - OTEL_SERVICE_NAME=my-django-app
      - OTEL_SERVICE_VERSION=1.0.0
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://collector:4317
      - OTEL_EXPORTER_OTLP_PROTOCOL=grpc
      - OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production

      # Database configuration
      - DATABASE_URL=postgresql://user:password@db:5432/dbname
    depends_on:
      - db
      - collector

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=dbname
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  collector:
    image: otel/opentelemetry-collector:latest
    command: ["--config=/etc/otel-collector-config.yaml"]
    volumes:
      - ./otel-collector-config.yaml:/etc/otel-collector-config.yaml
    ports:
      - "4317:4317"   # OTLP gRPC receiver
      - "4318:4318"   # OTLP HTTP receiver

volumes:
  postgres_data:
```

**Environment Variables:**

Configure OpenTelemetry using environment variables in your Docker environment:

```shell
# Service identification
OTEL_SERVICE_NAME=my-django-app
OTEL_SERVICE_VERSION=1.0.0

# Exporter configuration
OTEL_EXPORTER_OTLP_ENDPOINT=http://collector:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc

# Resource attributes
OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production,service.namespace=web
```

## Database Instrumentation

### PostgreSQL

For PostgreSQL-specific monitoring patterns and advanced configuration, see the [OpenTelemetry PostgreSQL guide](/guides/opentelemetry-postgresql).

Configure Django to use PostgreSQL by updating your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

The PostgreSQL backend uses the psycopg2 library internally. Install and configure the instrumentation:

```shell
pip install opentelemetry-instrumentation-psycopg2
```

Then instrument the library in your initialization code:

```python
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor

Psycopg2Instrumentor().instrument()
```

For [Gunicorn](#gunicorn) or [uWSGI](#uwsgi) deployments, add this instrumentation to your post-fork hooks.

### MySQL

For MySQL-specific monitoring patterns and query optimization insights, see the [OpenTelemetry MySQL guide](/guides/opentelemetry-mysql).

Configure Django to use MySQL by updating your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

The MySQL backend uses the [mysqlclient](https://pypi.org/project/mysqlclient/) library, which implements the Python Database API. Install the DB API instrumentation:

```shell
pip install opentelemetry-instrumentation-dbapi
```

Then instrument the mysqlclient library:

```python
import MySQLdb
from opentelemetry.instrumentation.dbapi import trace_integration

trace_integration(MySQLdb, "connect", "mysql")
```

For [Gunicorn](#gunicorn) or [uWSGI](#uwsgi) deployments, add this instrumentation to your post-fork hooks.

### SQLite

Configure Django to use SQLite by updating your `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

The SQLite backend uses Python's built-in [sqlite3](https://docs.python.org/3/library/sqlite3.html) library. Install the SQLite instrumentation:

```shell
pip install opentelemetry-instrumentation-sqlite3
```

Then instrument the sqlite3 library:

```python
from opentelemetry.instrumentation.sqlite3 import SQLite3Instrumentor

SQLite3Instrumentor().instrument()
```

For [Gunicorn](#gunicorn) or [uWSGI](#uwsgi) deployments, add this instrumentation to your post-fork hooks.

## Advanced Configuration

### Environment Variables

OpenTelemetry supports configuration through environment variables. Common ones include:

```shell
# Service identification
export OTEL_SERVICE_NAME="my-django-app"
export OTEL_SERVICE_VERSION="1.0.0"

# Exporter configuration
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
export OTEL_EXPORTER_OTLP_PROTOCOL="grpc"

# Resource attributes
export OTEL_RESOURCE_ATTRIBUTES="service.name=my-django-app,service.version=1.0.0"

# Disable specific instrumentations if needed
export OTEL_PYTHON_DJANGO_INSTRUMENT=false
```

### SQL Commentor

You can enable SQL commentor to enrich database queries with contextual information:

```python
from opentelemetry.instrumentation.django import DjangoInstrumentor

DjangoInstrumentor().instrument(is_sql_commentor_enabled=True)
```

This will append contextual tags to your SQL queries, transforming `SELECT * FROM users` into `SELECT * FROM users /*controller='users',action='index'*/`.

### Sampling Configuration

To control the volume of telemetry data, configure sampling in your tracer provider:

```python
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased

# Sample 10% of traces
sampler = TraceIdRatioBased(0.1)
provider = TracerProvider(sampler=sampler)
```

### Custom Resource Attributes

Add custom resource attributes to provide additional context:

```python
from opentelemetry.sdk.resources import Resource

resource = Resource.create({
    "service.name": "my-django-app",
    "service.version": "1.0.0",
    "deployment.environment": "production",
    "service.instance.id": "instance-123"
})

provider = TracerProvider(resource=resource)
```

## Error Handling and Exception Tracking

OpenTelemetry automatically captures unhandled exceptions, but you can also manually record exceptions:

```python
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

def my_view(request):
    span = trace.get_current_span()
    try:
        # Your business logic here
        result = risky_operation()
        return JsonResponse({"result": result})
    except Exception as e:
        # Record the exception and set error status
        span.record_exception(e)
        span.set_status(Status(StatusCode.ERROR, str(e)))
        return JsonResponse({"error": "Something went wrong"}, status=500)
```

## Performance Considerations

OpenTelemetry is designed to be efficient and lightweight, but it does introduce some overhead due to instrumentation and telemetry collection. The performance impact depends on several factors:

- **Volume of telemetry data**: More spans and attributes increase overhead
- **Exporter configuration**: Batch exporters are more efficient than real-time exporters
- **Sampling rate**: Lower sampling rates reduce overhead
- **System resources**: Available CPU and memory affect performance

To optimize performance:

1. **Configure appropriate sampling rates** to balance observability needs with performance
2. **Use batch exporters** instead of synchronous exporters when possible
3. **Monitor resource usage** and adjust configuration as needed
4. **Profile your application** to identify any performance bottlenecks introduced by instrumentation
5. **Use environment variables** to disable unnecessary instrumentations

## Production Deployment Best Practices

### Security Considerations

- Use secure endpoints (HTTPS) for exporting telemetry data
- Avoid logging sensitive information in span attributes
- Configure proper authentication for telemetry backends
- Review and sanitize custom attributes before adding them to spans

### Resource Management

- Set appropriate memory limits for batch processors
- Configure timeouts for exporters to prevent blocking
- Monitor the telemetry pipeline's resource consumption
- Use compression when exporting large volumes of data

### Monitoring the Monitor

- Set up health checks for your telemetry pipeline
- Monitor exporter success/failure rates
- Track the volume of telemetry data being generated
- Alert on telemetry pipeline failures

## What is Uptrace?

Uptrace is a high-performance, open-source [Application Performance Monitoring (APM)](/opentelemetry/apm) platform built for modern distributed systems. Whether you're debugging microservices, optimizing database queries, or ensuring SLA compliance, Uptrace provides unified observability without vendor lock-in.

### Key Features

Uptrace offers all-in-one observability with a single interface for traces, metrics, and logs, eliminating the need for context switching between multiple [APM tools](/tools/top-apm-tools). Built on OpenTelemetry standards for maximum compatibility, it provides:

- **Blazing Fast Performance**: Processes 10,000+ spans per second on a single core with advanced compression reducing 1KB spans to ~40 bytes
- **Cost-Effective at Scale**: AGPL open-source license with 95% storage savings vs. traditional solutions and no per-seat pricing or data ingestion limits
- **Developer-First Experience**: SQL-like query language for traces, PromQL-compatible metrics queries, and modern Vue.js UI with intuitive workflows

### Architecture

Uptrace leverages ClickHouse for real-time analysis with sub-second queries on billions of spans and exceptional 10:1 compression ratios, while PostgreSQL handles metadata with ACID compliance and rich data types support.

### Deployment Options

1. **Cloud (Fastest)**: Uptrace Cloud requires no installation, maintenance, or scaling. Sign up for a free account and get 1TB of storage and 100,000 timeseries
2. **Self-Hosted**: Deploy using Docker Compose with full control over your data. For more deployment options, see [open-source APM setup](/get/hosted/open-source-apm)

## uptrace-python OpenTelemetry Wrapper

uptrace-python is a thin wrapper over OpenTelemetry Python that configures OpenTelemetry SDK to export data to Uptrace. It does not add any new functionality and is provided only for your convenience.

### Installation

```shell
pip install uptrace
```

### Configuration for Django

Add the following configuration to your Django application's startup code (typically in `manage.py` or `wsgi.py`):

```python
import uptrace
from opentelemetry import trace

# Configure OpenTelemetry with Uptrace
uptrace.configure_opentelemetry(
    # Set DSN or use UPTRACE_DSN environment variable
    dsn="<your-uptrace-dsn>",
    service_name="my-django-app",
    service_version="1.0.0",
    deployment_environment="production",
)

# Get a tracer
tracer = trace.get_tracer("my_django_app", "1.0.0")
```

### Configuration Options

The following configuration options are supported:

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
        dsn
      </code>
    </td>
    
    <td>
      A data source that is used to connect to uptrace.dev
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service_name
      </code>
    </td>
    
    <td>
      service.name resource attribute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service_version
      </code>
    </td>
    
    <td>
      service.version resource attribute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        deployment_environment
      </code>
    </td>
    
    <td>
      deployment.environment resource attribute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resource_attributes
      </code>
    </td>
    
    <td>
      Any other resource attributes
    </td>
  </tr>
</tbody>
</table>

### Environment Variables

You can also use environment variables to configure the client:

```shell
# Data source name
export UPTRACE_DSN="https://<token>@uptrace.dev/<project_id>"

# Resource attributes
export OTEL_RESOURCE_ATTRIBUTES="service.name=my-django-app,service.version=1.0.0"

# Service name (takes precedence over OTEL_RESOURCE_ATTRIBUTES)
export OTEL_SERVICE_NAME="my-django-app"

# Propagators
export OTEL_PROPAGATORS="tracecontext,baggage"
```

### Django Integration Example

Here's a complete example for integrating uptrace-python with Django:

```python
# manage.py
import os
import sys
import uptrace
from opentelemetry.instrumentation.django import DjangoInstrumentor

def main():
    # Set Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

    # Configure Uptrace OpenTelemetry
    uptrace.configure_opentelemetry(
        # DSN from environment variable or directly
        # dsn="https://<token>@uptrace.dev/<project_id>",
        service_name="my-django-app",
        service_version="1.0.0",
        deployment_environment=os.environ.get("ENVIRONMENT", "development"),
    )

    # Instrument Django
    DjangoInstrumentor().instrument()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

### Gunicorn Integration

With Gunicorn, use the post_fork hook in your `gunicorn.conf.py`:

```python
import uptrace
from opentelemetry.instrumentation.django import DjangoInstrumentor

def post_fork(server, worker):
    uptrace.configure_opentelemetry(
        service_name="my-django-app",
        service_version="1.0.0",
        deployment_environment="production",
    )
    DjangoInstrumentor().instrument()
```

### uWSGI Integration

With uWSGI, use the postfork decorator:

```python
from uwsgidecorators import postfork
import uptrace
from opentelemetry.instrumentation.django import DjangoInstrumentor

@postfork
def init_tracing():
    uptrace.configure_opentelemetry(
        service_name="my-django-app",
        service_version="1.0.0",
        deployment_environment="production",
    )
    DjangoInstrumentor().instrument()
```

### Viewing Traces

uptrace-python provides a convenient way to get trace URLs:

```python
from opentelemetry import trace
import uptrace

def my_view(request):
    span = trace.get_current_span()

    # Your business logic here

    # Get the trace URL for debugging
    trace_url = uptrace.trace_url(span)
    print(f"View trace at: {trace_url}")

    return JsonResponse({"status": "success"})
```

### Performance Recommendations

To maximize performance and efficiency when using Uptrace, consider the following recommendations:

1. **Use BatchSpanProcessor**: Essential for exporting multiple spans in a single request
2. **Enable gzip compression**: Essential to compress data before sending and reduce traffic costs
3. **Prefer delta metrics temporality**: Recommended because such metrics are smaller and Uptrace converts cumulative metrics to delta anyway
4. **Use Protobuf over JSON**: Recommended as a generally more efficient encoding
5. **Prefer HTTP over gRPC**: Recommended as a more mature transport with better compatibility

### Troubleshooting SSL Errors

If you are getting SSL errors, try using different root certificates as a workaround:

```shell
export GRPC_DEFAULT_SSL_ROOTS_FILE_PATH=/etc/ssl/certs/ca-certificates.crt
```

## Troubleshooting

### Common Issues

<table>
<thead>
  <tr>
    <th>
      Issue
    </th>
    
    <th>
      Symptoms
    </th>
    
    <th>
      Solution
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      DJANGO_SETTINGS_MODULE not found
    </td>
    
    <td>
      ImportError or configuration errors on startup
    </td>
    
    <td>
      Set environment variable before calling <code>
        DjangoInstrumentor().instrument()
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Missing database instrumentation
    </td>
    
    <td>
      No database query spans in traces
    </td>
    
    <td>
      Install database-specific packages (psycopg2, dbapi, sqlite3)
    </td>
  </tr>
  
  <tr>
    <td>
      Worker process issues
    </td>
    
    <td>
      Spans missing in production with Gunicorn/uWSGI
    </td>
    
    <td>
      Use post-fork hooks to initialize OpenTelemetry after worker spawn
    </td>
  </tr>
  
  <tr>
    <td>
      High performance overhead
    </td>
    
    <td>
      Increased request latency
    </td>
    
    <td>
      Adjust sampling rates, use batch exporters, reduce custom spans
    </td>
  </tr>
  
  <tr>
    <td>
      Spans not appearing
    </td>
    
    <td>
      No trace data in backend
    </td>
    
    <td>
      Verify exporter endpoint, check network connectivity, enable debug logging
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-reload conflicts
    </td>
    
    <td>
      Duplicate instrumentation or initialization errors
    </td>
    
    <td>
      Use <code>
        --noreload
      </code>
      
       flag with <code>
        python manage.py runserver --noreload
      </code>
    </td>
  </tr>
</tbody>
</table>

### Debug Mode

To enable debug logging for OpenTelemetry:

```python
import logging

# Enable debug logging for OpenTelemetry
logging.getLogger("opentelemetry").setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
```

### Testing Instrumentation

You can test your instrumentation locally using the console exporter:

```python
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

# Use console exporter for testing
processor = BatchSpanProcessor(ConsoleSpanExporter())
```

## Best Practices

1. **Initialize instrumentation early**: Set up OpenTelemetry before your Django application starts handling requests
2. **Use meaningful span names**: Create descriptive span names that help identify operations
3. **Add relevant attributes**: Include context-specific attributes to make traces more useful
4. **Monitor performance impact**: Regularly assess the overhead introduced by instrumentation
5. **Configure appropriate sampling**: Balance observability needs with performance requirements
6. **Use semantic conventions**: Follow OpenTelemetry semantic conventions for consistency
7. **Implement proper error handling**: Capture and record exceptions with appropriate context
8. **Regular maintenance**: Keep OpenTelemetry libraries updated and review configurations periodically

## Frequently Asked Questions

**Does OpenTelemetry work with Django Debug Toolbar?** Yes, OpenTelemetry and Django Debug Toolbar serve different purposes and can coexist in the same application. Django Debug Toolbar is designed for local development debugging, displaying request/response information directly in your browser. OpenTelemetry provides production-ready distributed tracing and monitoring. You typically use Debug Toolbar during development and OpenTelemetry in production environments.

**What's the performance impact of OpenTelemetry instrumentation?** OpenTelemetry is designed to be lightweight with minimal performance overhead. The impact depends on your sampling rate, number of custom spans, and exporter configuration. In typical production deployments with reasonable sampling (10-50%), the overhead is usually less than 5% of request latency. Use batch exporters and appropriate sampling rates to minimize impact.

**Can I use OpenTelemetry with existing Sentry integration?** Yes, OpenTelemetry and Sentry can work together. Sentry focuses on error tracking and crash reporting, while OpenTelemetry provides comprehensive distributed tracing and metrics. You can run both simultaneously - Sentry for error monitoring and OpenTelemetry for performance monitoring and distributed tracing. Some teams use OpenTelemetry's exception recording alongside Sentry for complementary observability.

**Does auto-instrumentation support Django async views?** Yes, OpenTelemetry's Django instrumentation supports async views introduced in Django 3.1+. The `DjangoInstrumentor` automatically detects and instruments both sync and async view functions, creating appropriate spans for asynchronous request handling. Context propagation works correctly across async boundaries.

**How do I instrument Django REST Framework (DRF) endpoints?** Django REST Framework endpoints are automatically instrumented when you use `DjangoInstrumentor().instrument()`. DRF builds on Django's view system, so all HTTP requests to DRF viewsets and API views are traced automatically. For custom span attributes specific to API operations, you can add manual instrumentation within your DRF views to capture serializer validation, permission checks, or business logic timing.

**Can I filter sensitive data from traces?** Yes, you should filter sensitive data before it's exported. Avoid adding sensitive information (passwords, tokens, PII) to span attributes. You can use span processors to filter or redact attributes before export. Configure your application to sanitize request headers, query parameters, and custom attributes that might contain sensitive data.

## What's Next?

By integrating OpenTelemetry with Django, you gain valuable insights into your application's performance, behavior, and dependencies. You can monitor and troubleshoot issues, optimize performance, and ensure the reliability of your Django applications.

The telemetry data collected can help you:

- Identify performance bottlenecks
- Track request flows across services
- Monitor database query performance with [SQLAlchemy instrumentation](/guides/opentelemetry-sqlalchemy)
- Understand user behavior patterns
- Detect and diagnose errors
- Optimize resource utilization
- Improve overall application reliability

For alternative Python frameworks, explore [Flask](/guides/opentelemetry-flask) for lightweight applications or [FastAPI](/guides/opentelemetry-fastapi) for high-performance async APIs.
