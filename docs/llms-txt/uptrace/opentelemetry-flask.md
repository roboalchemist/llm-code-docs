# Source: https://uptrace.dev/raw/guides/opentelemetry-flask.md

# OpenTelemetry Flask Instrumentation and Monitoring

> Instrument and monitor Flask applications with OpenTelemetry. Setup FlaskInstrumentor for automatic tracing, SQLAlchemy integration, performance monitoring, and error tracking.

OpenTelemetry Flask instrumentation provides automatic tracing for HTTP requests, database queries, and application performance monitoring. Using FlaskInstrumentor, you can add observability to Flask applications without code changes, enabling distributed tracing, metrics collection, and error tracking across your Python web services.

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
      Flask Instrumentation
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-flask
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
      Logging Integration
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-logging
      </code>
    </td>
    
    <td>
      Correlate logs with traces
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
      Detect and instrument libraries
    </td>
  </tr>
</tbody>
</table>

**Quick Start:**

```python
pip install opentelemetry-instrumentation-flask
from opentelemetry.instrumentation.flask import FlaskInstrumentor
FlaskInstrumentor().instrument_app(app)
```

> **Note on Examples:** This guide uses Uptrace as the OpenTelemetry backend in code examples. However, OpenTelemetry is vendor-neutral and works with any OTLP-compatible backend (Jaeger, Grafana Cloud, Prometheus, etc.). Simply replace the `OTEL_EXPORTER_OTLP_ENDPOINT` and headers with your preferred backend configuration.

## What is OpenTelemetry?

OpenTelemetry is an open-source observability framework that provides a standardized way to collect, process, and export telemetry data from applications. It combines three pillars of observability:

### The Three Pillars of Observability:

1. [Traces](/opentelemetry/distributed-tracing): Track requests as they flow through distributed systems
2. [Metrics](/opentelemetry/metrics): Quantitative measurements of system performance and behavior
3. [Logs](/opentelemetry/logs): Discrete records of events that occurred in your application

### Benefits of OpenTelemetry:

- **Vendor Neutrality**: Works with multiple observability backends
- **Standardization**: Consistent APIs across languages and frameworks
- **Automatic Instrumentation**: Built-in support for popular libraries
- **Custom Instrumentation**: APIs for adding application-specific telemetry
- **Performance**: Designed for minimal overhead in production environments

OpenTelemetry enables developers to instrument their code to gain insights into application performance, behavior, and dependencies across distributed systems, making it easier to debug issues, optimize performance, and understand system behavior.

## Prerequisites and Installation

### System Requirements

- Python 3.7 or higher
- pip package manager
- A Flask application (existing or new)

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Python zero-code instrumentation guide](/get/opentelemetry-python/zero-code).

</alert>

### Core Dependencies

Install the essential OpenTelemetry packages for Flask. For comprehensive Python instrumentation, see the [OpenTelemetry Python guide](/get/opentelemetry-python).

```shell
# Core OpenTelemetry packages
pip install opentelemetry-api opentelemetry-sdk

# Flask-specific instrumentation
pip install opentelemetry-instrumentation-flask

# Optional: Auto-instrumentation for common libraries
pip install opentelemetry-bootstrap opentelemetry-instrumentation
```

### Optional Dependencies

Depending on your needs, you might also want:

```shell
# For database instrumentation
pip install opentelemetry-instrumentation-sqlalchemy
pip install opentelemetry-instrumentation-psycopg2  # PostgreSQL
pip install opentelemetry-instrumentation-pymongo  # MongoDB

# For HTTP client instrumentation
pip install opentelemetry-instrumentation-requests
pip install opentelemetry-instrumentation-urllib3

# For different exporters
pip install opentelemetry-exporter-jaeger
pip install opentelemetry-exporter-otlp
pip install opentelemetry-exporter-prometheus
```

### Verification

You can verify your installation by running:

```python
import opentelemetry
print(f"OpenTelemetry version: {opentelemetry.__version__}")
```

## Basic Setup

### OpenTelemetry SDK Initialization

Create a dedicated configuration module for OpenTelemetry setup. This approach keeps your instrumentation code organized and reusable.

Create a file called `telemetry.py`:

