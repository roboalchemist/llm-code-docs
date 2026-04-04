# Source: https://code.kx.com/kdbai/latest/integrations/kdb.html

Title: KDB.AI kdb+ - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/integrations/kdb.html

Markdown Content:
_This page explains how to integrate KDB.AI Server with kdb+._

The integration between kdb+ and KDB.AI Server helps you achieve the following:

*   Load and use existing kdb+ tables ([partitioned](https://code.kx.com/q/kb/partition/) or [splayed](https://code.kx.com/q/kb/splayed-tables/)) in KDB.AI Server.
*   Use KDB.AI Server via the q or Python APIs to perform similarity search on existing kdb+ datasets. 

KDB.AI kdb+/q

Kdb+ is a high-performance time-series database widely used in industries like finance for managing large datasets, particularly time-sensitive data. It is built to handle vast amounts of structured data efficiently. The q programming language is an integral part of kdb+ as its query language, designed for working with complex, high-speed analytics on large datasets. Q provides a concise syntax and is optimized for the operations typical in kdb+, such as querying and manipulating time-series data.

*   Watch this 15-episode series of [Intro to kdb+ and q](https://www.youtube.com/watch?v=8eoysfqO3UY&list=PLypX5sYuDqvrwBD2EMWadIMiTqJZmVsqm) tutorials
*   [Install kdb+](https://code.kx.com/q/learn/install/)
*   [Get started with q and kdb+](https://code.kx.com/q/learn/)

Benefits of Non-Transformed TSS on Splayed/Partitioned Tables
**How Non-Transformed TSS works**

Non-Transformed TSS allows you to perform similarity searches directly on raw time series data without needing to transform or preprocess the data into vector embeddings. This method involves scanning the time series with a sliding window and computing distances between the query vector and each occurrence of the sliding window.

**Why it’s useful on splayed or partitioned tables in kdb+:**

*   **Efficiency:** By avoiding the transformation step, Non-Transformed TSS can save significant computational resources and time, making it more efficient for real-time applications.
*   **Scalability:** Splayed and partitioned tables are designed to handle large datasets efficiently. Non-Transformed TSS leverages this structure to perform rapid similarity searches across vast amounts of time series data.
*   **Pattern Recognition:** This method is excellent for identifying patterns and anomalies in time series data, which is crucial in fields like finance, where detecting trends and outliers quickly can be highly valuable.
*   **Integration:** Non-Transformed TSS can be seamlessly integrated with existing kdb+ tables, allowing users to perform advanced similarity searches without migrating data or altering the existing database structure.

This integration helps kdb+ and KDB.AI users complete the following actions with the q or Python API:

*   Perform similarity searches on embeddings stored in a kdb+ splayed table.
*   Perform Non-transformed Temporal Similarity Search (TSS) on a kdb+ splayed table. 
*   Perform Non-transformed Temporal Similarity Search (TSS) on a kdb+ partitioned table.

Prerequisites
-------------

Before you start, make sure you have the following:

*   A valid q installation and an existing [kdb+ table on disk](https://code.kx.com/q/learn/brief-introduction/) with vector embeddings.
*   Access to [KDB.AI Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html), an endpoint and API Key.
*   Knowledge about [vector embeddings](https://kdb.ai/learning-hub/articles/vector-embeddings/).
*   Knowledge of [writing q code](https://code.kx.com/q4m3/) using an environment of choice (command line, IDE, notebooks).

Setup
-----

To use KDB.AI with kdb+, start the Docker container and mount the volume for your existing kdb+ database on disk:

```
docker run -it -e KDB_K4LICENSE_B64         \
               -v $PWD/path/to/kdb/:/db:cached,ro  \
               portal.dl.kx.com/kdbai-db:1.4.0
```

KDB.AI q API functions for Non-Transformed TSS
----------------------------------------------

Below is a description and breakdown of the APIs associated with running a Non-Transformed Temporal Similarity Search on an external kdb+ table.

### Create table

`createTable`

Create a KDB.AI table linked to an existing kdb+ table mounted in the KDB.AI Server container.

**Parameters**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Database name | Yes |
| table | symbol | Table name | Yes |
| externalDataReferences | table | List of external kdb+ table references | Yes |
| indexes | dict | List of indexes to associate to the external kdb+ table | Optional |

Please be aware that you cannot use the KDB+ integration to create IVF (Inverted File) and IVFPQ (Inverted File with Product Quantization) indexes. This is due to the restriction that training is not allowed on KDB+ reference tables, which prevents the use of these methods.

Example:

Python REST q

```
import kdbai_client as kdbai
session = kdbai.Session()
db = session.database('default')
table = db.create_table('myTable', external_data_references=[{'path': b'/db', 'provider': 'kx'}])
```

```
curl -X POST -H 'Content-type: application/json' -d '{"table": "myTable", "externalDataReferences": [{"path": "/db", "provider": "kx"}]}' http://localhost:8081/api/v2/databases/default/tables
```

```
q)gw:hopen 8082

q)gw(`createTable;(!) . flip((`database;`default);(`table;`myTable);(`externalDataReferences;enlist `path`provider!("/db";`kx))))
```

### List tables

`listTables`

List the tables from the `default` KDB.AI database.

**Parameters**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Name of the KDB.AI database | Yes |

Example:

Python REST q

```
db.tables
```

```
curl http://localhost:8081/api/v2/databases/default/tables
```

```
q)res:gw(`listTables;enlist[`database]!enlist`default)
q)res[`result]`tables
```

### Perform Non-Transformed TSS search

`search`

Perform a TSS search on the table.

**Parameters**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Database name | Yes |
| table | symbol | Table name | Yes |
| type | list | Search type: should be ``tss` for TSS search | Yes |
| vectors | dictionary | Dictionary with keys being the colums to search and values being list of query vectors | Yes |
| n | long | Number of matches to return | Yes |
| searchBy | list | (Non Transformed TSS only) Perform a TSS search for each group (not to be confused with `groupBy` which is used for final aggregation of the results) |  |
| options | dictionary | TSS search options like `returnMatches` and `force` | Optional |
| filter | list | List of filtering conditions | Optional |
| groupBy | list | Columns to group by as a list of symbols | Optional |
| aggs | dict | Aggregations | Optional |
| sortCols | list | Columns to sort by as a list of symbols | Optional |

Example:

Python REST q

```
table.search(type='tss', vectors={'price': [[0., 3., 2., 5., 2., 3., 0.]]}, n=10, options={'force': True})
```

```
curl -s -H "Content-Type: application/json" -H "X-Api-Key: ''" http://localhost:8081/api/v2/databases/default/tables/myTable/search -d '{"vectors":{"price": [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}, "n":10}'
```

```
// Basic TSS search on the `price` column
q)res:gw(`search;`database`table`type`vectors`n!(`default;`myTable;`tss;enlist[`price]!enlist enlist 8?1f;10))
q)first res`result

// TSS search on the `price` column with extra options to return the matched pattern and to force the execution on partitioned tables with failing partitions
q)res:gw(`search;`database`table`type`vectors`n`options!(`default;`myTable;`tss;enlist[`price]!enlist enlist 8?1f;10;`returnMatches`force!11b))
q)first res`result

// TSS search on the `price` column returning a specific subset of columns
q)res:gw(`search;`database`table`type`vectors`n`aggs!(`default;`myTable;`tss;enlist[`price]!enlist enlist 8?1f;10;`time`symbol`volume`price`nnDist`nnIdx!`time`symbol`volume`price`nnDist`nnIdx))
q)first res`result
```

### Query

`query`

Query data from the table.

**Parameters**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Database name | Yes |
| table | symbol | Table name | Yes |
| filter | list | List of filtering conditions | Optional |
| groupBy | list | Columns to group by as a list of symbols | Optional |
| aggs | dict | Aggregations | Optional |
| sortCols | list | Columns to sort by as a list of symbols | Optional |

Example:

Python REST q

```
table.query()
```

```
curl -X POST -H 'Content-type: application/json' -d '{}' http://localhost:8081/api/v2/databases/default/tables/myTable/query
```

```
q)gw(`query;`database`table!(`default;`myTable))
```

### Drop table

`deleteTable`

Delete the KDB.AI table (without touching the external kdb+ table).

**Parameters**

| **Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| database | symbol | Database name | Yes |
| table | symbol | Table name | Yes |

Example:

Python REST q

```
table.drop()
```

```
curl -X DELETE http://localhost:8081/api/v2/databases/default/tables/myTable
```

```
q)gw(`deleteTable;`database`table!`default`myTable)
```

Important: refer to this [notebook](https://code.kx.com/kdbai/latest/notebooks/Non_Transformed_TSS_qAPI_Demo.ipynb) for a working example of using an external kdb+ table with KDB.AI.

Troubleshooting
---------------

If you encounter connection issues, verify your network settings and access credentials. Consult the KDB.AI and kdb+ documentation for specific error codes. If you need help, feel free to reach out to the KDB.AI [Slack community](http://kx.com/slack) or email [support@kdb.ai](mailto:support@kdb.ai).

Next steps:
-----------

*   Read our blog post titled [Turbocharge kdb+ databases with temporal similarity search](https://kx.com/blog/turbocharge-kdb-databases-similarity-search/).
