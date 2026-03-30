# Source: https://code.kx.com/kdbai/latest/use/ingestion.html

Title: KDB.AI Ingest Data - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/ingestion.html

Markdown Content:
How to Ingest Data in KDB.AI
----------------------------

_This page covers how to insert randomly generated data into your KDB.AI database._

An optional list of metadata columns is included for each document; this enhances filtering during querying and searching.

Real-world applications often involve substantially higher-dimensional vectors than our example.

Generate data
-------------

Prior to ingestion, retrieve the table you want to load the data into and prepare the data for insertion:

Python JSON q

```
import numpy as np 
import pandas as pd 
import kdbai_client as kdbai

session = kdbai.Session()

session.database('default').tables # check created tables

# Connect with the KDB.AI table
documents = session.database('default').table("documents")
documents.query()

# Generate data
n_rows = 20000
numDim = 12

data = pd.DataFrame({
    'id': np.arange(n_rows, dtype='int16'),
    'tag': np.random.choice([True, False], n_rows),
    'author': [f'author{i}' for i in range(n_rows)],
    'length': np.random.randint(0, 1000, n_rows, dtype='int32'),
    'content': [f'document{i}' for i in range(n_rows)],
    'createdTime': pd.date_range(start='2020-01-01', periods=n_rows, freq='1D'),
    'embeddings': [np.random.rand(numDim).astype('float32') for _ in range(n_rows)]
})
```

JSON data can be generated in any language. In the example below `.j.j` from `q` is used to generate example data. The output of `.j.j` is used as a standard for how table data should be formatted.

