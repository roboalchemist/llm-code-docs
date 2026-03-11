# Source: https://uptrace.dev/raw/get/opentelemetry-python.md

# OpenTelemetry Python distro for Uptrace

> Step-by-step guide to install and configure OpenTelemetry Python SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/python-original.svg)This document explains how to configure the OpenTelemetry Python SDK to export spans (traces), logs, and metrics to Uptrace using OTLP/HTTP.

## Choose Your Setup Path

### Option A: Quick Start with uptrace-python

Best for: Getting started quickly, automatic configuration

[uptrace-python](https://github.com/uptrace/uptrace-python) is a thin wrapper over [opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python) that configures the OpenTelemetry SDK to export data to Uptrace. It does not add any new functionality and is provided only for your convenience.

> [Continue below](#quick-start)

### Option B: Direct OTLP Configuration

Best for: Existing OpenTelemetry users, custom exporters, fine-grained control

> [Direct OTLP Setup](/get/opentelemetry-python/otlp)

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install uptrace-python

```shell
pip install uptrace
```

### Step 3: Basic Configuration

You can configure the Uptrace client using a [DSN](/get#dsn) (Data Source Name) from the project settings page. Replace `<FIXME>` with your actual Uptrace DSN, and `myservice` with a name that identifies your application.

```python
import uptrace
from opentelemetry import trace

uptrace.configure_opentelemetry(
    # copy your project DSN here or use UPTRACE_DSN env var
    # dsn="<FIXME>",

    service_name="myservice",
    service_version="v1.0.0",
    deployment_environment="production",
)
```

### Step 4: Create Your First Trace

Copy the [code](https://github.com/uptrace/uptrace-python/tree/master/example/basic) to `main.py`:

```python
#!/usr/bin/env python3

import uptrace
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

# Configure OpenTelemetry with sensible defaults.
uptrace.configure_opentelemetry(
    # copy your project DSN here or use UPTRACE_DSN env var
    # dsn="<FIXME>",

    service_name="myservice",
    service_version="1.0.0",
)

# Create a tracer. Usually, tracer is a global variable.
tracer = trace.get_tracer("app_or_package_name", "1.0.0")

# Create a root span (a trace) to measure some operation.
with tracer.start_as_current_span("main-operation") as main:
    # The context manager handles ending the span automatically.

    # Create a child span for an HTTP operation.
    with tracer.start_as_current_span("GET /posts/:id") as child1:
        child1.set_attributes({
            "http.method": "GET",
            "http.route": "/posts/:id",
            "http.url": "http://localhost:8080/posts/123",
            "http.status_code": 200,
        })
        # Record an error
        try:
            raise ValueError("dummy error")
        except Exception as exc:
            child1.record_exception(exc)
            child1.set_status(Status(StatusCode.ERROR, str(exc)))

    # Create a child span for a database operation.
    with tracer.start_as_current_span("SELECT") as child2:
        child2.set_attributes({
            "db.system": "mysql",
            "db.statement": "SELECT * FROM posts LIMIT 100",
        })

    print(f"trace: {uptrace.trace_url(main)}")

# Send buffered spans and free resources.
uptrace.shutdown()
```

### Step 5: Run Your Application

Run the code, replacing `<FIXME>` with your Uptrace DSN:

```shell
$ UPTRACE_DSN="<FIXME>" python main.py
trace: https://app.uptrace.dev/traces/<trace_id>
```

### Step 6: View Your Trace

Follow the link to view the trace:

![Basic trace](/get/basic-trace.png)

## Configuration Options

You can find the full list of available options at [PyPI](https://pypi.org/project/uptrace/).

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
      A data source that specifies Uptrace project credentials. For example, <code>
        https://<secret>@api.uptrace.dev?grpc=4317
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service_name
      </code>
    </td>
    
    <td>
      <code>
        service.name
      </code>
      
       resource attribute. For example, <code>
        myservice
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service_version
      </code>
    </td>
    
    <td>
      <code>
        service.version
      </code>
      
       resource attribute. For example, <code>
        1.0.0
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        deployment_environment
      </code>
    </td>
    
    <td>
      <code>
        deployment.environment
      </code>
      
       resource attribute. For example, <code>
        production
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resource_attributes
      </code>
    </td>
    
    <td>
      Any other resource attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resource
      </code>
    </td>
    
    <td>
      Resource attributes representing an entity that produces telemetry.
    </td>
  </tr>
</tbody>
</table>

## Application Servers

The `BatchSpanProcessor` spawns a background thread to export spans. This doesn't work well with application servers like Gunicorn and uWSGI that use a pre-forking model. During the fork, the child process inherits locks from the parent process, causing deadlocks.

To resolve this issue, configure OpenTelemetry using post-fork hooks:

### Gunicorn

Use the [post_fork](https://docs.gunicorn.org/en/stable/settings.html#post-fork) hook:

```python
# gunicorn.conf.py
import uptrace

def post_fork(server, worker):
    uptrace.configure_opentelemetry(
        service_name="myservice",
        service_version="1.0.0",
    )
```

### uWSGI

Use the [postfork](https://uwsgi-docs.readthedocs.io/en/latest/PythonDecorators.html#uwsgidecorators.postfork) decorator:

```python
from uwsgidecorators import postfork
import uptrace

@postfork
def init_tracing():
    uptrace.configure_opentelemetry(
        service_name="myservice",
        service_version="1.0.0",
    )
```

## What's Next?

Instrument more operations to get a detailed picture of your application. Prioritize network calls, database queries, errors, and logs.

### By Use Case

<table>
<thead>
  <tr>
    <th>
      I want to...
    </th>
    
    <th>
      Read this
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Instrument without code changes
    </td>
    
    <td>
      <a href="/get/opentelemetry-python/zero-code">
        Zero-code instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-python/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-python/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-python/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-python/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-python/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-python/resources">
        Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry Django](/guides/opentelemetry-django)
- [OpenTelemetry Flask](/guides/opentelemetry-flask)
- [OpenTelemetry FastAPI](/guides/opentelemetry-fastapi)
