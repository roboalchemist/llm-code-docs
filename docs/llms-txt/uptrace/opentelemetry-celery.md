# Source: https://uptrace.dev/raw/guides/opentelemetry-celery.md

# OpenTelemetry Celery Instrumentation Guide

> Complete guide to monitoring Celery applications with OpenTelemetry. Learn task tracing, worker instrumentation, and Uptrace integration for distributed task queues.

OpenTelemetry enables comprehensive monitoring of Celery applications by automatically collecting telemetry data including task execution times, worker performance, queue depths, and error rates. By integrating OpenTelemetry, you can capture distributed traces across your task pipeline and export this data to observability backends for analysis and visualization.

## What is Celery?

Celery is a distributed task queue for Python that allows you to run asynchronous and scheduled tasks. It's built on message passing and can operate with multiple brokers like Redis, RabbitMQ, and Amazon SQS. Celery is commonly used for background processing, periodic tasks, and distributed computing.

Celery consists of several components: producers (clients that send tasks), brokers (message transport), workers (processes that execute tasks), and result backends (stores for task results). This architecture makes it ideal for scaling applications horizontally and handling time-consuming operations without blocking user requests.

## What is OpenTelemetry?

OpenTelemetry is an open-source observability framework that aims to standardize and simplify the collection, processing, and export of [telemetry data](/opentelemetry/distributed-tracing) from applications and systems.

OpenTelemetry supports multiple programming languages and platforms, making it suitable for a wide range of applications and environments. For detailed Python instrumentation, see the [OpenTelemetry Python guide](/get/opentelemetry-python).

OpenTelemetry enables developers to instrument their code and collect telemetry data, which can then be exported to various [OpenTelemetry backends](/blog/opentelemetry-backend) or observability platforms for analysis and visualization. Using the [OpenTelemetry Collector](/opentelemetry/collector), you can centralize telemetry data collection, perform data transformations, and route data to multiple observability backends simultaneously.

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Python zero-code instrumentation guide](/get/opentelemetry-python/zero-code).

</alert>

## Installation

To instrument a Celery application with OpenTelemetry, install the required packages:

```shell
pip install opentelemetry-api opentelemetry-sdk opentelemetry-instrumentation-celery
```

### Additional Instrumentation

Depending on your broker and result backend, you may also want to install additional instrumentation:

```shell
# For Redis broker/backend
pip install opentelemetry-instrumentation-redis

# For RabbitMQ (if using kombu)
pip install opentelemetry-instrumentation-kombu

# For database result backends
pip install opentelemetry-instrumentation-psycopg2  # PostgreSQL
pip install opentelemetry-instrumentation-sqlite3   # SQLite
```

### Exporter Installation

To export telemetry data to observability backends, install an appropriate exporter:

```shell
# For OTLP (recommended)
pip install opentelemetry-exporter-otlp

# For console output (development/testing)
pip install opentelemetry-exporter-otlp-proto-http
```

## Basic Instrumentation

### Automatic Instrumentation

The simplest way to instrument Celery is using the worker process initialization hook. This ensures proper initialization in Celery's prefork worker model:

```python
from celery import Celery
from celery.signals import worker_process_init
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create Celery app first
app = Celery('tasks', broker='redis://localhost:6379/0')

@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    """Initialize OpenTelemetry in each worker process"""

    # Configure OpenTelemetry
    resource = Resource(attributes={
        SERVICE_NAME: "celery-worker"
    })

    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Instrument Celery
    CeleryInstrumentor().instrument()

@app.task
def add(x, y):
    return x + y
```

### Manual Instrumentation

For more control over tracing, you can manually instrument specific tasks:

```python
from celery import Celery
from celery.signals import worker_process_init
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create Celery app first
app = Celery('tasks', broker='redis://localhost:6379/0')

@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    """Initialize OpenTelemetry in each worker process"""
    resource = Resource(attributes={SERVICE_NAME: "celery-worker"})
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Instrument Celery
    CeleryInstrumentor().instrument()

# Get tracer after initialization
tracer = trace.get_tracer(__name__)

@app.task
def process_data(data_id):
    with tracer.start_as_current_span("process_data") as span:
        # Add custom attributes
        span.set_attribute("data.id", data_id)
        span.set_attribute("worker.name", "data_processor")

        # Your task logic here
        result = expensive_computation(data_id)

        # Record result information
        span.set_attribute("result.size", len(result))
        span.set_attribute("task.status", "completed")

        return result
```

## Worker Configuration

### Worker Startup with Instrumentation

