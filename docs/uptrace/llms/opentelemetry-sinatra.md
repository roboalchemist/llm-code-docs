# Source: https://uptrace.dev/raw/guides/opentelemetry-sinatra.md

# OpenTelemetry Sinatra monitoring

> Learn how to instrument Sinatra applications with OpenTelemetry for distributed tracing, request monitoring, and performance insights.

OpenTelemetry Sinatra instrumentation allows developers to monitor and diagnose issues with their Sinatra applications, providing valuable insights into HTTP request handling and application behavior in production.

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
      Sinatra Instrumentation
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-sinatra
      </code>
    </td>
    
    <td>
      Auto-trace HTTP requests
    </td>
  </tr>
  
  <tr>
    <td>
      Rack Instrumentation
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-rack
      </code>
    </td>
    
    <td>
      Low-level request tracing
    </td>
  </tr>
  
  <tr>
    <td>
      OTLP Exporter
    </td>
    
    <td>
      <code>
        opentelemetry-exporter-otlp
      </code>
    </td>
    
    <td>
      Export to OTLP backends
    </td>
  </tr>
  
  <tr>
    <td>
      All Instrumentations
    </td>
    
    <td>
      <code>
        opentelemetry-instrumentation-all
      </code>
    </td>
    
    <td>
      Install all available gems
    </td>
  </tr>
</tbody>
</table>

**Quick Start:**

```ruby
gem 'opentelemetry-instrumentation-sinatra'
# Then in your app:
OpenTelemetry::SDK.configure do |c|
  c.service_name = 'my-sinatra-app'
  c.use 'OpenTelemetry::Instrumentation::Sinatra'
end
```

## What is Sinatra?

Sinatra is a lightweight, flexible web application framework for Ruby. It provides a simple DSL (Domain Specific Language) for quickly creating web applications with minimal effort.

Key features of Sinatra include:

- Minimal and expressive DSL for defining routes
- Built on top of Rack middleware
- Support for various template engines (ERB, Haml, Slim)
- Easy integration with databases and ORMs
- Flexible configuration and extensions

Sinatra's simplicity makes it ideal for microservices, APIs, and small to medium-sized web applications.

## What is OpenTelemetry?

[OpenTelemetry](/opentelemetry) is an observability framework â an API, SDK, and tools designed to aid in the generation and collection of application telemetry data such as metrics, logs, and [distributed traces](/opentelemetry/distributed-tracing). It provides a vendor-neutral way to instrument applications and export telemetry data to various observability backends.

OpenTelemetry supports multiple programming languages and platforms, making it suitable for a wide range of applications and environments.

OpenTelemetry enables developers to instrument their code and collect telemetry data, which can then be exported to various [OpenTelemetry backends](/blog/opentelemetry-backend) or observability platforms for analysis and visualization. The [OpenTelemetry Collector](/opentelemetry/collector) serves as an intermediary layer that can receive, process, and export telemetry data with advanced features like tail sampling and metric aggregation.

## Sinatra instrumentation

OpenTelemetry Sinatra instrumentation automatically traces incoming HTTP requests, capturing route information, request parameters, and response status codes.

To install the instrumentation:

```shell
gem install opentelemetry-instrumentation-sinatra
```

If you use Bundler, add to your Gemfile:

```ruby
gem 'opentelemetry-sdk'
gem 'opentelemetry-exporter-otlp'
gem 'opentelemetry-instrumentation-sinatra'
```

