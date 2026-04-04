# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/vector-embeddings.md

# Vector Embeddings

An *embedding* refers to the reduction of high-dimensional data, such as unstructured text, to a representation
with fewer dimensions, such as a vector. Modern deep learning techniques can create vector embeddings,
which are structured numerical representations, from unstructured data such as
text and images, while preserving semantic notions of similarity and dissimilarity in the geometry of the vectors they produce.

The following illustration is a simplified example of the vector embedding and geometric similarity of natural language
text. In practice, neural networks produce embedding vectors with hundreds or even thousands of dimensions, not two as
shown here, but the concept is the same. Semantically similar text yields vectors that “point” in the same general
direction.

Many applications can benefit from the ability to find text or images similar to a target. For example, when a new
support case is logged at a help desk, the support team can benefit from the ability to find similar cases that have
already been resolved. The advantage of using embedding vectors in this application is that it goes beyond keyword
matching to semantic similarity, so related records can be found even if they don’t contain exactly the same words.

Snowflake Cortex offers the [EMBED_TEXT_768](../../sql-reference/functions/embed_text-snowflake-cortex.md) and
[EMBED_TEXT_1024](../../sql-reference/functions/embed_text_1024-snowflake-cortex.md) functions and several
[Vector functions](../../sql-reference/functions-vector.md) to compare them for various applications.

## Text embedding models

Snowflake offers the following text embedding models. See below for more details.