Create a worker startup script that initializes OpenTelemetry properly:

```python
# worker.py
import os
from celery import Celery
from celery.signals import worker_process_init
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

@worker_process_init.connect(weak=False)
def initialize_tracing(*args, **kwargs):
    """Initialize OpenTelemetry tracing for Celery worker"""

    # Create resource with worker information
    resource = Resource(attributes={
        SERVICE_NAME: "celery-worker",
        "service.version": "1.0.0",
        "deployment.environment": os.environ.get("ENVIRONMENT", "development"),
        "worker.hostname": os.environ.get("HOSTNAME", "unknown"),
    })

    # Configure tracer provider
    provider = TracerProvider(resource=resource)

    # Configure OTLP exporter
    otlp_exporter = OTLPSpanExporter(
        endpoint="http://localhost:4317",
        insecure=True,
    )

    processor = BatchSpanProcessor(otlp_exporter)
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Instrument Celery
    CeleryInstrumentor().instrument()

@app.task
def example_task(data):
    # Your task logic here
    return f"Processed: {data}"
```

### Worker Execution

Start the worker with the instrumented configuration:

```shell
# Start worker with instrumentation
celery -A worker worker --loglevel=info

# For production with multiple workers
celery -A worker worker --loglevel=info --concurrency=4
```

## Producer (Client) Instrumentation

Instrument the client code that sends tasks to Celery:

```python
# client.py
from celery import Celery
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Initialize OpenTelemetry for producer
resource = Resource(attributes={
    SERVICE_NAME: "celery-producer"
})

provider = TracerProvider(resource=resource)
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Instrument Celery
CeleryInstrumentor().instrument()

# Create Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

def send_task():
    # This will be traced automatically
    result = app.send_task('tasks.process_data', args=[123])
    return result
```

## Advanced Configuration

### Custom Span Attributes

Add custom attributes to Celery spans for better observability:

```python
from celery import Celery
from celery.signals import worker_process_init
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    """Initialize OpenTelemetry in each worker process"""
    resource = Resource(attributes={SERVICE_NAME: "celery-worker"})
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    def custom_span_processor(span, task):
        """Custom function to add attributes to Celery spans"""

        # Add task-specific attributes
        span.set_attribute("celery.task.queue", task.request.delivery_info.get('routing_key', 'default'))
        span.set_attribute("celery.task.retries", task.request.retries)
        span.set_attribute("celery.task.eta", str(task.request.eta) if task.request.eta else "immediate")

        # Add worker information
        span.set_attribute("celery.worker.hostname", task.request.hostname)

        # Add custom business logic attributes
        if hasattr(task.request, 'correlation_id'):
            span.set_attribute("business.correlation_id", task.request.correlation_id)

    # Configure instrumentation with custom processor
    CeleryInstrumentor().instrument(
        span_name_callback=lambda task: f"celery.task.{task.name}",
        span_processor_callback=custom_span_processor
    )
```

### Error Handling and Exception Tracking

Enhance error tracking in Celery tasks:

```python
from celery import Celery
from celery.signals import worker_process_init
from celery.exceptions import Retry
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    """Initialize OpenTelemetry in each worker process"""
    resource = Resource(attributes={SERVICE_NAME: "celery-worker"})
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    CeleryInstrumentor().instrument()

@app.task(bind=True)
def risky_task(self, data):
    span = trace.get_current_span()

    try:
        # Your task logic here
        result = process_risky_operation(data)

        # Set success attributes
        span.set_attribute("task.result.success", True)
        span.set_attribute("task.result.items_processed", len(result))

        return result

    except RetryableError as e:
        # Handle retryable errors
        span.record_exception(e)
        span.set_attribute("task.retry.attempt", self.request.retries + 1)
        span.set_attribute("task.retry.reason", str(e))

        # Retry with exponential backoff
        raise self.retry(exc=e, countdown=60, max_retries=3)

    except Exception as e:
        # Handle permanent failures
        span.record_exception(e)
        span.set_status(Status(StatusCode.ERROR, str(e)))
        span.set_attribute("task.error.type", type(e).__name__)
        span.set_attribute("task.error.fatal", True)

        raise
```

### Task Result Tracking

Track task results and completion status:

