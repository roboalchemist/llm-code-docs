# Source: https://code.kx.com/kdbai/latest/use/hybrid-search.html

Title: Hybrid Search - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/hybrid-search.html

Markdown Content:
How to Perform a Hybrid Search in KDB.AI
----------------------------------------

_This page details how to execute a hybrid search in KDB.AI._

In KDB.AI, a hybrid search returns results based on both dense and sparse vector search. The process includes querying and re-ranking of results across both vector sets. The weight factor on the search for each algorithm can be controlled through the parameter named `index_params`.

Before we dive in, go to the [understanding hybrid search](https://code.kx.com/kdbai/latest/reference/hybrid.html) page to make sure you're familiar with dense vectors, sparse vectors, tokenization, and the Best Matching 25 (BM25) algorithm.

A hybrid search blends a dense search with a sparse search. Therefore, you need to perform the following:

1.   [Dense search](https://code.kx.com/kdbai/latest/use/hybrid-search.html#1-dense-search)
2.   [Sparse search](https://code.kx.com/kdbai/latest/use/hybrid-search.html#2-sparse-search)
3.   [Hybrid search](https://code.kx.com/kdbai/latest/use/hybrid-search.html#3-hybrid-search)

Setup
-----

Before you start, make sure you have:

*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download/) license
*   Installed the latest version of KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
*   [Python Client](https://code.kx.com/kdbai/latest/reference/python-client.html)

1. Dense search
---------------

For details on how to perform a standalone dense search, go to the [How to conduct a similarity search](https://code.kx.com/kdbai/latest/use/search.html) page.

2. Sparse search
----------------

This section details how to perform a standalone sparse search.

### 2.1 Create table with a sparse index in KDB.AI

To use sparse vectors, you need to create a table with a sparse index.

*   Parameters

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| `k` | Term saturation | real | false | 1.25 |
| `b` | Document length impact on relevance | real | false | 0.75 |

The values of `k` and `b` can be modified in place at search time.

Python JSON q

```
schema = [
     {'name': 'id', 'type': 'int32'},
     {'name': 'sym', 'type': 'str'},
     {'name': 'time', 'type': 'datetime64[ns]'},
     {'name': 'text', 'type': 'general'}]
indexes = [{'name': 'sparse_index', 'type': 'bm25', 'column': 'text', 'params': {'k': 1.25, 'b': 0.75}}]
```

```
{
  "schema": [
    {"name": "id", "type": "int"},
    {"name": "sym", "type": "symbol"},
    {"name": "time", "type": "timestamp"},
    {"name": "text", "type": ""}
  ],
  "indexes": [{"name": "sparse_index", "type": "bm25", "column": "text", "params": {"k": 1.25, "b": 0.75}}]
}
```

```
schema: flip `name`type!(`id`sym`time`text;`i`s`p`E)
indexes: enlist `name`type`column`params!(`sparse_index;`bm25;`text;`k`b!(1.25 0.75))
```

You can use these schemas to create the tables as shown on the [Manage Tables](https://code.kx.com/kdbai/latest/use/manage-tables.html) page.

### 2.2 Insert sparse vectors

Before the data is inserted, the sparse vectors should be prepared as dictionaries with integer keys and values:

Python JSON q

Here is an example of generating a pandas dataframe with sparse vectors as the payload for insert:

```
import numpy as np 
import pandas as pd
import kdbai_client as kdbai

# Connect with the KDB.AI table
session = kdbai.Session()  # by default, creates session to localhost:8082 using QIPC connection
database = session.database('default')

for table in database.tables:
  if table.name == 'documents':
    table.drop()
    break

schema = [
  {'name': 'id', 'type': 'int16'},
  {'name': 'tag', 'type': 'bool'},
  {'name': 'author', 'type': 'str'},
  {'name': 'length', 'type': 'int32'},
  {'name': 'content', 'type': 'str'},
  {'name': 'createdDate', 'type': 'datetime64[ns]'},
  {'name': 'sparse', 'type': 'general'}
]
indexes = [{'name': 'sparse_index', 'type': 'bm25', 'column': 'sparse', 'params': {'k': 1.25, 'b': 0.75}}]
documents = database.create_table('documents', schema=schema, indexes=indexes) 

# Generate data
n_rows = 2000

data = pd.DataFrame({
    'id': np.arange(n_rows, dtype='int16'),
    'tag': np.random.choice([True, False], n_rows),
    'author': [f'author{i}' for i in range(n_rows)],
    'length': np.random.randint(0, 1000, n_rows, dtype='int32'),
    'content': [f'document{i}' for i in range(n_rows)],
    'createdDate': pd.date_range(start='2020-01-01', periods=n_rows, freq='1D'),
    'sparse': [{int(y+1):1 for y in np.random.choice(range(1200),x+1,replace=False)} for x in np.random.choice(range(120),n_rows)]})
```

Here is an example of generating a JSON file with sparse vectors as the payload for insert:

```
[
  {
    "id": 21212,
    "tag": true,
    "author": "jill",
    "length": 68,
    "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
    "createdDate": "2023-10-11T00:00:00.000000000",
    "sparse": {"1996": 2, "101": 1, "11190": 1, "5598": 1, "2058": 1, "4231": 1, "102": 1}
  },
  {
    "id": 19376,
    "tag": false,
    "author": "joe",
    "length": 626,
    "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
    "createdDate": "2023-10-11T00:00:00.000000000",
    "sparse": {"1996": 1, "11190": 1, "2058": 1, "4231": 1, "102": 1}
  }
]
```

```
id: 21212 21212
tag: 10b
author: `jill`joe
content: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789
createdDate: 2023.10.11T00:00:00.000000000 2023.10.11T00:00:00.000000000
dense: (til 12; til 12)
sparse: ((1996 101 11190 5598 2058 5231 102!2 1 1 1 1 1 1);(1996 11190 2058 4231 102! 1 1 1 1 1))

data: `id`tag`author`content`createdDate`dense`sparse!(id tag content createdDate dense sparse)
```

Now you can populate your table with data.

Python JSON q

Populate the `documents` table with the above dataframe.

```
documents.insert(data)
```

Populate the `documents` table with a curl http request.

Save the following to a local file named `insert.json`:

```
{
  "rows": [
    {
      "id": 21212,
      "tag": true,
      "author": "jill",
      "length": 68,
      "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
      "createdDate": "2023-10-11T00:00:00.000000000",
      "sparse": {"1996": 2, "101": 1, "11190": 1, "5598": 1, "2058": 1, "4231": 1, "102": 1}
    },
    {
      "id": 19376,
      "tag": false,
      "author": "joe",
      "length": 626,
      "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
      "createdDate": "2023-10-11T00:00:00.000000000",
      "sparse": {"1996": 1, "5598": 1, "2058": 1, "4231": 1, "102": 1}
    }
  ]
}
```

Ensure that the `@` sign is included before the filename, otherwise, the file becomes URI-encoded.

```
curl -H 'Content-Type: application/json' -d @insert.json localhost:8081/api/v2/databases/default/tables/documents/insert
```

```
gw(`insertData;`database`table`payload!(`default;`documents;data))
```

### 2.3. Perform a sparse search

The search endpoint is overloaded to accept lists of sparse vectors:

*   Parameters Index Options

| **Option** | **Description** | **Type** | **Required** | **Default** |
| --- | --- | --- | --- | --- |
| `k` | Term saturation | real | false | 1.25 |
| `b` | Document length impact on relevance | real | false | 0.75 |

Python JSON q

```
documents.search(vectors={'sparse_index': [{1:2,3:1}]},n=3)
```

```
curl -s -H "Content-Type: application/json" localhost:8081/api/v2/databases/default/tables/documents/search \
-d '{"n": 3,"vectors": {"sparse_index": [{"1":2,"3":1}]}}'
```

```
// gw is a handler to the gateway
gw(`search;`database`table`n`vectors!(`default;`documents;3;enlist[`sparse_index]!enlist[enlist[(1 3)!(2 1)]]))
```

3. Hybrid search
----------------

Combining the sparse and dense searches is the basis of the hybrid search. You can use the parameter `index_params` to determine the weighting of each leg of the search.

For intermediate values, the following algorithm demonstrates an example that assumes:

*   the number of matches is 4.
*   `weight` are 0.6 and 0.4.
*   the dense search returned vectors in order 3, 2, 1, 5.
*   the sparse search returned vectors in order 4, 3, 2, 1.

| **Vector** | **Sparse** | **Dense** | **Re-ranked** |
| --- | --- | --- | --- |
| Vector 1 | 3 | 4 | 3 |
| Vector 2 | 2 | 3 | 2 |
| Vector 3 | 1 | 2 | 1 |
| Vector 4 | null | 1 | 4 |
| Vector 5 | 5 | null | 5 |

We deduced the combined ranking (re-ranked) by the reciprocal rank fusion scores defined by the following formula:

score(i)=0.4 1+sparserank(i)+0.6 1+denserank(i)

We computed the scores as below:

Since vector 1 occurs in the sparse search in position 3 and in the dense search in position 4, it receives a score of 0.22, as calculated below:

![Image 1](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20%20{\fontsize{10}{10}%200.4\cdot(1/(1+3))%20+%200.6\cdot(1/(1+4))%20}})

Since vector 2 occurs in the sparse search in position 2 and in the dense search in position 3, it receives a score of 0.28:

![Image 2](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{\fontsize{10}{10}%200.4\cdot(1/(1+2))%20+%200.6\cdot(1/(1+3))%20}})

Since vector 3 occurs in the sparse search in position 1 and in the dense search in position 2, it receives a score of 0.4:

![Image 3](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{\fontsize{10}{10}%200.4\cdot(1/(1+1))%20+%200.6\cdot(1/(1+2))%20}})

Since vector 4 doesn't occur in the sparse search and in the dense search in position 1, it receives a score of 0.2:

![Image 4](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{\fontsize{10}{10}%200.4\cdot(0)%20+%200.6\cdot(1/(1+2))%20}})

Since vector 5 occurs in the sparse search in position 5 and doesn't occur in the dense search, it receives a score of 0.08:

![Image 5](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20{\fontsize{10}{10}%200.4\cdot(1/(1+4))%20+%200.6\cdot(0)%20}})

Comparing these five scores, the top four results are returned based on the sorted value.

Summary
-------

To perform a hybrid search, you need to define the dense and sparse vectors in the schema. See the [Schema](https://code.kx.com/kdbai/latest/use/manage-tables.html#schema) section on the [Manage Tables](https://code.kx.com/kdbai/latest/use/manage-tables.html) page.

Python JSON q

```
schema = [
  {'name': 'id', 'type': 'int16'},
  {'name': 'tag', 'type': 'bool'},
  {'name': 'author', 'type': 'str'},
  {'name': 'length', 'type': 'int32'},
  {'name': 'content', 'type': 'str'},
  {'name': 'dense', 'type': 'float32s'},
  {'name': 'sparse', 'type': 'general'}
]
indexes = [
  {'name': 'dense_index', 'type': 'hnsw', 'column': 'dense', 'params': {'dims': 10, 'metric': 'L2'}},
  {'name': 'sparse_index', 'type': 'bm25', 'column': 'sparse', 'params': {'k': 1.25, 'b': 0.75}}
]
```

```
{
  "schema": [
    {"name": "id", "type": "int16"},
    {"name": "tag", "type": "bool"},
    {"name": "author", "type": "str"},
    {"name": "length", "type": "int32"},
    {"name": "content", "type": "str"},
    {"name": "dense", "type": "float32s"},
    {"name": "sparse", "type": "general"}
  ],
  "indexes": [
    {"name": "dense_index", "type": "hnsw", "column": "dense", "params": {"dims": 10, "metric": "L2"}},
    {"name": "sparse_index", "type": "bm25", "column": "sparse", "params": {"k": 1.25, "b": 0.75}}
  ]
}
```

```
schema: flip `name`type!(`id`tag`author`length`content`dense`sparse;`i`b`s`i`s`E`)
indexes: enlist `name`type`column`params!(`dense_index;`hnsw;`dense;`dims`metric!(10;`L2))
indexes,: enlist `name`type`column`params!(`sparse_index;`bm25;`sparse;`k`b!(1.25 0.75))
```

Assuming a `documents` table exists with the correct schema, you can insert the data via Python (as a pandas dataframe) or via REST (as a JSON file):

Python JSON q

Here is an example of generating a pandas dataframe with sparse and dense vectors as the payload for insert:

```
import kdbai_client as kdbai
import numpy as np 
import pandas as pd 

# Connect with the KDB.AI table
session = kdbai.Session()  # by default, creates session to localhost:8082 using QIPC connection
database = session.database('default')
documents = database.table('documents')

# Generate data
n_rows = 2000

data = pd.DataFrame({
    'id': np.arange(n_rows, dtype='int16'),
    'tag': np.random.choice([True, False], n_rows),
    'author': [f'author{i}' for i in range(n_rows)],
    'length': np.random.randint(0, 1000, n_rows, dtype='int32'),
    'content': [f'document{i}' for i in range(n_rows)],
    'createdDate': pd.date_range(start='2020-01-01', periods=n_rows, freq='1D'),
    'dense': [np.random.rand(10).astype('float32') for _ in range(n_rows)],
    'sparse': [{int(y + 1):1 for y in np.random.choice(range(1200), x + 1, replace=False)} for x in np.random.choice(range(120), n_rows)]})

documents.insert(data)
```

Here is an example of generating a JSON file with sparse and dense vectors as the payload for insert:

```
[
  {
    "id": 21212,
    "tag": true,
    "author": "jill",
    "length": 68,
    "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
    "createdDate": "2023-10-11T00:00:00.000000000",
    "dense": [0,1,2,3,4,5,6,7,8,9,10,11],
    "sparse": {"1996": 2, "101": 1, "11190": 1, "5598": 1, "2058": 1, "4231": 1, "102": 1}
  },
  {
    "id": 19376,
    "tag": false,
    "author": "joe",
    "length": 626,
    "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
    "createdDate": "2023-10-11T00:00:00.000000000",
    "dense": [0,1,2,3,4,5,6,7,8,9,10,11],
    "sparse": {"1996": 1, "11190": 1, "2058": 1, "4231": 1, "102": 1}
  }
]
```

```
id: 21212 21212
tag: 10b
author: `jill`joe
content: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789
createdDate: 2023.10.11T00:00:00.000000000 2023.10.11T00:00:00.000000000
dense: (til 12; til 12)
sparse: ((1996 101 11190 5598 2058 5231 102!2 1 1 1 1 1 1);(1996 11190 2058 4231 102! 1 1 1 1 1))

data: `id`tag`author`content`createdDate`dense`sparse!(id tag content createdDate dense sparse)
```

Assuming a `documents` table exists with a compliant schema, once you insert the data via Python of REST, perform the hybrid search:

Python JSON q

```
index_params = {
  'dense_index': {'weight': 0.6},
  'sparse_index': {'weight': 0.4}
}
documents.search(vectors={'dense_index': [[0,0,0,0,0,0,0,0,0,0]], 'sparse_index': [{1:2, 3:1}]}, n=3, index_params=index_params)
```

```
curl -s -H "Content-Type: application/json" localhost:8081/api/v2/databases/default/tables/documents/search \
-d '{"n": 3, "vectors": {"sparse_index": [{"1":2, "3":1}], "dense_index": [[0,0,0,0,0,0,0,0,0,0]]}, "indexParams": {"dense_index": {"weight": 0.6}, "sparse_index": {"weight": 0.4}}}'
```

```
gw(`insertData;`database`table`payload!(`default;`documents;data))
```

End-to-end example
------------------

This example demonstrates how to perform each of the three searches on some dummy data.

Click here to expand the code sample

```
import pandas as pd
import numpy as np
import kdbai_client as kdbai

### start session

session = kdbai.Session()
database = session.database('default')

### create table

schema = [
        {'name': 'id', 'type': 'int32'},
        {'name': 'sym', 'type': 'str'},
        {'name': 'dense', 'type': 'float32s'},
        {'name': 'sparse', 'type': 'general'}
]
indexes = [
  {'name': 'dense_index', 'type': 'hnsw', 'column': 'dense', 'params': {'dims': 10, 'metric': 'L2'}},
  {'name': 'sparse_index', 'type': 'bm25', 'column': 'sparse', 'params': {'k': 1.25, 'b': 0.75}},
]

table = database.create_table("example", schema=schema, indexes=indexes)

### insert data

df = pd.DataFrame({
'id': range(1000),
'sym': np.random.choice(['AAA', 'BBB'], 1000),
'dense': [x.astype('float32') for x in np.random.rand(1000, 10)],
'sparse': [{int(y + 1): 1 for y in np.random.choice(range(1200), x + 1, replace=False)} for x in np.random.choice(range(120), 1000)]})

table.insert(df)

### Dense search

result = table.search(vectors={'dense_index': [np.float32([0.1,0,0,0,0,0,0,0,0,0])]}, n=3)
print(result)

### Sparse search

result = table.search(vectors={'sparse_index': [{1:1,4:1,34:2,2:1}]}, n=3)
print(result)

### Hybrid search

index_params = {
  'dense_index': {'weight': 0.6},
  'sparse_index': {'weight': 0.4}
}
result = table.search(vectors={'dense_index': [np.float32([0.1,0,0,0,0,0,0,0,0,0])], 'sparse_index': [{1:1,4:1,34:2,2:1}]}, n=3, index_params=index_params)
print(result)

### cleanup
table.drop()
```

Next steps
----------

Now that you're familiar with hybrid search, you can do the following:

*   Try a [Hybrid Search in our sample project](https://kdb.ai/learning-hub/samples/hybrid-search-sample/).
*   Review our articles on [Improving Accuracy](https://kdb.ai/learning-hub/articles/improve-accuracy-with-hybrid-search/) with Hybrid Search and [Optimizing Hyperparameters](https://kdb.ai/learning-hub/articles/optimizing-hyperparameters-in-hybrid-search/) in Hybrid Search.
*   Watch our videos to [learn more about Hybrid search](https://kdb.ai/learning-hub/video-lessons/hybrid-search-in-vector-databases/) or [this video tutorial](https://kdb.ai/learning-hub/video-lessons/hybrid-search-tutorial-for-vector-databases/) to get started with your own real data.
*   Move on to perform a [Transformed Temporal Similarity Search](https://code.kx.com/kdbai/latest/use/transformed-tss.html) and/or a [Non-Transformed Temporal Similarity Search](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html).
