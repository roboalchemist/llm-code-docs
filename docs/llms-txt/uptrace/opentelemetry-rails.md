# Source: https://uptrace.dev/raw/guides/opentelemetry-rails.md

# Ruby on Rails Application Monitoring with OpenTelemetry

> Rails monitoring guide using OpenTelemetry. Monitor Rails app performance, ActiveRecord queries, and server metrics with distributed tracing and APM capabilities.

This Rails monitoring guide shows you how to implement performance monitoring and observability in your Ruby on Rails applications using OpenTelemetry.

With OpenTelemetry Rails instrumentation, you can monitor Rails app performance, track ActiveRecord query performance, and gain insights into your Ruby application monitoring metrics.

**Comparing Rails monitoring tools?** See our [Rails monitoring tools comparison](/tools/rails-monitoring-tools) covering Scout APM, AppSignal, New Relic, and other solutions.

**Note:** While OpenTelemetry supports traces, metrics, and logs, the Ruby implementation currently has stable support for **traces only**. Metrics and logs APIs are under development and should be considered experimental.

## What is OpenTelemetry?

[OpenTelemetry](/opentelemetry) is an observability framework â an API, SDK, and tools designed to aid in the generation and collection of application telemetry data such as metrics, logs, and [distributed traces](/opentelemetry/distributed-tracing). It provides a vendor-neutral way to instrument applications and export telemetry data to various observability backends.

## What is Ruby on Rails?

Ruby on Rails is a popular open-source web application framework written in the Ruby programming language. Rails follows the Model-View-Controller (MVC) architectural pattern and provides conventions and libraries to simplify and accelerate web development.

Ruby on Rails has gained popularity due to its focus on developer happiness, productivity, and code simplicity. It has been used to build a wide range of applications, from small websites to large, high-traffic platforms.

## Prerequisites

Before implementing OpenTelemetry in your Rails application, ensure you have:

- Ruby >= 3.0 (CRuby >= 3.0, JRuby >= 9.3.2.0, or TruffleRuby >= 22.1)
- A Ruby on Rails application (any supported version)
- Basic understanding of observability concepts
- Access to an observability backend (Jaeger, Zipkin, commercial APM, etc.)

For comprehensive Ruby instrumentation details, see the [OpenTelemetry Ruby guide](/get/opentelemetry-ruby).

## Installation

### Core Dependencies

Install the required OpenTelemetry gems. You can install them directly or add them to your Gemfile:

```ruby
# Add to your Gemfile
gem 'opentelemetry-sdk'
gem 'opentelemetry-exporter-otlp'
gem 'opentelemetry-instrumentation-all'
```

The `opentelemetry-instrumentation-all` metapackage provides comprehensive Rails monitoring for all popular Ruby libraries with minimal configuration.

Alternatively, install via command line:

```shell
gem install opentelemetry-sdk
gem install opentelemetry-exporter-otlp
gem install opentelemetry-instrumentation-all
```

### Rails-Specific Instrumentation

The `opentelemetry-instrumentation-all` metapackage bundles all Ruby-based instrumentation libraries into a single package, providing a convenient way to add telemetry for all your libraries with minimal effort.

For more granular control, you can install specific instrumentation packages:

```shell
gem install opentelemetry-instrumentation-rails
gem install opentelemetry-instrumentation-active_record
gem install opentelemetry-instrumentation-action_pack
gem install opentelemetry-instrumentation-action_view
gem install opentelemetry-instrumentation-active_job
```

## Configuration

### Basic Setup (Recommended)

For Rails applications, the recommended way to initialize OpenTelemetry is in a Rails initializer. Create a file named `config/initializers/opentelemetry.rb`:

```ruby
# config/initializers/opentelemetry.rb
require 'opentelemetry/sdk'
require 'opentelemetry/instrumentation/all'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'your-rails-app'
  c.use_all() # enables all available instrumentation!
end
```

### Alternative Configuration in environment.rb

You can also configure OpenTelemetry in `config/environment.rb` before application initialization:

```ruby
require 'opentelemetry/sdk'
require_relative 'application'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'your-rails-app'
  c.use_all
end

Rails.application.initialize!
```

### Selective Instrumentation

If you prefer more control over which libraries are instrumented, you can specify individual instrumentations:

```ruby
require 'opentelemetry/sdk'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'your-rails-app'
  c.use 'OpenTelemetry::Instrumentation::Rails'
  c.use 'OpenTelemetry::Instrumentation::ActionPack'
  c.use 'OpenTelemetry::Instrumentation::ActionView'
  c.use 'OpenTelemetry::Instrumentation::ActiveRecord'
end
```

