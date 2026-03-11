# Source: https://uptrace.dev/raw/guides/opentelemetry-slim.md

# OpenTelemetry Slim Framework: Instrumentation and Monitoring Guide

> Instrument and monitor Slim PHP applications with OpenTelemetry. Setup auto-instrumentation, manual tracing, database monitoring, and Docker deployment for PHP microservices.

OpenTelemetry Slim instrumentation provides automatic tracing for HTTP requests, routing, and middleware in Slim PHP applications. Using `opentelemetry-auto-slim`, you can add observability to your PHP microservices and track request latencies, database queries, and errors across distributed systems.

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
      Slim Auto-Instrument
    </td>
    
    <td>
      <code>
        open-telemetry/opentelemetry-auto-slim
      </code>
    </td>
    
    <td>
      Auto-trace HTTP requests
    </td>
  </tr>
  
  <tr>
    <td>
      PDO Instrumentation
    </td>
    
    <td>
      <code>
        open-telemetry/opentelemetry-auto-pdo
      </code>
    </td>
    
    <td>
      Trace database queries
    </td>
  </tr>
  
  <tr>
    <td>
      Guzzle Instrumentation
    </td>
    
    <td>
      <code>
        open-telemetry/opentelemetry-auto-guzzle
      </code>
    </td>
    
    <td>
      Trace outgoing HTTP calls
    </td>
  </tr>
  
  <tr>
    <td>
      OpenTelemetry SDK
    </td>
    
    <td>
      <code>
        open-telemetry/sdk
      </code>
    </td>
    
    <td>
      Core SDK and exporters
    </td>
  </tr>
</tbody>
</table>

## What is OpenTelemetry?

[OpenTelemetry](/opentelemetry) is an open-source observability framework that standardizes the collection of telemetry data from applications. It provides three pillars of observability:

- **Distributed Traces**: Track requests across services and components
- **Metrics**: Collect quantitative measurements of application performance
- **Logs**: Capture structured application logs with trace correlation

OpenTelemetry is vendor-neutral, meaning you can export data to any compatible [OpenTelemetry backend](/blog/opentelemetry-backend) such as Uptrace, Jaeger, or Grafana. Deploying an [OpenTelemetry Collector](/opentelemetry/collector) in your infrastructure provides enhanced telemetry data processing capabilities, including filtering, enrichment, and batching before data reaches your backend.

## Prerequisites

- **PHP 8.1+**
- **Slim Framework 4.x**
- **Composer** for dependency management
- **OpenTelemetry PHP extension**

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [PHP zero-code instrumentation guide](/get/opentelemetry-php/zero-code).

</alert>

## Step 1: Install the OpenTelemetry Extension

The OpenTelemetry PHP extension enables auto-instrumentation by hooking into PHP function calls at the runtime level.

### Install Build Dependencies

<code-group>

```shell [Linux (apt)]
sudo apt-get install gcc make autoconf php-dev
```

```shell [macOS (homebrew)]
brew install gcc make autoconf
```

</code-group>

### Install the Extension

<code-group>

```shell [pecl]
pecl install opentelemetry
```

```shell [pickle]
php pickle.phar install opentelemetry
```

```shell [php-extension-installer (Docker)]
install-php-extensions opentelemetry
```

</code-group>

### Enable the Extension

Add to your `php.ini` file (run `php --ini` to find the location):

```ini
[opentelemetry]
extension=opentelemetry.so
```

### Verify Installation

```shell
php -m | grep opentelemetry
```

## Step 2: Install Slim Instrumentation

The Slim auto-instrumentation package registers hooks via Composer that automatically create spans for `App::handle()` and routing middleware.

```shell
composer require open-telemetry/opentelemetry-auto-slim
```

Install the OpenTelemetry SDK and OTLP exporter:

```shell
# Core SDK
composer require open-telemetry/sdk

# OTLP exporter (gRPC or HTTP)
composer require open-telemetry/exporter-otlp

# Required transport
composer require php-http/guzzle7-adapter
```

## Step 3: Configure OpenTelemetry

### Using Uptrace SDK

The simplest approach is the [Uptrace PHP SDK](/get/opentelemetry-php), which bundles the OpenTelemetry SDK with sensible defaults:

```shell
composer require uptrace/uptrace
```

In your `public/index.php`, add configuration right after the autoloader:

