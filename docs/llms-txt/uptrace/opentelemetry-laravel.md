# Source: https://uptrace.dev/raw/guides/opentelemetry-laravel.md

# OpenTelemetry Integration for Laravel: Full Guide

> Learn how to implement OpenTelemetry in Laravel applications with step-by-step setup, auto-instrumentation, and PHP observability best practices for production monitoring.

OpenTelemetry integration with Laravel applications provides comprehensive observability through distributed tracing, metrics, and logging. This guide shows you how to implement OpenTelemetry in Laravel using auto-instrumentation for production-ready monitoring.

## What is OpenTelemetry?

OpenTelemetry is an open-source observability framework that provides a standardized way to collect, process, and export telemetry data from applications and infrastructure. It combines metrics, logs, and [distributed traces](/opentelemetry/distributed-tracing) into a unified toolkit that helps developers understand how their systems are performing. For Laravel applications, it offers:

- **Auto-instrumentation**: Automatic tracing of Laravel framework components
- **Distributed tracing**: End-to-end request tracking across services
- **Performance monitoring**: Database queries, HTTP requests, and job processing
- **Custom metrics**: Business-specific measurements and KPIs

## Why Use OpenTelemetry with Laravel?

Compared to other Laravel monitoring solutions:

<table>
<thead>
  <tr>
    <th>
      Solution
    </th>
    
    <th>
      Setup
    </th>
    
    <th>
      Cost
    </th>
    
    <th>
      Distributed Tracing
    </th>
    
    <th>
      Vendor Lock-in
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        OpenTelemetry
      </strong>
    </td>
    
    <td>
      Medium
    </td>
    
    <td>
      Free + Backend
    </td>
    
    <td>
      Excellent
    </td>
    
    <td>
      None
    </td>
  </tr>
  
  <tr>
    <td>
      Laravel Pulse
    </td>
    
    <td>
      Easy
    </td>
    
    <td>
      Free
    </td>
    
    <td>
      None
    </td>
    
    <td>
      None
    </td>
  </tr>
  
  <tr>
    <td>
      Laravel Nightwatch
    </td>
    
    <td>
      Easy
    </td>
    
    <td>
      Paid
    </td>
    
    <td>
      Good
    </td>
    
    <td>
      Yes
    </td>
  </tr>
  
  <tr>
    <td>
      New Relic
    </td>
    
    <td>
      Easy
    </td>
    
    <td>
      Expensive
    </td>
    
    <td>
      Excellent
    </td>
    
    <td>
      Yes
    </td>
  </tr>
</tbody>
</table>

OpenTelemetry provides industry-standard observability without vendor lock-in, making it ideal for distributed Laravel applications.

## Requirements

Before implementing OpenTelemetry in Laravel applications:

- **PHP 8.1+** (required for auto-instrumentation)
- **Laravel 6.0 - 12.0** (full support up to Laravel 12.0)
- **OpenTelemetry PHP Extension**
- **Composer** for dependency management

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [PHP zero-code instrumentation guide](/get/opentelemetry-php/zero-code).

</alert>

## Step 1: Install OpenTelemetry Extension

The extension enables auto-instrumentation for Laravel applications. Multiple installation methods are available:

```bash
# Method 1: PECL (recommended)
pecl install opentelemetry

# Method 2: Package managers
apt-get install php-opentelemetry  # Ubuntu/Debian
yum install php-opentelemetry      # CentOS/RHEL

# Method 3: Alpine Linux (for Docker)
echo "@testing https://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
apk add php81-pecl-opentelemetry@testing
```

Add to your `php.ini` file:

```ini
extension=opentelemetry

# Optional settings
opentelemetry.validate_hook_functions=On
opentelemetry.conflicts=none
```

Verify the installation works:

```bash
php --ri opentelemetry
# Should display extension information and version
```

## Step 2: Install Laravel Packages

Install the required packages for Laravel OpenTelemetry integration:

```bash
# Core Laravel auto-instrumentation package
composer require open-telemetry/opentelemetry-auto-laravel

# OpenTelemetry SDK and exporter
composer require open-telemetry/sdk open-telemetry/exporter-otlp

# For Uptrace integration (optional)
composer require uptrace/uptrace
```

## Step 3: Configure OpenTelemetry

Add OpenTelemetry initialization to `public/index.php` right after the autoloader:

```php
<?php
require __DIR__.'/../vendor/autoload.php';

/*
|--------------------------------------------------------------------------
| Configure OpenTelemetry
|--------------------------------------------------------------------------
*/

use Uptrace\Distro;

$uptrace = Distro::builder()
    ->setDsn(env('UPTRACE_DSN', 'your-project-dsn'))
    ->setServiceName(env('OTEL_SERVICE_NAME', 'laravel-app'))
    ->setServiceVersion(env('OTEL_SERVICE_VERSION', '1.0.0'))
    ->buildAndRegisterGlobal();
```

Set up environment variables in your `.env` file using the standard OpenTelemetry configuration:

```env
# Service identification
OTEL_SERVICE_NAME=laravel-ecommerce
OTEL_SERVICE_VERSION=1.0.0

# Uptrace configuration
UPTRACE_DSN=https://your-project-token@api.uptrace.dev/project-id

# Enable auto-instrumentation
OTEL_PHP_AUTOLOAD_ENABLED=true
OTEL_TRACES_EXPORTER=otlp
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp

# OTLP protocol settings
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4318

# Sampling (adjust based on traffic)
OTEL_TRACES_SAMPLER=parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG=1.0

# Context propagation
OTEL_PROPAGATORS=tracecontext,baggage
```

## Step 4: Test the Integration

Start your Laravel application and OpenTelemetry will automatically instrument it:

```bash
php artisan serve
```

Make some requests to generate traces:

```bash
curl http://localhost:8000/
curl http://localhost:8000/api/users
```

You should see traces appearing in your Uptrace project dashboard.

## Custom Instrumentation Examples

While auto-instrumentation covers most Laravel components, you can add custom instrumentation for business logic:

### Controller with Custom Spans

This example shows how to add business context to your Laravel controllers:

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use OpenTelemetry\API\Globals;
use OpenTelemetry\API\Trace\Span;
use OpenTelemetry\API\Trace\StatusCode;

class OrderController extends Controller
{
    public function store(Request $request)
    {
        $tracer = Globals::tracerProvider()->getTracer('order-service');
        $span = $tracer->spanBuilder('create-order')
            ->setAttribute('user.id', $request->user()?->id)
            ->setAttribute('order.items.count', count($request->input('items', [])))
            ->startSpan();

        $scope = $span->activate();

        try {
            $validated = $request->validate([
                'customer_email' => 'required|email',
                'items' => 'required|array|min:1',
            ]);

            // Database operations are automatically traced
            $order = \App\Models\Order::create([
                'customer_email' => $validated['customer_email'],
                'total' => $this->calculateTotal($validated['items']),
                'status' => 'pending',
            ]);

            $span->setAttribute('order.id', $order->id);
            $span->setStatus(StatusCode::STATUS_OK);

            return response()->json(['order_id' => $order->id], 201);

        } catch (\Exception $e) {
            $span->setStatus(StatusCode::STATUS_ERROR, $e->getMessage());
            $span->recordException($e);
            throw $e;
        } finally {
            $scope->detach();
            $span->end();
        }
    }
}
```

### Custom Business Metrics

Track important business metrics alongside technical performance data:

```php
<?php

namespace App\Services;

use OpenTelemetry\API\Globals;

class BusinessMetrics
{
    private $meter;
    private $orderCounter;
    private $revenueHistogram;

    public function __construct()
    {
        $this->meter = Globals::meterProvider()->getMeter('business-metrics');

        $this->orderCounter = $this->meter->createCounter(
            'orders_total',
            'count',
            'Total number of orders'
        );

        $this->revenueHistogram = $this->meter->createHistogram(
            'order_value',
            'USD',
            'Order value distribution'
        );
    }

    public function recordOrder(string $status, float $value, string $channel): void
    {
        $attributes = [
            'order.status' => $status,
            'order.channel' => $channel,
        ];

        $this->orderCounter->add(1, $attributes);
        $this->revenueHistogram->record($value, $attributes);
    }
}
```

### Laravel Job Instrumentation

Add custom spans to Laravel queue jobs for better visibility:

```php
<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use OpenTelemetry\API\Globals;

class ProcessOrderJob implements ShouldQueue
{
    use Dispatchable, Queueable;

    public function __construct(
        public readonly int $orderId
    ) {}