### Disabling Specific Instrumentation

You can disable specific instrumentation libraries using configuration or environment variables:

```ruby
# Disable via configuration
OpenTelemetry::SDK.configure do |c|
  config = {'OpenTelemetry::Instrumentation::Redis' => { enabled: false }}
  c.use_all(config)
end
```

```shell
# Disable via environment variable
export OTEL_RUBY_INSTRUMENTATION_REDIS_ENABLED=false
```

## Environment Variables Configuration

Configure OpenTelemetry using environment variables for flexible deployment:

### Essential Environment Variables

```shell
# Service identification
export OTEL_SERVICE_NAME="your-rails-app"

# Exporter configuration
export OTEL_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318"

# For production with authentication
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"

# Resource attributes
export OTEL_RESOURCE_ATTRIBUTES="environment=production,version=1.0.0"
```

### Console Output for Development

For development and testing, you can output traces to the console:

```shell
export OTEL_TRACES_EXPORTER=console
rails server -p 3000
```

### Debug Configuration

Enable debug logging to troubleshoot configuration issues:

```shell
export OTEL_LOG_LEVEL=debug
```

## ActiveRecord Instrumentation

For comprehensive activerecord monitoring and database query performance tracking, ensure ActiveRecord instrumentation is enabled:

```ruby
# If using selective instrumentation
require 'opentelemetry-instrumentation-active_record'

OpenTelemetry::SDK.configure do |c|
  c.use 'OpenTelemetry::Instrumentation::ActiveRecord'
end
```

The `opentelemetry-instrumentation-active_record` gem provides automatic instrumentation for ActiveRecord, capturing trace data for database queries, including SQL statements and their execution duration.

## Manual Instrumentation

### Creating Custom Spans

Add custom instrumentation to capture application-specific logic:

```ruby
# Obtain a tracer
tracer = OpenTelemetry.tracer_provider.tracer('your-app-tracer')

# Create spans for custom logic
def process_order(order)
  tracer.in_span('process_order') do |span|
    span.add_attributes({
      'order.id' => order.id,
      'order.total' => order.total,
      'customer.id' => order.customer_id
    })

    # Your business logic here
    span.add_event('Order validation completed')
    validate_order(order)

    span.add_event('Payment processing started')
    process_payment(order)

    span.set_status(OpenTelemetry::Trace::Status.ok)
  end
rescue StandardError => e
  span&.record_exception(e)
  span&.set_status(OpenTelemetry::Trace::Status.error("Order processing failed: #{e.message}"))
  raise
end
```

### Adding Context to Current Spans

Enrich existing spans with additional information:

```ruby
def track_user_action(user, action)
  current_span = OpenTelemetry::Trace.current_span
  return unless current_span.recording?

  current_span.add_attributes({
    'user.id' => user.id,
    'user.role' => user.role,
    'action.type' => action
  })

  current_span.add_event("User performed action: #{action}")
end
```

### Using Semantic Conventions

Use semantic conventions for standardized attributes:

```ruby
require 'opentelemetry/semantic_conventions'

current_span = OpenTelemetry::Trace.current_span
current_span.add_attributes({
  OpenTelemetry::SemanticConventions::Trace::HTTP_METHOD => "POST",
  OpenTelemetry::SemanticConventions::Trace::HTTP_URL => "https://api.example.com/orders"
})
```

### Exception Handling

Properly handle and record exceptions in spans:

```ruby
def risky_operation
  tracer.in_span('risky_operation') do |span|
    # Your code that might raise an exception
    some_risky_code()
  end
rescue StandardError => e
  # The span is automatically marked as error and exception is recorded
  # when using tracer.in_span
  Rails.logger.error("Operation failed: #{e.message}")
  raise
end
```

## Production Configuration

### Performance Optimization

For production environments, use BatchSpanProcessor for more efficient trace processing:

```ruby
require 'opentelemetry/sdk'
require 'opentelemetry/exporter/otlp'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'your-rails-app'
  c.add_span_processor(
    OpenTelemetry::SDK::Trace::Export::BatchSpanProcessor.new(
      OpenTelemetry::Exporter::OTLP::Exporter.new
    )
  )
  c.use_all
end
```

### Resource Attributes

Configure resource attributes to provide context about your service:

```ruby
OpenTelemetry::SDK.configure do |c|
  c.service_name = 'your-rails-app'
  c.service_version = '1.2.3'
  c.resource = OpenTelemetry::SDK::Resources::Resource.create({
    'deployment.environment' => Rails.env,
    'service.namespace' => 'ecommerce',
    'service.instance.id' => Socket.gethostname
  })
  c.use_all
end
```

