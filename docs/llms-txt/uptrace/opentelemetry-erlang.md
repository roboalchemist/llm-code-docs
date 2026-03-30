# Source: https://uptrace.dev/raw/get/opentelemetry-erlang.md

# OpenTelemetry Erlang/Elixir for Uptrace

> Step-by-step guide to install and configure OpenTelemetry Erlang/Elixir SDKs, export telemetry to Uptrace, and verify that traces and metrics arrive via OTLP.

![undefined](/devicon/elixir-original.svg)This document explains how to configure the OpenTelemetry Erlang/Elixir SDK to export spans (traces) and metrics to Uptrace using OTLP/gRPC.

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install dependencies

Add the necessary OpenTelemetry packages to your project dependencies:

<code-group>

```elixir [Elixir]
# mix.exs
defp deps do
  [
    {:opentelemetry, "~> 1.3"},
    {:opentelemetry_api, "~> 1.2"},
    {:opentelemetry_exporter, "~> 1.6"}
  ]
end
```

```erlang [Erlang]
%% rebar.config
{deps, [
  {opentelemetry, "~> 1.3"},
  {opentelemetry_api, "~> 1.2"},
  {opentelemetry_exporter, "~> 1.6"}
]}.
```

</code-group>

Run the appropriate command to install dependencies:

```bash
# For Elixir projects
mix deps.get

# For Erlang projects
rebar3 compile
```

### Step 3: Basic Configuration

Configure the OpenTelemetry SDK to export traces to Uptrace. Replace `<YOUR_UPTRACE_DSN>` with your actual Uptrace DSN from the project settings.

<code-group>

```elixir [Elixir]
# config/config.exs or config/runtime.exs
config :opentelemetry,
  span_processor: :batch,
  traces_exporter: :otlp

config :opentelemetry_exporter,
  otlp_protocol: :grpc,
  otlp_compression: :gzip,
  otlp_endpoint: "https://api.uptrace.dev:4317",
  otlp_headers: [{"uptrace-dsn", "<YOUR_UPTRACE_DSN>"}]
```

```erlang [Erlang]
%% sys.config
[
 {opentelemetry,
  [{span_processor, batch},
   {traces_exporter, otlp}]},

 {opentelemetry_exporter,
  [{otlp_protocol, grpc},
   {otlp_compression, gzip},
   {otlp_endpoint, "https://api.uptrace.dev:4317"},
   {otlp_headers, [{"uptrace-dsn", "<YOUR_UPTRACE_DSN>"}]}]}
].
```

</code-group>

### Step 4: Create Your First Trace

Create a simple example to verify the setup:

<code-group>

```elixir [Elixir]
# lib/my_app/example.ex
defmodule MyApp.Example do
  require OpenTelemetry.Tracer

  def main do
    # Create a tracer
    OpenTelemetry.Tracer.with_span "main-operation" do
      OpenTelemetry.Tracer.set_attribute("user.id", "12345")

      # Create a child span
      OpenTelemetry.Tracer.with_span "child-operation" do
        OpenTelemetry.Tracer.set_attributes(%{
          "http.method" => "GET",
          "http.url" => "http://localhost:8080/api/users"
        })

        # Simulate some work
        :timer.sleep(100)
      end
    end

    IO.puts("Trace sent to Uptrace!")
  end
end
```

```erlang [Erlang]
%% src/my_app_example.erl
-module(my_app_example).
-export([main/0]).
-include_lib("opentelemetry_api/include/otel_tracer.hrl").

main() ->
    ?with_span(<<"main-operation">>, #{}, fun() ->
        ?set_attribute(<<"user.id">>, <<"12345">>),

        ?with_span(<<"child-operation">>, #{}, fun() ->
            ?set_attributes([
                {<<"http.method">>, <<"GET">>},
                {<<"http.url">>, <<"http://localhost:8080/api/users">>}
            ]),

            %% Simulate some work
            timer:sleep(100)
        end)
    end),

    io:format("Trace sent to Uptrace!~n").
```

</code-group>

### Step 5: Run Your Application

Run the code with your Uptrace DSN set:

```bash
# For Elixir
UPTRACE_DSN="<FIXME>" mix run -e "MyApp.Example.main()"

# For Erlang
UPTRACE_DSN="<FIXME>" rebar3 shell -s my_app_example main
```

### Step 6: View Your Trace

Open the Uptrace dashboard to view your trace. You should see the `main-operation` span with the `child-operation` nested inside it.

![Basic trace](/get/basic-trace.png)

## Environment Variables

