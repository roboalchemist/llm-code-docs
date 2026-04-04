# Source: https://code.kx.com/kdbai/latest/use/search.html

Title: KDB.AI Similarity Search - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/search.html

Markdown Content:
How to Conduct a Similarity Search in KDB.AI
--------------------------------------------

_This page provides details of how to execute similarity searches. For more advanced search filters, see [Customize Filters](https://code.kx.com/kdbai/latest/use/filter.html)._

Similarity searches in KDB.AI are based on Approximate Nearest Neighbor (ANN) algorithms.

Setup
-----

Before you start, make sure you have:

*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download/) license
*   Installed the latest version of KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)
*   [Python Client](https://code.kx.com/kdbai/latest/reference/python-client.html)

Select the table to search
--------------------------

To perform a search, specify the name of the table in which the relevant vector embeddings are stored. Using Python Client, you can create a `table` object from the session:

Python

```
documents = session.table("documents")
```

Now that you have a vector embedding, you can perform a search for the nearest neighbors. Python Client uses the `table` object, whereas REST Client uses the table name as above. In this example, the embeddings are assumed to be eight dimensional and the number of nearest neighbors is set to `3`.

Use the following command to search for the nearest neighbors:

Python REST q

```
index_name = 'vector_index'
documents.search(vectors={index_name: [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}, n=3)
```

```
curl -s -H "Content-Type: application/json" localhost:8082/api/v2/databases/default/tables/documents/search \
-d '{"n": 3, "vectors" {"vector_index":[[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}}'
```

```
// gw is a handler to the gateway
vectors: enlist[`vector_index]!enlist enlist 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0;
gw(`search;`database`table`n`vectors!(`default;`documents;3;vectors))
```

Batch searches
--------------

For larger workloads you can send multiple query vectors at once as seen in the following command.

Python REST q

```
index_name = 'vector_index'
documents.search(vectors={index_name: [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0],[1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0]]}, n=3)
```

```
curl -s -H "Content-Type: application/json" localhost:8082/api/v2/databases/default/tables/documents/search \ 
-d '{"n":3,
"vectors": {"vector_index": [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0],[1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0]]}}'
```

```
// gw is a handler to the gateway
vectors: enlist[`vector_index]!enlist (1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0; 1.0 7.0 1.0 1.0 7.0 1.0 1.0 7.0 1.0 1.0 7.0 1.0);
gw(`search;`database`table`n`vectors!(`default;`documents;3;vectors))
```

Customize searches using Range
------------------------------

Use the keyword `range` to find all vectors within a distance you define. This applies to the qFlat index only.

Python REST q

```
index_name = 'qFlat_index'
documents.search(vectors={qFlat_index: [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0],[1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0]]}, range=5.5)
```

```
curl -s -H "Content-Type: application/json" localhost:8082/api/v2/databases/default/tables/documents/search \ 
-d '{"vectors": {"vector_index": [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0],[1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0,1.0,7.0,1.0]]}, "range":5.5}'
```

```
// gw is a handler to the gateway
vectors: enlist[`vector_index]!enlist (1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0; 1.0 7.0 1.0 1.0 7.0 1.0 1.0 7.0 1.0 1.0 7.0 1.0);
gw(`search;`database`table`vectors`range!(`default;`documents;vectors;5.5e))
```

Note

Each `range` search query can return a maximum of 10 million results. If your query reaches this limit, reduce the range or refine your filters to narrow the results.

Processing results
------------------

You can return a subset of the columns in the table, reducing the amount to data sent back to the client:

Python REST q

```
index_name = "vector_index"
documents.search(vectors={index_name: [[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}, n=3, aggs=[["author", "content"]])
```

```
curl -s -H "Content-Type: application/json" localhost:8082/api/v2/databases/default/tables/documents/search \ 
-d '{"n":3,
"vectors":{"vector_index":[[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}, aggs:[["author","content"]]}'
```

```
// gw is a handler to the gateway
vectors: enlist[`vector_index]!enlist enlist 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0;
gw(`search;`database`table`vectors`n`aggs!(`default;`documents;vectors;3;{x!x}(`author;`content)))
```

In addition to returning a subset of the columns, you can return aggregated results, grouped by categorical variables, and sorted by column name:

Python REST q

```
index_name = "vector_index"
documents.search(vectors={index_name:[[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}, n=3, aggs={"sumLength":["sum","length"]}, group_by=["author"], sort_columns=["sumLength"])
```

```
curl -s -H "Content-Type: application/json" localhost:8082/api/v2/databases/default/tables/documents/search \ 
-d '{"n":3,
"vectors":{"vector_index":[[1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,1.0]]}, aggs:{"sumLength":["sum","length"]},
groupBy:["author"],sort_columns:["sumLength"]}'
```

```
// gw is a handler to the gateway
vectors: enlist[`vector_index]!enlist enlist 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0 1.0 0.0 1.0;
gw(`search;`database`table`vectors`n`aggs`groupBy`sortColumns!(`default;`documents;vectors;3;enlist[`sumLength]!enlist (`sum;`length);`author;`sumLength))
```

You can find all supported aggregations listed [here](https://code.kx.com/kdbai/latest/use/query.html#supported-aggregations).

Next steps
----------

Now that you're familiar with how to perform a similarity search, move on to the following:

*   Try similarity searches in our [Document Search](https://kdb.ai/learning-hub/samples/document-search/), [Sentiment Analysis](https://kdb.ai/learning-hub/samples/sentiment-analysis/), and [Recommendation Systems](https://kdb.ai/learning-hub/samples/recommendation-systems/) sample projects.
*   Review our articles on [Methods of Similarity](https://kdb.ai/learning-hub/articles/methods-of-similarity/), and [Mechanics of Search](https://kdb.ai/learning-hub/articles/mechanics-of-search/), [Document Search](https://kdb.ai/learning-hub/samples/document-search/), [Sentiment Analysis](https://kdb.ai/learning-hub/samples/sentiment-analysis/), and [Recommendation Systems](https://kdb.ai/learning-hub/samples/recommendation-systems/) for more context.
*   Watch our videos to learn more about [Methods of Similarity](https://kdb.ai/learning-hub/video-lessons/similarity-metrics-for-vector-databases/) and [Vector Search](https://kdb.ai/learning-hub/video-lessons/introduction-to-vector-search/).
*   Move on to perform a [Hybrid Search](https://code.kx.com/kdbai/latest/use/hybrid-search.html)
