# Source: https://docs.aurelio.ai/semantic-router/client-reference/index/qdrant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.index.qdrant

## QdrantIndex Objects

```python  theme={null}
class QdrantIndex(BaseIndex)
```

The name of the collection to use

#### add

```python  theme={null}
def add(embeddings: List[List[float]],
        routes: List[str],
        utterances: List[str],
        function_schemas: Optional[List[Dict[str, Any]]] = None,
        metadata_list: List[Dict[str, Any]] = [],
        batch_size: int = DEFAULT_UPLOAD_BATCH_SIZE,
        **kwargs)
```

Add records to the index.

**Arguments**:

* `embeddings` (`List[List[float]]`): The embeddings to add.
* `routes` (`List[str]`): The routes to add.
* `utterances` (`List[str]`): The utterances to add.
* `function_schemas` (`Optional[List[Dict[str, Any]]]`): The function schemas to add.
* `metadata_list` (`List[Dict[str, Any]]`): The metadata to add.
* `List[List[float]]`0 (`List[List[float]]`1): The batch size to use for the upload.

#### get\_utterances

```python  theme={null}
def get_utterances(include_metadata: bool = False) -> List[Utterance]
```

Gets a list of route and utterance objects currently stored in the index.

**Arguments**:

* `include_metadata` (`bool`): Whether to include function schemas and metadata in
  the returned Utterance objects - QdrantIndex does not currently support this
  parameter so it is ignored. If required for your use-case please reach out to
  semantic-router maintainers on GitHub via an issue or PR.

**Returns**:

`List[Utterance]`: A list of Utterance objects.

#### delete

```python  theme={null}
def delete(route_name: str)
```

Delete records from the index.

**Arguments**:

* `route_name` (`str`): The name of the route to delete.

#### describe

```python  theme={null}
def describe() -> IndexConfig
```

Describe the index.

**Returns**:

`IndexConfig`: The index configuration.

#### is\_ready

```python  theme={null}
def is_ready() -> bool
```

Checks if the index is ready to be used.

**Returns**:

`bool`: True if the index is ready, False otherwise.

#### query

```python  theme={null}
def query(
    vector: np.ndarray,
    top_k: int = 5,
    route_filter: Optional[List[str]] = None,
    sparse_vector: dict[int, float] | SparseEmbedding | None = None
) -> Tuple[np.ndarray, List[str]]
```

Query the index.

**Arguments**:

* `vector` (`np.ndarray`): The vector to query.
* `top_k` (`int`): The number of results to return.
* `route_filter` (`Optional[List[str]]`): The route filter to apply.
* `sparse_vector` (`dict[int, float] | SparseEmbedding | None`): The sparse vector to query.

**Returns**:

`Tuple[np.ndarray, List[str]]`: A tuple of the scores and route names.

#### aquery

```python  theme={null}
async def aquery(
    vector: np.ndarray,
    top_k: int = 5,
    route_filter: Optional[List[str]] = None,
    sparse_vector: dict[int, float] | SparseEmbedding | None = None
) -> Tuple[np.ndarray, List[str]]
```

Asynchronously query the index.

**Arguments**:

* `vector` (`np.ndarray`): The vector to query.
* `top_k` (`int`): The number of results to return.
* `route_filter` (`Optional[List[str]]`): The route filter to apply.
* `sparse_vector` (`dict[int, float] | SparseEmbedding | None`): The sparse vector to query.

**Returns**:

`Tuple[np.ndarray, List[str]]`: A tuple of the scores and route names.

#### aget\_routes

```python  theme={null}
def aget_routes()
```

Asynchronously get all routes from the index.

**Returns**:

`List[str]`: A list of routes.

#### delete\_index

```python  theme={null}
def delete_index()
```

Delete the index.

**Returns**:

`None`: None

#### convert\_metric

```python  theme={null}
def convert_metric(metric: Metric)
```

Convert the metric to a Qdrant distance metric.

**Arguments**:

* `metric` (`Metric`): The metric to convert.

**Returns**:

`Distance`: The converted metric.

#### \_\_len\_\_

```python  theme={null}
def __len__()
```

Returns the total number of vectors in the index. If the index is not initialized

returns 0.

**Returns**:

`int`: The total number of vectors.

#### adelete

```python  theme={null}
async def adelete(route_name: str) -> list[str]
```

Asynchronously delete records from the index by route name.

**Arguments**:

* `route_name` (`str`): The name of the route to delete.

**Returns**:

`list[str]`: List of IDs of the vectors deleted (empty list, as Qdrant does not return IDs).

#### adelete\_index

```python  theme={null}
async def adelete_index()
```

Asynchronously delete the index (collection) from Qdrant.

**Returns**:

`None`: None

#### ais\_ready

```python  theme={null}
async def ais_ready() -> bool
```

Checks if the index is ready to be used asynchronously.

#### aadd

```python  theme={null}
async def aadd(embeddings: List[List[float]],
               routes: List[str],
               utterances: List[str],
               function_schemas: Optional[List[Dict[str, Any]]] = None,
               metadata_list: List[Dict[str, Any]] = [],
               batch_size: int = DEFAULT_UPLOAD_BATCH_SIZE,
               **kwargs)
```

Asynchronously add records to the index, including metadata in the payload.

#### aget\_utterances

```python  theme={null}
async def aget_utterances(include_metadata: bool = False) -> List[Utterance]
```

Asynchronously gets a list of route and utterance objects currently stored in the index, including metadata.


Built with [Mintlify](https://mintlify.com).