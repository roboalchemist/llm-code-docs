# Source: https://www.traceloop.com/docs/openllmetry/integrations/elasticsearch-apm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Elasticsearch APM Service

Connect OpenLLMetry to [Elastic APM](https://www.elastic.co/guide/en/apm/guide/current/index.html) to visualize LLM traces in Kibana's native APM interface. This integration uses OpenTelemetry Protocol (OTLP) to route traces from your application through an OpenTelemetry Collector to Elastic APM Server.

<Note>
  This integration requires an OpenTelemetry Collector to route traces between Traceloop OpenLLMetry client and Elastic APM Server.
  Elastic APM Server 8.x+ supports OTLP natively.
</Note>

## Quick Start

<Steps>
  <Step title="Install OpenLLMetry">
    Install the Traceloop SDK alongside your LLM provider client:

    ```bash  theme={null}
    pip install traceloop-sdk openai
    ```
  </Step>

  <Step title="Configure OpenTelemetry Collector">
    Configure your OpenTelemetry Collector to receive traces from OpenLLMetry and forward them to APM Server.

    Create an `otel-collector-config.yaml` file:

    ```yaml  theme={null}
    receivers:
      otlp:
        protocols:
          http:
            endpoint: localhost:4318
          grpc:
            endpoint: localhost:4317

    processors:
      batch:
        timeout: 10s
        send_batch_size: 1024

      memory_limiter:
        check_interval: 1s
        limit_mib: 512

      resource:
        attributes:
          - key: service.name
            action: upsert
            value: your-service-name # Match this to app_name parameter value when calling Traceloop.init()

    exporters:
      # Export to APM Server via OTLP
      otlp/apm:
        endpoint: http://localhost:8200 # APM Server Endpoint
        tls:
          insecure: true # Allow insecure connection from OTEL Collector to APM Server (for demo purposes)
        compression: gzip

      # Logging exporter for debugging (can ignore if not needed)
      logging:
        verbosity: normal # This is the verbosity of the logging
        sampling_initial: 5
        sampling_thereafter: 200

      # Debug exporter to verify trace data
      debug:
        verbosity: detailed
        sampling_initial: 10
        sampling_thereafter: 10

    extensions:
      health_check:
        endpoint: localhost:13133 # Endpoint of OpenTelemetry Collector's health check extension

    service:
      extensions: [health_check] # Enable health check extension

      pipelines:
        traces:
          receivers: [otlp]
          processors: [memory_limiter, batch, resource]
          exporters: [otlp/apm, logging, debug]

        metrics:
          receivers: [otlp]
          processors: [memory_limiter, batch, resource]
          exporters: [otlp/apm, logging]

        logs:
          receivers: [otlp]
          processors: [memory_limiter, batch, resource]
          exporters: [otlp/apm, logging]
    ```

    <Warning>
      In production, enable TLS and use APM Server secret tokens for authentication.
      Set `tls.insecure: false` and configure `headers: Authorization: Bearer <token>`.
    </Warning>
  </Step>

  <Step title="Initialize Traceloop">
    Import and initialize Traceloop before any LLM imports:

    ```python  theme={null}
    from os import getenv

    from traceloop.sdk import Traceloop
    from openai import OpenAI

    # Initialize Traceloop with OTLP endpoint
    Traceloop.init(
        app_name="your-service-name",
        api_endpoint="http://localhost:4318"
    )

    # Traceloop must be initialized before importing the LLM client
    # Traceloop instruments the OpenAI client automatically
    client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

    # Make LLM calls - automatically traced
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    ```

    <Note>
      The `app_name` parameter sets the service name visible in Kibana APM's service list.
    </Note>
  </Step>

  <Step title="View Traces in Kibana">
    Navigate to Kibana's APM interface:

    1. Open Kibana at `http://localhost:5601`
    2. Go to **Observability → APM → Services**
    3. Click on your service name (e.g., `your-service-name`)
    4. View transactions and trace timelines with full LLM metadata

    Each LLM call appears as a span containing:

    * Model name (`gen_ai.request.model`)
    * Token usage (`gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`)
    * Prompts and completions (configurable)
    * Request duration and latency
  </Step>
</Steps>

## Environment Variables

Configure OpenLLMetry behavior using environment variables:

| Variable                  | Description                      | Default                 |
| ------------------------- | -------------------------------- | ----------------------- |
| `TRACELOOP_BASE_URL`      | OpenTelemetry Collector endpoint | `http://localhost:4318` |
| `TRACELOOP_TRACE_CONTENT` | Capture prompts/completions      | `true`                  |

<Warning>
  Set `TRACELOOP_TRACE_CONTENT=false` in production to prevent logging sensitive prompt content.
</Warning>

## Using Workflow Decorators

For complex applications with multiple steps, use workflow decorators to create hierarchical traces:

```python  theme={null}
from os import getenv
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task
from openai import OpenAI

Traceloop.init(
  app_name="recipe-service",
  api_endpoint="http://localhost:4318",
)

# Traceloop must be initialized before importing the LLM client
# Traceloop instruments the OpenAI client automatically
client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

@task(name="generate_recipe")
def generate_recipe(dish: str):
    """LLM call - creates a child span"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a chef."},
            {"role": "user", "content": f"Recipe for {dish}"}
        ]
    )
    return response.choices[0].message.content


@workflow(name="recipe_workflow")
def create_recipe(dish: str, servings: int):
    """Parent workflow - creates the root transaction"""
    recipe = generate_recipe(dish)
    return {"recipe": recipe, "servings": servings}

# Call the workflow
result = create_recipe("pasta carbonara", 4)
```

In Kibana APM, you'll see:

* `recipe_workflow.workflow` as the parent transaction
* `generate_recipe.task` as a child span
* `openai.chat.completions` as the LLM API span with full metadata

## Example Trace Visualization

### Trace View

<Frame>
  <img src="https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm.png?fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=3c80793f031dc7a87e87cdf818495de2" data-og-width="3443" width="3443" data-og-height="1318" height="1318" data-path="img/integrations/elasticsearch-apm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm.png?w=280&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=68771b6ac1b26188ccb5732adb8281b1 280w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm.png?w=560&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=ce20f6272fd048bd636018887b7f5f52 560w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm.png?w=840&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=1cb138720fc31f85a2c6a94d00c0178d 840w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm.png?w=1100&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=6b8f239c1436eb17db0f64e040637dc8 1100w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm.png?w=1650&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=82fd84f1affb46255df961ab43bb964e 1650w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm.png?w=2500&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=d17782cd7e2356e79c2ee733ecf1f165 2500w" />
</Frame>

### Trace Details

<Frame>
  <img src="https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm-trace-details.png?fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=64630899a978784a6dfbb37148ac0531" data-og-width="2066" width="2066" data-og-height="1122" height="1122" data-path="img/integrations/elasticsearch-apm-trace-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm-trace-details.png?w=280&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=ef8c6257a763e91a1d90aa88fbbfefa3 280w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm-trace-details.png?w=560&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=ade727d4a1539c30ebeaa85eeeb39d8b 560w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm-trace-details.png?w=840&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=61c8bd0b1902f2d6fc8a9b26b4273b15 840w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm-trace-details.png?w=1100&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=a75e9a1a411ec7a1c32cacf4e9b32182 1100w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm-trace-details.png?w=1650&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=a8bf49b1cce9db2c7203c93185d1ae3f 1650w, https://mintcdn.com/enrolla/1lszxSzWiDlUFRyz/img/integrations/elasticsearch-apm-trace-details.png?w=2500&fit=max&auto=format&n=1lszxSzWiDlUFRyz&q=85&s=00eae35bd6daa0d0a7fbc8a0a1527034 2500w" />
</Frame>

## Captured Metadata

OpenLLMetry automatically captures these attributes in each LLM span:

**Request Attributes:**

* `gen_ai.request.model` - Model identifier
* `gen_ai.request.temperature` - Sampling temperature
* `gen_ai.system` - Provider name (OpenAI, Anthropic, etc.)

**Response Attributes:**

* `gen_ai.response.model` - Actual model used
* `gen_ai.response.id` - Unique response identifier
* `gen_ai.response.finish_reason` - Completion reason

**Token Usage:**

* `gen_ai.usage.input_tokens` - Input token count
* `gen_ai.usage.output_tokens` - Output token count
* `llm.usage.total_tokens` - Total tokens

**Content (if enabled):**

* `gen_ai.prompt.{N}.content` - Prompt messages
* `gen_ai.completion.{N}.content` - Generated completions

## Production Considerations

<Tabs>
  <Tab title="Content Logging">
    Disable prompt/completion logging in production:

    ```bash  theme={null}
    export TRACELOOP_TRACE_CONTENT=false
    ```

    This prevents sensitive data from being stored in Elasticsearch.
  </Tab>

  <Tab title="Sampling">
    Configure sampling in the OpenTelemetry Collector to reduce trace volume:

    ```yaml  theme={null}
    processors:
      probabilistic_sampler:
        sampling_percentage: 10  # Sample 10% of traces
    ```
  </Tab>

  <Tab title="Security">
    Enable APM Server authentication:

    ```yaml  theme={null}
    exporters:
      otlp/apm:
        endpoint: https://localhost:8200
        headers:
          Authorization: "Bearer <secret-token>"
        tls:
          insecure: false
    ```
  </Tab>
</Tabs>

## Resources

* [Elastic APM Documentation](https://www.elastic.co/docs/solutions/observability/apm)
* [OpenTelemetry Collector Configuration](https://opentelemetry.io/docs/collector/configuration/)
* [Traceloop SDK Configuration](https://www.traceloop.com/docs/openllmetry/configuration)
