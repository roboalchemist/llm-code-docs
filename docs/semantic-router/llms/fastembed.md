# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/fastembed.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.fastembed

## FastEmbedEncoder Objects

```python  theme={null}
class FastEmbedEncoder(DenseEncoder)
```

Dense encoder that uses local FastEmbed to embed documents. Supports text only.

Requires the fastembed package which can be installed with `pip install 'semantic-router[fastembed]'`

**Arguments**:

* `name`: The name of the embedding model to use.
* `max_length`: The maximum length of the input text.
* `cache_dir`: The directory to cache the embedding model.
* `threads`: The number of threads to use for the embedding.

#### \_\_init\_\_

```python  theme={null}
def __init__(score_threshold: float = 0.5, **data)
```

Initialize the FastEmbed encoder.

**Arguments**:

* `score_threshold` (`float`): The threshold for the score of the embedding.

#### \_\_call\_\_

```python  theme={null}
def __call__(docs: List[str]) -> List[List[float]]
```

Embed a list of documents. Supports text only.

**Arguments**:

* `docs` (`List[str]`): The documents to embed.

**Raises**:

* `ValueError`: If the embedding fails.

**Returns**:

`List[List[float]]`: The vector embeddings of the documents.


Built with [Mintlify](https://mintlify.com).