# Source: https://uptrace.dev/raw/guides/opentelemetry-symfony.md

# OpenTelemetry Symfony monitoring

> OpenTelemetry Symfony is an integration that allows you to use OpenTelemetry with the Symfony PHP framework.

OpenTelemetry Symfony integration allows you to collect telemetry data such as traces, metrics, and logs from your Symfony applications, providing insights into their performance and behavior.

## What is OpenTelemetry?

OpenTelemetry is an open-source observability framework that provides a standardized way to collect, process, and export telemetry data from applications and infrastructure. It combines metrics, logs, and [distributed traces](/opentelemetry/distributed-tracing) into a unified toolkit that helps developers understand how their systems are performing.

OpenTelemetry supports multiple programming languages and platforms, making it suitable for a wide range of applications and environments. For PHP instrumentation details, see the [OpenTelemetry PHP guide](/get/opentelemetry-php).

OpenTelemetry enables developers to instrument their code and collect telemetry data, which can then be exported to various [OpenTelemetry backends](/blog/opentelemetry-backend) or observability platforms for analysis and visualization. Many aspects of OpenTelemetry can be configured using [environment variables](/opentelemetry/env-vars), allowing for flexible deployment configurations without code changes.

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [PHP zero-code instrumentation guide](/get/opentelemetry-php/zero-code).

</alert>

## Auto-instrumentation

OpenTelemetry PHP auto-instrumentation is a powerful feature that allows you to collect telemetry data from your PHP applications with minimal manual configuration.

It automatically adds instrumentation to your application, capturing telemetry data without requiring you to modify code manually.

To use auto-instrumentation, you need to install OpenTelemetry extension.

1. Setup development environment. Installing from source requires proper development environment and some dependencies:<code-group>

```shell [Linux (apt)]
sudo apt-get install gcc make autoconf php-dev
```

```shell [macOS (homebrew)]
brew install gcc make autoconf
```

</code-group>
2. Build/install the extension. With your environment set up you can install the extension:<code-group>

```shell [pecl]
pecl install opentelemetry
```

```shell [picle]
php pickle.phar install opentelemetry
```

```shell [php-extension-installer (docker)]
install-php-extensions opentelemetry
```

</code-group>
3. Add the extension to your `php.ini` file (run `php --ini` to find out file location):```ini
[opentelemetry]
extension=opentelemetry.so
```
4. Verify that the extension is installed and enabled:```shell
php -m | grep opentelemetry
```

## OpenTelemetry Symfony

Symfony auto-instrumentation significantly reduces the manual work required to implement OpenTelemetry in a Symfony application, providing immediate visibility into application performance and behavior.

Install the OpenTelemetry Symfony bundle:

```sh
composer require open-telemetry/opentelemetry-auto-symfony
```

Add the bundle to your `config/bundles.php`:

```sh
return [
    // ...
    OpenTelemetry\Contrib\Symfony\OtelSdkBundle\OtelSdkBundle::class => ['all' => true],
];
```

Create `config/packages/otel.yaml`:

```yaml
otel_sdk:
  resource:
    attributes:
      service.name: 'your-service-name'
  traces:
    sampler:
      type: 'always_on'
  exporters:
    otlp:
      dsn: 'https://api.uptrace.dev:4318'
      protocol: 'http/protobuf'
```

## Manual instrumentation

For custom instrumentation, you can inject the tracer into your services:

```php
use OpenTelemetry\API\Trace\TracerInterface;

class YourService
{
    public function __construct(private TracerInterface $tracer) {}

    public function someMethod()
    {
        $span = $this->tracer->spanBuilder('custom-operation')->startSpan();
        try {
            // Your code here
        } finally {
            $span->end();
        }
    }
}
```

## Conclusion

By integrating OpenTelemetry with Symfony, you can build more robust, observable, and performant PHP applications.

For alternative PHP frameworks, explore [Laravel](/guides/opentelemetry-laravel) for rapid development with auto-instrumentation or [Slim](/guides/opentelemetry-slim) for lightweight microservices.
