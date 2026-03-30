# Source: https://code.kx.com/kdbai/latest/use/non-transformed-tss.html

Title: Non-Transformed Temporal Similarity Search - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/non-transformed-tss.html

Markdown Content:
How to Perform a Non-Transformed TSS Search in KDB.AI
-----------------------------------------------------

_This page details how to execute a Non-Transformed Temporal Similarity Search (Non-Transformed TSS) search in KDB.AI._

To use the Non-Transformed TSS search, you don't need to extract vectors from the time series. The algorithm performs the following actions:

1.   Takes simple time series (numerical sequence stored in a kdb+ column) as input.
2.   Scans the time series with a sliding window (of the same size as the query vector; size can be changed between queries).
3.   Computes the list of distances between the query vector and each occurrence of the sliding window.
4.   Returns the k-nearest neighbors.

Setup
-----

Before you start, make sure you have:

*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download/) license
*   Installed the latest version of KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
*   [Python Client](https://code.kx.com/kdbai/latest/reference/python-client.html)

To store and search temporal data using the Non-Transformed TSS method, follow these steps:

1.   [Import dependencies](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html#1-import-dependencies)
2.   [Create schema](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html#2-create-schema)
3.   [Insert data](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html#3-insert-data)
4.   [Perform searches](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html#4-perform-searches)

1. Import dependencies
----------------------

Start by importing the following dependencies:

Python

```
import sys
import kdbai_client as kdbai
from pprint import pprint # for pretty printing
import pandas as pd
import numpy as np
```

2. Create schema
----------------

Open a KDB.AI session to create a schema:

Python REST q

```
session = kdbai.Session()
session.database('default').tables # check what tables are already created

schema = [
            {"name": "realTime", "type": "datetime64[ns]"},
            {"name": "sym", "type": "str"},
            {"name": "price", "type": "float64"},
            {"name": "priceReals", "type": "float32"},
            {"name": "volumeLongs", "type": "int64"},
            {"name": "volumeInts", "type": "int32"},
            {"name": "volumeShorts", "type": "int16"},
            {"name": "size", "type": "int32"},
            ]

table = session.database('default').create_table('trade', schema)
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables \
--header 'Content-Type: application/json' \
--data '{  
"table":"trade",
"schema": [
    {
    "name": "realTime",
    "type": "timestamp"
    },
    {
    "name": "sym",
    "type": "symbol"
    },
    {
    "name": "price",
    "type": "float"
    },
    {
    "name": "priceReals",
    "type": "real"
    },
    {
    "name": "volumeLongs",
    "type": "long"
    },
    {
    "name": "volumeInts",
    "type": "int"
    },
    {
    "name": "volumeShorts",
    "type": "short"
    },
    {
    "name": "size",
    "type": "int"
    }
]
    }' | jq .
```

```
`gw set hopen 8082;

dims:10;
mySchema:flip `name`type!(`realTime`sym`price`priceReals`volumeLongs`volumeInts`volumeShorts`size;`p`s`f`e`j`i`h`j);

// create
p:`database`table`schema!(`default;`trade;mySchema);
gw(`createTable;p);
```

or alternatively, if you have an existing [kdb+ table on disk](https://code.kx.com/q/learn/brief-introduction/) and would like to create from it, run the command below:

Python REST q

```
table = session.database('default').create_table(table="trade",external_data_references=[{"path":b'/db', "provider" :"kx"}])
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables \
--header 'Content-Type: application/json' \
--data '{  
"table":"trade",
"externalDataReferences": [{
    "path": "/db",
    "provider": "kx"
    }]
    }' | jq .
```

```
`gw set hopen 8082;

ref:enlist `path`provider!("/db";`kx);
p:`database`table`externalDataReferences!(`default;`trade;ref);
gw(`createTable;p);
```

3. Insert data
--------------

Create the data `df` that contains your time series data and the numerical column(s) you wish to search:

Python q

```
numRows = 100

df = pd.DataFrame()
df['realTime'] = sorted(np.random.randint(sys.maxsize, size=numRows).astype('datetime64[ns]'))
df['sym'] = np.random.choice(['aaa', 'bbb', 'ccc'], size=numRows).astype('str')
df['price'] = [x.astype('float64') for x in np.random.rand(numRows)]
df['priceReals'] = [x.astype('float32') for x in np.random.rand(numRows)]
df['volumeLongs'] = [x.astype('int64') for x in np.random.randint(0, 100, numRows)]
df['volumeInts'] = [x.astype('int32') for x in np.random.randint(0, 100, numRows)]
df['volumeShorts'] = [x.astype('int16') for x in np.random.randint(0, 100, numRows)]
df['size'] = np.random.randint(100, size=numRows).astype('int32')
```

```
splits:34 33 33;
N:sum splits; 
t:([] realTime:asc N?0p;sym:raze {x#y}'[splits;`aaa`bbb`ccc]; price:N?1f; priceReals:"e"$N?1f; volumeLongs:"j"$N?1f; volumeInts:"i"$N?1f; volumeShorts:"h"$N?1f; size:til N);
```

Insert `df` into the table:

Python REST q

```
table.insert(df)
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/insert \
--header 'Content-Type: application/json' \
--data '{  
    "payload": [
            {
            "realTime": "2001.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 1.1,
            "priceReals": 14.7,
            "volumeLongs": 27,
            "volumeInts": 37,
            "volumeShorts": 47,
            "size": 42
            },
            {
            "realTime": "2002.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 2.2,
            "priceReals": 14.7,
            "volumeLongs": 27,
            "volumeInts": 37,
            "volumeShorts": 47,
            "size": 36
            },
            {
            "realTime": "2003.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 3.4,
            "priceReals": 14.7,
            "volumeLongs": 27,
            "volumeInts": 37,
            "volumeShorts": 47,
            "size": 24
            },
            {
            "realTime": "2004.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 4.7,
            "priceReals": 14.7,
            "volumeLongs": 27,
            "volumeInts": 37,
            "volumeShorts": 47,
            "size": 11
            },
            {
            "realTime": "2004.01.01D00:48:57.051633652",
            "sym": "bbb",
            "price": 4.7,
            "priceReals": 14.7,
            "volumeLongs": 27,
            "volumeInts": 37,
            "volumeShorts": 47,
            "size": 11
            }
        ]
    }' | jq .
```

```
r:gw(`insertData;`database`table`payload!(`default;`trade;t));
```

Run a query to check the contents of the table:

Python REST q

```
table.query()
```

```
curl -s -X POST localhost:8081/api/v2/databases/default/tables/trade/query | jq .
```

```
(gw(`query;`database`table!(`default;`trade)))[`result];
```

4. Perform searches
-------------------

Now you can conduct a temporal similarity search, (searching for a pattern in any one of the numerical columns), as below:

Python REST q

```
# single query search
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss")[0]

# multiple queries search
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4],[7,1,2,3,4,7,1,2,3,4]]}, n=3, type="tss")
```

```
# single query search
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss"
    }' | jq .

# multiple queries search
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.3,2.3,3.3], [1.4,2.4,3.4]]},
    "n": 1,
    "type": "tss"
    }' | jq .
```

```
tqry1:enlist[`price]!enlist enlist 1.1 1.2 1.3; // single query search
tqry2:enlist[`price]!enlist (1.1 1.2 1.3;2.1 2.2 2.3); // multiple queries search
first (gw(`search;`database`table`vectors`n`type!(`default;`trade;tqry1;10;`tss)))[`result];
(gw(`search;`database`table`vectors`n`type!(`default;`trade;tqry2;10;`tss)))[`result];
```

If the column contains fewer values than the pattern being searched for, add `force` to `options`. This is particularly useful when searching a partitioned table where some partitions may be empty or contain very few rows.

Python REST q

```
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=5, type="tss", options={'force':True})[0]
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"force" : true}
    }' | jq .
```

```
first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqry1;3;`tss;(enlist `force)!(enlist 1b))))[`result];
```

Another `option` is `normalize`. Use it to control whether the input data is standardized before similarity is calculated. By default, `normalize` is set to `True` (`1b` in q), meaning TSS performs [Z-normalization](https://en.wikipedia.org/wiki/Standard_score). To disable normalization, set `normalize` to `False` (`0b` in q).

### Outlier searches

You can also perform an outlier search of the numerical column by specifying a negative value for `n`:

Python REST q

```
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss")[0] # similarity search
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=-3, type="tss")[0] # outlier search
```

```
# similarity search
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss"
    }' | jq .

# outlier search
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": -1,
    "type": "tss"
    }' | jq .
```

```
tqry1:enlist[`price]!enlist enlist 1.1 1.2 1.3;
first (gw(`search;`database`table`vectors`n`type`searchBy`options!(`default;`trade;tqry1;10;`tss;`sym;enlist[`force]!enlist 1b)))[`result];
first (gw(`search;`database`table`vectors`n`type`searchBy`options!(`default;`trade;tqry1;10;`tss;`sym;`force`returnMatches!11b)))[`result];
```

### TSS search by group

Sometimes you may want to search by different categories instead of searching the input column as a whole. For example, in a trading use case the prices in the data would refer to different stocks, so we may want to perform our searches by symbol; or in IoT, we may want to search patterns by sensor.

To do this, add the `searchBy` argument to the search function.

Python REST q

```
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", search_by="sym", options={"force":True})[0]
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", search_by="sym", options={"force":True, "returnMatches":True})[0]
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "searchBy": ["sym"],
    "options":{"force" : true}
    }' | jq .

curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "searchBy": ["sym"],
    "options":{"force" : true, "returnMatches" : true}
    }' | jq .
```

```
first (gw(`search;`database`table`vectors`n`type`searchBy!(`default;`trade;tqry1;10;`tss)))[`result];
first (gw(`search;`database`table`vectors`n`type`searchBy`options!(`default;`trade;tqry1;10;`tss;`sym;enlist[`returnMatches]!enlist 1b)))[`result];
```

Tip: When using the `searchBy` option, the TSS searches for each group are parallelized using multiple threads.

The `searchBy` may return a lot more results than a simple TSS search. In the case of a splayed table, it will return `n` matches for each group. In the case of a partitioned table, it will return `n` matches for each group and each partition.

### Return the matched patterns

If you would like to obtain the original values of the captured data, add `returnMatches` to `options`. This inserts an extra column `nnMatch` in the result, which contains the original values:

Python REST q

```
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .
```

```
first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqry1;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result];
```

### Searching different data types

Apart from the standard `floats`, you can also search other columns of `reals`, `longs`, `ints` and `shorts`.

Python REST q

```
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]
table.search(vectors={'priceReals': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]
table.search(vectors={'volumeLongs': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]
table.search(vectors={'volumeInts': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]
table.search(vectors={'volumeShorts': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .

curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"priceReals" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .

curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"volumeLongs" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .

curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"volumeInts" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .

curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"volumeShorts" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .
```

```
tqryF:enlist[`price]!enlist enlist "f"$1.1 1.2 1.3; // single query search
tqryE:enlist[`priceReals]!enlist enlist "e"$1.1 1.2 1.3; // single query search
tqryJ:enlist[`volumeLongs]!enlist enlist "j"$1.1 1.2 1.3; // single query search
tqryI:enlist[`volumeInts]!enlist enlist "i"$1.1 1.2 1.3; // single query search
tqryH:enlist[`volumeShorts]!enlist enlist "h"$1.1 1.2 1.3; // single query search

first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqryF;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result];
first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqryE;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result];
first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqryJ;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result];
first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqryI;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result];
first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqryH;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result];
```

End-to-end example
------------------

By putting the snippets of create/insert/search together, you obtain a complete example of the Non-transformed TSS method.

Example: Non-Transformed TSS search

Python REST q

```
import sys
import kdbai_client as kdbai
from pprint import pprint # for pretty printing
import pandas as pd
import numpy as np

session = kdbai.Session()
session.database('default').tables # check what tables are already created

schema = [
            {"name": "realTime", "type": "datetime64[ns]"},
            {"name": "sym", "type": "str"},
            {"name": "price", "type": "float64"},
            {"name": "size", "type": "int32"},
            ]

table = session.database('default').create_table('trade', schema)

numRows = 40

df = pd.DataFrame()
df['realTime'] = sorted(np.random.randint(sys.maxsize, size=numRows).astype('datetime64[ns]'))
df['sym'] = np.random.choice(['aaa', 'bbb'], size=numRows).astype('str')
df['price'] = [x.astype('float64') for x in np.random.rand(numRows)]
df['size'] = np.random.randint(100, size=numRows).astype('int32')

table.insert(df)
table.query()

table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=5, type="tss")[0]
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4],[7,1,2,3,4,7,1,2,3,4]]}, n=5, type="tss")
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss")[0] # similarity search
table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=-3, type="tss")[0] # outlier search

table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]  # return original values
table.search(vectors={'size': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", options={"returnMatches":True})[0]  # search the integer column

table.search(vectors={'price': [[0,1,2,3,4,0,1,2,3,4]]}, n=3, type="tss", search_by = "sym",options={"force":True})[0]  # search by sym
```

```
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables \
--header 'Content-Type: application/json' \
--data '{  
"table":"trade",
"schema": [
    {
    "name": "realTime",
    "type": "timestamp"
    },
    {
    "name": "sym",
    "type": "symbol"
    },
    {
    "name": "price",
    "type": "float"
    },
    {
    "name": "size",
    "type": "int"
    }
]
    }' | jq .

curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/insert \
--header 'Content-Type: application/json' \
--data '{  
    "payload": [
            {
            "realTime": "2001.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 1.1,
            "size": 42
            },
            {
            "realTime": "2002.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 2.2,
            "size": 36
            },
            {
            "realTime": "2003.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 3.4,
            "size": 24
            },
            {
            "realTime": "2004.01.01D00:48:57.051633652",
            "sym": "aaa",
            "price": 4.7,
            "size": 11
            },
            {
            "realTime": "2004.01.01D00:48:57.051633652",
            "sym": "bbb",
            "price": 4.7,
            "size": 11
            }
        ]
    }' | jq .

curl -s -X POST localhost:8081/api/v2/databases/default/tables/trade/query | jq .

# single query search
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss"
    }' | jq .

# multiple queries search
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.3,2.3,3.3], [1.4,2.4,3.4]]},
    "n": 1,
    "type": "tss"
    }' | jq .

# outlier search
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": -1,
    "type": "tss"
    }' | jq .

# return matches
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .

# other data type
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"size" : [[1,3,7]]},
    "n": 1,
    "type": "tss",
    "options":{"returnMatches" : true}
    }' | jq .

# search by sym
curl -s -X POST http://localhost:8081/api/v2/databases/default/tables/trade/search \
--header 'Content-Type: application/json' \
--data '{  
    "vectors":{"price" : [[1.2,2.2,3.2]]},
    "n": 1,
    "type": "tss",
    "searchBy":["sym"],
    "options":{"force" : true}
    }' | jq .
```

```
`gw set hopen 8082;

dims:10;
mySchema:flip `name`type!(`realTime`sym`price`size;`p`s`f`j);

// create
p:`database`table`schema!(`default;`trade;mySchema);
gw(`createTable;p);

// insert
splits:34 33 33;
N:sum splits;
t:([] realTime:asc N?0p;sym:raze {x#y}'[splits;`aaa`bbb`ccc]; price:N?1f; size:til N);
r:gw(`insertData;`database`table`payload!(`default;`trade;t));

(gw(`query;`database`table!(`default;`trade)))[`result];

// search
tqry1:enlist[`price]!enlist enlist 1.1 1.2 1.3; // single query search
tqry2:enlist[`price]!enlist (1.1 1.2 1.3;2.1 2.2 2.3); // multiple queries search
tqryInt:enlist[`size]!enlist enlist 1 3 6; // single query search
first (gw(`search;`database`table`vectors`n`type!(`default;`trade;tqry1;10;`tss)))[`result];
(gw(`search;`database`table`vectors`n`type!(`default;`trade;tqry2;10;`tss)))[`result];
first (gw(`search;`database`table`vectors`n`type!(`default;`trade;tqry1;-10;`tss)))[`result]; // outlier search

first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqry1;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result]; // return original pattern
first (gw(`search;`database`table`vectors`n`type`options!(`default;`trade;tqryInt;10;`tss;enlist[`returnMatches]!enlist 1b)))[`result]; // search integer column

first (gw(`search;`database`table`vectors`n`type`searchBy`options!(`default;`trade;tqry1;10;`tss;`sym;enlist[`force]!enlist 1b)))[`result]; // return original pattern
```

As you can see in the above comparison, the main grammatical differences between running the Non-Transformed TSS search vs. other cases are:

|  | Non-Transformed TSS | Transformed TSS or Non-TSS |
| --- | --- | --- |
| `type` | `tss` | `flat`, `hnsw` etc. |
| `dims` | Not required | Required |
| Entries in the search column | Scalars | Vectors |
| Outlier search | Available | N/A |

We support all numerical types (for example, `float64`, `float32`, `int64`, `int32`, `int16`) as data and Non-Transformed TSS query. However, for numerical precision, the Non-Transformed TSS calculation uses `float64` in all cases.

Next steps
----------

Now that you're familiar with a Non-Transformed TSS search, we suggest the following:

*   Try a Non-Transformed TSS in our [sample project](https://kdb.ai/learning-hub/samples/non-transformed-temporal-similarity-search-sample/).
*   Review our article on [discovering time series insights](https://kdb.ai/learning-hub/articles/discovering-time-series-insights-with-temporal-similarity-search/) with Temporal Similarity Search.
*   Watch our video to [learn more about Non-Transformed TSS](https://kdb.ai/learning-hub/video-lessons/temporal-similarity-search-overview/) or our [video tutorial](https://kdb.ai/learning-hub/video-lessons/temporal-similarity-search-tutorial/) to get started with your own real data.
*   Discover some of our integrations like [LlamaIndex for RAG](https://code.kx.com/kdbai/latest/integrations/llamaindex.html) or [kdb+ for seamless time-series insights](https://code.kx.com/kdbai/latest/integrations/kdb.html.)
