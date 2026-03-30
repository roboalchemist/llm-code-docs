# Source: https://uptrace.dev/raw/get/opentelemetry-ruby.md

# OpenTelemetry Ruby distro for Uptrace

> Step-by-step guide to install and configure OpenTelemetry Ruby SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/ruby-original.svg)This document explains how to configure the OpenTelemetry Ruby SDK to export spans (traces) and metrics to Uptrace using OTLP/HTTP.

## Choose Your Setup Path

### Option A: Quick Start with uptrace-ruby

Best for: Getting started quickly, automatic configuration

[uptrace-ruby](https://github.com/uptrace/uptrace-ruby) is a thin wrapper over [opentelemetry-ruby](https://github.com/open-telemetry/opentelemetry-ruby) that configures the OpenTelemetry SDK to export data to Uptrace. It does not add any new functionality and is provided only for your convenience.

â [Continue below](#quick-start)

### Option B: Direct OTLP Configuration

Best for: Existing OpenTelemetry users, custom exporters, fine-grained control

â [Direct OTLP Setup](/get/opentelemetry-ruby/otlp)

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install uptrace-ruby

Add to `Gemfile`:

```ruby
gem 'uptrace'
```

Or install the gem:

```shell
gem install uptrace
```

### Step 3: Basic Configuration

You can configure the Uptrace client using a [DSN](/get#dsn) (Data Source Name) from the project settings page. Replace `<FIXME>` with your actual Uptrace DSN, and `myservice` with a name that identifies your application.

```ruby
require 'uptrace'

Uptrace.configure_opentelemetry(dsn: '') do |c|
  # DSN can be set via UPTRACE_DSN environment variable
  # Example: export UPTRACE_DSN="https://<project_secret>@uptrace.dev?grpc=4317"

  c.service_name = 'myservice'
  c.service_version = '1.0.0'
end
```

### Step 4: Create Your First Trace

Copy the [code](https://github.com/uptrace/uptrace-ruby/tree/master/example/traces) to `main.rb`:

```ruby
#!/usr/bin/env ruby
# frozen_string_literal: true

require 'rubygems'
require 'bundler/setup'
require 'uptrace'

# Configure OpenTelemetry with sensible defaults.
Uptrace.configure_opentelemetry(dsn: '') do |c|
  c.service_name = 'myservice'
  c.service_version = '1.0.0'

  c.resource = OpenTelemetry::SDK::Resources::Resource.create(
    'deployment.environment' => ENV.fetch('RACK_ENV', 'development')
  )
end

# Ensure spans are flushed even if the program exits unexpectedly.
at_exit { OpenTelemetry.tracer_provider.shutdown }

# Register a tracer (usually stored globally).
TRACER = OpenTelemetry.tracer_provider.tracer('my_app', '0.1.0')

# Example trace with nested spans.
TRACER.in_span('main-operation', kind: :server) do |main_span|
  # Simulate an HTTP request span.
  TRACER.in_span('GET /posts/:id', kind: :client) do |http_span|
    http_span.set_attribute('http.method', 'GET')
    http_span.set_attribute('http.route', '/posts/:id')
    http_span.set_attribute('http.url', 'http://localhost:8080/posts/123')
    http_span.set_attribute('http.status_code', 200)
    http_span.record_exception(ArgumentError.new('Invalid parameter'))
  end

  # Simulate a database query span.
  TRACER.in_span('SELECT posts', kind: :client) do |db_span|
    db_span.set_attribute('db.system', 'mysql')
    db_span.set_attribute('db.statement', 'SELECT * FROM posts LIMIT 100')
  end

  # Print the trace URL (clickable in console).
  puts "Trace URL: #{Uptrace.trace_url(main_span)}"
end
```

### Step 5: Run Your Application

Run the code, replacing `<FIXME>` with your Uptrace DSN:

```shell
$ UPTRACE_DSN="<FIXME>" ruby main.rb
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
        resource
      </code>
    </td>
    
    <td>
      Resource attributes representing an entity that produces telemetry.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        use_all()
      </code>
    </td>
    
    <td>
      Enables all available <a href="https://opentelemetry.io/ecosystem/registry/?language=ruby&component=instrumentation" rel="nofollow">
        auto-instrumentations
      </a>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        use(name, config)
      </code>
    </td>
    
    <td>
      Enables specific instrumentation with optional configuration.
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
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-ruby/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-ruby/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-ruby/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-ruby/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-ruby/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect environment info
    </td>
    
    <td>
      <a href="/get/opentelemetry-ruby/resources">
        Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry Rails](/guides/opentelemetry-rails)
- [OpenTelemetry Sinatra](/guides/opentelemetry-sinatra)
