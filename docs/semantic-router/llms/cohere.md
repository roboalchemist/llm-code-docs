# Source: https://docs.aurelio.ai/semantic-router/client-reference/llms/cohere.md

# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/cohere.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.cohere

## CohereEncoder Objects

```python  theme={null}
class CohereEncoder(LiteLLMEncoder)
```

Dense encoder that uses Cohere API to embed documents. Supports text only. Requires
a Cohere API key from [https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys).

#### \_\_init\_\_

```python  theme={null}
def __init__(name: str | None = None,
             cohere_api_key: str | None = None,
             score_threshold: float = 0.3)
```

Initialize the Cohere encoder.

**Arguments**:

* `name` (`str`): The name of the embedding model to use such as "embed-english-v3.0" or
  "embed-multilingual-v3.0".
* `cohere_api_key` (`str`): The API key for the Cohere client, can also
  be set via the COHERE\_API\_KEY environment variable.
* `score_threshold` (`float`): The threshold for the score of the embedding.


Built with [Mintlify](https://mintlify.com).