# Source: https://code.kx.com/kdbai/latest/use/supported-indexes.html

Title: KDB.AI Indexes - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/supported-indexes.html

Markdown Content:
How to Use Indexes in KDB.AI
----------------------------

_This page describes how to use indexes in KDB.AI and key parameters that can be tailored to specific use cases._

Index comparison
----------------

|  | **Flat** | **qFlat** | **HNSW** | **qHNSW** | **IVF** | **IVFPQ** |
| --- | --- | --- | --- | --- | --- | --- |
| Retrieval speed | Low | Low | Very high | Very high | Moderate | High |
| Indexing speed | Very high | Very high | Low | Low | Moderate | Moderate |
| Accuracy | Highest | Highest | Balanced & tunable | Balanced & tunable | Balanced & tunable | Balanced & tunable |
| Memory used | High | Very low | Very high | Low | High | Moderate |
| Storage | Memory | Disk | Memory | Disk | Memory | Memory |

HNSW, qHNSW, IVF, and IVFPQ can be configured with different hyper-parameters to optimize memory usage, retrieval speed, and accuracy. Generally, HNSW indexes are both fast and accurate but require a lot of memory. On the other hand, IVF indexes tend to be slower and less accurate but are more memory-efficient, especially the product quantized version, IVFPQ.

Flat
----

The Flat search performs an exhaustive search against all vectors in the search space.

When to use Flat?

Use Flat for:

*   Low-dimensional data
*   Small-scale databases
*   Simple querying
*   Real-time data ingestion
*   Low-query volume

Pros Cons

Guarantees 100% recall and precision.

Can be slower and less efficient than other types of vector indexes.

You can configure the Flat index with a number of distance metrics. As the search is exhaustive, it finds the exact nearest neighbors without approximations.

### Build parameters

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Number of dimensions | long | true | 8 |
| metric | Distance metric | symbol | false | L2 |

Python JSON q

```
indexes = [
    {
        'name': 'flat_index',
        'column': 'embeddings',
        'type': 'flat',
        'params': {'dims': 25}
    }
]
```

```
{
    "indexes": [
        {
            "name": "flat_index",
            "column": "embeddings",
            "type": "flat",
            "params": {"dims": 25}
        }
    ]
}
```

