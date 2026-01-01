# Source: https://braintrust.dev/docs/integrations/sdk-integrations/traceloop.md

# TraceLoop

[TraceLoop OpenLLMetry](https://www.traceloop.com/docs) is an observability framework for LLM applications. Braintrust integrates with TraceLoop via OpenTelemetry to capture LLM calls, workflows, and application traces.

## Setup

This integration uses Braintrust's [Python SDK OpenTelemetry configuration](/integrations/sdk-integrations/opentelemetry#python-sdk-configuration).

Install Traceloop alongside the Braintrust SDK with OpenTelemetry support and the OpenAI client:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" traceloop openai
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
TRACELOOP_BASE_URL=https://api.braintrust.dev/otel
TRACELOOP_HEADERS="Authorization=Bearer%20<Your API Key>, x-bt-parent=project_id:<Your Project ID>"
```

<Note>
  When setting the bearer token, encode the space between "Bearer" and your API key using `%20`.
</Note>

## Trace with TraceLoop

Initialize TraceLoop and your traces will automatically be sent to the Braintrust project specified in the `x-bt-parent` header:

```python title="traceloop_braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from openai import OpenAI
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow

Traceloop.init(disable_batch=True)
client = OpenAI()

@workflow(name="story")
def run_story_stream(client):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Tell me a short story about LLM evals."}],
    )
    return completion.choices[0].message.content

print(run_story_stream(client))
```

## Resources

* [TraceLoop OpenLLMetry documentation](https://www.traceloop.com/docs)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt