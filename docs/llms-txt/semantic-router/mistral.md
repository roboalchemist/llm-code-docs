# Source: https://docs.aurelio.ai/semantic-router/client-reference/llms/mistral.md

# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/mistral.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.mistral

This file contains the MistralEncoder class which is used to encode text using MistralAI

## MistralEncoder Objects

```python  theme={null}
class MistralEncoder(LiteLLMEncoder)
```

Class to encode text using MistralAI. Requires a MistralAI API key from
[https://console.mistral.ai/api-keys/](https://console.mistral.ai/api-keys/)

#### \_\_init\_\_

```python  theme={null}
def __init__(name: str | None = None,
             mistralai_api_key: str | None = None,
             score_threshold: float = 0.4)
```

Initialize the MistralEncoder.

**Arguments**:

* `name` (`str`): The name of the embedding model to use such as "mistral-embed".
* `mistralai_api_key` (`str`): The MistralAI API key.
* `score_threshold`: The score threshold for the embeddings.


Built with [Mintlify](https://mintlify.com).