You can also configure OpenTelemetry using environment variables, which is useful for containerized deployments:

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.uptrace.dev:4317"
export OTEL_EXPORTER_OTLP_PROTOCOL="grpc"
export OTEL_EXPORTER_OTLP_COMPRESSION="gzip"
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<YOUR_UPTRACE_DSN>"
```

For more configuration options, see the [OTLP Exporter Configuration](/get/opentelemetry-erlang/otlp) guide.

## Configuration Options

The following configuration options are available for the OpenTelemetry Erlang/Elixir SDK:

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
        span_processor
      </code>
    </td>
    
    <td>
      Span processor type: <code>
        :batch
      </code>
      
       (recommended) or <code>
        :simple
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        traces_exporter
      </code>
    </td>
    
    <td>
      Traces exporter: <code>
        :otlp
      </code>
      
       for OTLP, <code>
        {:otel_exporter_stdout, []}
      </code>
      
       for stdout
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otlp_protocol
      </code>
    </td>
    
    <td>
      OTLP protocol: <code>
        :grpc
      </code>
      
       (recommended) or <code>
        :http_protobuf
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otlp_endpoint
      </code>
    </td>
    
    <td>
      OTLP endpoint URL. For Uptrace: <code>
        https://api.uptrace.dev:4317
      </code>
      
       (gRPC) or <code>
        https://api.uptrace.dev
      </code>
      
       (HTTP)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otlp_compression
      </code>
    </td>
    
    <td>
      Compression: <code>
        :gzip
      </code>
      
       (recommended) or <code>
        :none
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otlp_headers
      </code>
    </td>
    
    <td>
      List of headers to include with each request. Include <code>
        {"uptrace-dsn", "<YOUR_DSN>"}
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resource
      </code>
    </td>
    
    <td>
      Map of <a href="/get/opentelemetry-erlang/resources">
        resource attributes
      </a>
      
       like <code>
        service.name
      </code>
      
       and <code>
        deployment.environment
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        sampler
      </code>
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/sampling">
        Sampling
      </a>
      
       configuration to control trace collection rate
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resource_detectors
      </code>
    </td>
    
    <td>
      List of <a href="/get/opentelemetry-erlang/resources">
        resource detectors
      </a>
      
       to automatically detect environment info
    </td>
  </tr>
</tbody>
</table>

## Application Configuration

Configure OpenTelemetry to start as a temporary application to prevent crashes from affecting your main application:

<code-group>

```elixir [Elixir]
# mix.exs
def project do
  [
    app: :my_app,
    # ... other config
    releases: [
      my_app: [
        applications: [opentelemetry: :temporary]
      ]
    ]
  ]
end
```

```erlang [Erlang]
%% rebar.config
{relx, [
  {release, {my_app, "0.1.0"}, [
    {opentelemetry, temporary},
    my_app
  ]}
]}.
```

</code-group>

This ensures that if OpenTelemetry terminates, your main application continues running.

## Phoenix Framework Integration

To instrument Phoenix applications, add the Phoenix instrumentation library:

```elixir
# mix.exs
defp deps do
  [
    # ... existing deps
    {:opentelemetry_phoenix, "~> 1.1"},
    {:opentelemetry_cowboy, "~> 0.2"},
    {:opentelemetry_ecto, "~> 1.2"}  # For database instrumentation
  ]
end
```

Configure Phoenix instrumentation in your application start function:

```elixir
# lib/my_app/application.ex
def start(_type, _args) do
  # Setup instrumentation before starting supervision tree
  :opentelemetry_cowboy.setup()
  OpentelemetryPhoenix.setup(adapter: :cowboy2)
  OpentelemetryEcto.setup([:my_app, :repo])

  children = [
    MyApp.Repo,
    {Phoenix.PubSub, name: MyApp.PubSub},
    MyAppWeb.Endpoint
  ]

  opts = [strategy: :one_for_one, name: MyApp.Supervisor]
  Supervisor.start_link(children, opts)
end
```

This provides automatic instrumentation for HTTP requests, database queries, and Phoenix channels.

## Troubleshooting

If traces don't appear in Uptrace:

1. **Verify DSN**: Double-check your Uptrace DSN in the configuration
2. **Check connectivity**: Ensure your application can reach `https://api.uptrace.dev:4317`
3. **Review logs**: Look for OpenTelemetry error messages in your application logs
4. **Test configuration**: Use the stdout exporter for local testing:

```elixir
# config/dev.exs
config :opentelemetry,
  traces_exporter: {:otel_exporter_stdout, []}
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
      Configure OTLP exporter
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/otlp">
        OTLP Exporter
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/resources">
        Resource detectors
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-erlang/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry Phoenix](https://hexdocs.pm/opentelemetry_phoenix/readme.html)
- [OpenTelemetry Cowboy](https://github.com/open-telemetry/opentelemetry-erlang-contrib/tree/main/instrumentation/opentelemetry_cowboy)
- [OpenTelemetry Ecto](https://hexdocs.pm/opentelemetry_ecto/readme.html)
