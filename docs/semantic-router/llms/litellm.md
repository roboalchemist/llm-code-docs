# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/litellm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.litellm

#### litellm\_to\_list

```python  theme={null}
def litellm_to_list(embeds: litellm.EmbeddingResponse) -> list[list[float]]
```

Convert a LiteLLM embedding response to a list of embeddings.

**Arguments**:

* `embeds`: The LiteLLM embedding response.

**Returns**:

A list of embeddings.

## LiteLLMEncoder Objects

```python  theme={null}
class LiteLLMEncoder(DenseEncoder, AsymmetricDenseMixin)
```

LiteLLM encoder class for generating embeddings using LiteLLM.

The LiteLLMEncoder class is a subclass of DenseEncoder and utilizes the LiteLLM SDK
to generate embeddings for given documents. It supports all encoders supported by LiteLLM
and supports customization of the score threshold for filtering or processing the embeddings.

#### \_\_init\_\_

```python  theme={null}
def __init__(name: str | None = None,
             score_threshold: float | None = None,
             api_key: str | None = None)
```

Initialize the LiteLLMEncoder.

**Arguments**:

* `name` (`str`): The name of the embedding model to use. Must use LiteLLM naming
  convention (e.g. "openai/text-embedding-3-small" or "mistral/mistral-embed").
* `score_threshold` (`float`): The score threshold for the embeddings.

#### \_\_call\_\_

```python  theme={null}
def __call__(docs: list[Any], **kwargs) -> list[list[float]]
```

Encode a list of text documents into embeddings using LiteLLM.

**Arguments**:

* `docs`: List of text documents to encode.

**Returns**:

List of embeddings for each document.

#### acall

```python  theme={null}
async def acall(docs: list[Any], **kwargs) -> list[list[float]]
```

Encode a list of documents into embeddings using LiteLLM asynchronously.

**Arguments**:

* `docs`: List of documents to encode.

**Returns**:

List of embeddings for each document.


Built with [Mintlify](https://mintlify.com).