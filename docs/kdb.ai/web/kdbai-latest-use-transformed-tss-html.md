# Source: https://code.kx.com/kdbai/latest/use/transformed-tss.html

Title: Transformed Temporal Similarity Search - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/transformed-tss.html

Markdown Content:
How to Perform a Transformed Temporal Similarity Search in KDB.AI
-----------------------------------------------------------------

_This page details how to execute a Transformed TSS search in KDB.AI._

Before we dive in, go to the [Understanding Transformed TSS search](https://code.kx.com/kdbai/latest/reference/transformed-tss.html) page to make sure you're familiar with concepts like dimensionality reduction, timeseries windows, and fast moving vectors.

Setup
-----

To perform a Transformed TSS search, make sure you have:

*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download/) license
*   Installed the latest version of KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
*   [Python Client](https://code.kx.com/kdbai/latest/reference/python-client.html)

1. Define your schema, indexes and Embedding attribute parameters
-----------------------------------------------------------------

To use the Transformed TSS method, the column to be searched needs to have vectors (not scalars) in each entry. For general schema setup details see the [Manage Tables](https://code.kx.com/kdbai/latest/use/manage-tables.html) page.

For indexes, the `dims` argument is no longer required, as data in any length will be embedded to the size of the embeddings' dimension.

When the table is created, add an extra `embedding_configurations` for Python (or `embeddingConfigurations` for q) attribute to your create function.

2. Embedding Configurations
---------------------------

| **Option** | **Description** | **Type** | **Required** | **Default** | **Allowed values** |
| --- | --- | --- | --- | --- | --- |
| `dims` | Reduced dimensionality of the data desired | int | true | 8 | 1,2,3,... |
| `type` | Embedding method to use | str | true | None | 'tsc' |
| `on_insert_error` | The action to take if there are records that would error on insertion. Either reject the batch or skip the erroneous record | string | false | 'reject_all' | 'reject_all', 'skip_row' |

A window fails to insert if the dimensionality is already less than the dimensionality specified by `dims`.

The selection of `dims` depends largely on the complexity of the data in the window; the more movement in the window, the larger this number should be.

Python REST q

```
indexes = [ {"name": "myVectorIndex", "type": "flat", 
                "params": {"metric": "L2"},
                "column": "price"}]

embedding_conf = {'price': {"dims": 8, "type": "tsc", "on_insert_error": "reject_all" }}

table_TSC = session.database('default').create_table('tradeTSC', schema, indexes=indexes, embedding_configurations=embedding_conf)
```

```
curl -X POST http://localhost:8082/api/v2/databases/default/tables \
--header 'Content-Type: application/json' \
--data '{  
"table":"tradeTSC",
"schema": [
    {
    "name": "sym",
    "type": "float"
    },
    {
    "name": "price",
    "type": "floats"
    }
],
"indexes":[
        {
            "name":"myVectorIndex",
            "type": "flat",
            "column":"price",
            "params":{
                "metric": "L2"
            }
    }
    ],
"embeddingConfigurations":{
    "price": {
                "dims": 3, 
                "type": "tsc", 
                "on_insert_error": "reject_all" 
                }
        }
    }'
```

```
idx:`name`column`type`params!(enlist `myVectorIndex;enlist `price;enlist `flat;enlist (enlist `metric)!(enlist `L2));
ebd:enlist[`price]!enlist (`dims`type`on_insert_error)!(eDims;`tsc;`skip_row);

p:`database`table`schema`indexes`embeddingConfigurations!(`default;`tradeTSC;mySchema;flip idx;ebd);
```

3. Follow our index recommendations
-----------------------------------

Transformed TSS produces the best results using [HNSW, IVF, and FLAT indexes](https://code.kx.com/kdbai/latest/use/supported-indexes.html). The added layer of product quantisation used in IVFPQ severely impacts the quality of the results returned.

Example: Transformed TSS search

Python q

```
# In this example we generate dummy market data using PyKX, create an index using the TSC feature exposed by KDB.AI,
# and search for a pattern of interest in the data

# Imports

# KX Dependencies
import pykx as kx
import kdbai_client as kdbai

# Other Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.stride_tricks import sliding_window_view
from matplotlib.text import Text
from tqdm import tqdm

import psutil

# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")

# Report memory usage of Python + KDB.AI

def get_memory_usage():
    virtual_memory = psutil.virtual_memory()
    return virtual_memory.used / (1024 ** 2)  # Memory usage in megabytes

# Generate Dummy Data

D = 10 # Sliding Window Size
kx.q['D'] = D
kx.q('\S 100')
kx.q('''
gen_marketTrades: { [num;ticker]
    :marketTrades:: update price:{max(abs -0.5 + x + y;5.0)}\[first price; count[i]?1.0] from 
                        `time xasc ([] time:(.z.d-30)+num?15D00:00:00; 
                        sym:num#ticker; 
                        qty:D*1+num?10;
                        price:num#25.0)
    };
''')
df1 = kx.q('gen_marketTrades[500;`AAA]').pd() # Create records for AAA
df2 = kx.q('gen_marketTrades[500;`BBB]').pd() # Create records for BBB
# Concatenate the DataFrames
df = pd.concat([df1, df2], ignore_index=True)

print(f"System Memory Usage: {get_memory_usage():.2f} MB")

# Method 1: Only Windowing - This method is shown as a point of comparison for the TSC method

# Vector Construction

# Create the vector column
vecdf = df.groupby(['sym']).apply(
    lambda x: pd.DataFrame({
        'sym': x['sym'].iloc[0],
        'time': sliding_window_view(x['time'], D)[:, 0],  # Adjusted to keep the last time in the window
        'price': list(sliding_window_view(x['price'], D))
    })
).reset_index(drop=True).reset_index()

vecdf.head()
print(f"System Memory Usage: {get_memory_usage():.2f} MB")

# Index Construction
session = kdbai.Session()

session.database('default').tables

schema = [
            {"name": "index", "type": "int64"},
            {"name": "sym", "type": "str"},
            {"name": "time", "type": "datetime64[ns]"},
            {"name": "price", "type": "float32s"},
            ]

indexes = [ {"name": "myVectorIndex", "type": "flat", 
                "params": {"metric": "L2"},
                "column": "price"}]

embedding_conf = {'price': {"dims": 8, "type": "tsc", "on_insert_error": "reject_all" }}

table_TSC = session.database('default').create_table('tradeTSC', schema, indexes=indexes, embedding_configurations=embedding_conf)

# Index Population
table_TSC.insert(vecdf.reset_index(drop=True))

# Search

# We take the hundredth vector and use that as our search vector
q = vecdf['price'][100].tolist()

res = table_TSC.search(vectors={'myVectorIndex': [q]}, n=10)[0]
print(res)

print(f"System Memory Usage: {get_memory_usage():.2f} MB")
```

```
`gw set hopen 8082;
eDims:3;
mySchema:flip `name`type!(`id`myDate`time`tag`price`text;`j`d`p`s`F`C);
idx:`name`column`type`params!(enlist `myVectorIndex;enlist `price;enlist `flat;enlist (enlist `metric)!(enlist `L2));
ebd:enlist[`price]!enlist (`dims`type`on_insert_error)!(eDims;`tsc;`skip_row);

// create
p:`database`table`schema`indexes`embeddingConfigurations!(`default;`tradeTSC;mySchema;flip idx;ebd);
gw(`createTable;p);
gw(`query;`database`table!(`default;`tradeTSC));

// insert
N:10; 
t:([] id:til N; myDate:2015.01.01 + asc N?100j; time:asc N?0p; tag:N?`3; price:(eDims + N?10j)?\:1f; text:{rand[16]?" "} each til N);
count each t[`price]; // Note that price have various lengths
r:gw(`insertData;`database`table`payload!(`default;`tradeTSC;t));
c:gw(`query;`database`table!(`default;`tradeTSC));

// search
q:sums neg[0.5]+50?1f;
tqry:enlist[`myVectorIndex]!enlist enlist q;
k:5;
rS:gw(`search;`database`table`vectors`n!(`default;`tradeTSC;tqry;k));
first rS[`result];
```

Next steps
----------

Now that you're familiar with how to perform a Transformed TSS search, move on to the following:

*   Try a Transformed TSS in our [sample project](https://kdb.ai/learning-hub/samples/transformed-temporal-similarity-search-sample/).
*   Review our article on [discovering time series insights](https://kdb.ai/learning-hub/articles/discovering-time-series-insights-with-temporal-similarity-search/) with Temporal Similarity Search.
*   Watch our video to [learn more about Transformed TSS](https://kdb.ai/learning-hub/video-lessons/temporal-similarity-search-overview/) or our [video tutorial](https://kdb.ai/learning-hub/video-lessons/temporal-similarity-search-overview/) to get started with your own real data.
*   Move on to [perform a Non-transformed TSS](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html).
