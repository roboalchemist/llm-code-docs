# Source: https://docs.aurelio.ai/semantic-router/client-reference/routers/base.md

# Source: https://docs.aurelio.ai/semantic-router/client-reference/llms/base.md

# Source: https://docs.aurelio.ai/semantic-router/client-reference/index/base.md

# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.base

## DenseEncoder Objects

```python  theme={null}
class DenseEncoder(BaseModel)
```

#### set\_score\_threshold

```python  theme={null}
@field_validator("score_threshold")
def set_score_threshold(cls, v: float | None) -> float | None
```

Set the score threshold. If None, the score threshold is not used.

**Arguments**:

* `v` (`float | None`): The score threshold.

**Returns**:

`float | None`: The score threshold.

#### \_\_call\_\_

```python  theme={null}
def __call__(docs: List[Any]) -> List[List[float]]
```

Encode a list of documents. Documents can be any type, but the encoder must

be built to handle that data type. Typically, these types are strings or
arrays representing images.

**Arguments**:

* `docs` (`List[Any]`): The documents to encode.

**Returns**:

`List[List[float]]`: The encoded documents.

#### acall

```python  theme={null}
async def acall(docs: List[Any]) -> List[List[float]]
```

Encode a list of documents asynchronously. Documents can be any type, but the

encoder must be built to handle that data type. Typically, these types are
strings or arrays representing images.

**Arguments**:

* `docs` (`List[Any]`): The documents to encode.

**Returns**:

`List[List[float]]`: The encoded documents.

## SparseEncoder Objects

```python  theme={null}
class SparseEncoder(BaseModel)
```

An encoder that encodes documents into a sparse format.

#### \_\_call\_\_

```python  theme={null}
def __call__(docs: List[str]) -> List[SparseEmbedding]
```

Sparsely encode a list of documents. Documents can be any type, but the encoder must

be built to handle that data type. Typically, these types are strings or
arrays representing images.

**Arguments**:

* `docs` (`List[Any]`): The documents to encode.

**Returns**:

`List[SparseEmbedding]`: The encoded documents.

#### acall

```python  theme={null}
async def acall(docs: List[Any]) -> List[SparseEmbedding]
```

Encode a list of documents asynchronously. Documents can be any type, but the

encoder must be built to handle that data type. Typically, these types are
strings or arrays representing images.

**Arguments**:

* `docs` (`List[Any]`): The documents to encode.

**Returns**:

`List[SparseEmbedding]`: The encoded documents.

## AsymmetricDenseMixin Objects

```python  theme={null}
class AsymmetricDenseMixin()
```

#### encode\_queries

```python  theme={null}
def encode_queries(docs: List[str]) -> List[List[float]]
```

Convert query texts to dense embeddings optimized for querying

#### encode\_documents

```python  theme={null}
def encode_documents(docs: List[str]) -> List[List[float]]
```

Convert document texts to dense embeddings optimized for storage

#### aencode\_queries

```python  theme={null}
async def aencode_queries(docs: List[str]) -> List[List[float]]
```

Async version of encode\_queries

#### aencode\_documents

```python  theme={null}
async def aencode_documents(docs: List[str]) -> List[List[float]]
```

Async version of encode\_documents

## AsymmetricSparseMixin Objects

```python  theme={null}
class AsymmetricSparseMixin()
```

#### encode\_queries

```python  theme={null}
def encode_queries(docs: List[str]) -> List[SparseEmbedding]
```

Convert query texts to dense embeddings optimized for querying

#### encode\_documents

```python  theme={null}
def encode_documents(docs: List[str]) -> List[SparseEmbedding]
```

Convert document texts to dense embeddings optimized for storage

#### aencode\_queries

```python  theme={null}
async def aencode_queries(docs: List[str]) -> List[SparseEmbedding]
```

Async version of encode\_queries

#### aencode\_documents

```python  theme={null}
async def aencode_documents(docs: List[str]) -> List[SparseEmbedding]
```

Async version of encode\_documents


Built with [Mintlify](https://mintlify.com).