```
flatIndex: `name`column`type`params!(`flat_index;`embeddings;`flat;enlist[`dims]!enlist 25)
indexes: enlist flat_index
```

Create table example for the Flat index:

```
schema = [
            {'name': 'id', 'pytype': 'str'},
            {'name': 'tag', 'pytype': 'str'},
            {'name': 'text', 'pytype': 'bytes'},
            {'name': 'embeddings', 'type': 'float32s'}
            ]

flat_index = [
            {
                'name': 'vectorIndex',
                'type': 'flat',
                'column': 'embeddings',
                'params': {'dims': 1536, 'metric': 'L2'},
            }
        ]
# get the database connection. Default database name is 'default'
db = session.database('default')

# create the table
table = db.create_table('documents', schema=schema, indexes=flat_index)
```

 Storage: the Flat index is stored in-memory. 
qFlat
-----

The qFlat search performs an exhaustive search against all vectors in the search space.

When to use qFlat?

The qFlat index is the Flat index stored [on-disk instead of in-memory](https://code.kx.com/kdbai/latest/reference/index.html#2-in-memory-vs-on-disk). Use qFlat for:

*   Situations when you would use Flat, but memory is limited
*   Low-dimensional data
*   Small-scale databases
*   Simple querying
*   Real-time data ingestion
*   Low-query volume

Pros Cons

*   Guarantees 100% recall and precision. 
*   Useful when memory is limited.

Can be slower and less efficient than other types of vector indexes.

You can configure the qFlat index with a number of distance metrics. As the search is exhaustive, it finds the exact nearest neighbors without approximations.

### Build parameters

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Number of dimensions | long | true | 8 |
| metric | Distance metric | symbol | false | L2 |

### Search parameters

At search time, qFlat can either return `n` nearest neighbors, or all neighbors that fall within a specified `range`. The `range` option is applicable to qFlat indexes only.

*   `index_options` at `search()`

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| `n` | Number of nearest neighbors to return | int | false | None |
| `range` | Range within which the nearest neighbors are returned | float | false | None |

Python JSON q

```
indexes = [
    {
        'name': 'qflat_index',
        'column': 'embeddings',
        'type': 'qFlat',
        'params': {'dims': 25}
    }
]
```

```
{
    "indexes": [
        {
            "name": "qflat_index",
            "column": "embeddings",
            "type": "qFlat",
            "params": {"dims": 25}
        }
    ]
}
```

```
qFlatIndex: `name`column`type`params!(`qflat_index;`embeddings;`qFlat;enlist[`dims]!enlist 25)
indexes: enlist qFlatIndex
```

Create table example for the qFlat index:

```
schema = [
            {'name': 'id', 'pytype': 'str'},
            {'name': 'tag', 'pytype': 'str'},
            {'name': 'text', 'pytype': 'bytes'},
            {'name': 'embeddings', 'type': 'float32s'}
        ]

qflat_index = [
            {
                'name': 'vectorIndex',
                'type': 'qFlat',
                'column': 'embeddings',
                'params': {'dims': 25, 'metric': 'L2'},
            }
        ]
# get the database connection. Default database name is 'default'
db = session.database('default')

# create the table
table = db.create_table('documents', schema=schema, indexes=qflat_index)
```

Example of a `range` search for the qFlat index:

```
schema = [
            {'name': 'id', 'pytype': 'str'},
            {'name': 'tag', 'pytype': 'str'},
            {'name': 'text', 'pytype': 'bytes'},
            {'name': 'embeddings', 'type': 'float32s'}
        ]

qflat_index = [
            {
                'name': 'vectorIndex',
                'type': 'qFlat',
                'column': 'embeddings',
                'params': {'dims': 25, 'metric': 'L2'},
            }
        ]
# get the database connection. Default database name is 'default'
db = session.database('default')

# create the table
table = db.create_table('documents', schema=schema, indexes=qflat_index)

# Perform a more precise search using the range option
table.search(vectors={vectorIndex: [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}, range=5.5)
```

HNSW
----

A Hierarchical Navigable Small Worlds (HNSW) index establishes connections between vertices in the graph based on their distances. These links are instrumental in enabling efficient traversal and navigation through the hierarchical graph during the search process.

When to use HNSW?

Use HNSW for:

*   Medium-Large scale datasets
*   Good accuracy
*   High-dimensional data (hundred or thousands of dimensions)
*   Efficient nearest-neighbor search for: 
    *   recommendation systems
    *   content-based image retrieval
    *   NLP tasks

*   Approximate nearest-neighbor search when looking for cost reduction
*   Large-scale databases
*   Real-time and dynamic data
*   Highly resourced environments (distributed and parallel computing)

Pros Cons

*   More efficient than flat or qFlat.
*   Simple to configure and scalable for real-time and dynamic data.

*   Can be small inaccuracies in results. 
*   Uses quite a lot of memory. 
*   Tuning for highest accuracy performance is computationally expensive.

Use the HNSW index to search and navigate through the layers of a graph to find increasingly similar data in that graph. This approach is extremely efficient with search performance a measure of the complexity of the graph.

### Build parameters

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Number of dimensions | long | true | 8 |
| efConstruction | Number of nodes at each step of the graph construction. | int | false | 8 |
| M | Valence of each node in graph | int | false | 8 |
| metric | Distance metric | symbol | false | L2 |

### Search parameters

*   `index_options` at `search()` (and `dense_index_options` at `hybrid_search()`)

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| `efSearch` | Nodes considered at each step (search) | int | false | 8 |

For optimal balance between accuracy and performance, choose a value of 2 - 10 times your `n` for `efSearch`. As a rule, increase the value for higher accuracy at the cost of slower search times.

For coding example of using the argument `index_options at search()`, refer to the [Python API Client](https://code.kx.com/kdbai/latest/reference/python-client.html) documentation.

Python JSON q

```
indexes = [
    {
        'name': 'hnsw_index',
        'column': 'embeddings',
        'type': 'hnsw',
        'params': { 'dims': 25, 'efConstruction': 8, 'M': 8, 'metric': 'L2'}}
    }
]
```

```
{
    "indexes": [
        {
            "name": "hnsw_index",
            "column": "embeddings",
            "type": "hnsw",
            "params": { "dims": 25, "efConstruction": 8, "M": 8, "metric": "L2"}}
        }
    ]
}
```

```
hnswIndex: `name`column`type`params!(`hnsw_index;`embeddings;`hnsw;`dims`M`efConstruction!(25;8;8))
indexes: enlist hnswIndex
```

Create table example for the HNSW index:

```
schema = [
            {'name': 'id', 'pytype': 'str'},
            {'name': 'tag', 'pytype': 'str'},
            {'name': 'text', 'pytype': 'bytes'},
            {'name': 'embeddings', 'type': 'float32s'}
        ]

hnsw_index = [
            {
                'name': 'vectorIndex',
                'type': 'hnsw',
                'column': 'embeddings',
                'params': { 'dims': 25,
                            'efConstruction': 8,
                            'M': 8,
                            'metric': 'L2'},
            }
        ]
# get the database connection. Default database name is 'default'
db = session.database('default')

# create the table
table = db.create_table('documents', schema=schema, indexes=hnsw_index)
```

qHNSW
-----

The q Hierarchical Navigable Small Worlds (qHNSW) index establishes connections between vertices in the graph based on their distances. These links are instrumental in enabling efficient traversal and navigation through the hierarchical graph during the search process.

Use the HNSW index to search and navigate through the layers of a graph to find increasingly similar data in that graph. This approach is extremely efficient with search performance a measure of the complexity of the graph.

When to use qHNSW?

The qHNSW index is the HNSW index stored [on-disk instead of in-memory](https://code.kx.com/kdbai/latest/reference/index.html#2-in-memory-vs-on-disk). Use qHNSW for:

*   Situations when you would use HNSW, but memory is limited
*   Medium-Large scale datasets
*   Good accuracy
*   High-dimensional data (hundred or thousands of dimensions)
*   Efficient nearest neighbor search for:

    *   recommendation systems
    *   content-based image retrieval
    *   NLP tasks

*   Approximate nearest neighbor search when looking for cost reduction

*   Large-scale databases
*   Real-time and dynamic data
*   Highly resourced environments (distributed and parallel computing)

Pros Cons

*   More efficient than flat or qFlat. 
*   Simple to configure.
*   Scalable for real-time and dynamic data. 
*   Useful when memory is limited.

Lower accuracy than similarity search and IVFPQ.

### Build parameters

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| dims | Number of dimensions | long | true | 8 |
| efConstruction | Number of nodes at each step of the graph construction. | int | false | 8 |
| M | Valence of each node in graph | int | false | 8 |
| metric | Distance metric | symbol | false | L2 |
| mmapLevel | Level of memory mapping. Accepted values: - 0 for both vectors and node connection in memory; - 1 for memory-mapped vectors and in-memory nodes ; - 2 for both vectors and node connections memory mapped. | int | No | 1 |

### Search parameters

*   `index_options` at `search()` (and `dense_index_options` at `hybrid_search()`)

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| `efSearch` | Nodes considered at each step (search) | int | false | 8 |

For optimal balance between accuracy and performance, choose a value of 2 - 10 times your `n` for `efSearch`. As a rule, increase the value for higher accuracy at the cost of slower search times.

For coding example of using the argument `index_options at search()`, refer to the [Python API Client](https://code.kx.com/kdbai/latest/reference/python-client.html) documentation.

Python JSON q

```
index = [
    {
        'name': 'qhnsw_index',
        'column': 'embeddings',
        'type': 'qHnsw',
        'params': { 'dims': 25, 'efConstruction': 8, 'M': 8, 'metric': 'L2'}}
    }
]
```

```
{
    "indexes": [
        {
            "name": "qhnsw_index",
            "column": "embeddings",
            "type": "qHnsw",
            "params": { "dims": 25, "efConstruction": 8, "M": 8, "metric": "L2"}}
        }
    ]
}
```

```
qhnswIndex: `name`column`type`params!(`qhnsw_index;`embeddings;`qHnsw;`dims`M`efConstruction!(25;8;8))
indexes: enlist qhnswIndex
```

Create table example for the qHnsw index:

```
schema = [
            {'name': 'id', 'pytype': 'str'},
            {'name': 'tag', 'pytype': 'str'},
            {'name': 'text', 'pytype': 'bytes'},
            {'name': 'embeddings', 'type': 'float32s'}
        ]

qhnsw_index = [
            {
                'name': 'vectorIndex',
                'type': 'qHnsw',
                'column': 'embeddings',
                'params': {
                            'dims': 25,
                            'efConstruction': 8,
                            'M': 8,
                            'metric': 'L2'},
            }
        ]
# get the database connection. Default database name is 'default'
db = session.database('default')

# create the table
table = db.create_table('documents', schema=schema, indexes=qhnsw_index)
```

IVF
---

When using an Inverted File (IVF) search, first you train the index on a set of points that are used to generate cluster centroids using a k-means algorithm.

When to use IVF?

Use IVF for:

*   Large-scale datasets
*   High-dimensional data (hundreds or thousands of dimensions)
*   Fast searches

Pros Cons

More efficient than flat or qFlat.

Lower accuracy than brute force search.

The data is not partitioned into a cluster based on centroid distance. The search is performed by running a flat search against the most relevant clusters. As only a subset of the data is searched, the results are returned much quicker, but as a consequence can be less accurate compared to flat searches..

### Build parameters

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| nclusters | Number of clusters into which the data is divided. | int | false | 8 |
| metric | Distance metric | symbol | false | L2 |

### Search parameters

*   `index_options` at `search()` (and `dense_index_options` at `hybrid_search()`)

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| clusters | The number of clusters to be traversed in the search | int | false | 2 |

[Training](https://code.kx.com/kdbai/latest/use/ingestion.html#train-index) is required to initialize the IVF index.

Python JSON q

```
indexes = [
    {
        'name': 'ivf_index',
        'column': 'embeddings',
        'type': 'ivf',
        'params': { 'nclusters': 10, 'metric': 'CS'}}
    }
]
```

```
{
    "indexes": [
        {
            "name": "ivf_index",
            "column": "embeddings",
            "type": "ivf",
            "params": { "nclusters": 10, "metric": "CS"}}
        }
    ]
}
```

```
ivfIndex: `name`column`type`params!(`ivf_index;`embeddings;`ivf;enlist[`nclusters]!enlist 10)
indexes: enlist ivfIndex
```

Create table example for the IVF index:

```
schema = [
            {'name': 'id', 'pytype': 'str'},
            {'name': 'tag', 'pytype': 'str'},
            {'name': 'text', 'pytype': 'bytes'},
            {'name': 'embeddings', 'type': 'float32s'}
        ]

ivf_index = [
            {
                'name': 'vectorIndex',
                'type': 'ivf',
                'column': 'embeddings',
                'params': {'nclusters': 10, 'metric': 'CS'},
            }
        ] 
# get the database connection. Default database name is 'default'
db = session.database('default')

# create the table
table = db.create_table('documents', schema=schema, indexes=ivf_index)
```

IVFPQ
-----

You can compress input data using the product quantization method before applying the IVF schema above. This is known as Inverted File Product Quantization (IVFPQ). IVFPQ can greatly reduce the size of the index held in memory and improve search speeds.

When to use IVFPQ?

Use IVFPQ for:

*   Large-scale datasets
*   Situations where accuracy is not critical
*   Memory efficiency

Pros Cons

*   More efficient than flat or qFlat. 
*   Very memory efficient.

Lower accuracy than standard IVF index with similar parameters due to compression.

For configuring the IVFPQ index to balance between search accuracy and efficiency, use these parameters:

### Build parameters

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| nclusters | Number of clusters into which the data is divided. Clustering helps to reduce the search space by grouping similar data points together. | int | false | 8 |
| nsplits | Number of splits or partitions of the data. Each split is quantized separately, which helps in managing large datasets more efficiently. | int | false | 8 |
| nbits | Number of bits used for encoding each sub-vector in the product quantization process. It determines the precision of the quantization. | int | false | 8 |
| metric | Distance metric | str | false | L2 |

### Search parameters

*   `index_options` at `search()` (and `dense_index_options` at `hybrid_search()`)

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| `clusters` | The number of clusters to be traversed in the search | int | false | 2 |

[Training](https://code.kx.com/kdbai/latest/use/ingestion.html#train-index) is required, to initialize the IVFPQ index.

Python JSON q

```
indexes = [
    {
        'name': 'ivf_index',
        'column': 'embeddings',
        'type': 'ivf',
        'params': {'nclusters': 10, 'metric': 'CS', 'nsplits': 8, 'nbits': 8}}
    }
]
```

```
{
    "indexes": [
        {
            "name": "ivf_index",
            "column": "embeddings",
            "type": "ivf",
            "params": {"nclusters": 50, "metric": "CS", "nsplits": 8, "nbits": 8}}
        }
    ]
}
```

```
ivfpqIndex: `name`column`type`params!(`ivfpq_index;`embeddings;`ivfpq;`nclusters`nsplits`nbits!(50;8;8))
indexes: enlist ivfpqIndex
```

Create table example for the IVFPQ index:

```
schema = [
            {'name': 'id', 'pytype': 'str'},
            {'name': 'tag', 'pytype': 'str'},
            {'name': 'text', 'pytype': 'bytes'},
            {'name': 'embeddings', 'type': 'float32s'}
        ]

ivfpq_index = [
            {
                'name': 'vectorIndex',
                'type': 'ivfpq',
                'column': 'embeddings',
                'params': { 'metric': 'L2',
                            'nclusters': 50,
                            'nsplits': 8,
                            'nbits': 8},
            }
        ]
# get the database connection. Default database name is 'default'
db = session.database('default')

# create the table
table = db.create_table('documents', schema=schema, indexes=ivfpq_index)
```

Tips for choosing the right number of clusters (`nclusters`) for IVF and IVFPQ:

*   **Dataset characteristics**: The size and distribution of your dataset play a crucial role. Larger datasets typically benefit from more clusters, which can enhance search precision but also require more memory and longer indexing times.
*   **Balancing act**: More clusters can lead to finer partitioning, improving search accuracy. However, this comes at the cost of increased memory usage and slower indexing. You'll need to find a balance that suits your needs.
*   **Iterative testing**: Start with a smaller number of clusters and incrementally increase them, observing the impact on performance. 
*   **Training vector quantity**: Ensure you have enough training vectors to capture the diversity of your dataset. Depending on its complexity, you might need anywhere from a few thousand to tens of thousands of vectors.
*   **Performance metrics**: Use metrics such as recall and precision to evaluate different configurations. This will help you understand the trade-offs and select the best setup for your specific use case.

### How to choose training data and vector embeddings

When selecting training data for your Inverted File Index (IVF), it's crucial to use a subset of your actual dataset rather than randomly generated data. This ensures the training vectors accurately represent the characteristics of your dataset, leading to a more effective and tailored index.

For vector embeddings, especially in the context of Transformed TSS embeddings, you should train on the compressed embeddings. These are the dimensions that will be stored in the index, making them the most relevant for training purposes.

By carefully selecting representative training data and focusing on the compressed embeddings, you can significantly enhance the performance and accuracy of your IVF.

Multiple indexes
----------------

In KDB.AI, you can optimize your queries by adding multiple indexes to a single table (at table creation time), each of which can be associated with an embedding column. This feature is particularly useful for handling diverse datasets and improving query performance. Here’s a breakdown of how to use multiple indexes:

*   Multiple indexes can share the same embedding column, so there’s no need to duplicate the embeddings, saving storage and maintaining efficiency. For instance, you might have:

    *   A fast HNSW index with parameters `m: 8` and `ef construction: 16` for quick searches.
    *   A more accurate but slower HNSW index with parameters `m: 64` and `ef construction: 512`.

*   Assign weights to different indexes during searches to fine-tune result ranking based on the importance of various data aspects. This feature allows for more precise and relevant search outcomes.

Important! The sum of all weights must be equal to 1.
