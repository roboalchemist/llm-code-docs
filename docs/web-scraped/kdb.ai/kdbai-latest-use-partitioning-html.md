# Source: https://code.kx.com/kdbai/latest/use/partitioning.html

Title: How to partition data in KDB.AI

URL Source: https://code.kx.com/kdbai/latest/use/partitioning.html

Markdown Content:
How to partition data in KDB.AI - KDB.AI Documentation
===============
- [x] - [x] 

[Skip to content](https://code.kx.com/kdbai/latest/use/partitioning.html#how-to-partition-data-in-kdbai)

[](https://code.kx.com/kdbai/latest/index.html "KDB.AI Homepage")

 KDB.AI Documentation 

1.9.0
*   [1.9.0](https://code.kx.com/kdbai/1.9.0/)
*   [1.8.0](https://code.kx.com/kdbai/1.8.0/)
*   [1.7.0](https://code.kx.com/kdbai/1.7.0/)
*   [1.6.0](https://code.kx.com/kdbai/1.6.0/)
*   [1.5.0](https://code.kx.com/kdbai/1.5.0/)
*   [1.4.0](https://code.kx.com/kdbai/1.4.0/)
*   [1.3.0](https://code.kx.com/kdbai/1.3.0/)
*   [1.2.0](https://code.kx.com/kdbai/1.2.0/)
*   [1.1.0](https://code.kx.com/kdbai/1.1.0/)
*   [1.0.0](https://code.kx.com/kdbai/1.0.0/)

 How to partition data in KDB.AI 

Type to start searching

*   [Home](https://code.kx.com/kdbai/latest/index.html)
*   [Learn](https://code.kx.com/kdbai/latest/reference/authentication.html)
*   [How To](https://code.kx.com/kdbai/latest/use/database.html)
*   [API Reference](https://code.kx.com/kdbai/latest/reference/python-client.html)
*   [Integrations](https://code.kx.com/kdbai/latest/integrations/allintegrations.html)
*   [Examples](https://github.com/KxSystems/kdbai-samples/)
*   [Releases](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-latest.html)
*   [Help and Support](https://code.kx.com/kdbai/latest/support/known-issues.html)

[](https://code.kx.com/kdbai/latest/ "KDB.AI Documentation") KDB.AI Documentation  
*   - [x]  Home   Home  
    *   [About KDB.AI](https://code.kx.com/kdbai/latest/index.html)
    *   - [x]  Get Started   Get Started  
        *   [Prerequisites](https://code.kx.com/kdbai/latest/gettingStarted/pre-requisites.html)
        *   [KDB.AI Server Setup](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
        *   [Quick Start](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html)
        *   [Versioning and Upgrade](https://code.kx.com/kdbai/latest/versioning.html)

*   - [x]  Learn   Learn  
    *   [Authentication and Authorization (New)](https://code.kx.com/kdbai/latest/reference/authentication.html)
    *   [Database](https://code.kx.com/kdbai/latest/reference/database.html)
    *   [Table](https://code.kx.com/kdbai/latest/reference/table.html)
    *   [Data Types](https://code.kx.com/kdbai/latest/reference/supported-types.html)
    *   [Index](https://code.kx.com/kdbai/latest/reference/index.html)
    *   [Similarity Metrics](https://code.kx.com/kdbai/latest/reference/metrics.html)
    *   [Hybrid Search](https://code.kx.com/kdbai/latest/reference/hybrid.html)
    *   [Transformed TSS](https://code.kx.com/kdbai/latest/reference/transformed-tss.html)
    *   [Non-Transformed TSS](https://code.kx.com/kdbai/latest/reference/non-transformed-tss.html)
    *   [Dynamic Time Warping](https://code.kx.com/kdbai/latest/reference/dynamic-time-warping.html)
    *   [Filters](https://code.kx.com/kdbai/latest/reference/filters.html)
    *   [Partitioning](https://code.kx.com/kdbai/latest/reference/partition.html)
    *   [Reranking](https://code.kx.com/kdbai/latest/reference/reranking.html)
    *   [Parallel Processing](https://code.kx.com/kdbai/latest/reference/multithreading.html)
    *   [Learning Hub](https://kdb.ai/learning-hub)

*   - [x]  How To   How To  
    *   [Use Databases](https://code.kx.com/kdbai/latest/use/database.html)
    *   [Manage Tables](https://code.kx.com/kdbai/latest/use/manage-tables.html)
    *   [Ingest Data](https://code.kx.com/kdbai/latest/use/ingestion.html)
    *   [Query Data](https://code.kx.com/kdbai/latest/use/query.html)
    *   [Delete Data](https://code.kx.com/kdbai/latest/use/delete-data.html)
    *   [Use Indexes](https://code.kx.com/kdbai/latest/use/supported-indexes.html)
    *   - [x]  Search   Search  
        *   [Similarity Search](https://code.kx.com/kdbai/latest/use/search.html)
        *   [Hybrid Search](https://code.kx.com/kdbai/latest/use/hybrid-search.html)
        *   [Transformed TSS](https://code.kx.com/kdbai/latest/use/transformed-tss.html)
        *   [Non-Transformed TSS](https://code.kx.com/kdbai/latest/use/non-transformed-tss.html)
        *   [Dynamic Time Warping (DTW)](https://code.kx.com/kdbai/latest/use/dynamic-time-warping-dtw.html)

    *   [Customize Filters](https://code.kx.com/kdbai/latest/use/filter.html)
    *   - [x]  Partition  [Partition](https://code.kx.com/kdbai/latest/use/partitioning.html) On this page  
        *   [Setup](https://code.kx.com/kdbai/latest/use/partitioning.html#setup)
        *   [Import dependencies](https://code.kx.com/kdbai/latest/use/partitioning.html#import-dependencies)
        *   [Partition a table on any metadata column](https://code.kx.com/kdbai/latest/use/partitioning.html#partition-a-table-on-any-metadata-column)
            *   [Create table](https://code.kx.com/kdbai/latest/use/partitioning.html#create-table)
            *   [Insert data](https://code.kx.com/kdbai/latest/use/partitioning.html#insert-data)

        *   [Query partitioned data](https://code.kx.com/kdbai/latest/use/partitioning.html#query-partitioned-data)
        *   [Best practices](https://code.kx.com/kdbai/latest/use/partitioning.html#best-practices)

    *   [Rerank](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   - [x]  Set Up Authentication   Set Up Authentication  
        *   [Static Authentication](https://code.kx.com/kdbai/latest/use/set-up-static-authentication.html)
        *   [OAuth 2.0](https://code.kx.com/kdbai/latest/use/set-up-oauth2-authentication.html)

    *   [Get System Usage Info](https://code.kx.com/kdbai/latest/use/get-system-usage-info.html)

*   - [x]  API Reference   API Reference  
    *   [Python API](https://code.kx.com/kdbai/latest/reference/python-client.html)
    *   [q API](https://code.kx.com/kdbai/latest/reference/qAPI.html)
    *   [REST API](https://code.kx.com/kdbai/latest/reference/rest-api.html)
    *   [Naming and Reserved Words](https://code.kx.com/kdbai/latest/reference/naming-convention-reserved-words.html)
    *   [Glossary](https://code.kx.com/kdbai/latest/reference/glossary.html)

*   - [x]  Integrations   Integrations  
    *   [All integrations](https://code.kx.com/kdbai/latest/integrations/allintegrations.html)
    *   [kdb+](https://code.kx.com/kdbai/latest/integrations/kdb.html)
    *   [OpenAI](https://code.kx.com/kdbai/latest/integrations/openai.html)
    *   [LangChain](https://code.kx.com/kdbai/latest/integrations/langchain.html)
    *   [LlamaIndex](https://code.kx.com/kdbai/latest/integrations/llamaindex.html)
    *   [Vector IO](https://code.kx.com/kdbai/latest/integrations/vector-io.html)
    *   [Azure AI](https://code.kx.com/kdbai/latest/integrations/azureml.html)
    *   [Hugging Face](https://code.kx.com/kdbai/latest/integrations/hugging-face.html)
    *   [Unstructured](https://code.kx.com/kdbai/latest/integrations/unstructured-io.html)
    *   [Cohere](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Jina AI](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Voyage AI](https://code.kx.com/kdbai/latest/use/rerank.html)
    *   [Model Context Protocol (MCP) Server](https://code.kx.com/kdbai/latest/integrations/mcp-server.html)

*   - [x]  Examples   Examples  
    *   [GitHub Samples](https://github.com/KxSystems/kdbai-samples/)

*   - [x]  Releases   Releases  
    *   [Latest](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-latest.html)
    *   [Previous](https://code.kx.com/kdbai/latest/releaseNotes/release-notes-previous.html)

*   - [x]  Help and Support   Help and Support  
    *   [Known Issues](https://code.kx.com/kdbai/latest/support/known-issues.html)
    *   [FAQs and Troubleshooting](https://code.kx.com/kdbai/latest/support/FAQ-troubleshooting.html)
    *   [Slack Community](http://kx.com/slack)

 On this page  
*   [Setup](https://code.kx.com/kdbai/latest/use/partitioning.html#setup)
*   [Import dependencies](https://code.kx.com/kdbai/latest/use/partitioning.html#import-dependencies)
*   [Partition a table on any metadata column](https://code.kx.com/kdbai/latest/use/partitioning.html#partition-a-table-on-any-metadata-column)
    *   [Create table](https://code.kx.com/kdbai/latest/use/partitioning.html#create-table)
    *   [Insert data](https://code.kx.com/kdbai/latest/use/partitioning.html#insert-data)

*   [Query partitioned data](https://code.kx.com/kdbai/latest/use/partitioning.html#query-partitioned-data)
*   [Best practices](https://code.kx.com/kdbai/latest/use/partitioning.html#best-practices)

How to Partition Data in KDB.AI
===============================

_This page provides details on partitioning data within the KDB.AI._

If you're new to this topic, start with [Learn: KDB.AI partitioning](https://code.kx.com/kdbai/latest/reference/partition.html).

KDB.AI support partitioning for tables with any of the following indexes:

*   dense Flat index
*   dense qFlat index
*   dense HNSW index
*   dense qHNSW index
*   sparse index
*   TSS index
*   any combination of the above indexes

Setup
-----

Before starting, you must have:

*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download/) license
*   Installed the latest version of KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
*   [Python Client](https://code.kx.com/kdbai/latest/reference/python-client.html)

Import dependencies
-------------------

Import the following dependencies:

```python
import sys
import kdbai_client as kdbai
from pprint import pprint # for pretty printing
import pandas as pd
import numpy as np
```

Partition a table on any metadata column
----------------------------------------

### Create table

Create a table by specifying multiple metadata columns to partition:

Python q REST 

```python
schema = [
    {'name': 'id', 'type': 'int16'},
    {'name': 'sym', 'type': 'str'},
    {'name': 'date', 'type': 'datetime64[D]'},
    {'name': 'embeddings', 'type': 'float32s'},
    {'name': 'sparse', 'type': 'general'}
]
indexes = [
    {'name': 'flat_index', 'column': 'embeddings', 'type': 'flat', 'params': {'dims': 25}},
    {'name': 'hnsw_fast', 'column': 'embeddings', 'type': 'hnsw', 'params': {'dims': 25, 'M': 8, 'efConstruction': 8}},
    {'name': 'sparse_index', 'column': 'sparse', 'type': 'bm25', 'params': {'k': 1.25, 'b': 0.75}}
]

# Local server
session = kdbai.Session(endpoint='http://localhost:8082')

# Get the database connection. Default database name is 'default'
database = session.database('default')

table = database.create_table('example', schema=schema, indexes=indexes, partition_column='date')
```

```q
schema: flip `name`type!(`id`sym`date`embeddings`sparse;`h`s`d`E`)
flatIndex: `name`column`type`params!(`flat_index;`embeddings;`flat;enlist[`dims]!enlist 25)
hnswFast: `name`column`type`params!(`hnsw_fast;`embeddings;`hnsw;`dims`M`efConstruction!(25;8;8))
sparseIndex: `name`column`type`params!(`sparse_index;`sparse;`bm25;`k`b!(1.25;0.75))
indexes: (flatIndex;hnswFast;sparseIndex)
gw: hopen 8082;
gw(`createTable;`database`table`schema`indexes`partitionColumn!(`default;`documents;schema;indexes;`date))
```

```json
{
    "table": "example",
    "schema": [
        {"name": "id", "type": "short"},
        {"name": "sym", "type": "symbol"},
        {"name": "date", "type": "date"},
        {"name": "embeddings", "type": "reals"},
        {"name": "sparse", "type": "reals"},
    ],
    "indexes": [
        {"name": "flat_index", "column": "embeddings", "type": "flat", "params": {"dims": 25}},
        {"name": "hnsw_fast", "column": "embeddings", "type": "hnsw", "params": {"dims": 25, "M": 8, "efConstruction": 8}},
        {"name": "sparse_index", "column": "sparse", "type": "bm25", "params": {"k": 1.25, "b": 0.75}}
    ],
    "partitionColumn": "date"
}
```

```sh
curl -X POST -H "Content-Type: application/json" -d @schemaAbove.json localhost:8081/api/v2/databases/default/tables
```

The system creates a number of partitions, within the specified columns, by default, and should not be defined by the user.

Result: The table is created such that it is partitioned on composite values in the specified metadata columns.

Example of Python code for partition by 
```python
symbol
```
 column:

```python
table_partitioned_by_sym = database.create_table('example', schema=schema, indexes=indexes, partition_column='sym')
```

### Insert data

Add partitions by inserting data.

Python q REST 

```python
row_count = 1000
df = pd.DataFrame({
    'id': list(range(row_count)),
    'sym': np.random.choice(['AAA', 'BBB', 'CCC', 'DDD'], 1000),
    'date': np.random.choice(pd.date_range(start='2021-01-01', periods=row_count/4, freq='1D'), row_count),
    'embeddings': list(np.random.rand(row_count, 25).astype(np.float32)),
    'sparse': [{np.random.randint(1, 1000): np.random.rand() for _ in range(np.random.randint(10))} for _ in range(row_count)]
    })
table.insert(df)
```

```q
id: 21212 21212
sym: aaa bbb
date: 2023.10.11T00:00:00.000000000 2023.10.11T00:00:00.000000000
embeddings: (25?1e; 25?1e)
sparse: ((1996 101 11190 5598 2058 5231 102!2 1 1 1 1 1 1);(1996 11190 2058 4231 102! 1 1 1 1 1))

data: `id`sym`date`embeddings`sparse!(id sym date embeddings sparse)
gw: hopen 8082;
gw(`insertData;`database`table`payload!(`default;`example;data))
```

```json
{
  "rows": [
    {
      "id": 21212,
      "sym": "aaa",
      "date": "2023-10-11T00:00:00.000000000",
      "embeddings": [0.439081, 0.5759051, 0.5919004, 0.8481566, 0.389056, 0.391543, 0.08123546, 0.9367504, 0.2782122, 0.2392341, 0.1508133, 0.1567317, 0.9785, 0.7043314, 0.9441671, 0.7833686, 0.4099561, 0.6108817, 0.4976492, 0.4087545, 0.449731, 0.01392076, 0.714878, 0.1946509, 0.09059025],
      "sparse": {"1996": 2, "101": 1, "11190": 1, "5598": 1, "2058": 1, "4231": 1, "102": 1}
    },
    {
      "id": 19376,
      "sym": "bbb",
      "date": "2023-10-11T00:00:00.000000000",
      "embeddings": [0.6203014, 0.9326316, 0.2747066, 0.05752515, 0.2560658, 0.2310108, 0.08724017, 0.1024432, 0.8671097, 0.7278528, 0.1627662, 0.6884756, 0.8177547, 0.7520102, 0.1086824, 0.9598964, 0.03668341, 0.6430982, 0.6708738, 0.6789082, 0.412317, 0.9877844, 0.3867353, 0.726781, 0.4046546],
      "sparse": {"1996": 1, "5598": 1, "2058": 1, "4231": 1, "102": 1}
    }
  ]
}
```

```sh
curl -H 'Content-Type: application/json' -d @insert.json localhost:8081/api/v2/databases/default/tables/example/insert
```

Query partitioned data
----------------------

You can perform searches and queries using filters on the partition column. This capability ensures that queries are executed efficiently by limiting the scope of data scanned to the relevant partitions. For instance, use this query to count the rows on each partition:

Python q REST 

```python
table.query(aggs={'cnt': ['count', 'id']}, group_by=['date'])
```

```q
gw(`query;`database`table`aggs`groupBy!(`default;`example;enlist[`cnt]!enlist[`count`id];enlist[`date]))
```

```q
curl -s -H "Content-Type: application/json" localhost:8081/api/v2/databases/default/tables/example/query \
-d '{"aggs":{"cnt":["count","id"]}, "groupBy":["date"]}'
```

Best practices
--------------

*   **Consistent Partitioning Strategy:** Maintain a consistent approach to partitioning to simplify data management and ensure optimal performance.

*   **Monitor Performance:** Consistently track query performance and modify partitioning strategies as necessary.

*   **Data Archiving:** Implement archiving strategies for older partitions to manage storage effectively and keep the system performant.

[Previous Customize Filters](https://code.kx.com/kdbai/latest/use/filter.html)[Next Rerank](https://code.kx.com/kdbai/latest/use/rerank.html)

 © 2026 KX Systems, Inc. KX, KDB-X, and kdb+ are registered trademarks of KX Systems, Inc., a subsidiary of KX Software Limited. 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

![Image 1](https://id.rlcdn.com/464526.gif)

By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts.[Cookies Policy.](https://kx.com/cookie-policy/)

Cookies Settings Reject All Accept All

![Image 2: KX Logo](https://cdn-ukwest.onetrust.com/logos/2e246b76-a09f-455a-b12d-cb0cc60b7d47/36d73287-3cef-4657-ad68-1de87d20bcfb/e5b10d3a-3252-4f3a-8f47-e55d701ecfdf/KX-Logo-Black-500x500.png)

Privacy Preference Center
-------------------------

*   ### Your Privacy 
*   ### Strictly Necessary Cookies 
*   ### Performance Cookies 
*   ### Functional Cookies 
*   ### Targeting Cookies 

#### Your Privacy

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. 

[More information](https://cookiepedia.co.uk/giving-consent-to-cookies)

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

- [x] Performance Cookies 

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

#### Functional Cookies

- [x] Functional Cookies 

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Targeting Cookies

- [x] Targeting Cookies 

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Clear

- [x] checkbox label label

Apply Cancel

Confirm My Choices

Allow All

[![Image 3: Powered by Onetrust](https://cdn-ukwest.onetrust.com/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
