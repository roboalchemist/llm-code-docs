# Lancedb Documentation

Source: https://docs.lancedb.com/llms-full.txt

---

# Add Columns
Source: https://docs.lancedb.com/api-reference/data/add-columns

api-reference/openapi.yml post /v1/table/{name}/add_columns
Add new columns to a table using SQL expressions that can reference existing columns. You can generate computed columns or add null-filled columns with explicit type casting.



# Delete Data
Source: https://docs.lancedb.com/api-reference/data/delete-data

api-reference/openapi.yml post /v1/table/{name}/delete
Delete rows from a table using a SQL predicate filter. The delete operation permanently removes rows that match the specified filter criteria.



# Drop Columns
Source: https://docs.lancedb.com/api-reference/data/drop-columns

api-reference/openapi.yml post /v1/table/{name}/drop_columns
Remove columns from a table permanently. This operation cannot be undone and will result in the loss of all data in the specified columns.



# Insert Data
Source: https://docs.lancedb.com/api-reference/data/insert-data

api-reference/openapi.yml post /v1/table/{name}/insert
Insert data into a table with support for append and overwrite modes. Data must be provided in Apache Arrow IPC stream format and the schema must be compatible with the existing table schema.



# Merge-Insert (Upsert) Data
Source: https://docs.lancedb.com/api-reference/data/merge-insert-upsert-data

api-reference/openapi.yml post /v1/table/{name}/merge_insert
Perform a merge-insert operation (upsert) on a table by combining insert, update, and delete operations based on matching criteria. This endpoint enables sophisticated data synchronization patterns for keeping tables in sync with external data sources.



# Search Data
Source: https://docs.lancedb.com/api-reference/data/search-data

api-reference/openapi.yml post /v1/table/{name}/query
Perform advanced search queries combining vector search, full-text search, and SQL filtering. This endpoint supports multiple search paradigms including vector similarity search, keyword-based search using BM25, and hybrid search with automatic reranking.



# Update Column Details
Source: https://docs.lancedb.com/api-reference/data/update-column-details

api-reference/openapi.yml post /v1/table/{name}/alter_columns
Alter the name, type, or nullability of existing columns in a table. This operation allows you to modify column properties while preserving data integrity.



# Update Data
Source: https://docs.lancedb.com/api-reference/data/update-data

api-reference/openapi.yml post /v1/table/{name}/update
Update rows in a table using SQL expressions and an optional predicate filter. The update operation modifies existing data based on the specified column updates and filter conditions.



# Create Index
Source: https://docs.lancedb.com/api-reference/index/create-index

api-reference/openapi.yml post /v1/table/{name}/create_index
Create an index on a table column to optimize search performance for vector, scalar, or full-text search operations. Index creation is asynchronous and the type of index should be chosen based on your data characteristics and query patterns.



# Get Index Details
Source: https://docs.lancedb.com/api-reference/index/get-index-details

api-reference/openapi.yml get /v1/table/{name}/index/{index_name}/stats
Get detailed statistics and configuration information for a specific index. This endpoint provides information about indexed rows, index type, and performance metrics for the specified index.



# List Indexes
Source: https://docs.lancedb.com/api-reference/index/list-indexes

api-reference/openapi.yml get /v1/table/{name}/index/list
List all indices associated with a table including their status and configuration details. This endpoint provides information about both vector and scalar indexes that have been created for the table.



# Introduction
Source: https://docs.lancedb.com/api-reference/introduction

API reference for LanceDB Cloud with Python, JavaScript, and Rust SDK examples.

## Introduction

**LanceDB Cloud REST API** allows you to interact with your remote table using standard HTTP requests.

