# Source: https://docs.shaped.ai/docs/v2/query_reference/shapedql

Title: Shaped Query Language | Shaped Docs

URL Source: https://docs.shaped.ai/docs/v2/query_reference/shapedql

Markdown Content:
Skip to main content
Docs
ShapedQL
API
Playground
Sign up
Search docs
Shaped Query Language
Shaped Query Language

The Shaped Query Language (ShapedQL) is a SQL-like domain-specific language for building recommendation and ranking queries. It provides a familiar SQL syntax while supporting retrieval, filtering, scoring, and reordering. This reference uses the canonical syntax throughout: FROM retrieve(...) to union retrievers, and SELECT score(...) AS alias / reranker columns with ORDER BY alias.

Quick Start​

Simple recommendation query:

ShapedQL
Python SDK
TypeScript SDK
REST
SELECT * 
FROM retrieve(similarity(embedding_ref='als', limit=50, 
                        encoder='precomputed_user', input_user_id='$user_id'))
LIMIT 10


Response:

{
  "results": [
    {
      "id": "item123",
      "score": 0.95,
      "attributes": {
        "name": "Product Name",
        "price": 99.99
      }
    }
  ]
}

Overview​

The query language transpiles SQL-like queries into query configuration objects that define the complete query pipeline. Queries can be written in two formats:

SQL Syntax: A SQL-like string that gets transpiled to a query config
YAML/JSON Query Objects: Direct configuration objects with explicit structure

This document focuses on the SQL syntax, which provides a familiar interface for building recommendation and ranking queries.

Mental model​

ShapedQL queries map to a multi-stage ranking pipeline:

Retrieve: Select candidates (e.g., text_search(...), similarity(...), ids(...)).
Filter: Apply rules to exclude candidates.
Score: Compute a relevance score with SELECT score(expression='...') AS alias and ORDER BY alias.
Reorder: Post-process ordering (e.g., diversity, exploration).

Standard information retrieval reranking fits naturally into the score stage: text rerankers like colbert_v2(...) and cross_encoder(...), rank fusion like RRF, and linear interpolation are all expressed as scoring expressions and work the same way for both search and recommendations.

Query endpoints​

You can run ShapedQL against two different endpoints. Both accept a query string (ShapedQL) and optional parameters in the request body.

Global query: POST /v2/query​

A single endpoint that routes your query by the FROM clause:

Data (analytics) – Runs on ClickHouse. Use a data.* table reference:
FROM data.table_name – Your tables (batch or real-time connectors)
FROM data.view_name – Your views (SQL or LLM transforms)
FROM data.engine_name.items – Item catalog for engine engine_name
FROM data.engine_name.interactions / data.engine_name.users – Engine interaction or user data
Engine (recommendations/ranking) – Proxied to the named engine. Use an engine.* table reference with the engine name as the middle part:
FROM engine.engine_name.retrieve(similarity(...), text_search(...)) – Same ShapedQL as per-engine, but with the engine.engine_name. prefix.

Rules for the global endpoint:

Use one namespace per query: either only data.* or only engine.*. You cannot mix data.table and engine.my_engine.retrieve(...) in the same query.
Data queries must include a LIMIT (max 10,000 rows).
Engine queries are rewritten to local scope (the engine.engine_name. prefix is stripped) and sent to that engine’s query endpoint.

Example (data):

SELECT * FROM data.my_events_table
WHERE created_at > '2024-01-01'
LIMIT 100


Example (engine):

SELECT score(expression='m1', input_user_id='$user_id') AS s, *
FROM engine.my_recommender.retrieve(similarity(embedding_ref='als', limit=50,
                                               encoder='precomputed_user',
                                               input_user_id='$user_id'))
ORDER BY s LIMIT 20

Per-engine query: POST /v2/engines/{engine_name}/query​

Runs ShapedQL in the context of a single engine. You pass engine_name in the path; the query body uses the same ShapedQL as elsewhere, but without any data.* or engine.* prefix.

FROM is local to that engine: FROM retrieve(...), FROM retrieve(similarity(...)), etc.
No routing: the server already knows which engine to use.
Use this when your app already has the engine name and only does retrieval/ranking (no analytics or cross-engine needs).

Example:

SELECT score(expression='m1', input_user_id='$user_id') AS s, *
FROM retrieve(similarity(embedding_ref='als', limit=50,
                         encoder='precomputed_user', input_user_id='$user_id'))
ORDER BY s LIMIT 20


Request: POST /v2/engines/my_recommender/query with the above as query and optional parameters (e.g. user_id).

Global vs per-engine: when to use which​
Use case	Endpoint	Why
One API for both analytics and recommendations	Global POST /v2/query	Same base URL; route by FROM data.* vs FROM engine.*.
Query tables/views or engine-backed tables (data.engine_name.items)	Global POST /v2/query	Only the global endpoint supports data.*.
Your client already has the engine name and only runs ranking queries	Per-engine POST /v2/engines/{name}/query	Simpler query (no prefix); no routing step.
Building a single “query gateway” that accepts arbitrary ShapedQL	Global POST /v2/query	Callers can target data or any engine via the query text.

Both endpoints return the same shape of response (e.g. results with id, score, attributes). The global endpoint requires a read-write API key; per-engine uses the same auth as the rest of the API.

SQL vs YAML Format​

Use SQL When:

You're familiar with SQL and want a quick way to write queries
You need ad-hoc queries for experimentation
You want a concise, readable syntax
You're building simple to moderately complex queries

Use YAML/JSON When:

You need fine-grained control over every query component
You're defining complex queries with many nested options
You want explicit type safety and validation
You're programmatically generating queries

SQL Example:

ShapedQL
Python SDK
TypeScript SDK
YAML
SELECT * FROM retrieve(similarity(embedding_ref='als', limit=50)) LIMIT 10


Both formats transpile to the same internal query configuration.

Basic Syntax​

Use retrieve(...) in FROM to union retrievers, put score(...) AS alias and rerankers (e.g. diversity(...) AS alias) in SELECT, and reference those aliases in ORDER BY:

SELECT [score(expression='...') AS score_alias]
       [reranker(...) AS rerank_alias]  -- e.g. diversity(score=score_alias, ...)
       [columns | *]
FROM retrieve(retriever_function(...), retriever_function(...), ...)
[WHERE filter_expression]
[ORDER BY alias [DESC]]   -- alias from SELECT (score or reranker)
[LIMIT n]

ShapedQL
Python SDK
TypeScript SDK
SELECT score(expression='m1') AS s, diversity(score=s, strength=0.3) AS r, *
FROM retrieve(similarity(embedding_ref='als', limit=50),
              text_search(query='$query', limit=30))
WHERE category = 'electronics' ORDER BY r LIMIT 20


Query Execution Pipeline:

Retrieval: The retrieve(...) function runs each retriever in parallel
Union: Results are combined (union) and deduplicated
Filtering: The WHERE clause is applied
Scoring: Score and reranker expressions in SELECT are evaluated
Ordering: ORDER BY sorts by the chosen alias (score or reranker)
Limiting: The final result is limited to LIMIT rows

Clause order: SELECT → FROM retrieve(...) → WHERE → ORDER BY → LIMIT. Only one score() is allowed per query; you can have multiple reranker columns and order by any alias.

Notes:

Use retrieve(retriever1, retriever2, ...) to union multiple retrievers
If no FROM clause is specified, a default filter retriever is used
Function names are case-insensitive
SQL comments (-- comment) are supported
String literals support escaped quotes: 'O''Reilly' or "He said ""Hello"""
Entity Types​

Queries operate on one of several entity types:

item: Items to be recommended (products, content, etc.)
user: Users to be recommended (for user-to-user recommendations)
user_attribute: Attributes associated with a user.
item_attribute: Attributes associated with an item.

The entity_type parameter determines which entity type a query operates on. All retrievers in a single query must use the same entity type. If not specified, the default is item.

Retriever Functions​

Retriever functions define how candidates are initially retrieved. All retriever functions support the entity_type parameter and the optional where parameter for filter expressions. The where parameter uses DataFusion SQL syntax (see WHERE Clause for complete syntax documentation).

Multiple Retrievers:

The canonical form uses the retrieve(...) function to union one or more retrievers. All retrievers execute in parallel and their results are merged (union) and deduplicated. All retrievers must use the same entity_type.

SELECT * 
FROM retrieve(
    similarity(embedding_ref='als', limit=50),
    text_search(query='$query', mode='lexical', limit=50)
)
LIMIT 20


No FROM Clause:

If no FROM clause is specified, a default filter retriever is used with limit=100.

similarity()​

Performs vector similarity search using embeddings.

ShapedQL
Python SDK
TypeScript SDK
YAML
similarity(
    embedding_ref='name',
    limit=100,
    encoder='precomputed_user',
    input_user_id='$user_id',
    where='optional_filter_expression',
    name='optional_step_name'
)

