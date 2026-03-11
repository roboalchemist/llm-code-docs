# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/jina.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.jina

This file contains the JinaEncoder class which is used to encode text using Jina

## JinaEncoder Objects

```python  theme={null}
class JinaEncoder(LiteLLMEncoder)
```

Class to encode text using Jina. Requires a Jina API key from
[https://jina.ai/api-keys/](https://jina.ai/api-keys/)

#### \_\_init\_\_

```python  theme={null}
def __init__(name: str | None = None,
             api_key: str | None = None,
             score_threshold: float = 0.4)
```

Initialize the JinaEncoder.

**Arguments**:

* `name`: The name of the embedding model to use such as "jina-embeddings-v3".
* `jina_api_key` (`str`): The Jina API key.


Built with [Mintlify](https://mintlify.com).