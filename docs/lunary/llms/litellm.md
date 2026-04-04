# Source: https://docs.lunary.ai/docs/integrations/litellm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LiteLLM Integration

LiteLLM provides callbacks, making it easy for you to log your completions responses.

## Using Callbacks

First, sign up to get an app ID on the Lunary dashboard.

With these 2 lines of code, you can instantly log your responses across all providers with lunary:

```py  theme={null}
litellm.success_callback = ["lunary"]
litellm.failure_callback = ["lunary"]
```

Complete code

```python  theme={null}
from litellm import completion

## set env variables
os.environ["LUNARY_PUBLIC_KEY"] = "0x0"
# Optional: os.environ["LUNARY_API_URL"] = "self-hosting-url"

os.environ["OPENAI_API_KEY"], os.environ["COHERE_API_KEY"] = "", ""

# set callbacks
litellm.success_callback = ["lunary"]
litellm.failure_callback = ["lunary"]

#openai call
response = completion(
  model="gpt-4o", 
  messages=[{"role": "user", "content": "Hi 👋 - i'm openai"}],
  user="some_user_id",
  metadata={"tags": ["tag1", "tag2"]}
)

#cohere call
response = completion(
  model="command-nightly", 
  messages=[{"role": "user", "content": "Hi 👋 - i'm cohere"}],
  user="some_user_id"
)
```