| Model name | Output dimensions | Context window | Language support |
| --- | --- | --- | --- |
| snowflake-arctic-embed-m-v1.5 | 768 | 512 | English-only |
| snowflake-arctic-embed-m | 768 | 512 | English-only |
| e5-base-v2 | 768 | 512 | English-only |
| snowflake-arctic-embed-l-v2.0 | 1024 | 512 | Multilingual |
| voyage-multilingual-2 | 1024 | 32000 | Multilingual ([supported languages](https://blog.voyageai.com/2024/06/10/voyage-multilingual-2-multilingual-embedding-model/)) |
| nv-embed-qa-4 | 1024 | 512 | English-only |

Supported models might have different [costs](aisql.md).

## About vector similarity functions

The measurement of similarity between vectors is a fundamental operation in semantic comparison. Snowflake Cortex
provides four vector similarity functions: VECTOR_INNER_PRODUCT, VECTOR_L1_distance, VECTOR_L2_DISTANCE, and
VECTOR_COSINE_SIMILARITY. To learn more about these functions, see [Vector functions](../../sql-reference/functions-vector.md).

For syntax and usage details, see the reference page for each function:

* [VECTOR_INNER_PRODUCT](../../sql-reference/functions/vector_inner_product.md)
* [VECTOR_L1_DISTANCE](../../sql-reference/functions/vector_l1_distance.md)
* [VECTOR_L2_DISTANCE](../../sql-reference/functions/vector_l2_distance.md)
* [VECTOR_COSINE_SIMILARITY](../../sql-reference/functions/vector_cosine_similarity.md)

## Examples

The following examples use the vector similarity functions.

This SQL example uses the VECTOR_INNER_PRODUCT function to determine which vectors in the table
are closest to each other between columns `a` and `b`:

```sqlexample
CREATE TABLE vectors (a VECTOR(float, 3), b VECTOR(float, 3));
INSERT INTO vectors SELECT [1.1,2.2,3]::VECTOR(FLOAT,3), [1,1,1]::VECTOR(FLOAT,3);
INSERT INTO vectors SELECT [1,2.2,3]::VECTOR(FLOAT,3), [4,6,8]::VECTOR(FLOAT,3);

-- Compute the pairwise inner product between columns a and b
SELECT VECTOR_INNER_PRODUCT(a, b) FROM vectors;
```

```output
+------+
| 6.3  |
|------|
| 41.2 |
+------+
```

This SQL example calls the VECTOR_COSINE_SIMILARITY function to find the vector closes to `[1,2,3]`:

```sqlexample
SELECT a, VECTOR_COSINE_SIMILARITY(a, [1,2,3]::VECTOR(FLOAT, 3)) AS similarity
    FROM vectors
ORDER BY similarity DESC
LIMIT 1;
```

```output
+-------------------------+
| [1, 2.2, 3] | 0.9990... |
+-------------------------+
```

### Snowflake Python Connector

These examples show how to use the VECTOR data type and vector similarity functions with the Python Connector.

> **Note:**
>
> Support for the VECTOR type was introduced in version 3.6 of the Snowflake Python Connector.

```python
import snowflake.connector

conn = ... # Set up connection
cur = conn.cursor()

# Create a table and insert some vectors
cur.execute("CREATE OR REPLACE TABLE vectors (a VECTOR(FLOAT, 3), b VECTOR(FLOAT, 3))")
values = [([1.1, 2.2, 3], [1, 1, 1]), ([1, 2.2, 3], [4, 6, 8])]
for row in values:
        cur.execute(f"""
            INSERT INTO vectors(a, b)
                SELECT {row[0]}::VECTOR(FLOAT,3), {row[1]}::VECTOR(FLOAT,3)
        """)

# Compute the pairwise inner product between columns a and b
cur.execute("SELECT VECTOR_INNER_PRODUCT(a, b) FROM vectors")
print(cur.fetchall())
```

```output
[(6.30...,), (41.2...,)]
```

```python
# Find the closest vector to [1,2,3]
cur.execute(f"""
    SELECT a, VECTOR_COSINE_SIMILARITY(a, {[1,2,3]}::VECTOR(FLOAT, 3))
        AS similarity
        FROM vectors
        ORDER BY similarity DESC
        LIMIT 1;
""")
print(cur.fetchall())
```

```output
[([1.0, 2.2..., 3.0], 0.9990...)]
```

### Snowpark Python

These examples show how to use the VECTOR data type and vector similarity functions with the Snowpark Python Library.

> **Note:**
>
> * Support for the VECTOR type was introduced in version 1.11 of Snowpark Python.
> * The Snowpark Python library does not support the [VECTOR_COSINE_SIMILARITY](../../sql-reference/functions/vector_cosine_similarity.md) function.

```python
from snowflake.snowpark import Session, Row
session = ... # Set up session
from snowflake.snowpark.types import VectorType, StructType, StructField
from snowflake.snowpark.functions import col, lit, vector_l2_distance
schema = StructType([StructField("vec", VectorType(int, 3))])
data = [Row([1, 2, 3]), Row([4, 5, 6]), Row([7, 8, 9])]
df = session.create_dataframe(data, schema)
df.select(
    "vec",
    vector_l2_distance(df.vec, lit([1, 2, 2]).cast(VectorType(int, 3))).as_("dist"),
).sort("dist").limit(1).show()
```

```output
----------------------
|"VEC"      |"DIST"  |
----------------------
|[1, 2, 3]  |1.0     |
----------------------
```

## Create vector embeddings from text

To create a vector embedding from a piece of text, you can use the [EMBED_TEXT_768 (SNOWFLAKE.CORTEX)](../../sql-reference/functions/embed_text-snowflake-cortex.md) or
[EMBED_TEXT_1024 (SNOWFLAKE.CORTEX)](../../sql-reference/functions/embed_text_1024-snowflake-cortex.md) functions, depending on the output dimensions of the model.
This function returns the vector embedding for a given English-language text. This vector can be used with the
vector comparison functions to determine the semantic similarity of two documents.

```sqlexample
SELECT SNOWFLAKE.CORTEX.EMBED_TEXT_768(model, text)
```

> **Tip:**
>
> You can use other embedding models through [Snowpark Container Services](../../developer-guide/snowpark-container-services/overview.md). For more information, see
> [Embed Text Container Service](https://github.com/Snowflake-Labs/sfguide-text-embedding-snowpark-container-service).

> **Important:**
>
> EMBED_TEXT_768 and EMBED_TEXT_1024 are Cortex LLM Functions, so their usage is governed by the same access controls as the other
> Cortex LLM Functions. For instructions on accessing these functions, see the [Cortex LLM Functions Required Privileges](aisql.md).

## Example use cases

This section shows how to use embeddings, the vector similarity functions, and VECTOR data type to implement popular use cases
such as vector similarity search and retrieval-augmented generation (RAG).

### Vector similarity search

To implement a search for semantically similar documents, first store the embeddings for the documents to be searched.
Keep the embeddings up to date when documents are added or edited.

In this example, the documents are call center issues logged by support representatives. The issue is stored in a column
called `issue_text` in the table `issues`. The following SQL creates a new vector column to hold the
embeddings of the issues.

```sqlexample
ALTER TABLE issues ADD COLUMN issue_vec VECTOR(FLOAT, 768);

UPDATE issues
  SET issue_vec = SNOWFLAKE.CORTEX.EMBED_TEXT_768('snowflake-arctic-embed-m', issue_text);
```

To perform a search, create an embedding of the search term or target document, and then use a vector similarity function
to locate documents with similar embeddings. Use ORDER BY and LIMIT clauses to select the top *k* matching documents,
and optionally use a WHERE condition to specify a minimum similarity.

Generally, the call to the vector similarity function should appear in the SELECT clause, not in the WHERE clause. This
way, the function is called only for the rows specified by the WHERE clause, which may restrict the query based on some
other criteria, instead of operating over all rows in the table. To test a similarity value in the WHERE clause, define
a column alias for the VECTOR_COSINE_SIMILARITY call in the SELECT clause, and use that alias in a condition in the WHERE
clause.

This example finds up to five issues matching the search term from the last 90 days, assuming the cosine similarity with
the search term is at least 0.7.

```sqlexample
SELECT
  issue,
  VECTOR_COSINE_SIMILARITY(
    issue_vec,
    SNOWFLAKE.CORTEX.EMBED_TEXT_768('snowflake-arctic-embed-m', 'User could not install Facebook app on his phone')
  ) AS similarity
FROM issues
ORDER BY similarity DESC
LIMIT 5
WHERE DATEDIFF(day, CURRENT_DATE(), issue_date) < 90 AND similarity > 0.7;
```

### Retrieval-Augmented Generation (RAG)

In retrieval-augmented generation (RAG), a user’s query is used to find similar documents using
vector similarity. The top document is then passed to a large language model
(LLM) along with the user’s query, providing context for the generative response (completion). This can
improve the appropriateness of the response significantly.

In the following example, `wiki` is a table with a text column `content`, and `query` is a single-row
table with a text column `text`.

```sqlexample
-- Create embedding vectors for wiki articles (only do once)
ALTER TABLE wiki ADD COLUMN vec VECTOR(FLOAT, 768);
UPDATE wiki SET vec = SNOWFLAKE.CORTEX.EMBED_TEXT_768('snowflake-arctic-embed-m', content);

-- Embed incoming query
SET query = 'in which year was Snowflake Computing founded?';
CREATE OR REPLACE TABLE query_table (query_vec VECTOR(FLOAT, 768));
INSERT INTO query_table SELECT SNOWFLAKE.CORTEX.EMBED_TEXT_768('snowflake-arctic-embed-m', $query);

-- Do a semantic search to find the relevant wiki for the query
WITH result AS (
    SELECT
        w.content,
        $query AS query_text,
        VECTOR_COSINE_SIMILARITY(w.vec, q.query_vec) AS similarity
    FROM wiki w, query_table q
    ORDER BY similarity DESC
    LIMIT 1
)

-- Pass to large language model as context
SELECT SNOWFLAKE.CORTEX.COMPLETE('mistral-7b',
    CONCAT('Answer this question: ', query_text, ' using this text: ', content)) FROM result;
```

## Cost considerations

Snowflake Cortex LLM Functions, including EMBED_TEXT_768 and EMBED_TEXT_1024, incur compute cost based on the number of tokens processed.

> **Note:**
>
> A token is the smallest unit of text processed by Snowflake Cortex LLM Functions, approximately equal to four
> characters of text. The equivalence of raw input or output text to tokens can vary by model.

* For the EMBED_TEXT_768 and EMBED_TEXT_1024 functions, only input tokens are counted towards the billable total.
* Vector similarity functions do not incur token-based costs.

For more information about billing of Cortex LLM Functions, see [Cortex LLM Functions Cost Considerations](aisql.md).
For general information about compute costs, see [Understanding compute cost](../cost-understanding-compute.md).
