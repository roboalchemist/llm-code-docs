# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/aurelio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.aurelio

## AurelioSparseEncoder Objects

```python  theme={null}
class AurelioSparseEncoder(SparseEncoder, AsymmetricSparseMixin)
```

Sparse encoder using Aurelio Platform's embedding API. Requires an API key from
[https://platform.aurelio.ai](https://platform.aurelio.ai)

#### \_\_init\_\_

```python  theme={null}
def __init__(name: str | None = None, api_key: Optional[str] = None)
```

Initialize the AurelioSparseEncoder.

**Arguments**:

* `name` (`str | None`): The name of the model to use.
* `api_key` (`str | None`): The API key to use.

#### \_\_call\_\_

```python  theme={null}
def __call__(docs: list[str]) -> list[SparseEmbedding]
```

Encode a list of queries using the Aurelio Platform embedding API. Documents
must be strings, sparse encoders do not support other types.

#### acall

```python  theme={null}
async def acall(docs: list[str]) -> list[SparseEmbedding]
```

Asynchronously encode a list of documents using the Aurelio Platform

embedding API. Documents must be strings, sparse encoders do not support other
types.

:param docs: The documents to encode.
:type docs: list\[str]
:param input\_type:
:type semantic\_router.encoders.encode\_input\_type.EncodeInputType
:return: The encoded documents.
:rtype: list\[SparseEmbedding]

#### fit

```python  theme={null}
def fit(docs: List[str])
```

Fit the encoder to a list of documents. AurelioSparseEncoder does not support

fit yet.

**Arguments**:

* `docs` (`list[str]`): The documents to fit the encoder to.


Built with [Mintlify](https://mintlify.com).