This configuration enables ruby server monitoring by capturing host and process information alongside your Rails application metrics.

### Sampling Configuration

Configure sampling to manage trace volume in high-traffic applications:

```ruby
OpenTelemetry::SDK.configure do |c|
  c.service_name = 'your-rails-app'
  # Sample 10% of traces
  c.add_span_processor(
    OpenTelemetry::SDK::Trace::Export::BatchSpanProcessor.new(
      OpenTelemetry::Exporter::OTLP::Exporter.new,
      max_export_batch_size: 512,
      export_timeout_millis: 30_000
    )
  )
  c.use_all
end
```

## Running Your Instrumented Application

### Development Mode

```shell
# Console output for debugging
OTEL_TRACES_EXPORTER=console rails server
```

### Production Mode

```shell
OTEL_SERVICE_NAME=your-rails-app \
OTEL_EXPORTER=otlp \
OTEL_EXPORTER_OTLP_ENDPOINT=https://your-collector.example.com:4318 \
OTEL_RESOURCE_ATTRIBUTES=environment=production \
rails server
```

### Docker Deployment

Example Dockerfile configuration:

```dockerfile
FROM ruby:3.1

# Set environment variables
ENV OTEL_SERVICE_NAME=your-rails-app
ENV OTEL_EXPORTER=otlp
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318

# Copy application code
COPY . /app
WORKDIR /app

# Install dependencies
RUN bundle install

CMD ["rails", "server", "-b", "0.0.0.0"]
```

## Troubleshooting

### Common Issues

1. **Missing traces**: Ensure the exporter endpoint is reachable and properly configured
2. **Performance impact**: Use BatchSpanProcessor in production environments
3. **Missing instrumentation**: Verify that required gems are installed and enabled
4. **High memory usage**: Configure sampling and batch processing appropriately

### Debugging

Enable console output to verify trace generation:

```shell
export OTEL_TRACES_EXPORTER=console
export OTEL_LOG_LEVEL=debug
rails server
```

### Verifying Installation

Create a simple test to verify OpenTelemetry is working:

```ruby
# In a Rails controller or console
tracer = OpenTelemetry.tracer_provider.tracer('test')
tracer.in_span('test_span') do |span|
  span.add_attributes({'test' => 'value'})
  puts "OpenTelemetry is working!"
end
```

### Health Check Endpoint

Add a health check endpoint to verify instrumentation:

```ruby
# In routes.rb
get '/health', to: 'health#check'

# In app/controllers/health_controller.rb
class HealthController < ApplicationController
  def check
    tracer = OpenTelemetry.tracer_provider.tracer('health_check')
    tracer.in_span('health_check') do |span|
      span.add_attributes({
        'service.name' => Rails.application.class.module_parent_name,
        'service.version' => '1.0.0'
      })
      render json: { status: 'ok', timestamp: Time.current }
    end
  end
end
```

## What is Uptrace?

Uptrace is an open-source [Application Performance Monitoring (APM)](/opentelemetry/apm) platform built specifically for OpenTelemetry. It provides a unified observability solution that supports distributed tracing, metrics, and logs in a single interface.

### Key Features

- **Unified Interface** - Single dashboard for traces, metrics, and logs
- **OpenTelemetry Native** - Built from the ground up to fully follow OpenTelemetry specifications
- **High Performance** - Processes 10,000+ spans per second on a single core
- **Efficient Storage** - Advanced compression (1KB spans compressed to ~40 bytes)
- **Cost-Effective** - Open-source with affordable cloud hosting options
- **Rich Dashboards** - Intuitive query builder and visualization tools
- **Alerting** - Automated alerts via email, Slack, Telegram, and more

For comparing with other solutions, see [top APM tools](/tools/top-apm-tools).

### Deployment Options

1. **Uptrace Cloud** - Managed service with no setup required
2. **Self-Hosted** - Deploy on your own infrastructure using [open-source APM setup](/get/hosted/open-source-apm)
3. **Hybrid** - Mix of cloud and on-premises depending on needs

## uptrace-ruby OpenTelemetry Wrapper

The `uptrace-ruby` gem is a thin wrapper over the standard `opentelemetry-ruby` SDK that pre-configures OpenTelemetry to export data to Uptrace. It doesn't add new functionality but simplifies the setup process significantly.

### Benefits of uptrace-ruby

