# Source: https://docs.vllm.ai/en/stable/examples/online_serving/opentelemetry/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/opentelemetry.md "Edit this page")

# Setup OpenTelemetry POC[¶](#setup-opentelemetry-poc "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/online_serving/opentelemetry>.

1.  Install OpenTelemetry packages:

    ::: 
        pip install \
          'opentelemetry-sdk>=1.26.0,<1.27.0' \
          'opentelemetry-api>=1.26.0,<1.27.0' \
          'opentelemetry-exporter-otlp>=1.26.0,<1.27.0' \
          'opentelemetry-semantic-conventions-ai>=0.4.1,<0.5.0'
    :::

2.  Start Jaeger in a docker container:

    ::: 
        # From: https://www.jaegertracing.io/docs/1.57/getting-started/
        docker run --rm --name jaeger \
            -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
            -p 6831:6831/udp \
            -p 6832:6832/udp \
            -p 5778:5778 \
            -p 16686:16686 \
            -p 4317:4317 \
            -p 4318:4318 \
            -p 14250:14250 \
            -p 14268:14268 \
            -p 14269:14269 \
            -p 9411:9411 \
            jaegertracing/all-in-one:1.57
    :::

3.  In a new shell, export Jaeger IP:

    ::: 
        export JAEGER_IP=$(docker inspect   --format '}' jaeger)
        export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=grpc://$JAEGER_IP:4317
    :::

    Then set vLLM\'s service name for OpenTelemetry, enable insecure connections to Jaeger and run vLLM:

    ::: 
        export OTEL_SERVICE_NAME="vllm-server"
        export OTEL_EXPORTER_OTLP_TRACES_INSECURE=true
        vllm serve facebook/opt-125m --otlp-traces-endpoint="$OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"
    :::

4.  In a new shell, send requests with trace context from a dummy client

    ::: 
        export JAEGER_IP=$(docker inspect --format '}' jaeger)
        export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=grpc://$JAEGER_IP:4317
        export OTEL_EXPORTER_OTLP_TRACES_INSECURE=true
        export OTEL_SERVICE_NAME="client-service"
        python dummy_client.py
    :::

5.  Open Jaeger webui: <http://localhost:16686/>

    In the search pane, select `vllm-server` service and hit `Find Traces`. You should get a list of traces, one for each request. [![Traces](https://i.imgur.com/GYHhFjo.png)](https://i.imgur.com/GYHhFjo.png)

6.  Clicking on a trace will show its spans and their tags. In this demo, each trace has 2 spans. One from the dummy client containing the prompt text and one from vLLM containing metadata about the request. [![Spans details](https://i.imgur.com/OPf6CBL.png)](https://i.imgur.com/OPf6CBL.png)

## Exporter Protocol[¶](#exporter-protocol "Permanent link")

OpenTelemetry supports either `grpc` or `http/protobuf` as the transport protocol for trace data in the exporter. By default, `grpc` is used. To set `http/protobuf` as the protocol, configure the `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` environment variable as follows:

    export OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
    export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://$JAEGER_IP:4318/v1/traces
    vllm serve facebook/opt-125m --otlp-traces-endpoint="$OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"

## Instrumentation of FastAPI[¶](#instrumentation-of-fastapi "Permanent link")

OpenTelemetry allows automatic instrumentation of FastAPI.

1.  Install the instrumentation library

    ::: 
        pip install opentelemetry-instrumentation-fastapi
    :::

2.  Run vLLM with `opentelemetry-instrument`

    ::: 
        opentelemetry-instrument vllm serve facebook/opt-125m
    :::

3.  Send a request to vLLM and find its trace in Jaeger. It should contain spans from FastAPI.

[![FastAPI Spans](https://i.imgur.com/hywvoOJ.png)](https://i.imgur.com/hywvoOJ.png)

## Example materials[¶](#example-materials "Permanent link")

dummy_client.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    import requests
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
    from opentelemetry.trace import SpanKind, set_tracer_provider
    from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

    trace_provider = TracerProvider()
    set_tracer_provider(trace_provider)

    trace_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    trace_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

    tracer = trace_provider.get_tracer("dummy-client")

    url = "http://localhost:8000/v1/completions"
    with tracer.start_as_current_span("client-span", kind=SpanKind.CLIENT) as span:
        prompt = "San Francisco is a"
        span.set_attribute("prompt", prompt)
        headers = 
        TraceContextTextMapPropagator().inject(headers)
        payload = 
        response = requests.post(url, headers=headers, json=payload)