    public function handle(): void
    {
        $tracer = Globals::tracerProvider()->getTracer('order-jobs');
        $span = $tracer->spanBuilder('process-order')
            ->setAttribute('order.id', $this->orderId)
            ->setAttribute('queue.name', $this->queue ?? 'default')
            ->startSpan();

        $scope = $span->activate();

        try {
            $order = \App\Models\Order::findOrFail($this->orderId);

            // Process payment (HTTP calls are automatically traced)
            $paymentResult = \Http::post('/api/payments', [
                'order_id' => $this->orderId,
                'amount' => $order->total,
            ]);

            $order->update(['status' => 'completed']);

        } finally {
            $scope->detach();
            $span->end();
        }
    }
}
```

## Production Configuration

### Environment-Specific Settings

Configure different sampling rates for different environments:

**Development:**

```env
# Full sampling for debugging
OTEL_TRACES_SAMPLER_ARG=1.0
```

**Production:**

```env
# Reduced sampling for performance
OTEL_TRACES_SAMPLER_ARG=0.1
OTEL_BSP_SCHEDULE_DELAY=5000
OTEL_BSP_MAX_EXPORT_BATCH_SIZE=512
```

### Docker Configuration

For containerized Laravel applications:

```dockerfile
FROM php:8.1-fpm

# Install OpenTelemetry extension
RUN pecl install opentelemetry
RUN echo "extension=opentelemetry" > /usr/local/etc/php/conf.d/opentelemetry.ini

COPY . /var/www/html
RUN composer install --optimize-autoloader --no-dev

ENV OTEL_PHP_AUTOLOAD_ENABLED=true
ENV OTEL_SERVICE_NAME=laravel-app

EXPOSE 9000
CMD ["php-fpm"]
```

## Common Issues

### No Traces Appearing

Check if the OpenTelemetry extension is properly loaded:

```bash
# Verify extension is installed
php -m | grep opentelemetry

# Check if autoloading is enabled
echo $OTEL_PHP_AUTOLOAD_ENABLED

# Test with console exporter
export OTEL_TRACES_EXPORTER=console
php artisan serve
```

### Performance Impact

If you notice performance degradation, optimize the configuration:

```env
# Reduce sampling rate
OTEL_TRACES_SAMPLER_ARG=0.05

# Increase batch processing
OTEL_BSP_SCHEDULE_DELAY=10000
OTEL_BSP_MAX_EXPORT_BATCH_SIZE=1024

# Disable specific instrumentation if not needed
OTEL_PHP_DISABLED_INSTRUMENTATIONS=psr3,psr16
```

### Missing Database Traces

Ensure database instrumentation is not disabled:

```env
# Remove any disabled instrumentation that might affect DB queries
# OTEL_PHP_DISABLED_INSTRUMENTATIONS should not contain 'pdo' or 'eloquent'
```

## Comparison with Laravel Pulse

Laravel comes with built-in monitoring via Pulse, but OpenTelemetry offers different advantages:

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
      Laravel Pulse
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Distributed Tracing
      </strong>
    </td>
    
    <td>
      Full support
    </td>
    
    <td>
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Custom Metrics
      </strong>
    </td>
    
    <td>
      Unlimited
    </td>
    
    <td>
      Limited
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        External Services
      </strong>
    </td>
    
    <td>
      Auto-traced
    </td>
    
    <td>
      Manual setup
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Storage
      </strong>
    </td>
    
    <td>
      Any backend
    </td>
    
    <td>
      Database only
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Performance Impact
      </strong>
    </td>
    
    <td>
      Configurable
    </td>
    
    <td>
      Fixed
    </td>
  </tr>
</tbody>
</table>

Use OpenTelemetry when you need distributed tracing across multiple services, or want to integrate with existing observability infrastructure.

## Conclusion

OpenTelemetry provides comprehensive observability for Laravel applications with minimal setup effort. The auto-instrumentation package handles most common scenarios automatically, while custom instrumentation allows you to add business-specific context where needed.

Key benefits:

- **Zero-code auto-instrumentation** for Laravel framework
- **Industry-standard telemetry** compatible with any backend
- **Production-ready performance** with configurable sampling
- **Extensible** with custom metrics and spans

For alternative PHP frameworks, explore [Symfony](/guides/opentelemetry-symfony) for enterprise applications or [Slim](/guides/opentelemetry-slim) for lightweight microservices.

Ready to start monitoring your Laravel application? [Sign up for Uptrace](https://app.uptrace.dev/join) and get comprehensive observability in minutes. Explore [open-source APM deployment](/get/hosted/open-source-apm) options or compare with [top APM tools](/tools/top-apm-tools) for Laravel monitoring.

## Resources

- [OpenTelemetry PHP Documentation](https://opentelemetry.io/docs/languages/php/)
- [Laravel Auto-instrumentation Package](https://packagist.org/packages/open-telemetry/opentelemetry-auto-laravel)
- [Uptrace Laravel Integration](/get/opentelemetry-php#framework-integration)
- [Working Example on GitHub](https://github.com/uptrace/uptrace-php/tree/master/example/laravel)