```php
<?php

require __DIR__ . '/../vendor/autoload.php';

// Configure OpenTelemetry with Uptrace
$uptrace = Uptrace\Distro::builder()
    // Set DSN here or use UPTRACE_DSN env var
    ->setDsn('<FIXME>')
    ->setServiceName('slim-app')
    ->setServiceVersion('1.0.0')
    ->buildAndRegisterGlobal();

// Create Slim app
$app = Slim\Factory\AppFactory::create();

$app->get('/', function ($request, $response) {
    $response->getBody()->write('Hello, World!');
    return $response;
});

$app->get('/health', function ($request, $response) {
    $response->getBody()->write(json_encode(['status' => 'ok']));
    return $response->withHeader('Content-Type', 'application/json');
});

$app->run();
```

### Using OpenTelemetry SDK Directly

For a vendor-neutral setup, configure the SDK through environment variables:

```shell
export OTEL_SERVICE_NAME="slim-app"
export OTEL_TRACES_EXPORTER="otlp"
export OTEL_METRICS_EXPORTER="otlp"
export OTEL_LOGS_EXPORTER="otlp"
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.uptrace.dev:4317"
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>"
export OTEL_EXPORTER_OTLP_COMPRESSION="gzip"
export OTEL_PHP_AUTOLOAD_ENABLED="true"
```

With `OTEL_PHP_AUTOLOAD_ENABLED=true`, the SDK initializes automatically via Composer and no code changes are needed. For more details, see the [OpenTelemetry PHP guide](/get/opentelemetry-php).

## Custom Instrumentation

Add custom spans to trace specific business logic beyond automatic instrumentation:

```php
<?php

use OpenTelemetry\API\Globals;
use OpenTelemetry\API\Trace\StatusCode;

$app->post('/api/orders', function ($request, $response) {
    $tracer = Globals::tracerProvider()->getTracer('slim-app');
    $span = $tracer->spanBuilder('create-order')->startSpan();
    $scope = $span->activate();

    try {
        $data = json_decode($request->getBody()->getContents(), true);
        $span->setAttribute('order.customer_id', $data['customer_id'] ?? '');
        $span->setAttribute('order.item_count', count($data['items'] ?? []));

        // Validate order
        $validateSpan = $tracer->spanBuilder('validate-order')->startSpan();
        validateOrder($data);
        $validateSpan->end();

        // Save to database
        $dbSpan = $tracer->spanBuilder('save-order')->startSpan();
        $dbSpan->setAttribute('db.operation', 'INSERT');
        $dbSpan->setAttribute('db.table', 'orders');
        $orderId = saveOrder($data);
        $dbSpan->end();

        $span->setAttribute('order.id', $orderId);
        $response->getBody()->write(json_encode(['order_id' => $orderId]));
        return $response->withHeader('Content-Type', 'application/json');

    } catch (\Exception $e) {
        $span->recordException($e);
        $span->setStatus(StatusCode::STATUS_ERROR, $e->getMessage());
        $response->getBody()->write(json_encode(['error' => $e->getMessage()]));
        return $response->withHeader('Content-Type', 'application/json')->withStatus(500);
    } finally {
        $scope->detach();
        $span->end();
    }
});
```

### Tracing Middleware

Create reusable middleware for cross-cutting tracing concerns:

```php
<?php

use OpenTelemetry\API\Globals;
use Psr\Http\Message\ServerRequestInterface as Request;
use Psr\Http\Server\RequestHandlerInterface as Handler;
use Slim\Psr7\Response;

$app->add(function (Request $request, Handler $handler) {
    $tracer = Globals::tracerProvider()->getTracer('slim-app');
    $span = $tracer->spanBuilder('request-middleware')->startSpan();
    $scope = $span->activate();

    try {
        // Add request metadata
        $span->setAttribute('http.user_agent', $request->getHeaderLine('User-Agent'));
        $span->setAttribute('client.ip', $request->getServerParams()['REMOTE_ADDR'] ?? '');

        $response = $handler->handle($request);

        $span->setAttribute('http.status_code', $response->getStatusCode());
        return $response;
    } finally {
        $scope->detach();
        $span->end();
    }
});
```

## Database Instrumentation

### PDO Auto-Instrumentation

Automatically trace all PDO database queries:

```shell
composer require open-telemetry/opentelemetry-auto-pdo
```

No code changes are needed. All queries executed through PDO will be automatically traced with query text, execution time, and database metadata.

### Eloquent (via Illuminate Database)

If you use Illuminate Database (Eloquent) with Slim:

```shell
composer require open-telemetry/opentelemetry-auto-laravel
```

This traces Eloquent queries, model events, and database transactions via the Laravel auto-instrumentation package, which covers the Illuminate database layer.

## Environment Variables Configuration