- [Documentation](https://opentelemetry.io/docs/languages/ruby/instrumentation/)
- [Reference](https://rubydoc.info/gems/opentelemetry-instrumentation-sinatra)

## Getting started

Configure OpenTelemetry and enable Sinatra instrumentation:

```ruby
require 'sinatra'
require 'opentelemetry/sdk'
require 'opentelemetry/exporter/otlp'
require 'opentelemetry/instrumentation/sinatra'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'my-sinatra-app'
  c.use 'OpenTelemetry::Instrumentation::Sinatra'
end
```

Alternatively, you can use `use_all` to install all available instrumentations:

```ruby
require 'sinatra'
require 'opentelemetry/sdk'
require 'opentelemetry/exporter/otlp'
require 'opentelemetry-instrumentation-all'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'my-sinatra-app'
  c.use_all
end
```

## Configuration with Uptrace

To export telemetry data to Uptrace:

```ruby
require 'sinatra'
require 'uptrace'
require 'opentelemetry/instrumentation/sinatra'

Uptrace.configure_opentelemetry(dsn: 'https://<token>@api.uptrace.dev/<project_id>') do |c|
  c.service_name = 'my-sinatra-app'
  c.use 'OpenTelemetry::Instrumentation::Sinatra'
end
```

## Instrumentation options

The Sinatra instrumentation supports several configuration options:

<table>
<thead>
  <tr>
    <th>
      Option
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        record_frontend_span
      </code>
    </td>
    
    <td>
      Create a separate span for Rack request processing
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
</tbody>
</table>

Example with options:

```ruby
OpenTelemetry::SDK.configure do |c|
  c.use 'OpenTelemetry::Instrumentation::Sinatra', {
    record_frontend_span: true
  }
end
```

## Creating custom spans

Add custom spans around specific operations in your routes:

```ruby
require 'sinatra'
require 'opentelemetry/sdk'

tracer = OpenTelemetry.tracer_provider.tracer('my-sinatra-app')

get '/users/:id' do
  user_id = params[:id]

  # Create a custom span for database operation
  user = tracer.in_span('fetch_user', attributes: { 'user.id' => user_id }) do |span|
    result = User.find(user_id)
    span.set_attribute('user.name', result.name) if result
    result
  end

  if user
    content_type :json
    user.to_json
  else
    halt 404, { error: 'User not found' }.to_json
  end
end
```

## Adding attributes to spans

Enrich spans with custom attributes for better observability:

```ruby
require 'sinatra'
require 'opentelemetry/sdk'

get '/orders/:id' do
  order_id = params[:id]

  # Get the current span
  span = OpenTelemetry::Trace.current_span

  # Add custom attributes
  span.set_attribute('order.id', order_id)
  span.set_attribute('order.type', 'standard')

  order = Order.find(order_id)
  if order
    span.set_attribute('order.total', order.total.to_f)
    span.set_attribute('order.items_count', order.items.count)
  end

  content_type :json
  order.to_json
end
```

## Recording errors

Record errors in your routes to mark spans as failed:

```ruby
require 'sinatra'
require 'opentelemetry/sdk'

get '/process/:id' do
  span = OpenTelemetry::Trace.current_span

  begin
    result = process_item(params[:id])
    content_type :json
    result.to_json
  rescue StandardError => e
    # Record the error on the span
    span.record_exception(e)
    span.status = OpenTelemetry::Trace::Status.error(e.message)

    halt 500, { error: e.message }.to_json
  end
end
```

## Global error handling

Set up a global error handler to capture all unhandled exceptions:

```ruby
require 'sinatra'
require 'opentelemetry/sdk'

error do
  span = OpenTelemetry::Trace.current_span
  error = env['sinatra.error']

  span.record_exception(error)
  span.status = OpenTelemetry::Trace::Status.error(error.message)

  content_type :json
  { error: error.message }.to_json
end
```

## Rack middleware integration

Since Sinatra is built on Rack, you can add additional OpenTelemetry Rack instrumentation for lower-level request tracing:

```ruby
require 'sinatra'
require 'opentelemetry/sdk'
require 'opentelemetry/instrumentation/sinatra'
require 'opentelemetry/instrumentation/rack'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'my-sinatra-app'
  c.use 'OpenTelemetry::Instrumentation::Rack'
  c.use 'OpenTelemetry::Instrumentation::Sinatra'
end
```

## Captured span attributes

The Sinatra instrumentation automatically captures:

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
        http.method
      </code>
    </td>
    
    <td>
      HTTP method (GET, POST, etc.)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.route
      </code>
    </td>
    
    <td>
      Matched route pattern
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.target
      </code>
    </td>
    
    <td>
      Request path with query string
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.status_code
      </code>
    </td>
    
    <td>
      HTTP response status code
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.request.method
      </code>
    </td>
    
    <td>
      HTTP request method
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        url.path
      </code>
    </td>
    
    <td>
      URL path
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
        sinatra.template
      </code>
    </td>
    
    <td>
      Rendered template name
    </td>
  </tr>
</tbody>
</table>

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## Modular vs Classic Sinatra

OpenTelemetry works with both Sinatra styles:

### Classic Style

```ruby
require 'sinatra'
require 'opentelemetry/sdk'
require 'opentelemetry/instrumentation/sinatra'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'classic-sinatra-app'
  c.use 'OpenTelemetry::Instrumentation::Sinatra'
end

get '/' do
  'Hello World'
end
```

### Modular Style

```ruby
require 'sinatra/base'
require 'opentelemetry/sdk'
require 'opentelemetry/instrumentation/sinatra'

OpenTelemetry::SDK.configure do |c|
  c.service_name = 'modular-sinatra-app'
  c.use 'OpenTelemetry::Instrumentation::Sinatra'
end

class MyApp < Sinatra::Base
  get '/' do
    'Hello World'
  end
end
```

## FAQ

**What is OpenTelemetry Sinatra instrumentation?** It's a Ruby gem that automatically traces incoming HTTP requests to Sinatra applications, capturing route information, request parameters, and response status codes without requiring manual instrumentation.

**Does it work with both Sinatra classic and modular style?** Yes, the instrumentation works with both Sinatra's classic DSL style and the modular `Sinatra::Base` approach. Configure OpenTelemetry before defining your routes.

**How do I exclude health check endpoints?** Currently, the Sinatra instrumentation doesn't have built-in URL exclusion. You can filter spans at the exporter level or use the Rack instrumentation's filtering capabilities.

**Should I use Sinatra instrumentation with Rack instrumentation?** You can use both together. Rack instrumentation provides lower-level request tracing, while Sinatra instrumentation adds Sinatra-specific context like route patterns and template names. Add both to `c.use` for comprehensive coverage.

**How do I correlate logs with traces?** Use the `opentelemetry-instrumentation-logger` gem or manually inject trace context into your log formatter using `OpenTelemetry::Trace.current_span.context`.

**What Ruby versions are supported?** OpenTelemetry Ruby gems support Ruby 3.0 and later. Check the gem's documentation for the most current version requirements.

**How do I trace background jobs?** For Sidekiq or other background job processors, use their respective OpenTelemetry instrumentation gems (`opentelemetry-instrumentation-sidekiq`, etc.) to trace jobs and maintain context propagation.

## What's next?

With OpenTelemetry Sinatra instrumentation in place, you can monitor request latency, track error rates, and trace requests across your distributed systems.

Next steps to enhance your observability:

- Create custom spans using the [OpenTelemetry Ruby Tracing API](/get/opentelemetry-ruby/tracing)
- Add database instrumentation for ActiveRecord, Sequel, or PG
- Explore [Rails instrumentation](/guides/opentelemetry-rails) for full-featured Ruby applications
- Set up the [OpenTelemetry Collector](/opentelemetry/collector) for production deployments
