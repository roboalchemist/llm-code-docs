# Source: https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html

Title: Quickstart for KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html

Markdown Content:
Quick start
-----------

This guide outlines the essential steps to using KDB.AI. Before proceeding, ensure your environment is set up as described in [Prerequisites](https://code.kx.com/kdbai/latest/gettingStarted/pre-requisites.html) and has the necessary information to connect to [KDB.AI Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html).

Required imports
----------------

```
import sys
import numpy as np
import pandas as pd
import kdbai_client as kdbai
from logging import Logger
```

 Connect to the local server, create a session, and connect to the database: 

```
# Local server
session = kdbai.Session(endpoint='http://localhost:8082')

# Get the database connection. Default database name is 'default'
database = session.database('default')
```

Set up table schema and configure the index
-------------------------------------------

Before creating a table you must first set the table schema. This is defined as a python dictionary containing a list of columns. For each column you must define the name and a `type`. Full schema definition specifications are available in the [manage tables](https://code.kx.com/kdbai/latest/use/manage-tables.html) section.

Python REST

```
# Set up the schema and index for the KDB.AI table, specifying embeddings column with 8 dimensions, Euclidean Distance, and flat index
schema = [
    {"name": "id", "type": "str"},
    {"name": "vectors", "type": "float32s"}
]

# Define the index
index = [
    {
        "name": "flat_index",
        "type": "flat",
        "column": "vectors",
        "params": {"dims": 8, "metric": "L2"},
    }
]
```

```
# Using a local server
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

curl -X "POST" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables -d @table.json
```

The request body is in a file called `_table.json_`:

```
{
"table": "quickstartkdbai",
"schema": [
    {"name": "id", "type": "char"},
    {"name": "vectors", "type": "floats"}
],
"indexes": [ 
    {"name": "vectorIndex", "type": "flat", 
    "params": {"dims": 8, "metric": "L2"},
    "column": "vectors"}
]
}
```

Create a new table
------------------

After defining the schema and index configuration, you can create the table in the default database. The associated index will be automatically generated based on the configuration provided.

Python REST

```
# Create the table in the default database
table = database.create_table(
        table="quickstartkdbai",
        schema=schema,
        indexes=index
    )
```

```
# Using a local server
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

curl -X "POST" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" \
-s $KDBAI_ENDPOINT/api/v2/databases/default/tables -d @table.json
```

Once created, the table is ready to accept data. In the next step, you will insert vector embeddings into the table and verify that the records have been stored correctly.

Add data to your table
----------------------

Generate an array of five 8-dimensional vectors that will be the vector embeddings:

Python REST

You can then add these to the [pandas dataframe](https://www.w3schools.com/python/pandas/pandas_dataframes.asp) ensuring the column names/types match the table schema.

```
# Insert a row of data with sample vectors
try:
    ids = ['h', 'e', 'l', 'l', 'o']  # Example ID values
    vectors = np.random.rand(40).astype(np.float32).reshape(5,8)
    df = pd.DataFrame({"id": ids, "vectors": list(vectors)})
    table.insert(df)
# Check we have our row
    if(len(table.query().values) == 5):
        f"Row with ID {id} in table {table_name} was inserted successfully"
    else:
        Logger.info(f"Could not insert a row with ID {id} into table {table_name}.")
except Exception as e:
    f'Exception {e} occurred trying to insert a row with ID {id} into table {table_name}.'
    sys.exit(1)
finally:
    pass
```

JSON data can be generated in any language. Below [`.j.j`](https://code.kx.com/q/ref/dotj/#jj-serialize) from [`q`](https://code.kx.com/q/) is used to generate example data and write to a file to `insert.json`.

```
# start the kdb+ binary with the q command
q
# run the following on the 'q)' prompt
`insert.json 0: enlist .j.j `table`rows!(`quickstartkdbai;([] id:"hello";vectors:(5;8)#(5*8)?1e))
\\
```

The contents of the generated file should be:

```
$ cat insert.json
{
    "payload": [
        {"id":"h","vectors":[0.3927524,0.5170911,0.5159796,0.4066642,0.1780839,0.3017723,0.785033,0.5347096]},
        {"id":"e","vectors":[0.7111716,0.411597,0.4931835,0.5785203,0.08388858,0.1959907,0.375638,0.6137452]},
        {"id":"l","vectors":[0.5294808,0.6916099,0.2296615,0.6919531,0.4707882,0.6346716,0.9672399,0.2306385]},
        {"id":"l","vectors":[0.949975,0.439081,0.5759051,0.5919004,0.8481566,0.389056,0.391543,0.08123546]},
        {"id":"o","vectors":[0.9367504,0.2782122,0.2392341,0.1508133,0.1567317,0.9785,0.7043314,0.9441671]}
    ]
}
```

As above, if you pipe the result to a tool like `jq` you can see the result pretty printed.

```
$ cat insert.json | jq
{
  "payload": [
    {
      "id": "h",
      "vectors": [
        0.3927524,
        0.5170911,
        0.5159796,
        0.4066642,
        0.1780839,
        0.3017723,
        0.785033,
        0.5347096
      ]
    },
...
```

```
# Using a local server
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

# insert data from file insert.json
curl -X "POST" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables/quickstartkdbai/insert  -d @insert.json
```

Query the table
---------------

Use the following command to query data from the table.

Python REST

The `query` function accepts a wide range of arguments to make it easy to filter, aggregate, and sort. Run `?table.query` to see them all.

```
data = table.query()
print(f'Table data:\n {data}')
```

```
# Using a local server
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

curl -H 'Content-Type: application/json' -H "X-Api-Key: $KDBAI_TOKEN" $KDBAI_ENDPOINT/api/v2/databases/default/tables/quickstartkdbai/query -d '{"filter" : []}'
```

As above, if you pipe the result to a tool like `jq` you can see the result pretty printed.

```
curl -H 'Content-Type: application/json' -H "X-Api-Key: $KDBAI_TOKEN" $KDBAI_ENDPOINT/api/v2/databases/default/tables/quickstartkdbai/query -d '{"filter" : []}' | jq
"result": [
{
  "id": "h",
  "vectors": [
    0.6594225,
    0.5260468,
    0.2424757,
    0.2224251,
    0.6360764,
    0.05000889,
    0.2665702,
    0.9261618
  ]
},
...
```

Run similarity search
---------------------

Search for the nearest neighbors using the following command:

The dimension of input query vectors **must** match the vector embedding dimensions in the table, defined in schema above.

Python REST

```
# Run a similarity search
results = table.search(vectors={'flat_index':[[0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]}, n=3)
print(f'Similarity search results: {results}\n\n')
```

```
# Using a local server
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

curl -s -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" $KDBAI_ENDPOINT/api/v2/databases/default/tables/quickstartkdbai/search -d '{"vectors":{"vectorIndex": [[0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]}, "n":3,"options":{"distanceColumn":"dist"}}'
```

As above, if you pipe the result to a tool like `jq` you can see the result pretty printed.

```
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

curl -s -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" $KDBAI_ENDPOINT/api/v2/databases/default/tables/quickstartkdbai/search -d '{"vectors":{"vectorIndex": [[0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]}, "n":3,"options":{"distanceColumn":"dist"}}' | jq
{
  "result": [
    {
      "id": "h",
      "vectors": [
        0.6594225,
        0.5260468,
        0.2424757,
        0.2224251,
        0.6360764,
        0.05000889,
        0.2665702,
        0.9261618
      ]
    },
...
```

The closest matching neighbors for the query vector are returned along with the calculation of [L2 (Euclidean Distance) similarity](https://code.kx.com/kdbai/latest/reference/metrics.html#euclidean-distance-represented-as-l2).

Retrieve a list of tables
-------------------------

Display a list of tables, including your recently created table, using the following command:

Python REST

```
print(database.tables)
# This command should return an array with the table: [KDBAI table "quickstartkdbai"]
```

```
# Using a local server
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

curl -X "GET" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables
```

If you pipe the result to a tool such as `jq` you can see the result pretty printed:

```
curl -s localhost:8081/api/v2/databases | jq
{
  "result": {
    "database": "default",
    "tables": [
      "quickstartkdbai"
    ]
  }
}
```

Delete table
------------

Use the following command when you want to delete a table:

Python REST

```
# Clean up our table
if(table in database.tables):
    database.table(table_name).drop()
```

```
# Using a local server
KDBAI_ENDPOINT='http://localhost:8081'
KDBAI_TOKEN=''

curl -X "DELETE" -H "Content-Type: application/json" -H "X-Api-Key: $KDBAI_TOKEN" -s $KDBAI_ENDPOINT/api/v2/databases/default/tables/quickstartkdbai
```

Once you delete a table, you cannot use it again.

In KDB.AI, when you delete a table, the associated index is also removed.

Next steps
----------

Now that you are successfully making indexes with KDB.AI, you can start inserting your own data and analysing it:

*   [Manage tables](https://code.kx.com/kdbai/latest/use/manage-tables.html)
*   [Query data](https://code.kx.com/kdbai/latest/use/query.html)
*   [Conduct a similarity search](https://code.kx.com/kdbai/latest/use/search.html)

Samples
-------

You can also explore the following:

*   Samples on the [Learning Hub](https://kdb.ai/learning-hub#Samples)
*   [GitHub repository](https://github.com/KxSystems/kdbai-samples/tree/main/quickstarts)
*   The [Quickstart notebook](https://github.com/KxSystems/kdbai-samples/blob/main/quickstarts%2Fpython_quickstart.ipynb) (run it in [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/quickstarts%2Fpython_quickstart.ipynb))