```
n: 2000;
// Note: for simplicity we do not randomize content, createdTime, or embeddings
rows:.j.j flip `id`tag`author`length`content`createdTime`embeddings!(n?0h;n?0b;n?`bob`joe`jill;n?1000;n#enlist .Q.an;n#.z.p;n#enlist "e"$til 12);
```

An example preview of this data, where `n` is `2`, would be:

```
[
  {
    "id": 21212,
    "tag": true,
    "author": "jill",
    "length": 68,
    "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
    "createdTime": "2023-10-11T00:00:00.000000000",
    "embeddings": [0,1,2,3,4,5,6,7,8,9,10,11]
  },
  {
    "id": 19376,
    "tag": false,
    "author": "joe",
    "length": 626,
    "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
    "createdTime": "2023-10-11T00:00:00.000000000",
    "embeddings": [0,1,2,3,4,5,6,7,8,9,10,11]
  }
]
```

```
n:3;
t:flip `id`tag`author`length`content`createdTime`embeddings!(n?0h;n?0b;n?`bob`joe`jill;n?1000;n#enlist .Q.an;n#.z.p;n#enlist "e"$til 12);
```

For the insert, only include fields that exist in the target table. In the case of metadata columns with null values, KDB.AI handles the insert operation gracefully. However, this approach is not applicable for vector columns, as nulls are not accepted in those cases.

Ensure precise alignment of data types with the table schema to avoid exceptions.

### Choose the JSON row format

JSON supports the following types:

*   String
*   Number
*   Object
*   Array
*   Boolean
*   Null

When formatting JSON row data, it must match one of these types based on the database’s column schema. Databases often differentiate between numeric types such as `long`, `real`, `float`, `int`, and `short`, whereas JSON only has a generic `Number` type. Therefore, if you need to store a specific numeric type such as `long` in the database, you must define `long` in the schema and send the JSON `Number` in the payload. The database then converts the JSON `Number` to the specified type according to the schema.

For example, a table with a boolean column requires the row data to be a literal boolean value of `true` or `false`. Parsing values from the string `true` or `false`, or from the numbers `0` and `1`, is not supported.

Use the corresponding [JSON formats for database types](https://code.kx.com/kdbai/latest/reference/supported-types.html#database-types-and-json-formats).

If null is provided for a value, it is replaced by its relevant empty string or largest negative number.

JSON null is not supported within arrays. If you require a data point to be numerically null, set the value to the largest negative number appropriate.

For columns containing multiple data types, no conversion takes place. All numbers are set as `float`. This results in suboptimal data storage and compression.

JSON row types vs. metadata types

It's important to differentiate between JSON row types and index metadata types. JSON row types are used to format the data rows for insertion based on the table schema. In contrast, metadata types provide additional descriptive information about the data to enhance filtering and searching capabilities.

Use metadata types to define the attributes of each document. These types are linked to specific columns in your table schema and are used to store additional information that aids in data retrieval. Metadata types can include various data types such as dates, strings, and numbers.

To learn more about metadata types and how they can be utilized, refer to this [Metadata filtering](https://kdb.ai/learning-hub/samples/metadata-filtering/) article.

Insert
------

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
  "payload": [
    {
      "id": 21212,
      "tag": true,
      "author": "jill",
      "length": 68,
      "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
      "createdTime": "2023-10-11T00:00:00.000000000",
      "embeddings": [0,1,2,3,4,5,6,7,8,9,10,11]
    },
    {
      "id": 19376,
      "tag": false,
      "author": "joe",
      "length": 626,
      "content": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
      "createdTime": "2023-10-11T00:00:00.000000000",
      "embeddings": [0,1,2,3,4,5,6,7,8,9,10,11]
    }
  ]
}
```

Ensure that the `@` sign is included before the filename, otherwise, the file becomes uri-encoded.

```
curl -s -X POST -H 'Content-Type: application/json' -d @insert.json localhost:8081/api/v2/databases/default/tables/documents/insert
```

```
r:gw(`insertData;`database`table`payload!(`default;`documents;t));
```

If the supplied embeddings are not the same dimension as the table, the operation fails.

When inserting data into a schema, ensure that embeddings are generated beforehand, as no embedding is done during the insertion step. For Transformed TSS, the provided embeddings are compressed to the target dimensionality and then stored. Always start with the full/raw embeddings before any compression or reduction.

When working with text, chunking refers to how source material is broken up prior to passing to a model for the creation of embeddings. For example, you can choose between:

*   Processing an entire document and generate a single embedding
*   Separating the document into paragraphs or sentences and have embeddings at that level.

Typically, you would chunk sentences, which results in multiple rows per document.

Batch inserts
-------------

KX recommends inserting data in batches, by passing a dataframe to the insert method. This can significantly improve performance in some cases. For large dataframes, you can split the `df`. The fewer batches sent, the more efficient the inserts are.

Python

```
from tqdm import tqdm 
n = 200  # batch size

for i in tqdm(range(0, data.shape[0], n)):
    documents.insert(data[i:i+n].reset_index(drop=True))
```

Insert data with caution, the current version of KDB.AI does not support individual record updates or deletions.

Note that **batch** and **chunk** are not synonymous:

*   **Chunking** is determined by the decision taken on how the source text is broken down for embedding purposes.
*   **Batching** is determined by the total size of your dataframe and the number of rows that can be inserted into KDB.AI at a time.

Tip: Chunk as appropriate, but pack as much data into each batch you insert as possible.

Train index
-----------

The [IVF](https://code.kx.com/kdbai/latest/use/supported-indexes.html#ivf) and [IVFPQ](https://code.kx.com/kdbai/latest/use/supported-indexes.html#ivfpq) indexes need training before using them for similarity searching. The `train` function operates in a manner similar to the `insert` function, except the payload provided is used for the primary purpose of training the index, without the data from the payload being inserted for query into the index.

Python REST q

```
# Following a similar schema but with the index set as ivfpq
schema = [
        {'name': 'id', 'type': 'int16'},
        {'name': 'tag', 'type': 'bool'},
        {'name': 'author', 'type': 'str'},
        {'name': 'length', 'type': 'int32'},
        {'name': 'content', 'type': 'str'},
        {'name': 'createdTime', 'type': 'datetime64[ns]'},
        {'name': 'embeddings', 'type': 'float32s'},
        ]
indexes =[{
              "name": "vectorIndex", 
              "column": "embeddings",
              "type": "ivfpq", 
              "params": {"metric": "L2", 'nsplits':4},
              }]

documentsIVFPQ = session.database('default').create_table('documentsIVFPQ', schema, indexes=indexes)

# Train on a subset of the data
documentsIVFPQ.train(data[:10000])

# Return: 'True'
```

Training data is provided [identically to an insert](https://code.kx.com/kdbai/latest/use/ingestion.html#insert), except that the URL is `/api/v2/train`.

To train an index using the same data from the insert example, `insert.json`, update the name of the table and run:

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables \
--header 'Content-Type: application/json' \
--data '{  
  "table":"documentsIVFPQ",
  "schema": [
    {"name": "id", "type": "short"},
    {"name": "tag", "type": "boolean"},
    {"name": "author", "type": "char"},
    {"name": "length", "type": "int"},
    {"name": "content", "type": "char"},
    {"name": "createdTime", "type": "timestamp"},
    {"name": "embeddings", "type": "floats"}
  ],
  "indexes":[
        {
            "name":"vectorIndex",
            "type": "ivfpq",
            "column":"embeddings",
            "params":{
                "metric": "L2",
                "nsplits": 4
            }
      }
      ]
    }' | jq .

curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/documentsIVFPQ/train \
--header 'Content-Type: application/json' \
--data @insert.json | jq .
```

```
`gw set hopen 8082;

dims:16;
mySchema:flip `name`type!(`id`tag`author`length`content`createdTime`embeddings;`h`b`s`j`C`p`E);

idx:`name`column`type`params!(enlist `myVectorIndex;enlist `embeddings;enlist `ivfpq;enlist (`metric`nsplits)!(`L2;4));

// create
p:`database`table`schema`indexes!(`default;`documentsIVFPQ;mySchema;flip idx);
gw(`createTable;p);

// train
n:20000; 
t:flip `id`tag`author`length`content`createdTime`embeddings!(n?0h;n?0b;n?`bob`joe`jill;n?1000;n#enlist .Q.an;n#.z.p;n#enlist "e"$til 12);

r:gw(`trainData;`database`table`payload!(`default;`documentsIVFPQ;t));
```

Training must occur before data insertion. Vectors used for training are not included in the index and they won't be available for search operations. [How to choose training data and vector embeddings](https://code.kx.com/kdbai/latest/use/supported-indexes.html#how-to-choose-training-data-and-vector-embeddings).

Next steps
----------

Now that you have data in your table, you can [query it](https://code.kx.com/kdbai/latest/use/query.html).