```python
from celery.signals import task_success, task_failure, task_retry
from opentelemetry import trace

@task_success.connect
def task_success_handler(sender=None, result=None, **kwargs):
    """Handle successful task completion"""
    span = trace.get_current_span()
    span.set_attribute("celery.task.status", "success")
    span.set_attribute("celery.task.result.type", type(result).__name__)

@task_failure.connect
def task_failure_handler(sender=None, task_id=None, exception=None, traceback=None, einfo=None, **kwargs):
    """Handle task failures"""
    span = trace.get_current_span()
    span.set_attribute("celery.task.status", "failure")
    span.set_attribute("celery.task.exception", str(exception))
    span.record_exception(exception)

@task_retry.connect
def task_retry_handler(sender=None, task_id=None, reason=None, einfo=None, **kwargs):
    """Handle task retries"""
    span = trace.get_current_span()
    span.set_attribute("celery.task.status", "retry")
    span.set_attribute("celery.task.retry.reason", str(reason))
```

## Broker-Specific Configuration

### Redis Configuration

For Redis broker, add Redis instrumentation:

```python
from celery import Celery
from celery.signals import worker_process_init
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create Celery app with Redis configuration
app = Celery('tasks')
app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    """Initialize OpenTelemetry in each worker process"""
    resource = Resource(attributes={SERVICE_NAME: "celery-worker"})
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Instrument Redis
    RedisInstrumentor().instrument()

    # Instrument Celery
    CeleryInstrumentor().instrument()
```

### RabbitMQ Configuration

For RabbitMQ broker, configure with appropriate instrumentation:

```python
from celery import Celery
from celery.signals import worker_process_init
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Create Celery app with RabbitMQ configuration
app = Celery('tasks')
app.conf.update(
    broker_url='pyamqp://guest@localhost//',
    result_backend='rpc://',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)

@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    """Initialize OpenTelemetry in each worker process"""
    resource = Resource(attributes={SERVICE_NAME: "celery-worker"})
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Instrument Celery (includes kombu instrumentation)
    CeleryInstrumentor().instrument()
```

## Monitoring and Metrics

### Custom Metrics Collection

Collect custom metrics alongside traces:

```python
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

# Configure metrics
metric_reader = PeriodicExportingMetricReader(
    OTLPMetricExporter(endpoint="http://localhost:4317", insecure=True),
    export_interval_millis=30000,
)
metrics.set_meter_provider(MeterProvider(metric_readers=[metric_reader]))

# Create meter and instruments
meter = metrics.get_meter("celery_metrics")
task_duration_histogram = meter.create_histogram(
    "celery.task.duration",
    description="Duration of Celery task execution",
    unit="ms"
)
task_counter = meter.create_counter(
    "celery.tasks.total",
    description="Total number of Celery tasks"
)

@app.task
def monitored_task(data):
    start_time = time.time()

    try:
        # Your task logic
        result = process_data(data)

        # Record metrics
        duration = (time.time() - start_time) * 1000
        task_duration_histogram.record(duration, {"task_name": "monitored_task", "status": "success"})
        task_counter.add(1, {"task_name": "monitored_task", "status": "success"})

        return result

    except Exception as e:
        # Record failure metrics
        duration = (time.time() - start_time) * 1000
        task_duration_histogram.record(duration, {"task_name": "monitored_task", "status": "error"})
        task_counter.add(1, {"task_name": "monitored_task", "status": "error"})
        raise
```

## Production Deployment

### Environment Configuration

Use environment variables for production configuration:

```python
import os
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

def configure_tracing():
    """Configure OpenTelemetry based on environment variables"""

    # OTLP endpoint configuration
    otlp_endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")

    # Service configuration
    service_name = os.environ.get("OTEL_SERVICE_NAME", "celery-worker")
    service_version = os.environ.get("OTEL_SERVICE_VERSION", "1.0.0")
    environment = os.environ.get("DEPLOYMENT_ENVIRONMENT", "production")

    # Resource attributes
    resource = Resource(attributes={
        SERVICE_NAME: service_name,
        "service.version": service_version,
        "deployment.environment": environment,
    })

    # Configure exporter
    exporter = OTLPSpanExporter(endpoint=otlp_endpoint)
    processor = BatchSpanProcessor(exporter)

    provider = TracerProvider(resource=resource)
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
```

### Docker Configuration

Example Dockerfile for containerized Celery workers:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Set OpenTelemetry environment variables
ENV OTEL_SERVICE_NAME=celery-worker
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4317

# Start worker with instrumentation
CMD ["celery", "-A", "worker", "worker", "--loglevel=info"]
```

## What is Uptrace?

Uptrace is a [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues. Compare with other [top APM tools](/tools/top-apm-tools) for task queue monitoring.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## uptrace-python with Celery

For simplified configuration, you can use the uptrace-python wrapper:

### Installation

```shell
pip install uptrace
```

### Configuration

```python
import uptrace
from opentelemetry.instrumentation.celery import CeleryInstrumentor