-- Basic example
SELECT * FROM retrieve(similarity(embedding_ref='als', limit=50)) LIMIT 10

-- With filter expression
SELECT * FROM retrieve(similarity(
    embedding_ref='als', 
    limit=50, 
    where='category = "electronics" AND price < 100'
)) LIMIT 10


Parameters:

embedding_ref (required, string):

The name of the embedding model to use for similarity search.
Example: 'als', 'dssm', 'collaborative-filtering'
Must match a pre-configured embedding in your Shaped environment

limit (optional, int, default: 100):

Maximum number of candidate items to retrieve before any filtering or reordering
For best performance, keep this under 1000
Example: limit=50

entity_type (optional, string, default: 'items'):

Type of entities to retrieve
Allowed values: 'items' or 'users'
Example: entity_type='users'

encoder (optional, string, SQL syntax only):

Configuration for the query encoder (SQL syntax uses encoder, but transpiles to query_encoder)
In SQL: Use string like encoder='precomputed_user' with additional encoder parameters as separate arguments
Default: 'interaction_pooling' if not specified (transpiler chooses appropriate default)
Example in SQL: encoder='precomputed_user', input_user_id='$user_id'
Note: In YAML/JSON/Python SDK, use query_encoder as an object instead

where (optional, string):

Filter expression using DataFusion SQL syntax
Applied during the retrieval phase for better performance
Example: where='category = "electronics" AND price < 100'
Supports parameters: where='category = $category'

name (optional, string):

Identifier for this step in query execution logs
Useful for debugging complex queries
Example: name='retrieve_similar_items'
text_search()​

Performs full-text search using lexical or vector search.

ShapedQL
Python SDK
TypeScript SDK
YAML
-- Basic syntax
text_search(
    query='$query',
    mode='lexical',
    limit=100,
    entity_type='items',
    where='optional_filter_expression',
    name='optional_step_name'
)

-- Lexical search example
SELECT name, price
FROM retrieve(text_search(query='$query', mode='lexical', entity_type='items'))

-- Vector search with filter
SELECT * 
FROM retrieve(text_search(
    query='$query', 
    mode='vector', 
    where='category = "electronics" AND price < 100', 
    limit=50
))
LIMIT 20


Parameters:

query (required, string, SQL syntax only):

The search query string (SQL syntax uses query, but transpiles to input_text_query)
For vector search, this will be encoded using the specified text embedding
Example: query='wireless headphones'
Note: In YAML/JSON/Python SDK, use input_text_query instead

mode (required, string or object):

Search mode to use
In SQL syntax: mode='lexical' or mode='vector'
In YAML/JSON/Python SDK: Object with type field
Lexical: {'type': 'lexical'} or {type: lexical}
Vector: {'type': 'vector', 'text_embedding_ref': 'embedding_name'} or {type: vector, text_embedding_ref: embedding_name}
Options:
'lexical': Traditional text search using BM25 scoring
'vector': Semantic search using embeddings (requires text_embedding_ref)
Example: mode='vector' (SQL) or mode={'type': 'vector', 'text_embedding_ref': 'text_embedding'} (Python SDK)

limit (optional, int, default: 100):

Maximum number of results to return
For best performance, keep this under 1000
Example: limit=50

entity_type (optional, string, default: 'items'):

Type of entities to search
Allowed values: 'items', 'users', or custom entity types
Example: entity_type='products'

where (optional, string):

Additional filter expression in DataFusion SQL syntax
Applied after text search for additional filtering
Example: where='price < 100 AND in_stock = true'
Supports parameters: where='category = $category'

name (optional, string):

Identifier for this step in query execution logs
Useful for debugging and monitoring
Example: name='product_search'

Performance Tips:

Use where clauses to filter results early in the pipeline
For best performance with vector search, ensure your embeddings are pre-computed
For lexical search, consider using fuzziness_edit_distance in the mode object for fuzzy matching
column_order()​

Retrieves candidates ordered by column values.

ShapedQL
Python SDK
TypeScript SDK
YAML
-- Basic syntax
column_order(
    columns='col1 DESC, col2 ASC',
    limit=100,
    entity_type='items',
    where='optional_filter_expression',
    name='optional_step_name'
)

-- Order by single column
SELECT * FROM retrieve(column_order(columns='price DESC', limit=100))

-- Order by multiple columns
SELECT * FROM retrieve(column_order(columns='category ASC, price DESC', limit=100))

-- With filter expression
SELECT * FROM retrieve(column_order(
    columns='rating DESC', 
    where='category = "electronics"', 
    limit=200
))


Parameters:

columns (required): Column(s) to order by
In SQL syntax: String format like 'price DESC, rating ASC' or 'column_name ASC NULLS FIRST'
In YAML/JSON/Python SDK: Array of objects with name, ascending (boolean), and optionally nulls_first (boolean)
Example SQL: columns='price DESC, rating ASC'
Example Python: columns=[{'name': 'price', 'ascending': False}, {'name': 'rating', 'ascending': True}]
Example YAML:
columns:
  - name: price
    ascending: false
  - name: rating
    ascending: true
    nulls_first: false

limit (default: 100): Maximum number of candidates to retrieve
entity_type (default: 'items'): Type of entities to retrieve
where (optional): Filter expression
name (optional): Step name for debugging/explanation

Column Ordering Syntax (SQL):

column_name ASC - Ascending order
column_name DESC - Descending order
column_name ASC NULLS FIRST - Nulls first
column_name DESC NULLS LAST - Nulls last

Multiple columns can be specified, separated by commas.

Derived columns:

With an interaction_table, Shaped automatically generates two convenience columns:

_derived_popular_rank: Popularity score from interaction frequency and recency
_derived_chronological_rank: Chronological ranking from item timestamps

Useful for popular item retrieval, trending algorithms, and chronological ordering. See Derived columns for details.

Example:

ShapedQL
Python SDK
TypeScript SDK
SELECT * FROM retrieve(column_order(columns='price DESC, rating ASC', limit=100))
WHERE in_stock = true
LIMIT 20


Example with derived columns:

ShapedQL
Python SDK
TypeScript SDK
-- Popular items
SELECT * FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=100))
LIMIT 20

ShapedQL
Python SDK
TypeScript SDK
-- Chronological items
SELECT * FROM retrieve(column_order(columns='_derived_chronological_rank DESC', limit=100))
LIMIT 20

filter()​

Retrieves candidates matching a filter expression. The where parameter uses the same DataFusion SQL syntax as the WHERE clause. See the WHERE Clause section for complete syntax documentation.

ShapedQL
Python SDK
TypeScript SDK
filter(
    where='expression',
    limit=100,
    entity_type='items',
    name='optional_step_name'
)


Parameters:

where (required): Filter expression using DataFusion SQL syntax. Note: Subqueries are not supported.
limit (default: 100): Maximum number of candidates to retrieve
entity_type (default: 'items'): Entity type to retrieve
name (optional): Step name for debugging/explanation

Examples:

ShapedQL
Python SDK
TypeScript SDK
YAML
-- Simple filter expression
SELECT * FROM retrieve(filter(where='category = "electronics" AND price < 100', 
                     limit=200))
LIMIT 20

-- Using a parameter
SELECT * FROM retrieve(filter(where='category = $category AND price < $max_price',
                     limit=100))
LIMIT 10

ids()​

Retrieves a specific list of entity IDs. This is the primary retriever for reranking use-cases where you already have a set of candidates.

ShapedQL
Python SDK
TypeScript SDK
YAML
-- Basic syntax
ids(item_ids=['item1', 'item2', 'item3'], 
    where='optional_filter_expression',
    name='optional_step_name')

-- Using a parameter
SELECT score(expression='click_through_rate', input_user_id='$user_id') AS s, *
FROM retrieve(ids($candidate_item_ids)) ORDER BY s LIMIT 10

-- Reranking with diversity
SELECT score(expression='click_through_rate', input_user_id='$user_id') AS s,
       diversity(score=s, strength=0.3) AS r, *
FROM retrieve(ids($item_ids)) ORDER BY r LIMIT 10


Parameters:

item_ids (required, list of strings or parameter): The list of entity IDs to retrieve. Can be provided as a parameter reference (e.g., $candidate_item_ids) or as a literal list.
where (optional, string): Filter expression using DataFusion SQL syntax applied to the retrieved IDs.
name (optional, string): Identifier for this step in query execution logs.

Use Cases:

Reranking: When you have a list of candidates from an external source (e.g., search engine, business logic) and want to reorder them using Shaped's scoring models.
Filtering by IDs: When you want to retrieve specific items by their IDs and apply additional filtering or scoring.

Example:

