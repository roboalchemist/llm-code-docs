# Source: https://uptrace.dev/raw/get/opentelemetry-php.md

# OpenTelemetry PHP distro for Uptrace

> Step-by-step guide to install and configure OpenTelemetry PHP SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/php-original.svg)This document explains how to configure the OpenTelemetry PHP SDK to export spans (traces), logs, and metrics to Uptrace using OTLP/HTTP.

## Choose Your Setup Path

### Option A: Quick Start with uptrace-php

Best for: Getting started quickly, automatic configuration

[uptrace-php](https://github.com/uptrace/uptrace-php) is a thin wrapper over [opentelemetry-php](https://github.com/open-telemetry/opentelemetry-php) that configures the OpenTelemetry SDK to export data to Uptrace. It does not add any new functionality and is provided only for your convenience.

> [Continue below](#quick-start)

### Option B: Direct OTLP Configuration

Best for: Existing OpenTelemetry users, custom exporters, fine-grained control

> [Direct OTLP Setup](/get/opentelemetry-php/otlp)

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install uptrace-php

**Prerequisites:** Install Composer following the [official installation guide](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-macos).

```bash
composer require uptrace/uptrace
```

### Step 3: Basic Configuration

You can configure the Uptrace client using a [DSN](/get#dsn) (Data Source Name) from the project settings page. Replace `<FIXME>` with your actual Uptrace DSN, and `myservice` with a name that identifies your application.

```php
<?php

declare(strict_types=1);
require __DIR__ . '/vendor/autoload.php';

use OpenTelemetry\API\Common\Instrumentation\Globals;

$uptrace = Uptrace\Distro::builder()
    // copy your project DSN here or use UPTRACE_DSN env var
    //->setDsn('<FIXME>')

    ->setServiceName('myservice')
    ->setServiceVersion('1.0.0')
    ->setResourceAttributes(['deployment.environment' => 'production'])
    ->buildAndRegisterGlobal();
```

### Step 4: Create Your First Trace

Copy the [code](https://github.com/uptrace/uptrace-php/tree/master/example) to `main.php`:

```php
<?php

declare(strict_types=1);
require __DIR__ . '/vendor/autoload.php';

use OpenTelemetry\API\Common\Instrumentation\Globals;
use OpenTelemetry\API\Trace\SpanKind;
use OpenTelemetry\API\Trace\StatusCode;

// Configure OpenTelemetry with sensible defaults.
$uptrace = Uptrace\Distro::builder()
    // copy your project DSN here or use UPTRACE_DSN env var
    // ->setDsn('<FIXME>')

    ->setServiceName('myservice')
    ->setServiceVersion('1.0.0')
    ->buildAndRegisterGlobal();

// Create a tracer. Usually, tracer is a global variable.
$tracer = Globals::tracerProvider()->getTracer('app_or_package_name');

// Create a root span (a trace) to measure some operation.
$main = $tracer->spanBuilder('main-operation')->startSpan();
// End the span when the operation we are measuring is done.
$mainScope = $main->activate();

// The activated scope carries the parent span (main).
// That is how OpenTelemetry manages span relations.
$child1 = $tracer->spanBuilder('GET /posts/:id')
    ->setSpanKind(SpanKind::KIND_SERVER)
    ->startSpan();
$child1Scope = $child1->activate();

$child1->setAttributes([
    'http.method' => 'GET',
    'http.route' => '/posts/:id',
    'http.url' => 'http://localhost:8080/posts/123',
    'http.status_code' => 200,
]);

$exc = new \Exception('dummy error');
$child1->recordException($exc);
$child1->setStatus(StatusCode::STATUS_ERROR, $exc->getMessage());

$child1Scope->detach();
$child1->end();

$child2 = $tracer->spanBuilder('SELECT')->startSpan();
$child2Scope = $child2->activate();

$child2->setAttributes([
    'db.system' => 'mysql',
    'db.statement' => 'SELECT * FROM posts LIMIT 100',
]);

$child2Scope->detach();
$child2->end();

$mainScope->detach();
$main->end();

echo "trace: " . $uptrace->traceUrl($main) . PHP_EOL;
```

### Step 5: Run Your Application

Run the code, replacing `<FIXME>` with your Uptrace DSN:

```bash
UPTRACE_DSN="<FIXME>" php main.php
trace: https://app.uptrace.dev/traces/<trace_id>
```

### Step 6: View Your Trace

Follow the link to view the trace:

![Basic trace](/get/basic-trace.png)

## Configuration Options

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
        setDsn
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
        setServiceName
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
        setServiceVersion
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
        setResourceAttributes
      </code>
    </td>
    
    <td>
      Any other resource attributes including <code>
        deployment.environment
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setSampling
      </code>
    </td>
    
    <td>
      Configures <a href="/get/opentelemetry-php/sampling">
        sampling
      </a>
      
       to reduce costs in high-volume applications.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setDebug
      </code>
    </td>
    
    <td>
      Enable debug mode for troubleshooting.
    </td>
  </tr>
</tbody>
</table>

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
      <a href="/get/opentelemetry-php/zero-code">
        Zero-code instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-php/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-php/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-php/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-php/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-php/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-php/resources">
        Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry Symfony](/guides/opentelemetry-symfony)
- [OpenTelemetry Laravel](/guides/opentelemetry-laravel)
- [OpenTelemetry Slim](/guides/opentelemetry-slim)
