# Source: https://uptrace.dev/raw/get/opentelemetry-erlang/propagation.md

# OpenTelemetry Context Propagation in Erlang/Elixir

> Learn how to implement context propagation for distributed tracing in Erlang/Elixir OpenTelemetry applications.

![undefined](/devicon/elixir-original.svg)This guide covers Erlang/Elixir-specific implementation of context propagation. For a comprehensive overview of context propagation concepts, W3C TraceContext, propagators, and troubleshooting, see the [OpenTelemetry Context Propagation](/opentelemetry/context-propagation) guide.

Most context propagation in Erlang/Elixir applications is handled automatically by instrumentation libraries like [OpenTelemetry Phoenix](https://github.com/opentelemetry-beam/opentelemetry_phoenix), [OpenTelemetry Cowboy](https://github.com/open-telemetry/opentelemetry-erlang-contrib/tree/main/instrumentation/opentelemetry_cowboy), and HTTP client libraries. These libraries automatically extract and inject W3C Trace Context headers including `traceparent` for distributed tracing.

However, there are scenarios where manual context propagation is necessary, such as custom protocols, message queues, or when working with unsupported HTTP libraries. This guide covers manual handling of `traceparent` headers for distributed tracing.

## TraceParent header format

The `traceparent` header follows the W3C Trace Context specification:

```text
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

Format breakdown:

- `00` - Version (currently always "00")
- `4bf92f3577b34da6a3ce929d0e0e4736` - Trace ID (32 hex characters)
- `00f067aa0ba902b7` - Parent Span ID (16 hex characters)
- `01` - Trace flags (8-bit field, "01" = sampled)

## Manual context extraction

Extract trace context from incoming requests when automatic instrumentation isn't available:

### Elixir manual extraction

```elixir
defmodule MyApp.TraceContext do
  def extract_from_headers(headers) when is_map(headers) do
    headers_list = Enum.map(headers, fn {k, v} -> {String.downcase(k), v} end)
    :otel_propagator_text_map.extract(headers_list)
  end

  def extract_from_headers(headers) when is_list(headers) do
    # Normalize header names to lowercase
    normalized_headers = Enum.map(headers, fn
      {key, value} when is_binary(key) -> {String.downcase(key), value}
      {key, value} when is_atom(key) -> {Atom.to_string(key) |> String.downcase(), value}
    end)

    :otel_propagator_text_map.extract(normalized_headers)
  end
end

# Usage in a custom HTTP handler
defmodule MyApp.CustomHandler do
  require OpenTelemetry.Tracer

  def handle_request(headers, body) do
    # Extract context from headers
    MyApp.TraceContext.extract_from_headers(headers)

    # Now any spans created will be part of the distributed trace
    OpenTelemetry.Tracer.with_span "custom_request_handler" do
      OpenTelemetry.Tracer.set_attribute("request.body_size", byte_size(body))

      # Process the request
      process_request(body)
    end
  end

  defp process_request(body) do
    # Your business logic here
    Jason.decode(body)
  end
end
```

### Erlang manual extraction

```erlang
-module(trace_context).
-export([extract_from_headers/1]).
-include_lib("opentelemetry_api/include/otel_tracer.hrl").

extract_from_headers(Headers) when is_list(Headers) ->
    % Normalize headers to lowercase
    NormalizedHeaders = lists:map(fun({Key, Value}) ->
        NormalizedKey = case Key of
            K when is_binary(K) -> string:lowercase(binary_to_list(K));
            K when is_list(K) -> string:lowercase(K);
            K when is_atom(K) -> string:lowercase(atom_to_list(K))
        end,
        {list_to_binary(NormalizedKey), Value}
    end, Headers),

    otel_propagator_text_map:extract(NormalizedHeaders).

% Usage in custom handler
handle_request(Headers, Body) ->
    % Extract context from headers
    trace_context:extract_from_headers(Headers),

    % Create span as part of distributed trace
    ?with_span(<<"custom_request_handler">>, #{}, fun() ->
        ?set_attribute(<<"request.body_size">>, byte_size(Body)),

        % Process the request
        process_request(Body)
    end).

process_request(Body) ->
    % Your business logic here
    jsx:decode(Body).
```

## Manual context injection

Inject trace context into outgoing requests when automatic instrumentation isn't available:

### Elixir manual injection

```elixir
defmodule MyApp.CustomHTTPClient do
  def make_request(url, body) do
    # Prepare headers map for injection
    headers = %{}

    # Inject current trace context
    injected_headers = :otel_propagator_text_map.inject(headers)

    # Convert to format expected by HTTP client
    header_list = Enum.map(injected_headers, fn {k, v} -> {k, v} end)

    # Make HTTP request with injected headers
    case :httpc.request(:post, {url, header_list, "application/json", body}, [], []) do
      {:ok, {{_Version, 200, _ReasonPhrase}, _Headers, ResponseBody}} ->
        {:ok, ResponseBody}
      {:ok, {{_Version, StatusCode, _ReasonPhrase}, _Headers, _Body}} ->
        {:error, {:http_error, StatusCode}}
      {:error, Reason} ->
        {:error, Reason}
    end
  end
end

# Usage with custom span
defmodule MyApp.ExternalService do
  require OpenTelemetry.Tracer

  def send_data(data) do
    OpenTelemetry.Tracer.with_span "external_service_call" do
      OpenTelemetry.Tracer.set_attributes(%{
        "service.name" => "external_api",
        "http.method" => "POST",
        "data.size" => byte_size(data)
      })

      case MyApp.CustomHTTPClient.make_request("https://api.example.com/data", data) do
        {:ok, response} ->
          OpenTelemetry.Tracer.set_attribute("http.status_code", 200)
          {:ok, response}
        {:error, reason} ->
          OpenTelemetry.Tracer.set_status(:error, "External service call failed")
          OpenTelemetry.Tracer.set_attribute("error.type", "http_error")
          {:error, reason}
      end
    end
  end
end
```

### Erlang manual injection

```erlang
-module(custom_http_client).
-export([make_request/2]).

make_request(Url, Body) ->
    % Prepare headers for injection
    Headers = #{},

    % Inject current trace context
    InjectedHeaders = otel_propagator_text_map:inject(Headers),

    % Convert to list format for httpc
    HeaderList = maps:fold(fun(K, V, Acc) ->
        [{binary_to_list(K), binary_to_list(V)} | Acc]
    end, [], InjectedHeaders),

    % Make HTTP request with injected headers
    case httpc:request(post, {Url, HeaderList, "application/json", Body}, [], []) of
        {ok, {{_Version, 200, _ReasonPhrase}, _ResponseHeaders, ResponseBody}} ->
            {ok, ResponseBody};
        {ok, {{_Version, StatusCode, _ReasonPhrase}, _ResponseHeaders, _Body}} ->
            {error, {http_error, StatusCode}};
        {error, Reason} ->
            {error, Reason}
    end.

% Usage with custom span
-module(external_service).
-export([send_data/1]).
-include_lib("opentelemetry_api/include/otel_tracer.hrl").

send_data(Data) ->
    ?with_span(<<"external_service_call">>, #{}, fun() ->
        ?set_attribute(<<"service.name">>, <<"external_api">>),
        ?set_attribute(<<"http.method">>, <<"POST">>),
        ?set_attribute(<<"data.size">>, byte_size(Data)),

        case custom_http_client:make_request("https://api.example.com/data", Data) of
            {ok, Response} ->
                ?set_attribute(<<"http.status_code">>, 200),
                {ok, Response};
            {error, Reason} ->
                ?set_status(?OTEL_STATUS_ERROR, <<"External service call failed">>),
                ?set_attribute(<<"error.type">>, <<"http_error">>),
                {error, Reason}
        end
    end).
```

## Message queue propagation

Propagate trace context through message queues for distributed tracing:

### Elixir with RabbitMQ

```elixir
defmodule MyApp.MessageProducer do
  def publish_message(queue, message) do
    # Inject trace context into message headers
    headers = :otel_propagator_text_map.inject(%{})

    # Convert headers for AMQP
    amqp_headers = Enum.map(headers, fn {k, v} -> {k, :longstr, v} end)

    # Publish message with trace context
    AMQP.Basic.publish(
      MyApp.RabbitMQ.channel(),
      "",
      queue,
      Jason.encode!(message),
      headers: amqp_headers
    )
  end
end

defmodule MyApp.MessageConsumer do
  require OpenTelemetry.Tracer

  def handle_message(payload, meta) do
    # Extract trace context from message headers
    headers = case meta.headers do
      :undefined -> %{}
      header_list ->
        Enum.reduce(header_list, %{}, fn {key, _type, value}, acc ->
          Map.put(acc, key, value)
        end)
    end

    # Extract context and make it current
    :otel_propagator_text_map.extract(headers)

    # Process message within distributed trace
    OpenTelemetry.Tracer.with_span "message_consumer" do
      OpenTelemetry.Tracer.set_attributes(%{
        "messaging.system" => "rabbitmq",
        "messaging.destination" => meta.routing_key,
        "messaging.message_payload_size_bytes" => byte_size(payload)
      })

      case Jason.decode(payload) do
        {:ok, message} ->
          process_message(message)
        {:error, reason} ->
          OpenTelemetry.Tracer.set_status(:error, "Message decode failed")
          {:error, reason}
      end
    end
  end

  defp process_message(message) do
    # Your message processing logic
    IO.inspect(message, label: "Processing message")
  end
end
```

## Custom protocol propagation

Propagate context over custom protocols:

### Elixir GenServer with context

```elixir
defmodule MyApp.WorkerPool do
  use GenServer
  require OpenTelemetry.Tracer

  def submit_work(pid, work_data) do
    # Inject current trace context
    trace_headers = :otel_propagator_text_map.inject(%{})

    # Send work with trace context
    GenServer.call(pid, {:submit_work, work_data, trace_headers})
  end

  def handle_call({:submit_work, work_data, trace_headers}, _from, state) do
    # Extract trace context from headers
    :otel_propagator_text_map.extract(trace_headers)

    # Process work within distributed trace
    result = OpenTelemetry.Tracer.with_span "worker_process" do
      OpenTelemetry.Tracer.set_attributes(%{
        "worker.pid" => inspect(self()),
        "work.type" => work_data.type,
        "work.priority" => work_data.priority
      })

      # Simulate work processing
      :timer.sleep(100)

      OpenTelemetry.Tracer.add_event("work.completed", %{
        "work.id" => work_data.id
      })

      {:ok, "Work completed"}
    end

    {:reply, result, state}
  end
end
```

## Debugging trace propagation

Debug and validate trace context propagation:

### Elixir debugging utilities

```elixir
defmodule MyApp.TraceDebugger do
  require Logger

  def debug_current_context do
    span_ctx = OpenTelemetry.Tracer.current_span_ctx()

    if OpenTelemetry.Span.is_valid(span_ctx) do
      trace_id = OpenTelemetry.Span.trace_id(span_ctx)
      span_id = OpenTelemetry.Span.span_id(span_ctx)
      trace_flags = OpenTelemetry.Span.trace_flags(span_ctx)

      # Format as traceparent header
      traceparent = "00-#{trace_id}-#{span_id}-#{String.pad_leading(Integer.to_string(trace_flags, 16), 2, "0")}"

      Logger.info("Current trace context - TraceParent: #{traceparent}")

      %{
        trace_id: trace_id,
        span_id: span_id,
        trace_flags: trace_flags,
        traceparent: traceparent,
        valid: true
      }
    else
      Logger.warning("No valid trace context found")
      %{valid: false}
    end
  end

  def debug_headers(headers) do
    traceparent = case Map.get(headers, "traceparent") do
      nil -> "Not found"
      value -> value
    end

    tracestate = case Map.get(headers, "tracestate") do
      nil -> "Not found"
      value -> value
    end

    Logger.info("Header debug - TraceparentHeader: #{traceparent}, Tracestate: #{tracestate}")

    %{
      traceparent: traceparent,
      tracestate: tracestate
    }
  end
end

# Usage in debugging
defmodule MyApp.DebugController do
  def debug_action(conn, _params) do
    # Debug incoming headers
    headers = Enum.into(conn.req_headers, %{})
    MyApp.TraceDebugger.debug_headers(headers)

    # Debug current context
    MyApp.TraceDebugger.debug_current_context()

    json(conn, %{status: "debug_complete"})
  end
end
```

## What's next?

- [Get started](/get/opentelemetry-erlang)
- [Configure OTLP Exporter](/get/opentelemetry-erlang/otlp)
- [Learn about OpenTelemetry Erlang/Elixir Tracing API](/get/opentelemetry-erlang/tracing)
- [Learn about OpenTelemetry Erlang/Elixir Logs](/get/opentelemetry-erlang/logs)
- [Learn about OpenTelemetry Erlang/Elixir Resource detectors](/get/opentelemetry-erlang/resources)
- [Learn about OpenTelemetry Erlang/Elixir Sampling](/get/opentelemetry-erlang/sampling)