# Configure OpenTelemetry with Uptrace
uptrace.configure_opentelemetry(
    # Set DSN or use UPTRACE_DSN environment variable
    dsn="<your-uptrace-dsn>",
    service_name="celery-worker",
    service_version="1.0.0",
    deployment_environment="production",
)

# Instrument Celery
CeleryInstrumentor().instrument()

# Your Celery app
from celery import Celery
app = Celery('tasks', broker='redis://localhost:6379/0')
```

### Environment Variables

```shell
# Uptrace configuration
export UPTRACE_DSN="https://<token>@uptrace.dev/<project_id>"

# OpenTelemetry configuration
export OTEL_SERVICE_NAME="celery-worker"
export OTEL_SERVICE_VERSION="1.0.0"

# Start worker
celery -A tasks worker --loglevel=info
```

## Troubleshooting

### Common Issues

1. **Double instrumentation**: Ensure you only call `CeleryInstrumentor().instrument()` once per worker process
2. **Missing broker traces**: Install appropriate broker instrumentation (Redis/RabbitMQ)
3. **Worker startup issues**: Initialize OpenTelemetry using `worker_process_init` hook, not at module level
4. **Span not appearing**: Check that exporters are configured correctly and tracer provider is set
5. **High overhead**: Adjust sampling rates and batch processor settings
6. **Fork-safety issues**: Use worker process initialization hook to avoid sharing connections between processes

### Debug Configuration

Enable debug logging to troubleshoot instrumentation:

```python
import logging

# Enable OpenTelemetry debug logging
logging.getLogger("opentelemetry").setLevel(logging.DEBUG)

# Enable Celery debug logging
logging.getLogger("celery").setLevel(logging.DEBUG)

# Configure root logger
logging.basicConfig(level=logging.DEBUG)
```

### Performance Optimization

Configure appropriate settings for production:

```python
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased

# Configure sampling (sample 10% of traces)
sampler = TraceIdRatioBased(0.1)
provider = TracerProvider(sampler=sampler)

# Optimize batch processor
processor = BatchSpanProcessor(
    exporter,
    max_queue_size=2048,
    schedule_delay_millis=5000,
    max_export_batch_size=512,
)
```

## FAQ

**Why initialize OpenTelemetry in worker_process_init instead of at module level?** Celery's prefork worker model creates child processes that don't inherit the parent's OpenTelemetry state properly. Using `worker_process_init` ensures each worker process has its own correctly initialized tracer provider and exporter connections.

**How do I trace tasks across multiple services?** OpenTelemetry automatically propagates trace context through Celery's message headers. When you instrument both the producer (client) and worker, the task spans are linked together in a single distributed trace.

**Why are my spans not appearing?** Common causes include: not initializing in `worker_process_init`, missing exporter configuration, double instrumentation (calling `instrument()` twice), or network issues reaching the telemetry backend. Enable debug logging to diagnose.

**How do I reduce tracing overhead in production?** Use sampling to trace a percentage of tasks. Configure `TraceIdRatioBased(0.1)` to sample 10% of traces. Also tune the `BatchSpanProcessor` settings for your throughput requirements.

**Can I trace Celery Beat scheduled tasks?** Yes, scheduled tasks are traced like any other task. The span captures when the task was scheduled to run vs when it actually executed.

**How do I correlate logs with traces?** Use OpenTelemetry's logging integration to inject trace and span IDs into your log records. This lets you filter logs by trace ID when investigating issues.

**What's the difference between producer and worker instrumentation?** Producer instrumentation captures when tasks are sent (including routing and serialization). Worker instrumentation captures task execution (including retries and failures). Both are needed for complete visibility.

## What's next?

By integrating OpenTelemetry with Celery, you gain valuable insights into your distributed task processing pipeline. You can monitor task performance, track queue depths, identify bottlenecks, and troubleshoot issues across your asynchronous workflow.

The telemetry data collected helps you:

- Monitor task execution times and success rates
- Track worker performance and resource utilization
- Identify bottlenecks in task processing pipelines
- Debug failed tasks and retry patterns
- Optimize queue management and worker scaling
- Understand task dependencies and data flow
- Improve overall system reliability and performance

Celery is commonly used with web frameworks for handling background tasks. Learn how to instrument your web application with [Django](/guides/opentelemetry-django), [Flask](/guides/opentelemetry-flask), or [FastAPI](/guides/opentelemetry-fastapi) to get end-to-end visibility from HTTP requests through async task execution.
