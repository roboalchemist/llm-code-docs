# Source: https://docs.lunary.ai/docs/integrations/opentelemetry/otel-python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending OTEL Traces from Python

> How to use OpenTelemetry Python SDK to export traces to Lunary.

# Exporting OpenTelemetry Traces from Python

You can send traces from any Python application or framework to Lunary using the standard OpenTelemetry SDK.

## 1. Install Dependencies

```sh  theme={null}
pip install opentelemetry-sdk opentelemetry-exporter-otlp
```

## 2. Configure Your Environment

Set your Lunary API key and endpoint as OTEL environment variables:

```sh  theme={null}
import os

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://api.lunary.ai/v1/otel"
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Bearer {os.environ['LUNARY_PUBLIC_KEY']}"
```

## 3. Set up OTEL Tracing

```python  theme={null}
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

exporter = OTLPSpanExporter()
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(exporter))
```

## 4. Emit Traces

You can now add spans to your code:

```python  theme={null}
with tracer.start_as_current_span("My LLM Call") as span:
    # Attach GenAI-related context
    span.set_attribute("gen_ai.request.model", "gpt-4.1")
    span.set_attribute("gen_ai.prompt.0.content", "Hello, LLM world!")
    span.set_attribute("gen_ai.usage.prompt_tokens", 25)
    # Call your LLM/model here
```

## Advanced: Custom Attributes

You can tag spans for sessions, users, or experiments:

```python  theme={null}
span.set_attribute("lunary.user.id", "user-123")
span.set_attribute("lunary.tags", ["my-experiment", "beta"])
```