Configure OpenTelemetry through environment variables for production:

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Example Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        OTEL_SERVICE_NAME
      </code>
    </td>
    
    <td>
      Service name
    </td>
    
    <td>
      <code>
        slim-app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_EXPORTER_OTLP_ENDPOINT
      </code>
    </td>
    
    <td>
      OTLP collector endpoint
    </td>
    
    <td>
      <code>
        https://api.uptrace.dev:4317
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_EXPORTER_OTLP_HEADERS
      </code>
    </td>
    
    <td>
      Authentication headers
    </td>
    
    <td>
      <code>
        uptrace-dsn=<FIXME>
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER
      </code>
    </td>
    
    <td>
      Sampling strategy
    </td>
    
    <td>
      <code>
        parentbased_traceidratio
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER_ARG
      </code>
    </td>
    
    <td>
      Sampling ratio (0.0 to 1.0)
    </td>
    
    <td>
      <code>
        0.1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_PHP_AUTOLOAD_ENABLED
      </code>
    </td>
    
    <td>
      Auto-init via Composer
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_EXPORTER_OTLP_COMPRESSION
      </code>
    </td>
    
    <td>
      Compression algorithm
    </td>
    
    <td>
      <code>
        gzip
      </code>
    </td>
  </tr>
</tbody>
</table>

For the full list, see the [OpenTelemetry environment variables reference](/opentelemetry/env-vars).

## Docker Deployment

Deploy a Slim application with OpenTelemetry in Docker:

```dockerfile
FROM php:8.3-apache

# Install php-extension-installer, then use it to add the OpenTelemetry extension
ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/
RUN chmod +x /usr/local/bin/install-php-extensions && \
    install-php-extensions opentelemetry

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html
COPY composer.json composer.lock ./
RUN composer install --no-dev --optimize-autoloader

COPY . .

# Point Apache to Slim's public/ directory
ENV APACHE_DOCUMENT_ROOT=/var/www/html/public
RUN sed -ri 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf && \
    a2enmod rewrite

# Configure OpenTelemetry via environment variables
ENV OTEL_SERVICE_NAME="slim-app"
ENV OTEL_TRACES_EXPORTER="otlp"
ENV OTEL_METRICS_EXPORTER="otlp"
ENV OTEL_EXPORTER_OTLP_COMPRESSION="gzip"
ENV OTEL_PHP_AUTOLOAD_ENABLED="true"

EXPOSE 80
```

With Docker Compose:

```yaml
version: '3.8'

services:
  slim-app:
    build: .
    ports:
      - "80:80"
    environment:
      - OTEL_SERVICE_NAME=slim-app
      - OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
      - OTEL_EXPORTER_OTLP_HEADERS=uptrace-dsn=${UPTRACE_DSN}
      - OTEL_PHP_AUTOLOAD_ENABLED=true
    depends_on:
      - mysql

  mysql:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: slimapp
```

For a complete Docker setup with the OpenTelemetry Collector, see the [Docker deployment guide](/guides/opentelemetry-docker).

## PHP-FPM Considerations

When running Slim behind PHP-FPM, telemetry is exported at the end of each request. For high-traffic applications, consider:

- Using the [OpenTelemetry Collector](/opentelemetry/collector) as a local relay to batch and forward telemetry
- Adjusting batch processor settings via environment variables
- Monitoring PHP-FPM worker pool usage alongside application traces

For PHP-FPM-specific configuration, see the [PHP-FPM instrumentation guide](/guides/opentelemetry-php-fpm).

## Troubleshooting

**Extension not loading**: Verify with `php -m | grep opentelemetry`. If missing, check that `php.ini` has the correct `extension=opentelemetry.so` line and the `.so` file exists in the extensions directory (`php -i | grep extension_dir`).

**No traces appearing**: Confirm `OTEL_EXPORTER_OTLP_ENDPOINT` is reachable. Check PHP error logs for SDK initialization errors.

**Auto-instrumentation not working**: Ensure `OTEL_PHP_AUTOLOAD_ENABLED=true` is set, or verify that Uptrace/SDK initialization happens before `$app->run()`.

**High memory usage**: Reduce the batch processor queue size:

```shell
export OTEL_BSP_MAX_QUEUE_SIZE=512
export OTEL_BSP_MAX_EXPORT_BATCH_SIZE=128
```

**Debug logging**: Enable verbose output:

```shell
export OTEL_LOG_LEVEL=debug
```

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's next?

Your Slim application is now instrumented with OpenTelemetry for comprehensive monitoring. Next steps:

- [Laravel instrumentation](/guides/opentelemetry-laravel) for full-featured PHP applications
- [Symfony instrumentation](/guides/opentelemetry-symfony) for enterprise PHP frameworks
- [PHP-FPM instrumentation](/guides/opentelemetry-php-fpm) for production PHP deployments
- [OpenTelemetry PHP guide](/get/opentelemetry-php) for deeper instrumentation options
