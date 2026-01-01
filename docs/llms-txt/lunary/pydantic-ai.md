# Source: https://docs.lunary.ai/docs/integrations/pydantic-ai.md

# Pydantic AI Integration

<Warning>
  This integration is currently in beta. If you encounter any issues or unexpected behavior, please reach out for feedback and support.
</Warning>

Lunary supports Pydantic AI through OpenTelemetry instrumentation via Logfire.

To integrate Pydantic AI with Lunary, you only need to configure the OpenTelemetry exporter and instrument Pydantic AI:

```python  theme={null}
os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://api.lunary.ai" # replace by your api endpoint if you're self-hosting Lunary
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Bearer {os.environ['LUNARY_PRIVATE_KEY']}"

logfire.configure(send_to_logfire=False)
logfire.instrument_pydantic_ai()
```

## Full Example

Here's a complete example showing how to use Pydantic AI with Lunary:

```python  theme={null}
import os
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://api.lunary.ai"
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Bearer {os.environ['LUNARY_PRIVATE_KEY']}"

logfire.configure(send_to_logfire=False)
logfire.instrument_pydantic_ai()


class MyModel(BaseModel):
    city: str
    country: str

agent = Agent(model='open:gpt-4.1', output_type=MyModel, model_settings={'temperature': 0.7})

if __name__ == '__main__':
    result = agent.run_sync('The windy city in the US of A.')
    print(result.output)
```

This will automatically track:

* Agent calls and responses
* Model parameters and settings
* Output schema validation
* Performance metrics
* Errors and exceptions

All telemetry data will be sent to Lunary for monitoring and analysis.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt