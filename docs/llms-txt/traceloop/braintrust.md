# Source: https://www.traceloop.com/docs/openllmetry/integrations/braintrust.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Braintrust and OpenLLMetry

To set up Braintrust as an [OpenTelemetry](https://opentelemetry.io/docs/) backend, you'll need to route the traces to Braintrust's OpenTelemetry endpoint, set your API key, and specify a parent project or experiment. Braintrust supports common patterns from [OpenLLLMetry](https://github.com/traceloop/openllmetry).

For more information, see the [Braintrust documentation](https://www.braintrust.dev/docs/guides/tracing#traceloop).

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/braintrust.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=85e32a38e296f84fbbca8645e3e33c44" data-og-width="2412" width="2412" data-og-height="1558" height="1558" data-path="img/integrations/braintrust.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/braintrust.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f681f888cc11d2e8f7643d167e87785b 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/braintrust.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=905ace05bcc10e82a69a9bb6f424d398 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/braintrust.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=536395e1fac5fd7977cc1911102ab1b0 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/braintrust.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=090a00b2ba77020aa410654709589dc2 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/braintrust.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=fce0010fab1ba9b20e0441bc583bb00e 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/braintrust.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ed2e1af9091d951eac330544a27bcfdd 2500w" />
</Frame>

To export OTel traces from Traceloop OpenLLMetry to Braintrust, set the following environment variables:

```bash  theme={null}
TRACELOOP_BASE_URL=https://api.braintrust.dev/otel
TRACELOOP_HEADERS="Authorization=Bearer%20<Your API Key>, x-bt-parent=project_id:<Your Project ID>"
```

Note: When setting the bearer token, make sure to URL encode the space between "Bearer" and your API key using `%20`. For example:

```bash  theme={null}
# Incorrect format
TRACELOOP_HEADERS="Authorization=Bearer sk-RiPodT20anlA1d3ki4T5I0V24WHXFuwvlPivUUoUGOnczOVI, x-bt-parent=project_id:<Your Project ID>"

# Correct format
TRACELOOP_HEADERS="Authorization=Bearer%20sk-RiPodT20anlA1d3ki4T5I0V24WHXFuwvlPivUUoUGOnczOVI, x-bt-parent=project_id:<Your Project ID>"
```

Important: The project ID is not the same as your project name. To find your project ID:

1. Navigate to your project configuration page at: `https://www.braintrust.dev/app/ORG_NAME/p/PROJECT_NAME/configuration`
2. Scroll to the bottom of the page
3. Look for the "Copy Project ID" button to get the correct ID for the `x-bt-parent` header

Traces will then appear under the Braintrust project or experiment provided in the `x-bt-parent` header.

```python  theme={null}
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
