# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/voyage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.voyage

This file contains the VoyageEncoder class which is used to encode text using Voyage

## VoyageEncoder Objects

```python  theme={null}
class VoyageEncoder(LiteLLMEncoder)
```

Class to encode text using Voyage. Requires a Voyage API key from
[https://voyageai.com/api-keys/](https://voyageai.com/api-keys/)

#### \_\_init\_\_

```python  theme={null}
def __init__(name: str | None = None,
             api_key: str | None = None,
             score_threshold: float = 0.4)
```

Initialize the VoyageEncoder.

**Arguments**:

* `name` (`str`): The name of the embedding model to use such as "voyage-embed".
* `voyage_api_key` (`str`): The Voyage API key.


Built with [Mintlify](https://mintlify.com).