ShapedQL
Python SDK
TypeScript SDK
SELECT score(expression='click_through_rate', input_user_id='$user_id',
             input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(ids($candidate_item_ids)) ORDER BY s LIMIT 10

candidate_attributes()​

Retrieves candidates from attributes provided at query time. Used for reranking items not in the catalog.

ShapedQL
Python SDK
TypeScript SDK
candidate_attributes($item_attributes, entity_type='items', where='optional_filter_expression')


Parameters:

item_attributes (required, list of objects or parameter reference):
In SQL syntax: Parameter reference like $item_attributes (first positional argument)
In YAML/JSON/Python SDK: Array of item attribute dictionaries or parameter reference
Example SQL: candidate_attributes($item_attributes)
Example Python: CandidateAttributes(item_attributes='$item_attributes') or CandidateAttributes(item_attributes=[{'title': 'Item 1', 'category': 'electronics'}])
entity_type (default: 'items'): Entity type to retrieve
where (optional): Filter expression using DataFusion SQL syntax (see WHERE Clause)
name (optional): Step name for debugging/explanation

Example:

ShapedQL
Python SDK
TypeScript SDK
SELECT * FROM candidate_attributes($item_attributes)
LIMIT 10

... (rest of the code remains the same)
Query Encoders​

Query encoders determine how the query vector is created for similarity search. They are specified via the encoder parameter in similarity() retrievers.

Default Encoders:

precomputed_user - Default when using precomputed user embeddings
interaction_pooling - Default when using interaction-based encoders

If no encoder is specified, the system will choose an appropriate default based on the embedding type and available data.

precomputed_user (default)​

Uses a precomputed user embedding. This is the default encoder for user-based recommendations when precomputed embeddings are available.

ShapedQL
Python SDK
TypeScript SDK
similarity(embedding_ref='als', encoder='precomputed_user', 
          input_user_id='$user_id')


Parameters:

input_user_id (default: '$user_id'): User ID parameter or value to use for the precomputed embedding.
precomputed_item​

Uses a precomputed item embedding. Useful for item-to-item similarity queries.

ShapedQL
Python SDK
TypeScript SDK
similarity(embedding_ref='als', encoder='precomputed_item', 
          input_item_id='$item_id')


Parameters:

input_item_id (default: '$item_id'): Item ID parameter or value to use for the precomputed embedding.
interaction_pooling (default)​

Creates a query vector by pooling embeddings from a user's interaction history. This encoder retrieves the user's recent interactions and pools their item embeddings. This is the default encoder when using interaction-based recommendations.

ShapedQL
Python SDK
TypeScript SDK
similarity(embedding_ref='als', encoder='interaction_pooling',
          input_user_id='$user_id',
          truncate_interactions=20,
          pooling_function='mean')


Parameters:

input_user_id (default: '$user_id'): User ID parameter or value to pool interactions for.
truncate_interactions (default: 10): Maximum number of interactions to use for pooling.
pooling_function (default: 'mean'): Function to use when pooling multiple embeddings. Options: 'mean', 'max', 'sum', 'min'.
interaction_round_robin​

Creates a query vector using round-robin retrieval from user interaction clusters. This encoder groups interactions into clusters and retrieves from each cluster in a round-robin fashion.

ShapedQL
Python SDK
TypeScript SDK
similarity(embedding_ref='als', encoder='interaction_round_robin',
          input_user_id='$user_id',
          num_clusters=5,
          pooling_function='mean')


Parameters:

input_user_id (default: '$user_id'): User ID parameter or value for round-robin retrieval.
num_clusters (default: 5): Number of interaction clusters to create.
pooling_function (default: 'mean'): Function to use when pooling cluster results. Options: 'mean', 'max', 'sum', 'min'.
user_attribute_pooling​

Creates a query vector by encoding the user's attributes. This can only be used with a content or text embedding.

ShapedQL
Python SDK
TypeScript SDK
similarity(embedding_ref='content_embedding', encoder='user_attribute_pooling',
          input_user_id='$user_id',
          input_user_features='$user_features')


Parameters:

input_user_id (optional): User ID parameter or value to encode. If provided, user features from the database will be merged with input_user_features.
input_user_features (optional): User features dictionary to encode. This will be merged with features from input_user_id if both are provided.
item_attribute_pooling​

Creates a query vector by encoding the item's attributes. This can only be used with a content or text embedding.

ShapedQL
Python SDK
TypeScript SDK
similarity(embedding_ref='content_embedding', encoder='item_attribute_pooling',
          input_item_id='$item_id',
          input_item_features='$item_features')


Parameters:

input_item_id (optional): Item ID parameter or value to encode. If provided, item features from the database will be merged with input_item_features.
input_item_features (optional): Item features dictionary to encode. This will be merged with features from input_item_id if both are provided.
Filter Functions​

Filter functions are used in the WHERE clause to apply prebuilt filters or truncate candidate sets.

prebuilt()​

Applies a prebuilt filter defined in your model configuration.

WHERE prebuilt('filter_name', input_user_id='$user_id')


Parameters:

First argument or filter_ref (required): Filter name (e.g., 'filter_name')
input_user_id (optional): User ID parameter for personal filters
name (optional): Step name for debugging/explanation

Filter References:

Prebuilt filters are defined in your model configuration and can be referenced by name. The filter name should match a filter defined in data.filters.

Example query:

SELECT * FROM retrieve(similarity(embedding_ref='als', limit=100))
WHERE price > 100 AND prebuilt('exclude_purchased', input_user_id='$user_id')
LIMIT 20


This assumes you have a filter named exclude_purchased defined in your model configuration.

Example engine configuration:

The following config creates a filter dataset of all the items a user has reviewed before.

data:
  filters:
    - name: exclude_seen_items
      filter_type: 
        type: personal_filter
        user_id_column: user_id
        item_id_column: item_id
      filter_table: 
        type: query
        query: SELECT item_id, user_id FROM reviews
[...rest of engine config]

truncate()​

Truncates the candidate set to a maximum length.

WHERE truncate(500)


Parameters:

First argument or max_length (required): Maximum number of candidates to keep
name (optional): Step name for debugging/explanation

Example:

SELECT * FROM retrieve(similarity(embedding_ref='als', limit=1000))
WHERE truncate(500)
LIMIT 20

Reorder Functions​

Reorder functions (rerankers) apply post-retrieval reordering to diversify or explore the results.

Specify rerankers in the SELECT list with an alias, then order by that alias. Example: SELECT diversity(score=s, strength=0.3) AS r, * FROM ... ORDER BY r LIMIT 20. Supported rerankers: diversity(...), exploration(...), boost(...).

diversity()​

Applies diversity reordering to reduce similarity between consecutive results.

SELECT score(expression='m1') AS s, diversity(score=s, strength=0.3) AS r, *
FROM retrieve(similarity(embedding_ref='als', limit=50)) ORDER BY r LIMIT 20


Parameters:

First argument or strength (default: 0.5): Diversity strength (0.0 to 1.0)
diversity_lookback_window (default: 30): Number of previous items to consider for diversity.
diversity_lookforward_window (default: 30): Top number of candidate items in the ranked list to consider for diversity.
diversity_attributes (default: None): Which attributes to look at when determining diversity. Defaults to all supported fields.
text_encoding_embedding_ref (default: None): Which text embedding to use when determining diversity.
exploration()​

Applies exploration reordering to balance exploitation and exploration. This injects items from a specified retriever into the main ranking results. All items from the exploration retriever are treated with equal weight (1.0), and the strength parameter determines how often exploration items are selected over top-scored items.

ShapedQL
Python SDK
TypeScript SDK
YAML
-- Option 1: Reference a named retriever from FROM (retriever parameter by name).
SELECT score(expression='click_through_rate', input_user_id='$user_id',
             input_interactions_item_ids='$interaction_item_ids') AS s,
       exploration(score=s, retriever='explore', strength=0.3) AS r, *
FROM retrieve(
    similarity(embedding_ref='als', input_user_id='$user_id', limit=100, name='main'),
    filter(where='category = "new_releases"', name='explore')
)
ORDER BY r LIMIT 20

-- Option 2: Specify the exploration retriever inline.
SELECT score(expression='click_through_rate', input_user_id='$user_id',
             input_interactions_item_ids='$interaction_item_ids') AS s,
       exploration(score=s, retriever=filter(where='category = "new_releases"'),
                   strength=0.3) AS r, *
FROM retrieve(similarity(embedding_ref='als', input_user_id='$user_id', limit=100))
ORDER BY r LIMIT 20


Filtering: Same filter stage as main candidates (pagination, prebuilt, expression) before blending.

Parameters:

retriever (optional): Retriever function to use for exploration. If not specified, uses the first retriever from the FROM clause. If specified in ShapedQL, must be a full retriever function call (e.g., filter(where='category = "new_releases"')). Cannot be a string name reference in ShapedQL (though YAML/JSON formats support string references to named retrievers).
strength (default: 0.5): Exploration strength (0.0 to 1.0). Higher values inject more items from the exploration pool.
diversity_lookback_window (default: 20): Number of previous items to consider when applying diversity alongside exploration.
boosted()​

Applies boosted reordering using boost values from item metadata. Unlike exploration(), which treats all items equally, boosted() uses the boost column from item metadata as weights. Items with higher boost values have a higher probability of being selected during injection.

Key Differences from exploration():

exploration(): All items from the retriever have equal weight (1.0)
boosted(): Items use their boost column value as weight, so items with higher boost values are more likely to be selected

Filtering: Same as exploration().

ShapedQL
Python SDK
TypeScript SDK
YAML
-- Option 1: Reference a named retriever from FROM (retriever parameter by name).
SELECT score(expression='click_through_rate', input_user_id='$user_id',
             input_interactions_item_ids='$interaction_item_ids') AS s,
       boosted(score=s, retriever='boosted_items', strength=0.3) AS r, *
FROM retrieve(
    similarity(embedding_ref='als', input_user_id='$user_id', limit=100, name='main'),
    filter(where='boost > 0', name='boosted_items')
)
ORDER BY r LIMIT 20

-- Option 2: Specify the boost retriever inline.
SELECT score(expression='click_through_rate', input_user_id='$user_id',
             input_interactions_item_ids='$interaction_item_ids') AS s,
       boosted(score=s, retriever=filter(where='boost > 0'), strength=0.3) AS r, *
FROM retrieve(similarity(embedding_ref='als', input_user_id='$user_id', limit=100))
ORDER BY r LIMIT 20


Parameters:

retriever (optional): Retriever function to use for boosting. If not specified, uses the first retriever from the FROM clause. If specified in ShapedQL, must be a full retriever function call (e.g., filter(where='boost > 0')). Cannot be a string name reference in ShapedQL (though YAML/JSON formats support string references to named retrievers). Items from this retriever should have a boost column in their metadata.
strength (default: 0.5): Boost strength (0.0 to 1.0). Closer to 1.0 pulls more items from the boosted retriever. Items with boost=1 are prioritized most strongly.

Multiple rerankers:

List multiple rerankers in SELECT with aliases, then order by the final one:

SELECT score(expression='m1') AS s,
       diversity(score=s, strength=0.3) AS d,
       exploration(score=s, retriever='promoted', strength=0.2) AS e, *
FROM retrieve(...) ORDER BY e LIMIT 20

Parameters​

Parameters allow runtime value substitution using $parameter_name or $parameter.name syntax.

Parameter Syntax​
$param_name - Simple parameter reference
$parameter.param_name - Explicit parameter reference
$param.param_name - Alternative syntax (normalized to $parameter.name)

Supported Parameter Types:

int - Integer values
float - Floating-point numbers
str - String values
bool - Boolean values (true/false)
List[int] - Arrays of integers
List[float] - Arrays of floats
List[str] - Arrays of strings
List[bool] - Arrays of booleans

Important Notes:

Parameters are substituted at query execution time, not at transpilation time
Parameter names must be valid identifiers (letters, numbers, underscores)
limit is a reserved keyword and cannot be used as a parameter name (use max_results or similar instead)
Nested function calls are not supported in parameter values
Common Parameters​
$user_id - User identifier
$item_id - Item identifier
$query - Search query text
$item_ids - List of item IDs for reranking
$item_attributes - Item attributes for reranking
$limit - Result limit (use LIMIT clause instead when possible)
Parameter Examples​
-- Using user_id parameter
SELECT * FROM retrieve(similarity(embedding_ref='als', 
                       encoder='precomputed_user',
                       input_user_id='$user_id'))
LIMIT 10

-- Using query parameter
SELECT * FROM retrieve(text_search(query='$query', mode='lexical'))
LIMIT 20

-- Using item_ids parameter for reranking
SELECT * FROM retrieve(ids($item_ids)) LIMIT 10

SELECT Clause​

The SELECT clause specifies which columns to return and, in the canonical form, which score and reranker expressions to compute.

SELECT * - Returns all columns (default)
SELECT column1, column2 - Returns specific columns
Canonical: SELECT score(expression='...') AS alias - Defines the scoring expression; use ORDER BY alias to sort by it.
Canonical: SELECT diversity(...) AS alias, exploration(...) AS alias, boost(...) AS alias - Rerankers as computed columns; use ORDER BY alias to apply them. Only one score() is allowed per query; multiple rerankers are allowed.

Example (canonical):

SELECT score(expression='m1') AS s, diversity(score=s, strength=0.3) AS r, *
FROM retrieve(similarity(embedding_ref='als', limit=50)) ORDER BY r LIMIT 10


Example (simple columns):

SELECT name, price, category
FROM retrieve(similarity(embedding_ref='als', limit=50))
LIMIT 10

WHERE Clause​

The WHERE clause applies filtering expressions using DataFusion SQL syntax. You can combine regular SQL expressions with filter functions. The same filter expression syntax is also used in the where parameter of all retriever functions (see Retriever Functions).

Filter expressions use DataFusion SQL syntax and are evaluated in two contexts:

Retrieval layer: In the where parameter of any retriever function (e.g., similarity(), text_search(), column_order(), filter(), etc.)
Post-retrieval: In the WHERE clause of ShapedQL queries
Supported Operations​

Filter expressions support the following operators and functions:

Comparison Operators:

=, !=, >, >=, <, <=

Logical Operators:

AND, OR, NOT

Null Checks:

IS NULL, IS NOT NULL

Boolean Checks:

IS TRUE, IS NOT TRUE, IS FALSE, IS NOT FALSE

Membership Operations:

IN (...), NOT IN (...) - Note: Subqueries are not supported inside IN clauses. Use a list of values or a parameter instead.

String Operations:

LIKE, NOT LIKE
ILIKE (case-insensitive LIKE)

Range Operations:

BETWEEN ... AND ...

Functions:

regexp_match(column, pattern) - Regular expression matching
CAST(value AS type) - Type casting
array_has(sequential_column, value) - Check if array contains value
array_has_any(sequential_column, values) - Check if array contains any value from list
array_has_all(sequential_column, values) - Check if array contains all values from list

Boolean Values:

true, false
Examples​

Simple Comparisons:

-- Basic comparison
WHERE category = 'electronics' AND price < 100

-- Multiple conditions
WHERE price > 50 AND price < 500 AND in_stock = true


Complex Expressions with Parentheses:

-- Grouped conditions
WHERE (category = 'electronics' OR category = 'computers')
  AND price BETWEEN 50 AND 500

-- Nested logic
WHERE ((label IN [10, 20]) AND (note.email IS NOT NULL))
  OR NOT note.created


Null and Boolean Checks:

-- Null checks
WHERE description IS NOT NULL AND author IS NULL

-- Boolean checks
WHERE is_published IS TRUE AND is_archived IS NOT TRUE


String Matching:

-- LIKE pattern matching
WHERE name LIKE '%shirt%' AND description LIKE 'Blue%'

-- Case-insensitive matching
WHERE category ILIKE 'ELECTRONICS'


Array Operations:

-- Check if array contains value
WHERE array_has(category_sequence, 'sports')

-- Check if array contains any value from list
WHERE array_has_any(category_sequence, ['sports', 'news'])

-- Check if array contains all values from list
WHERE array_has_all(tags, ['featured', 'popular'])


Regular Expressions:

-- Regex pattern matching
WHERE regexp_match(description, '^[A-Z].*')


Type Casting:

-- Cast to different type
WHERE CAST(price AS INTEGER) > 100


With Filter Functions:

-- Combining SQL expressions with filter functions
WHERE price > 100 
  AND prebuilt('ref:data.filters:category_filter', input_user_id='$user_id')
  AND truncate(500)


Note: Filter expressions are evaluated using DataFusion SQL syntax, so DataFusion functions and operators are supported. Use parameters for dynamic values rather than trying to embed complex expressions.

ORDER BY Clause​

The ORDER BY clause specifies how to score and sort results in the score stage of the query pipeline. It maps to the score block in the JSON query configuration.

When to use ORDER BY:

Omit ORDER BY - Uses the retriever's default score (PassthroughScore)
SELECT score(...) AS alias - Put the scoring expression in the SELECT list with an alias, then use ORDER BY alias. Example: SELECT score(expression='m1') AS s, * FROM ... ORDER BY s LIMIT 20. The expression is a value model string that can reference models, user/item attributes, retrieval scores, and functions.

Default scoring (no ORDER BY):

-- Use retriever's default score - no ORDER BY needed
SELECT * FROM retrieve(similarity(embedding_ref='als', limit=50))
LIMIT 10


Custom expression scoring:

Put the scoring expression in SELECT with an alias, then ORDER BY alias:

-- Single model
SELECT score(expression='click_through_rate', input_user_id='$user_id',
             input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(similarity(embedding_ref='als', limit=50)) ORDER BY s LIMIT 10

-- Ensemble of multiple models
SELECT score(expression='0.6 * click_through_rate + 0.4 * conversion_rate',
             input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20

-- Simple expression combining model scores
SELECT score(expression='0.6 * click_through_rate + 0.4 * conversion_rate',
             input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(similarity(embedding_ref='als', limit=50)) ORDER BY s LIMIT 10


The score() function evaluates the value model expression with the provided user context and interaction history. User context comes from input_user_id and input_interactions_item_ids query parameters. See the Value Model Expressions section below for available objects, functions, and operators.

Value Model Expressions​

Value model expressions are Python-like mathematical expressions evaluated per user-item pair to compute a relevance score. Use them inside score() in your SELECT list, e.g. SELECT score(expression='...') AS s, * FROM retrieve(...) ORDER BY s. They support accessing user/item attributes, trained model outputs, retrieval scores, text encodings, and various utility functions.

Available Objects​

User Object (user):

Access all attributes from your user table (use in SELECT with an alias, then ORDER BY that alias):

score(expression='click_through_rate + 0.1 * user.age + 0.05 * user.membership_tier', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


Common attributes: user.user_id, user.age, user.location, user.interests, etc. All columns from your user table are available.

Item Object (item):

Access all attributes from your item table:

score(expression='click_through_rate - 0.05 * item.price + 0.1 * item.rating', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


Common attributes: item.item_id, item.price, item.category, item.rating, etc. All columns from your item table are available.

Retrieval Object (retrieval):

Access scores and ranks from named retrievers in your query. Retrieval scores are only materialized if referenced in the expression (performance optimization).

Direct Score Attributes:

Access retriever scores by name:

score(expression='0.5 * retrieval.vector_search + 0.5 * retrieval.lexical_search', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


Rank Attributes:

Access retriever ranks with _rank suffix:

score(expression='click_through_rate - 0.01 * retrieval.vector_search_rank', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


Methods:

retrieval.get_score(name, default=0.0) - Get score with default value
retrieval.get_rank(name, default=999) - Get rank with default value

Example:

score(expression='click_through_rate + 0.1 * retrieval.get_score("vector_search", 0.0)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')

Rank fusion (RRF)​

Reciprocal rank fusion (RRF) combines multiple ranked lists using only ranks. This is useful when mixing retrievers with different score scales.

score(expression='1.0 / (60 + retrieval.get_rank("vector_search", 999)) + 1.0 / (60 + retrieval.get_rank("lexical_search", 999))')

Available Functions​

Text Encoding Functions:

text_encoding(entity, embedding_ref='text_embedding') - Get text encoding vector for a user or item entity using the specified embedding. Returns None if encoding is not available.

score(expression='cosine_similarity(text_encoding(user, embedding_ref=''text_embedding''), text_encoding(item, embedding_ref=''text_embedding''))', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


pooled_text_encoding(recent_interactions, pool_fn='mean', embedding_ref='text_embedding') - Compute pooled encoding from user's recent interactions using the specified embedding. Pooling functions: 'mean', 'max'.

score(expression='cosine_similarity(pooled_text_encoding(user.recent_interactions, pool_fn=''mean'', embedding_ref=''text_embedding''), text_encoding(item, embedding_ref=''text_embedding''))', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')

Text reranking functions​

Use these zero-shot rerankers for text-based reranking on a smaller candidate set. In these examples, $params.query is a request parameter containing the query text.

colbert_v2(item, query) - Late-interaction text reranker.
cross_encoder(item, query) - Cross-encoder text reranker.

Examples:

SELECT score(expression='colbert_v2(item, $params.query)') AS s, *
FROM retrieve(ids($candidate_item_ids)) ORDER BY s LIMIT 20

SELECT score(expression='cross_encoder(item, $params.query)') AS s, *
FROM retrieve(ids($candidate_item_ids)) ORDER BY s LIMIT 20


Similarity Functions:

cosine_similarity(a, b) - Compute cosine similarity between two vectors. Returns 0.0 if either vector is None.

score(expression='0.5 * click_through_rate + 0.5 * cosine_similarity(text_encoding(user, embedding_ref=''text_embedding''), text_encoding(item, embedding_ref=''text_embedding''))', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


dot(a, b) - Compute dot product of two vectors. Returns 0.0 if either vector is None.

Distance Functions:

haversine_distance(lat1, lon1, lat2, lon2) - Calculate distance in kilometers between two geographic coordinates.

score(expression='click_through_rate - 0.1 * haversine_distance(user.lat, user.lon, item.lat, item.lon)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


Utility Functions:

coalesce(*args) - Return the first non-null, non-NaN value from arguments.

score(expression='click_through_rate + 0.1 * coalesce(user.age, 25)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


now_seconds() - Return current Unix timestamp in seconds.

Math Functions:

Standard Python math functions are available: abs(), sqrt(), log(), exp(), max(), min(), pow(), round(), etc.

score(expression='click_through_rate + 0.1 * log(item.price + 1)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')

Operators​

Value model expressions support standard Python operators:

Arithmetic: +, -, *, /, ** (exponentiation), % (modulo)
Comparison: ==, !=, >, <, >=, <=
Logical: and, or, not
Conditional: if ... else ... (ternary operator)
Model References​

Reference trained models from your engine configuration by name:

score(expression='0.6 * click_through_rate + 0.4 * conversion_rate', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids')


Model names must match the model names defined in your engine's training block.

Policy Features​

Policy features from policy_scores_dict are available as direct variables in the expression. These are features computed by policy models (e.g., embedding policies).

Expression Evaluation​
Value models are evaluated pair-wise (one score per user-item pair)
All functions handle None values gracefully (return 0.0 or default values)
Expressions must return a numeric value (float or int)
Value Model Examples​

Simple Model Scoring:

SELECT score(expression='click_through_rate', input_user_id='$user_id',
             input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(similarity(embedding_ref='als', limit=50)) ORDER BY s LIMIT 10


Ensemble of Multiple Models:

SELECT score(expression='0.6 * click_through_rate + 0.4 * conversion_rate',
             input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20


Combining Model Scores with Retrieval Scores:

SELECT score(expression='0.5 * retrieval.vector_search + 0.3 * retrieval.lexical_search + 0.2 * click_through_rate', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(
    text_search(query=$query, mode='vector', limit=50, name='vector_search'),
    text_search(query=$query, mode='lexical', limit=50, name='lexical_search')
) ORDER BY s LIMIT 20


Using Text Encodings for Similarity:

SELECT score(expression='0.7 * click_through_rate + 0.3 * cosine_similarity(text_encoding(user, embedding_ref=''text_embedding''), text_encoding(item, embedding_ref=''text_embedding''))', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(similarity(embedding_ref='als', limit=50)) ORDER BY s LIMIT 10


Using User and Item Attributes:

SELECT score(expression='click_through_rate + 0.1 * user.age - 0.05 * item.price + 0.2 * item.rating', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20


Using Pooled Text Encodings from Interactions:

SELECT score(expression='0.6 * click_through_rate + 0.4 * cosine_similarity(pooled_text_encoding(user.recent_interactions, pool_fn=''mean'', embedding_ref=''text_embedding''), text_encoding(item, embedding_ref=''text_embedding''))', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(similarity(embedding_ref='als', limit=50)) ORDER BY s LIMIT 10


Complex Expression with Multiple Features:

SELECT score(expression='0.4 * click_through_rate + 0.3 * retrieval.vector_search + 0.2 * cosine_similarity(text_encoding(user, embedding_ref=''text_embedding''), text_encoding(item, embedding_ref=''text_embedding'')) + 0.1 * (user.age / 100.0) - 0.05 * log(item.price + 1)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20


Using Geographic Distance:

SELECT score(expression='click_through_rate - 0.1 * haversine_distance(user.lat, user.lon, item.lat, item.lon)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20


Using Retrieval Ranks:

SELECT score(expression='click_through_rate - 0.01 * retrieval.vector_search_rank - 0.005 * retrieval.lexical_search_rank', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(
    text_search(query=$query, mode='vector', limit=50, name='vector_search'),
    text_search(query=$query, mode='lexical', limit=50, name='lexical_search')
) ORDER BY s LIMIT 20

Common Value Model Patterns​

Popular (by upvotes):

SELECT score(expression='item.upvotes', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20


Chronological (by publish date):

SELECT score(expression='item.published_at', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20


Trendy (popularity with time decay):

SELECT score(expression='(item.score - 1) / ((((now_seconds() - item.published_at) / 3600) + 2) ** 1.8)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20


Personalized (trendy with personalization):

SELECT score(expression='((item.score / 1000) + cosine_similarity(text_encoding(item, embedding_ref=''text_embedding''), pooled_text_encoding(user.recent_interactions, embedding_ref=''text_embedding''))) / ((((now_seconds() - item.published_at) / 3600) + 2) ** 1.8)', input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s, *
FROM retrieve(column_order(columns='_derived_popular_rank ASC', limit=1000))
ORDER BY s LIMIT 20

LIMIT Clause​

The LIMIT clause specifies the maximum number of results to return.

LIMIT 20


Or using a parameter:

LIMIT $limit


Note: The LIMIT applies after all retrieval, filtering, scoring, and reordering operations.

Complete Examples​
Basic Similarity Search​
SELECT * 
FROM retrieve(similarity(embedding_ref='als', limit=50, 
                         encoder='precomputed_user', input_user_id='$user_id'))
LIMIT 10

Text Search with Filtering​
SELECT name, price, category
FROM retrieve(text_search(query='$query', mode='lexical', entity_type='items', limit=100))
WHERE category = 'electronics' AND price < 500
LIMIT 20

User Search​
SELECT * 
FROM retrieve(text_search(query='$query', entity_type='users', limit=50))
LIMIT 10

Reranking with Diversity​
SELECT score(expression='click_through_rate', input_user_id='$user_id') AS s,
       diversity(score=s, strength=0.3) AS r, *
FROM retrieve(ids($item_ids)) ORDER BY r LIMIT 10

Complex Query with Multiple Filters​
SELECT score(expression='0.7 * similarity_score + 0.3 * rating',
             input_user_id='$user_id', input_interactions_item_ids='$interaction_item_ids') AS s,
       diversity(score=s, strength=0.2) AS d,
       exploration(score=s, strength=0.1) AS e, name, price, rating
FROM retrieve(similarity(embedding_ref='als', limit=200,
                         encoder='interaction_pooling',
                         input_user_id='$user_id',
                         truncate_interactions=20))
WHERE price > 100 
  AND category IN ('electronics', 'computers')
  AND prebuilt('ref:data.filters:exclude_purchased', input_user_id='$user_id')
  AND truncate(500)
ORDER BY e LIMIT 20

Column Ordering​
SELECT * 
FROM retrieve(column_order(columns='price DESC, rating DESC NULLS LAST', limit=100))
WHERE in_stock = true
LIMIT 20

Query Patterns and Recipes​
Pattern: Cold Start Recommendations​

For new users without interaction history, use attribute-based similarity:

SELECT score(expression='m1') AS s, diversity(score=s, strength=0.3) AS r, *
FROM retrieve(similarity(embedding_ref='content_embedding',
                         encoder='user_attribute_pooling',
                         input_user_features='$user_features',
                         limit=100))
ORDER BY r LIMIT 20

Pattern: Multi-Stage Retrieval​

Retrieve from multiple sources and combine:

SELECT score(expression='m1') AS s, diversity(score=s, strength=0.2) AS r, *
FROM retrieve(
    similarity(embedding_ref='collaborative', limit=50),
    similarity(embedding_ref='content', limit=50),
    text_search(query='$query', mode='lexical', limit=50)
)
WHERE category = '$category' ORDER BY r LIMIT 20

Pattern: Time-Based Filtering​

Filter by recency using date comparisons:

SELECT * 
FROM retrieve(similarity(embedding_ref='als', limit=100))
WHERE created_at > '2024-01-01'
  AND last_interaction > '2024-12-01'
LIMIT 20


For dynamic dates, use parameters:

SELECT * 
FROM retrieve(similarity(embedding_ref='als', limit=100))
WHERE created_at > $start_date
  AND last_interaction > $recent_date
LIMIT 20

Pattern: A/B Testing Queries​

Use parameters to switch between query variants. Note that parameters work best for values, not entire expressions:

SELECT score(expression='m1') AS s, diversity(score=s, strength=$diversity_strength) AS r, *
FROM retrieve(similarity(embedding_ref=$embedding_name, limit=$retriever_limit))
WHERE category = $test_category ORDER BY r LIMIT $result_limit


For more complex A/B testing, define separate saved queries and switch between them at the application level.

Pattern: Category-Specific Recommendations​

Personalize by category with fallback:

SELECT * 
FROM retrieve(similarity(embedding_ref='als', 
                         encoder='interaction_pooling',
                         input_user_id='$user_id',
                         where='category = $category',
                         limit=50))
WHERE category = $category
LIMIT 20


If no results, fall back to general recommendations by omitting the category filter.

Unsupported Features​

The following SQL features are not supported:

JOINs - Use multiple retriever functions instead
Subqueries (in FROM or WHERE clause) - Use retriever functions or prebuilt filters instead
Nested function calls - Functions cannot be nested (e.g., similarity(embedding_ref=func('arg')) is invalid)
GROUP BY / Aggregations - This DSL is for ranking, not analytics
HAVING clause - Use WHERE instead
Window functions (OVER clause) - Not supported
Common Table Expressions (WITH clause) - Use retriever functions instead
Multiple statements - Only single SELECT statements are allowed
Table aliases - Not supported in FROM clause
Column aliases in SELECT - Column names are used as-is
Limits and Constraints​
Result Limits​
Engine queries (per-engine endpoint): Maximum 1000 results per query (LIMIT clause).
Global endpoint data queries (FROM data.*): Maximum 10,000 results; LIMIT is required.
Retriever limits: Each retriever can fetch up to the value set in its limit parameter (tune for recall vs performance).
String Length Limits​
Maximum string length: 1000 characters for string parameters and values
Performance Considerations​
Retriever Limits: Set appropriate limit values in retriever functions to balance recall and performance. Retrieving too many candidates can slow down queries.
Filter Complexity: Complex WHERE clauses with many conditions may impact performance. Consider using prebuilt filters for frequently-used filter patterns.
Multiple Retrievers: When using multiple retrievers, they execute in parallel for better performance.
Pagination​

Pagination tracks which results have been returned for a given pagination_key to ensure users see new content on subsequent requests. The system filters out items that have already been returned for the same key.

Configuration​

Enable pagination by setting page_expiration_in_seconds to a positive value in your engine's deployment config:

deployment:
  pagination:
    page_expiration_in_seconds: 600  # Set to 0 to disable (default)


Pagination only works when page_expiration_in_seconds > 0. When disabled (default), pagination_key has no effect.

Usage​

Provide a pagination_key to track which items have been returned.

{
  "query": "SELECT * FROM retrieve(similarity(embedding_ref='als', limit=50)) LIMIT 20",
  "parameters": {
    "user_id": "user123"
  },
  "pagination_key": "user123_session_abc",
  "return_explanation": true
}


Use the same pagination_key in subsequent requests to continue pagination.

Parameters​

pagination_key (optional, string)

Identifier for tracking returned items. Use any string you want.
Each unique key maintains separate pagination state.

ignore_pagination (optional, boolean, default: false)

When true, ignores pagination and returns results from the beginning.
API Usage​
Endpoints​

Global query (data + engine in one endpoint; see Query endpoints):

POST /v2/query – Execute a ShapedQL query. Use FROM data.* for analytics or FROM engine.engine_name.retrieve(...) for recommendations.

Per-engine ad-hoc and saved queries:

POST /v2/engines/{engine_name}/query – Execute a ShapedQL query string in that engine’s context (no data.* or engine.* prefix).
POST /v2/engines/{engine_name}/queries/{query_name} – Execute a saved query
GET /v2/engines/{engine_name}/queries – List all saved queries
GET /v2/engines/{engine_name}/queries/{query_name} – Get saved query details
Authentication​

All requests require an API key in the x-api-key header:

x-api-key: YOUR_API_KEY

Making Query Requests​

Queries can be executed via the API in two ways:

Ad-hoc queries: Send a SQL query string directly in the request
Saved queries: Reference a pre-saved query by name (defined in model configuration)

Key Differences:

Ad-hoc queries: Flexible, can be modified per request, but must be validated each time
Saved queries: Pre-validated, reusable, can define parameter schemas, better for production use
Defining Saved Queries​

Saved queries are defined in your model configuration YAML under the queries section:

queries:
  personalized_recommendations:
    params:
      user_id:
        type: string
        required: true
      limit:
        type: number
        default: 20
    query: |
      SELECT score(expression='m1', input_user_id='$user_id') AS s,
             diversity(score=s, strength=0.3) AS r, *
      FROM retrieve(similarity(embedding_ref='als', limit=100,
                               encoder='interaction_pooling',
                               input_user_id='$user_id'))
      ORDER BY r LIMIT $limit


Benefits of Saved Queries:

Pre-validated at deployment time (SQL syntax errors caught early)
Parameter schemas with types and defaults
Reusable across multiple API calls
Better performance (no re-parsing on each request)
Version controlled with your model configuration

Query Validation:

Saved queries are automatically validated when you create or update an engine. If a SQL query has syntax errors, you'll get a clear error message during engine setup, preventing deployment of invalid queries.

Ad-hoc Query Request:

{
  "query": "SELECT * FROM retrieve(similarity(embedding_ref='als', limit=50)) LIMIT 10",
  "parameters": {
    "user_id": "user123"
  },
  "return_metadata": true,
  "return_explanation": false
}


Saved Query Request:

{
  "parameters": {
    "user_id": "user123",
    "query": "laptop"
  },
  "return_metadata": true
}

Response Format​

Query responses include the following structure:

{
  "results": [
    {
      "id": "item123",
      "score": 0.95,
      "attributes": {
        "name": "Product Name",
        "price": 99.99,
        "category": "electronics"
      }
    }
  ],
  "explanation": {
    "retrieval": [...],
    "filtering": [...],
    "scoring": [...],
    "reordering": [...]
  }
}


Response Fields:

results: Array of result objects, each containing:
id: Entity identifier (string)
score: Relevance score (float, 0.0 to 1.0)
attributes: Entity metadata object (if return_metadata=true)
journey: Entity journey tracking object (if return_journey_explanations=true)
explanation: Detailed execution breakdown object (if return_explanation=true)
retrieval: List of retrieval step explanations
filtering: List of filtering step explanations
scoring: Scoring step explanation
reordering: List of reordering step explanations
pagination_key: Pagination key for fetching next page (string, only if more results available)

HTTP Status Codes:

200 OK - Query executed successfully
400 Bad Request - Invalid request format
401 Unauthorized - Missing or invalid API key
404 Not Found - Saved query not found (for saved query endpoint)
422 Unprocessable Entity - Query validation error (invalid SQL, missing parameters, etc.)
500 Internal Server Error - Server error during query execution

Empty Results:

If a query returns zero results, you'll still receive a 200 OK response with an empty results array. This is normal behavior - it means the query executed successfully but no entities matched your criteria. Use return_explanation=true to understand why no results were returned (e.g., filters removed all candidates).

Best Practices​
Query Design​

Set Appropriate Limits: Use retriever limit parameters to retrieve enough candidates (typically 50-200) while keeping final LIMIT reasonable (10-50 for most use cases).

Use Prebuilt Filters: For frequently-used filter patterns, define them as prebuilt filters in your model configuration and reference them with prebuilt().

Combine Retrievers: Use FROM retrieve(retriever1, retriever2, ...) to combine strategies (e.g. similarity + text_search); results are unioned and deduplicated.

Optimize WHERE Clauses: Place the most selective filters first in WHERE clauses. Use indexes on frequently-filtered columns.

Parameterize Queries: Use parameters for dynamic values (user IDs, search queries) rather than string concatenation.

Performance Tips​

Retriever Limits: Start with smaller retriever limits (50-100) and increase if needed. Larger limits improve recall but increase latency.

Filter Early: Apply filters in the WHERE clause or retriever where parameter to reduce the candidate set early in the pipeline.

Use Truncate: If you retrieve many candidates but only need a subset, use truncate() to limit before expensive scoring operations.

Diversity Strength: Use moderate diversity values (0.2-0.4) to balance diversity and relevance. Higher values may reduce relevance.

Column Selection: Use SELECT column1, column2 instead of SELECT * when you only need specific columns to reduce response size.

Security Considerations​

Parameter Validation: Always validate and sanitize user-provided parameters before passing them to queries.

SQL Injection Prevention: The query language automatically handles parameter substitution safely. Parameters are never concatenated into SQL strings. Never concatenate user input directly into query strings.

Access Control: Ensure proper authentication and authorization for query endpoints. Users should only be able to query data they have access to.

API Key Security: Never expose API keys in client-side code or public repositories. Use server-side proxies for client applications.

When to Use Each Retriever​
Retriever	Best For	Avoid When
similarity()	Personalized recommendations, similar items/users	No embeddings configured
text_search()	Search features, keyword queries	No text fields indexed
column_order()	Trending, newest, most popular	Need personalization
filter()	Rule-based retrieval, filtering only	Need ranking/scoring
ids()	Reranking known items	Initial retrieval (no candidates)
candidate_attributes()	Reranking new/ephemeral items	Items in catalog
Common Use Cases​
Personalized Recommendations​

Retrieve personalized recommendations for a user based on their interaction history:

SELECT score(expression='m1', input_user_id='$user_id') AS s,
       diversity(score=s, strength=0.3) AS r, *
FROM retrieve(similarity(embedding_ref='als', limit=100,
                         encoder='interaction_pooling',
                         input_user_id='$user_id',
                         truncate_interactions=20))
WHERE prebuilt('ref:data.filters:exclude_purchased', input_user_id='$user_id')
ORDER BY r LIMIT 20

Search with Filters​

Combine text search with attribute filtering:

SELECT name, price, category
FROM retrieve(text_search(query='$query', mode='lexical', limit=200))
WHERE category = '$category' 
  AND price BETWEEN $min_price AND $max_price
  AND in_stock = true
LIMIT 20

Trending Items​

Retrieve trending items ordered by popularity metrics:

SELECT * 
FROM retrieve(column_order(columns='views DESC, likes DESC, created_at DESC', limit=100))
WHERE created_at > '2024-12-01'
LIMIT 20


Use a date parameter for dynamic filtering:

SELECT * 
FROM retrieve(column_order(columns='views DESC, likes DESC, created_at DESC', limit=100))
WHERE created_at > $start_date
LIMIT 20

Reranking​

Rerank a set of candidate items with diversity:

SELECT score(expression='m1', input_user_id='$user_id') AS s,
       diversity(score=s, strength=0.4) AS d,
       exploration(score=s, strength=0.2) AS e, *
FROM retrieve(ids($item_ids)) ORDER BY e LIMIT 10

Hybrid Search​

Combine similarity and text search for better recall:

SELECT * 
FROM retrieve(
    similarity(embedding_ref='als', limit=50),
    text_search(query='$query', mode='lexical', limit=50)
)
WHERE category = '$category'
LIMIT 20

User-to-User Recommendations​

Find similar users:

SELECT * 
FROM retrieve(similarity(embedding_ref='user_embedding', 
                         encoder='precomputed_user',
                         input_user_id='$user_id',
                         entity_type='users',
                         limit=50))
LIMIT 10

Troubleshooting​
Common Errors​

"Unknown retriever function: 'similiarity'"

Unknown retriever function: 'similiarity'. 
Supported: candidate_attributes, column_order, filter, ids, similarity, text_search
Did you mean: similarity?

Check function name spelling (case-insensitive)
The error message includes suggestions for similar function names

"All retrievers must use the same entity_type"

All retrievers must use the same entity_type. Found: items and users

Ensure all retriever functions in your query use the same entity_type parameter
Remove conflicting entity_type specifications

"Parameter 'limit' exceeds maximum"

Parameter 'limit' exceeds maximum allowed value of 1000. Got: 5000

The LIMIT value must be ≤ 1000
Reduce the LIMIT value or use pagination for larger result sets

"'limit' is a reserved keyword"

Failed to parse SQL: 'limit' is a reserved keyword and cannot be used as a 
parameter name. Use 'max_results' instead.

Don't use limit as a parameter name
Use max_results, result_limit, or similar instead

"JOINs are not supported"

JOINs are not supported. Use retriever functions to combine data sources:
FROM retrieve(similarity(...), text_search(...), ...).

Use multiple retriever functions in the FROM clause instead of JOINs

"Subqueries in FROM clause are not supported"

Subqueries in FROM clause are not supported. Use retriever functions instead

Replace subqueries with retriever functions

"GROUP BY and aggregations are not supported"

GROUP BY and aggregations are not supported. This DSL is designed for ranking 
queries, not analytical queries.

This query language is for recommendations/ranking, not analytics
Use a data warehouse or OLAP system for analytical queries

"Nested function calls are not supported"

Nested function calls are not supported. 
Example: similarity(embedding_ref=func('arg')) is invalid.
Use simple values: similarity(embedding_ref='als')

Don't nest functions within function arguments
Use parameters for dynamic values instead

"Missing required parameter: 'input_user_id'"

Missing required field: 'parameters.user_id'. Please include this field in 
your request.

Provide all required parameters in the request
Check saved query parameter schemas for required fields

"Embedding 'als2' referenced in retriever is not defined"

Embedding 'als2' not found in model configuration

Verify the embedding name exists in your model configuration
Check for typos in the embedding_ref parameter
Query Performance Issues​

Slow queries:

Reduce retriever limit values
Add filters earlier in the pipeline (in retriever where or WHERE clause)
Use truncate() to limit candidate sets before scoring
Check if multiple retrievers can be optimized or combined

Low recall:

Increase retriever limit values
Use multiple retrievers to combine different retrieval strategies
Adjust diversity/exploration strength (lower values improve relevance)

Inconsistent results:

Ensure parameters are provided consistently
Use pagination keys for consistent pagination
Check for non-deterministic operations (some reorder functions may have slight variations)
Error Handling​

The query language provides helpful error messages for common issues:

Unknown retriever functions: Includes suggestions for similar function names
Invalid parameter syntax: Explains correct parameter format
Missing required parameters: Lists which parameters are required
Entity type mismatches: Explains entity type conflicts
Invalid function arguments: Describes expected argument types and values
Limit violations: Shows maximum allowed values

All errors include context about where the error occurred in your query to help with debugging.

Error Response Format​

Error responses follow this structure:

{
  "status_code": 422,
  "message": "Invalid query configuration: similarity() requires a non-empty 'embedding_ref'",
  "data": null
}


Common Error Messages:

"SQL query cannot be empty" - Query string is empty or whitespace
"Unknown retriever function: 'X'" - Function name not recognized
"All retrievers must use the same entity_type" - Entity type conflict
"Parameter 'limit' exceeds maximum" - LIMIT value too large
"Failed to transpile SQL query: ..." - SQL syntax error
"Saved query 'X' not found" - Saved query doesn't exist
"Missing required field: 'X'" - Required request field missing
Quick Reference​
Retriever Functions​

Use inside FROM retrieve(...). Example: FROM retrieve(similarity(...), text_search(...)).

Function	Purpose	Key Parameters
similarity()	Vector similarity search	embedding_ref, encoder, limit
text_search()	Full-text search	query, mode, limit
column_order()	Order by column values	columns, limit
filter()	Filter-based retrieval	where, limit
ids()	Retrieve by IDs (reranking)	item_ids (list or parameter)
candidate_attributes()	Rerank from attributes	Parameter reference
Query Encoders​
Encoder	Use Case	Key Parameters
precomputed_user (default)	User-based recommendations	input_user_id
precomputed_item	Item-to-item similarity	input_item_id
interaction_pooling (default)	Pool user interactions	input_user_id, truncate_interactions
interaction_round_robin	Round-robin from interactions	input_user_id, num_clusters
user_attribute_pooling	Encode user attributes	input_user_id, input_user_features
item_attribute_pooling	Encode item attributes	input_item_id, input_item_features
Filter Functions​
Function	Purpose	Parameters
prebuilt()	Apply prebuilt filter	filter_ref, input_user_id
truncate()	Limit candidate set	max_length
Reorder Functions​

Use in SELECT with an alias, then ORDER BY alias. Each takes a score alias when ordering by a reranker (e.g. diversity(score=s, strength=0.3) AS r).

Function	Purpose	Key Parameters
diversity()	Reduce similarity	score (alias), strength (0.0-1.0)
exploration()	Inject items with equal weight	score, retriever, strength
boosted()	Inject items by boost column	score, retriever, strength
Common Parameters​
$user_id - User identifier (string)
$item_id - Item identifier (string)
$query - Search query text (string)
$item_ids - List of item IDs (array of strings)
$item_attributes - Item attributes dictionary (object/array)
$limit - Result limit (integer) - Note: use LIMIT clause when possible

Array Parameters Example:

{
  "parameters": {
    "item_ids": ["item1", "item2", "item3"]
  }
}

Limits​
Engine queries: Maximum LIMIT 1000. Global data queries: maximum LIMIT 10,000 (and LIMIT is required).
Maximum string length: 1000 characters for parameters/values.
SQL Operators​
Comparison: =, !=, >, <, >=, <=
Logical: AND, OR, NOT
String: LIKE, ILIKE
Null: IS NULL, IS NOT NULL
Membership: IN (...), NOT IN (...)
Range: BETWEEN ... AND ...

See also: Query endpoints (global vs per-engine), API Usage (endpoints and saved queries).

Glossary​
Ad-hoc Query: A query sent directly in the API request
Candidate: An entity retrieved by a retriever function
Embedding: A vector representation of an entity or query
Encoder: A component that converts user/item input into a query vector
Engine: A deployed model with its configuration (also called model name)
Entity Type: The type of entity being queried (items or users)
Filter: A condition that excludes entities from results
Pagination: Mechanism for retrieving results in pages
Prebuilt Filter: A filter defined in the model configuration
Query Pipeline: The sequence of retrieve → filter → score → reorder → limit operations
Reorder: Post-processing step that modifies result order (diversity, exploration, etc.)
Retriever: A function that retrieves candidate entities from the index
Saved Query: A pre-defined query stored in the model configuration
Score: A relevance score assigned to each entity (0.0 to 1.0)
Transpilation: Converting SQL syntax to query configuration objects
FAQ​

Q: Can I use SQL joins in queries?

No, joins are not supported. Use multiple retriever functions in the FROM clause to combine data from different sources. The retrievers execute in parallel and results are merged.

Q: How do I filter out items a user has already seen?

Define a prebuilt personal filter in your model configuration and use it in your query:

WHERE prebuilt('exclude_seen', input_user_id='$user_id')


Q: Can I use SQL functions in WHERE clauses?

Yes, DataFusion SQL functions are supported. For example: WHERE LENGTH(name) > 10 or WHERE price * 1.1 > 100.

Q: How does ordering work?

Put your scoring expression in SELECT as score(expression='...') AS s and any reranker (e.g. diversity) as diversity(score=s, strength=0.3) AS r. Then use ORDER BY s or ORDER BY r (or another alias). Omit ORDER BY to use the retriever's default score.

Q: How do I debug slow queries?

Use return_explanation=true to see:

How many candidates each retriever found
How long each step took
Which filters removed the most candidates

Q: Can I cache query results?

The platform handles caching automatically. Identical queries with identical parameters within a short time window may return cached results.

Q: What happens if a parameter is missing?

If a required parameter is missing, you'll get a 422 error with details about which parameter is missing. Optional parameters use their default values if not provided.

Q: Can I use this for analytics queries?

No, this DSL is designed for ranking and recommendation queries, not analytical queries. It doesn't support GROUP BY, aggregations, or other analytical operations.

Q: How do I create a saved query?

Add it to your model configuration YAML under queries and deploy. See Defining Saved Queries for details.

Q: What happens if my query returns zero results?

Queries that return zero results are handled gracefully. You'll receive an empty results array with a 200 OK status. The explanation field (if requested) will show how many candidates were found at each stage, helping you debug why no results were returned.

Q: Can I test queries before deploying?

Yes! You can test queries in two ways:

Ad-hoc queries: Use the ad-hoc query endpoint to test SQL syntax and logic before creating saved queries
Console UI: Use the query console in the dashboard to interactively test queries with live data

Q: Are there limits on query complexity?

There are no explicit limits on query complexity (number of retrievers, filters, etc.), but very complex queries may impact performance. Monitor query execution times using return_explanation=true and optimize as needed.

Quick Start
Overview
Mental model
Query endpoints
SQL vs YAML Format
Basic Syntax
Entity Types
Retriever Functions
similarity()
text_search()
column_order()
filter()
ids()
candidate_attributes()
Query Encoders
precomputed_user (default)
precomputed_item
interaction_pooling (default)
interaction_round_robin
user_attribute_pooling
item_attribute_pooling
Filter Functions
prebuilt()
truncate()
Reorder Functions
diversity()
exploration()
boosted()
Parameters
Parameter Syntax
Common Parameters
Parameter Examples
SELECT Clause
WHERE Clause
Supported Operations
Examples
ORDER BY Clause
Value Model Expressions
Available Objects
Available Functions
Operators
Model References
Policy Features
Expression Evaluation
Value Model Examples
Common Value Model Patterns
LIMIT Clause
Complete Examples
Basic Similarity Search
Text Search with Filtering
User Search
Reranking with Diversity
Complex Query with Multiple Filters
Column Ordering
Query Patterns and Recipes
Pattern: Cold Start Recommendations
Pattern: Multi-Stage Retrieval
Pattern: Time-Based Filtering
Pattern: A/B Testing Queries
Pattern: Category-Specific Recommendations
Unsupported Features
Limits and Constraints
Result Limits
String Length Limits
Performance Considerations
Pagination
Configuration
Usage
Parameters
API Usage
Endpoints
Authentication
Making Query Requests
Defining Saved Queries
Response Format
Best Practices
Query Design
Performance Tips
Security Considerations
When to Use Each Retriever
Common Use Cases
Personalized Recommendations
Search with Filters
Trending Items
Reranking
Hybrid Search
User-to-User Recommendations
Troubleshooting
Common Errors
Query Performance Issues
Error Handling
Error Response Format
Quick Reference
Retriever Functions
Query Encoders
Filter Functions
Reorder Functions
Common Parameters
Limits
SQL Operators
Glossary
FAQ
