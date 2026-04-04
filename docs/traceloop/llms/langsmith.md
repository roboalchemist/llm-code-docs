# Source: https://www.traceloop.com/docs/openllmetry/integrations/langsmith.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with LangSmith and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/langsmith.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c348394b2956c4b5c17846094c722089" data-og-width="2814" width="2814" data-og-height="1796" height="1796" data-path="img/integrations/langsmith.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/langsmith.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=84a003a365a8c346661f9361640d8df4 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/langsmith.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=61e0561feb6eb8e28cb280c1d1a28236 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/langsmith.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=805e709d01fcb7d7ee050127e6719ba9 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/langsmith.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=95f6615f98164d0a9e7290d0eeabb8f6 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/langsmith.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=abac893003c0b703efa5626e01928c56 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/langsmith.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6fdfbb15950c0dbaf6043f1f7f916dd3 2500w" />
</Frame>

LangSmith is an [all-in-one developer platform](https://www.langchain.com/langsmith) for every step of the LLM-powered application lifecycle.

LangSmith supports ingesting traces using OpenTelemetry / OpenLLMetry format. For more details, see [LangSmith's OpenTelemetry documentation](https://docs.smith.langchain.com/observability/how_to_guides/tracing/trace_with_opentelemetry).

### To Log Traces to Langsmith

Signup for LangSmith and create an API Key. Then setup your environment variables:

```bash  theme={null}
TRACELOOP_BASE_URL=https://api.smith.langchain.com/otel
TRACELOOP_HEADERS="x-api-key=<LANGSMITH_API_KEY>"
```

You can then log traces with OpenLLMetry to LangSmith, here is an example:

```python  theme={null}
from openai import OpenAI
from traceloop.sdk import Traceloop

client = OpenAI()
Traceloop.init()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
```