```python
"""
OpenTelemetry configuration for Flask application.
This module handles the initialization of tracing, metrics, and exporters.
"""

import os
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME, SERVICE_VERSION

def configure_opentelemetry(service_name: str = "flask-app", service_version: str = "1.0.0"):
    """
    Configure OpenTelemetry with proper resource attributes and exporters.

    Args:
        service_name: Name of your service
        service_version: Version of your service
    """

    # Create resource with service information
    resource = Resource.create({
        SERVICE_NAME: service_name,
        SERVICE_VERSION: service_version,
        "environment": os.getenv("ENVIRONMENT", "development"),
        "team": os.getenv("TEAM", "backend"),
    })

    # Configure tracing
    trace_provider = TracerProvider(resource=resource)

    # Choose exporter based on environment
    if os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT"):
        # Production: Use OTLP exporter
        otlp_exporter = OTLPSpanExporter(
            endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT"),
            headers={"Authorization": f"Bearer {os.getenv('OTEL_API_KEY', '')}"}
        )
        trace_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
    else:
        # Development: Use console exporter
        console_exporter = ConsoleSpanExporter()
        trace_provider.add_span_processor(BatchSpanProcessor(console_exporter))

    # Set the global tracer provider
    trace.set_tracer_provider(trace_provider)

    # Configure metrics (optional)
    metrics.set_meter_provider(MeterProvider(resource=resource))

    return trace.get_tracer(__name__)

# Initialize tracer
tracer = configure_opentelemetry()
```

### Basic Flask Application Setup

Now integrate OpenTelemetry with your Flask application:

```python
# app.py
from flask import Flask, request, jsonify
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from telemetry import configure_opentelemetry

# Initialize OpenTelemetry before creating Flask app
tracer = configure_opentelemetry(
    service_name="my-flask-api",
    service_version="1.0.0"
)

# Create Flask application
app = Flask(__name__)

# Instrument the Flask app
FlaskInstrumentor().instrument_app(app)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!", "status": "healthy"})

@app.route('/health')
def health_check():
    return jsonify({"status": "ok", "service": "my-flask-api"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Flask Instrumentation

### Automatic Instrumentation

OpenTelemetry provides automatic instrumentation for Flask applications, which captures HTTP requests, responses, and basic metadata without requiring code changes.

#### Basic Instrumentation

```python
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Simple instrumentation
FlaskInstrumentor().instrument_app(app)
```

#### Advanced Configuration Options

```python
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Configure with custom options
FlaskInstrumentor().instrument_app(
    app,
    # Add SQL comment context to database queries
    enable_commenter=True,
    commenter_options={
        "opentelemetry_values": True,  # Include OpenTelemetry trace context
    },
    # Exclude certain routes from tracing
    excluded_urls="health,metrics,favicon.ico",
    # Custom request hook for adding attributes
    request_hook=request_hook_function,
    # Custom response hook for adding attributes
    response_hook=response_hook_function,
)
```

#### Custom Hook Functions

```python
def request_hook_function(span, environ):
    """Add custom attributes to request spans."""
    if span and span.is_recording():
        # Add user information if available
        user_id = environ.get('HTTP_X_USER_ID')
        if user_id:
            span.set_attribute("user.id", user_id)

        # Add API version
        api_version = environ.get('HTTP_X_API_VERSION', 'v1')
        span.set_attribute("api.version", api_version)

def response_hook_function(span, status, response_headers):
    """Add custom attributes based on response."""
    if span and span.is_recording():
        # Add response size
        content_length = next(
            (value for key, value in response_headers if key.lower() == 'content-length'),
            None
        )
        if content_length:
            span.set_attribute("http.response.size", int(content_length))
```

### Auto-Instrumentation with Bootstrap

For a more comprehensive setup, you can use auto-instrumentation to automatically detect and instrument common libraries:

```shell
# Install auto-instrumentation
pip install opentelemetry-bootstrap opentelemetry-instrumentation

# Bootstrap (detects installed libraries)
opentelemetry-bootstrap -a install

# Run your application with auto-instrumentation
opentelemetry-instrument --traces_exporter console --metrics_exporter console python app.py
```

## Advanced Configuration

### Environment Variables Configuration

OpenTelemetry supports configuration through environment variables:

```bash
# Service identification
export OTEL_SERVICE_NAME="my-flask-api"
export OTEL_SERVICE_VERSION="1.2.0"
export OTEL_RESOURCE_ATTRIBUTES="environment=production,team=backend"

# Exporters
export OTEL_TRACES_EXPORTER="otlp"
export OTEL_METRICS_EXPORTER="prometheus"
export OTEL_LOGS_EXPORTER="console"

# OTLP Endpoint
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.uptrace.dev"
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=YOUR_DSN"

# Sampling
export OTEL_TRACES_SAMPLER="traceidratio"
export OTEL_TRACES_SAMPLER_ARG="0.1"  # Sample 10% of traces
```

### Custom Sampling Strategies

```python
from opentelemetry.sdk.trace.sampling import (
    TraceIdRatioBasedSampler,
    ParentBasedSampler,
    NEVER_SAMPLE,
    ALWAYS_SAMPLE
)

# Custom sampler that samples based on route
class RouteBasedSampler:
    def __init__(self, high_volume_routes=None, sample_rate=0.01):
        self.high_volume_routes = high_volume_routes or ['/health', '/metrics']
        self.low_sample = TraceIdRatioBasedSampler(sample_rate)
        self.high_sample = TraceIdRatioBasedSampler(1.0)

    def should_sample(self, parent_context, trace_id, name, kind, attributes, links, trace_state):
        # Sample health checks and metrics at lower rate
        if any(route in name for route in self.high_volume_routes):
            return self.low_sample.should_sample(
                parent_context, trace_id, name, kind, attributes, links, trace_state
            )
        return self.high_sample.should_sample(
            parent_context, trace_id, name, kind, attributes, links, trace_state
        )

# Use custom sampler
trace_provider = TracerProvider(
    sampler=RouteBasedSampler(),
    resource=resource
)
```

### Resource Detection

Automatically detect and include resource information:

```python
from opentelemetry.sdk.resources import Resource
from opentelemetry.resourcedetector.aws_ec2 import AwsEc2ResourceDetector
from opentelemetry.resourcedetector.process import ProcessResourceDetector

# Automatically detect resource attributes
resource = Resource.create().merge(
    AwsEc2ResourceDetector().detect()  # AWS EC2 metadata
).merge(
    ProcessResourceDetector().detect()  # Process information
)
```

## Custom Instrumentation

### Manual Span Creation

Add custom spans to trace specific business logic:

```python
from flask import Flask, request
from opentelemetry import trace

app = Flask(__name__)
tracer = trace.get_tracer(__name__)

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    # Create a custom span for the entire operation
    with tracer.start_as_current_span("get_user_operation") as span:
        # Add attributes to the span
        span.set_attribute("user.id", user_id)
        span.set_attribute("operation.type", "read")

        try:
            # Simulate user validation
            with tracer.start_as_current_span("validate_user_permissions"):
                if not validate_user_permissions(user_id):
                    span.set_attribute("error", True)
                    span.set_attribute("error.type", "permission_denied")
                    return jsonify({"error": "Access denied"}), 403

            # Simulate database query
            with tracer.start_as_current_span("database_query") as db_span:
                db_span.set_attribute("db.operation", "SELECT")
                db_span.set_attribute("db.table", "users")
                user_data = fetch_user_from_database(user_id)
                db_span.set_attribute("db.rows_affected", 1 if user_data else 0)

            # Process user data
            with tracer.start_as_current_span("process_user_data"):
                processed_user = process_user_data(user_data)

            span.set_attribute("operation.success", True)
            return jsonify(processed_user)

        except Exception as e:
            # Record the exception in the span
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            span.set_attribute("error", True)
            span.set_attribute("error.type", type(e).__name__)
            return jsonify({"error": "Internal server error"}), 500

def validate_user_permissions(user_id):
    """Simulate permission validation."""
    # Add custom logic here
    return user_id > 0

def fetch_user_from_database(user_id):
    """Simulate database fetch."""
    return {"id": user_id, "name": f"User {user_id}", "email": f"user{user_id}@example.com"}

def process_user_data(user_data):
    """Simulate data processing."""
    if user_data:
        return {
            "id": user_data["id"],
            "name": user_data["name"],
            "email": user_data["email"],
            "processed_at": "2024-01-15T10:30:00Z"
        }
    return None
```

### Decorators for Automatic Tracing

Create reusable decorators for common patterns:

```python
import functools
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def trace_function(name=None, attributes=None):
    """Decorator to automatically trace function calls."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            span_name = name or f"{func.__module__}.{func.__name__}"
            with tracer.start_as_current_span(span_name) as span:
                # Add default attributes
                span.set_attribute("function.name", func.__name__)
                span.set_attribute("function.module", func.__module__)

                # Add custom attributes
                if attributes:
                    for key, value in attributes.items():
                        span.set_attribute(key, value)

                try:
                    result = func(*args, **kwargs)
                    span.set_attribute("function.success", True)
                    return result
                except Exception as e:
                    span.record_exception(e)
                    span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
                    raise
        return wrapper
    return decorator

# Usage example
@trace_function(name="business_logic.calculate_total", attributes={"operation.type": "calculation"})
def calculate_order_total(items):
    """Calculate the total price of order items."""
    total = sum(item.get('price', 0) * item.get('quantity', 0) for item in items)
    return total

@app.route('/api/orders/total', methods=['POST'])
def calculate_total():
    items = request.json.get('items', [])
    total = calculate_order_total(items)
    return jsonify({"total": total})
```

### Adding Context and Baggage

Use OpenTelemetry context and baggage to pass information across service boundaries:

```python
from opentelemetry import baggage, context
from opentelemetry.trace import set_span_in_context

@app.route('/api/orders', methods=['POST'])
def create_order():
    # Set baggage for cross-service context
    ctx = baggage.set_baggage("user.id", request.headers.get("X-User-ID", "anonymous"))
    ctx = baggage.set_baggage("request.id", request.headers.get("X-Request-ID", "unknown"), ctx)

    with tracer.start_as_current_span("create_order") as span:
        # Get baggage values
        user_id = baggage.get_baggage("user.id", ctx)
        request_id = baggage.get_baggage("request.id", ctx)

        span.set_attribute("user.id", user_id)
        span.set_attribute("request.id", request_id)

        # Process order...
        return jsonify({"status": "created", "user_id": user_id})
```

## Database Instrumentation

### SQLAlchemy Integration

Comprehensive SQLAlchemy instrumentation setup:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from sqlalchemy import event

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost/mydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Instrument SQLAlchemy with detailed configuration
SQLAlchemyInstrumentor().instrument(
    engine=db.engine,
    # Enable SQL commenter to add trace context to SQL queries
    enable_commenter=True,
    commenter_options={
        "opentelemetry_values": True,
    },
)

# Optional: Add custom database event listeners
@event.listens_for(db.engine, "before_cursor_execute")
def receive_before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    """Add custom logic before SQL execution."""
    current_span = trace.get_current_span()
    if current_span:
        current_span.add_event("sql.before_execute", {"statement": statement})

@event.listens_for(db.engine, "after_cursor_execute")
def receive_after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    """Add custom logic after SQL execution."""
    current_span = trace.get_current_span()
    if current_span:
        current_span.add_event("sql.after_execute", {"rowcount": cursor.rowcount})

# Example model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

@app.route('/api/users')
def get_users():
    # This query will be automatically traced
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
```

### Multiple Database Support

```python
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
from opentelemetry.instrumentation.pymongo import PyMongoInstrumentor

# PostgreSQL with psycopg2
Psycopg2Instrumentor().instrument()

# MongoDB
PyMongoInstrumentor().instrument()

# Multiple SQLAlchemy engines
main_engine = create_engine("postgresql://...")
analytics_engine = create_engine("postgresql://...")

SQLAlchemyInstrumentor().instrument(
    engine=main_engine,
    service="user-service-main-db"
)

SQLAlchemyInstrumentor().instrument(
    engine=analytics_engine,
    service="user-service-analytics-db"
)
```

## Analyzing Observability Data

### Key Metrics to Monitor

1. **Request Metrics**:
  - Request rate (requests per second)
  - Response time percentiles (p50, p95, p99)
  - Error rate percentage
  - Request size distribution
2. **Database Metrics**:
  - Query execution time
  - Connection pool usage
  - Database errors and timeouts
  - Slow query identification
3. **System Metrics**:
  - CPU and memory usage
  - Garbage collection frequency
  - Thread pool utilization

### Custom Metrics Collection

```python
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader

# Configure metrics
metric_reader = PeriodicExportingMetricReader(
    ConsoleMetricExporter(),
    export_interval_millis=5000,
)
metrics.set_meter_provider(MeterProvider(metric_readers=[metric_reader]))

# Create meter and instruments
meter = metrics.get_meter(__name__)

# Counter for API requests
request_counter = meter.create_counter(
    name="api_requests_total",
    description="Total API requests",
    unit="1",
)

# Histogram for request duration
request_duration = meter.create_histogram(
    name="api_request_duration_seconds",
    description="API request duration",
    unit="s",
)

# Gauge for active connections
active_connections = meter.create_up_down_counter(
    name="active_connections",
    description="Number of active database connections",
    unit="1",
)

@app.before_request
def before_request():
    """Record metrics before processing request."""
    request.start_time = time.time()
    request_counter.add(1, {"method": request.method, "endpoint": request.endpoint})

@app.after_request
def after_request(response):
    """Record metrics after processing request."""
    if hasattr(request, 'start_time'):
        duration = time.time() - request.start_time
        request_duration.record(
            duration,
            {
                "method": request.method,
                "status_code": str(response.status_code),
                "endpoint": request.endpoint or "unknown"
            }
        )
    return response
```

## Troubleshooting

### Common Issues and Solutions

1. **No Traces Appearing**:

```python
# Debug configuration
import os
os.environ["OTEL_LOG_LEVEL"] = "DEBUG"

# Check if tracer is properly initialized
tracer = trace.get_tracer(__name__)
print(f"Tracer: {tracer}")
print(f"Tracer provider: {trace.get_tracer_provider()}")

# Verify span creation
with tracer.start_as_current_span("test-span") as span:
    print(f"Span context: {span.get_span_context()}")
    span.set_attribute("test", "value")
```

1. **High Memory Usage**:

```python
# Configure batch processor with memory limits
from opentelemetry.sdk.trace.export import BatchSpanProcessor

processor = BatchSpanProcessor(
    exporter,
    max_queue_size=512,         # Reduce queue size
    export_timeout_millis=5000, # Faster exports
    schedule_delay_millis=1000, # More frequent exports
    max_export_batch_size=128   # Smaller batches
)
```

1. **Performance Issues**:

```python
# Profile instrumentation overhead
import time

def profile_instrumentation():
    """Profile the overhead of instrumentation."""

    # Test without instrumentation
    start = time.time()
    for _ in range(1000):
        # Simulate work
        pass
    baseline = time.time() - start

    # Test with instrumentation
    start = time.time()
    for _ in range(1000):
        with tracer.start_as_current_span("test"):
            # Simulate work
            pass
    instrumented = time.time() - start

    overhead = ((instrumented - baseline) / baseline) * 100
    print(f"Instrumentation overhead: {overhead:.2f}%")

# Run profiling
if __name__ == "__main__":
    profile_instrumentation()
```

### Debugging Tools

```python
# Custom debug middleware
class DebugTelemetryMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        def debug_start_response(status, headers, exc_info=None):
            current_span = trace.get_current_span()
            if current_span and current_span.is_recording():
                print(f"Span ID: {current_span.get_span_context().span_id}")
                print(f"Trace ID: {current_span.get_span_context().trace_id}")
                print(f"Status: {status}")
            return start_response(status, headers, exc_info)

        return self.app(environ, debug_start_response)

# Use in development
if app.config.get('DEBUG'):
    app.wsgi_app = DebugTelemetryMiddleware(app.wsgi_app)
```

## How to Host Flask App with Built-in Monitoring?

Deploy your Flask application with integrated OpenTelemetry monitoring using production-ready WSGI servers.

### Using Gunicorn

Gunicorn is the recommended WSGI server for production Flask deployments:

```bash
# Install Gunicorn
pip install gunicorn

# Run with OpenTelemetry instrumentation
gunicorn -w 4 -b 0.0.0.0:8000 \
  --access-logfile - \
  --error-logfile - \
  --log-level info \
  app:app
```

OpenTelemetry automatically instruments Gunicorn workers when FlaskInstrumentor is configured in your application.

### Using Docker

Deploy Flask with OpenTelemetry in a Docker container:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

**requirements.txt:**

```txt
flask>=3.0.0
gunicorn>=21.0.0
opentelemetry-api
opentelemetry-sdk
opentelemetry-instrumentation-flask
opentelemetry-instrumentation-sqlalchemy
opentelemetry-exporter-otlp
```

Build and run:

```bash
docker build -t flask-otel-app .
docker run -p 8000:8000 \
  -e OTEL_SERVICE_NAME="flask-app" \
  -e OTEL_EXPORTER_OTLP_ENDPOINT="https://api.uptrace.dev" \
  -e OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=YOUR_DSN" \
  flask-otel-app
```

### Using Docker Compose

For multi-service deployments with monitoring:

```yaml
version: '3.8'

services:
  flask-app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OTEL_SERVICE_NAME=flask-app
      - OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev
      - OTEL_EXPORTER_OTLP_HEADERS=uptrace-dsn=${UPTRACE_DSN}
      - DATABASE_URL=postgresql://user:password@postgres:5432/dbname
    depends_on:
      - postgres

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Run with:

```bash
export UPTRACE_DSN="your_dsn_here"
docker-compose up -d
```

### Cloud Platforms

**AWS Elastic Beanstalk:**

Create `.ebextensions/python.config`:

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
  aws:elasticbeanstalk:application:environment:
    OTEL_SERVICE_NAME: flask-app-production
    OTEL_EXPORTER_OTLP_ENDPOINT: https://api.uptrace.dev
```

**Google Cloud Run:**

Deploy with automatic OpenTelemetry instrumentation:

```bash
gcloud run deploy flask-app \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars OTEL_SERVICE_NAME=flask-app,OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev
```

All deployments automatically include OpenTelemetry monitoring when FlaskInstrumentor is initialized in your application code.

## Best Practices

### Performance Optimization

1. **Sampling Strategy**: Use appropriate sampling rates for different environments:

```python
# Production sampling configuration
SAMPLING_RATES = {
    "production": 0.01,    # 1% sampling
    "staging": 0.1,        # 10% sampling
    "development": 1.0,    # 100% sampling
}

environment = os.getenv("ENVIRONMENT", "development")
sampling_rate = SAMPLING_RATES.get(environment, 1.0)

tracer_provider = TracerProvider(
    sampler=TraceIdRatioBasedSampler(sampling_rate)
)
```

1. **Attribute Guidelines**:

```python
# Good: Structured, consistent attributes
span.set_attributes({
    "user.id": user_id,
    "user.role": user_role,
    "operation.type": "database_query",
    "database.table": "users",
    "database.operation": "SELECT"
})

# Avoid: High-cardinality attributes
# span.set_attribute("sql.query", full_sql_query)  # Can cause memory issues
# span.set_attribute("user.session_id", session_id)  # Too many unique values
```

1. **Span Lifecycle Management**:

```python
def process_with_proper_span_management():
    with tracer.start_as_current_span("main_operation") as main_span:
        try:
            # Child spans are automatically linked to parent
            with tracer.start_as_current_span("sub_operation_1"):
                result1 = do_something()

            with tracer.start_as_current_span("sub_operation_2"):
                result2 = do_something_else()

            main_span.set_attribute("operation.success", True)
            return combine_results(result1, result2)

        except Exception as e:
            main_span.record_exception(e)
            main_span.set_status(trace.Status(trace.StatusCode.ERROR))
            raise
```

### Security Considerations

1. **Sensitive Data Filtering**:

```python
import re

SENSITIVE_PATTERNS = [
    re.compile(r'password', re.IGNORECASE),
    re.compile(r'token', re.IGNORECASE),
    re.compile(r'secret', re.IGNORECASE),
    re.compile(r'key', re.IGNORECASE),
]

def sanitize_attributes(attributes):
    """Remove sensitive data from span attributes."""
    sanitized = {}
    for key, value in attributes.items():
        if any(pattern.search(key) for pattern in SENSITIVE_PATTERNS):
            sanitized[key] = "[REDACTED]"
        else:
            sanitized[key] = value
    return sanitized

# Use in custom instrumentation
def secure_span_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with tracer.start_as_current_span(func.__name__) as span:
            # Sanitize function arguments before adding as attributes
            safe_attrs = sanitize_attributes(kwargs)
            for key, value in safe_attrs.items():
                span.set_attribute(f"function.arg.{key}", str(value))

            return func(*args, **kwargs)
    return wrapper
```

1. **Network Security**:

```python
# Use TLS for OTLP exports
otlp_exporter = OTLPSpanExporter(
    endpoint="https://secure-collector.example.com",
    headers={
        "Authorization": f"Bearer {os.getenv('OTEL_API_KEY')}",
        "X-API-Version": "v1"
    },
    insecure=False,  # Ensure TLS is used
)
```

### Error Handling and Monitoring

```python
import logging
from opentelemetry.instrumentation.logging import LoggingInstrumentor

# Configure logging instrumentation
LoggingInstrumentor().instrument(set_logging_format=True)

# Create logger
logger = logging.getLogger(__name__)

@app.errorhandler(500)
def handle_internal_error(error):
    """Custom error handler with tracing."""
    current_span = trace.get_current_span()
    if current_span:
        current_span.set_attribute("error", True)
        current_span.set_attribute("error.type", "internal_server_error")
        current_span.record_exception(error)
        current_span.set_status(trace.Status(trace.StatusCode.ERROR, "Internal server error"))

    logger.error(f"Internal server error: {str(error)}", exc_info=True)
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def handle_not_found(error):
    """Handle 404 errors with tracing."""
    current_span = trace.get_current_span()
    if current_span:
        current_span.set_attribute("http.status_code", 404)
        current_span.set_attribute("error.type", "not_found")

    return jsonify({"error": "Resource not found"}), 404
```

## FAQ

### General Questions

1. **What's the performance impact of OpenTelemetry instrumentation?** OpenTelemetry is designed to have minimal performance impact, typically adding less than 5% overhead in production environments. The actual impact depends on:

- Sampling rate (lower rates = less overhead)
- Number of custom spans created
- Attribute complexity and cardinality
- Export frequency and batch sizes

1. **Can I use OpenTelemetry with existing monitoring solutions?** Yes! OpenTelemetry supports multiple exporters simultaneously. You can export traces to Jaeger, metrics to Prometheus, and logs to your existing centralized logging system all at once.
2. **How do I handle sensitive data in traces?** Use attribute sanitization, avoid logging sensitive request/response bodies, and consider using OpenTelemetry's sampling and filtering capabilities. Always review what data is being collected before deploying to production.
3. **Why are my traces not appearing in my observability backend?**

Common causes include:

1. Incorrect exporter configuration
2. Network connectivity issues
3. Authentication problems
4. Sampling configuration excluding your traces
5. Service name mismatches

Use console exporter for debugging and verify your configuration step by step.

1. **How do I trace across different Flask blueprints?** OpenTelemetry Flask instrumentation automatically works across blueprints. Each route in any blueprint will be traced individually. You can add custom spans within blueprint handlers just like regular routes.
2. **Can I disable instrumentation for specific routes?**

Yes, use the `excluded_urls` parameter:

```python
FlaskInstrumentor().instrument_app(
    app,
    excluded_urls="health,metrics,static/*"  # Exclude multiple patterns
)
```

1. **How do I correlate logs with traces?**

Use OpenTelemetry's logging instrumentation:

```python
from opentelemetry.instrumentation.logging import LoggingInstrumentor

LoggingInstrumentor().instrument(set_logging_format=True)
```

This automatically adds trace and span IDs to log records.

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues. Compare with other [top APM tools](/tools/top-apm-tools) for your Flask applications.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's Next?

### Explore More Examples

- **Flask Basic Example** - Simple Flask application with OpenTelemetry
- **Flask Auto-instrumentation** - Using automatic instrumentation
- **Flask and Gunicorn** - Production deployment with Gunicorn
- **Flask and uWSGI** - Alternative WSGI server setup

### Related Guides

- [OpenTelemetry Python Tracing API](/get/opentelemetry-python/tracing) - Deep dive into the tracing API
- [Instrumenting SQLAlchemy with OpenTelemetry](/guides/opentelemetry-sqlalchemy) - Database instrumentation guide
- [OpenTelemetry Backends Comparison](/blog/opentelemetry-backend) - Choosing the right observability platform

Ready to implement observability in your Flask application? Start with the basic setup and gradually add more advanced features as your monitoring needs evolve.
