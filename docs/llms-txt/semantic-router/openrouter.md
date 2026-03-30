# Source: https://docs.aurelio.ai/semantic-router/client-reference/llms/openrouter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.llms.openrouter

## OpenRouterLLM Objects

```python  theme={null}
class OpenRouterLLM(BaseLLM)
```

LLM for OpenRouter. Requires an OpenRouter API key, see here for more information
[https://openrouter.ai/docs/api-reference/authentication#using-an-api-key](https://openrouter.ai/docs/api-reference/authentication#using-an-api-key)

#### \_\_init\_\_

```python  theme={null}
def __init__(name: Optional[str] = None,
             openrouter_api_key: Optional[str] = None,
             base_url: str = "https://openrouter.ai/api/v1",
             temperature: float = 0.01,
             max_tokens: int = 200)
```

Initialize the OpenRouterLLM.

**Arguments**:

* `name` (`Optional[str]`): The name of the OpenRouter model to use.
* `openrouter_api_key` (`Optional[str]`): The OpenRouter API key.
* `base_url` (`str`): The base URL for the OpenRouter API.
* `temperature` (`float`): The temperature of the LLM.
* `max_tokens` (`int`): The maximum number of tokens to generate.

#### \_\_call\_\_

```python  theme={null}
def __call__(messages: List[Message]) -> str
```

Call the OpenRouterLLM.

**Arguments**:

* `messages` (`List[Message]`): The messages to pass to the OpenRouterLLM.

**Returns**:

`str`: The response from the OpenRouterLLM.


Built with [Mintlify](https://mintlify.com).