- **Simplified Configuration** - Pre-configured with sensible defaults for Uptrace
- **Automatic Setup** - Handles OTLP exporter configuration automatically
- **Performance Optimized** - Configured for optimal performance with Uptrace
- **Easy Integration** - Drop-in replacement for standard OpenTelemetry setup

### Installation

Add the uptrace-ruby gem to your Gemfile:

```ruby
# Add to your Gemfile
gem 'uptrace'
```

Or install directly:

```shell
gem install uptrace
```

### Basic Rails Configuration

Replace your standard OpenTelemetry configuration with uptrace-ruby:

```ruby
# config/initializers/opentelemetry.rb
require 'uptrace'

# Configure OpenTelemetry with Uptrace
# Copy your project DSN here or use UPTRACE_DSN env var
Uptrace.configure_opentelemetry(dsn: 'https://TOKEN@api.uptrace.dev?grpc=4317') do |c|
  # c is OpenTelemetry::SDK::Configurator
  c.service_name = 'your-rails-app'
  c.service_version = '1.0.0'
  c.resource = OpenTelemetry::SDK::Resources::Resource.create({
    'deployment.environment' => Rails.env,
    'service.namespace' => 'your-namespace'
  })
end
```

### Environment Variable Configuration

You can also configure uptrace-ruby using environment variables:

```shell
export UPTRACE_DSN="https://TOKEN@api.uptrace.dev?grpc=4317"
export OTEL_SERVICE_NAME="your-rails-app"
export OTEL_SERVICE_VERSION="1.0.0"
export OTEL_RESOURCE_ATTRIBUTES="environment=production"
```

Then use a simplified configuration:

```ruby
# config/initializers/opentelemetry.rb
require 'uptrace'

# DSN will be read from UPTRACE_DSN environment variable
Uptrace.configure_opentelemetry do |c|
  c.service_name = ENV['OTEL_SERVICE_NAME']
  c.service_version = ENV['OTEL_SERVICE_VERSION']
end
```

### Complete Rails Example with uptrace-ruby

Here's a complete example of instrumenting a Rails application with uptrace-ruby:

```ruby
# Gemfile
gem 'uptrace'
gem 'opentelemetry-instrumentation-all'

# config/initializers/opentelemetry.rb
require 'uptrace'
require 'opentelemetry/instrumentation/all'

Uptrace.configure_opentelemetry(dsn: ENV['UPTRACE_DSN']) do |c|
  c.service_name = 'your-rails-app'
  c.service_version = '1.0.0'
  c.resource = OpenTelemetry::SDK::Resources::Resource.create({
    'deployment.environment' => Rails.env,
    'service.namespace' => 'ecommerce'
  })

  # Enable all available instrumentations
  c.use_all
end
```

### Getting Trace URLs

One unique feature of uptrace-ruby is the ability to get direct URLs to traces:

```ruby
# In your application code
tracer = OpenTelemetry.tracer_provider.tracer('your-app-tracer')

tracer.in_span('process_order') do |span|
  # Your business logic here
  process_order_logic()

  # Get a direct URL to this trace in Uptrace
  trace_url = Uptrace.trace_url(span)
  Rails.logger.info("View this trace: #{trace_url}")
end
```

### Custom Instrumentation with uptrace-ruby

```ruby
require 'uptrace'

# Configure Uptrace
Uptrace.configure_opentelemetry(dsn: ENV['UPTRACE_DSN'])

# Get a tracer
tracer = OpenTelemetry.tracer_provider.tracer('my_app', '1.0.0')

def create_user(name, email)
  tracer.in_span('create_user', kind: :server) do |span|
    span.add_attributes({
      'user.name' => name,
      'user.email' => email
    })

    # Your business logic
    user = User.create(name: name, email: email)

    # Log the trace URL for debugging
    Rails.logger.info("User creation trace: #{Uptrace.trace_url(span)}")

    user
  end
end
```

### Running with uptrace-ruby

```shell
# Set your Uptrace DSN
export UPTRACE_DSN="https://TOKEN@api.uptrace.dev?grpc=4317"

# Run your Rails application
rails server
```

### Uptrace vs Standard OTLP Configuration

**Standard OpenTelemetry Configuration:**

```ruby
require 'opentelemetry/sdk'
require 'opentelemetry/exporter/otlp'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'your-rails-app'
  c.add_span_processor(
    OpenTelemetry::SDK::Trace::Export::BatchSpanProcessor.new(
      OpenTelemetry::Exporter::OTLP::Exporter.new(
        endpoint: 'https://api.uptrace.dev/v1/traces',
        headers: { 'uptrace-dsn' => 'your-dsn' }
      )
    )
  )
end
```

