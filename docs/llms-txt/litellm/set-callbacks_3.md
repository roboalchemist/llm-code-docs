# set callbacks
litellm.success_callback=["helicone"]

#openai call
response = completion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hi 👋 - i'm openai"}])

#cohere call
response = completion(model="command-nightly", messages=[{"role": "user", "content": "Hi 👋 - i'm cohere"}])

```

### Approach 2: \[OpenAI + Azure only\] Use Helicone as a proxy [​](https://docs.litellm.ai/observability/helicone_integration\#approach-2-openai--azure-only-use-helicone-as-a-proxy "Direct link to approach-2-openai--azure-only-use-helicone-as-a-proxy")

Helicone provides advanced functionality like caching, etc. Helicone currently supports this for Azure and OpenAI.

If you want to use Helicone to proxy your OpenAI/Azure requests, then you can -

- Set helicone as your base url via: `litellm.api_url`
- Pass in helicone request headers via: `litellm.headers`

Complete Code

```codeBlockLines_e6Vv
import litellm
from litellm import completion

litellm.api_base = "https://oai.hconeai.com/v1"
litellm.headers = {"Helicone-Auth": f"Bearer {os.getenv('HELICONE_API_KEY')}"}

response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "how does a court case get to the Supreme Court?"}]
)

print(response)

```

- [Use Helicone to log requests across all LLM Providers (OpenAI, Azure, Anthropic, Cohere, Replicate, PaLM)](https://docs.litellm.ai/observability/helicone_integration#use-helicone-to-log-requests-across-all-llm-providers-openai-azure-anthropic-cohere-replicate-palm)
  - [Approach 1: Use Callbacks](https://docs.litellm.ai/observability/helicone_integration#approach-1-use-callbacks)
  - [Approach 2: OpenAI + Azure only Use Helicone as a proxy](https://docs.litellm.ai/observability/helicone_integration#approach-2-openai--azure-only-use-helicone-as-a-proxy)

## Supabase Integration Guide
[Skip to main content](https://docs.litellm.ai/observability/supabase_integration#__docusaurus_skipToContent_fallback)