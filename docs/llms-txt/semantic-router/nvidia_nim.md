# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/nvidia_nim.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.nvidia_nim

This file contains the NimEncoder class which is used to encode text using Nim

## NimEncoder Objects

```python  theme={null}
class NimEncoder(LiteLLMEncoder)
```

Class to encode text using Nvidia NIM. Requires a Nim API key from
[https://nim.ai/api-keys/](https://nim.ai/api-keys/)

#### \_\_init\_\_

```python  theme={null}
def __init__(name: str | None = None,
             api_key: str | None = None,
             score_threshold: float = 0.4)
```

Initialize the NimEncoder.

**Arguments**:

* `name` (`str`): The name of the embedding model to use such as "nv-embedqa-e5-v5".
* `nim_api_key` (`str`): The Nim API key.


Built with [Mintlify](https://mintlify.com).