**With uptrace-ruby:**

```ruby
require 'uptrace'

Uptrace.configure_opentelemetry(dsn: 'your-dsn') do |c|
  c.service_name = 'your-rails-app'
end
```

## Integration with Observability Backends

OpenTelemetry supports various observability platforms through the OTLP protocol:

- **Uptrace** - Open-source APM with native OpenTelemetry support
- **Jaeger** - Distributed tracing backend
- **Zipkin** - Distributed tracing system
- **Prometheus** - Metrics collection (when metrics support is stable)
- **Elastic APM** - Application performance monitoring
- **Commercial solutions** - Datadog, New Relic, Honeycomb, SignalFx, etc.

Configure the appropriate endpoint and authentication for your chosen backend.

### Example: Jaeger Configuration

```shell
export OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger-collector:14268/api/traces
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"
```

### Example: Uptrace Configuration

```shell
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=https://TOKEN@api.uptrace.dev?grpc=4317"
export OTEL_EXPORTER_OTLP_COMPRESSION=gzip
```

## Security Considerations

### Sensitive Data

Be careful not to include sensitive information in span attributes:

```ruby
# Bad - includes sensitive data
span.add_attributes({
  'user.email' => user.email,
  'user.password' => user.password  # Never do this!
})

# Good - uses safe identifiers
span.add_attributes({
  'user.id' => user.id,
  'user.role' => user.role
})
```

### Data Sanitization

Consider implementing attribute processors to sanitize data:

```ruby
OpenTelemetry::SDK.configure do |c|
  c.add_span_processor(
    OpenTelemetry::SDK::Trace::Export::SimpleSpanProcessor.new(
      YourCustomSanitizingExporter.new
    )
  )
end
```

## Performance Considerations

### Best Practices

1. **Use BatchSpanProcessor** in production for better performance
2. **Configure appropriate sampling** to manage trace volume
3. **Avoid expensive operations** in span creation
4. **Check if span is recording** before adding attributes:

```ruby
if span.recording?
  span.add_attributes(expensive_computation())
end
```

## Future Roadmap

### Metrics (Under Development)

When metrics support becomes stable, you'll be able to collect custom metrics:

```ruby
# Future functionality (not yet stable)
meter = OpenTelemetry.meter_provider.meter('your-app-meter')
counter = meter.create_counter('requests_total')
counter.add(1, attributes: { 'method' => 'GET' })
```

### Logs (Under Development)

Log correlation with traces will be available when logs support is stable.

## FAQ

**Does Rails monitoring impact application performance?**<br />


Minimal impact (~1-3ms per request). Use sampling and BatchSpanProcessor for high-traffic Rails applications.

**Which Rails monitoring tools work with OpenTelemetry?**<br />


OpenTelemetry works with Uptrace, Jaeger, Zipkin, and other APM tools supporting the OTLP protocol.

**How to monitor ActiveRecord performance specifically?**<br />


ActiveRecord instrumentation is included in the setup and automatically captures database query performance metrics.

**What are the best ruby monitoring tools for Rails?**<br />


OpenTelemetry is the modern standard for ruby monitoring, working with APM tools like Uptrace, Jaeger, and commercial solutions.

## What's Next?

OpenTelemetry allows you to instrument specific parts of your code for custom telemetry collection. You can use OpenTelemetry Ruby APIs to manually create spans and add custom attributes, events, or metrics to capture additional information.

Consider exploring:

- **Custom span creation** for business-critical operations
- **Distributed tracing** across microservices
- **Performance monitoring** and alerting based on trace data
- **Error tracking** and exception correlation
- **Business metrics** and SLI/SLO tracking (when metrics are stable)

For lightweight Ruby applications, explore [Sinatra](/guides/opentelemetry-sinatra) instrumentation. For more advanced usage, refer to the [OpenTelemetry Ruby manual instrumentation documentation](https://opentelemetry.io/docs/languages/ruby/instrumentation/).

## Additional Resources

- [OpenTelemetry Ruby Official Documentation](https://opentelemetry.io/docs/languages/ruby/)
- [OpenTelemetry Ruby GitHub Repository](https://github.com/open-telemetry/opentelemetry-ruby)
- [OpenTelemetry Ruby Contrib Repository](https://github.com/open-telemetry/opentelemetry-ruby-contrib)
- [OpenTelemetry Specification](https://opentelemetry.io/docs/specs/otel/)
- [Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/)