<Tip>[LanceDB Quickstart](https://lancedb.com/documentation/quickstart/) will get you up and running in 5 minutes!</Tip>

Our [documentation site](https://lancedb.com/documentation/) covers SDK examples in Python, Typescript and Rust.

## Authentication

All HTTP requests to LanceDB APIs must contain an <u>x-api-key</u> header that specifies a valid API key and
must be encoded as JSON or Arrow RPC.

### Get the API Key

1. Go to [LanceDB Cloud](https://accounts.lancedb.com/sign-up) and complete the onboarding.

![create](https://mintlify.s3.us-west-1.amazonaws.com/lancedb-bcbb4faf/assets/create.png)

2. Let's call this particular **Project** `embedding`.
3. Save the API key and the project instance name: `embedding-yhs6bg`.

This is how the Project looks in the LanceDB Cloud Dashboard:
![projects](https://mintlify.s3.us-west-1.amazonaws.com/lancedb-bcbb4faf/assets/projects.png)

4. In your terminal, check the existence of the remote **Project**. Specify the remote LanceDB **Project** `db` and `region`.

```shell
curl -X GET "https://{db}.{region}.api.lancedb.com/v1/tables" \
   -H "Content-Type: application/json" \
   -H "x-api-key: LANCEDB_API_KEY"
```

5. Now, create a **Table** to store data. Let's call it `words`.

```shell
curl -X POST "https://embedding-yhs6bg.us-east-1.api.lancedb.com/v1/tables/words" \
   -H "Content-Type: application/vnd.apache.arrow.stream" \
   -H "x-api-key: LANCEDB_API_KEY"
```

* the `db` is `embedding-yhs6bg`
* the `region` is `us-east-1`
* the name of the table is `words`.

6. Now check that the **Table has** been created:

```shell
curl -X GET "https://embedding-yhs6bg.us-east-1.api.lancedb.com/v1/tables" \
   -H "Content-Type: application/json" \
   -H "x-api-key: LANCEDB_API_KEY"
```

You can always check from the LanceDB Cloud Dashboard:

![words](https://mintlify.s3.us-west-1.amazonaws.com/lancedb-bcbb4faf/assets/words.png)

That's it - you're connected! Now, you can start adding data and querying it.
The best way to start is to try the [LanceDB Quickstart](https://lancedb.com/documentation/quickstart/) or read the [documentation site](https://lancedb.com/documentation/).


# SDK Reference
Source: https://docs.lancedb.com/api-reference/sdk-reference

SDK reference for LanceDB Cloud with Python, JavaScript, and Rust SDK examples.

## Supported Libraries:

| SDK Reference                                                                                                        | Description                                                 |
| :------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [Python SDK](https://lancedb.github.io/lancedb/python/python/)                                                       | Full-featured Python client with pandas & numpy integration |
| [Typescript SDK](https://lancedb.github.io/lancedb/js/)                                                              | Modern JavaScript/TypeScript SDK for Node.js and browsers   |
| [Rust SDK](https://docs.rs/lancedb/latest/lancedb/index.html)                                                        | Native Rust implementation for high performance             |
| [Java API Quickstart](https://github.com/lancedb/vectordb-recipes/tree/main/examples/saas_examples/rest_api_example) | Streamline REST API interactions in Java                    |


# Count Table Rows
Source: https://docs.lancedb.com/api-reference/tables/count-table-rows

api-reference/openapi.yml post /v1/table/{name}/count_rows
Count the number of rows in a table with optional filtering. You can pass a SQL predicate to count only the rows that match specific criteria.



# Create Table
Source: https://docs.lancedb.com/api-reference/tables/create-table

api-reference/openapi.yml post /v1/table/{name}/create
Create a new table in the database with schema inferred from the provided Arrow data. The table name must be unique within the database and vector columns are automatically detected and optimized for search operations.

**Example curl command:**
```bash
curl --request POST \
  --url https://{db}.{region}.api.lancedb.com/v1/table/{name}/create \
  --header 'Content-Type: application/vnd.apache.arrow.stream' \
  --header 'x-api-key: <api-key>' \
  --data-binary @data.arrow
```




# Drop Table
Source: https://docs.lancedb.com/api-reference/tables/drop-table

api-reference/openapi.yml post /v1/table/{name}/drop
Drop a table and all its associated data permanently. If the table does not exist, the operation will return 200 without error.



# Get Table Details
Source: https://docs.lancedb.com/api-reference/tables/get-table-details

api-reference/openapi.yml post /v1/table/{name}/describe
Get detailed information about a table including schema, statistics, and metadata. This endpoint provides comprehensive table information useful for understanding table structure, monitoring performance metrics, and planning data operations.




# List Tables
Source: https://docs.lancedb.com/api-reference/tables/list-tables

api-reference/openapi.yml get /v1/table
List all tables in the database with optional pagination support. Returns a paginated list of table names with configurable limits and page tokens for efficient navigation through large result sets.




# Rename Table
Source: https://docs.lancedb.com/api-reference/tables/rename-table

api-reference/openapi.yml post /v1/table/{name}/rename
Rename a table to a new name. The new table name must be unique within the database and cannot conflict with existing table names.



