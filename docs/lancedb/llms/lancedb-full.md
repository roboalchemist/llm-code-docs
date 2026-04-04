# Lancedb Documentation

Source: https://docs.lancedb.com/llms-full.txt

---

# Client SDKs
Source: https://docs.lancedb.com/api-reference/index

SDK & REST API reference for LanceDB

For detailed information of the available functions and methods in your preferred language's SDKs,
refer to the API documentation linked below.

If you're looking for a REST API reference, visit the [REST API](/api-reference/rest) page.

## Supported SDKs

Python, Typescript and Rust SDKs are officially supported by LanceDB.

| SDK Reference                                                  | Description                                                        |
| :------------------------------------------------------------- | ------------------------------------------------------------------ |
| [Python SDK](https://lancedb.github.io/lancedb/python/python/) | Full-featured Python client with pandas & numpy integration        |
| [Typescript SDK](https://lancedb.github.io/lancedb/js/)        | A TypeScript wrapper around the Rust library, built with `napi-rs` |
| [Rust SDK](https://docs.rs/lancedb/latest/lancedb/index.html)  | Native Rust library with persistent-storage and high performance   |

## Examples in other languages

Other language SDKs are available through examples or third-party contributions.

| SDK Examples                                                                                                         | Description                              |
| :------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [Java API Quickstart](https://github.com/lancedb/vectordb-recipes/tree/main/examples/saas_examples/rest_api_example) | Streamline REST API interactions in Java |


# REST API Reference
Source: https://docs.lancedb.com/api-reference/rest/index

API reference for LanceDB

[Lance REST Namespace](https://lance.org/format/namespace/rest/catalog-spec/?h=rest) spec
is an OpenAPI protocol that enables reading, writing and managing Lance tables by connecting
those metadata services or building a custom metadata server in a standardized way.

LanceDB OSS allows you to interface with Lance tables via the REST Namespace.
However, LanceDB's Cloud and Enterprise products provide an extended REST API with
additional endpoints for managing projects, tables, and data.
If you have specific needs or questions about the Enterprise/Cloud REST API Namespace,
please [contact us](mailto:support@lancedb.com).

## Authentication

<Badge>Cloud</Badge>
<Badge>Enterprise</Badge>

All HTTP requests to LanceDB APIs must contain an <u>x-api-key</u> header that specifies a valid API key and
must be encoded as JSON or Arrow RPC.

The tutorial below demonstrates how to connect to LanceDB Cloud using the REST API.

### Get the API Key

1. Go to [LanceDB Cloud](https://accounts.lancedb.com/sign-up) and complete the onboarding.

<img alt="create" />

2. Let's call this particular **Project** `embedding`.
3. Save the API key and the project instance name: `embedding-yhs6bg`.

This is how the Project looks in the LanceDB Cloud Dashboard:

<img alt="projects" />

4. In your terminal, check the existence of the remote **Project**. Specify the remote LanceDB **Project** `db` and `region`.

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
curl -X GET "https://{db}.{region}.api.lancedb.com/v1/tables" \
   -H "Content-Type: application/json" \
   -H "x-api-key: LANCEDB_API_KEY"
```

5. Now, create a **Table** to store data. Let's call it `words`.

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
curl -X POST "https://embedding-yhs6bg.us-east-1.api.lancedb.com/v1/tables/words" \
   -H "Content-Type: application/vnd.apache.arrow.stream" \
   -H "x-api-key: LANCEDB_API_KEY"
```

* the `db` is `embedding-yhs6bg`
* the `region` is `us-east-1`
* the name of the table is `words`.

6. Now check that the **Table has** been created:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
curl -X GET "https://embedding-yhs6bg.us-east-1.api.lancedb.com/v1/tables" \
   -H "Content-Type: application/json" \
   -H "x-api-key: LANCEDB_API_KEY"
```

You can always check from the LanceDB Cloud Dashboard:

<img alt="words" />

That's it -- you're connected! Now, you can start adding data and querying it.
You can visit the tutorial section to build your own applications with LanceDB.

<Card title="Tutorials" icon="book" href="/tutorials/">
  Check out our tutorials on building various applications with LanceDB.
</Card>


# Check if a namespace exists
Source: https://docs.lancedb.com/api-reference/rest/namespace/check-if-a-namespace-exists

api-reference/rest/openapi.yml post /v1/namespace/{id}/exists
Check if namespace `id` exists.

This operation must behave exactly like the DescribeNamespace API, 
except it does not contain a response body.




# Create a new namespace
Source: https://docs.lancedb.com/api-reference/rest/namespace/create-a-new-namespace

api-reference/rest/openapi.yml post /v1/namespace/{id}/create
Create new namespace `id`.

During the creation process, the implementation may modify user-provided `properties`, 
such as adding additional properties like `created_at` to user-provided properties, 
omitting any specific property, or performing actions based on any property value.




# Describe a namespace
Source: https://docs.lancedb.com/api-reference/rest/namespace/describe-a-namespace

api-reference/rest/openapi.yml post /v1/namespace/{id}/describe
Describe the detailed information for namespace `id`.




# Drop a namespace
Source: https://docs.lancedb.com/api-reference/rest/namespace/drop-a-namespace

api-reference/rest/openapi.yml post /v1/namespace/{id}/drop
Drop namespace `id` from its parent namespace.




# List namespaces
Source: https://docs.lancedb.com/api-reference/rest/namespace/list-namespaces

api-reference/rest/openapi.yml get /v1/namespace/{id}/list
List all child namespace names of the parent namespace `id`.

REST NAMESPACE ONLY
REST namespace uses GET to perform this operation without a request body.
It passes in the `ListNamespacesRequest` information in the following way:
- `id`: pass through path parameter of the same name
- `page_token`: pass through query parameter of the same name
- `limit`: pass through query parameter of the same name




# List tables in a namespace
Source: https://docs.lancedb.com/api-reference/rest/namespace/list-tables-in-a-namespace

api-reference/rest/openapi.yml get /v1/namespace/{id}/table/list
List all child table names of the parent namespace `id`.

REST NAMESPACE ONLY
REST namespace uses GET to perform this operation without a request body.
It passes in the `ListTablesRequest` information in the following way:
- `id`: pass through path parameter of the same name
- `page_token`: pass through query parameter of the same name
- `limit`: pass through query parameter of the same name




# Add new columns to table schema
Source: https://docs.lancedb.com/api-reference/rest/table/add-new-columns-to-table-schema

api-reference/rest/openapi.yml post /v1/table/{id}/add_columns
Add new columns to table `id` using SQL expressions or default values.




# Analyze query execution plan
Source: https://docs.lancedb.com/api-reference/rest/table/analyze-query-execution-plan

api-reference/rest/openapi.yml post /v1/table/{id}/analyze_plan
Analyze the query execution plan for a query against table `id`.
Returns detailed statistics and analysis of the query execution plan.

REST NAMESPACE ONLY
REST namespace returns the response as a plain string
instead of the `AnalyzeTableQueryPlanResponse` JSON object.




# Check if a table exists
Source: https://docs.lancedb.com/api-reference/rest/table/check-if-a-table-exists

api-reference/rest/openapi.yml post /v1/table/{id}/exists
Check if table `id` exists.

This operation should behave exactly like DescribeTable, 
except it does not contain a response body.

For DirectoryNamespace implementation, a table exists if either:
- The table has Lance data versions (regular table created with CreateTable)
- A `.lance-reserved` file exists in the table directory (declared table created with DeclareTable)




# Count rows in a table
Source: https://docs.lancedb.com/api-reference/rest/table/count-rows-in-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/count_rows
Count the number of rows in table `id`

REST NAMESPACE ONLY
REST namespace returns the response as a plain integer
instead of the `CountTableRowsResponse` JSON object.




# Create a new tag
Source: https://docs.lancedb.com/api-reference/rest/table/create-a-new-tag

api-reference/rest/openapi.yml post /v1/table/{id}/tags/create
Create a new tag for table `id` that points to a specific version.




# Create a scalar index on a table
Source: https://docs.lancedb.com/api-reference/rest/table/create-a-scalar-index-on-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/create_scalar_index
Create a scalar index on a table column for faster filtering operations.
Supports scalar indexes (BTREE, BITMAP, LABEL_LIST, FTS, etc.).
This is an alias for CreateTableIndex specifically for scalar indexes.
Index creation is handled asynchronously.
Use the `ListTableIndices` and `DescribeTableIndexStats` operations to monitor index creation progress.




# Create a table with the given name
Source: https://docs.lancedb.com/api-reference/rest/table/create-a-table-with-the-given-name

api-reference/rest/openapi.yml post /v1/table/{id}/create
Create table `id` in the namespace with the given data in Arrow IPC stream.

The schema of the Arrow IPC stream is used as the table schema.
If the stream is empty, the API creates a new empty table.

REST NAMESPACE ONLY
REST namespace uses Arrow IPC stream as the request body.
It passes in the `CreateTableRequest` information in the following way:
- `id`: pass through path parameter of the same name
- `mode`: pass through query parameter of the same name




# Create an empty table
Source: https://docs.lancedb.com/api-reference/rest/table/create-an-empty-table

api-reference/rest/openapi.yml post /v1/table/{id}/create-empty
Create an empty table with the given name without touching storage.
This is a metadata-only operation that records the table existence and sets up aspects like access control.

For DirectoryNamespace implementation, this creates a `.lance-reserved` file in the table directory
to mark the table's existence without creating actual Lance data files.

**Deprecated**: Use `DeclareTable` instead.




# Create an index on a table
Source: https://docs.lancedb.com/api-reference/rest/table/create-an-index-on-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/create_index
Create an index on a table column for faster search operations.
Supports vector indexes (IVF_FLAT, IVF_HNSW_SQ, IVF_PQ, etc.) and scalar indexes (BTREE, BITMAP, FTS, etc.).
Index creation is handled asynchronously. 
Use the `ListTableIndices` and `DescribeTableIndexStats` operations to monitor index creation progress.




# Declare a table
Source: https://docs.lancedb.com/api-reference/rest/table/declare-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/declare
Declare a table with the given name without touching storage.
This is a metadata-only operation that records the table existence and sets up aspects like access control.

For DirectoryNamespace implementation, this creates a `.lance-reserved` file in the table directory
to mark the table's existence without creating actual Lance data files.




# Delete a tag
Source: https://docs.lancedb.com/api-reference/rest/table/delete-a-tag

api-reference/rest/openapi.yml post /v1/table/{id}/tags/delete
Delete an existing tag from table `id`.




# Delete rows from a table
Source: https://docs.lancedb.com/api-reference/rest/table/delete-rows-from-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/delete
Delete rows from table `id`.




# Deregister a table
Source: https://docs.lancedb.com/api-reference/rest/table/deregister-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/deregister
Deregister table `id` from its namespace.




# Describe information of a table
Source: https://docs.lancedb.com/api-reference/rest/table/describe-information-of-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/describe
Describe the detailed information for table `id`.

REST NAMESPACE ONLY
REST namespace passes `with_table_uri` and `load_detailed_metadata` as query parameters instead of in the request body.




# Drop a specific index
Source: https://docs.lancedb.com/api-reference/rest/table/drop-a-specific-index

api-reference/rest/openapi.yml post /v1/table/{id}/index/{index_name}/drop
Drop the specified index from table `id`.

REST NAMESPACE ONLY
REST namespace does not use a request body for this operation.
The `DropTableIndexRequest` information is passed in the following way:
- `id`: pass through path parameter of the same name
- `index_name`: pass through path parameter of the same name




# Drop a table
Source: https://docs.lancedb.com/api-reference/rest/table/drop-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/drop
Drop table `id` and delete its data.

REST NAMESPACE ONLY
REST namespace does not use a request body for this operation.
The `DropTableRequest` information is passed in the following way:
- `id`: pass through path parameter of the same name




# Get query execution plan explanation
Source: https://docs.lancedb.com/api-reference/rest/table/get-query-execution-plan-explanation

api-reference/rest/openapi.yml post /v1/table/{id}/explain_plan
Get the query execution plan for a query against table `id`.
Returns a human-readable explanation of how the query will be executed.

REST NAMESPACE ONLY
REST namespace returns the response as a plain string
instead of the `ExplainTableQueryPlanResponse` JSON object.




# Get table index statistics
Source: https://docs.lancedb.com/api-reference/rest/table/get-table-index-statistics

api-reference/rest/openapi.yml post /v1/table/{id}/index/{index_name}/stats
Get statistics for a specific index on a table. Returns information about
the index type, distance type (for vector indices), and row counts.




# Get table statistics
Source: https://docs.lancedb.com/api-reference/rest/table/get-table-statistics

api-reference/rest/openapi.yml post /v1/table/{id}/stats
Get statistics for table `id`, including row counts, data sizes, and column statistics.




# Get version for a specific tag
Source: https://docs.lancedb.com/api-reference/rest/table/get-version-for-a-specific-tag

api-reference/rest/openapi.yml post /v1/table/{id}/tags/version
Get the version number that a specific tag points to for table `id`.




# Insert records into a table
Source: https://docs.lancedb.com/api-reference/rest/table/insert-records-into-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/insert
Insert new records into table `id`.

REST NAMESPACE ONLY
REST namespace uses Arrow IPC stream as the request body.
It passes in the `InsertIntoTableRequest` information in the following way:
- `id`: pass through path parameter of the same name
- `mode`: pass through query parameter of the same name




# List all tables
Source: https://docs.lancedb.com/api-reference/rest/table/list-all-tables

api-reference/rest/openapi.yml get /v1/table
List all tables across all namespaces.

REST NAMESPACE ONLY
REST namespace uses GET to perform this operation without a request body.
It passes in the `ListAllTablesRequest` information in the following way:
- `page_token`: pass through query parameter of the same name
- `limit`: pass through query parameter of the same name
- `delimiter`: pass through query parameter of the same name




# List all tags for a table
Source: https://docs.lancedb.com/api-reference/rest/table/list-all-tags-for-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/tags/list
List all tags that have been created for table `id`.
Returns a map of tag names to their corresponding version numbers and metadata.

REST NAMESPACE ONLY
REST namespace does not use a request body for this operation.
The `ListTableTagsRequest` information is passed in the following way:
- `id`: pass through path parameter of the same name
- `page_token`: pass through query parameter of the same name
- `limit`: pass through query parameter of the same name




# List all versions of a table
Source: https://docs.lancedb.com/api-reference/rest/table/list-all-versions-of-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/version/list
List all versions (commits) of table `id` with their metadata.

REST NAMESPACE ONLY
REST namespace does not use a request body for this operation.
The `ListTableVersionsRequest` information is passed in the following way:
- `id`: pass through path parameter of the same name
- `page_token`: pass through query parameter of the same name
- `limit`: pass through query parameter of the same name




# List indexes on a table
Source: https://docs.lancedb.com/api-reference/rest/table/list-indexes-on-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/index/list
List all indices created on a table. Returns information about each index
including name, columns, status, and UUID.




# Merge insert (upsert) records into a table
Source: https://docs.lancedb.com/api-reference/rest/table/merge-insert-upsert-records-into-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/merge_insert
Performs a merge insert (upsert) operation on table `id`.
This operation updates existing rows
based on a matching column and inserts new rows that don't match.
It returns the number of rows inserted and updated.

REST NAMESPACE ONLY
REST namespace uses Arrow IPC stream as the request body.
It passes in the `MergeInsertIntoTableRequest` information in the following way:
- `id`: pass through path parameter of the same name
- `on`: pass through query parameter of the same name
- `when_matched_update_all`: pass through query parameter of the same name
- `when_matched_update_all_filt`: pass through query parameter of the same name
- `when_not_matched_insert_all`: pass through query parameter of the same name
- `when_not_matched_by_source_delete`: pass through query parameter of the same name
- `when_not_matched_by_source_delete_filt`: pass through query parameter of the same name




# Modify existing columns
Source: https://docs.lancedb.com/api-reference/rest/table/modify-existing-columns

api-reference/rest/openapi.yml post /v1/table/{id}/alter_columns
Modify existing columns in table `id`, such as renaming or changing data types.




# Query a table
Source: https://docs.lancedb.com/api-reference/rest/table/query-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/query
Query table `id` with vector search, full text search and optional SQL filtering.
Returns results in Arrow IPC file or stream format.

REST NAMESPACE ONLY
REST namespace returns the response as Arrow IPC file binary data
instead of the `QueryTableResponse` JSON object.




# Register a table to a namespace
Source: https://docs.lancedb.com/api-reference/rest/table/register-a-table-to-a-namespace

api-reference/rest/openapi.yml post /v1/table/{id}/register
Register an existing table at a given storage location as `id`.




# Remove columns from table
Source: https://docs.lancedb.com/api-reference/rest/table/remove-columns-from-table

api-reference/rest/openapi.yml post /v1/table/{id}/drop_columns
Remove specified columns from table `id`.




# Rename a table
Source: https://docs.lancedb.com/api-reference/rest/table/rename-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/rename
Rename table `id` to a new name.




# Restore table to a specific version
Source: https://docs.lancedb.com/api-reference/rest/table/restore-table-to-a-specific-version

api-reference/rest/openapi.yml post /v1/table/{id}/restore
Restore table `id` to a specific version.




# Update a tag to point to a different version
Source: https://docs.lancedb.com/api-reference/rest/table/update-a-tag-to-point-to-a-different-version

api-reference/rest/openapi.yml post /v1/table/{id}/tags/update
Update an existing tag for table `id` to point to a different version.




# Update rows in a table
Source: https://docs.lancedb.com/api-reference/rest/table/update-rows-in-a-table

api-reference/rest/openapi.yml post /v1/table/{id}/update
Update existing rows in table `id`.




# Update table schema metadata
Source: https://docs.lancedb.com/api-reference/rest/table/update-table-schema-metadata

api-reference/rest/openapi.yml post /v1/table/{id}/schema_metadata/update
Replace the schema metadata for table `id` with the provided key-value pairs.

REST NAMESPACE ONLY
REST namespace uses a direct object (map of string to string) as both request and response body
instead of the wrapped `UpdateTableSchemaMetadataRequest` and `UpdateTableSchemaMetadataResponse`.




# Alter information of a transaction.
Source: https://docs.lancedb.com/api-reference/rest/transaction/alter-information-of-a-transaction

api-reference/rest/openapi.yml post /v1/transaction/{id}/alter
Alter a transaction with a list of actions such as setting status or properties.
The server should either succeed and apply all actions, or fail and apply no action.




# Describe information about a transaction
Source: https://docs.lancedb.com/api-reference/rest/transaction/describe-information-about-a-transaction

api-reference/rest/openapi.yml post /v1/transaction/{id}/describe
Return a detailed information for a given transaction




# Get started with LanceDB Cloud
Source: https://docs.lancedb.com/cloud/get-started

Learn how to ingest data into LanceDB Cloud and run search, in just a few minutes.

In this tutorial, you'll ingest a dataset from Huggingface into your [LanceDB Cloud](/cloud/) table,
connect to a remote LanceDB cluster and run some search queries.

For interactive code, check out the [Python notebook](https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/saas_examples/python_notebook/LanceDB_Cloud_quickstart.ipynb)  or the [TypeScript
example](https://github.com/lancedb/vectordb-recipes/tree/main/examples/saas_examples/ts_example/quickstart)

## Getting started

1. Sign up for LanceDB Cloud [by clicking here](https://accounts.lancedb.com/sign-up).
2. Follow [this tutorial](https://app.storylane.io/share/pudefwx54tun) to create a LanceDB Cloud project.

## 1. Installation

<CodeGroup>
  ```bash Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  pip install lancedb datasets
  ```

  ```bash TypeScript icon=js theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  npm install @lancedb/lancedb
  ```
</CodeGroup>

## 2. Connect to LanceDB

* For [LanceDB Cloud](/cloud/) users, the database URI (which starts with `db://`) and API key can both be retrieved from the LanceDB Cloud UI.
* For [LanceDB Enterprise](/enterprise/) users, please [contact us](mailto:contact@lancedb.com) to obtain your database URI, API key, and `host_override` URL.

<CodeGroup>
  ```py Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  import numpy as np
  import pyarrow as pa
  import os

  # Connect to LanceDB Cloud/Enterprise
  uri = "db://your-database-uri"
  api_key = "your-api-key"
  region = "us-east-1"

  # (Optional) For LanceDB Enterprise, set the host override to your enterprise endpoint
  host_override = os.environ.get("LANCEDB_HOST_OVERRIDE")

  db = lancedb.connect(
      uri=uri,
      api_key=api_key,
      region=region,
      host_override=host_override
  )
  ```

  ```ts TypeScript icon=js expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import { connect, Index, Table } from '@lancedb/lancedb';
  import { FixedSizeList, Field, Float32, Schema, Utf8 } from 'apache-arrow';

  // Connect to LanceDB Cloud/Enterprise
  const dbUri = process.env.LANCEDB_URI || 'db://your-database-uri';
  const apiKey = process.env.LANCEDB_API_KEY;
  const region = process.env.LANCEDB_REGION;

  // (Optional) For LanceDB Enterprise, set the host override to your enterprise endpoint
  const hostOverride = process.env.LANCEDB_HOST_OVERRIDE;

  const db = await connect(dbUri, {
      apiKey,
      region,
      hostOverride
  });
  ```
</CodeGroup>

## 3. Load Dataset

For large datasets, the operation should be performed in batches to optimize memory usage.
Let's see how it looks when we try to load a larger dataset.

<CodeGroup>
  ```py Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from datasets import load_dataset

  # Load a sample dataset from HuggingFace with pre-computed embeddings
  sample_dataset = load_dataset("sunhaozhepy/ag_news_sbert_keywords_embeddings", split="test[:1000]")
  print(f"Loaded {len(sample_dataset)} samples")
  print(f"Sample features: {sample_dataset.features}")
  print(f"Column names: {sample_dataset.column_names}")

  # Preview the first sample
  print(sample_dataset[0])

  # Get embedding dimension
  vector_dim = len(sample_dataset[0]["keywords_embeddings"])
  print(f"Embedding dimension: {vector_dim}")
  ```

  ```ts TypeScript icon=js expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const BATCH_SIZE = 100; // HF API default limit
  const POLL_INTERVAL = 10000; // 10 seconds
  const MAX_RETRIES = 5;
  const INITIAL_RETRY_DELAY = 1000; // 1 second

  interface Document {
      text: string;
      label: number;
      keywords: string[];
      embeddings?: number[];
      [key: string]: unknown;
  }

  interface HfDatasetResponse {
      rows: {
          row: {
              text: string;
              label: number;
              keywords: string[];
              keywords_embeddings?: number[];
          };
      }[];
  }

  /**
   * Loads documents from the Hugging Face dataset API in batches
   */
  async function loadDataset(datasetName: string, split: string = 'train', targetSize: number = 1000, offset: number = 0): Promise<Document[]> {    
      try {
          console.log('Fetching dataset...');
          const batches = Math.ceil(targetSize / BATCH_SIZE);
          let allDocuments: Document[] = [];
          const hfToken = process.env.HF_TOKEN; // Optional Hugging Face token

          for (let i = 0; i < batches; i++) {
              const offset = i * BATCH_SIZE;
              const url = `https://datasets-server.huggingface.co/rows?dataset=${datasetName}&config=default&split=${split}&offset=${offset}&limit=${BATCH_SIZE}`;
              console.log(`Fetching batch ${i + 1}/${batches} from offset ${offset}...`);
              
              // Add retry logic with exponential backoff
              let retries = 0;
              let success = false;
              let data: HfDatasetResponse | null = null;

              while (!success && retries < MAX_RETRIES) {
                  try {
                      const headers: HeadersInit = {
                          'Content-Type': 'application/json',
                      };
                      
                      // Add authorization header if token is available
                      if (hfToken) {
                          headers['Authorization'] = `Bearer ${hfToken}`;
                      }
                      
                      const fetchOptions = {
                          method: 'GET',
                          headers,
                          timeout: 30000, // 30 second timeout
                      };
                      
                      const response = await fetch(url, fetchOptions);
                      if (!response.ok) {
                          const errorText = await response.text();
                          console.error(`Error response (attempt ${retries + 1}):`, errorText);
                          throw new Error(`HTTP error! status: ${response.status}, body: ${errorText}`);
                      }
                      
                      data = JSON.parse(await response.text()) as HfDatasetResponse;
                      if (!data.rows) {
                          throw new Error('No rows found in response');
                      }
                      
                      success = true;
                  } catch (error) {
                      retries++;
                      if (retries >= MAX_RETRIES) {
                          console.error(`Failed after ${MAX_RETRIES} retries:`, error);
                          throw error;
                      }
                      
                      const delay = INITIAL_RETRY_DELAY * Math.pow(2, retries - 1);
                      console.log(`Retry ${retries}/${MAX_RETRIES} after ${delay}ms...`);
                      await new Promise(resolve => setTimeout(resolve, delay));
                  }
              }
              
              // Ensure data is defined before using it
              if (!data || !data.rows) {
                  throw new Error('No data received after retries');
              }
              
              console.log(`Received ${data.rows.length} rows in batch ${i + 1}`);
              const documents = data.rows.map(({ row }) => ({
                  text: row.text,
                  label: row.label,
                  keywords: row.keywords,
                  embeddings: row.keywords_embeddings
              }));
              allDocuments = allDocuments.concat(documents);
              
              if (data.rows.length < BATCH_SIZE) {
                  console.log('Reached end of dataset');
                  break;
              }
          }

          console.log(`Total documents loaded: ${allDocuments.length}`);
          return allDocuments;
      } catch (error) {
          console.error("Failed to load dataset:", error);
          throw error;
      }
  }

  // Load dataset
  console.log('Loading AG News dataset...');
  const datasetName = "sunhaozhepy/ag_news_sbert_keywords_embeddings";
  const split = "test";
  const targetSize = 1000;
  const sampleData = await loadDataset(datasetName, split, targetSize);
  console.log(`Loaded ${sampleData.length} examples from AG News dataset`);
  ```
</CodeGroup>

## 4. Ingest Data

<CodeGroup>
  ```py Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import pyarrow as pa

  # Create a table with the dataset
  table_name = "lancedb-cloud-quickstart"
  table = db.create_table(table_name, data=sample_dataset, mode="overwrite")

  # Convert list to fixedsizelist on the vector column
  table.alter_columns(dict(path="keywords_embeddings", data_type=pa.list_(pa.float32(), vector_dim)))
  print(f"Table '{table_name}' created successfully")
  ```

  ```ts TypeScript icon=js expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const tableName = "lancedb-cloud-quickstart";

  const dataWithEmbeddings: Document[] = sampleData;
  const firstDocWithEmbedding = dataWithEmbeddings.find((doc: Document) => 
      (doc.embeddings && Array.isArray(doc.embeddings) && doc.embeddings.length > 0));
      
  if (!firstDocWithEmbedding || !firstDocWithEmbedding.embeddings || !Array.isArray(firstDocWithEmbedding.embeddings)) {
      throw new Error('No document with valid embeddings found in the dataset. Please check if keywords_embeddings field exists.');
  }
  const embeddingDimension = firstDocWithEmbedding.embeddings.length;

  // Create schema
  const schema = new Schema([
      new Field('text', new Utf8(), true),
      new Field('label', new Float32(), true),
      new Field('keywords', new Utf8(), true),
      new Field('embeddings', new FixedSizeList(embeddingDimension, new Field('item', new Float32(), true)), true)
  ]);

  // Create table with data
  const table = await db.createTable(tableName, dataWithEmbeddings, { 
      schema,
      mode: "overwrite" 
  });
  console.log('Successfully created table');
  ```
</CodeGroup>

## 5. Build an Index

After creating a table with vector data, you'll want to create an index to enable fast similarity searches. The index creation process optimizes the data structure for efficient vector similarity lookups, significantly improving query performance for large datasets.

<Check>
  Unlike in LanceDB OSS, the `create_index`/`createIndex` operation executes **asynchronously** in LanceDB Cloud/Enterprise. To ensure the index is fully built, you can use the `wait_timeout` parameter or call `wait_for_index` on the table.
</Check>

<CodeGroup>
  ```py Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from datetime import timedelta

  # Create a vector index and wait for it to complete
  table.create_index("cosine", vector_column_name="keywords_embeddings", wait_timeout=timedelta(seconds=120))
  print(table.index_stats("keywords_embeddings_idx"))
  ```

  ```ts TypeScript icon=js expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Create a vector index
  await table.createIndex("embeddings", {
  config: Index.ivfPq({
      distanceType: "cosine",
  }),
  });

  // Wait for the index to be ready
  const indexName = "embeddings_idx";
  await table.waitForIndex([indexName], 120);
  console.log(await table.indexStats(indexName));
  ```
</CodeGroup>

## 6. Vector Search

Once you have created and indexed your table, you can perform vector similarity searches.
LanceDB provides a flexible search API that allows you to find similar vectors, apply filters, and select specific columns to return. The examples below demonstrate basic vector searches as well as filtered searches that combine vector similarity with traditional SQL-style filtering.

<CodeGroup>
  ```py Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  query_dataset = load_dataset("sunhaozhepy/ag_news_sbert_keywords_embeddings", split="test[5000:5001]")
  print(f"Query keywords: {query_dataset[0]['keywords']}")
  query_embed = query_dataset["keywords_embeddings"][0]

  # A vector search
  result = (
      table.search(query_embed)
      .select(["text", "keywords", "label"])
      .limit(5)
      .to_pandas()
  )
  print("Search results:")
  print(result)
  ```

  ```ts TypeScript icon=js expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Perform semantic search with a new query
  const queryDocs = await loadDataset(datasetName, split, 1, targetSize);
  if (queryDocs.length === 0) {
      throw new Error("Failed to load a query document");
  }
  const queryDoc = queryDocs[0];
  if (!queryDoc.embeddings || !Array.isArray(queryDoc.embeddings)) {
      throw new Error("Query document doesn't have a valid embedding after processing");
  }
  const results = await table.search(queryDoc.embeddings)
      .limit(5)
      .select(['text','keywords','label'])
      .toArray();

  console.log('Search Results:');
  console.log(results);
  ```
</CodeGroup>

## 7. Filtered Search

Add filter to your vector search query. Your can use SQL statements, like `where` for filtering.

<CodeGroup>
  ```py Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  filtered_result = (
      table.search(query_embed)
      .where("label > 2")
      .select(["text", "keywords", "label"])
      .limit(5)
      .to_pandas()
  )
  print("Filtered search results (label > 2):")
  print(filtered_result)
  ```

  ```ts TypeScript icon=js expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const filteredResults = await table.search(queryDoc.embeddings)
      .where("label > 2")
      .limit(5)
      .select(['text', 'keywords','label'])
      .toArray();

  console.log('Search Results with filter:');
  console.log(filteredResults);
  ```
</CodeGroup>

## What's Next?

It's time to use LanceDB Cloud/Enterprise in your own projects!
We've prepared more [tutorials](/tutorials/) for you to continue learning. If you
have any questions, reach out via [Discord](https://discord.gg/AUEWnJ7Txb).


# LanceDB Cloud
Source: https://docs.lancedb.com/cloud/index

Serverless vector search via a managed solution.

LanceDB Cloud is a fully managed, serverless vector search service that enables developers to build, deploy, and
scale AI-powered applications without infrastructure management overhead.

Designed for production workloads, LanceDB Cloud provides cost-effective scaling that adapts to your application
needs. The service is currently in public beta with general availability coming soon.

Access your data through the [LanceDB Cloud UI](https://cloud.lancedb.com/) and benefit from automatic scaling, built-in security,
and enterprise-grade reliability.

<img alt="What is LanceDB?" />

## Key Features

LanceDB Cloud provides the same underlying fast vector database and search engine that powers the OSS version,
but without the need to maintain your own infrastructure. Because it's serverless, you only pay for the storage
you use, and you can scale compute up and down as needed depending on the size of your data and its associated index.

| Feature                         | Description                                                                                                                                              |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Serverless & Cost Efficient** | Automatically scales to zero when idle, with usage-based pricing so you onlypay for what you use. No need to manage or pay for always-on infrastructure. |
| **True Multimodal Storage**     | Store raw data, embeddings, and metadata together for fast retrieval and filtering. Optimized for vectors, text, images and more.                        |
| **Simple Migration**            | Seamlessly migrate from open source LanceDB by just changing the connection URL. No code changes required.                                               |
| **Enterprise-Grade Security**   | Data encryption at rest, SOC2 Type 2 compliance, and HIPAA compliance for regulated workloads.                                                           |
| **Full Observability**          | Native integration with OpenTelemetry for comprehensive logging, monitoring and distributed tracing.                                                     |

## Which LanceDB to Use?

### LanceDB OSS: Embedded Vector Search

LanceDB OSS acts an embedded, in-process vector database designed for production in self-hosted deployments. It integrates seamlessly into your existing application architecture and ML pipelines, providing full control over your data and infrastructure.

**Ideal for:** Self-hosting and organizations requiring complete data sovereignty in their own cloud.

### LanceDB Cloud: Managed Serverless Service

LanceDB Cloud is a fully managed, serverless vector database that eliminates infrastructure management overhead. The service automatically handles scaling, security, and operational tasks while providing enterprise-grade reliability and performance.

**Ideal for:** Production applications, teams requiring rapid deployment, organizations needing automatic scaling, and workloads requiring enterprise security features.

<Info>
  Both versions leverage the same high-performance Lance data format, ensuring consistent performance and enabling effortless migration from OSS to Cloud when your needs evolve. [Start with Cloud today](https://cloud.lancedb.com) to experience the benefits of managed infrastructure.
</Info>

## Upgrading to Cloud

When your application requires a managed deployment for production, you can seamlessly transition from OSS to Cloud by simply updating your connection string to point to the remote database.

LanceDB Cloud enables you to scale your AI applications from development to production without code changes or infrastructure management overhead.

<a href="https://accounts.lancedb.com/sign-up">
  <img alt="LanceDB Cloud: Serverless vector search with enterprise-grade performance!" />
</a>


# Demo Application Gallery
Source: https://docs.lancedb.com/demos/index

Demo apps showcasing end-to-end applications built with LanceDB for production use cases.

Explore the demo applications built with LanceDB below.

| App                                                         | Description                                                                                                  |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [Semantic.Art](#semantic-art)                               | A multimodal art discovery platform using feelings, phrases, and images.                                     |
| [Wikipedia 41M Hybrid Search](#wikipedia-41m-hybrid-search) | An interactive hybrid search demo combining full-text search and vector search.                              |
| [Video Search](#video-search)                               | A video search application that allows searching through a library of videos using natural language queries. |

## Semantic.art

<Badge>multimodal</Badge>
<Badge>hybrid-search</Badge>
<Badge>vector-search</Badge>
<Badge>semantic-routing</Badge>

<Card title="Semantic.art" href="https://www.semantic.art/">
  Semantic.art turns real, human-made art discovery into a multimodal search experience using
  feelings, phrases, and images. It's built with LanceDB hybrid search and semantic routing.

  <Card title="Learn how it's built" href="https://lancedb.com/blog/semanticdotart/">
    Read in detail about how Semantic.art is built in this blog post.
  </Card>
</Card>

## Wikipedia 41M Hybrid Search

<Badge>multimodal</Badge>
<Badge>hybrid-search</Badge>
<Badge>vector-search</Badge>
<Badge>fts</Badge>

<Card title="Wikipedia 41M Hybrid Search" href="https://lancedb-demos.vercel.app/demo/wikipedia-search">
  Interactive hybrid search, full-text search (FTS) and vector search demo with 41M+ Wikipedia entries.
  Explore the power of combining FTS with vector search for more relevant results.

  <Card title="Learn how it's built" href="https://lancedb.com/blog/feature-full-text-search/">
    Read in detail about how the Wikipedia 41M hybrid search demo is built in this blog post.
  </Card>
</Card>

## Video Search

<Badge>multimodal</Badge>
<Badge>video-search</Badge>
<Badge>vector-search</Badge>

<Card title="Video Search" href="https://lancedb-demos.vercel.app/demo/video-search">
  Search through a library of videos using natural language queries. This demo showcases how to use LanceDB
  to perform semantic search on video content.
</Card>


# Managing Embeddings
Source: https://docs.lancedb.com/embedding/index

Use the embedding API in LanceDB -- registry, functions, schemas, and multi-language SDK support.

Modern machine learning models can be trained to convert raw data into embeddings, which are vectors
of floating point numbers. The position of an embedding in vector space captures the semantics of
the data, so vectors that are close to each other are considered similar.

LanceDB provides an embedding function registry in OSS as well as its Cloud and Enterprise versions
([see below](#embeddings-in-lancedb-cloud-and-enterprise))
that automatically generates vector embeddings during data ingestion. Automatic query-time embedding
generation is currently only supported in LanceDB OSS. The API abstracts embedding generation, allowing
you to focus on your application logic.

## Embedding Registry

<Badge>OSS</Badge>

In LanceDB OSS, you can get a supported embedding function from the registry, and then use it in your table schema.
Once configured, the embedding function will automatically generate embeddings when you insert data
into the table. And when you query the table, you can provide a query string or other input, and the
embedding function will generate an embedding for it.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.embeddings import get_registry
  from lancedb.pydantic import LanceModel, Vector

  # Get a sentence-transformer function
  func = get_registry().get("sentence-transformers").create()

  class MySchema(LanceModel):
      # Embed the 'text' field automatically
      text: str = func.SourceField()
      # Store the embeddings in the 'vector' field
      vector: Vector(func.ndims()) = func.VectorField()

  # Create a LanceDB table with the schema
  import lancedb
  db = lancedb.connect("./mydb")
  table = db.create_table("mytable", schema=MySchema)
  # Insert data - embeddings are generated automatically
  table.add([
      {"text": "This is a test."},
      {"text": "Another example."}
  ])

  # Query the table - embeddings are generated for the query
  results = table.search("test example").limit(5).to_pandas()
  print(results)

  ## Example Output
  #                                   text                            vector  _distance
  # 0                     This is a test.  [0.0123, -0.0456, ..., 0.0789]  0.123456
  # 1                     Another example.  [0.0234, -0.0567, ..., 0.0890]  0.234567
  ```
</CodeGroup>

### Using an embedding function

The `.create()` method accepts several arguments to configure the embedding function's behavior. `max_retries` is a special argument that applies to all providers.

| Argument      | Type  | Description                                                                  |
| ------------- | ----- | ---------------------------------------------------------------------------- |
| `name`        | `str` | The name of the model to use (e.g., `text-embedding-3-small`).               |
| `max_retries` | `int` | The maximum number of times to retry on a failed API request. Defaults to 7. |

Other arguments are provider-specific. Common arguments include the following:

| Argument     | Type  | Description                                                                            |
| ------------ | ----- | -------------------------------------------------------------------------------------- |
| `batch_size` | `int` | The number of inputs to process in a single batch. Provider-specific.                  |
| `api_key`    | `str` | The API key for the embedding provider. Can also be set via environment variables.     |
| `device`     | `str` | The device to run the model on (e.g., "cpu", "cuda"). Defaults to automatic detection. |

Find the full list of arguments for each provider in the [integrations](/integrations/embedding) section.

## Embedding model providers

LanceDB supports most popular embedding providers.

### Text embeddings

| Provider              | Model ID                | Default Model            |
| --------------------- | ----------------------- | ------------------------ |
| OpenAI                | `openai`                | `text-embedding-ada-002` |
| Sentence Transformers | `sentence-transformers` | `all-MiniLM-L6-v2`       |
| Hugging Face          | `huggingface`           | `colbert-ir/colbertv2.0` |
| Cohere                | `cohere`                | `embed-english-v3.0`     |
| ...                   | ...                     | ...                      |

### Multimodal embedding

| Provider  | Model ID    | Supported Inputs           |
| --------- | ----------- | -------------------------- |
| OpenCLIP  | `open-clip` | Text, Images               |
| ImageBind | `imagebind` | Text, Images, Audio, Video |
| ...       | ...         | ...                        |

You can find all supported embedding models in the [integrations](/integrations/embedding) section.

## Embeddings in LanceDB Cloud and Enterprise

Currently, the embedding registry on LanceDB <Badge>Cloud</Badge> or
<Badge>Enterprise</Badge> supports automatic generation of embeddings during data ingestion,
generated on the client side (and stored on the remote table). We don't yet support automatic query-time
embedding generation when sending queries, though this is planned for a future release.

For now, you can manually generate the embeddings at query time using the same embedding function that
was used during ingestion, and pass the embeddings to the search function.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  from lancedb.embeddings import get_registry
  from lancedb.pydantic import LanceModel, Vector

  db = lancedb.connect(...)
  func = get_registry().get("sentence-transformers").create()

  class MySchema(LanceModel):
      text: str = func.SourceField()
      vector: Vector(func.ndims()) = func.VectorField()

  table = db.create_table("mytable", schema=MySchema)
  table.add([
      {"text": "This is a test."},
      {"text": "Another example."}
  ])

  # Manually generate embeddings for the query
  query_vector = func.generate_embeddings(["test example"])[0]
  results = table.search(query_vector).limit(5).to_pandas()
  ```
</CodeGroup>

## Custom Embedding Functions

You can always implement your own embedding function by inheriting from `TextEmbeddingFunction`
(for text) or `EmbeddingFunction` (for multimodal data).

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.embeddings import register, TextEmbeddingFunction
  from functools import cached_property

  @register("my-embedder")
  class MyTextEmbedder(TextEmbeddingFunction):
      model_name: str = "my-model"
      
      def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
          # Your embedding logic here
          return self._model.encode(texts).tolist()
      
      def ndims(self) -> int:
          # Return the dimensionality of the embeddings
          return len(self.generate_embeddings(["test"])[0])
      
      @cached_property
      def _model(self):
          # Initialize your model once
          return MyEmbeddingModel(self.model_name)
  ```
</CodeGroup>


# Embeddings: Quickstart
Source: https://docs.lancedb.com/embedding/quickstart

Quickstart guide for generating and working with embeddings.

LanceDB will automatically vectorize the data both at ingestion and query time. All you need to do is specify which model to use.

We support popular embedding models like OpenAI, Hugging Face, Sentence Transformers, CLIP, and more.

## Step 1: Import Required Libraries

First, import the necessary LanceDB components:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  from lancedb.pydantic import LanceModel, Vector
  from lancedb.embeddings import get_registry
  ```
</CodeGroup>

* `lancedb`: The main database connection and operations
* `LanceModel`: Pydantic model for defining table schemas
* `Vector`: Field type for storing vector embeddings
* `get_registry()`: Access to the embedding function registry. It has all the supported as well custom embedding functions registered by the user

## Step 2: Connect to LanceDB Cloud

Establish a connection to your LanceDB instance:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Enter your LanceDB connection URI for OSS, Cloud or Enterprise here
  db = lancedb.connect(...)
  ```
</CodeGroup>

## Step 3: Initialize the Embedding Function

Choose and configure your embedding model:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  model = get_registry().get("sentence-transformers").create(name="BAAI/bge-small-en-v1.5", )
  ```
</CodeGroup>

This creates a Sentence Transformers embedding function using the BGE model. You can:

* Change `"sentence-transformers"` to other providers like `"openai"`, `"cohere"`, etc.
* Modify the model name for different embedding models
* Set `device="cuda"` for GPU acceleration if available

## Step 4: Define Your Schema

Create a Pydantic model that defines your table structure:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  class Words(LanceModel):
      text: str = model.SourceField()  
      vector: Vector(model.ndims()) = model.VectorField()
  ```
</CodeGroup>

* `SourceField()`: This field will be embedded
* `VectorField()`: This stores the embeddings
* `model.ndims()`: Sets vector dimensions for your model

## Step 5: Create Table and Ingest Data

Create a table with your schema and add data:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table = db.create_table("words", schema=Words)
  table.add([
      {"text": "hello world"},
      {"text": "goodbye world"}
  ])
  ```
</CodeGroup>

The `table.add()` call automatically:

* Takes the text from each document
* Generates embeddings using your chosen model
* Stores both the original text and the vector embeddings

## Step 6: Query with Automatic Embedding

Note: On LanceDB cloud, automatic query embedding is not supported. You need to pass the embedding vector directly.

Search your data using natural language queries:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  query = "greetings"
  actual = table.search(query).limit(1).to_pydantic(Words)[0]
  print(actual.text)
  ```
</CodeGroup>

The search process:

1. Automatically converts your query text to embeddings
2. Finds the most similar vectors in your table
3. Returns the matching documents

## Examples

LanceDB currently supports the via SDKs in [Python, Typescript and Rust](/api-reference/).

Below are some examples of generating and querying embeddings when using the embedding registry.


# Architecture
Source: https://docs.lancedb.com/enterprise/architecture

Learn about LanceDB Enterprise architecture and system design.

LanceDB Enterprise consists of the following key components:

* Query Fleet
* Plan Execution Fleet
* Indexer Fleet

<img alt="architecture" />

### Query Execution

The LanceDB stateless query fleet is capable of managing **tens of thousands** of queries per second (QPS) per table with minimal latency.
This level of throughput satisfies the requirements of even the most demanding production environments.

Each query is compiled into a distributed query plan and executed on the Plan Execution Fleet in parallel.
Additionally, each query is auto-vectorized for recent generations of `x86_64` and `ARM`
CPUs for enhanced hardware efficiency.

### Plan Execution Fleet

Each plan execution node is equipped with high-performance NVMe SSDs that act as
a hybrid cache for cloud object storage systems like AWS S3,
Google Cloud Storage, and Azure Blob Storage.

The distributed query plan enforces cache locality for both data and indices using a variant of
the **consistent hashing** algorithm with a low cache miss rate.
LanceDB can serve warm queries with latency in **the single-digit to low double-digit milliseconds** range.

### Write Path

LanceDB Enterprise is engineered for high-throughput data ingestion and indexing.
The system ensures data persistence on durable object storage before confirming any write request.

An extensive indexing fleet, enhanced with hardware acceleration, operates asynchronously to
perform partial or full indexing, data compaction, and cleanup.
Furthermore, we achieve high-throughput indexing operations without compromising query performance.

<Note>
  Customer data does not go through the event queue. The queue sends events such as
  "create an index" to the indexers to trigger actions.
</Note>

<Info>
  Indexing scales down to zero when there is no activity on the table.
</Info>


# Benchmarks
Source: https://docs.lancedb.com/enterprise/benchmarks

See numbers from LanceDB Enterprise's performance scalability and latency benchmarks.

LanceDB's architecture is designed to deliver **25ms** vector search latency.
Even with metadata filtering, our query latency remains as low as **50ms**.
It is important to note that we can support thousands of QPS with such query performance.

| Percentile | Vector Search | Vector Search w. Filtering | Full-Text Search |
| :--------: | :-----------: | :------------------------: | :--------------: |
|     P50    |      25ms     |            30ms            |       26ms       |
|     P90    |      26ms     |            39ms            |       37ms       |
|     P99    |      35ms     |            50ms            |       42ms       |

## Dataset

We used two datasets for this benchmark test: the [dbpedia-entities-openai-1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M)
for vector search, and a synthetic dataset for vector search with metadata filtering.

| Name                       |  # Vectors | Vector Dimension |
| :------------------------- | :--------: | :--------------: |
| dbpedia-entities-openai-1M |  1,000,000 |       1536       |
| synthetic dataset          | 15,000,000 |        256       |

## Vector Search

We ran vector queries with dbpedia-entities-openai-1M with a warmed-up cache.
The query latency is as follows:

| Percentile | Latency |
| :--------: | :-----: |
|     P50    |   25ms  |
|     P90    |   26ms  |
|     P99    |   35ms  |
|     Max    |   49ms  |

## Full-Text Search

With the same dataset and a warmed-up cache, the full-text search performance is as follows:

| Percentile | Latency |
| :--------: | :-----: |
|     P50    |   26ms  |
|     P90    |   37ms  |
|     P99    |   42ms  |
|     Max    |   98ms  |

## Vector Search with Metadata Filtering

We created a 15M-vector dataset with sufficient complexity to thoroughly test our complex metadata filtering capabilities.
Such filtering can span a wide range of scalar columns, e.g., "find Sci-fi movies since 1900".

With a warmed-up cache, the query performance using slightly more selective filters,
e.g., "find Sci-fi movies between the years 2000 and 2012", is as follows:

| Percentile | Latency |
| :--------: | :-----: |
|     P50    |   30ms  |
|     P90    |   39ms  |
|     P99    |   50ms  |

The query performance using complex filters, e.g., "find Sci-fi movies since 1900", is as follows:

| Percentile | Latency |
| :--------: | :-----: |
|     P50    |   65ms  |
|     P90    |   76ms  |
|     P99    |  100ms  |

<Check>
  Our benchmarks are designed to provide consistent and reproducible performance evaluations of LanceDB. We regularly update and re-run these benchmarks to ensure the data remains accurate and relevant.
</Check>


# Azure deployment guide
Source: https://docs.lancedb.com/enterprise/deployment/azure

Learn how to deploy LanceDB Enterprise on Azure with AKS, Private Link, and Blob Storage.

LanceDB Enterprise can be deployed on Azure using Azure Kubernetes Service (AKS) with Azure Blob Storage for data persistence and Azure Private Link for secure connectivity.

## General Architecture Overview

```mermaid theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
graph TB
    subgraph "Client VPC"
        Client[Client Applications]
    end
    
    subgraph "Server VPC"
        PLS[Azure Private Link Service]
        
        subgraph "AKS Cluster"
            LDB[LanceDB Enterprise<br/>Query Nodes, Plan Executors,<br/>Lance Agent, Indexer Pods]
        end
        
        EH[Azure EventHub<br/>for LanceDB internal<br/>message passing]
        
        BS[Azure Blob Storage]
        
        WI[Azure Workload Identity]
    end
    
    Client ==>|Private Link| PLS
    PLS ==> LDB
    LDB <-->|Read/Write| BS
    LDB -->|Async Events| EH
    EH -->|Process| LDB
    
    WI -.->|RBAC| BS
    WI -.->|Assigned| LDB
    
    style Client fill:#d7e3fc,stroke:#5c6bc0,stroke-width:2px,color:#0d1b2a
    style PLS fill:#f3e5f5,stroke:#ab47bc,stroke-width:2px,color:#311432
    style LDB fill:#ffe0b2,stroke:#fb8c00,stroke-width:2px,color:#4a2f11
    style EH fill:#f8bbd0,stroke:#ec407a,stroke-width:2px,color:#4a0821
    style BS fill:#e0f2f1,stroke:#26a69a,stroke-width:2px,color:#09312d
    style WI fill:#e6f4ea,stroke:#66bb6a,stroke-width:2px,color:#1d3a1f
```

### Key Components

* **LanceDB architecture** is deployed in an AKS cluster within its own VPC
* **Client applications** connect to the cluster securely using Azure Private Link
* **AKS cluster** is granted Azure Blob Storage read/write permissions using Azure Workload Identity
* **Azure EventHub** can be used as the message queue by LanceDB Enterprise for internal message communication (alternative: self-hosted Kafka cluster in AKS)

## Read Path Architecture

```mermaid theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
graph LR
    subgraph "Client Network"
        C[Client App]
    end
    
    subgraph "Azure AKS Cluster"
        PL[Private Link<br/>Service]
        QN[Query Nodes<br/>Phalanx]
        PE[Plan Executors<br/>Distributed Data Cache]
    end
    
    subgraph "Storage"
        BS[Azure Blob<br/>Storage]
    end
    
    C -->|Private<br/>Connection| PL
    PL --> QN
    QN -->|Query<br/>Request| PE
    PE -->|Cache Miss<br/>Read Data| BS
    
    style C fill:#d7e3fc,stroke:#5c6bc0,color:#0d1b2a
    style PL fill:#f3e5f5,stroke:#ab47bc,color:#311432
    style QN fill:#ffe0b2,stroke:#fb8c00,color:#4a2f11
    style PE fill:#ffecb3,stroke:#ffb74d,color:#4a2f11
    style BS fill:#e0f2f1,stroke:#26a69a,color:#09312d
```

### Read Path Flow

1. **Client Application** sends query request through Private Link
2. **Query Nodes** receive and process the request
3. **Plan Executors** optimize and execute the query using distributed data cache to speed up read queries
4. **Azure Blob Storage** stores data and indices in Lance, while Plan Executors maintain distributed cache for performance

## Write Path Architecture

```mermaid theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
graph LR
    subgraph "Client Network"
        C[Client App]
    end
    
    subgraph "Azure AKS Cluster"
        PL[Private Link<br/>Service]
        QN[Query Nodes<br/>Phalanx]
        LA[Lance Agent]
        IP[Indexer Pods<br/>On-Demand]
    end
    
    subgraph "Messaging"
        EH[Azure EventHub<br/>Write Events]
    end
    
    subgraph "Storage"
        BS[Azure Blob<br/>Storage]
    end
    
    C -->|Private<br/>Connection| PL
    PL --> QN
    QN -->|Sync<br/>Write| BS
    QN -->|Async<br/>Events| EH
    EH -->|Consume| LA
    LA -->|Launch| IP
    IP -->|Index &<br/>Optimize| BS
    
    style C fill:#d7e3fc,stroke:#5c6bc0,color:#0d1b2a
    style PL fill:#f3e5f5,stroke:#ab47bc,color:#311432
    style QN fill:#ffe0b2,stroke:#fb8c00,color:#4a2f11
    style LA fill:#ffe5c3,stroke:#ffb74d,color:#4a2f11
    style IP fill:#ffe5c3,stroke:#ffb74d,color:#4a2f11
    style EH fill:#f8bbd0,stroke:#ec407a,color:#4a0821
    style BS fill:#e0f2f1,stroke:#26a69a,color:#09312d
```

### Write Path Flow

Query nodes write data and indices synchronously to Azure Blob Storage in Lance data format while asynchronously sending data modification events to Azure EventHub (or self-hosted Kafka cluster). These write events are processed by the Lance Agent, which launches indexing pods or data optimization pods to optimize data for better read performance.

## Deployment Options

### Storage Architecture Support

```mermaid theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
graph TB
    subgraph "Multi-Account & Multi-Container Support"
        SA1[Storage Account 1]
        SA2[Storage Account 2]
        SA3[Storage Account N]
        
        SA1 --> C1A[Container A]
        SA1 --> C1B[Container B]
        SA1 --> C1C[Container C]
        
        SA2 --> C2A[Container X]
        SA2 --> C2B[Container Y]
        
        SA3 --> C3A[Container 1]
        SA3 --> C3B[Container 2]
    end
    
    style SA1 fill:#e0f2f1,stroke:#26a69a,color:#09312d
    style SA2 fill:#e0f2f1,stroke:#26a69a,color:#09312d
    style SA3 fill:#e0f2f1,stroke:#26a69a,color:#09312d
```

### Deployment Models

LanceDB Enterprise supports three deployment models on Azure:

#### 1. Fully Managed Service

* **Infrastructure and storage** in LanceDB's Azure account
* **Complete management** by LanceDB team
* **Simplest setup** for customers

#### 2. BYOC (Bring Your Own Cloud)

* **Infrastructure and storage** in customer's Azure account
* **Fully Managed by LanceDB**
* **Full control** over data residency

#### 3. Hybrid - Bring Your Own Container

* **Infrastructure** in LanceDB's account
* **Storage containers** in customer's account

<Note>
  For private deployments, high performance at extreme scale, or if you have strict security requirements, [contact us about LanceDB Enterprise](mailto:contact@lancedb.com).
</Note>


# Deployment guide
Source: https://docs.lancedb.com/enterprise/deployment/index

Learn how to deploy LanceDB Enterprise in production environments.

There are two deployment models available for LanceDB Enterprise: **Managed** and **BYOC**.
Both models support AWS, GCP, and Azure cloud platforms.

## Managed deployment

This is a private deployment of LanceDB Enterprise.
All applications run in cloud accounts managed by LanceDB in the same location as your client applications.

This hands-off approach is recommended for users who do not wish to manage the infrastructure themselves.

To access your deployment, LanceDB can provision either a public or private load balancer.

## Bring-your-own-cloud (BYOC) deployment

With this deployment model, LanceDB Enterprise is installed into your own cloud account.

This approach is recommended when:

* Users' security requirements for data residency preclude them from having data leave their account
* Other applications need to access the object storage directly

To deploy, an identity will be provisioned in your account with permissions to manage the infrastructure.

## Custom deployments

LanceDB Enterprise installation is highly configurable and customizable to your needs.
If you have any other specific deployment requirements, please reach out to our support team
at [contact@lancedb.com](mailto:contact@lancedb.com).


# LanceDB Enterprise vs OSS
Source: https://docs.lancedb.com/enterprise/features

Key benefits and differentiating features of LanceDB Enterprise over LanceDB OSS.

Modern AI workloads produce petabytes of multimodal data that must be queried in real time. On top of that, enterprise AI systems must stay completely private and air-gapped.

LanceDB offers two self-hosted options to meet such requirements: LanceDB OSS, a single-process library, and LanceDB Enterprise, a distributed cluster with automated scaling and low-latency caching.

This document compares their architectures and operational models so you can select the deployment that meets your performance targets and resource constraints.

## Differentiating features

LanceDB Enterprise is a distributed cluster that spans many machines (unlike LanceDB OSS, which is an embedded database that runs inside your process). Both are built on top of the same Lance columnar file format, so moving data from one edition to the other requires no conversion.

| Dimension                       | LanceDB OSS                           | LanceDB Enterprise                      | What the difference means                                                                             |
| :------------------------------ | :------------------------------------ | :-------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **Mode**                        | Single process                        | Distributed fleet                       | OSS lives on one host. Enterprise spreads work across nodes and keeps serving even if one node fails. |
| **Latency from object storage** | 500–1000 ms                           | 50–200 ms                               | Enterprise mitigates network delay with an SSD cache and parallel reads.                              |
| **Throughput**                  | 10–50 QPS                             | Up to 10,000 QPS                        | A cluster can serve thousands of concurrent users; a single process cannot.                           |
| **Cache**                       | None                                  | Distributed NVMe cache                  | Enterprise keeps hot data near compute and avoids repeated S3 calls.                                  |
| **Indexing & compaction**       | Manual                                | Automatic                               | Enterprise runs background jobs that rebuild and compact data without downtime.                       |
| **Data format**                 | Supports multiple available standards | Supports multiple available standards   | No vendor lock-in; data moves freely between editions.                                                |
| **Deployment**                  | Embedded in your code                 | Bring-Your-Own-Cloud or Managed Service | Enterprise meets uptime, compliance, and support goals that OSS cannot.                               |

### Architecture and scale

LanceDB OSS is directly embedded into your service. The process owns all CPU, memory, and storage, so scale is limited to what the host can provide.
LanceDB Enterprise separates work into routers, execution nodes, and background workers. New nodes join the cluster through a discovery service; they register, replicate metadata, and begin answering traffic without a restart. A distributed control plane watches node health, shifts load away from unhealthy nodes, and enforces consensus rules that prevent split-brain events.

Read More: [LanceDB Enterprise Architecture](/enterprise/architecture/)

### Latency of data retrieval

With Lance OSS every query fetches data from S3, GCS, or Azure Blob. Each round trip to an object store adds several hundred milliseconds, especially when data is cold.

LanceDB Enterprise uses NVMe SSDs as a hybrid cache, before the data store is even accessed. The first read fills the cache, and subsequent reads come from the local disk and return in tens of milliseconds. Parallel chunked reads further reduce tail latency. This gap matters when the application serves interactive dashboards or real-time recommendations.

Read More: [LanceDB Enterprise Performance](/enterprise/benchmarks/)

### Throughput of search queries

A single LanceDB OSS process shares one CPU pool with the rest of the application. When concurrent queries hit that CPU, retrieval and similarity processes compete for cores. The server cannot process more work in parallel and any extra traffic waits in the queue, raising latency without increasing queries per second.

LanceDB Enterprise distributes queries across many execution nodes. Each node runs a dedicated vector search engine that exploits all cores and uses SIMD instructions. A load balancer assigns queries to the least-loaded node, so throughput grows roughly linearly as more nodes join the cluster.

### Caching of commonly retrieved data

LanceDB OSS has no built-in cache. Every read repeats the same object-store round trip and pays the same latency penalty.

LanceDB Enterprise shards a cache across the fleet with consistent hashing. Popular vectors remain on local NVMe drives until they age out under a least-recently-used policy. Cache misses fall back to the object store, fill the local shard, and serve future reads faster. This design slashes both latency and egress cost for workloads with temporal locality.

### Maintenance of vector indexes

Vector indexes fragment when data is inserted, updated, or deleted. Fragmentation slows queries because the engine must scan more blocks. LanceDB OSS offers a CLI call to compact or rebuild the index, but you must schedule it and stop queries while it runs.

LanceDB Enterprise runs compaction jobs in the background. It copies data to a scratch space, rebuilds the index, swaps the old files atomically, and frees disk space. Production traffic continues uninterrupted.

Read More: [Indexing in LanceDB](/indexing/)

### Deployment and governance

When you work with LanceDB OSS, it is included as part of your binary, Docker, or serverless function. The footprint is small, and no extra services run beside it.

LanceDB Enterprise comes in two flavors. The Bring-Your-Own-Cloud (BYOC) template installs the control plane, routers, and nodes inside your VPC, so data never leaves your account. The managed SaaS option hands day-to-day operations to the vendor, including patching, scaling, and 24×7 monitoring. Both enterprise modes support private networking, role-based access control, audit logs, and single sign-on.

Read More: [LanceDB Enterprise Performance](/enterprise/deployment/)

## Which option is best?

LanceDB OSS makes sense when the entire dataset fits on one machine, daily traffic remains under fifty queries per second, and your team can run manual maintenance without affecting users.

[It's very simple to get started with OSS](/quickstart/): Get started with `pip install lancedb` and begin ingesting your data and vectors into LanceDB.

Move to LanceDB Enterprise when you have petabyte-scale data, or you need latency to be below 200 ms, or you need higher query throughput towards thousands of QPS, or your business requires high availability, compliance controls, and vendor support.

If these sound like your use cases, [reach out via this form](https://lancedb.com/contact/) and we can help you scope your workload and arrange an Enterprise proof of concept.


# LanceDB Enterprise
Source: https://docs.lancedb.com/enterprise/index

Features and benefits of LanceDB Enterprise.

**LanceDB Enterprise** is both a **private cloud or a BYOC solution** that transforms your data lake into
a high-performance vector database or lakehouse that can operate at extreme scale.

With a vector database built for [lakehouse architecture](/enterprise/architecture), you can serve millions of tables and tens
of billions of rows in a single index, improve retrieval quality using hybrid search with blazing-fast
metadata filters, and reduce costs by up to 200x with object storage.

<Callout icon="key">
  For private deployments, high performance at extreme scale, or if you have strict security requirements,
  [reach out to us](mailto:contact@lancedb.com) regarding LanceDB Enterprise.
</Callout>

## Key benefits of LanceDB Enterprise

Below, we list the three main benefits of using LanceDB Enterprise over the open-source version of LanceDB.

### 1. Perfect for large deployments

LanceDB Enterprise powers global deployments with a secure, compliant distributed lakehouse system that
ensures complete data sovereignty and high performance at scale.

| Benefit                 | Description                                                                                     |
| :---------------------- | :---------------------------------------------------------------------------------------------- |
| **Flexible Deployment** | Bring your own cloud, account, region, or Kubernetes cluster, or let LanceDB manage it for you. |
| **Multi-Cloud Support** | Available on AWS, GCP, and Azure. Open data layer that eliminates vendor lock-in.               |
| **Data Security**       | Encryption at rest, SOC 2 Type II, and HIPAA compliance.                                        |

### 2. Best performance for petabyte scale

LanceDB OSS is built on the highly-efficient Lance format and offers extensive features out of the box. Our
Enterprise solution amplifies these benefits by means of a custom-build distributed system.

| Benefit         | Description                                                                                                                                                                 |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Performance** | Tens of thousands of QPS with latency in single-digit milliseconds, hundreds of thousands of rows per second write throughput, and low-latency indexing across many tables. |
| **Scalability** | Support workloads requiring data isolation with millions of active tables, or a single table with billions of rows.                                                         |

### 3. Developer experience

LanceDB Enterprise extends our OSS product with production-grade features while maintaining full
compatibility. Move from prototype to production by simply updating your connection string -- no code
changes or data migration required!

| Benefit                  | Description                                                                                                                      |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Effortless Migration** | Migrate from Open Source LanceDB to LanceDB Enterprise by simply using a connection URL.                                         |
| **Observability**        | First-class integration with existing observability systems for logging, monitoring, and distributed traces using OpenTelemetry. |

Take a look at a more thorough [list of benefits of LanceDB Enterprise](/enterprise/features).


# Security & compliance
Source: https://docs.lancedb.com/enterprise/security

Learn about LanceDB Enterprise security features and best practices.

LanceDB Enterprise maintains the highest security standards with SOC 2 Type II and HIPAA compliance certifications. Our security framework ensures enterprise-grade protection for your data and workloads across all deployment models.

## Security Certifications

* **SOC 2 Type II**: Independent audit confirming our security controls and operational effectiveness
* **HIPAA Compliance**: Certified to handle protected health information (PHI) in healthcare applications
* **Regular Audits**: Ongoing security assessments to maintain compliance standards

### Future Compliance

Going forward, LanceDB will maintain SOC 2 Type II and HIPAA compliance by conducting continuous
audits to ensure our security practices remain aligned with industry standards and evolving
risks. Meanwhile, we are actively working on GDPR compliance.
[Contact us](mailto:contact@lancedb.com) to request a letter of engagement.

## LanceDB Enterprise

### Data Security

Customer data is strictly protected and remains within the confines of your account.
We maintain rigorous data isolation and encryption protocols to ensure confidentiality.
LanceDB Enterprise only receives telemetry data for monitoring system health.
At LanceDB, customer data security is paramount.

### Encryption

LanceDB Enterprise safeguards your data through encryption at rest, preventing
unauthorized access. This comprehensive encryption covers all data stored within the
object store and cache.


# LanceDB Cloud FAQ
Source: https://docs.lancedb.com/faq/faq-cloud

Commonly asked questions about LanceDB Cloud.

This section provides answers to the most common questions asked about LanceDB Cloud. By following these guidelines, you can ensure a smooth, performant experience with LanceDB Cloud.

## Connection

### Should I reuse the database connection?

Yes! It is recommended to establish a single database connection and maintain
it throughout your interaction with the tables within.

LanceDB uses HTTP connections to communicate with the servers. By reusing the Connection object, you avoid the overhead of repeatedly establishing HTTP connections, significantly improving efficiency.

### Should I reuse the `Table` object?

For optimal performance, `table = db.open_table()` should be called once and used for all subsequent table operations.
If there are changes to the opened table, the table will always reflect the latest version of the data.

## Indexing

### What are the vector indexing types supported by LanceDB Cloud?

We support `IVF_PQ` and `IVF_HNSW_SQ` as the `index_type` which is passed to `create_index`.
LanceDB Cloud tunes the indexing parameters automatically to achieve the best tradeoff
between query latency and query quality.

### When should users call `create_index()`? Does creating an index too early cause unbalanced indices?

`create_index` is asynchronous. LanceDB, in the background, will determine when to
trigger the index build job. When there are updates to the table data, we will optimize
the existing indices accordingly so that query performance is not impacted.

### When I add new rows to a table, do I need to manually update the vector index?

No! LanceDB Cloud triggers an asynchronous background job to index the new vectors.
Even though indexing is asynchronous, your vectors will still be immediately searchable.
LanceDB uses brute-force search to search over unindexed rows. This makes your new data
immediately available but may increase latency temporarily.
To disable the brute-force part of search, set the `fast_search` flag in your query to `true`.

### Do I need to reindex the whole dataset if only a small portion of the data is deleted or updated?

No! Similar to adding data to the table, LanceDB Cloud triggers an asynchronous background
job to update the existing indices. Therefore, no action is needed from users and newly updated
data will be available for search immediately. There is absolutely no downtime expected.

### Do I need to recreate my full-text search (FTS)/scalar index if I updated the table data?

No! LanceDB will automatically optimize the FTS index for you. Meanwhile, newly updated
data will be available for search immediately.

This applies to scalar indices as well.

### How do I know whether an index has been created?

While LanceDB Cloud indexes are typically created quickly, best practices differ
between index types:

* **Full-Text Search (FTS) and Scalar Indexes**
  Queries executed immediately after `create_fts_index` or `create_scalar_index` calls
  may fail if the background indexing process hasn't completed.
  Wait for index confirmation before querying.

* **Vector Indexes**
  Queries after `create_index` will not generate errors,
  but may experience degraded performance during ongoing index optimization.
  For consistent performance, wait until indexing finishes.

It's recommended to use `list_indices` to verify index creation before querying. As an alternative, you can check the table details
in the UI, where the existing indices will be displayed.

### How to find out number of unindexed rows?

You can call `index_stats` with the index name to check the number of
indexed and unindexed rows.

### Which indices should be enabled on filter columns? What's the impact of not indexing?

It is strongly recommended to create scalar indices on the filter columns. Scalar indices
will reduce the amount of data that needs to be scanned and thus speed up the filter.
LanceDB supports `BITMAP`, `BTREE`, and `LABEL_LIST` as our scalar index types. You
can see more details [here](/indexing#scalar-index).

### Does LanceDB always recreate the full index or incrementally update existing centroids?

LanceDB implements an optimization algorithm to decide whether a delta index will be
appended versus a full retrain on the index is needed.

## Query

### Can LanceDB support vector search combined with metadata filtering?

Yes! LanceDB supports blazing-fast vector search with metadata filtering. Both
prefiltering (default) and postfiltering are supported.
We have seen **30ms** as the p50 latency for a dataset size of 15 million.
You can see [here](/search/filtering/) for more details.

### What should I do if I need to search for rows by `id`?

LanceDB Cloud currently does not support an ID or primary key column. You are recommended to add a user-defined ID column. To significantly improve the query performance with SQL clauses, a scalar BITMAP/BTREE index should be created on this column.

### Why is my query latency higher than expected?

Multiple factors can impact query latency. To reduce query latency, consider the
following:

* Send pre-warm queries: Send a few queries to warm up the cache before
  an actual user query.
* Check network latency: LanceDB Cloud is hosted in AWS us-east-1 region.
  It is recommended to run queries from an EC2 instance that is in the same region.
* Create scalar indices: If you are filtering on metadata, it is recommended to
  create scalar indices on those columns. This will speed up searches with metadata filtering.
  See [here](/indexing#scalar-index) for more details on creating a scalar index.

### Will I always query the latest data?

* For LanceDB Cloud users, yes, strong consistency is guaranteed.
* For LanceDB Enterprise users, strong consistency is set by default. However, you can
  change the `weak_read_consistency_interval_seconds` parameter on the query node to trade off
  between read consistency and query performance.

### How does `fast_search` work?

If you do not need to query from the unindexed data, you can call `fast_search` to
make queries faster, with the unindexed data excluded.


# LanceDB Enterprise FAQ
Source: https://docs.lancedb.com/faq/faq-enterprise

Commonly asked questions about LanceDB Enterprise.

This section provides answers to the most common questions asked about LanceDB Enterprise. For assistance with LanceDB Enterprise, please [contact us](mailto:support@lancedb.com) via email and one of our
support staff will get back to you.

### Architecture and Fault Tolerance

#### What's the impact of losing each component (query node, indexer, etc.) in the LanceDB stack?

LanceDB Enterprise employs component-level replication to ensure fault tolerance and
continuous operations. While the system remains fully functional during replica
failures, transient performance impacts (e.g., elevated latency or reduced throughput)
may occur until automated recovery completes.\
For architectural deep dives, including redundancy configurations,
please contact the LanceDB team.

#### What does plan executor cache versus not cache?

The plan executor caches the table data, not the table indices.

#### Should I use disk cache or memory cache for the plan executor?

LanceDB implements highly performant consistent hashing for our plan executors.
NVMe SSD caching is enabled by default for all deployments.

#### How is the PE (Plan Executor) fleet shared? What fault tolerance exists (how many nodes can be lost)?

LanceDB's plan executor is typically deployed with 2+ replicas for fault tolerance:

* Mirrored Caches: Each query replica maintains synchronized copies of data subsets,
  enabling low-latency query execution.
* Load Balancing: Traffic is distributed evenly across replicas.

With a single replica failure, there is no downtime - the system remains
operational with degraded performance, as the remaining
replicas will handle all the traffic until the failed replica comes back online.

### Consistency

#### How is strong/weak consistency configured in the enterprise stack?

By default, LanceDB Enterprise operates in strong consistency mode.
Once a write is successfully acknowledged, a new Lance dataset version manifest
file is created. Subsequent reads always load the latest manifest file to
ensure the most up-to-date data.

However, this increases query latency and can place significant load on the storage system
under high concurrency. We offer the `weak_read_consistency_interval_seconds` parameter
to adjust consistency level (whose default value is zero). This parameter Defines the interval
(in seconds) at which the system checks for table updates from other processes.

<Tip>
  **Recommended Setting**

  To balance consistency and performance, setting `weak_read_consistency_interval_seconds` to 30–60 seconds is often a
  good trade-off. This reduces unnecessary cloud storage operations while still
  keeping data reasonably fresh for most applications.

  Note that **this setting only affects read operations**. Write operations always remain strongly consistent.
</Tip>

### Indexing

#### Can I use GPU for indexing?

Yes! Please [contact](mailto:support@lancedb.com) the LanceDB team to enable GPU-based indexing for
your deployment. Then you just need to call `create_index`, and the backend will use GPU for indexing.
LanceDB is able to index a few billion vectors under 4 hours.

### Cluster Configuration

#### What are the parameters that can be configured for my LanceDB cluster?

LanceDB Enterprise offers granular control over performance, resilience, and
operational behavior through a comprehensive set of parameters: replication factors for
each component, consistency level, graceful shutdown time intervals, etc. Please
contact the LanceDB team for detailed documentation on such parameter configurations.

### Monitoring and Alerts

#### What are the metrics that LanceDB exposes for monitoring?

We have various metrics set up for monitoring each component in the LanceDB stack:

* Query node: RPS, query latency, error codes, slow take count, CPU/memory utilization, etc.
* Plan executor: SSD cache hit/miss, CPU/memory utilization, etc.

Please contact the LanceDB team for the comprehensive list of monitoring metrics.

#### How do I integrate LanceDB's monitoring metrics with my monitoring dashboard?

LanceDB uses Prometheus for metrics collection and OpenTelemetry (OTel) to export such
metrics with data enrichment. The LanceDB team will work with you to integrate the
monitoring metrics with your preferred dashboard.

### Other

#### How do I check the Lance version of my dataset?

Upgrade to a recent pylance version (v0.18.0+), then use *LanceDataset.data\_storage\_version*

```py theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
>>> lance.dataset("my_dataset").data_storage_version
'2.0'
```


# LanceDB: Frequently Asked Questions
Source: https://docs.lancedb.com/faq/faq-oss

Commonly asked questions about LanceDB OSS.

This section covers some common questions and issues that you may encounter when using LanceDB.

### Is LanceDB open source?

Yes, LanceDB is an open source vector database available under an Apache 2.0 license. We also have a serverless SaaS solution, LanceDB Cloud, available under a commercial license.

### What is the difference between Lance and LanceDB?

[Lance](https://github.com/lancedb/lance) is a modern columnar data format for AI, written in Rust. It's perfect for building search engines, feature stores and being the foundation of large-scale ML training jobs requiring high performance IO and shuffles. It also has native support for storing, querying, and inspecting deeply nested data for robotics or large blobs like images, point clouds, and more.

LanceDB is the vector database that's built on top of Lance, and utilizes the underlying optimized storage format to build efficient disk-based indexes that power semantic search & retrieval applications, from RAGs to QA bots to recommender systems.

### Why invent another data format instead of using Parquet?

As we mention in our talk titled "[Lance, a modern columnar data format](https://www.youtube.com/watch?v=ixpbVyrsuL8)", Parquet and other tabular formats that derive from it are rather dated (Parquet is over 10 years old), especially when it comes to random access on vectors. We needed a format that's able to handle the complex trade-offs involved in shuffling, scanning, OLAP and filtering large datasets involving vectors, and our extensive experiments with Parquet didn't yield sufficient levels of performance for modern ML. [Our benchmarks](https://lancedb.com/blog/benchmarking-random-access-in-lance/) show that Lance is up to 1000x faster than Parquet for random access, which we believe justifies our decision to create a new data format for AI.

### Why build in Rust?

We believe that the Rust ecosystem has attained mainstream maturity and that Rust will form the underpinnings of large parts of the data and ML landscape in a few years. Performance, latency and reliability are paramount to a vector DB, and building in Rust allows us to iterate and release updates more rapidly due to Rust's safety guarantees. Both Lance (the data format) and LanceDB (the database) are written entirely in Rust. We also provide Python, JavaScript, and Rust client libraries to interact with the database.

### What makes LanceDB different?

LanceDB is among the few embedded vector DBs out there that we believe can unlock a whole new class of LLM-powered applications in the browser or via edge functions. Lance's multimodal nature allows you to store the raw data, metadata and the embeddings all at once, unlike other solutions that typically store just the embeddings and metadata.

The Lance data format that powers our storage system also provides true zero-copy access and seamless interoperability with numerous other data formats (like Pandas, Polars, Pydantic) via Apache Arrow, as well as automatic data versioning and data management without needing extra infrastructure.

### How large of a dataset can LanceDB handle?

LanceDB and its underlying data format, Lance, are built to scale to really large amounts of data (hundreds of terabytes). We are currently working with customers who regularly perform operations on 200M+ vectors, and we're fast approaching billion scale and beyond, which are well-handled by our disk-based indexes, without you having to break the bank.

### Do I need to build a vector index to run vector search?

No. LanceDB is blazing fast (due to its disk-based index) for even brute force kNN search, within reason. In our benchmarks, computing 100K pairs of 1000-dimension vectors takes less than 20ms. For small datasets of \~100K records or applications that can accept \~100ms latency, a vector index is usually not necessary.

For large-scale (>1M) or higher dimension vectors, it is beneficial to create a vector index. See the [Vector Indexes](/indexing/vector-index/) section for more details.

### How can I speed up data inserts?

It's highly recommended to perform bulk inserts via batches (for e.g., Pandas DataFrames or lists of dicts in Python) to speed up inserts for large datasets. Inserting records one at a time is slow and can result in suboptimal performance because each insert creates a new data fragment on disk. Batching inserts allows LanceDB to create larger fragments (and their associated manifests), which are more efficient to read and write.

### Do I need to set a refine factor when using an index?

Yes. LanceDB uses PQ, or Product Quantization, to compress vectors and speed up search when using an ANN index. However, because PQ is a lossy compression algorithm, it tends to reduce recall while also reducing the index size. To address this trade-off, we introduce a process called **refinement**. The normal process computes distances by operating on the compressed PQ vectors. The refinement factor (*rf*) is a multiplier that takes the top-k similar PQ vectors to a given query, fetches `rf * k` *full* vectors and computes the raw vector distances between them and the query vector, reordering the top-k results based on these scores instead.

For example, if you're retrieving the top 10 results and set `refine_factor` to 25, LanceDB will fetch the 250 most similar vectors (according to PQ), compute the distances again based on the full vectors for those 250 and then re-rank based on their scores. This can significantly improve recall, with a small added latency cost (typically a few milliseconds), so it's recommended you set a `refine_factor` of anywhere between 5-50 and measure its impact on latency prior to deploying your solution.

### How can I improve IVF-PQ recall while keeping latency low?

When using an IVF-PQ index, there's a trade-off between recall and latency at query time. You can improve recall by increasing the number of probes and the `refine_factor`. In our benchmark on the GIST-1M dataset, we show that it's possible to achieve >0.95 recall with a latency of under 10 ms on most systems, using \~50 probes and a `refine_factor` of 50. This is, of course, subject to the dataset at hand and a quick sensitivity study can be performed on your own data. You can find more details on the benchmark in a past [blog post](https://medium.com/etoai/benchmarking-lancedb-92b01032874a).

<img alt="" />

### How much data can LanceDB practically manage without affecting performance?

We target good performance on \~10-50 billion rows and \~10-30 TB of data. For the best performance and
scalability guarantees, check out [LanceDB Enterprise](/enterprise).

### Does LanceDB support concurrent operations?

LanceDB can handle concurrent reads very well, and can scale horizontally. The main constraint is how well the storage layer you've chosen, scales. For writes, we support concurrent writing, though too many concurrent writers can lead to failing writes as there is a limited number of times a writer retries a commit.

<Warning>
  If you use Python's multiprocessing, you should probably not use `fork` as Lance is multi-threaded
  internally and `fork` and multi-threaded Python do not work well together.
  [Refer to this discussion](https://discuss.python.org/t/concerns-regarding-deprecation-of-fork-with-alive-threads/33555)
  for more information.
</Warning>


# Frequently Asked Questions
Source: https://docs.lancedb.com/faq/index

Common questions about LanceDB

Find answers to common questions about LanceDB across different deployment options and use cases.

<Card title="Can't find what you're looking for?" icon="question">
  Reach out on [Discord](https://discord.gg/AUEWnJ7Txb) for community support or [contact us](mailto:support@lancedb.com) for enterprise assistance.
</Card>

| Category                                  | Description                                                                         |
| :---------------------------------------- | :---------------------------------------------------------------------------------- |
| [LanceDB OSS](/faq/faq-oss)               | Questions about LanceDB open source deployment, installation, and community support |
| [LanceDB Cloud](/faq/faq-cloud)           | Questions about LanceDB Cloud service, pricing, and managed deployment              |
| [LanceDB Enterprise](/faq/faq-enterprise) | Questions about enterprise features, security, compliance, and support              |


# Feature catalog
Source: https://docs.lancedb.com/features

An outline of all the features offered by LanceDB, across its open source, cloud, and enterprise offerings.

## Storage

LanceDB provides flexible storage backends that support both cloud object storage and local high-performance storage for different deployment scenarios.

| Feature                                  | Description                                            | OSS | Cloud | Enterprise |
| :--------------------------------------- | :----------------------------------------------------- | :-: | :---: | :--------: |
| [Object, File, Block Storage](/storage/) | Support for AWS, GCS, Azure and S3-compatible vendors. |  ✅  |   ✅   |      ✅     |
| [Local SSD/NVMe Storage](/storage/)      | Support for storage on customer's custom servers.      |  ✅  |       |      ✅     |

## Tables

LanceDB's table abstraction provides ACID-compliant data management with schema evolution, versioning, and consistency guarantees for vector and scalar data.

| Feature                                      | Description                                           | OSS | Cloud | Enterprise |
| :------------------------------------------- | :---------------------------------------------------- | :-: | :---: | :--------: |
| [Tables - CRUD Operations](/tables/)         | Basic API to create, read, update, drop tables.       |  ✅  |   ✅   |      ✅     |
| [Tables - Data Evolution](/tables/schema/)   | Alter column schema, datatype,  backfill + merge data |  ✅  |   ✅   |      ✅     |
| [Tables - Versioning](/tables/versioning/)   | Append, overwrite, check versions + tag them.         |  ✅  |   ✅   |      ✅     |
| [Tables - Consistency](/tables/consistency/) | Synchronize database with underlying storage.         |  ✅  |   ✅   |      ✅     |

## Ingestion

LanceDB's ingestion pipeline handles both vector embedding generation and data loading with support for multiple formats and efficient batch operations.

| Feature                                                   | Description                                                               | OSS | Cloud | Enterprise |
| :-------------------------------------------------------- | :------------------------------------------------------------------------ | :-: | :---: | :--------: |
| [Embedding - Text Data](/embedding/)                      | Generate vector embeddings from text data using various embedding models. |  ✅  |   ✅   |      ✅     |
| [Embedding - Multimodal Data](/embedding/)                | Generate embeddings from images, audio, and other multimodal content.     |  ✅  |   ✅   |      ✅     |
| [Embedding - CPU & GPU Device Configuration](/embedding/) | Configure CPU or GPU acceleration for embedding generation performance.   |  ✅  |   ✅   |      ✅     |
| [Embedding - Environment Variables](/embedding/)          | Manage API keys and configuration for embedding model access.             |  ✅  |   ✅   |      ✅     |
| [Data Ingestion - Default](/tables/create/)               | Formerly called Adding Data to a Table.                                   |  ✅  |   ✅   |      ✅     |
| [Data Ingestion - Formats](/tables/create/)               | Pandas, Polars, Pyarrow, Pydantic                                         |  ✅  |   ✅   |      ✅     |
| [Data Ingestion - Upsert](/tables/update/)                | Update existing records or insert new ones based on key.                  |  ✅  |   ✅   |      ✅     |
| [Data Ingestion - Merge Insert](/tables/update/)          | Combine data from multiple sources into a single table.                   |  ✅  |   ✅   |      ✅     |

## Indexing

LanceDB's indexing system provides multiple vector and scalar index types with automated optimization for fast similarity search and retrieval operations.

| Feature                                                 | Description                                                           | OSS | Cloud | Enterprise |
| :------------------------------------------------------ | :-------------------------------------------------------------------- | :-: | :---: | :--------: |
| [Vector Index - IVF\_FLAT](/indexing/vector-index/)     | Minimal index that looks at IVF partitions, instead of brute forcing. |  ✅  |   ✅   |      ✅     |
| [Vector Index - IVF\_PQ](/indexing/vector-index/)       | Default vector index using Euclidean distance.                        |  ✅  |   ✅   |      ✅     |
| [Vector Index - IVF\_SQ](/indexing/vector-index/)       | IVF index built using scalar quantized vectors.                       |  ✅  |   ✅   |      ✅     |
| [Vector Index - IVF\_HNSW\_SQ](/indexing/vector-index/) | HNSW built on IVF's partitions + vectors that are scalar quantized.   |  ✅  |   ✅   |      ✅     |
| [Vector Index - Binary](/indexing/vector-index/)        | IVF\_FLAT with Hamming distance for binary vectors.                   |  ✅  |   ✅   |      ✅     |
| [Scalar Index](/indexing/scalar-index/)                 | BTREE, BITMAP, LABEL\_LIST                                            |  ✅  |   ✅   |      ✅     |
| [Automated Indexing](/indexing/vector-index/)           | Indexing happens in the background no config.                         |     |   ✅   |      ✅     |
| [Bypass Automated Indexing](/indexing/)                 | When you want to search over all available vectors.                   |  ✅  |   ✅   |      ✅     |
| [Reindexing - Manual](/indexing/reindexing/)            | User needs to specify that they want to reindex.                      |  ✅  |   ✅   |      ✅     |
| [Reindexing - Automated](/indexing/reindexing/)         | Reindexing happens in the background no config                        |     |   ✅   |      ✅     |
| [GPU Indexing - Manual](/indexing/gpu-indexing/)        | User needs to specify which indexing device to use.                   |  ✅  |   ✅   |      ✅     |
| [GPU Indexing - Automated](/indexing/gpu-indexing/)     | Indexing device is automatically set for user.                        |     |   ✅   |      ✅     |
| [Full Text Search Index](/indexing/fts-index/)          | Inverted index                                                        |  ✅  |   ✅   |      ✅     |

## Search

LanceDB's search capabilities combine vector similarity search, full-text search, and hybrid approaches to provide comprehensive retrieval functionality across different data types.

| Feature                                                         | Description                                                           | OSS | Cloud | Enterprise |
| :-------------------------------------------------------------- | :-------------------------------------------------------------------- | :-: | :---: | :--------: |
| [Vector Search - No Index](/search/vector-search/)              | Goes through all the available vectors.                               |  ✅  |   ✅   |      ✅     |
| [Vector Search - ANN Index](/search/vector-search/)             | Retrieves top K similar vectors.                                      |  ✅  |   ✅   |      ✅     |
| [Vector Search - Multivectors](/search/multivector-search/)     | Late interaction vector search.                                       |  ✅  |   ✅   |      ✅     |
| [Vector Search - Distance Range](/search/vector-search/)        | Search for vectors within a specific distance threshold.              |  ✅  |   ✅   |      ✅     |
| [Vector Search - Binary Vectors](/search/vector-search/)        | Search using binary vector representations for efficiency.            |  ✅  |   ✅   |      ✅     |
| [Vector Search - Filtering](/search/filtering/)                 | Apply scalar filters during vector search operations.                 |  ✅  |   ✅   |      ✅     |
| [Vector Search - Batch API](/search/vector-search/)             | Process multiple search queries in a single request.                  |  ✅  |   ✅   |      ✅     |
| [Vector Search - Async Indexing](/search/vector-search/)        | Fallback brute force for fast performance.                            |     |   ✅   |      ✅     |
| [Full Text Search - FTS Index](/search/full-text-search/)       | Inverted Index                                                        |  ✅  |   ✅   |      ✅     |
| [Full Text Search - Tokenizer](/search/full-text-search/)       | Ngram and other common methods of splitting text data.                |  ✅  |   ✅   |      ✅     |
| [Full Text Search - Scalar Index](/search/full-text-search/)    | BTREE, BITMAP, LABEL\_LIST for non-vector data.                       |  ✅  |   ✅   |      ✅     |
| [Full Text Search - Fuzzy Search](/search/full-text-search/)    | Searching when there is a typo on the query.                          |  ✅  |   ✅   |      ✅     |
| [Full Text Search - Prefix Matching](/search/full-text-search/) | Search for text that starts with specific characters.                 |  ✅  |   ✅   |      ✅     |
| [Full Text Search - Score Boosting](/search/full-text-search/)  | Increase relevance scores for specific terms or fields.               |  ✅  |   ✅   |      ✅     |
| [Full Text Search - Boolean Logic](/search/full-text-search/)   | Use AND, OR, NOT operators in text search queries.                    |  ✅  |   ✅   |      ✅     |
| [Full Text Search - Array Fields](/search/full-text-search/)    | Search within array or list data types.                               |  ✅  |   ✅   |      ✅     |
| [Hybrid Search - FTS Index](/search/hybrid-search/)             | Combine vector and full-text search in single query.                  |  ✅  |   ✅   |      ✅     |
| [Hybrid Search - Reranking](/search/hybrid-search/)             | Reorder search results using additional ranking models.               |  ✅  |   ✅   |      ✅     |
| [SQL Queries](/search/sql)                                      | Execute standard SQL queries on LanceDB tables.                       |  ✅  |   ✅   |      ✅     |
| [Query Optimization](/search/optimize-queries/)                 | Explain query plan, analyze query plan, optimization config settings. |  ✅  |   ✅   |      ✅     |

## Filtering

LanceDB's filtering system provides flexible query capabilities that can be applied independently or in combination with vector and full-text search operations.

| Feature                                            | Description                                       | OSS | Cloud | Enterprise |
| :------------------------------------------------- | :------------------------------------------------ | :-: | :---: | :--------: |
| [Filtering - no Vector Search](/search/filtering/) | Apply filters without vector search operations.   |  ✅  |   ✅   |      ✅     |
| [Filtering - Vector Search](/search/filtering/)    | Apply filters during vector search operations.    |  ✅  |   ✅   |      ✅     |
| [Filtering - Full Text Search](/search/filtering/) | Apply filters during full-text search operations. |  ✅  |   ✅   |      ✅     |


# Dependency Verification
Source: https://docs.lancedb.com/geneva/deployment/dependency-verification

Diagnose and resolve package version mismatches between local and Ray worker environments.

When running Geneva UDFs on Ray, your code is serialized locally and executed on remote workers. If the worker environment differs from your local environment, you may encounter subtle and difficult-to-debug errors.

## Example environment mismatch errors

| Symptom                                                            | Likely Cause                              |
| ------------------------------------------------------------------ | ----------------------------------------- |
| `TypeError: Enum.__new__() missing 1 required positional argument` | `attrs` version mismatch                  |
| `TypeError: Can't instantiate abstract class`                      | Package structure differences             |
| `ArrowInvalid: cannot cast` / serialization errors                 | NumPy 1.x vs 2.x mismatch                 |
| `ModuleNotFoundError` on workers                                   | Package only installed locally            |
| Model loading failures                                             | PyTorch version mismatch                  |
| Permission denied errors                                           | Missing API keys in envrionment variables |

These issues are notoriously difficult to debug because the error messages often don't indicate the root cause.

## The `compare_ray_environments` Tool

Geneva provides a diagnostic tool to compare your local environment against Ray workers.

If you are encountering a hang or exception you can use the following diagnosis worklflow to resolve the problem.

<Steps>
  <Step>
    **Run the diagnostic tool** programatically or via the CLI.
  </Step>

  <Step>
    **Check PACKAGES and ENV VARS output sections for mismatches**.
  </Step>

  <Step>
    **Identify critical packages**: numpy, torch, pyarrow, attrs, pydantic.
  </Step>

  <Step>
    **Identify inconsistent environment variables**: `AWS_*`,  `GOOGLE_APPLICATION_CREDENTIALS`
  </Step>

  <Step>
    **Fix with manifest** for quick testing:

    ```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
    from geneva.manifest.builder import GenevaManifestBuilder
    manifest = GenevaManifestBuilder.create("fix").pip(["numpy==1.26.4"]).build()
    ```
  </Step>

  <Step>
    **OPTIONAL: Build custom image** for production (if using KubeRay).
  </Step>
</Steps>

### Programmatic Usage

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from geneva.runners.ray.compare_env import compare_ray_environments

  # Compare and print (requires Geneva context to be initialize via `with db.context(..)`)
  result = compare_ray_environments()

  # Compare environments, filtering environment variables with specified prefix
  result = compare_ray_environments(env_prefix="PY")
  ```
</CodeGroup>

### CLI Usage

<CodeGroup>
  ```bash CLI icon="terminal" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Connect to existing Ray cluster
  python -m geneva.runners.ray.compare_env

  # Start new local Ray cluster
  python -m geneva.runners.ray.compare_env --address local

  # Filter env vars by prefix
  python -m geneva.runners.ray.compare_env --env-prefix RAY

  # Show full JSON snapshots
  python -m geneva.runners.ray.compare_env --show-all

  # Skip sys.path comparison
  python -m geneva.runners.ray.compare_env --no-sys-path
  ```
</CodeGroup>

## Understanding the Output

The tool outputs several sections to help you identify mismatches.

### PYTHON / PLATFORM

Shows Python version and OS information for both environments:

```
=== PYTHON / PLATFORM ===
Local:
  Python: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0]
  Impl  : CPython
  Exec  : /home/user/.venv/bin/python
  OS    : Linux 5.15.0-generic (x86_64)

Remote:
  Python: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0]
  Impl  : CPython
  Exec  : /home/ray/anaconda3/bin/python
  OS    : Linux 5.4.0-aws (x86_64)
```

<Warning>
  Watch for different Python versions or different OS types (macOS local vs Linux remote).
</Warning>

#### Architecture Mismatch (macOS to Linux)

If you see different OS types (e.g., `Darwin` locally vs `Linux` remotely), compiled extensions may fail with `ModuleNotFoundError` or segfaults.

**Solution**: Run Geneva from the same OS/architecture as your cluster (typically Linux x86\_64). Use a Linux VM, container, or remote development environment.

### Environment Variables

Environment variables present in only one environment:

```
=== ENV VARS: keys only in LOCAL ===
  + CONDA_PREFIX
  + VIRTUAL_ENV

=== ENV VARS: keys only in REMOTE ===
  + RAY_ADDRESS
  + KUBERNETES_SERVICE_HOST
```

<Warning>
  Missing `AWS_*` or `GOOGLE_APPLICATION_CREDENTIALS` can cause storage authentication failures.
</Warning>

#### Passing Environment Variables to Workers

If critical environment variables are missing on workers, you can pass them via the manifest or cluster configuration.

**Option 1: Via Manifest**

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from geneva.manifest.builder import GenevaManifestBuilder
  import os

  manifest = (
      GenevaManifestBuilder.create("my-manifest")
      .env({
          "AWS_ACCESS_KEY_ID": os.environ["AWS_ACCESS_KEY_ID"],
          "AWS_SECRET_ACCESS_KEY": os.environ["AWS_SECRET_ACCESS_KEY"],
          "MY_API_KEY": os.environ["MY_API_KEY"],
      })
      .build()
  )
  ```
</CodeGroup>

**Option 2: Via Cluster Configuration**

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from geneva.cluster.builder import GenevaClusterBuilder
  import os

  cluster = (
      GenevaClusterBuilder.create("my-cluster")
      .ray_init_kwargs({
          "runtime_env": {
              "env_vars": {
                  "AWS_ACCESS_KEY_ID": os.environ["AWS_ACCESS_KEY_ID"],
                  "AWS_SECRET_ACCESS_KEY": os.environ["AWS_SECRET_ACCESS_KEY"],
              }
          }
      })
      .build()
  )
  ```
</CodeGroup>

<Warning>
  Avoid hardcoding secrets. Use `os.environ` to pass values from your local environment, or use a secrets manager in production.
</Warning>

### Packages

The tool shows version mismatches and packages only present in one environment:

```
=== PACKAGES: version mismatches ===
  * numpy: local=1.26.4  remote=2.2.6
  * torch: local=2.0.1  remote=2.8.0+cpu
  * attrs: local=23.2.0  remote=24.2.0
  * pyarrow: local=14.0.1  remote=17.0.0

=== PACKAGES: only in LOCAL ===
  + my-custom-package
  + dev-tools

=== PACKAGES: only in REMOTE ===
  + kuberay-client
```

<Warning>
  Watch for major version differences (NumPy 1.x vs 2.x) and PyTorch version mismatches.
</Warning>

#### Common Package Issues

| Issue                | Symptoms                                                             | Fix                             |
| -------------------- | -------------------------------------------------------------------- | ------------------------------- |
| **NumPy 1.x vs 2.x** | `ArrowInvalid`, `ValueError: cannot convert`, serialization failures | Pin `numpy==1.26.4`             |
| **PyTorch mismatch** | Model loading failures, CUDA errors, unexpected inference results    | Pin to matching `torch` version |
| **attrs mismatch**   | `TypeError: Enum.__new__() missing 1 required positional argument`   | Pin `attrs` to local version    |
| **Missing package**  | `ModuleNotFoundError: No module named 'xyz'`                         | Add package to manifest         |

#### Fixing Package Mismatches

**Option 1: Manifest pip Dependencies**

Specify packages in a Geneva manifest for a quick fix:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from geneva.manifest.builder import GenevaManifestBuilder

  manifest = (
      GenevaManifestBuilder.create("my-manifest")
      .pip([
          "numpy==1.26.4",
          "torch==2.0.1",
          "attrs==23.2.0",
      ])
      .build()
  )

  # Then use with db.context()
  conn = geneva.connect("s3://my-bucket/my-db")
  conn.define_manifest("my-manifest", manifest)
  with conn.context(cluster="my-cluster", manifest="my-manifest"):
      conn.open_table("my-table").backfill("my-column")
  ```
</CodeGroup>

*Pros*: Quick, reusable across sessions, stored with your database.

*Cons*: Slower startup (downloads packages), may not work for complex dependencies.

**Option 2: Custom Ray Worker Image**

For KubeRay deployments, build a custom worker image:

<CodeGroup>
  ```dockerfile Dockerfile icon="docker" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Dockerfile.ray-worker
  FROM rayproject/ray:2.30.0-py311

  # Install exact versions
  RUN pip install \
      numpy==1.26.4 \
      torch==2.0.1 \
      attrs==23.2.0 \
      geneva==0.8.0

  # Copy any custom packages
  COPY ./my_udfs /app/my_udfs
  ```
</CodeGroup>

Then reference in RayCluster spec:

<CodeGroup>
  ```yaml Kubernetes icon="kubernetes" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  spec:
    workerGroupSpecs:
      - template:
          spec:
            containers:
              - image: your-registry/ray-worker:latest
  ```
</CodeGroup>

*Pros*: Fastest startup, reproducible.

*Cons*: Requires image build/push workflow.

**Option 3: Conda Environment**

Use a conda environment on workers via the cluster builder:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from geneva.cluster.builder import GenevaClusterBuilder

  cluster = (
      GenevaClusterBuilder.create("my-cluster")
      .ray_init_kwargs({
          "runtime_env": {"conda": "environment.yml"}
      })
      .build()
  )
  ```
</CodeGroup>

Or specify conda channels and dependencies inline:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  cluster = (
      GenevaClusterBuilder.create("my-cluster")
      .ray_init_kwargs({
          "runtime_env": {
              "conda": {
                  "channels": ["conda-forge"],
                  "dependencies": [
                      "python=3.10",
                      "ffmpeg<8",
                      "torchvision=0.22.1"
                  ]
              },
              "config": {"eager_install": True}
          }
      })
      .build()
  )
  ```
</CodeGroup>

*Pros*: Best for complex dependencies with native libraries (ffmpeg, CUDA).

*Cons*: Slower environment creation, requires conda on workers.

## API Reference

For detailed API documentation on the environment comparison functions, see the [Geneva Diagnostics API Reference](https://lancedb.github.io/geneva/api/diagnostics).


# Deploy Geneva using Helm
Source: https://docs.lancedb.com/geneva/deployment/helm

Learn how to deploy Geneva on Kubernetes using the Geneva Helm Chart

<Tip>
  **Feature Engineering is deployed automatically in LanceDB Enterprise**

  In self-managed environments, Geneva can be installed into existing Kubernetes clusters using Helm. Please [contact LanceDB](https://lancedb.com/contact/) for access to the Helm Chart and related resources.
</Tip>

## Pre-requisites

* An existing Kubernetes cluster
* An existing node pool(s) for Geneva workloads. By default, Geneva uses node selector
  `{"geneva.lancedb.com/ray-head": "true"}` for Ray head nodes, and
  `{"geneva.lancedb.com/ray-worker-cpu": "true"}` and `{"geneva.lancedb.com/ray-worker-gpu": "true"}`
  for Ray CPU worker and Ray GPU worker nodes respectively. This can be overridden in the Geneva client.
* Geneva Helm chart. Please [contact LanceDB](https://lancedb.com/contact/) for access to the Helm Chart and related resources.

For more information on deploying the required cloud resources, see the [manual deployment instructions](/geneva/deployment/).

## Geneva Helm Chart

The Helm chart includes resources required for running [Geneva](https://lancedb.com/docs/geneva/) in Kubernetes.

It includes services, service accounts, RBAC roles, etc. that are used by the Geneva client to manage resources.

## Install

1. Authenticate with Kubernetes cluster, i.e. update kubeconfig
2. Configure Helm chart values

In values.yaml, configure the service account, node selectors, and cloud resources, if applicable.

```
geneva:
  # Object storage root URI
  rootUri:
    value: "s3://my-data-bucket"

  serviceAccount:
    # Service account for Geneva worker pods and services
    annotations:
      # Set per-CSP annotations to provide access to CSP resources, i.e.
      # eks.amazonaws.com/role-arn: arn:aws:iam::0123456789:role/geneva_service_role
      # iam.gke.io/gcp-service-account: geneva-service-account@my-project.iam.gserviceaccount.com

  gcp:
    # GCP service account email for the Geneva client.
    # It should have access to the GKS cluster and "roles/storage.objectUser"
    # permissions on the object storage bucket.
    # e.g., geneva-client-sa@project-id.iam.gserviceaccount.com
    clientServiceAccount: ""

  aws:
    # AWS IAM role ARN to be assumed by the Geneva client.
    # This role should have an access entry to the cluster with username matching the role ARN.
    # It should also have r/w access to the object storage bucket.
    # e.g., arn:aws:iam::123456789012:role/geneva-client-role
    clientRoleArn: ""
```

3. Install kuberay operator

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
export NAMESPACE=geneva

helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
helm install kuberay-operator kuberay/kuberay-operator -n $NAMESPACE --create-namespace
```

4. Install NVIDIA device plugin (if using GPU nodes)

For GPU support, the NVIDIA device plugin must be installed in your EKS cluster:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
curl https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.17.0/deployments/static/nvidia-device-plugin.yml > nvidia-device-plugin.yml
kubectl apply -f nvidia-device-plugin.yml
```

5. Install Geneva Helm chart

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
helm install geneva ./geneva -n $NAMESPACE --create-namespace
```


# Manual Deployment on Kubernetes
Source: https://docs.lancedb.com/geneva/deployment/index

Learn how to deploy Geneva on Kubernetes using KubeRay for distributed feature engineering workflows on GKE and EKS.

<Tip>
  **Feature Engineering is deployed automatically in LanceDB Enterprise**

  Feature Engineering is deployed automatically as part of [LanceDB Enterprise](/enterprise/).
  For manual installation in self-managed environments, follow the instructions below.
</Tip>

## Prerequisites

* Kubernetes cluster with KubeRay 1.1+ operator installed
* Ray 2.43+

See below for installation instructions for:

* Amazon Web Services (AWS) Elastic Kubernetes Service (EKS)
* Google Cloud Platform (GCP) Google Kubernetes Engine (GKE)

## Basic Kubernetes Setup

<Tip>
  Kubernetes resources can be deployed automatically via [Helm](/geneva/deployment/helm/) or manually
  via the instructions below.
</Tip>

In the following sections we'll use these variables:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
NAMESPACE=geneva  # replace with your actual namespace if different
KSA_NAME=geneva-ray-runner # replace with an identity name
```

### Kubernetes Service Account (KSA)

Inside your Kubernetes cluster, you need a Kubernetes service account which provides the credentials your k8s pods (Ray) run with. Here's how to create your KSA.

#### Create a Kubernetes Service Account (KSA)

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl create namespace $NAMESPACE   # skip if it already exists

kubectl create serviceaccount $KSA_NAME \
  --namespace $NAMESPACE
```

You can verify using:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl get serviceaccounts -n $NAMESPACE $KSA_NAME
```

The Kubernetes service account (KSA) needs RBAC permissions inside the k8s cluster to provision Ray clusters via CRDs.

#### Create a k8s Role

Create a k8s role that can access the Ray CRD operations.

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ${KSA_NAME}-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["ray.io"]
  resources: ["rayclusters"]
  verbs: ["get", "patch", "delete"]
EOF
```

#### Bind the ClusterRole to Your KSA

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: ${KSA_NAME}-binding
subjects:
- kind: ServiceAccount
  name: ${KSA_NAME}
  namespace: ${NAMESPACE}
roleRef:
  kind: ClusterRole
  name: ${KSA_NAME}-role
  apiGroup: rbac.authorization.k8s.io
EOF
```

Now confirm your permissions:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl auth can-i get pods --as=system:serviceaccount:${NAMESPACE}:${KSA_NAME}
```

## Geneva on GKE

Google Kubernetes Engine (GKE) is a GCP service that deploys Kubernetes and can manage on-demand provisioning of cluster nodes. Ray can be deployed on GKE clusters using the KubeRay k8s operator.

GKE provides the option for an out-of-the-box KubeRay operator deployment. The version of KubeRay is tied to the version of GKE you have deployed. Currently these versions are supported:

* GKE 1.30 / KubeRay 1.1
* GKE 1.31 / KubeRay 1.2

Alternatively, you can also deploy your own KubeRay operator to get the latest KubeRay 1.3 version.

The following sections describe in more details other required configuration settings required for Geneva to perform distributed execution.

### GKE Node Pools

GKE allows you to specify templates for virtual machines in "node pools". These allow you to manage and configure resources such as the number of CPUs, number of GPUs, amount of memory, and if instances are spot or regular virtual machines.

You can define your node pools however you want but Geneva uses three specific Kubernetes labels when deploying Ray pods on GKE: `ray-head`, `ray-worker-cpu`, `ray-worker-gpu`

* **Head nodes** are where the Ray dashboard and scheduler run. They should be non-spot instances and should not have processing workloads scheduled on them. Geneva looks for nodes with the `geneva.lancedb.com/ray-head` k8s label for this role.

* **CPU Worker nodes** are where distributed processing that does not require GPU should be scheduled. Geneva looks for nodes with the `geneva.lancedb.com/ray-worker-cpu` k8s label when these nodes are requested.

* **GPU Worker nodes** are where distributed processing that require GPU should be scheduled. Geneva looks for nodes with the `geneva.lancedb.com/ray-worker-gpu` k8s label when these nodes are requested.

### GKE + k8s Permissions

Geneva needs the ability to deploy a KubeRay cluster and submit jobs to Ray. The workers in the Ray cluster need the ability to read and write to the Google Cloud Storage (GCS) buckets. This requires setting up the proper k8s permissions and GCP IAM grants. There are three main areas to setup and verify:

* Kubernetes Service Account (KSA)
* Google Service Account (GSA)
* GKE settings (GKE workload identity)

<img alt="geneva-security-reqs" />

#### Geneva Security Requirements

In the following sections we'll use these variables:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
NAMESPACE=geneva  # replace with your actual namespace if different
KSA_NAME=geneva-ray-runner # replace with an identity name
PROJECT_ID=...  # replace with your google cloud project name
GSA_EMAIL=${KSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
LANCEDB_URI=gs://bucket/db  # replace with your own path
```

#### Google Service Account (GSA)

To give your k8s workers the ability to read and write from your LanceDB buckets, your KSA needs to be bound to a Google Cloud service account (GSA) with those grants. With this setup, any pod using the KSA will automatically get a token that lets it impersonate the GSA.

Let's set this up:

**Create a Google Cloud Service Account**

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
gcloud iam service-accounts create ${KSA_NAME} \
  --project=${PROJECT_ID} \
  --description="Service account for ray workloads in GKE" \
  --display-name="Ray Runner GSA"
```

You can verify this using:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
gcloud iam service-accounts list --filter="displayName:Ray Runner GSA"
```

> **Warning**: You need `roles/iam.serviceAccountAdmin` or minimally `roles/iam.serviceAccountTokenCreator` rights to run these commands.

Next, you'll need to verify that your KSA is bound to your GSA and has `roles/iam.workloadIdentityUser`:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
gcloud iam service-accounts get-iam-policy $GSA_EMAIL \
  --project=$PROJECT_ID \
  --format="json" | jq '.bindings[] | select(.role=="roles/iam.workloadIdentityUser")'
```

Give your GSA rights to access the LanceDB bucket:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
gcloud storage buckets add-iam-policy-binding ${LANCEDB_URI} \
  --member="serviceAccount:${KSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"
```

#### GKE Workload Identity

A GKE workload identity is required to enable k8s workloads access Google Cloud services securely and without needing to manually manage service account keys. The workload identity is attached to Google Cloud service accounts (GSA) and mapped to a Kubernetes service account (KSA). This feature needs to be enabled on the GKE cluster.

You can confirm that your workers have abilities to read/write to the LanceDB bucket:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl run gcs-test --rm -it --image=google/cloud-sdk:slim \
  --serviceaccount=${KSA_NAME} \
  -n ${NAMESPACE} \
  -- bash

echo "hello" > test.txt
gsutil cp test.txt ${LANCEDB_URI}/demo-check/test-write.txt
```

Confirm the identity inside the pod:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
curl -H "Metadata-Flavor: Google" \
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email
```

## Geneva on AWS EKS

Geneva can be used to provision Ray clusters running in Amazon Web Services (AWS) Elastic Kubernetes Service (EKS).

In the following sections we'll use these variables:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
NAMESPACE=geneva  # replace with your actual namespace if different
CLUSTER=geneva  # replace with your actual namespace if different
KSA_NAME=geneva-ray-runner # replace with an identity name
```

### EKS Node Groups

EKS allows you to specify templates for virtual machines in "node groups". These allow you to manage and configure resources such as the number of CPUs, number of GPUs, amount of memory, and if instances are spot or regular virtual machines.

You can define your node groups however you want but Geneva uses three specific Kubernetes labels when deploying Ray pods on EKS: `ray-head`, `ray-worker-cpu`, `ray-worker-gpu`

* **Head nodes** are where the Ray dashboard and scheduler run. They should be non-spot instances and should not have processing workloads scheduled on them. Geneva looks for nodes with the `geneva.lancedb.com/ray-head: true` k8s label for this role.

* **CPU Worker nodes** are where distributed processing that does not require GPU should be scheduled. Geneva looks for nodes with the `geneva.lancedb.com/ray-worker-cpu: true` k8s label when these nodes are requested.

* **GPU Worker nodes** are where distributed processing that require GPU should be scheduled. Geneva looks for nodes with the `geneva.lancedb.com/ray-worker-gpu: true` k8s label when these nodes are requested.

### Install KubeRay Operator Using Helm

Geneva requires the KubeRay operator to be installed in your EKS cluster.

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
helm install kuberay-operator kuberay/kuberay-operator -n $NAMESPACE
```

### Install NVIDIA Device Plugin

For GPU support, the NVIDIA device plugin must be installed in your EKS cluster:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
curl https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.17.0/deployments/static/nvidia-device-plugin.yml > nvidia-device-plugin.yml
kubectl apply -f nvidia-device-plugin.yml
```

### Configure Access Control

<img alt="eks-auth" />

#### Environment IAM Principal

Geneva must be run in an environment with access to [AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) with permissions to `sts:AssumeRole` on the Geneva Client IAM Role.

For example, this could be a laptop with credentials provided by environment variables, or an EC2 instance with credentials provided via Instance Profile.

#### Create IAM Role for Geneva Client

The Geneva Client IAM Role is assumed by the Geneva client to provision the Kuberay cluster and run remote jobs.

This role requires IAM permissions to access the storage bucket and Kubernetes API.

Create an IAM role with the following policy:

```json theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "ClusterAccess",
        "Action": [
            "eks:DescribeCluster",
            "eks:AccessKubernetesApi"
        ],
        "Effect": "Allow",
        "Resource": "<your eks cluster arn>"
      },
      {
        "Sid": "AllowListBucket",
        "Effect": "Allow",
        "Action": [
          "s3:ListBucket"
        ],
        "Resource": "arn:aws:s3:::<your storage bucket>"
      },
      {
        "Sid": "AllowAllS3ObjectActions",
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:HeadObject"
        ],
        "Resource": "arn:aws:s3:::<your storage bucket>/*"
      }
    ]
}
```

This role should also have a trust policy with `sts:AssumeRole` permissions for any principal initiating the Geneva client.

When using Geneva, this role can be specified with the `role_name` RayCluster parameter.

#### Create EKS Access Entry

Create an [EKS access entry](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) to allow the Geneva Client Role to access the Kubernetes API for the EKS Cluster.

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
aws eks create-access-entry --cluster-name $CLUSTER --principal-arn <your geneva client role ARN> --type STANDARD
aws eks associate-access-policy --cluster-name $CLUSTER --principal-arn <your geneva client role ARN> --access-scope type=cluster --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy
```

#### Create EKS OIDC Provider

Create an OIDC provider for your EKS cluster. This is required to allow Kubernetes Service Accounts (KSA) to assume IAM roles. See [AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html#_create_oidc_provider_console).

#### Create IAM Role for Service Account

An IAM role is required for the Kubernetes Service Account (KSA) that will be used by the Ray head and worker pods.

This role must have permissions to access the storage bucket and to describe the EKS cluster:

```json theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "ClusterAccess",
        "Action": [
            "eks:DescribeCluster"
        ],
        "Effect": "Allow",
        "Resource": "<your eks cluster arn>"
      },
      {
        "Sid": "AllowListBucket",
        "Effect": "Allow",
        "Action": [
          "s3:ListBucket"
        ],
        "Resource": "arn:aws:s3:::<your storage bucket>"
      },
      {
        "Sid": "AllowAllS3ObjectActions",
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:HeadObject"
        ],
        "Resource": "arn:aws:s3:::<your storage bucket>/*"
      }
    ]
}
```

In addition, it must have a trust policy allowing the EKS OIDC provider to assume the role from the Kubernetes Service Account:

```json theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "<OIDC Provider ARN>"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "<OIDC Provider>:aud": "sts.amazonaws.com",
                    "<OIDC Provider>:sub": "system:serviceaccount:$NAMESPACE:$KSA_NAME"
                }
            }
        }
    ]
}
```

#### Associate the IAM Role with the Kubernetes Service Account

Modify the Kubernetes Service Account created in "Basic Kubernetes setup" to associate it with the IAM role created above.

The role ARN is specified using `eks.amazonaws.com/role-arn` annotation:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl annotate serviceaccount "$KSA_NAME" \
  -n "$NAMESPACE" \
  "eks.amazonaws.com/role-arn=$ROLE_ARN" \
  --overwrite
```

### Initialize the Ray Cluster

Initialize the Ray cluster using the node selectors and metadata from above:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from geneva.runners.ray._mgr import ray_cluster
from geneva.runners.ray.raycluster import (K8sConfigMethod, _HeadGroupSpec, _WorkerGroupSpec)

head_spec = _HeadGroupSpec(
    service_account="geneva-ray-runner",
    num_cpus=1,
    memory=2048,
    node_selector={"geneva.lancedb.com/ray-head": "true"},
)

worker_spec = _WorkerGroupSpec(
    name="worker",
    min_replicas=1,
    service_account="geneva-ray-runner",
    num_cpus=2,
    memory=4096,
    node_selector={"geneva.lancedb.com/ray-worker-cpu": "true"},
)

with ray_cluster(
    name="my-ray-cluster",
    namespace="geneva",
    cluster_name="geneva",
    config_method=K8sConfigMethod.EKS_AUTH,
    region="us-east-1",
    use_portforwarding=True,
    head_group=head_spec,
    worker_groups=[worker_spec],
    role_name="geneva-client-role",
) as cluster:
    table.backfill("embedding")
```


# Troubleshooting Geneva Deployments
Source: https://docs.lancedb.com/geneva/deployment/troubleshooting

Learn how to diagnose and resolve common issues with Geneva deployments, including version compatibility, permissions, and serialization errors.

We'll cover common problems you may encounter when using Geneva and troubleshooting tips to solve them.

## Common Issues to Verify

Here are some areas to verify to identify the source of problems with your Geneva deployment:

* **Versions compatibility** (Ray, Python, Lance)
* **Remote Ray execution** and hardware resource availability
* **Sufficient permissions** to access data
* **Worker code** only returns serializable values (no open files, no GPU resident buffers)

## Confirming Dependency Versions

Geneva uses Ray for distributed execution. Ray requires the version deployed cluster services and clients to be exactly the same. Minor versions of Python must match both on client and cluster services (e.g. 3.10.3 and 3.10.5 are ok, but 3.10.3 and 3.12.1 are not.)

Geneva has been tested with Ray 2.44+ and Python 3.10.x and 3.12.x.

You can run this code in your notebook to verify your environment matches your expectations:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  !python --version
  !pip show lancedb  # need 0.22.0b0+
  !echo $VIRTUAL_ENV
  ```
</CodeGroup>

## Confirming Remote Ray Execution

Geneva allows you to specify the resources of your worker nodes. You can verify that your cluster has the resources (e.g. GPUs) available for your jobs and that remote execution is working properly.

You can get some basic information about resources available to your Ray:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  print(ray.available_resources())
  ```
</CodeGroup>

You can verify basic remote execution via Ray:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  @ray.remote
  def check_remote():
    return "Hello from a worker"

  print(ray.get(check_remote.remote()))
  ```
</CodeGroup>

You can also verify that versions of specific libraries are present in the execution environment:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # does ray have cuda?
  @ray.remote
  def check_pyarrow():
      import pyarrow
      return pyarrow.__version__

  print(ray.get(check_pyarrow.remote()))
  ```
</CodeGroup>

> **Note**: You should execute Geneva code from a machine or VM that has the same architecture and OS type as the nodes in your cluster. This will allow for shared libraries to be shipped. For example, if you use a Mac to host a Jupyter notebook, Geneva will push Mac libraries to your Linux cluster and likely result in module not found errors due to OS/architecture differences.

For GPU-dependent UDFs and jobs, you can verify that GPU worker nodes have the CUDA library:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # does ray have cuda?
  @ray.remote(num_gpus=1)
  def check_cuda():
      import torch
      return torch.version.cuda, torch.cuda.is_available()

  print(ray.get(check_cuda.remote()))
  ```
</CodeGroup>

## Confirming Sufficient Permissions

While your notebook or working environment may have credentials to read and write to particular buckets, your jobs need sufficient rights to read and write to them as well. Adding `import geneva` to any remote function can help verify that your workers have sufficient grants.

Here we add `import geneva` to help trigger potential permissions problems:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  @ray.remote(num_gpus=1)
  def check_cuda():
      import geneva # this is currently required before other imports
      import torch
      return torch.version.cuda, torch.cuda.is_available()

  print(ray.get(check_cuda.remote()))
  ```
</CodeGroup>

### GCE Permissions Errors in Job Logs

If you are using Geneva managed Ray deployed on GKE, the errors may look like this:

```
PermissionError: [Errno 13] google::cloud::Status(PERMISSION_DENIED: Permanent error, with a last message of Caller does not have storage.objects.get access to the Google Cloud Storage object. Permission 'storage.objects.get' denied on resource (or it may not exist). error_info={reason=forbidden, domain=global, metadata={gcloud-cpp.retry.function=GetObjectMetadata, gcloud-cpp.retry.reason=permanent-error, gcloud-cpp.retry.original-message=Caller does not have storage.objects.get access to the Google Cloud Storage object. Permission 'storage.objects.get' denied on resource (or it may not exist)., http_status_code=403}}). Detail: [errno 13] Permission denied
```

This indicates that your workers and/or head node are not being run with the correct service account or with an account that has sufficient access. Please double check the service account's accesses and make sure to add your service account that has access to the buckets as a parameter to your Head and Worker specs. See `service_account="geneva-integ-test"` below:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  raycluster = ray_cluster(
      name= k8s_name,
      namespace=k8s_namespace,
      use_portforwarding=True,
      head_group=_HeadGroupSpec(
          num_cpus=8,
          service_account="geneva-integ-test"
      ),
      worker_groups=[
          _WorkerGroupSpec(
              name="cpu",
              num_cpus=60,
              memory="120G",
              service_account="geneva-integ-test",
          ),
          _WorkerGroupSpec(
              name="gpu",
              num_cpus=8,
              memory="32G",
              num_gpus=1,
              service_account="geneva-integ-test",
          ),
      ],
  )
  ```
</CodeGroup>

## Serialization Errors

Serialization is a critical subsystem of Geneva. In order to store UDFs and perform distributed execution, both code and data must be serializable. Errors in this area can be subtle and difficult to find.

There are a few basic rules:

1. **Python objects** passed to distributed processes or written to LanceDB must be able to be pickled or unpickled using the Python pickle or cloudpickle library.
2. **Python code** used for distributed execution, including UDFs used to calculate values written to columns must be able to be pickled or unpickled using the Python pickle or cloudpickle library.
3. **Python code or objects** need to have the same encoding and representation on the client-side and the server-side.

Below is a list of error categories and examples and how to fix them.

### Serialization Library Mismatches

Any Python code and objects must be able to be serialized by the client and deserialized on the server side, and vice versa. This includes objects that are generated on the fly such as those using the `attrs` library.

The distributed processing engine Geneva uses, Ray, also depends on the `attrs` library. Different versions may create different object signatures that are not compatible when shipped from client-side to server-side and vice versa. This means you'll need to have compatible versions of this library on both sides.

Here's an example error message. It is subtle and does not directly point to the `attrs` library:

```
...
  File "/home/runner/work/geneva/geneva/.venv/lib/python3.12/site-packages/ray/util/client/common.py", line 414, in _prepare_client_task
    self._ensure_ref()
  File "/home/runner/work/geneva/geneva/.venv/lib/python3.12/site-packages/ray/util/client/common.py", line 384, in _ensure_ref
    self._ref = ray.worker._put_pickled(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/geneva/geneva/.venv/lib/python3.12/site-packages/ray/util/client/worker.py", line 509, in _put_pickled
    raise cloudpickle.loads(resp.error)
TypeError: Enum.__new__() missing 1 required positional argument: 'value'
```

This was solved by updating the `attrs` module on the client side to use the same version found on the server side.

### Objects with Unserializable Elements

Python objects may have internal references to unpickleable objects such as open file handles or open network clients with machine specific state. There are two strategies here:

1. **Remove the reference** to unpickleable objects.
2. **Keep objects with unserializable state** only on the client or only on the server. This could be moving clients into the UDF function, or converting objects into serializable versions before transmitting them.

For example, creating clients or opening files must be inside the UDF. You may see pickling-related errors like this:

```
...
raise PicklingError(
_pickle.PicklingError: Pickling client objects is explicitly not supported.
Clients have non-trivial state that is local and unpickleable.
```

Geneva pulls in your UDFs so they can be sent to remote worker nodes. For the method to be sent, the data must be "pickleable".

**So instead of this:**

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from google.cloud import storage
  storage_client = storage.Client() # this has unpickleable state
  bucket = storage_client.bucket(BUCKET_NAME) # this has a reference to storage_client
  ...

  @udf
  def udf_function(...)
    ...
    blob = bucket.blob(video_path) # the udf's closure captures the unpickleable storage_client
    ...
  ```
</CodeGroup>

**Do this:**

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from google.cloud import storage

  # ...

  @udf
  def udf_function(...)
    # ...
    storage_client = storage.Client() # this has unpickleable state
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(video_path) # blob is bytes and is pickleable so is safe
    # ...
  ```
</CodeGroup>

### Disconnect or Serialization Errors with GPU Dependent UDFs

When using GPU code, the typical process loads some values and tensors from CPU memory to GPU memory. Even after moving data (`data.cpu().tolist()`), there may be references to GPU memory. While this is not a problem with local execution, when doing a distributed job it may cause problems because the GPU references are not serializable and not needed. You must take steps to eliminate references to structures in GPU memory since they cannot be serialized and sent between workers. This can be achieved by explicitly disconnecting references to the GPU memory (`data.cpu().detach().tolist()`) to get only-CPU resident fully serializable objects.

Here are some typical error messages:

```
Exception in thread Thread-27 (_proxy):
Traceback (most recent call last):
  File "/home/jon/.pyenv/versions/3.10.16/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/home/jon/proj/geneva-deepseek-vl2/.venv/lib/python3.10/site-packages/ipykernel/ipkernel.py", line 772, in run_closure
    _threading_Thread_run(self)
  File "/home/jon/.pyenv/versions/3.10.16/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/home/jon/proj/geneva-deepseek-vl2/src/geneva/runners/ray/_portforward.py", line 172, in _proxy
    {s1: s2, s2: s1}[s].sendall(data)
BrokenPipeError: [Errno 32] Broken pipe
Log channel is reconnecting. Logs produced while the connection was down can be found on the head node of the cluster in `ray_client_server_[port].out`
2025-04-11 02:25:21 INFO Starting proxy from pod to client
2025-04-11 02:25:21 INFO Proxy started
2025-04-11 02:25:21 INFO Proxying between <kubernetes.stream.ws_client.PortForward._Port._Socket object at 0x70b2bf9033a0> and <socket.socket fd=230, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 59979), raddr=('127.0.0.1', 32956)>
2025-04-11 02:25:21 INFO Waiting for client connection
2025-04-11 02:25:21,828 ERROR dataclient.py:330 -- Unrecoverable error in data channel.
---------------------------------------------------------------------------
...

File ~/proj/geneva-deepseek-vl2/.venv/lib/python3.10/site-packages/grpc/_channel.py:1006, in _end_unary_response_blocking(state, call, with_call, deadline)
   1004         return state.response
   1005 else:
-> 1006     raise _InactiveRpcError(state)

_InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
    status = StatusCode.NOT_FOUND
    details = "Failed to serialize response!"
    debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2025-04-11T02:25:22.209209484+00:00", grpc_status:5, grpc_message:"Failed to serialize response!"}"
>

Unexpected exception:
Traceback (most recent call last):
  File "/home/jon/proj/geneva-deepseek-vl2/.venv/lib/python3.10/site-packages/ray/util/client/logsclient.py", line 67, in _log_main
    for record in log_stream:
  File "/home/jon/proj/geneva-deepseek-vl2/.venv/lib/python3.10/site-packages/grpc/_channel.py", line 543, in __next__
    return self._next()
  File "/home/jon/proj/geneva-deepseek-vl2/.venv/lib/python3.10/site-packages/grpc/_channel.py", line 969, in _next
    raise self
grpc._channel._MultiThreadedRendezvous: <_MultiThreadedRendezvous of RPC that terminated with:
    status = StatusCode.NOT_FOUND
    details = "Logstream proxy failed to connect. Channel for client bd854100340640fb8b5770d2bf173197 not found."
    debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"Logstream proxy failed to connect. Channel for client bd854100340640fb8b5770d2bf173197 not found.", grpc_status:5, created_time:"2025-04-11T02:25:32.223710374+00:00"}"
>
```


# Multimodal Feature Engineering with Geneva
Source: https://docs.lancedb.com/geneva/index

Learn how to do multimodal feature engineering in LanceDB Enterprise to transform raw data into meaningful features for AI models.

<Badge>Enterprise-only</Badge>

When working with multimodal data at scale, [LanceDB Enterprise](/enterprise) makes it easy
to define, extract, and transform raw data into useful information and features for your
AI applications. LanceDB Enterprise's *Multimodal Feature Engineering* package is designed to improve
the productivity of AI engineers operating at immense scale.

With an API designed to leverage LanceDB's optimized data storage and retrieval, it
streamlines prototyping extraction and transformation tasks, performing experiments, exploring your
data, scaling up execution, and moving to production.

<Card>
  Feature Engineering and the `geneva` Python package are currently only available as part of
  [LanceDB Enterprise](/enterprise). Please [contact us](mailto:contact@lancedb.com) if you're interested
  in scaling up your feature engineering workloads for your AI and multimodal use cases.
</Card>

The `geneva` package uses Python [User Defined Functions (UDFs)](/geneva/udfs/) to define features
as columns in a Lance dataset. Adding a feature is straightforward:

<Steps>
  <Step>
    Prototype your Python function in your favorite environment.
  </Step>

  <Step>
    Wrap the function with a small UDF decorator (see [UDFs](/geneva/udfs/)).
  </Step>

  <Step>
    Register the UDF as a virtual column using `Table.add_columns()`.
  </Step>

  <Step>
    Trigger a `backfill` operation (see [Backfilling](/geneva/jobs/backfilling/)).
  </Step>
</Steps>

<Tip>
  You can build your Python feature generator function in an IDE or a notebook using your project's Python versions and dependencies. `geneva` will automate much of the dependency and version management needed to move from prototype to scale and production.
</Tip>

## Continue learning

Visit the following pages to learn more about featuring engineering in LanceDB Enterprise:

* **Overview**: [What is Feature Engineering?](/geneva/overview/)
* **UDFs**: [Using UDFs](/geneva/udfs/) · [Blob helpers](/geneva/udfs/blobs/) · [Error handling](/geneva/udfs/error_handling) · [Advanced configuration](/geneva/udfs/advanced-configuration)
* **Jobs**: [Backfilling](/geneva/jobs/backfilling/) · [Startup optimizations](/geneva/jobs/startup/) · [Materialized views](/geneva/jobs/materialized-views/) · [Execution contexts](/geneva/jobs/contexts/) · [Geneva console](/geneva/jobs/console) · [Performance](/geneva/jobs/performance/)
* **Deployment**: [Deployment overview](/geneva/deployment/) · [Helm deployment](/geneva/deployment/helm/) · [Troubleshooting](/geneva/deployment/troubleshooting/)


# Backfilling
Source: https://docs.lancedb.com/geneva/jobs/backfilling

Learn how to trigger backfill operations to populate column values in your LanceDB table using Geneva's distributed framework.

## Triggering Backfill

Triggering backfill creates a distributed job to run the UDF and populate the column values in your LanceDB table. The Geneva framework simplifies several aspects of distributed execution.

**Checkpoints**: Each batch of UDF execution is checkpointed so that partial results are not lost in case of job failures. Jobs can resume and avoid most of the expense of having to recalculate values.

## Adaptive checkpoint sizing

Geneva can automatically adjust checkpoint sizes during a backfill. It starts with small checkpoints (faster proof-of-life) and grows them as it observes stable throughput, while staying within safe bounds. Planning still uses your configured checkpoint size (`checkpoint_size`), but the actual checkpoint chunks can be smaller when adaptive sizing is enabled.

Adaptive sizing is always clamped to bounds:

* `max_checkpoint_size`: Upper bound. Defaults to the job's checkpoint size (`checkpoint_size`) and is capped at that value if you set a larger max.
* `min_checkpoint_size`: Lower bound. Defaults to 1.

When `min_checkpoint_size == max_checkpoint_size`, adaptive sizing is disabled and checkpoints are fixed-size.

You can set adaptive bounds in two places:

* On the UDF definition via `@udf(..., min_checkpoint_size=..., max_checkpoint_size=...)`
* On the backfill call via `table.backfill(..., min_checkpoint_size=..., max_checkpoint_size=...)`

Backfill-level values take precedence over UDF defaults.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  @udf(min_checkpoint_size=25, max_checkpoint_size=200)
  def embed_udf(text):
      ...

  # Override the UDF defaults for this run
  tbl.backfill("embedding", min_checkpoint_size=10, max_checkpoint_size=100)
  ```
</CodeGroup>

## Managing concurrency

One way to speed up the execution of a job to give it more resources and to have it work in parallel.  There are a few settings you can use on the backfill command to tune this.

* process-level `concurrency`
* thread-level `intra_applier_concurrency`

Process level concurrency can be set with the `concurrency` parameter.  This lets you specify the number of processes calculating values using the UDF.  The default is 8 and should be set to the number of GPUs you would like to dedicate to your job.  This can also be used based on CPU constraints.  So if you have 40 machines with 4 GPUs each, you could set ths value to 160.  If you set the value higher than the resources available, Geneva will try to schedule as much of the resources as it can (and potentially auto-scale to get more resources).

Thread level concurrency can be set with the `intra_applier_concurrency` parameter.  This lets you specify the number of threads in each process is calculating values using the UDF.  The default is 1.  If you have CPU heavy jobs this may be the best setting to tweak to get more utilization out of your systems. If you set the value higher than the resources available, Geneva will try to schedule as much of the resources as it can get.

The two settings can be used in combination.  So if your UDF requires 1 CPU and you set `concurrency` to 10 and `intra_applier_concurrency` to 5, you will potentially have 50 instances of the UDFs running in parallel.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # backfill embeddings with 10 * 5 = 50 instances
  tbl.backfill("embedding", concurrency=10, intra_applier_concurrency=5)
  ```
</CodeGroup>

## Managing commit visibility

Feature engineering jobs at scale can take days to complete.  Two settings can help you present progress to other readers incrementally.

* Limit the number of rows processed with `num_frags`
* Perform intermediate commits with `commit_granularity`

The `num_frags` parameter lets you limit the number of fragments processed before the job is considered complete.  If you have a table with 1000 fragments, you could set `num_frags` to 1 to see how your UDF performs and if to validate the values generated.  You can then later run with a larger `num_frags` value or without the `num_frags` setting to complete the backfill.  Any fragments prevoiusly computed are not computed again.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # only backfill 2 fragments so experiement can be done on the sample
  tbl.backfill("embedding", num_frags=2)
  ```
</CodeGroup>

The `commit_granularity` parameter lets you specify how many fragments need to be ready to commit before a intermediate commit occurs and makes partial results visible to other readers.  So for our example with a table of 1000 fragments, you can set `commit_granularity` to 10 to see progress updates every 10 fragments.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # backfill all fragments and perform an intermediate commit every 10 fragments to expose incremental results.
  tbl.backfill("embedding", commit_granularity=10)
  ```
</CodeGroup>

## Filtered Backfills

Geneva allows you to specify SQL-style filters on the backfill operation. This lets you to apply backfills to a specified subset of the table's rows.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # only backfill video content whose filenames start with 'a'
  tbl.backfill("content", where="starts_with(filename, 'a')")
  # only backfill embeddings of only those videos with content
  tbl.backfill("embedding", where="content is not null")
  ```
</CodeGroup>

Geneva also allows you to incrementally add more rows or have jobs that just update rows that were previously skipped.

If new rows are added, we can run the same command and the new rows that meet the criteria will be updated.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # only backfill video content whose filenames start with 'a'
  tbl.backfill("content", where="starts_with(filename, 'a')")
  # only backfill embeddings of only those videos with content
  tbl.backfill("embedding", where="content is not null")
  ```
</CodeGroup>

Or, you can use filters to add in or overwrite content in rows previously backfilled.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # only backfill video content whose filenames start with 'a' or 'b' but only if content not pulled previously
  tbl.backfill("content", where="(starts_with(filename, 'a') or starts_with(filename, 'b')) and content is null")
  # only backfill embeddings of only those videos with content and no prevoius embeddings
  tbl.backfill("embedding", where="content is not null and embeddding is not null")
  ```
</CodeGroup>

Reference:

* [`backfill` API](https://lancedb.github.io/geneva/api/table/#geneva.table.Table.backfill)
* [`backfill_async` API](https://lancedb.github.io/geneva/api/table/#geneva.table.Table.backfill_async)


# Backfill Conflicts
Source: https://docs.lancedb.com/geneva/jobs/conflicts

Learn how Geneva handles conflicts during backfill operations and what to do when they occur.

## Overview

Geneva backfills operate on a **point-in-time snapshot** of your table. When other operations modify the table during or between backfills, conflicts can occur. Geneva >=0.9.0 automatically handles most conflict scenarios, reducing unnecessary recomputation and enabling graceful recovery.

## Safe Operations During Backfill

These operations can safely run while a backfill is in progress:

| Operation                              | Why It's Safe                                         |
| -------------------------------------- | ----------------------------------------------------- |
| `merge_insert` (Insert-only)           | Creates new fragments without modifying existing ones |
| `add()` / append data                  | Creates new fragments without modifying existing ones |
| Read operations (`search`, `to_arrow`) | Read-only, no fragment modification                   |
| Adding new columns                     | Schema change only, no fragment rewrite               |

## Operations That Cause Conflicts

These operations can conflict with running backfills:

| Operation                        | What Happens                                                |
| -------------------------------- | ----------------------------------------------------------- |
| `compact_files()` / `optimize()` | Reorganizes fragments, invalidating the backfill's snapshot |
| `merge_insert` with updates      | Modifies existing rows, causing fragment conflicts          |
| `delete()`                       | Modifies existing fragments                                 |

<Warning>
  When a conflict occurs, affected fragments fail gracefully. The backfill completes what it can, and you can re-run it to process the remaining rows.
</Warning>

## How Geneva Handles Conflicts

### Concurrent Backfills on Different Columns

When multiple backfills run on the same table but different columns, Geneva handles version conflicts automatically:

1. Each backfill writes to different column files (field IDs)
2. If a commit conflict occurs, Geneva retries at the latest version
3. The retry merges the new column data without overwriting other columns

This is controlled by the `GENEVA_VERSION_CONFLICT_MAX_RETRIES` environment variable (default: 10). See [Advanced Configuration](/geneva/udfs/advanced-configuration) for details.

### Compaction Between Backfills

When you run compaction between backfills (not during), Geneva handles it efficiently:

| Scenario                                         | Behavior                                                    |
| ------------------------------------------------ | ----------------------------------------------------------- |
| Backfill, compact, re-backfill (same UDF)        | Already-computed rows are skipped via `WHERE <col> IS NULL` |
| Partial backfill, compact, resume                | Incremental processing continues from where it left off     |
| Backfill, `alter_columns` (new UDF), re-backfill | Full reprocessing with new UDF (intentional)                |

<Note>
  Geneva's default behavior is to skip rows that already have values (`WHERE <col> IS NULL`). This means compaction doesn't cause unnecessary recomputation.
</Note>

## Recovery Steps

When a conflict occurs during a backfill:

1. **Wait** for any concurrent operations (compaction, updates) to complete
2. **Re-run** the backfill:
   ```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   tbl.backfill("column_name")
   ```
3. **Only uncomputed rows** will be processed (rows with NULL values in the target column)

Checkpoints from the previous run are preserved, so you won't lose progress on successfully computed rows.

## Best Practices

### Sequence Your Operations

For the smoothest experience, sequence your operations:

```
1. Complete all data ingestion
2. Run backfill to compute UDF columns
3. Run compaction/optimization
```

### Use Insert-Only Operations During Backfill

If you need to add data while a backfill is running, use insert-only operations:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Safe: INSERT-only merge_insert
tbl.merge_insert("id").when_not_matched_insert_all().execute(new_data)

# Unsafe: Updates to existing rows
tbl.merge_insert("id").when_matched_update_all().execute(data)  # May conflict
```

### Monitor Backfill Progress

Use async backfills to monitor progress and handle errors:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
fut = tbl.backfill_async("column_name")
while not fut.done():
    time.sleep(1)
# Check for errors before subsequent operations
result = fut.result()
```

### Disable Auto-Compaction During Large Backfills

If using LanceDB Cloud or Enterprise with auto-compaction enabled, consider disabling it during large backfill operations to avoid conflicts.

## Related

* [Backfilling](/geneva/jobs/backfilling) - Triggering and configuring backfill operations
* [Advanced Configuration](/geneva/udfs/advanced-configuration) - Environment variables for retry behavior


# Geneva Console
Source: https://docs.lancedb.com/geneva/jobs/console



The Geneva Console provides a web-based interface for monitoring and managing Geneva jobs, clusters, and manifests.

<img alt="geneva-console" />

## Why a Geneva Console?

* Collaboration: The console helps multiple people work together. Individual jobs can be run in a notebook or workflow, but to collaborate on jobs, it helps to be able to see everything that's running on a given database.
* History: See what has run in the past and diagnose any problems with your jobs.
* Shared resources: The console stores definitions of clusters and manifests, so you can easily tell what resources you want to use to run your job.

## Getting Started

The Geneva console is installed with the Geneva Helm chart; [contact LanceDB](https://lancedb.com/contact/) for access to the Helm chart).

1. Install or upgrade the Geneva Helm chart (see [Helm Deployment](/geneva/deployment/helm/)).
2. Find the pod that's running the console:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl get pods -l app.kubernetes.io/name=geneva-console -n $NAMESPACE

NAME                          READY   STATUS    RESTARTS   AGE
geneva-console-abc123-abcde   2/2     Running   0          4m58s
```

3. Forward port 3000 to access the console:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
kubectl port-forward -n $NAMESPACE geneva-console-abc123-abcde 3000:3000
```

4. Open `http://localhost:3000` in your browser. When prompted, enter your bucket and database, like:

```
s3://my-bucket/my-db
```

## What's in the Console?

### Jobs Overview

The heart of the console is an overview of all jobs that are running on a given database. See each job's status, progress, timing, and initiator.

### Job Details

Click on a job's ID to get more details, especially events that have happened in a job's life cycle, and metrics such as number of workers, rows, and fragments written.

### Clusters

See the Geneva clusters that you have defined to run jobs. Because clusters can be reused by name, this view can help you run a new job with the same resource constraints as a previous job.

### Manifests

See the Manifests you've defined and what packages/dependencies they contain. As with clusters, manifests are reusable, so it's easy to start a new job with the same dependencies as an old one by just specifying the manifest name.


# Execution Contexts
Source: https://docs.lancedb.com/geneva/jobs/contexts

Learn how Geneva automatically packages and deploys your Python execution environment to worker nodes for distributed execution.

Geneva automatically packages and deploys your Python execution environment to its worker nodes. This ensures that distributed execution occurs in the same environment and dependencies as your prototype.

We currently support one processing backend: **Ray**. There are 3 ways to connect to a Ray cluster:

1. Local Ray
2. KubeRay: create a cluster on demand in your Kubernetes cluster.
3. Existing Ray Cluster

## Ray Clusters

### Local Ray

To execute jobs without an external Ray cluster, you can just trigger the `Table.backfill` method. This will auto-create a Ray cluster on your machine. Because it's on your laptop/desktop, this is only suitable for prototyping on small datasets. But it is the easiest way to get started. Simply define the UDF, add a column, and trigger the job:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  @udf
  def filename_len(filename: str) -> int:
      return len(filename)

  tbl.add_columns({"filename_len": filename_len})
  tbl.backfill("filename_len")
  ```
</CodeGroup>

Geneva will package up your local environment and send it to each worker node, so they'll have access to all the same dependencies as if you ran a simple Python script yourself.

### KubeRay

If you have a Kubernetes cluster with kuberay-operator, you can use Geneva to automatically provision RayClusters. To do so, define a Geneva cluster, representing the resource needs, Docker images, and other Ray configurations necessary to run your job. Make sure your cluster has adequate compute resources to provision the RayCluster. Here is an example Geneva cluster definition:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import sys
  import ray
  import geneva
  from geneva.cluster.builder import GenevaClusterBuilder
  from geneva.cluster import K8sConfigMethod
  from geneva.runners.ray.raycluster import get_ray_image

  db = geneva.connect("s3://my-bucket/my-db")

  ray_version = ray.__version__
  python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
  cluster_name = "my-geneva-cluster" # lowercase, numbers, hyphens only
  service_account = "my_k8s_service_account" # k8s service account bound geneva runs as
  k8s_namespace = "geneva"  # k8s namespace

  cluster = (
      GenevaClusterBuilder()
          .name(cluster_name)
          .namespace(k8s_namespace)
          .portforwarding(True) # required for kuberay to expose ray ports
          .aws_config(region="us-east-1") # only required if using AWS
          .config_method(K8sConfigMethod.LOCAL) # Load k8s config from `~/.kube.config`
          # (other options include EKS_AUTH to load from AWS EKS, or IN_CLUSTER to load the
          # config when running inside a pod in the cluster)
          .head_group(
              service_account=service_account,
              cpus=2,
              node_selector={"geneva.lancedb.com/ray-head":""}, # k8s label required for head in your cluster
          )
          .add_cpu_worker_group(
              cpus=4,
              memory="8Gi",
              service_account=service_account,
              node_selector={"geneva.lancedb.com/ray-worker-cpu":""}, # k8s label for cpu worker in your cluster
          )
          .add_gpu_worker_group(
              cpus=2,
              memory="8Gi",
              gpus=1,
              service_account=service_account,
              image=get_ray_image(ray_version, python_version, gpu=True), # Note the GPU image here
              node_selector={"geneva.lancedb.com/ray-worker-gpu":""}, # k8s label for gpu worker in your cluster
          )
          .build()
  )

  db.define_cluster(cluster_name, cluster)
  # define_cluster stores the cluster metadata in persistent storage. The Cluster can then be referenced by name and provisioned when creating an execution context.

  table = db.get_table("my_table")
  with db.context(cluster=cluster_name):
      table.backfill("my_udf")
  ```

  See [the API docs](https://lancedb.github.io/geneva/api/cluster/) for all the parameters GenevaClusterBuilder can use.
</CodeGroup>

### External Ray cluster

If you already have a Ray cluster, Geneva can execute jobs against it too. You do so by defining a Geneva cluster which has the address of the cluster. Here's an example:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import geneva
  from geneva.cluster.builder import GenevaClusterBuilder
  from geneva.cluster import GenevaClusterType

  db = geneva.connect(my_db_uri)
  cluster_name = "my-geneva-external-cluster"

  cluster = (
      GenevaClusterBuilder()
      .name(cluster_name)
      .cluster_type(GenevaClusterType.EXTERNAL_RAY)
      .ray_address("ray://my_ip:my_port")
      .portforwarding(False) # This must be False when using an external Ray cluster
      .build()
  )
  db.define_cluster(cluster_name, cluster)

  ```
</CodeGroup>

## Dependencies

Most UDFs require some dependencies: helper libraries like `pillow` for image processing, pre-trained models like `open-clip` to calculate embeddings, or even small config files. We have two ways to get them to workers:

1. Use defaults
2. Define a manifest

### Use Defaults

By default, LanceDB packages your local environment and sends it to Ray workers. This includes your local Python `site-packages` (defined by `site.getsitepackages()`) and either the current workspace root (if you're in a python repo) or the current working directory (if you're not). If you don't explicitly define a manifest, this is what will happen.

### Define a Manifest

Sometimes you need more control over what the workers get access to. For example:

* you might need to include files from another directory, or another python package
* you might not want to send all your local dependencies (if your repo has lots of dependencies but your UDF will only need a few)
* you might need packages to be built separately for the worker's architecture (for example, you can't build `pyarrow` on a Mac and run it on a Linux Ray worker).
* you might want to reuse dependencies between two backfill jobs, so you know they are running with the same environment.

For these use cases, you can define a Manifest. Calling `define_manifest()` packages files in the local environment and stores the Manifest metadata and files in persistent storage. The Manifest can then be referenced by name, shared, and reused.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from geneva.manifest.builder import GenevaManifestBuilder

  db = geneva.connect(my_db_uri)

  manifest_name="dev-manifest"
  manifest = (
      GenevaManifestBuilder()
          .name(manifest_name)
          .skip_site_packages(False)
          .pip(["lancedb", "numpy"])
          .py_modules(["my_module"])
      ).build()

  db.define_manifest(manifest_name, manifest)
  ```
</CodeGroup>

What's in a manifest and how can you define it? (methods are all on `GenevaManifestBuilder`)

| Contents                                                         | How you can define it                                                                                                                                                                                 |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Local python packages                                            | Will be uploaded automatically, unless you set `.skip_site_packages(True)`.                                                                                                                           |
| Local working directory (or workspace root, if in a python repo) | Will be uploaded automatically.                                                                                                                                                                       |
| Python packages to be installed with `pip`                       | Use `.pip(packages: list[str])` or `.add_pip(package: str)`. See [Ray's RuntimeEnv docs](https://docs.ray.io/en/latest/ray-core/api/doc/ray.runtime_env.RuntimeEnv.html) for details.                 |
| Local python packages outside of `site_packages`                 | Use `.py_modules(modules: list[str])` or `.add_py_module(module: str)`. See [Ray's RuntimeEnv docs](https://docs.ray.io/en/latest/ray-core/api/doc/ray.runtime_env.RuntimeEnv.html) for details.      |
| Container image for head node                                    | Use `.head_image(head_image: str)` or `default_head_image()` to use the default. Note that, if the image is also defined in the GenevaCluster, the image set here in the Manifest will take priority. |
| Container image for worker nodes                                 | Use `.worker_image(worker_image: str)` or `default_worker_image()` to use the default for the current platform. As with the head image, this takes priority over any images set in the Cluster.       |

If you want to see exactly what is being uploaded to the cluster, set `.delete_local_zips(False)` and `.local_zip_output_dir(path)` then examine the zip files in `path`.

## Putting it all together: Execution Contexts

An execution context represents the concrete execution environment (Cluster and Manifest) used to execute a distributed job.

Calling `context` will enter a context manager that will provision an execution cluster and execute the Job using the Cluster and Manifest definitions provided. Because you've already defined the cluster and manifest, you can just reference them by name. Note that providing a manifest is optional. Once completed, the context manager will automatically de-provision the cluster.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  db = geneva.connect(my_db_uri)
  tbl = db.get_table("my_table")

  # Providing a manifest is optional; if not provided, it will work as described in "Use defaults" above.
  with db.context(cluster=cluster_name, manifest=manifest_name):
      tbl.backfill("embedding")
  ```
</CodeGroup>

In a notebook environment, you can manually enter and exit the context manager in multiple steps like so:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  ctx = db.context(cluster=cluster_name, manifest=manifest_name)
  ctx.__enter()__

  # ... do stuff

  ctx.__exit__(None,None,None)
  ```
</CodeGroup>


# Materialized Views with UDFs
Source: https://docs.lancedb.com/geneva/jobs/materialized-views

Learn how to use Geneva's materialized view feature to declaratively manage batch updates of expensive operations using UDFs.

Geneva provides a materialized view feature that can be used to declaratively manage "batch" updates of expensive operations such as populating UDF columns. These updates are triggered via refresh operation. This can be used to optimize data layouts for training and to simplify some operations that traditionally may require external procedural orchestration (airflow, prefect, dagster).

> **Note**: This is similar to how traditional databases offer a materialized view feature to declaratively manage expensive aggregation and join operations.

## Process Overview

The process is straightforward:

1. Define a query on table, optionally including UDFs in the select clause.
2. Create the materialized view using `db.create_materialized_view(...)`.
3. Populate the new materialized view table using the `refresh` operation.

Just like with backfills, this operation is incremental, checkpointed, and run in a distributed manner.

## Example

Let's walk through an example using a raw video table as a base. We want to create a materialized view off the table that adds transcription columns to a subset of the values.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from geneva import connect, udf
  import pyarrow as pa

  db = connect("/path/to/lancedb")
  schema = pa.schema([
      pa.field("video_id",   pa.int64(),            nullable=False),
      pa.field("video_uri",  pa.string(),           nullable=False),
      pa.field("upload_ts",  pa.timestamp("us"),    nullable=False),
      pa.field("metadata",   pa.json(),             nullable=True),
  ])
  raw_videos = db.create_table(
      "raw_videos",
      schema=schema,
      primary_key="video_id"
  )
  ```
</CodeGroup>

Here's our UDFs, and the creation of a new empty materialized view.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  @udf
  def transcribe(video_uri) -> str:
    from whisper import load_model
    model = load_model("base")
    return model.transcribe(uri)["text"]

  @udf(data_type=pa.binary())
  def load_video(video_uri: pa.Array) -> pa.Array:
      videos = <expensive stuff>
      return ...

  q = raw_videos.search(None)
      .shuffle(seed=42)
      .select(
          {
              "video_uri": "video_uri",
              "video": load_video,
              "transcription": transcribe,
          }
      )

  view_table = db.create_materialized_view("table_view", q)
  ```
</CodeGroup>

To populate the values, we call `refresh`.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # explicitly copy values from the source table, applying UDF on cols.
  db.refresh("table_view")
  ```
</CodeGroup>

Note that the UDF is stored on the destination materialized view table.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  raw_table.add(...)
  db.refresh("table_view")  # only materialize new or modified rows.
  ```
</CodeGroup>

The operation is incremental. So the next time refresh on the table is called, only new fragments with new data get materialized into the materialized view table.

Materialized views are just tables so you can query them as well as modify them by adding new `add_columns`, `backfill` particular columns and deriving other materialized views or views from them.

Reference:

* [`create_materialized_view` API](https://lancedb.github.io/geneva/api/connection/#geneva.db.Connection.create_materialized_view)

## FAQ

### Do we copy the UDFs from the source table?

No. The UDF does not but any UDF calculated values in the original table come to the materialized table via refresh. New columns defined by the UDFs in the materialized view creation are attached only to the materialized view. They can be backfilled (since the UDF belongs to the view) or refreshed.

### On MV refresh, do we force materialization of UDFs cols on the source table?

No. They are managed at the source table only. If it is null the null values are propagated. Future options may force materialization/backfill "recursively".


# Distributed Job Performance
Source: https://docs.lancedb.com/geneva/jobs/performance

Learn how to tune Geneva distributed job performance by scaling compute resources and balancing write bandwidth.

When Geneva runs in distributed mode, jobs are deployed against a kubernetes kuberay instance that dynamically provisions a Ray cluster.  Jobs execution time depends on suffcient cpu/gpu resources for *computation* and sufficient *write bandwidth* to store the output values.  Tuning the performance of a job boils down to configuring the table or cluster resources.

## Scaling computation resoures

Geneva jobs can split and schedule computational work into smalller batches that are assigned to *tasks* which are distributed across the cluster.  As each task completes, each writes its output into a checkpoint file.  If a job is interurupted or run again, Geneva will look to see if a checkpoint for the computation is already present and if not will kick off computations.

Usually computation capacity is the bottleneck for job execution.  To complete all of a job's tasks more quickly, you just need to increase the amount of CPU/GPU resources available.

### GKE node pools

GKE + kuberay can autoscale the amount of VM nodes on demand.  Limitations on the amount of resources provisioned is configured via [nodepools](https://cloud.google.com/kubernetes-engine/docs/how-to/node-pools#scale-node-pool).  Node pools can be managed to scale vertically (type of machine) or horizontally (# of nodes)

Properly applying kubernetes labels to the nodepool machines allow you to control resources for different jobs in your cluster.

### Options on `Table.backfill(..)`

The `Table.backfill(..) ` method has several optional arguments to tune performance.  To saturate the CPUs in the cluster, the main arguments to change are `concurrency` which controls the number of task processes and `intra_applier_concurrency` which controls the number of task threads per task process.

`commit_granularity` controls how frequently fragments are committed so that partical results can be come visible to table readers.

Setting `checkpoint_size` smaller introduces finer-grained checkpoints and can help provide more frequent proof of life as a job is being executed.  This is useful if the computation on your data is expensive.

Reference:

* [`backfill` API](https://lancedb.github.io/geneva/api/table/#geneva.table.Table.backfill)
* [`backfill_async` API](https://lancedb.github.io/geneva/api/table/#geneva.table.Table.backfill_async)

## Balancing write bandwidth

While computation can be broken down to small tasks, new Lance column data for each fragment must be written out in a serialized fashion.  Each fragment has a writer that waits for checkpointed results to arrive, sequences them, and then serially write out the new datafile.

Writers can be a bottleneck if a lance dataset has a small number of fragments, espcially if the amount of data being written out is comparatively large.  Maximizing parallel write throughput can be achieved by having more fragments than nodes in the cluster.

### Symptom: Computation tasks complete but writers seem to hang

Certain jobs that take a small data set and expand it may appear as if the writer has frozen.

An example is table that contains a list of URLs pointing to large media files.  This list is relatively small (\< 100MB) and can fit into a single fragment.  A UDF that downloads will fetch all the data and then attempt to write all of it out through the single writer.  This single writer then can be responsible for serially writing out 500+GB of data to a single file!

To mitigate this, you can load your initial table so that there will be multipe fragments.  Each fragment with new outputs can be written in parallel with higher write throughput.


# Job and Session Startup Optimizations
Source: https://docs.lancedb.com/geneva/jobs/startup

Learn how to optimize Geneva job and session startup times for faster interactive development and production workflows.

During interactive sessions, there are two main actions where you would interact with Geneva.

* Compute cluster creation
* Job execution

Behind the scenes, Geneva packages your python environment and auto-provisions nodes to execute the jobs.  This can be time consuming, taking on the order of 5mins to complete before any work is done.   The following sections will describe what happens in these steps and how to diagnose and speed up these interactions.

## Compute cluster creation

To execute a Geneva job, you'll need to initialize a compute environment.  Here's the basic steps Geneva takes to instantiate that cluster:

* User requests a cluster
  * Scan workspace's python path for modules
    * Generate local workspace directory zip
    * Generate python site-packages directory zip(s)
    * Generate other dirs zip (may include your .venv)
  * Upload zips
  * Provision head node
    * Initialize head node

The requests to create an environment can take 5-10 mins to initiate.  The most time-consuming steps are generating directory zips and uploading them.  AI workloads often require many module packages and can be dependent on specific versions to work.  Common modules required for GPU use to run model inferrence can easily be 5GB-10GB of compressed content.  On GCE for example, this can take \~5mins to zip all this and \~1min to upload all of this data.

To speed this up, Geneva employs caching to help optimize the startup time.  There are a few things you can do to make subsequent runs faster, often times \<1 minute:

### Hashing and Caching

Geneva generates a hash of each path in the python path that takes into account files and their last modified time.  After the first time a directory zip is created and uploaded, the cached copy is used and no new zip is generated or uploaded.  However, if there are any changes (e.g. new module added or upgraded) a new hash created and the environment's content is zipped and uploaded.

### Isolate dynamic code and modules

If you use a Jupyter notebook environment for your driver, the content of the `.ipynb` file is constantly changing.  This means the hash for the directory that contains the notebook will change, even if the subdirectories do not.  If your notebook is in your home directory, this could pull in large amounts unneeded code and data.  To avoid this you can move your notebook into a subdirectory with no children.  When your notebook is executed it is updated but only the notebook content is resent.  Other path directories are unchanged, have the same hash and can skip zip and ship.

### Package dependecies into a docker image

Geneva has an option to skip the zip and ship of the site-packages.  Enabling this assumes that the default docker image is overriden with a custom image that has the `site-package` content preloaded.

### Pre-provision nodes and pods:

In your kubernetes configuration,  you can tag specific nodes with `geneva.lancedb.com/ray-head` k8s label.  These nodes should be configured to be on non-spot instances that are always up.  This makes initial kuberay cluster creation quick.

## Job execution

A backfill or materialized view jobs triggers the provisioning of worker nodes that will perform the computations and writes.   A cold start can be slow because several steps must take place before the UDFs can be applied.  However, once nodes and pods are warmed up, the time between submission and execution can be quick.

Here's the basic steps Geneva takes to kick off a Geneva job:

* User submits job (backfill)
  * plan scans
    * provision worker nodes (vms)
      * load vm
  * Autoscale workers nodes
    * provision worker nodes (vms)
      * load vm
    * schedule ray actors
      * download docker images
      * download zips
    * execute udf
    * orchestrate fragment write.

In practice, planning the initial distributed step scans require loading vm and pod images.  With a cold start, this can take \~5 minutes.

Here are some steps you can take to pre-warming worker nodes and pods so that exectuion can be more interactive:

**Set worker spec's replicas or min\_replicas to a value >0:**  When the kuberay cluster is instantiated this also pre-provision vm's so they are ready for k8s to place pod.    replicas (for initial # of worker nodes), and minWorkers (to keep a pool for nodes always up)

**Make a warmup call:**  Making an initial request to ray will load the pod and zips content to the worker node so that subsequent startups will be fast.

**Prevent nodes from auto-scaling down:** During cluster creation, you can specifiy `idle_timeout_seconds` option  -- this is the amount of time before an node needs to be idle before it is considered for de-provisioning.


# What is Feature Engineering?
Source: https://docs.lancedb.com/geneva/overview/index

Learn how to transform raw data into meaningful features for AI models using LanceDB's feature engineering capabilities. Scale your feature engineering workflows with distributed processing and UDFs.

This section introduces the concept of feature engineering using an example of a product
recommendation system.

<iframe title="YouTube video player" />

For your AI models to work well — whether for search, recommendations, or anything else — you need good data. But raw data is usually messy and incomplete. Before you can train a model or use it for search, you have to turn that raw data into clear, meaningful features.

Feature engineering is the process of cleaning up your data and creating new signals that actually help your model learn or make better predictions. This step is just as important for preparing training data as it is for powering your AI in production.

It can take some work to get from raw data to useful features. Let's look at a simple example to see why this matters and how it's done.

## The Challenge: Manual Feature Engineering

Imagine you are building a product recommendation system for a large e-commerce platform. The goal is to find items that are genuinely "similar" to a product a user is currently viewing.

This notion of "similarity" must be sophisticated. It goes far beyond a simple text match on the product description. It needs to incorporate nuanced business concepts like popularity, value, brand equity, and key product attributes.

### Step 1: The Raw Data Table

We start with a raw data table in our data lakehouse. We'll call it `products_raw`. This table contains the basic, unprocessed information scraped from our product catalog. An embedding model could be applied directly to the `description` column for semantic search. However, that would only capture a fraction of the story.

**Table: `products_raw`**

| product\_id | title        | description                           | category | price | original\_price | review\_count | avg\_rating |
| :---------- | :----------- | :------------------------------------ | :------- | :---- | :-------------- | :------------ | :---------- |
| 101         | V-Neck Tee   | "A soft, 100% cotton v-neck shirt."   | T-Shirt  | 25.00 | 25.00           | 1200          | 4.8         |
| 102         | Designer Tee | "Limited edition organic cotton tee." | T-Shirt  | 90.00 | 150.00          | 25            | 4.9         |
| 103         | New Tee      | "A new v-neck t-shirt."               | T-Shirt  | 22.00 | 22.00           | 1             | 5.0         |

### Step 2: The Problem with Raw Data

Using this raw data to generate embeddings for a recommendation model is destined for failure. Critical business signals that define true product similarity are either misleading, hidden, or entirely absent.

* **Misleading Popularity:** The "New Tee" boasts a perfect 5.0 rating, but with only a single review. Is it truly more "popular" or "better" than the "V-Neck Tee" with 1200 reviews and a 4.8 rating? A naive model would think so. This leads to poor recommendations.
* **Missing Price Context:** The model sees a price of \$90.00 for the "Designer Tee." It has no intrinsic understanding that this represents a steep 40% discount. This is a powerful purchasing signal. The model also doesn't know how this price compares to the average price of other T-shirts.
* **Hidden Attributes:** Key attributes like "organic" or "limited edition" are buried within the free-text `description`. They are invisible to any model that doesn't perform sophisticated text analysis. Yet, they are crucial for matching user preferences.

### Step 3: Manual Feature Engineering

To address these challenges, a data scientist or ML engineer typically embarks on a manual, code-intensive journey. The goal is to extract hidden signals and craft new, meaningful features. This process often takes place in a Jupyter notebook. It involves several intricate steps.

1. **Engineer `popularity_score`:**\
   To create a more accurate measure of popularity, combine the average rating with the volume of reviews. A common approach is to use logarithmic scaling. This prevents products with massive review counts from overwhelming the score.
   ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   popularity_score = log(review_count + 1) * avg_rating
   ```

2. **Engineer `price_tier`:**\
   To help the model understand value, bucket raw prices into clear tiers such as 'budget', 'mid-range', or 'premium'.
   **Logic:**\
   Use conditional logic (for example, `CASE WHEN` in SQL or `np.select` in Python) to assign a tier based on price thresholds.

3. **Engineer `discount_pct`:**\
   To explicitly signal a "deal" to the model, calculate the discount percentage by combining the original and current prices.
   **Logic:**
   ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   discount_pct = (original_price - price) / original_price
   ```

4. **Engineer `price_vs_cat_avg`:**\
   To contextualize a product's price, compare it to the average price within its category. This requires an aggregation step to compute the average price per category. Then, calculate the feature for each product.
   **Logic:**\
   For each product:
   ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   price_vs_cat_avg = price / avg_price_for_category
   ```

5. **Engineer `is_organic`:**\
   To surface key product attributes, process the `description` text to identify important keywords.
   **Logic:**\
   Use a regular expression or string search for the keyword "organic" to create a boolean (`true`/`false`) flag.

Each of these steps requires careful data manipulation and domain knowledge. Iterative experimentation is also needed to ensure the resulting features are both accurate and useful for downstream models.

### Step 4: The Enriched Table

After executing this complex chain of logic, we produce a new, enriched table. The features in this table are more potent and ready to be fed into an embedding model. This produces high-quality vectors for our recommendation system.

**Table: `products_engineered`**

| product\_id | ... | popularity\_score | price\_tier | discount\_pct | price\_vs\_cat\_avg | is\_organic |
| :---------- | :-- | :---------------- | :---------- | :------------ | :------------------ | :---------- |
| 101         | ... | 33.6              | 'budget'    | 0.0           | 0.54                | false       |
| 102         | ... | 15.9              | 'premium'   | 0.4           | 1.95                | true        |
| 103         | ... | 3.5               | 'budget'    | 0.0           | 0.47                | false       |

## Why Use Feature Engineering?

Manual feature engineering works for small datasets. However, things change dramatically at scale. In real-world production systems, you often need to process tens or hundreds of millions of records. Sometimes this must happen in real time. The logic that was simple in a notebook, such as aggregations, conditional logic, or text processing, becomes much harder to manage and execute efficiently.

As data grows, so does complexity. You might need to generate features from new sources. These could include user behavior logs, images, or videos. This can involve running large-scale machine learning models for tasks like image captioning or text embedding. These tasks require significant compute resources and robust infrastructure.

Managing this at scale means dealing with distributed systems, scheduling, and monitoring. You must ensure that feature pipelines are reliable and reproducible. Experimenting with new features or updating existing ones can require major engineering work. This slows down iteration and innovation. Infrastructure challenges, such as orchestrating batch and streaming jobs, handling dependencies, and scaling inference, often become the main bottleneck.

In short, the biggest challenge in modern feature engineering is not just coming up with good features. It is also about building infrastructure that can handle complex, multimodal operations. The goal is to deliver fresh, high-quality features quickly and reliably at massive scale.


# Geneva Python SDK
Source: https://docs.lancedb.com/geneva/reference

LanceDB Feature Engineering Python SDK Reference

<Card title="Geneva Python SDK Reference" href="https://lancedb.github.io/geneva/">
  Refer to the Geneva Python SDK reference documentation by clicking here.
</Card>


# Advanced Configuration
Source: https://docs.lancedb.com/geneva/udfs/advanced-configuration

Learn about environment variables for configuring Geneva behavior.

Geneva supports various environment variables that start with `GENEVA_` to configure advanced behavior and fine-tune system settings.

<Tip>
  All `GENEVA_` environment variables are optional and have sensible defaults. Only set them if you need to override the default behavior.
</Tip>

## Admission Control

Admission control validates cluster resources before starting jobs to prevent failures due to insufficient resources.

| Variable                    | Default | Description                                                                                                                                         |
| --------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GENEVA_ADMISSION__CHECK`   | `true`  | Enable admission control checks. Set to `false` to skip all checks.                                                                                 |
| `GENEVA_ADMISSION__STRICT`  | `true`  | If `true`, reject the job with `ResourcesUnavailableError` when resources are insufficient. If `false`, log a warning but allow the job to proceed. |
| `GENEVA_ADMISSION__TIMEOUT` | `3.0`   | Timeout in seconds for Ray API calls during admission control checks. Prevents hanging when the cluster is in a bad state.                          |

## Commit and Retry Configuration

Control retry behavior for commits and version conflicts.

| Variable                              | Default | Description                                                                                                                                                                                                      |
| ------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GENEVA_COMMIT_MAX_RETRIES`           | `12`    | Maximum number of retries for commit operations. With exponential backoff (1s, 2s, 4s, 8s, 16s, then 16s capped), 12 retries gives \~2.5 minutes total wait time before giving up.                               |
| `GENEVA_VERSION_CONFLICT_MAX_RETRIES` | `10`    | Maximum number of retries for version conflicts during commit. Version conflicts occur when concurrent backfills commit to the same fragments. Prevents infinite loops when concurrent commits keep conflicting. |
| `GENEVA_WRITER_STALL_IDLE_ROUNDS`     | `6`     | Number of idle rounds (5s each) before considering a writer stalled during drain. With many concurrent backfills, resource contention can slow writers without them being truly stalled.                         |

## Lance Retry Configuration

This section configures retry logic for Lance I/O operations. Retries occur on `OSError`, `ValueError`, and `RuntimeError("Too many concurrent writers")` exceptions, and are retried with exponential backoff with jitter.

| Variable                          | Default | Description                                                                              |
| --------------------------------- | ------- | ---------------------------------------------------------------------------------------- |
| `GENEVA_RETRY_LANCE_ATTEMPTS`     | `7`     | Maximum number of retry attempts for Lance I/O operations.                               |
| `GENEVA_RETRY_LANCE_INITIAL_SECS` | `0.5`   | Initial wait time in seconds for exponential backoff when retrying Lance I/O operations. |
| `GENEVA_RETRY_LANCE_MAX_SECS`     | `120.0` | Maximum wait time in seconds for exponential backoff when retrying Lance I/O operations. |

## Other Configuration

| Variable                      | Default     | Description                                                                                                                                        |
| ----------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GENEVA_RAY_INIT_MAX_RETRIES` | `5`         | Maximum number of retry attempts for `ray.init()` connection failures. Useful when connecting to Ray clusters that may be temporarily unavailable. |
| `GENEVA_K8S_AUTH_MAX_RETRIES` | `3`         | Maximum number of retries for Kubernetes authentication operations. Must be at least 1.                                                            |
| `GENEVA_CONFIG_DIR`           | `./.config` | Directory path where Geneva looks for configuration files (`.yaml`, `.json`, `.toml`). Can be an absolute or relative path.                        |


# Blob Types in Geneva UDFs
Source: https://docs.lancedb.com/geneva/udfs/blobs

Learn how to work with Lance Blobs in Geneva UDFs for handling large binary objects efficiently with lazy reading capabilities.

Geneva supports UDFs that take [Lance Blobs](https://lancedb.github.io/lance/guide/blob/) (large binary objects) as input and has the ability to write out columns with binaries encoded as Lance Blobs.  Lance blobs are an optimization intended for large objects (1's MBs -> 100MB's) and provide a file-like object that lazily reads large binary objects.

## Reading Blobs

Defining functions that read blob columns is straight forward.

For scalar UDFs, blob columns are expected to be of type `BlobFile`

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lance.blob import BlobFile

  @udf
  def work_on_udf(blob: BlobFile) -> int:
      assert isinstance(blob, BlobFile)
      data = blob.read()
      # do something intresting.

      return len(data)
  ```
</CodeGroup>

## Writing Blobs

Defining UDFs that write out `Blob`s to a new column is straightforward.   Here we add the standard metadata annotation to the UDF so that Geneva knows to write out Blobs.

For scalar udfs, your udf will return `bytes`, explicitly set the `data_type` to `pa.large_binary()`, and add the `field_metadata` that specifies blob encoding.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  @udf(data_type=pa.large_binary(), field_metadata={"lance-encoding:blob": "true"})
  def generate_blob(text: str, multiplier: int) -> bytes:
      """UDF that generates blob data by repeating text."""
      return (text * multiplier).encode("utf-8")
  ```
</CodeGroup>

For `pa.RecordBatch` batched UDFs you the effort is similar:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  @udf(data_type=pa.large_binary(), field_metadata={"lance-encoding:blob": "true"})
  def batch_to_blob(batch: pa.RecordBatch) -> pa.Array:
      """UDF that converts RecordBatch rows to blob data."""
      import json

      blobs = []
      for i in range(batch.num_rows):
          # do something that returns bytes
          blob_data = ... 
          blobs.append(blob_data)
      return pa.array(blobs, type=pa.large_binary())
  ```
</CodeGroup>


# Error Handling in Geneva UDFs
Source: https://docs.lancedb.com/geneva/udfs/error_handling

Learn how configure retry, skip, and fail behaviors for UDFs.

Geneva provides three ways to handle errors, in increasing complexity: factory functions, exception matchers, and full Tenacity control.

## Quick Start: Factory Functions

Use factory functions for common error handling patterns:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from geneva import udf, retry_transient
import pyarrow as pa

@udf(data_type=pa.int32(), on_error=retry_transient())
def my_udf(x: int) -> int:
    # Will retry on network errors (ConnectionError, TimeoutError, OSError)
    return call_external_api(x)
```

Geneva provides four built-in factory functions:

| Function            | Behavior                                                                    |
| ------------------- | --------------------------------------------------------------------------- |
| `retry_transient()` | Retry `ConnectionError`, `TimeoutError`, `OSError` with exponential backoff |
| `retry_all()`       | Retry any exception with exponential backoff                                |
| `skip_on_error()`   | Return `None` for any exception (skip the row)                              |
| `fail_fast()`       | Fail immediately on any exception (default behavior)                        |

### Customizing Retry Behavior

Factory functions accept parameters to customize behavior:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from geneva import udf, retry_transient, retry_all

# Increase max attempts
@udf(data_type=pa.int32(), on_error=retry_transient(max_attempts=5))
def more_retries(x: int) -> int:
    ...

# Change backoff strategy
@udf(data_type=pa.int32(), on_error=retry_all(max_attempts=3, backoff="fixed"))
def fixed_backoff(x: int) -> int:
    ...
```

**Parameters:**

* `max_attempts` (int): Maximum number of attempts (default: 3)
* `backoff` (str): Backoff strategy between retries
  * `"exponential"` (default): 1s, 2s, 4s, 8s... with jitter, capped at 60s
  * `"fixed"`: Fixed 1s delay between attempts
  * `"linear"`: 1s, 2s, 3s, 4s... capped at 60s

## Custom Exception Handling: Matchers

For fine-grained control, use `Retry`, `Skip`, and `Fail` matchers:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from geneva import udf, Retry, Skip, Fail

@udf(
    data_type=pa.int32(),
    on_error=[
        Retry(ConnectionError, TimeoutError, max_attempts=3),
        Retry(ValueError, match="rate limit", max_attempts=5),
        Skip(ValueError),  # Other ValueErrors - skip the row
        Fail(AuthError),   # Auth failures - fail immediately
    ]
)
def custom_handling(x: int) -> int:
    ...
```

**How matching works:**

1. Matchers are evaluated in order (first match wins)
2. More specific matchers should come before general ones
3. Unmatched exceptions fail the job

### Exception Matchers

| Matcher      | Behavior                      | Parameters                         |
| ------------ | ----------------------------- | ---------------------------------- |
| `Retry(...)` | Retry with backoff, then fail | `max_attempts`, `backoff`, `match` |
| `Skip(...)`  | Return `None` for that row    | `match`                            |
| `Fail(...)`  | Fail the job immediately      | `match`                            |

**Syntax:**

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Single exception
Retry(ConnectionError)

# Multiple exceptions
Retry(ConnectionError, TimeoutError, OSError)

# With parameters
Retry(ConnectionError, max_attempts=5, backoff="fixed")

# With message matching
Retry(ValueError, match="rate limit")
```

### Message Matching

Use the `match` parameter to filter exceptions by their message content. The pattern is a regex:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from geneva import Retry, Skip

# Simple substring (works because regex matches substrings)
Retry(ValueError, match="rate limit")
# Matches: ValueError("rate limit exceeded")

# Regex pattern
Retry(ValueError, match=r"rate.?limit")
# Matches: ValueError("rate limit")
# Matches: ValueError("ratelimit")
# Matches: ValueError("rate_limit")

# Case-insensitive matching (use (?i) flag)
Retry(ValueError, match=r"(?i)rate limit")
# Matches: ValueError("Rate Limit exceeded")
# Matches: ValueError("RATE LIMIT hit")

# Regex alternation (match multiple patterns)
Retry(ValueError, match=r"429|rate.?limit|throttl")
# Matches: ValueError("Error 429")
# Matches: ValueError("rate limit exceeded")
# Matches: ValueError("Request throttled")
```

For example, using matchers to distinguish error types:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
@udf(
    data_type=pa.string(),
    on_error=[
        # Retry rate limits with more attempts
        Retry(ValueError, match="rate limit", max_attempts=10),
        # Skip invalid input
        Skip(ValueError, match="invalid"),
        # Fail on other ValueErrors
        Fail(ValueError),
    ]
)
def api_call(x: str) -> str:
    ...
```

### Behavior Summary

| Outcome   | What Happens                       | When to Use                                                |
| --------- | ---------------------------------- | ---------------------------------------------------------- |
| **Retry** | Retry with backoff, then fail/skip | Transient errors: network issues, rate limits, timeouts    |
| **Skip**  | Return `None` for that row         | Bad input data, row-specific failures, optional enrichment |
| **Fail**  | Kill the job immediately           | Fatal errors: auth failures, configuration errors          |

## Advanced: Full Tenacity Control

For power users who need custom callbacks or complex retry conditions, omit `on_error` and use `error_handling=`:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from geneva import udf
from geneva.debug.error_store import ErrorHandlingConfig, UDFRetryConfig
from tenacity import wait_random_exponential, stop_after_delay

@udf(
    data_type=pa.int32(),
    error_handling=ErrorHandlingConfig(
        retry_config=UDFRetryConfig(
            retry=my_custom_retry_condition,
            stop=stop_after_delay(300),
            wait=wait_random_exponential(min=1, max=120),
            before_sleep=my_logging_callback,
        ),
    ),
)
def power_user_udf(x: int) -> int:
    ...
```

Note: `on_error=` and `error_handling=` cannot be used together.

## Restrictions

* **Skip behavior** only works with scalar UDFs (functions that process one row at a time)
* For batch UDFs that receive `RecordBatch`, use `Retry` or `Fail` only
* **All Retry matchers must use the same backoff strategy.** You cannot mix different backoff strategies in the same `on_error` list:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
@udf(on_error=[
    Retry(ConnectionError, backoff="exponential"),
    Retry(TimeoutError, backoff="fixed"),  # Error: different backoff!
])

@udf(on_error=[
    Retry(ConnectionError, backoff="fixed"),
    Retry(TimeoutError, backoff="fixed"),  # Same backoff - OK
])
```

* **Invalid regex patterns are rejected at construction time:**

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# This will raise ValueError due to the unclosed bracket
Retry(ValueError, match=r"[invalid")  

# But this will work:
Retry(ValueError, match=r"rate.?limit")
```


# User-Defined Functions
Source: https://docs.lancedb.com/geneva/udfs/index



## Converting functions into UDFs

Converting your Python code to a Geneva UDF is simple.  There are three kinds of UDFs that you can provide — scalar UDFs, batched UDFs and stateful UDFs.

In all cases, Geneva uses Python type hints from your functions to infer the input and output
[arrow data types](https://arrow.apache.org/docs/python/api/datatypes.html) that LanceDB uses.

### Scalar UDFs

The **simplest** form is a scalar UDF, which processes one row at a time:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from geneva import udf

@udf
def area_udf(x: int, y: int) -> int:
    return x * y
```

This UDF will take the value of `x` and value of `y` from each row and return the product.  The `@udf` wrapper is all that is needed.

### Batched UDFs

For **better performance**, you can also define batch UDFs that process multiple rows at once.

You can use `pyarrow.Array`s:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import pyarrow as pa
from geneva import udf

@udf(data_type=pa.int32())
def batch_filename_len(filename: pa.Array) -> pa.Array:
    lengths = [len(str(f)) for f in filename]
    return pa.array(lengths, type=pa.int32())
```

Or take entire rows using `pyarrow.RecordBatch`:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import pyarrow as pa
from geneva import udf

@udf(data_type=pa.int32())
def recordbatch_filename_len(batch: pa.RecordBatch) -> pa.Array:
    filenames = batch["filename"] 
    lengths = [len(str(f)) for f in filenames]
    return pa.array(lengths, type=pa.int32())
```

> **Note**:  Batch UDFS require you to specify `data_type` in the `@udf` decorator for batched UDFs which defines `pyarrow.DataType` of the returned `pyarrow.Array`.

### Struct fields and list inputs

You can pass nested `struct` fields directly into a UDF by specifying `input_columns` with dot notation. For list-typed inputs, Geneva can pass a NumPy array when the argument is annotated as `np.ndarray` (use `np.ndarray | None` for nullable lists).

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import numpy as np
import pyarrow as pa
from geneva import udf

struct_type = pa.struct([("vals", pa.list_(pa.int32()))])
schema = pa.schema([pa.field("info", struct_type)])

@udf(data_type=pa.int32(), input_columns=["info.vals"])
def sum_vals(vals: np.ndarray | None) -> int | None:
    if vals is None:
        return None
    assert isinstance(vals, np.ndarray)
    return int(np.sum(vals))
```

### Stateful UDFs

You can also define a **stateful** UDF that retains its state across calls.

This can be used to share code and **parameterize your UDFs**.  In the example below, the model being used is a parameter that can be specified at UDF registration time.  It can also be used to paramterize input column names of `pa.RecordBatch` batch UDFS.

This also can be used to **optimize expensive initialization** that may require heavy resource on the distributed workers.  For example, this can be used to load an model to the GPU once for all records sent to a worker instead of once per record or per batch of records.

A stateful UDF is a `Callable` class, with `__call__()` method.  The call method can be a scalar function or a batched function.

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from typing import Callable
from openai import OpenAI

@udf(data_type=pa.list_(pa.float32(), 1536))
class OpenAIEmbedding(Callable):
    def __init__(self, model: str = "text-embedding-3-small"):
        self.model = model
        # Per-worker openai client
        self.client: OpenAI | None = None

    def __call__(self, text: str) -> pa.Array:
        if self.client is None:
            self.client = OpenAI()

        resp = self.client.embeddings.create(model=self.model, input=text)
        return pa.array(resp.data[0].embeddings)
```

> **Note**:  The state is will be independently managed on each distributed Worker.

## UDF options

The `udf` can have extra annotations that specify resource requirements and operational characteristics.
These are just add parameters to the `udf(...)`.

### Resource requirements for UDFs

Some workers may require specific resources such as gpus, cpus and certain amounts of RAM.

You can provide these requirements by adding `num_cpus`, `num_gpus`, and `memory` parameters to the UDF.

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
@udf(..., num_cpus=1, num_gpus=0.5, memory = 4 * 1024**3) # require 1 CPU, 0.5 GPU, and 4GiB RAM
def func(...):
    ...
```

### Operational parameters for UDFs

#### checkpoint\_size

`checkpoint_size` controls how many rows are processed before checkpointing, and therefore reporting and saving progress.

UDFs can be quite varied: some can be simple operations where thousands of calls can be completed per second, while others may be slow and require 30s per row. So a simple default like "every 1000 rows" might write once a second or once every 8 hours!

Geneva will handle this internally, using an experimental feature that will adapt checkpoint sizing as a UDF progresses. However, if you want to see writes more or less frequently, you can set this manually. There are three parameters:

* `checkpoint_size`: the seed for the initial checkpoint size
* `min_checkpoint_size`: the minimum value that Geneva will use while adapting checkpoint size
* `max_checkpoint_size`: the maximum value that Geneva will use while adapting checkpoint size

Therefore, to force a checkpoint size (and effectively disable adaptive batch sizing), set all three of these parameters to the same value.

### Error handling

Depending on the UDF, you may want Geneva to ignore rows that hit failures, retry, or fail the entire job. For simple cases, Geneva provides a simple parameter, `on_error`, with the following options:

| Function            | Behavior                                                                    |
| ------------------- | --------------------------------------------------------------------------- |
| `retry_transient()` | Retry `ConnectionError`, `TimeoutError`, `OSError` with exponential backoff |
| `retry_all()`       | Retry any exception with exponential backoff                                |
| `skip_on_error()`   | Return `None` for any exception (skip the row)                              |
| `fail_fast()`       | Fail immediately on any exception (default behavior)                        |

If those are not specific enough, Geneva also provides [many more error handling options](/geneva/udfs/error_handling).

## Registering Features with UDFs

Registering a feature is done by providing the `Table.add_columns()` function a new column name and the Geneva UDF.

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import geneva
import numpy as np
import pyarrow as pa

lancedb_uri="gs://bucket/db"
db = geneva.connect(lancedb_uri)

# Define schema for the video table
schema = pa.schema([
    ("filename", pa.string()),
    ("duration_sec", pa.float32()),
    ("x", pa.int32()),
    ("y", pa.int32()),
])
tbl = db.create_table("videos", schema=schema, mode="overwrite")

# Generate fake data
N = 10
data = {
    "filename": [f"video_{i}.mp4" for i in range(N)],
    "duration_sec": np.random.uniform(10, 300, size=N).astype(np.float32),
    "x": np.random.choice([640, 1280, 1920], size=N),
    "y": np.random.choice([360, 720, 1080], size=N),
    "caption": [f"this is video {i}" for i in range(N)]
}

# Convert to Arrow Table and add to LanceDB
batch = pa.table(data, schema=schema)
tbl.add(batch)
```

Here's how to register a simple UDF:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
@udf
def area_udf(x: int, y: int) -> int:
    return x * y

@udf
def download_udf(filename: str) -> bytes:
    ...

# {'new column name': <udf>, ...}
# simple_udf's arguments are `x` and `y` so the input columns are
# inferred to be columns `x` amd `y`
tbl.add_columns({"area": area_udf, "content": download_udf })
```

Batched UDFs require return type in their `udf` annotations

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
@udf(data_type=pa.int32())
def batch_filename_len(filename: pa.Array) -> pa.Array:
    ...

# {'new column name': <udf>}
# batch_filename_len's input, `filename` input column is
# specified by the UDF's argument name.
tbl.add_columns({"filename_len": batch_filename_len})
```

or

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
@udf(data_type=pa.int32())
def recordbatch_filename_len(batch: pa.RecordBatch) -> pa.Array:
    ...

# {'new column name': <udf>}
# batch_filename_len's input.  pa.RecordBatch typed UDF
# argument pulls in all the column values for each row.
tbl.add_columns({"filename_len": recordbatch_filename_len})
```

Similarly, a stateful UDF is registered by providing an instance of the Callable object.  The call method may be a per-record function or a batch function.

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
@udf(data_type=pa.list_(pa.float32(), 1536))
class OpenAIEmbedding(Callable):
    ...
    def __call__(self, text: str) -> pa.Array:
        ...

# OpenAIEmbedding's call method input is inferred to be 'text' of
# type string from the __call__'s arguments, and its output type is
# a fixed size list of float32.
tbl.add_columns({"embedding": OpenAIEmbedding()})
```

## Changing data in computed columns

Let's say you backfilled data with your UDF then you noticed that your data has some issues.  Here are a few scenarios:

1. All the values are incorrect due to a bug in the UDF.
2. Most values are correct but some values are incorrect due to a failure in UDF execution.
3. Values calculated correctly and you want to perform a second pass to fixup some of the values.

In scenario 1, you'll most likely want to replaced the UDF with a new version and recalulate all the values.  You should perform a `alter_table` and then `backfill`.

In scenario 2, you'll most likely want to re-execute `backfill` to fill in the values.  If the error is in your code (certain cases not handled), you can modify the UDF, and perform an `alter_table`, and then `backfill` with some filters.

In scenario 3, you have a few options. A) You could `alter` your UDF and include the fixup operations in the UDF.  You'd `alter_table` and then `backfill` recalculating all the values.  B) You could have a chain of computed columns -- create a new column, calculate the "fixed" up values and have your application use the new column or a combination of the original column.  This is similar to A but does not recalulate A and can incur more storage.   C) You could `update` the values in the the column with the fixed up values.  This may be expedient but also sacrifices reproducability.

The next section shows you how to change your column definition by `alter`ing the UDF.

## Altering UDFs

You now want to revise the code.  To make the change, you'd update the UDF used to compute the column using the `alter_columns` API and the updated function.  The example below replaces the definition of column `area` to use the `area_udf_v2` function.

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
table.alter_columns({"path": "area", "udf": area_udf_v2} )
```

After making this change, the existing data already in the table does not change. However, when you perform your next basic `backfill` operation, all values would be recalculated and updated. If you only wanted some rows updated, you could perform a filtered backfill, targeting the specific rows that need the new upates.

For example, this filter would only update the rows where area was currently null.

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
table.backfill("area", where="area is null")
```

Reference:

* [`alter_columns` API](https://lancedb.github.io/geneva/api/table/#geneva.table.Table.alter_columns)


# LanceDB
Source: https://docs.lancedb.com/index

Multimodal lakehouse for AI.

**LanceDB** is a [multimodal lakehouse](https://lancedb.com/blog/multimodal-lakehouse/) for
AI, built on top of [Lance](/lance), an open-source lakehouse format. Below, we list a few
ways LanceDB can help you build and scale your AI and ML workloads.

<Steps>
  <Step title="Massively scalable, fast and high-quality retrieval − without breaking the bank">
    Use LanceDB as the data + retrieval layer for production AI workloads: RAG, agents, semantic search,
    recommendation systems, and more.
    Keep multimodal data, metadata, and embeddings in the same table and query them via vector search,
    full-text search or SQL. Easily add new features (columns in your tables) as your
    application evolves, without copying existing data.
  </Step>

  <Step title="High-performance random access and data management for model training">
    Use LanceDB to curate, explore and distribute very large multimodal datasets for training and fine-tuning models.
    LanceDB comes with built-in table versioning, schema evolution, and fast random access, making it practical to do
    dataset slicing, sampling, exploratory analysis and shuffles on large, evolving corpora.
  </Step>
</Steps>

LanceDB is designed for a variety of workloads and deployment scenarios, and supports use cases
that are way beyond traditional vector search. The LanceDB suite includes three products,
all built on top of the same open-source Lance format and table abstractions.

<img alt="" />

## Use cases

* **Embedding pipelines**: Add new columns (features), create embeddings, and transform your data at
  scale. LanceDB lets you extend tables both vertically and horizontally with minimal I/O overhead.
* **Search**: Build high-performance search and retrieval applications using LanceDB's optimized storage, including vector search, full-text search, and hybrid search with secondary indexes.
* **Training**: Efficiently access and manage large-scale multimodal datasets for training and fine-tuning AI models.
* **Exploratory Data Analysis**: Analyze and search through petabyte-scale multimodal datasets, including
  video and point cloud data, to gain insights and inform model development.

## Choose how you run LanceDB

Depending on your needs, you can choose one of three ways to run LanceDB.

### LanceDB OSS

The fastest way to get started is the open-source embedded library, with client SDKs in Python, TypeScript
and Rust. Run it locally during development, then use the same data model and APIs as you scale up
and need a managed solution. Start here:

<Columns>
  <Card title="Quickstart" icon="rocket" href="/quickstart">
    Get started with LanceDB in minutes.
  </Card>

  <Card title="Basic Table Operations" icon="search" href="/tables/">
    Create tables, search vectors, and modify data in LanceDB.
  </Card>
</Columns>

### LanceDB Enterprise

[LanceDB Enterprise](/enterprise) is a distributed and managed **multimodal lakehouse** built for
search, exploratory data analysis, feature engineering, and training-oriented data access workflows
on top of the same core table abstraction. This eliminates the need for teams to build bespoke
infrastructure to manage petabyte-scale multimodal datasets.
To get started, reach out at [contact@lancedb.com](mailto:contact@lancedb.com).

<Info>
  **Built with scale, performance, and security in mind.**

  LanceDB Enterprise is designed for very large-scale, high-performance, distributed workloads in
  private deployments, and can operate under strict security requirements.
</Info>

### LanceDB Cloud

[LanceDB Cloud](/cloud) is a serverless, managed service for users who are more
focused on search use cases. You can easily create and manage projects in the Cloud UI, and
integrate via REST API or client SDKs (Python, TypeScript, Rust).

<Card title="Serverless vector search" href="https://cloud.lancedb.com">
  Sign up for LanceDB Cloud by clicking here.
</Card>


# Full-Text Search (FTS) Index
Source: https://docs.lancedb.com/indexing/fts-index

Create and tune BM25-based full-text search indexes in LanceDB.

LanceDB Cloud and Enterprise provide performant full-text search based on BM25, allowing you to incorporate keyword-based search in your retrieval solutions.

<Note>
  The `create_fts_index` API returns immediately, but index building happens asynchronously.
</Note>

## Creating FTS Indexes

### Synchronous API

Use `create_fts_index` with synchronous LanceDB connections:

Check FTS index status using the API:

### Asynchronous API

When using async connections (`connect_async`), use `create_index` with the `FTS` configuration:

<Note>
  The `create_fts_index` method is not available on `AsyncTable`. Use `create_index` with `FTS` config instead.
</Note>

## Configuration Options

### FTS Parameters

| Parameter           | Type | Default     | Description                                              |
| :------------------ | :--- | :---------- | :------------------------------------------------------- |
| `with_position`     | bool | `False`     | Store token positions (required for phrase queries)      |
| `base_tokenizer`    | str  | `"simple"`  | Text splitting method (`simple`, `whitespace`, or `raw`) |
| `language`          | str  | `"English"` | Language for stemming/stop words                         |
| `max_token_length`  | int  | `40`        | Maximum token size; longer tokens are omitted            |
| `lower_case`        | bool | `True`      | Lowercase tokens                                         |
| `stem`              | bool | `True`      | Apply stemming (`running` → `run`)                       |
| `remove_stop_words` | bool | `True`      | Drop common stop words                                   |
| `ascii_folding`     | bool | `True`      | Normalize accented characters                            |

<Note title="Key parameters">
  * `max_token_length` can filter out base64 blobs or long URLs.
  * Disabling `with_position` reduces index size but disables phrase queries.
  * `ascii_folding` helps with international text (e.g., “café” → “cafe”).
</Note>

### Phrase Query Configuration

Enable phrase queries by setting:

| Parameter           | Required Value | Purpose                                       |
| :------------------ | :------------- | :-------------------------------------------- |
| `with_position`     | `True`         | Track token positions for phrase matching     |
| `remove_stop_words` | `False`        | Preserve stop words for exact phrase matching |


# GPU-Powered Vector Indexing
Source: https://docs.lancedb.com/indexing/gpu-indexing

Accelerate IVF and HNSW index builds with GPU acceleration in LanceDB.

With LanceDB's GPU-powered vector indexing you can index very large datasets in far less time
than you could with the default CPU-based indexing. In our tests, LanceDB
is capable of indexing billions of rows in under four hours on a 1-8 GPU cluster.

<Info>
  **Automatic GPU indexing**
  <Badge>Enterprise-only</Badge>

  Automatic GPU Indexing is currently only available in [LanceDB Enterprise](/enterprise/).
  Please [contact us](mailto:contact@lancedb.com) to enable this feature for your deployment.

  The vector index is created when you call `create_index`. The backend will use GPU resources
  to build either the IVF or HNSW indexes. The system automatically selects the optimal GPU
  configuration based on your data size and available hardware.

  This process is also asynchronous by default, but you can use `wait_for_index` to convert it
  into a synchronous process by waiting until the index is built.
</Info>

## Manual GPU indexing in LanceDB OSS

You can use the Python SDK to manually create the `IVF_PQ` index on a GPU. You'll need
[PyTorch>2.0](https://pytorch.org/). Note that GPU-based indexing is currently only
supported by the synchronous SDK in LanceDB OSS.

Specify the values `cuda` or `mps` (on Apple Silicon) for the `accelerator` parameter
to enable GPU training on your device.

### GPU indexing on Linux

### GPU indexing on macOS (Apple Silicon)

## Performance considerations

* GPU memory usage scales with `num_partitions` and vector dimensions
* For optimal performance, ensure GPU memory exceeds dataset size
* Batch size is automatically tuned based on available GPU memory
* Indexing speed improves with larger batch sizes

## Troubleshooting

If you encounter the error `AssertionError: Torch not compiled with CUDA enabled`,
you need to [install PyTorch with CUDA support](https://pytorch.org/get-started/locally/).


# Indexing Data
Source: https://docs.lancedb.com/indexing/index

Optimize search performance in LanceDB using vector indexes, full-text search, and scalar indexes. Understand IVF-PQ indexing for efficient vector similarity search.

Embeddings for a given dataset are made searchable via an **index**. The index is constructed by using data structures that store the embeddings such that it's very efficient to perform scans and lookups on them.

LanceDB provides a comprehensive suite of indexing strategies to optimize query performance across diverse workloads:

* **Vector Index**: Optimized for searching high-dimensional data (like images, audio, or text embeddings) by efficiently finding the most similar vectors
* **Full-Text Search Index**: Enables fast keyword-based searches by indexing words and phrases
* **Scalar Index**: Accelerates filtering and sorting of structured numeric or categorical data (e.g., timestamps, prices)

<Tip title="Working with scalar indices">
  Scalar indices serve as a foundational optimization layer, accelerating filtering across diverse search workloads. They can be combined with:

  * Vector search (prefilter or post-filter results using metadata)
  * Full-text search (combining keyword matching with structured filters)
  * SQL scans (optimizing WHERE clauses on scalar columns)
  * Key-value lookups (enabling rapid primary key-based retrievals)
</Tip>

## Supported Index Types

LanceDB provides a comprehensive suite of indexing strategies for different data types and use cases:

| Index                | Use Case                                                                                                                                    | Description                                                                                                                                                                                                                                        |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HNSW` (Vector)      | High recall and low latency vector searches. Ideal for applications requiring fast approximate nearest neighbor queries with high accuracy. | Hierarchical Navigable Small World—a graph-based approximate nearest neighbor algorithm.<br />Distance metrics: `l2` `cosine` `dot`<br />Quantizations: `PQ` `SQ`                                                                                  |
| `IVF` (Vector)       | Large-scale vector search with configurable accuracy/speed trade-offs. Supports binary vectors with hamming distance.                       | Inverted File Index—a partition-based approximate nearest neighbor algorithm that groups similar vectors into partitions for efficient search.<br />Distance metrics: `l2` `cosine` `dot` `hamming`<br />Quantizations: `None/Flat` `PQ` `SQ` `RQ` |
| `BTree` (Scalar)     | Numeric, temporal, and string columns with mostly distinct values. Best for highly selective queries on columns with many unique values.    | Sorted index storing sorted copies of scalar columns with block headers in a btree cache. Header entries map to blocks of rows (4096 rows per block) for efficient disk reads.                                                                     |
| `Bitmap` (Scalar)    | Low-cardinality columns with few thousand or fewer distinct values. Accelerates equality and range filters.                                 | Stores a bitmap for each distinct value in the column, with one bit per row indicating presence. Memory-efficient for low-cardinality data.                                                                                                        |
| `LabelList` (Scalar) | List columns (e.g., tags, categories, keywords) requiring array containment queries.                                                        | Scalar index for `List<T>` columns using an underlying bitmap index structure to enable fast array membership lookups.                                                                                                                             |
| `FTS` (Full-text)    | String columns (e.g., title, description, content) requiring keyword-based search with BM25 ranking.                                        | Full-text search index using BM25 ranking algorithm. Tokenizes text with configurable tokenization, stemming, stop word removal, and language-specific processing.                                                                                 |

<Note>
  TypeScript currently doesn't support `IvfSq` (IVF with Scalar Quantization).
</Note>

### Quantization Types

Vector indexes can use different quantization methods to compress vectors and improve search performance:

| Quantization                | Use Case                                                                                                      | Description                                                                                                                                        |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PQ` (Product Quantization) | Default choice for most vector search scenarios. Use when you need to balance index size and recall.          | Divides vectors into subvectors and quantizes each subvector independently. Provides a good balance between compression ratio and search accuracy. |
| `SQ` (Scalar Quantization)  | Use when you need faster indexing or when vector dimensions have consistent value ranges.                     | Quantizes each dimension independently. Simpler than PQ but typically provides less compression.                                                   |
| `RQ` (RabitQ Quantization)  | Use when you need maximum compression or have specific per-dimension requirements.                            | Per-dimension quantization using a RabitQ codebook. Provides fine-grained control over compression per dimension.                                  |
| `None/Flat`                 | Use for binary vectors (with `hamming` distance) or when you need maximum recall and have sufficient storage. | No quantization—stores raw vectors. Provides the highest accuracy but requires more storage and memory.                                            |

## Understanding the IVF-PQ Index

An ANN (Approximate Nearest Neighbors) index is a data structure that represents data in a way that makes it more efficient to search and retrieve. Using an ANN index is faster, but less accurate than kNN or brute force search because, in essence, the index is a lossy representation of the data.

A key distinguishing feature of LanceDB is it uses a disk-based index: IVF-PQ, which is a variant of the Inverted File Index (IVF) that uses Product Quantization (PQ) to compress the embeddings.

LanceDB is fundamentally different from other vector databases in that it is built on top of [Lance](https://github.com/lancedb/lance), an open-source columnar data format designed for performant ML workloads and fast random access. Due to the design of Lance, LanceDB's indexing philosophy adopts a primarily *disk-based* indexing philosophy.

## IVF-PQ

IVF-PQ is a composite index that combines inverted file index (IVF) and product quantization (PQ). The implementation in LanceDB provides several parameters to fine-tune the index's size, query throughput, latency and recall, which are described later in this section.

### Product Quantization

Quantization is a compression technique used to reduce the dimensionality of an embedding to speed up search.

Product quantization (PQ) works by dividing a large, high-dimensional vector of size into equally sized subvectors. Each subvector is assigned a "reproduction value" that maps to the nearest centroid of points for that subvector. The reproduction values are then assigned to a codebook using unique IDs, which can be used to reconstruct the original vector.

<img alt="" />

It's important to remember that quantization is a *lossy process*, i.e., the reconstructed vector is not identical to the original vector. This results in a trade-off between the size of the index and the accuracy of the search results.

As an example, consider starting with 128-dimensional vector consisting of 32-bit floats. Quantizing it to an 8-bit integer vector with 4 dimensions as in the image above, we can significantly reduce memory requirements.

<Note title="Effect of quantization">
  Original: `128 × 32 = 4096` bits
  Quantized: `4 × 8 = 32` bits

  Quantization results in a **128x** reduction in memory requirements for each vector in the index, which is substantial.
</Note>

### Inverted File Index (IVF) Implementation

While PQ helps with reducing the size of the index, IVF primarily addresses search performance. The primary purpose of an inverted file index is to facilitate rapid and effective nearest neighbor search by narrowing down the search space.

In IVF, the PQ vector space is divided into *Voronoi cells*, which are essentially partitions that consist of all the points in the space that are within a threshold distance of the given region's seed point. These seed points are initialized by running K-means over the stored vectors. The centroids of K-means turn into the seed points which then each define a region. These regions are then are used to create an inverted index that correlates each centroid with a list of vectors in the space, allowing a search to be restricted to just a subset of vectors in the index.

<img alt="" />

During query time, depending on where the query lands in vector space, it may be close to the border of multiple Voronoi cells, which could make the top-k results ambiguous and span across multiple cells. To address this, the IVF-PQ introduces the `nprobe` parameter, which controls the number of Voronoi cells to search during a query. The higher the `nprobe`, the more accurate the results, but the slower the query.

<img alt="" />

## HNSW Index Implementation

Approximate Nearest Neighbor (ANN) search is a method for finding data points near a given point in a dataset, though not always the exact nearest one. HNSW is one of the most accurate and fastest Approximate Nearest Neighbour search algorithms, It's beneficial in high-dimensional spaces where finding the same nearest neighbor would be too slow and costly.

### Types of ANN Search Algorithms

Approximate Nearest Neighbor (ANN) search is a method for finding data points near a given point in a dataset, though not always the exact nearest one. HNSW is one of the most accurate and fastest Approximate Nearest Neighbour search algorithms, It's beneficial in high-dimensional spaces where finding the same nearest neighbor would be too slow and costly

There are three main types of ANN search algorithms:

* **Tree-based search algorithms**: Use a tree structure to organize and store data points.
* **Hash-based search algorithms**: Use a specialized geometric hash table to store and manage data points. These algorithms typically focus on theoretical guarantees, and don't usually perform as well as the other approaches in practice.
* **Graph-based search algorithms**: Use a graph structure to store data points, which can be a bit complex.

HNSW is a graph-based algorithm. All graph-based search algorithms rely on the idea of a k-nearest neighbor (or k-approximate nearest neighbor) graph, which we outline below.\
HNSW also combines this with the ideas behind a classic 1-dimensional search data structure: the skip list.

### Understanding k-Nearest Neighbor Graphs

The k-nearest neighbor graph actually predates its use for ANN search. Its construction is quite simple:

* Each vector in the dataset is given an associated vertex.
* Each vertex has outgoing edges to its k nearest neighbors. That is, the k closest other vertices by Euclidean distance between the two corresponding vectors. This can be thought of as a "friend list" for the vertex.
* For some applications (including nearest-neighbor search), the incoming edges are also added.

Eventually, it was realized that the following greedy search method over such a graph typically results in good approximate nearest neighbors:

* Given a query vector, start at some fixed "entry point" vertex (e.g. the approximate center node).
* Look at that vertex's neighbors. If any of them are closer to the query vector than the current vertex, then move to that vertex.
* Repeat until a local optimum is found.

The above algorithm also generalizes to e.g. top 10 approximate nearest neighbors.

Computing a k-nearest neighbor graph is actually quite slow, taking quadratic time in the dataset size. It was quickly realized that near-identical performance can be achieved using a k-approximate nearest neighbor graph. That is, instead of obtaining the k-nearest neighbors for each vertex, an approximate nearest neighbor search data structure is used to build much faster.\
In fact, another data structure is not needed: This can be done "incrementally".
That is, if you start with a k-ANN graph for n-1 vertices, you can extend it to a k-ANN graph for n vertices as well by using the graph to obtain the k-ANN for the new vertex.

One downside of k-NN and k-ANN graphs alone is that one must typically build them with a large value of k to get decent results, resulting in a large index.

### Hierarchical Navigable Small Worlds (HNSW)

HNSW builds on k-ANN in two main ways:

* Instead of getting the k-approximate nearest neighbors for a large value of k, it sparsifies the k-ANN graph using a carefully chosen "edge pruning" heuristic, allowing for the number of edges per vertex to be limited to a relatively small constant.
* The "entry point" vertex is chosen dynamically using a recursively constructed data structure on a subset of the data, similarly to a skip list.

This recursive structure can be thought of as separating into layers:

* At the bottom-most layer, an k-ANN graph on the whole dataset is present.
* At the second layer, a k-ANN graph on a fraction of the dataset (e.g. 10%) is present.
* At the Lth layer, a k-ANN graph is present. It is over a (constant) fraction (e.g. 10%) of the vectors/vertices present in the L-1th layer.

Then the greedy search routine operates as follows:

* At the top layer (using an arbitrary vertex as an entry point), use the greedy local search routine on the k-ANN graph to get an approximate nearest neighbor at that layer.
* Using the approximate nearest neighbor found in the previous layer as an entry point, find an approximate nearest neighbor in the next layer with the same method.
* Repeat until the bottom-most layer is reached. Then use the entry point to find multiple nearest neighbors (e.g. top 10).


# Quantization
Source: https://docs.lancedb.com/indexing/quantization

Learn about quantization when creating an index in LanceDB.

Quantization compresses high-dimensional float vectors into a smaller, approximate representation, where instead of storing every vector as a float32 or float64, it's stored in compressed form, without too much of a compromise in search quality.

Use quantization when:

* You have a large dataset with relatively high-dimensional vectors (512, 768, 1024+)
* Index build time and query latency matter

LanceDB currently exposes multiple quantized vector index types, including:

* `IVF_PQ` -- Inverted File index with Product Quantization (default). See the [vector indexing guide](/indexing/vector-index) for `IVF_PQ` examples.
* `IVF_RQ` -- Inverted File index with **RaBitQ** quantization (binary, 1 bit per dimension). See [below](#rabitq-quantization) for details.

`IVF_PQ` is the default indexing option in LanceDB and works well in many cases. However, in cases where more drastic compression is needed, RaBitQ is also a reasonable option.

## RaBitQ quantization

RaBitQ is a binary quantization method that represents each normalized embedding using **1 bit per dimension**, plus a couple of small corrective scalars. In practice, a 1,024-dimensional `float32` vector that would normally take 4 KB can be compressed to roughly a few hundred bytes with RaBitQ, while still maintaining reasonable recall.

### How RaBitQ works

* Embeddings are grouped around centroids (as in other IVF indexes).
* Each residual vector is normalized and mapped to the nearest vertex of a randomly rotated hypercube on the unit sphere.
* The sign pattern of that vector is stored as bits (1 bit per dimension).
* Two small corrective factors are stored:
  1. The distance from the original vector to its centroid
  2. The dot product between the normalized vector and its quantized version

Compared to `IVF_PQ`, RaBitQ:

* Avoids training expensive PQ codebooks
* Builds indexes faster and handles updates more easily
* Maintains or improves recall at high dimensionality under the same storage budget

For a deeper dive into the theory and some benchmark results, see the blog post: [LanceDB's RaBitQ Quantization for Blazing Fast Vector Search](https://lancedb.com/blog/feature-rabitq-quantization/).

### Using RaBitQ

You can create an RaBitQ-backed vector index by setting `index_type="IVF_RQ"` when calling `create_index`.
`num_bits` controls how many bits per dimension are used:

## API Reference

1 bit is the classic RaBitQ setting, but you could (at higher computational cost) set it to 2, 4 or 8 bits if you want to improve the fidelity for better precision or recall.
It's also possible to tune the number of IVF partitions in `IVF_RQ`, similar to how you would do in `IVF_PQ`.
The full list of parameters to the algorithm are listed below.

* `distance_type`: Literal\["l2", "cosine", "dot"], defaults to "l2"\
  The distance metric to use for similarity comparison. Choose "l2" for Euclidean, "cosine" for cosine similarity, or "dot" for dot product.
* `num_partitions`: Optional\[int], defaults to None\
  Number of IVF partitions (affects index build time and query accuracy). More partitions can improve recall but may increase build time.
* `num_bits`: int, defaults to 1\
  Bits per dimension for quantization (1 is standard RaBitQ). Higher values improve fidelity at the cost of more storage and computation.
* `max_iterations`: int, defaults to 50\
  Maximum number of iterations for training the quantizer. Increase for larger datasets or to improve quantization quality.
* `sample_rate`: int, defaults to 256\
  Number of samples per partition during training. Higher values may improve accuracy but increase training time.
* `target_partition_size`: Optional\[int], defaults to None\
  Target number of vectors per partition. Adjust to control partition granularity and memory usage.


# Keeping Indexes Up-to-Date with Reindexing
Source: https://docs.lancedb.com/indexing/reindexing

Learn how to keep your indexes up-to-date in LanceDB using incremental indexing, including best practices for adding new records without full reindexing.

As you add new data to your LanceDB tables, your indexes may become outdated.
Reindexing is the process of updating the index to account for new data -- this applies to either a full-text search (FTS) index or a vector index. Reindexing is an important operation to run periodically as your data grows, as it has performance implications.

As data is being added and a reindex operation is running, LanceDB will combine results from the existing index with exhaustive/flat search on the new data. This is done to ensure that you're still retrieving results over all your data, but it does come at a performance cost. The more data that you add without reindexing, the impact on latency (due to exhaustive search) can be noticeable.

Rather than dropping an existing index entirely and reindexing from scratch, LanceDB supports **incremental indexing**.

## Incremental Indexing

<Badge>OSS</Badge>

In LanceDB OSS, you can manually trigger an incremental indexing operation using the `optimize()`
method on a table. This will perform compaction, pruning and updating of the index on the specified
table.

<Badge>Cloud</Badge>
<Badge>Enterprise</Badge>

LanceDB Cloud/Enterprise support incremental reindexing through an automated background process. When new data is added to a table, the system automatically triggers a new index build. As the dataset grows, indexes are asynchronously updated in the background.

* While indexes are being rebuilt, queries use brute force methods on unindexed rows, which may temporarily increase latency. To avoid this, set `fast_search=True` to search only indexed data.
* Use `index_stats()` to view the number of unindexed rows. This will be zero when indexes are fully up-to-date.

<Tip>
  **Performance and simplicity**

  The benefit of using LanceDB Cloud & Enterprise is that they automate the reindexing process
  and operate continuously in the background, minimizing the impact on latency under high loads.
  In OSS, you must manually manage the reindexing cadence based on your data growth and performance needs.
</Tip>


# Scalar Indexes
Source: https://docs.lancedb.com/indexing/scalar-index

Learn how to use scalar indexes in LanceDB for efficient metadata filtering and query optimization.

Scalar indexes organize data by scalar attributes (e.g., numbers, categories) and enable fast filtering of vector data. They accelerate retrieval of scalar data associated with vectors, thus enhancing query performance.

LanceDB supports three types of scalar indexes:

* `BTREE`: Stores column data in sorted order for binary search. Best for columns with many unique values.
* `BITMAP`: Uses bitmaps to track value presence. Ideal for columns with few unique values (e.g., categories, tags).
* `LABEL_LIST`: Special index for `List<T>` columns supporting `array_contains_all` and `array_contains_any` queries.

## Choosing the Right Index Type

| Data Type                                                       | Filter                                    | Index Type   |
| :-------------------------------------------------------------- | :---------------------------------------- | :----------- |
| Numeric, String, Temporal                                       | `<`, `=`, `>`, `in`, `between`, `is null` | `BTREE`      |
| Boolean, numbers or strings with fewer than 1,000 unique values | `<`, `=`, `>`, `in`, `between`, `is null` | `BITMAP`     |
| List of low cardinality of numbers or strings                   | `array_has_any`, `array_has_all`          | `LABEL_LIST` |

## Scalar Index Operations

### 1. Build the Index

You can create multiple scalar indexes within a table. By default, the index will be `BTREE`, but you can always configure another type like `BITMAP`

<Note title="LanceDB Cloud and Enterprise">
  If you are using Cloud or Enterprise, the `create_scalar_index` API returns immediately, but the building of the scalar index is asynchronous. To wait until all data is fully indexed, you can specify the `wait_timeout` parameter on `create_scalar_index()` or call `wait_for_index()` on the table.
</Note>

### 2. Check Index Status

### 3. Update the Index

Updating the table data (adding, deleting, or modifying records) requires that you also update the scalar index. This can be done by calling `optimize`, which will trigger an update to the existing scalar index.

<Note title="LanceDB Cloud">
  New data added after creating the scalar index will still appear in search results if optimize is not used, but with increased latency due to a flat search on the unindexed portion. LanceDB Cloud automates the optimize process, minimizing the impact on search speed.
</Note>

### 4. Run Indexed Searches

The following scan will be faster if the column `book_id` has a scalar index:

Scalar indexes can also speed up scans containing a vector search or full text search, and a prefilter:

## Index UUID Columns

LanceDB supports scalar indexes on UUID columns (stored as `FixedSizeBinary(16)`), enabling efficient lookups and filtering on UUID-based primary keys.

<Note>
  **To use `FixedSizeBinary`, ensure you have:**

  * Python SDK version `0.22.0` or later
  * TypeScript SDK version `0.19.0` or later
</Note>

### 1. Define UUID Type

### 2. Generate UUID Data

### 3. Create Table with UUID Column

### 4. Create and Wait for the Index

### 5. Perform Operations with the UUID Index


# Vector Indexes
Source: https://docs.lancedb.com/indexing/vector-index

Build and optimize vector indexes in LanceDB using IVF-PQ, HNSW, and binary indexes.

LanceDB offers two main vector indexing algorithms: **Inverted File (IVF)** and **Hierarchically Navigable Small Worlds (HNSW)**. You can create multiple vector indexes within a Lance table. This guide walks through common configurations and build patterns.

### Option 1: Self-Hosted Indexing

**Manual, Sync or Async:** If using LanceDB Open Source, you will have to build indexes manually, as well as reindex and tune indexing parameters. The Python SDK lets you do this *synchronously and asynchronously*.

### Option 2: Automated Indexing

**Automatic and Async:** Indexing is automatic in LanceDB Cloud/Enterprise. As soon as data is updated, our system automates index optimization. *This is done asynchronously*.

Here is what happens in the background - when a table contains a single vector column named `vector`, LanceDB automatically:

* Infers the vector column from the schema
* Creates an optimized `IVF_PQ` index without manual configuration
* The default distance is `l2` or euclidean

Finally, LanceDB Cloud/Enterprise will analyze your data distribution to **automatically configure indexing parameters**.

<Note title="Manual Index Creation">
  You can create a new index with different parameters using `create_index` - this replaces any existing index

  Although the `create_index` API returns immediately, the building of the vector index is asynchronous. To wait until all data is fully indexed, you can specify the `wait_timeout` parameter.
</Note>

## Example: Construct an IVF Index

In this example, we will create an index for a table containing 1536-dimensional vectors. The index will use IVF\_PQ with L2 distance, which is well-suited for high-dimensional vector search.

Make sure you have enough data in your table (at least a few thousand rows) for effective index training.

### Index Configuration

Sometimes you need to configure the index beyond default parameters:

* Index Types:
  * `IVF_PQ`: Default index type, optimized for high-dimensional vectors
  * `IVF_HNSW_SQ`: Combines IVF clustering with HNSW graph for improved search quality
* `metrics`: default is `l2`, other available are `cosine` or `dot`
  * When using `cosine` similarity, distances range from 0 (identical vectors) to 2 (maximally dissimilar)
* `num_partitions`: The number of partitions in the IVF portion of the index. This number is usually chosen to target a particular number of vectors per partition. A common heuristic is `num_rows / 8192`. Larger values generally make index building take longer but use less memory, and they often improve accuracy at the cost of slower search because queries typically need a higher `nprobes`. LanceDB automatically selects a sensible default `num_partitions` based on the heuristic mentioned above.
* `num_sub_vectors`: The number of sub-vectors that will be created during Product Quantization (PQ). This number is typically chosen based on the desired recall and the dimensionality of the vector. Larger `num_sub_vectors` increases accuracy but can significantly slow queries; a good starting point is `dimension / 8`.

Let's take a look at a sample request for an IVF index:

### 1. Setup

Connect to LanceDB and open the table you want to index.

### 2. Construct an IVF Index

Create an `IVF_PQ` index with `cosine` similarity. Specify `vector_column_name` if you use multiple vector columns or non-default names. By default LanceDB uses Product Quantization; switch to `IVF_SQ` for scalar quantization.

### 3. Query the IVF Index

Search using a random 1,536-dimensional embedding.

#### Search Configuration

The previous query uses:

* `limit`: number of results to return
* `nprobes`: number of IVF partitions to scan; covering roughly 5–10% of partitions often balances recall and latency
* `refine_factor`: reads additional candidates and reranks in memory
* `.to_pandas()`: converts the results to a pandas DataFrame

## Example: Construct an HNSW Index

### Index Configuration

There are three key parameters to set when constructing an HNSW index:

* `metric`: The default is `l2` euclidean distance metric. Other available are `dot` and `cosine`.
* `m`: The number of neighbors to select for each vector in the HNSW graph.
* `ef_construction`: The number of candidates to evaluate during the construction of the HNSW graph.

### 1. Construct an HNSW Index

### 2. Query the HNSW Index

## Example: Construct a Binary Vector Index

Binary vectors are useful for hash-based retrieval, fingerprinting, or any scenario where data can be represented as bits.

### Index Configuration

* Store binary vectors as fixed-size binary data (uint8 arrays, with 8 bits per byte). For storage, pack binary vectors into bytes to save space.
* Index Type: `IVF_FLAT` is used for indexing binary vectors
* `metric`: the `hamming` distance is used for similarity search
* The dimension of binary vectors must be a multiple of 8. For example, a 128-dimensional vector is stored as a uint8 array of size 16.

### 1. Create Table and Schema

### 2. Generate and Add Data

### 3. Construct the Binary Index

### 4. Vector Search

## Check Index Status

Vector index creation is fast - typically a few minutes for 1 million vectors with 1536 dimensions. You can check index status in two ways:

### Option 1: Check the UI

Navigate to your table page - the "Index" column shows index status. It remains blank if no index exists or if creation is in progress.

### Option 2: Use the API

Use `list_indices()` and `index_stats()` to check index status. The index name is formed by appending "\_idx" to the column name. Note that `list_indices()` only returns information after the index is fully built.
To wait until all data is fully indexed, you can specify the `wait_timeout` parameter on `create_index()` or call `wait_for_index()` on the table.


# GenKit
Source: https://docs.lancedb.com/integrations/ai/genkit



### genkitx-lancedb

Genkit is an open-source framework for building end-to-end AI and RAG pipelines with a clean, TypeScript-first
developer experience. The genkitx-lancedb plugin lets you use LanceDB as a high-performance vector store
inside your Genkit flows, so you can index, search, and retrieve data efficiently as part of your AI
applications.

### Installation

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
pnpm install genkitx-lancedb
```

### Usage

Adding LanceDB plugin to your genkit instance.

You can run this app with the following command:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
genkit start -- tsx --watch src/index.ts
```

This'll add LanceDB as a retriever and indexer to the genkit instance. You can see it in the GUI view

<img alt="Screenshot 2025-05-11 at 7 21 05 PM" />

**Testing retrieval on a sample table**
Let's see the raw retrieval results

<img alt="Screenshot 2025-05-11 at 7 21 05 PM" />

On running this query, you'll 5 results fetched from the lancedb table, where each result looks something like this:

<img alt="Screenshot 2025-05-11 at 7 21 18 PM" />

## Creating a custom RAG flow

Now that we've seen how you can use LanceDB for in a genkit pipeline, let's refine the flow and create a RAG. A RAG flow will consist of an index and a retreiver with its outputs postprocessed an fed into an LLM for final response

### Creating custom indexer flows

You can also create custom indexer flows, utilizing more options and features provided by LanceDB.

<img alt="Screenshot 2025-05-11 at 8 35 56 PM" />

In your console, you can see the logs

<img alt="Screenshot 2025-05-11 at 7 19 14 PM" />

### Creating custom retriever flows

You can also create custom retriever flows, utilizing more options and features provided by LanceDB.

Now using our retrieval flow, we can ask question about the ingsted PDF

<img alt="Screenshot 2025-05-11 at 7 18 45 PM" />


# Kiln AI
Source: https://docs.lancedb.com/integrations/ai/kiln



[**Kiln**](https://kiln.tech) is a free tool for building production-ready AI systems, combining an intuitive desktop application and an open-source Python library. It supports RAG pipelines, evaluations, agents, MCP tool-calling, synthetic data generation, and fine-tuning. Kiln provides deep integration with LanceDB for vector search, full-text search (BM25), and hybrid search.

## Quick Start: Build a RAG Pipeline in 5 Minutes with Kiln & LanceDB

Watch the [quick start overview on Vimeo](https://vimeo.com/1119945690).

Kiln's [app](https://kiln.tech/download) makes it easy to:

* Build a RAG pipeline with a simple drag-and-drop interface
* [Compare](#find-the-best-rag-pipeline-for-your-use-case) search index options (powered by LanceDB), document extractors, embedding models, and chunking strategies
* Create end-to-end [evaluations](https://docs.kiln.tech/docs/evaluations) to determine which search configuration works best for your use case
* Load your data from Kiln into LanceDB Cloud for production use
* Iterate with confidence by evaluating new content, prompts, models, and embeddings in minutes instead of weeks

## Find the Best RAG Pipeline for Your Use Case

There is no universal best RAG solution—only the best solution for your specific use case. Kiln makes it easy to compare state-of-the-art configurations and find which works best for you.

Start with pre-configured templates for state-of-the-art RAG at various performance/quality/cost levels, or experiment with any combination of options:

| Area                | Technologies                                                | Description                                                                                                                               |
| :------------------ | :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Search Index        | LanceDB                                                     | Compare LanceDB's vector search, full-text search (BM25), and hybrid search to find the best approach for your use case.                  |
| Content             | Kiln Document Library                                       | Collaborate on a document library with your team to find the best content for your RAG. Track every revision and tag document sets.       |
| Document Extraction | Gemini, OpenAI GPT, Qwen VL, and more                       | Find the most accurate document extraction models for converting PDFs, images, audio, video, and other formats into textual data for RAG. |
| Embeddings          | Embedding models from Gemini, OpenAI, Nomic, Qwen, and more | Find the embedding model best suited to your use case.                                                                                    |
| Chunking            | LlamaIndex                                                  | Find the ideal chunk size and method.                                                                                                     |

## Get Started

To get started, download the [Kiln App](https://kiln.tech/download), create a project, and navigate to "Docs & Search".

See the [Kiln documentation for creating a RAG system](https://docs.kiln.tech/docs/documents-and-search-rag) for details on each step of the process.

## More Information

* [Kiln Homepage](https://kiln.tech)
* [Download the Kiln App](https://kiln.tech/download)
* [Kiln GitHub Repository](https://github.com/Kiln-AI/Kiln)
* [Building RAG Systems - Kiln Documentation](https://docs.kiln.tech/docs/documents-and-search-rag)
* [Python Library](https://pypi.org/project/kiln-ai/) or `pip install kiln_ai`


# LangChain
Source: https://docs.lancedb.com/integrations/ai/langchain



**LangChain** is a framework designed for building applications with large language models (LLMs) by chaining together various components. It supports a range of functionalities including memory, agents, and chat models, enabling developers to create context-aware applications.

![Illustration](https://raw.githubusercontent.com/lancedb/assets/refs/heads/main/docs/assets/integration/langchain_rag.png)

LangChain streamlines these stages (in figure above) by providing pre-built components and tools for integration, memory management, and deployment, allowing developers to focus on application logic rather than underlying complexities.

Integration of **Langchain** with **LanceDB** enables applications to retrieve the most relevant data by comparing query vectors against stored vectors, facilitating effective information retrieval. It results in better and context aware replies and actions by the LLMs.

## Quick Start

You can load your document data using langchain's loaders, for this example we are using `TextLoader` and `OpenAIEmbeddings` as the embedding model.

## Documentation

In the above example `LanceDB` vector store class object is created using `from_documents()` method  which is a `classmethod` and returns the initialized class object.

You can also use `LanceDB.from_texts(texts: List[str],embedding: Embeddings)` class method.

The exhaustive list of parameters for `LanceDB` vector store are :

| Name                 | type                                  | Purpose                                                                                                                                  | default                          |
| :------------------- | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| `connection`         | (Optional) `Any`                      | `lancedb.db.LanceDBConnection` connection object to use.  If not provided, a new connection will be created.                             | `None`                           |
| `embedding`          | (Optional) `Embeddings`               | Langchain embedding model.                                                                                                               | Provided by user.                |
| `uri`                | (Optional) `str`                      | It specifies the directory location of **LanceDB database** and establishes a connection that can be used to interact with the database. | `/tmp/lancedb`                   |
| `vector_key`         | (Optional) `str`                      | Column name to use for vector's in the table.                                                                                            | `'vector'`                       |
| `id_key`             | (Optional) `str`                      | Column name to use for id's in the table.                                                                                                | `'id'`                           |
| `text_key`           | (Optional) `str`                      | Column name to use for text in the table.                                                                                                | `'text'`                         |
| `table_name`         | (Optional) `str`                      | Name of your table in the database.                                                                                                      | `'vectorstore'`                  |
| `api_key`            | (Optional `str`)                      | API key to use for LanceDB cloud database.                                                                                               | `None`                           |
| `region`             | (Optional) `str`                      | Region to use for LanceDB cloud database.                                                                                                | Only for LanceDB Cloud : `None`. |
| `mode`               | (Optional) `str`                      | Mode to use for adding data to the table. Valid values are "append" and "overwrite".                                                     | `'overwrite'`                    |
| `table`              | (Optional) `Any`                      | You can connect to an existing table of LanceDB, created outside of langchain, and utilize it.                                           | `None`                           |
| `distance`           | (Optional) `str`                      | The choice of distance metric used to calculate the similarity between vectors.                                                          | `'l2'`                           |
| `reranker`           | (Optional) `Any`                      | The reranker to use for LanceDB.                                                                                                         | `None`                           |
| `relevance_score_fn` | (Optional) `Callable[[float], float]` | Langchain relevance score function to be used.                                                                                           | `None`                           |
| `limit`              | `int`                                 | Set the maximum number of results to return.                                                                                             | `DEFAULT_K` (it is 4)            |

### Methods

##### `add_texts()`

This method turn texts into embedding and add it to the database.

| Name        | Purpose                                                         | defaults         |
| :---------- | :-------------------------------------------------------------- | :--------------- |
| `texts`     | `Iterable` of strings to add to the vectorstore.                | Provided by user |
| `metadatas` | Optional `list[dict()]` of metadatas associated with the texts. | `None`           |
| `ids`       | Optional `list` of ids to associate with the texts.             | `None`           |
| `kwargs`    | Other keyworded arguments provided by the user.                 | -                |

It returns list of ids of the added texts.

***

##### create\_index()

This method creates a scalar(for non-vector cols) or a vector index on a table.

| Name               | type            | Purpose                                                                               | defaults |
| :----------------- | :-------------- | :------------------------------------------------------------------------------------ | :------- |
| `vector_col`       | `Optional[str]` | Provide if you want to create index on a vector column.                               | `None`   |
| `col_name`         | `Optional[str]` | Provide if you want to create index on a non-vector column.                           | `None`   |
| `metric`           | `Optional[str]` | Provide the metric to use for vector index. choice of metrics: 'l2', 'dot', 'cosine'. | `l2`     |
| `num_partitions`   | `Optional[int]` | Number of partitions to use for the index.                                            | `256`    |
| `num_sub_vectors`  | `Optional[int]` | Number of sub-vectors to use for the index.                                           | `96`     |
| `index_cache_size` | `Optional[int]` | Size of the index cache.                                                              | `None`   |
| `name`             | `Optional[str]` | Name of the table to create index on.                                                 | `None`   |

For index creation make sure your table has enough data in it. An ANN index is ususally not needed for datasets \~100K vectors. For large-scale (>1M) or higher dimension vectors, it is beneficial to create an ANN index.

***

##### similarity\_search()

This method performs similarity search based on **text query**.

| Name     | Type                       | Purpose                                                                                                                                                     | Default |
| -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`  | `str`                      | A `str` representing the text query that you want to search for in the vector store.                                                                        | N/A     |
| `k`      | `Optional[int]`            | It specifies the number of documents to return.                                                                                                             | `None`  |
| `filter` | `Optional[Dict[str, str]]` | It is used to filter the search results by specific metadata criteria.                                                                                      | `None`  |
| `fts`    | `Optional[bool]`           | It indicates whether to perform a full-text search (FTS).                                                                                                   | `False` |
| `name`   | `Optional[str]`            | It is used for specifying the name of the table to query. If not provided, it uses the default table set during the initialization of the LanceDB instance. | `None`  |
| `kwargs` | `Any`                      | Other keyworded arguments provided by the user.                                                                                                             | N/A     |

Return documents most similar to the query **without relevance scores**.

***

##### similarity\_search\_by\_vector()

The method returns documents that are most similar to the specified **embedding (query) vector**.

| Name        | Type                       | Purpose                                                                                                                                                     | Default |
| ----------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `embedding` | `List[float]`              | The embedding vector you want to use to search for similar documents in the vector store.                                                                   | N/A     |
| `k`         | `Optional[int]`            | It specifies the number of documents to return.                                                                                                             | `None`  |
| `filter`    | `Optional[Dict[str, str]]` | It is used to filter the search results by specific metadata criteria.                                                                                      | `None`  |
| `name`      | `Optional[str]`            | It is used for specifying the name of the table to query. If not provided, it uses the default table set during the initialization of the LanceDB instance. | `None`  |
| `kwargs`    | `Any`                      | Other keyworded arguments provided by the user.                                                                                                             | N/A     |

**It does not provide relevance scores.**

***

##### similarity\_search\_with\_score()

Returns documents most similar to the **query string** along with their relevance scores.

| Name     | Type                       | Purpose                                                                                                                                                                                      | Default |
| -------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`  | `str`                      | A `str` representing the text query you want to search for in the vector store. This query will be converted into an embedding using the specified embedding function.                       | N/A     |
| `k`      | `Optional[int]`            | It specifies the number of documents to return.                                                                                                                                              | `None`  |
| `filter` | `Optional[Dict[str, str]]` | It is used to filter the search results by specific metadata criteria. This allows you to narrow down the search results based on certain metadata attributes associated with the documents. | `None`  |
| `kwargs` | `Any`                      | Other keyworded arguments provided by the user.                                                                                                                                              | N/A     |

It gets called by base class's `similarity_search_with_relevance_scores` which selects relevance score based on our `_select_relevance_score_fn`.

***

##### similarity\_search\_by\_vector\_with\_relevance\_scores()

Similarity search using **query vector**.

| Name        | Type                       | Purpose                                                                                   | Default |
| ----------- | -------------------------- | ----------------------------------------------------------------------------------------- | ------- |
| `embedding` | `List[float]`              | The embedding vector you want to use to search for similar documents in the vector store. | N/A     |
| `k`         | `Optional[int]`            | It specifies the number of documents to return.                                           | `None`  |
| `filter`    | `Optional[Dict[str, str]]` | It is used to filter the search results by specific metadata criteria.                    | `None`  |
| `name`      | `Optional[str]`            | It is used for specifying the name of the table to query.                                 | `None`  |
| `kwargs`    | `Any`                      | Other keyworded arguments provided by the user.                                           | N/A     |

The method returns documents most similar to the specified embedding (query) vector, along with their relevance scores.

***

##### max\_marginal\_relevance\_search()

This method returns docs selected using the maximal marginal relevance(MMR).
Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

| Name          | Type                                            | Purpose                                                                                                                                                | Default |
| ------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `query`       | `str`                                           | Text to look up documents similar to.                                                                                                                  | N/A     |
| `k`           | `Optional[int]`                                 | Number of Documents to return.                                                                                                                         | `4`     |
| `fetch_k`     | `Optional[int]`                                 | Number of Documents to fetch to pass to MMR algorithm.                                                                                                 | `None`  |
| `lambda_mult` | `float`                                         | Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. | `0.5`   |
| `filter`      | `Optional[Dict[str, str]]`                      | Filter by metadata.                                                                                                                                    | `None`  |
| `kwargs`      | Other keyworded arguments provided by the user. | -                                                                                                                                                      |         |

Similarly, `max_marginal_relevance_search_by_vector()` function returns docs most similar to the embedding passed to the function using MMR. instead of a string query you need to pass the embedding to be searched for.

***

##### add\_images()

This method ddds images by automatically creating their embeddings and adds them to the vectorstore.

| Name        | Type                   | Purpose                    | Default |
| ----------- | ---------------------- | -------------------------- | ------- |
| `uris`      | `List[str]`            | File path to the image     | N/A     |
| `metadatas` | `Optional[List[dict]]` | Optional list of metadatas | `None`  |
| `ids`       | `Optional[List[str]]`  | Optional list of IDs       | `None`  |

It returns list of IDs of the added images.


# LlamaIndex
Source: https://docs.lancedb.com/integrations/ai/llamaIndex



## Quickstart

LlamaIndex is a well-known framework for building LLM-powered agents over your data with LLMs and workflows.
You can build your LlamaIndex pipeline and persist your metadata and embeddings in LanceDB via the `LanceDBVectorStore` class.

First, install the LlamaIndex-LanceDB integration.

<CodeBlock icon="terminal">
  pip install llama-index-vector-stores-LanceDB
</CodeBlock>

Run the below script as an example.

The vector store connector will open an existing LanceDB directory or create the directory if it does not exist.

### Filtering

For metadata filtering, you can use a Lance SQL-like string filter as demonstrated in the example above. Additionally, you can also filter using the `MetadataFilters` class from LlamaIndex:

### Hybrid Search

For complete documentation, refer [here](https://lancedb.github.io/lancedb/hybrid_search/hybrid_search/). This example uses the `colbert` reranker. Make sure to install necessary dependencies for the reranker you choose.

In the snippet above, you can change/specify `query_type` when creating the engine/retriever
to use different search strategies, such as vector search or FTS.

## API reference

<Card title="LlamaIndex Vector Stores API reference" href="https://developers.llamaindex.ai/python/framework-api-reference/storage/vector_store/lancedb/">
  See the official LlamaIndex Vector Stores API reference for more details.
</Card>


# PromptTools
Source: https://docs.lancedb.com/integrations/ai/prompttools



[PromptTools](https://github.com/hegelai/prompttools) offers a set of free, open-source tools for testing and experimenting with models, prompts, and configurations. The core idea is to enable developers to evaluate prompts using familiar interfaces like code and notebooks. You can use it to experiment with different configurations of LanceDB, and test how LanceDB integrates with the LLM of your choice.

<a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/prompttools-eval-prompts/main.ipynb">
  <img alt="Open In Colab" />
</a>

![Alt text](https://prompttools.readthedocs.io/en/latest/_images/demo.gif "a title")


# Meta Llama Synthetic Data Kit
Source: https://docs.lancedb.com/integrations/ai/synthetic-data-kit

Use Meta Llama's Synthetic Data Kit with LanceDB to generate high-quality synthetic datasets for LLM fine-tuning and training.

[Sythetic Data Kit](https://github.com/meta-llama/synthetic-data-kit) is a tool from Meta LLAMA that helps you generate high-quality synthetic datasets for fine-tuning large language models (LLMs). It simplifies the process of preparing data for fine-tuning by providing a command-line interface (CLI) with a modular four-command flow.

One of the key features of the `synthetic-data-kit` is its use of the Lance format for storing and ingesting datasets. This allows for efficient storage and retrieval of data, which is crucial when working with large datasets.

### Key Features:

* **Data Ingestion:** The toolkit can ingest various file formats, including PDF, HTML, YouTube transcripts, DOCX, PPT, and TXT.
* **Fine-tuning Format Creation:** It can create different fine-tuning formats, such as question-answer (QA) pairs, QA pairs with Chain-of-Thought (CoT), and summarization formats.
* **Data Curation:** The tool uses Llama as a judge to curate high-quality examples, ensuring the quality of the generated dataset.
* **Flexible Saving Options:** You can save the generated datasets in various formats compatible with your fine-tuning workflow, including Hugging Face, JSONL, and JSON.

### How it Works:

The synthetic-data-kit follows a simple four-step process:

1. **Ingest:** Import your input files into the toolkit. The data is stored in the Lance format for efficient processing.
2. **Create:** Generate diverse fine-tuning datasets, such as reasoning, summarization, and QA pairs, from the ingested documents.
3. **Curate:** Use Llama to filter and select high-quality examples from the generated dataset.
4. **Save-as:** Export the curated dataset in your preferred format.

### Usage

The `synthetic-data-kit` uses Lance format to store and manage the data that you ingest. The workflow is a series of commands that build on each other, starting with the `ingest` command.

Here is an example of the end-to-end workflow:

1. **Ingest Data into a LanceDB dataset**

   This command takes a directory of source files and creates a LanceDB dataset from them.

   ```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   synthetic-data-kit ingest docs/report.pdf --multimodal
   # This will create a Lance dataset at data/parsed/report.lance
   # with 'text' and 'image' columns.

   #Generate multimodal-qa pairs from the ingested data
   synthetic-data-kit create data/parsed/report.lance --type multimodal-qa
   ```

2. **Create fine-tuning data**

   This command uses the LanceDB dataset created in the previous step to generate synthetic data in the desired format.

   ```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   synthetic_data create data/parsed/report.lance
   ```

3. **Curate the data**

   This step uses a language model to curate the generated data and ensure its quality.

   ```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   synthetic_data curate report.json
   ```

4. **Save the final dataset**

   Finally, save the curated data to a file in the desired format.

   ```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   synthetic_data save-as  report.json --save_path ./my_finetuning_data.jsonl
   ```

This workflow allows you to go from a collection of documents to a high-quality, fine-tuning dataset with just a few commands. The use of LanceDB in the background makes the process efficient and scalable.

### Getting Started:

To get started with the synthetic-data-kit, you can clone the [GitHub Repository](https://github.com/meta-llama/synthetic-data-kit) and install the necessary dependencies.

> **Note:** You will also need access to a Llama model, either running locally or via a hosted API.


# dlt
Source: https://docs.lancedb.com/integrations/data/dlt



[dlt](https://dlthub.com/docs/intro) is an open-source library that you can add to your Python scripts to load data from various and often messy data sources into well-structured, live datasets. dlt's [integration with LanceDB](https://dlthub.com/docs/dlt-ecosystem/destinations/lancedb) lets you ingest data from any source (databases, APIs, CSVs, dataframes, JSONs, and more) into LanceDB with a few lines of simple python code. The integration enables automatic normalization of nested data, schema inference, incremental loading and embedding the data. dlt also has integrations with several other tools like dbt, airflow, dagster etc. that can be inserted into your LanceDB workflow.

## How to ingest data into LanceDB

In this example, we will be fetching movie information from the [Open Movie Database (OMDb) API](https://www.omdbapi.com/) and loading it into a local LanceDB instance. To implement it, you will need an API key for the OMDb API (which can be created freely [here](https://www.omdbapi.com/apikey.aspx)).

1. **Install `dlt` with LanceDB extras:**
   ```sh theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   pip install dlt[lancedb]
   ```

2. **Inside an empty directory, initialize a `dlt` project with:**

   ```sh theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   dlt init rest_api lancedb
   ```

   This will add all the files necessary to create a `dlt` pipeline that can ingest data from any REST API (ex: OMDb API) and load into LanceDB.

   ```text theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   ├── .dlt
   │   ├── config.toml
   │   └── secrets.toml
   ├── rest_api
   ├── rest_api_pipeline.py
   └── requirements.txt
   ```

   dlt has a list of pre-built [sources](https://dlthub.com/docs/dlt-ecosystem/verified-sources/) like [SQL databases](https://dlthub.com/docs/dlt-ecosystem/verified-sources/sql_database), [REST APIs](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api), [Google Sheets](https://dlthub.com/docs/dlt-ecosystem/verified-sources/google_sheets), [Notion](https://dlthub.com/docs/dlt-ecosystem/verified-sources/notion) etc., that can be used out-of-the-box by running `dlt init <source_name> lancedb`. Since dlt is a python library, it is also very easy to modify these pre-built sources or to write your own custom source from scratch.

3. **Specify necessary credentials and/or embedding model details:**

   In order to fetch data from the OMDb API, you will need to pass a valid API key into your pipeline. Depending on whether you're using LanceDB OSS or LanceDB cloud, you also may need to provide the necessary credentials to connect to the LanceDB instance. These can be pasted inside `.dlt/sercrets.toml`.

   dlt's LanceDB integration also allows you to automatically embed the data during ingestion. Depending on the embedding model chosen, you may need to paste the necessary credentials inside `.dlt/sercrets.toml`:

   ```toml theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   [sources.rest_api]
   api_key = "api_key" # Enter the API key for the OMDb API

   [destination.lancedb]
   embedding_model_provider = "sentence-transformers"
   embedding_model = "all-MiniLM-L6-v2"
   [destination.lancedb.credentials]
   uri = ".lancedb"
   api_key = "api_key" # API key to connect to LanceDB Cloud. Leave out if you are using LanceDB OSS.
   embedding_model_provider_api_key = "embedding_model_provider_api_key" # Not needed for providers that don't need authentication (ollama, sentence-transformers).
   ```

   See [here](https://dlthub.com/docs/dlt-ecosystem/destinations/lancedb#configure-the-destination) for more information and for a list of available models and model providers.

4. **Write the pipeline code inside `rest_api_pipeline.py`:**

   The following code shows how you can configure dlt's REST API source to connect to the [OMDb API](https://www.omdbapi.com/), fetch all movies with the word "godzilla" in the title, and load it into a LanceDB table. The REST API source allows you to pull data from any API with minimal code, to learn more read the [dlt docs](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api).

   The script above will ingest the data into LanceDB as it is, i.e. without creating any embeddings. If we want to embed one of the fields (for example, `"Title"` that contains the movie titles), then we will use dlt's `lancedb_adapter` and modify the script as follows:

   * Add the following import statement:
   * Modify the pipeline run like this:

   This will use the embedding model specified inside `.dlt/secrets.toml` to embed the field `"Title"`.

5. **Install necessary dependencies:**

   ```sh theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   pip install -r requirements.txt
   ```

   Note: You may need to install the dependencies for your embedding models separately.

   ```sh theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   pip install sentence-transformers
   ```

6. **Run the pipeline:**
   Finally, running the following command will ingest the data into your LanceDB instance.
   ```sh theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   python custom_source.py
   ```

For more information and advanced usage of dlt's LanceDB integration, read [the dlt documentation](https://dlthub.com/docs/dlt-ecosystem/destinations/lancedb).


# DuckDB
Source: https://docs.lancedb.com/integrations/data/duckdb



<Badge>OSS-only</Badge>

In Python, LanceDB tables can also be queried with [DuckDB](https://duckdb.org/), an in-process SQL OLAP database.
This means you can write complex SQL queries to analyze your data in LanceDB.

The integration is done via [Apache Arrow](https://duckdb.org/docs/guides/python/sql_on_arrow), which provides
zero-copy data sharing between LanceDB and DuckDB. DuckDB is capable of passing down column selections and basic
filters to LanceDB, reducing the amount of data that needs to be scanned to perform your query. Finally, the
integration allows streaming data from LanceDB tables, allowing you to aggregate tables that don't fit into
memory.

<Tip>
  **DuckDB quacks Arrow**

  All of this uses the same mechanism described in DuckDB's [blog post](https://duckdb.org/2021/12/03/duck-arrow.html)"
  on how it integrates with Apache Arrow.
</Tip>

We can demonstrate this by first installing `duckdb` and `lancedb`.

<CodeBlock icon="terminal">
  pip install duckdb lancedb
</CodeBlock>

We will re-use the dataset [created previously](/integrations/data/pandas_and_pyarrow/):

The `to_lance` method converts the LanceDB table to a `LanceDataset`, which is accessible to DuckDB through the Arrow compatibility layer.
To query the resulting Lance dataset in DuckDB, all you need to do is reference the dataset by the same name in your SQL query.

```
┌─────────────┬─────────┬────────┐
│   vector    │  item   │ price  │
│   float[]   │ varchar │ double │
├─────────────┼─────────┼────────┤
│ [3.1, 4.1]  │ foo     │   10.0 │
│ [5.9, 26.5] │ bar     │   20.0 │
└─────────────┴─────────┴────────┘
```

You can very easily run any other DuckDB SQL queries on your data.

```
┌─────────────┐
│ mean(price) │
│   double    │
├─────────────┤
│        15.0 │
└─────────────┘
```


# Pandas and PyArrow
Source: https://docs.lancedb.com/integrations/data/pandas_and_pyarrow



Because Lance is built on top of [Apache Arrow](https://arrow.apache.org/),
LanceDB fits naturally into Pandas-first workflows. You can ingest a `DataFrame`,
query it with LanceDB's vector operators, and keep working in Pandas without any glue code.

## Create a dataset

Start by importing LanceDB alongside your usual Pandas utilities and connect to a temporary database.

Use the familiar `pd.DataFrame` API to prepare your rows, then pass the entire frame to `db.create_table`.

## Vector search

Queries can return Pandas frames as well, so you can immediately inspect the results or pipe them into downstream analytics.

## Async API

For web services or background jobs that already rely on `asyncio`, use the asynchronous helpers to keep everything non-blocking.


# Phidata
Source: https://docs.lancedb.com/integrations/data/phidata



[Phidata](https://docs.phidata.com/introduction) is a framework for building **AI Assistants** with long-term memory, contextual knowledge, and the ability to take actions using function calling. It helps turn general-purpose LLMs into specialized assistants tailored to your use case by extending its capabilities using **memory**, **knowledge**, and **tools**.

* **Memory**: Stores chat history in a **database** and enables LLMs to have long-term conversations.
* **Knowledge**: Stores information in a **vector database** and provides LLMs with business context. (Here we will use LanceDB)
* **Tools**: Enable LLMs to take actions like pulling data from an **API**, **sending emails** or **querying a database**, etc.

![example](https://raw.githubusercontent.com/lancedb/assets/refs/heads/main/docs/assets/integration/phidata_assistant.png)

Memory & knowledge make LLMs *smarter* while tools make them *autonomous*.

LanceDB is a vector database and its integration into Phidata makes it easy for us to provide a **knowledge base** to LLMs. It enables us to store information as embeddings and search for the **results** similar to ours using **query**.

<Info>
  **What is a Knowledge Base?**

  Knowledge Base is a database of information that the Assistant can search to improve its responses. This information is stored in a vector database and provides LLMs with business context, which makes them respond in a context-aware manner.

  While any type of storage can act as a knowledge base, vector databases offer the best solution for retrieving relevant results from dense information quickly.
</Info>

Let's see how using LanceDB inside Phidata helps in making LLM more useful:

## Prerequisites: install and import necessary dependencies

**Create a virtual environment**

1. install virtualenv package

<CodeBlock icon="terminal">
  pip install virtualenv
</CodeBlock>

2. Create a directory for your project and go to the directory and create a virtual environment inside it.

<CodeBlock icon="terminal">
  mkdir phi
</CodeBlock>

<CodeBlock icon="terminal">
  cd phi
</CodeBlock>

<CodeBlock icon="terminal">
  python -m venv phidata\_
</CodeBlock>

**Activating virtual environment**

1. from inside the project directory, run the following command to activate the virtual environment.

<CodeBlock icon="terminal">
  phidata\_/Scripts/activate
</CodeBlock>

**Install the following packages in the virtual environment**

<CodeBlock icon="terminal">
  pip install lancedb phidata youtube\_transcript\_api openai ollama numpy pandas
</CodeBlock>

**Create python files and import necessary libraries**

You need to create two files -- `transcript.py` and `ollama_assistant.py` or `openai_assistant.py`

<Warning>
  If creating Ollama assistant, download and install Ollama [from here](https://ollama.com/) and then run the Ollama instance in the background. Also, download the required models using `ollama pull <model-name>`. Check out the models [here](https://ollama.com/library)
</Warning>

**Run the following command to deactivate the virtual environment if needed**

<CodeBlock icon="terminal">
  deactivate
</CodeBlock>

## **Step 1** - Create a Knowledge Base for AI Assistant using LanceDB

Check out the list of **embedders** supported by **Phidata** and their usage [here](https://docs.phidata.com/embedder/introduction).

Here we have used `TextKnowledgeBase`, which loads text/docx files to the knowledge base.

Let's see all the parameters that `TextKnowledgeBase` takes -

| Name            | Type               | Purpose                                                                                                                                                                                              | Default          |
| :-------------- | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
| `path`          | `Union[str, Path]` | Path to text file(s). It can point to a single text file or a directory of text files.                                                                                                               | provided by user |
| `formats`       | `List[str]`        | File formats accepted by this knowledge base.                                                                                                                                                        | `[".txt"]`       |
| `vector_db`     | `VectorDb`         | Vector Database for the Knowledge Base. Phidata provides a wrapper around many vector DBs, you can import it like this - `from phi.vectordb.lancedb import LanceDb`                                  | provided by user |
| `num_documents` | `int`              | Number of results (documents/vectors) that vector search should return.                                                                                                                              | `5`              |
| `reader`        | `TextReader`       | Phidata provides many types of reader objects which read data, clean it and create chunks of data, encapsulate each chunk inside an object of the `Document` class, and return **`List[Document]`**. | `TextReader()`   |
| `optimize_on`   | `int`              | It is used to specify the number of documents on which to optimize the vector database. Supposed to create an index.                                                                                 | `1000`           |

??? Tip "Wonder! What is `Document` class?"
We know that, before storing the data in vectorDB, we need to split the data into smaller chunks upon which embeddings will be created and these embeddings along with the chunks will be stored in vectorDB. When the user queries over the vectorDB, some of these embeddings will be returned as the result based on the semantic similarity with the query.

When the user queries over vectorDB, the queries are converted into embeddings, and a nearest neighbor search is performed over these query embeddings which returns the embeddings that correspond to most semantically similar chunks(parts of our data) present in vectorDB.

Here, a "Document" is a class in Phidata. Since there is an option to let Phidata create and manage embeddings, it splits our data into smaller chunks(as expected). It does not directly create embeddings on it. Instead, it takes each chunk and encapsulates it inside the object of the `Document` class along with various other metadata related to the chunk. Then embeddings are created on these `Document` objects and stored in vectorDB.

However, using Phidata you can load many other types of data in the knowledge base(other than text). Check out [Phidata Knowledge Base](https://docs.phidata.com/knowledge/introduction) for more information.

Let's dig deeper into the `vector_db` parameter and see what parameters `LanceDb` takes -

| Name         | Type                    | Purpose                                                                                                                                                                                                                                          | Default           |
| :----------- | :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| `embedder`   | `Embedder`              | Phidata provides many Embedders that abstract the interaction with embedding APIs and utilize it to generate embeddings. Check out other embedders [here](https://docs.phidata.com/embedder/introduction)                                        | `OpenAIEmbedder`  |
| `distance`   | `List[str]`             | The choice of distance metric used to calculate the similarity between vectors, which directly impacts search results and performance in vector databases.                                                                                       | `Distance.cosine` |
| `connection` | `lancedb.db.LanceTable` | LanceTable can be accessed through `.connection`. You can connect to an existing table of LanceDB, created outside of Phidata, and utilize it. If not provided, it creates a new table using `table_name` parameter and adds it to `connection`. | `None`            |
| `uri`        | `str`                   | It specifies the directory location of **LanceDB database** and establishes a connection that can be used to interact with the database.                                                                                                         | `"/tmp/lancedb"`  |
| `table_name` | `str`                   | If `connection` is not provided, it initializes and connects to a new **LanceDB table** with a specified(or default) name in the database present at `uri`.                                                                                      | `"phi"`           |
| `nprobes`    | `int`                   | It refers to the number of partitions that the search algorithm examines to find the nearest neighbors of a given query vector. Higher values will yield better recall (more likely to find vectors if they exist) at the expense of latency.    | `20`              |

<Note>
  Since we just initialized the KnowledgeBase. The VectorDB table that corresponds to this Knowledge Base is not yet populated with our data. It will be populated in **Step 3**, once we perform the `load` operation.

  You can check the state of the LanceDB table using - `knowledge_base.vector_db.connection.to_pandas()`
</Note>

Now that the Knowledge Base is initialized, , we can go to **step 2**.

## **Step 2** -  Create an assistant with our choice of LLM and reference to the knowledge base.

Assistants add **memory**, **knowledge**, and **tools** to LLMs. Here we will add only **knowledge** in this example.

Whenever we will give a query to LLM, the assistant will retrieve relevant information from our **Knowledge Base**(table in LanceDB) and pass it to LLM along with the user query in a structured way.

* The `add_references_to_prompt=True` always adds information from the knowledge base to the prompt, regardless of whether it is relevant to the question.

To know more about an creating assistant in Phidata, check out [Phidata docs](https://docs.phidata.com/assistants/introduction) here.

## **Step 3** - Load data to Knowledge Base.

The above code loads the data to the Knowledge Base(LanceDB Table) and now it is ready to be used by the assistant.

| Name            | Type   | Purpose                                                                              | Default |
| :-------------- | :----- | :----------------------------------------------------------------------------------- | :------ |
| `recreate`      | `bool` | If True, it drops the existing table and recreates the table in the vectorDB.        | `False` |
| `upsert`        | `bool` | If True and the vectorDB supports upsert, it will upsert documents to the vector db. | `False` |
| `skip_existing` | `bool` | If True, skips documents that already exist in the vectorDB when inserting.          | `True`  |

> **Tip · What is upsert?**\
> Upsert is a database operation that combines “update” and “insert”. It updates existing records if a document with the same identifier exists, or inserts new records if no matching record exists. This keeps the knowledge base current without manual checks.

During the Load operation, Phidata directly interacts with the LanceDB library and performs the loading of the table with our data in the following steps -

1. **Creates** and **initializes** the table if it does not exist.

2. Then it **splits** our data into smaller **chunks**.

   > **Question · How do they create chunks?**\
   > **Phidata** provides multiple knowledge-base types depending on the source data. Most of them (except the LlamaIndexKnowledgeBase and LangChainKnowledgeBase) expose a `document_lists` iterator. During the load operation, this iterator reads the input (for example, text files), splits it into chunks, wraps each chunk in a `Document`, and yields lists of those `Document` objects.

3. Then **embeddings** are created on these chunks are **inserted** into the LanceDB Table

   > **Question · How do they insert the chunks into LanceDB?**\
   > Each list of `Document` objects from the previous step is processed as follows:
   >
   > * Generate embeddings for every `Document`.
   > * Clean the `content` field so only the text you care about is persisted.
   > * Prepare a payload with the `id`, the embedding (`vector`), and any metadata needed for retrieval.
   > * Add the prepared rows to the LanceDB table.

4. Now the internal state of `knowledge_base` is changed (embeddings are created and loaded in the table ) and it **ready to be used by assistant**.

## **Step 4** - Start a cli chatbot with access to the Knowledge base

For more information and amazing cookbooks of Phidata, read the [Phidata documentation](https://docs.phidata.com/introduction) and also visit [LanceDB x Phidata docmentation](https://docs.phidata.com/vectordb/lancedb).


# Polars
Source: https://docs.lancedb.com/integrations/data/polars_arrow



LanceDB supports [Polars](https://github.com/pola-rs/polars), a blazingly fast DataFrame library for Python written in Rust. Under the hood, both Lance and Polars speak Arrow, so passing data back and forth stays zero-copy and ergonomic.

## Create & Query a Table

Import the required libraries, including the optional Pydantic helpers if you plan to define schemas.

Build a Polars `DataFrame`, convert it to Arrow, and use it directly when creating a LanceDB table.

Run vector search and keep the results as a Polars `DataFrame` for further processing or visualization.

## Work with LazyFrames

When you want to operate on the entire table (potentially larger than RAM), convert to a Polars `LazyFrame` so you can chain transformations without loading everything at once.

## Define Schemas with Pydantic

You can also describe your table via `LanceModel` and continue ingesting data from Polars. This is useful when multiple teams share a schema or when you want validation.


# Pydantic
Source: https://docs.lancedb.com/integrations/data/pydantic



[Pydantic](https://docs.pydantic.dev/latest/) is a data validation library in Python.
LanceDB integrates with Pydantic for schema inference, data ingestion, and query result casting.
Using `lancedb.pydantic.LanceModel`, users can seamlessly
integrate Pydantic with the rest of the LanceDB APIs.

First, import the necessary LanceDB and Pydantic modules:

Next, define your Pydantic model by inheriting from `LanceModel` and specifying your fields including a vector field:

Set the database connection URL:

Now you can create a table, add data, and perform vector search operations:

## Vector Field

LanceDB provides a `lancedb.pydantic.Vector` method to define a
vector Field in a Pydantic Model.

This example demonstrates how LanceDB automatically converts Pydantic field types to their corresponding Apache Arrow data types. The `pydantic_to_schema()` function takes a Pydantic model and generates an Arrow schema where:

* `int` fields become `pa.int64()` (64-bit integers)
* `str` fields become `pa.utf8()` (UTF-8 encoded strings)
* `Vector(768)` becomes `pa.list_(pa.float32(), 768)` (fixed-size list of 768 float32 values)
* The `False` parameter indicates that the fields are not nullable

## Type Conversion

LanceDB automatically convert Pydantic fields to
[Apache Arrow DataType](https://arrow.apache.org/docs/python/generated/pyarrow.DataType.html#pyarrow.DataType).

Current supported type conversions:

| Pydantic Field Type | PyArrow Data Type                   |
| ------------------- | ----------------------------------- |
| `int`               | `pyarrow.int64`                     |
| `float`             | `pyarrow.float64`                   |
| `bool`              | `pyarrow.bool`                      |
| `str`               | `pyarrow.utf8()`                    |
| `list`              | `pyarrow.List`                      |
| `BaseModel`         | `pyarrow.Struct`                    |
| `Vector(n)`         | `pyarrow.FixedSizeList(float32, n)` |

LanceDB supports to create Apache Arrow Schema from a
`pydantic.BaseModel`
via `lancedb.pydantic.pydantic_to_schema` method.

This example shows a more complex Pydantic model with various field types and demonstrates how LanceDB handles:

* Basic types: `int` and `str` fields
* Vector fields: `Vector(1536)` creates a fixed-size list of 1536 float32 values
* List fields: `List[int]` becomes a variable-length list of int64 values
* Schema generation: The `pydantic_to_schema()` function automatically converts all these types to their Arrow equivalents


# Voxel51
Source: https://docs.lancedb.com/integrations/data/voxel51



# FiftyOne

[FiftyOne](https://docs.voxel51.com/) is an open source toolkit that enables users to curate better data and build better models. It includes tools for data exploration, visualization, and management, as well as features for collaboration and sharing.

Any developers, data scientists, and researchers who work with computer vision and machine learning can use FiftyOne to improve the quality of their datasets and deliver insights about their models.

<img alt="example" />

**FiftyOne** provides an API to create LanceDB tables and run similarity queries, both **programmatically in Python** and via **point-and-click in the App**.

Let's get started and see how to use **LanceDB** to create a **similarity index** on your FiftyOne datasets.

## Overview

[Embeddings](/embedding/) are foundational to all of the **vector search** features. In FiftyOne, embeddings are managed by the [**FiftyOne Brain**](https://docs.voxel51.com/user_guide/brain.html) that provides powerful machine learning techniques designed to transform how you curate your data from an art into a measurable science.

> *Have you ever wanted to find the images most similar to an image in your dataset?*

The **FiftyOne Brain** makes computing **visual similarity** really easy. You can compute the similarity of samples in your dataset using an embedding model and store the results in the **brain key**.
You can then sort your samples by similarity or use this information to find potential duplicate images.

We'll be doing the following :

1. **Create Index** - In order to run similarity queries against our media, we need to **index** the data. We can do this via the `compute_similarity()` function.

* In the function, specify the **model** you want to use to generate the embedding vectors, and what **vector search engine** you want to use on the **backend** (here LanceDB).

<Tip>
  You can also give the similarity index a name(`brain_key`), which is useful if you want to run vector searches against multiple indexes.
</Tip>

2. **Query** - Once you have generated your similarity index, you can query your dataset with `sort_by_similarity()`. The query can be any of the following:

* An ID (sample or patch)
* A query vector of same dimension as the index
* A list of IDs (samples or patches)
* A text prompt (search semantically)

## Prerequisites: install necessary dependencies

1. **Create and activate a virtual environment**

Install virtualenv package and run the following command in your project directory.

<CodeBlock icon="terminal">
  python -m venv fiftyone\_
</CodeBlock>

From inside the project directory run the following to activate the virtual environment.

<CodeGroup>
  <CodeBlock icon="linux">
    source fiftyone\_/Scripts/activate
  </CodeBlock>

  <CodeBlock icon="windows">
    fiftyone\_/Scripts/activate
  </CodeBlock>
</CodeGroup>

2. **Install the following packages in the virtual environment**

   To install FiftyOne, ensure you have activated any virtual environment that you are using, then run

<CodeBlock icon="terminal">
  pip install fiftyone
</CodeBlock>

## Understand basic workflow

The basic workflow shown below uses LanceDB to create a similarity index on your FiftyOne datasets:

1. Load a dataset into FiftyOne.

2. Compute embedding vectors for samples or patches in your dataset, or select a model to use to generate embeddings.

3. Use the `compute_similarity()` method to generate a LanceDB table for the samples or object patches embeddings in a dataset by setting the parameter `backend="lancedb"` and specifying a `brain_key` of your choice.

4. Use this LanceDB table to query your data with `sort_by_similarity()`.

5. If desired, delete the table.

## Quick Example

Let's jump on a quick example that demonstrates this workflow.

Make sure you install torch ([guide here](https://pytorch.org/get-started/locally/)) before proceeding.

!!! note
Running the code above will download the clip model (2.6Gb)

Once the similarity index has been generated, we can query our data in FiftyOne by specifying the `brain_key`:

The returned result are of type - `DatasetView`.

<Note>
  `DatasetView` does not hold its contents in-memory. Views simply store the rule(s) that are applied to extract the content of interest from the underlying Dataset when the view is iterated/aggregated on.

  This means, for example, that the contents of a `DatasetView` may change as the underlying Dataset is modified.
</Note>

> *Can you query a view instead of dataset?*

Yes, you can also query a view.

Performing a similarity search on a `DatasetView` will only return results from the view; if the view contains samples that were not included in the index, they will never be included in the result.

This means that you can index an entire Dataset once and then perform searches on subsets of the dataset by constructing views that contain the images of interest.

## Using LanceDB backend

By default, calling `compute_similarity()` or `sort_by_similarity()` will use an sklearn backend.

To use the LanceDB backend, simply set the optional `backend` parameter of `compute_similarity()` to `"lancedb"`:

Alternatively, you can configure FiftyOne to use the LanceDB backend by setting the following environment variable.

In your terminal, set the environment variable using:

<CodeGroup>
  <CodeBlock icon="linux">
    export FIFTYONE\_BRAIN\_DEFAULT\_SIMILARITY\_BACKEND=lancedb
  </CodeBlock>

  <CodeBlock icon="windows">
    \$Env:FIFTYONE\_BRAIN\_DEFAULT\_SIMILARITY\_BACKEND="lancedb" //powershell

    set FIFTYONE\_BRAIN\_DEFAULT\_SIMILARITY\_BACKEND=lancedb //cmd
  </CodeBlock>
</CodeGroup>

<Warning>
  This will only run during the terminal session. Once terminal is closed, environment variable is deleted.
</Warning>

Alternatively, you can **permanently** configure FiftyOne to use the LanceDB backend creating a `brain_config.json` at `~/.fiftyone/brain_config.json`. The JSON file may contain any desired subset of config fields that you wish to customize.

```json theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
{
  "default_similarity_backend": "lancedb"
}
```

This will override the default `brain_config` and will set it according to your customization. You can check the configuration by running the following code :

## LanceDB config parameters

The LanceDB backend supports query parameters that can be used to customize your similarity queries. These parameters include:

| Name            | Purpose                                                                                                          | Default          |
| :-------------- | :--------------------------------------------------------------------------------------------------------------- | :--------------- |
| **table\_name** | The name of the LanceDB table to use. If none is provided, a new table will be created                           | `None`           |
| **metric**      | The embedding distance metric to use when creating a new table. The supported values are ("cosine", "euclidean") | `"cosine"`       |
| **uri**         | The database URI to use. In this Database URI, tables will be created.                                           | `"/tmp/lancedb"` |

There are two ways to specify/customize the parameters:

1. **Using `brain_config.json` file**

```json theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
{
    "similarity_backends": {
        "lancedb": {
            "table_name": "your-table",
            "metric": "euclidean",
            "uri": "/tmp/lancedb"
        }
    }
}
```

2. **Directly passing to `compute_similarity()` to configure a specific new index** :

For a much more in depth walkthrough of the integration, visit the LanceDB x Voxel51 [docs page](https://docs.voxel51.com/integrations/lancedb.html).


# AWS Bedrock
Source: https://docs.lancedb.com/integrations/embedding/aws



AWS Bedrock supports multiple base models for generating text embeddings. You need to setup the AWS credentials to use this embedding function.
You can do so by using `awscli` and also add your session\_token:

```shell theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
aws configure
aws configure set aws_session_token "<your_session_token>"
```

to ensure that the credentials are set up correctly, you can run the following command:

```shell theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
aws sts get-caller-identity
```

Supported Embedding modelIDs are:

* `amazon.titan-embed-text-v1`
* `cohere.embed-english-v3`
* `cohere.embed-multilingual-v3`

Supported parameters (to be passed in `create` method) are:

| Parameter               | Type | Default Value                | Description                                                                                                                                                            |
| ----------------------- | ---- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **name**                | str  | "amazon.titan-embed-text-v1" | The model ID of the bedrock model to use. Supported base models for Text Embeddings: amazon.titan-embed-text-v1, cohere.embed-english-v3, cohere.embed-multilingual-v3 |
| **region**              | str  | "us-east-1"                  | Optional name of the AWS Region in which the service should be called (e.g., "us-east-1").                                                                             |
| **profile\_name**       | str  | None                         | Optional name of the AWS profile to use for calling the Bedrock service. If not specified, the default profile will be used.                                           |
| **assumed\_role**       | str  | None                         | Optional ARN of an AWS IAM role to assume for calling the Bedrock service. If not specified, the current active credentials will be used.                              |
| **role\_session\_name** | str  | "lancedb-embeddings"         | Optional name of the AWS IAM role session to use for calling the Bedrock service. If not specified, a "lancedb-embeddings" name will be used.                          |
| **runtime**             | bool | True                         | Optional choice of getting different client to perform operations with the Amazon Bedrock service.                                                                     |
| **max\_retries**        | int  | 7                            | Optional number of retries to perform when a request fails.                                                                                                            |

Usage Example:


# Cohere
Source: https://docs.lancedb.com/integrations/embedding/cohere



Using cohere API requires cohere package, which can be installed using `pip install cohere`. Cohere embeddings are used to generate embeddings for text data. The embeddings can be used for various tasks like semantic search, clustering, and classification.
You also need to set the `COHERE_API_KEY` environment variable to use the Cohere API.

Supported models are:

* embed-english-v3.0
* embed-multilingual-v3.0
* embed-english-light-v3.0
* embed-multilingual-light-v3.0
* embed-english-v2.0
* embed-english-light-v2.0
* embed-multilingual-v2.0

Supported parameters (to be passed in `create` method) are:

| Parameter           | Type  | Default Value          | Description                                                                                                                                                                                                                                                     |
| ------------------- | ----- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`              | `str` | `"embed-english-v2.0"` | The model ID of the cohere model to use. Supported base models for Text Embeddings: embed-english-v3.0, embed-multilingual-v3.0, embed-english-light-v3.0, embed-multilingual-light-v3.0, embed-english-v2.0, embed-english-light-v2.0, embed-multilingual-v2.0 |
| `source_input_type` | `str` | `"search_document"`    | The type of input data to be used for the source column.                                                                                                                                                                                                        |
| `query_input_type`  | `str` | `"search_query"`       | The type of input data to be used for the query.                                                                                                                                                                                                                |

Cohere supports following input types:

| Input Type              | Description                            |
| ----------------------- | -------------------------------------- |
| "`search_document`"     | Used for embeddings stored in a vector |
|                         | database for search use-cases.         |
| "`search_query`"        | Used for embeddings of search queries  |
|                         | run against a vector DB                |
| "`semantic_similarity`" | Specifies the given text will be used  |
|                         | for Semantic Textual Similarity (STS)  |
| "`classification`"      | Used for embeddings passed through a   |
|                         | text classifier.                       |
| "`clustering`"          | Used for the embeddings run through a  |
|                         | clustering algorithm                   |

Usage Example:


# ColPali
Source: https://docs.lancedb.com/integrations/embedding/colpali



We support [ColPali](https://github.com/illuin-tech/colpali) model embeddings for multimodal multi-vector retrieval. ColPali produces multiple embedding vectors per input (multi-vector), enabling more nuanced similarity matching between text queries and image documents.

Using ColPali requires the colpali-engine package, which can be installed using `pip install colpali-engine`.

<Info>
  ColPali produces **multi-vector** embeddings, meaning each input generates multiple embedding vectors rather than a single vector. Use `MultiVector(func.ndims())` instead of `Vector(func.ndims())` when defining your schema.
</Info>

Supported models are:

* Metric-AI/ColQwen2.5-3b-multilingual-v1.0 (default)
* vidore/colpali-v1.3
* vidore/colqwen2-v1.0
* vidore/colSmol-256M

Supported parameters (to be passed in `create` method) are:

| Parameter             | Type                           | Default Value                                 | Description                                                               |
| --------------------- | ------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------- |
| `model_name`          | `str`                          | `"Metric-AI/ColQwen2.5-3b-multilingual-v1.0"` | The name of the model to use.                                             |
| `device`              | `str`                          | `"auto"`                                      | The device for inference. Can be `"auto"`, `"cpu"`, `"cuda"`, or `"mps"`. |
| `dtype`               | `str`                          | `"bfloat16"`                                  | Data type for model weights (bfloat16, float16, float32, float64).        |
| `pooling_strategy`    | `str`                          | `"hierarchical"`                              | Token pooling strategy: `"hierarchical"`, `"lambda"`, or `None`.          |
| `pool_factor`         | `int`                          | `2`                                           | Factor to reduce sequence length when pooling is enabled.                 |
| `batch_size`          | `int`                          | `2`                                           | Batch size for processing inputs.                                         |
| `quantization_config` | `Optional[BitsAndBytesConfig]` | `None`                                        | Quantization configuration for the model (requires bitsandbytes).         |

This embedding function supports ingesting images as both bytes and URLs. You can query them using text.

Now we can search using text queries:


# Gemini
Source: https://docs.lancedb.com/integrations/embedding/gemini



With Google's Gemini, you can represent text (words, sentences, and blocks of text) in a vectorized form, making it easier to compare and contrast embeddings. For example, two texts that share a similar subject matter or sentiment should have similar embeddings, which can be identified through mathematical comparison techniques such as cosine similarity. For more on how and why you should use embeddings, refer to the Embeddings guide.
The Gemini Embedding Model API supports various task types:

| Task Type               | Description                                                                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "`retrieval_query`"     | Specifies the given text is a query in a search/retrieval setting.                                                                                         |
| "`retrieval_document`"  | Specifies the given text is a document in a search/retrieval setting. Using this task type requires a title but is automatically proided by Embeddings API |
| "`semantic_similarity`" | Specifies the given text will be used for Semantic Textual Similarity (STS).                                                                               |
| "`classification`"      | Specifies that the embeddings will be used for classification.                                                                                             |
| "`clusering`"           | Specifies that the embeddings will be used for clustering.                                                                                                 |

Usage Example:


# Hugging Face
Source: https://docs.lancedb.com/integrations/embedding/huggingface



We offer support for all Hugging Face models (which can be loaded via [transformers](https://huggingface.co/docs/transformers/en/index) library). The default model is `colbert-ir/colbertv2.0` which also has its own special callout - `registry.get("colbert")`. Some Hugging Face models might require custom models defined on the HuggingFace Hub in their own modeling files. You may enable this by setting `trust_remote_code=True`. This option should only be set to True for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine.

Example usage:


# IBM watsonx
Source: https://docs.lancedb.com/integrations/embedding/ibm



Generate text embeddings using IBM's watsonx.ai platform.

## Supported Models

You can find a list of supported models at [IBM watsonx.ai Documentation](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models-embed.html?context=wx). The currently supported model names are:

* `ibm/slate-125m-english-rtrvr`
* `ibm/slate-30m-english-rtrvr`
* `sentence-transformers/all-minilm-l12-v2`
* `intfloat/multilingual-e5-large`

## Parameters

The following parameters can be passed to the `create` method:

| Parameter   | Type | Default Value                  | Description                                               |
| ----------- | ---- | ------------------------------ | --------------------------------------------------------- |
| name        | str  | "ibm/slate-125m-english-rtrvr" | The model ID of the watsonx.ai model to use               |
| api\_key    | str  | None                           | Optional IBM Cloud API key (or set `WATSONX_API_KEY`)     |
| project\_id | str  | None                           | Optional watsonx project ID (or set `WATSONX_PROJECT_ID`) |
| url         | str  | None                           | Optional custom URL for the watsonx.ai instance           |
| params      | dict | None                           | Optional additional parameters for the embedding model    |

## Usage Example

First, the watsonx.ai library is an optional dependency, so must be installed seperately:

```
pip install ibm-watsonx-ai
```

Optionally set environment variables (if not passing credentials to `create` directly):

```sh theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
export WATSONX_API_KEY="YOUR_WATSONX_API_KEY"
export WATSONX_PROJECT_ID="YOUR_WATSONX_PROJECT_ID"
```


# ImageBind
Source: https://docs.lancedb.com/integrations/embedding/imagebind



We have support for [imagebind](https://github.com/facebookresearch/ImageBind) model embeddings. You can download our version of the packaged model via - `pip install imagebind-packaged==0.1.2`.

This function is registered as `imagebind` and supports Audio, Video and Text modalities(extending to Thermal,Depth,IMU data):

| Parameter   | Type   | Default Value      | Description                                                    |
| ----------- | ------ | ------------------ | -------------------------------------------------------------- |
| `name`      | `str`  | `"imagebind_huge"` | Name of the model.                                             |
| `device`    | `str`  | `"cpu"`            | The device to run the model on. Can be `"cpu"` or `"gpu"`.     |
| `normalize` | `bool` | `False`            | set to `True` to normalize your inputs before model ingestion. |

Below is an example demonstrating how the API works:

Now, we can search using any modality:

#### image search

#### audio search

#### Text search

You can add any input query and fetch the result as follows:

If you have any questions about the embeddings API, supported models, or see a relevant model missing, please raise an issue [on GitHub](https://github.com/lancedb/lancedb/issues).


# Instructor
Source: https://docs.lancedb.com/integrations/embedding/instructor



[Instructor](https://instructor-embedding.github.io/) is an instruction-finetuned text embedding model that can generate text embeddings tailored to any task (e.g. classification, retrieval, clustering, text evaluation, etc.) and domains (e.g. science, finance, etc.) by simply providing the task instruction, without any finetuning.

If you want to calculate customized embeddings for specific sentences, you can follow the unified template to write instructions.

<Info>
  Represent the `domain` `text_type` for `task_objective`:

  * `domain` is optional, and it specifies the domain of the text, e.g. science, finance, medicine, etc.
  * `text_type` is required, and it specifies the encoding unit, e.g. sentence, document, paragraph, etc.
  * `task_objective` is optional, and it specifies the objective of embedding, e.g. retrieve a document, classify the sentence, etc.
</Info>

More information about the model can be found at the [source URL](https://github.com/xlang-ai/instructor-embedding).

| Argument               | Type   | Default                                                              | Description                                               |
| ---------------------- | ------ | -------------------------------------------------------------------- | --------------------------------------------------------- |
| `name`                 | `str`  | "hkunlp/instructor-base"                                             | The name of the model to use                              |
| `batch_size`           | `int`  | `32`                                                                 | The batch size to use when generating embeddings          |
| `device`               | `str`  | `"cpu"`                                                              | The device to use when generating embeddings              |
| `show_progress_bar`    | `bool` | `True`                                                               | Whether to show a progress bar when generating embeddings |
| `normalize_embeddings` | `bool` | `True`                                                               | Whether to normalize the embeddings                       |
| `quantize`             | `bool` | `False`                                                              | Whether to quantize the model                             |
| `source_instruction`   | `str`  | `"represent the document for retrieval"`                             | The instruction for the source column                     |
| `query_instruction`    | `str`  | `"represent the document for retrieving the most similar documents"` | The instruction for the query                             |


# Jina
Source: https://docs.lancedb.com/integrations/embedding/jina



## Text Embedding Models

Jina embeddings are used to generate embeddings for text and image data.
You also need to set the `JINA_API_KEY` environment variable to use the Jina API.

You can find a list of supported models under [https://jina.ai/embeddings/](https://jina.ai/embeddings/)

Supported parameters (to be passed in `create` method) are:

| Parameter | Type  | Default Value    | Description                           |
| --------- | ----- | ---------------- | ------------------------------------- |
| `name`    | `str` | `"jina-clip-v1"` | The model ID of the jina model to use |

Usage Example:

## Multimodal Embedding Models

Jina embeddings can also be used to embed both text and image data, only some of the models support image data and you can check the list
under [https://jina.ai/embeddings/](https://jina.ai/embeddings/)

Supported parameters (to be passed in `create` method) are:

| Parameter | Type  | Default Value    | Description                           |
| --------- | ----- | ---------------- | ------------------------------------- |
| `name`    | `str` | `"jina-clip-v1"` | The model ID of the jina model to use |

Usage Example:


# Ollama
Source: https://docs.lancedb.com/integrations/embedding/ollama



Generate embeddings via the [ollama](https://github.com/ollama/ollama-python) python library. More details:

* [Ollama docs on embeddings](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings)
* [Ollama blog on embeddings](https://ollama.com/blog/embedding-models)

| Parameter              | Type                       | Default Value            | Description                                                                                      |
| ---------------------- | -------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------ |
| `name`                 | `str`                      | `nomic-embed-text`       | The name of the model.                                                                           |
| `host`                 | `str`                      | `http://localhost:11434` | The Ollama host to connect to.                                                                   |
| `options`              | `ollama.Options` or `dict` | `None`                   | Additional model parameters listed in the documentation for the Modelfile such as `temperature`. |
| `keep_alive`           | `float` or `str`           | `"5m"`                   | Controls how long the model will stay loaded into memory following the request.                  |
| `ollama_client_kwargs` | `dict`                     | `{}`                     | kwargs that can be past to the `ollama.Client`.                                                  |


# OpenAI
Source: https://docs.lancedb.com/integrations/embedding/openai



LanceDB registers the OpenAI embeddings function in the registry by default, as `openai`. Below are the parameters that you can customize when creating the instances:

| Parameter   | Type  | Default Value              | Description                                                                                                                             |
| ----------- | ----- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `name`      | `str` | `"text-embedding-ada-002"` | The name of the model.                                                                                                                  |
| `dim`       | `int` | Model default              | For OpenAI's newer text-embedding-3 model, we can specify a dimensionality that is smaller than the 1536 size. This feature supports it |
| `use_azure` | bool  | `False`                    | Set true to use Azure OpenAPI SDK                                                                                                       |


# OpenCLIP
Source: https://docs.lancedb.com/integrations/embedding/openclip



We support CLIP model embeddings using the open source alternative, [open-clip](https://github.com/mlfoundations/open_clip) which supports various customizations. It is registered as `open-clip` and supports the following customizations:

| Parameter    | Type   | Default Value         | Description                                                             |
| ------------ | ------ | --------------------- | ----------------------------------------------------------------------- |
| `name`       | `str`  | `"ViT-B-32"`          | The name of the model.                                                  |
| `pretrained` | `str`  | `"laion2b_s34b_b79k"` | The name of the pretrained model to load.                               |
| `device`     | `str`  | `"cpu"`               | The device to run the model on. Can be `"cpu"` or `"gpu"`.              |
| `batch_size` | `int`  | `64`                  | The number of images to process in a batch.                             |
| `normalize`  | `bool` | `True`                | Whether to normalize the input images before feeding them to the model. |

This embedding function supports ingesting images as both bytes and urls. You can query them using both test and other images.

<Info>
  LanceDB supports ingesting images directly from accessible links.
</Info>

Now we can search using text from both the default vector column and the custom vector column

Because we're using a multimodal embedding function, we can also search using images


# Sentence Transformers
Source: https://docs.lancedb.com/integrations/embedding/sentence-transformers



Allows you to set parameters when registering a `sentence-transformers` object.

<Info>
  Sentence transformer embeddings are normalized by default. It is recommended to use normalized embeddings for similarity search.
</Info>

| Parameter           | Type   | Default Value      | Description                                                                      |
| ------------------- | ------ | ------------------ | -------------------------------------------------------------------------------- |
| `name`              | `str`  | `all-MiniLM-L6-v2` | The name of the model                                                            |
| `device`            | `str`  | `cpu`              | The device to run the model on (can be `cpu` or `gpu`)                           |
| `normalize`         | `bool` | `True`             | Whether to normalize the input text before feeding it to the model               |
| `trust_remote_code` | `bool` | `False`            | Whether to trust and execute remote code from the model's Huggingface repository |

<Details title="Check out available sentence-transformer models here!">
  ```markdown theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
      - sentence-transformers/all-MiniLM-L12-v2
      - sentence-transformers/paraphrase-mpnet-base-v2
      - sentence-transformers/gtr-t5-base
      - sentence-transformers/LaBSE
      - sentence-transformers/all-MiniLM-L6-v2
      - sentence-transformers/bert-base-nli-max-tokens
      - sentence-transformers/bert-base-nli-mean-tokens
      - sentence-transformers/bert-base-nli-stsb-mean-tokens
      - sentence-transformers/bert-base-wikipedia-sections-mean-tokens
      - sentence-transformers/bert-large-nli-cls-token
      - sentence-transformers/bert-large-nli-max-tokens
      - sentence-transformers/bert-large-nli-mean-tokens
      - sentence-transformers/bert-large-nli-stsb-mean-tokens
      - sentence-transformers/distilbert-base-nli-max-tokens
      - sentence-transformers/distilbert-base-nli-mean-tokens
      - sentence-transformers/distilbert-base-nli-stsb-mean-tokens
      - sentence-transformers/distilroberta-base-msmarco-v1
      - sentence-transformers/distilroberta-base-msmarco-v2
      - sentence-transformers/nli-bert-base-cls-pooling
      - sentence-transformers/nli-bert-base-max-pooling
      - sentence-transformers/nli-bert-base
      - sentence-transformers/nli-bert-large-cls-pooling
      - sentence-transformers/nli-bert-large-max-pooling
      - sentence-transformers/nli-bert-large
      - sentence-transformers/nli-distilbert-base-max-pooling
      - sentence-transformers/nli-distilbert-base
      - sentence-transformers/nli-roberta-base
      - sentence-transformers/nli-roberta-large
      - sentence-transformers/roberta-base-nli-mean-tokens
      - sentence-transformers/roberta-base-nli-stsb-mean-tokens
      - sentence-transformers/roberta-large-nli-mean-tokens
      - sentence-transformers/roberta-large-nli-stsb-mean-tokens
      - sentence-transformers/stsb-bert-base
      - sentence-transformers/stsb-bert-large
      - sentence-transformers/stsb-distilbert-base
      - sentence-transformers/stsb-roberta-base
      - sentence-transformers/stsb-roberta-large
      - sentence-transformers/xlm-r-100langs-bert-base-nli-mean-tokens
      - sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens
      - sentence-transformers/xlm-r-base-en-ko-nli-ststb
      - sentence-transformers/xlm-r-bert-base-nli-mean-tokens
      - sentence-transformers/xlm-r-bert-base-nli-stsb-mean-tokens
      - sentence-transformers/xlm-r-large-en-ko-nli-ststb
      - sentence-transformers/bert-base-nli-cls-token
      - sentence-transformers/all-distilroberta-v1
      - sentence-transformers/multi-qa-MiniLM-L6-dot-v1
      - sentence-transformers/multi-qa-distilbert-cos-v1
      - sentence-transformers/multi-qa-distilbert-dot-v1
      - sentence-transformers/multi-qa-mpnet-base-cos-v1
      - sentence-transformers/multi-qa-mpnet-base-dot-v1
      - sentence-transformers/nli-distilroberta-base-v2
      - sentence-transformers/all-MiniLM-L6-v1
      - sentence-transformers/all-mpnet-base-v1
      - sentence-transformers/all-mpnet-base-v2
      - sentence-transformers/all-roberta-large-v1
      - sentence-transformers/allenai-specter
      - sentence-transformers/average_word_embeddings_glove.6B.300d
      - sentence-transformers/average_word_embeddings_glove.840B.300d
      - sentence-transformers/average_word_embeddings_komninos
      - sentence-transformers/average_word_embeddings_levy_dependency
      - sentence-transformers/clip-ViT-B-32-multilingual-v1
      - sentence-transformers/clip-ViT-B-32
      - sentence-transformers/distilbert-base-nli-stsb-quora-ranking
      - sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking
      - sentence-transformers/distilroberta-base-paraphrase-v1
      - sentence-transformers/distiluse-base-multilingual-cased-v1
      - sentence-transformers/distiluse-base-multilingual-cased-v2
      - sentence-transformers/distiluse-base-multilingual-cased
      - sentence-transformers/facebook-dpr-ctx_encoder-multiset-base
      - sentence-transformers/facebook-dpr-ctx_encoder-single-nq-base
      - sentence-transformers/facebook-dpr-question_encoder-multiset-base
      - sentence-transformers/facebook-dpr-question_encoder-single-nq-base
      - sentence-transformers/gtr-t5-large
      - sentence-transformers/gtr-t5-xl
      - sentence-transformers/gtr-t5-xxl
      - sentence-transformers/msmarco-MiniLM-L-12-v3
      - sentence-transformers/msmarco-MiniLM-L-6-v3
      - sentence-transformers/msmarco-MiniLM-L12-cos-v5
      - sentence-transformers/msmarco-MiniLM-L6-cos-v5
      - sentence-transformers/msmarco-bert-base-dot-v5
      - sentence-transformers/msmarco-bert-co-condensor
      - sentence-transformers/msmarco-distilbert-base-dot-prod-v3
      - sentence-transformers/msmarco-distilbert-base-tas-b
      - sentence-transformers/msmarco-distilbert-base-v2
      - sentence-transformers/msmarco-distilbert-base-v3
      - sentence-transformers/msmarco-distilbert-base-v4
      - sentence-transformers/msmarco-distilbert-cos-v5
      - sentence-transformers/msmarco-distilbert-dot-v5
      - sentence-transformers/msmarco-distilbert-multilingual-en-de-v2-tmp-lng-aligned
      - sentence-transformers/msmarco-distilbert-multilingual-en-de-v2-tmp-trained-scratch
      - sentence-transformers/msmarco-distilroberta-base-v2
      - sentence-transformers/msmarco-roberta-base-ance-firstp
      - sentence-transformers/msmarco-roberta-base-v2
      - sentence-transformers/msmarco-roberta-base-v3
      - sentence-transformers/multi-qa-MiniLM-L6-cos-v1
      - sentence-transformers/nli-mpnet-base-v2
      - sentence-transformers/nli-roberta-base-v2
      - sentence-transformers/nq-distilbert-base-v1
      - sentence-transformers/paraphrase-MiniLM-L12-v2
      - sentence-transformers/paraphrase-MiniLM-L3-v2
      - sentence-transformers/paraphrase-MiniLM-L6-v2
      - sentence-transformers/paraphrase-TinyBERT-L6-v2
      - sentence-transformers/paraphrase-albert-base-v2
      - sentence-transformers/paraphrase-albert-small-v2
      - sentence-transformers/paraphrase-distilroberta-base-v1
      - sentence-transformers/paraphrase-distilroberta-base-v2
      - sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
      - sentence-transformers/paraphrase-multilingual-mpnet-base-v2
      - sentence-transformers/paraphrase-xlm-r-multilingual-v1
      - sentence-transformers/quora-distilbert-base
      - sentence-transformers/quora-distilbert-multilingual
      - sentence-transformers/sentence-t5-base
      - sentence-transformers/sentence-t5-large
      - sentence-transformers/sentence-t5-xxl
      - sentence-transformers/sentence-t5-xl
      - sentence-transformers/stsb-distilroberta-base-v2
      - sentence-transformers/stsb-mpnet-base-v2
      - sentence-transformers/stsb-roberta-base-v2
      - sentence-transformers/stsb-xlm-r-multilingual
      - sentence-transformers/xlm-r-distilroberta-base-paraphrase-v1
      - sentence-transformers/clip-ViT-L-14
      - sentence-transformers/clip-ViT-B-16
      - sentence-transformers/use-cmlm-multilingual
      - sentence-transformers/all-MiniLM-L12-v1
  ```
</Details>

<Info>
  You can also load many other model architectures from the library. For example models from sources such as BAAI, Nomic, Salesforce Research, etc. See this HF hub page for all [supported models](https://huggingface.co/models?library=sentence-transformers).
</Info>

<Note title="BAAI embeddings example">
  Here is an example that uses the BAAI embedding model from the Hugging Face Hub [supported models](https://huggingface.co/models?library=sentence-transformers).
</Note>

Visit sentence-transformers [HuggingFace HUB](https://huggingface.co/sentence-transformers) page for more information on the available models.


# VoyageAI
Source: https://docs.lancedb.com/integrations/embedding/voyageai



Voyage AI provides cutting-edge embedding and rerankers.

Using voyageai API requires voyageai package, which can be installed using `pip install voyageai`. Voyage AI embeddings are used to generate embeddings for text data. The embeddings can be used for various tasks like semantic search, clustering, and classification.
You also need to set the `VOYAGE_API_KEY` environment variable to use the VoyageAI API.

Supported models are:

* voyage-context-3
* voyage-3.5
* voyage-3.5-lite
* voyage-3
* voyage-3-lite
* voyage-finance-2
* voyage-multilingual-2
* voyage-law-2
* voyage-code-2
* voyage-multimodal-3.5 (multimodal - supports text, images, and video)

<Info>
  **Multimodal Model:** `voyage-multimodal-3.5` supports text, images, and video inputs. It outputs 1024-dimensional embeddings by default, configurable via the `output_dimension` parameter (256, 512, 1024, 2048). See the [VoyageAI multimodal embeddings documentation](https://docs.voyageai.com/docs/multimodal-embeddings) for more details.
</Info>

Supported parameters (to be passed in `create` method) are:

| Parameter          | Type   | Default Value | Description                                                                                                                                                                                                             |
| ------------------ | ------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`             | `str`  | `None`        | The model ID of the model to use. Supported models: voyage-3, voyage-3-lite, voyage-3.5, voyage-3.5-lite, voyage-context-3, voyage-finance-2, voyage-multilingual-2, voyage-law-2, voyage-code-2, voyage-multimodal-3.5 |
| `input_type`       | `str`  | `None`        | Type of the input text. Default to None. Other options: query, document.                                                                                                                                                |
| `truncation`       | `bool` | `True`        | Whether to truncate the input texts to fit within the context length.                                                                                                                                                   |
| `output_dimension` | `int`  | `None`        | Output embedding dimension. Only supported by `voyage-multimodal-3.5`. Valid options: 256, 512, 1024 (default), 2048.                                                                                                   |

Usage Example:

### Multimodal Example

The `voyage-multimodal-3.5` model can embed text alongside images. You can use image URLs, file paths, or PIL Image objects:


# Integrations
Source: https://docs.lancedb.com/integrations/index

Connect LanceDB with popular AI providers, frameworks, and data platforms

LanceDB seamlessly plugs into the rest of your AI and data engineering stack. Use the sections
below to jump straight into the guides that matter for your workflow.

| Group                                              | Description                                                                                     |
| :------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [Embedding models](/integrations/embedding/)       | Connect with popular embedding model providers including OpenAI, Cohere, Hugging Face, and more |
| [Reranking models](/integrations/reranking/)       | Enhance search results with advanced reranking models and techniques                            |
| [AI platforms & frameworks](/integrations/ai/)     | Integrate with LangChain, LlamaIndex, Kiln, and other AI development frameworks                 |
| [Data platforms & frameworks](/integrations/data/) | Integrate LanceDB with popular data tools and platforms like DuckDB, Pydantic and dlt           |


# Answer.AI Rerankers
Source: https://docs.lancedb.com/integrations/reranking/answerdotai

Use AnswerDotAI's lightweight reranking library with LanceDB. Features unified API for common reranking models, configurable model selection, and comprehensive scoring options.

# Answer.AI Rerankers

This integration uses [AnswersDotAI's rerankers](https://github.com/AnswerDotAI/rerankers) to rerank the search results, providing a lightweight, low-dependency, unified API to use all common reranking and cross-encoder models.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

## Accepted Arguments

| Argument       | Type  | Default                                   | Description                                                                                                                                                                                                                                   |
| -------------- | ----- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_type`   | `str` | `"colbert"`                               | The type of model to use. Supported model types can be found here: [https://github.com/AnswerDotAI/rerankers](https://github.com/AnswerDotAI/rerankers).                                                                                      |
| `model_name`   | `str` | `"answerdotai/answerai-colbert-small-v1"` | The name of the reranker model to use.                                                                                                                                                                                                        |
| `column`       | `str` | `"text"`                                  | The name of the column to use as input to the cross encoder model.                                                                                                                                                                            |
| `return_score` | `str` | `"relevance"`                             | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all" is supported, will return relevance score along with the vector and/or fts scores depending on query type. |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status          | Description                                                                                           |
| -------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported     | Results only have the `_relevance_score` column.                                                      |
| `all`          | ❌ Not Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |

### Vector Search

| `return_score` | Status      | Description                                                                          |
| -------------- | ----------- | ------------------------------------------------------------------------------------ |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                                     |
| `all`          | ✅ Supported | Results have vector(`_distance`) along with Hybrid Search score(`_relevance_score`). |

### FTS Search

| `return_score` | Status      | Description                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                              |
| `all`          | ✅ Supported | Results have FTS(`score`) along with Hybrid Search score(`_relevance_score`). |


# Cohere Reranker
Source: https://docs.lancedb.com/integrations/reranking/cohere

Integrate Cohere's powerful reranking API with LanceDB for enhanced search results. Supports English and multilingual models with configurable scoring options for vector, FTS, and hybrid search.

# Cohere Reranker

This reranker uses the [Cohere](https://cohere.ai/) API to rerank the search results. You can use this reranker by passing `CohereReranker()` to the `rerank()` method. Note that you'll either need to set the `COHERE_API_KEY` environment variable or pass the `api_key` argument to use this reranker.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

```shell theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
pip install cohere
```

## Accepted Arguments

| Argument       | Type  | Default                 | Description                                                                                                                                                                                                                                  |
| -------------- | ----- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_name`   | `str` | `"rerank-english-v2.0"` | The name of the reranker model to use. Available cohere models are: rerank-english-v2.0, rerank-multilingual-v2.0                                                                                                                            |
| `column`       | `str` | `"text"`                | The name of the column to use as input to the cross encoder model.                                                                                                                                                                           |
| `top_n`        | `str` | `None`                  | The number of results to return. If None, will return all results.                                                                                                                                                                           |
| `api_key`      | `str` | `None`                  | The API key for the Cohere API. If not provided, the `COHERE_API_KEY` environment variable is used.                                                                                                                                          |
| `return_score` | `str` | `"relevance"`           | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all" is supported, will return relevance score along with the vector and/or fts scores depending on query type |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status          | Description                                                                                          |
| -------------- | --------------- | ---------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported     | Results only have the `_relevance_score` column                                                      |
| `all`          | ❌ Not Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`) |

### Vector Search

| `return_score` | Status      | Description                                                                         |
| -------------- | ----------- | ----------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column                                     |
| `all`          | ✅ Supported | Results have vector(`_distance`) along with Hybrid Search score(`_relevance_score`) |

### FTS Search

| `return_score` | Status      | Description                                                                  |
| -------------- | ----------- | ---------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column                              |
| `all`          | ✅ Supported | Results have FTS(`score`) along with Hybrid Search score(`_relevance_score`) |


# ColBERT Reranker
Source: https://docs.lancedb.com/integrations/reranking/colbert

Enhance search results with ColBERT's contextual reranking in LanceDB. Features efficient model deployment, device optimization, and flexible scoring options for vector, FTS, and hybrid search.

# ColBERT Reranker

This reranker uses ColBERT model to rerank the search results. You can use this reranker by passing `ColbertReranker()` to the `rerank()` method.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

## Accepted Arguments

| Argument       | Type  | Default                    | Description                                                                                                                                                                                                                                   |
| -------------- | ----- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_name`   | `str` | `"colbert-ir/colbertv2.0"` | The name of the reranker model to use.                                                                                                                                                                                                        |
| `column`       | `str` | `"text"`                   | The name of the column to use as input to the cross encoder model.                                                                                                                                                                            |
| `device`       | `str` | `None`                     | The device to use for the cross encoder model. If None, will use "cuda" if available, otherwise "cpu".                                                                                                                                        |
| `return_score` | `str` | `"relevance"`              | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all" is supported, will return relevance score along with the vector and/or fts scores depending on query type. |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status          | Description                                                                                           |
| -------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported     | Results only have the `_relevance_score` column.                                                      |
| `all`          | ❌ Not Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |

### Vector Search

| `return_score` | Status      | Description                                                                          |
| -------------- | ----------- | ------------------------------------------------------------------------------------ |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                                     |
| `all`          | ✅ Supported | Results have vector(`_distance`) along with Hybrid Search score(`_relevance_score`). |

### FTS Search

| `return_score` | Status      | Description                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                              |
| `all`          | ✅ Supported | Results have FTS(`score`) along with Hybrid Search score(`_relevance_score`). |


# Cross Encoder Reranker
Source: https://docs.lancedb.com/integrations/reranking/cross_encoder

Implement semantic search reranking in LanceDB using Cross Encoder models. Features configurable model selection, device optimization, and comprehensive scoring options for all search types.

# Cross Encoder Reranker

This reranker uses Cross Encoder models from sentence-transformers to rerank the search results. You can use this reranker by passing `CrossEncoderReranker()` to the `rerank()` method.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

## Accepted Arguments

| Argument       | Type  | Default                                  | Description                                                                                                                                                                                                                                   |
| -------------- | ----- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_name`   | `str` | `""cross-encoder/ms-marco-TinyBERT-L-6"` | The name of the reranker model to use.                                                                                                                                                                                                        |
| `column`       | `str` | `"text"`                                 | The name of the column to use as input to the cross encoder model.                                                                                                                                                                            |
| `device`       | `str` | `None`                                   | The device to use for the cross encoder model. If None, will use "cuda" if available, otherwise "cpu".                                                                                                                                        |
| `return_score` | `str` | `"relevance"`                            | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all" is supported, will return relevance score along with the vector and/or fts scores depending on query type. |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status          | Description                                                                                           |
| -------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported     | Results only have the `_relevance_score` column.                                                      |
| `all`          | ❌ Not Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |

### Vector Search

| `return_score` | Status      | Description                                                                          |
| -------------- | ----------- | ------------------------------------------------------------------------------------ |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                                     |
| `all`          | ✅ Supported | Results have vector(`_distance`) along with Hybrid Search score(`_relevance_score`). |

### FTS Search

| `return_score` | Status      | Description                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                              |
| `all`          | ✅ Supported | Results have FTS(`score`) along with Hybrid Search score(`_relevance_score`). |


# Jina Reranker
Source: https://docs.lancedb.com/integrations/reranking/jina

Integrate Jina's multilingual reranking API with LanceDB for improved search results. Features model selection, API key management, and flexible scoring options for all search types.

# Jina Reranker

This reranker uses the [Jina](https://jina.ai/reranker/) API to rerank the search results. You can use this reranker by passing `JinaReranker()` to the `rerank()` method. Note that you'll either need to set the `JINA_API_KEY` environment variable or pass the `api_key` argument to use this reranker.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

## Accepted Arguments

| Argument       | Type  | Default                                | Description                                                                                                                                                                                                                                   |
| -------------- | ----- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_name`   | `str` | `"jina-reranker-v2-base-multilingual"` | The name of the reranker model to use. You can find the list of available models in [https://jina.ai/reranker](https://jina.ai/reranker).                                                                                                     |
| `column`       | `str` | `"text"`                               | The name of the column to use as input to the cross encoder model.                                                                                                                                                                            |
| `top_n`        | `str` | `None`                                 | The number of results to return. If None, will return all results.                                                                                                                                                                            |
| `api_key`      | `str` | `None`                                 | The API key for the Jina API. If not provided, the `JINA_API_KEY` environment variable is used.                                                                                                                                               |
| `return_score` | `str` | `"relevance"`                          | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all" is supported, will return relevance score along with the vector and/or fts scores depending on query type. |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status          | Description                                                                                           |
| -------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported     | Results only have the `_relevance_score` column.                                                      |
| `all`          | ❌ Not Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |

### Vector Search

| `return_score` | Status      | Description                                                                          |
| -------------- | ----------- | ------------------------------------------------------------------------------------ |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                                     |
| `all`          | ✅ Supported | Results have vector(`_distance`) along with Hybrid Search score(`_relevance_score`). |

### FTS Search

| `return_score` | Status      | Description                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                              |
| `all`          | ✅ Supported | Results have FTS(`score`) along with Hybrid Search score(`_relevance_score`). |


# Linear Combination Reranker
Source: https://docs.lancedb.com/integrations/reranking/linear_combination

Learn about LanceDB's deprecated Linear Combination Reranker for combining semantic and full-text search scores.

# Linear Combination Reranker

> **Note:** This reranker is deprecated. Use the `RRFReranker` if you need a score-based reranker.

The Linear Combination Reranker combines the results of semantic and full-text search using a linear combination of the scores. The weights for the linear combination can be specified, and defaults to 0.7, i.e, 70% weight for semantic search and 30% weight for full-text search.

> **Note:** Supported query type – Hybrid search only.

## Accepted Arguments

| Argument       | Type    | Default       | Description                                                                                                                                                                                                               |
| -------------- | ------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `weight`       | `float` | `0.7`         | The weight to use for the semantic search score. The weight for the full-text search score is `1 - weights`.                                                                                                              |
| `return_score` | `str`   | `"relevance"` | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all", will return all scores from the vector and FTS search along with the relevance score. |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status      | Description                                                                                   |
| -------------- | ----------- | --------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column                                               |
| `all`          | ✅ Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_distance`) |


# MRR Reranker
Source: https://docs.lancedb.com/integrations/reranking/mrr

Combine and rerank search results using Mean Reciprocal Rank (MRR) algorithm in LanceDB. Supports weighted scoring for hybrid and multivector search.

# MRR Reranker

This reranker uses the Mean Reciprocal Rank (MRR) algorithm to combine and rerank search results from vector and full-text search. You can use this reranker by passing `MRRReranker()` to the `rerank()` method. The MRR algorithm calculates the average of reciprocal ranks across different search results, providing a balanced way to merge results from multiple ranking systems.

> **Note:** Supported query types – Hybrid and Multivector search.

## Accepted Arguments

| Argument        | Type    | Default       | Description                                                                                                                                                                                                             |
| --------------- | ------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `weight_vector` | `float` | `0.5`         | Weight for vector search results (0.0 to 1.0).                                                                                                                                                                          |
| `weight_fts`    | `float` | `0.5`         | Weight for FTS search results (0.0 to 1.0).                                                                                                                                                                             |
| `return_score`  | `str`   | `"relevance"` | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the `_relevance_score`. If "all", will return all scores from the vector and FTS search along with the relevance score. |

**Note:** `weight_vector` + `weight_fts` must equal 1.0.

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status      | Description                                                                                           |
| -------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                                                      |
| `all`          | ✅ Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |

### Multivector Search

| `return_score` | Status      | Description                                                                    |
| -------------- | ----------- | ------------------------------------------------------------------------------ |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                               |
| `all`          | ✅ Supported | Results have vector distances from all searches along with `_relevance_score`. |


# OpenAI Reranker (Experimental)
Source: https://docs.lancedb.com/integrations/reranking/openai

Explore experimental search reranking using OpenAI's GPT models in LanceDB. Features configurable model selection, API key management, and comprehensive scoring options for all search types.

# OpenAI Reranker (Experimental)

This reranker uses OpenAI chat model to rerank the search results. You can use this reranker by passing `OpenAI()` to the `rerank()` method.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

> **Warning:** This reranker is experimental. OpenAI does not have a dedicated reranking model, so it uses a chat model under the hood.

## Accepted Arguments

| Argument       | Type  | Default                 | Description                                                                                                                                                                                                                                   |
| -------------- | ----- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_name`   | `str` | `"gpt-4-turbo-preview"` | The name of the reranker model to use.                                                                                                                                                                                                        |
| `column`       | `str` | `"text"`                | The name of the column to use as input to the cross encoder model.                                                                                                                                                                            |
| `return_score` | `str` | `"relevance"`           | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all" is supported, will return relevance score along with the vector and/or fts scores depending on query type. |
| `api_key`      | `str` | `None`                  | The API key to use. If None, will use the OPENAI\_API\_KEY environment variable.                                                                                                                                                              |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status          | Description                                                                                           |
| -------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported     | Results only have the `_relevance_score` column.                                                      |
| `all`          | ❌ Not Supported | Results have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |

### Vector Search

| `return_score` | Status      | Description                                                                          |
| -------------- | ----------- | ------------------------------------------------------------------------------------ |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                                     |
| `all`          | ✅ Supported | Results have vector(`_distance`) along with Hybrid Search score(`_relevance_score`). |

### FTS Search

| `return_score` | Status      | Description                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Results only have the `_relevance_score` column.                              |
| `all`          | ✅ Supported | Results have FTS(`score`) along with Hybrid Search score(`_relevance_score`). |


# Reciprocal Rank Fusion Reranker
Source: https://docs.lancedb.com/integrations/reranking/rrf

Learn about LanceDB's default Reciprocal Rank Fusion (RRF) reranker for hybrid search. Implements the Cormack et al. algorithm for optimal search result ranking.

# Reciprocal Rank Fusion Reranker

This is the default reranker used by LanceDB hybrid search. Reciprocal Rank Fusion (RRF) is an algorithm that evaluates the search scores by leveraging the positions/rank of the documents. The implementation follows this [paper](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf).

> **Note:** Supported query type – Hybrid search.

## Accepted Arguments

| Argument       | Type  | Default       | Description                                                                                                                                                                                                             |
| -------------- | ----- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `K`            | `int` | `60`          | A constant used in the RRF formula (default is 60). Experiments indicate that k = 60 was near-optimal, but that the choice is not critical.                                                                             |
| `return_score` | `str` | `"relevance"` | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the `_relevance_score`. If "all", will return all scores from the vector and FTS search along with the relevance score. |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status      | Description                                                                                                 |
| -------------- | ----------- | ----------------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Returned rows only have the `_relevance_score` column.                                                      |
| `all`          | ✅ Supported | Returned rows have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |


# VoyageAI Reranker
Source: https://docs.lancedb.com/integrations/reranking/voyageai

Integrate VoyageAI's cutting-edge reranking models with LanceDB. Features model selection, API key management, and comprehensive scoring options for all search types.

# VoyageAI Reranker

Voyage AI provides cutting-edge embedding and rerankers.

This reranker uses the [VoyageAI](https://docs.voyageai.com/docs/) API to rerank the search results. You can use this reranker by passing `VoyageAIReranker()` to the `rerank()` method. Note that you'll either need to set the `VOYAGE_API_KEY` environment variable or pass the `api_key` argument to use this reranker.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

## Accepted Arguments

| Argument       | Type   | Default       | Description                                                                                                                                                                                                                                  |
| -------------- | ------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_name`   | `str`  | `None`        | The name of the reranker model to use. Available models are: rerank-2, rerank-2-lite                                                                                                                                                         |
| `column`       | `str`  | `"text"`      | The name of the column to use as input to the cross encoder model.                                                                                                                                                                           |
| `top_n`        | `str`  | `None`        | The number of results to return. If None, will return all results.                                                                                                                                                                           |
| `api_key`      | `str`  | `None`        | The API key for the Voyage AI API. If not provided, the `VOYAGE_API_KEY` environment variable is used.                                                                                                                                       |
| `return_score` | `str`  | `"relevance"` | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the \`\_relevance\_score. If "all" is supported, will return relevance score along with the vector and/or fts scores depending on query type |
| `truncation`   | `bool` | `None`        | Whether to truncate the input to satisfy the "context length limit" on the query and the documents.                                                                                                                                          |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status          | Description                                                                                          |
| -------------- | --------------- | ---------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported     | Returns only have the `_relevance_score` column                                                      |
| `all`          | ❌ Not Supported | Returns have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`) |

### Vector Search

| `return_score` | Status      | Description                                                                         |
| -------------- | ----------- | ----------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Returns only have the `_relevance_score` column                                     |
| `all`          | ✅ Supported | Returns have vector(`_distance`) along with Hybrid Search score(`_relevance_score`) |

### FTS Search

| `return_score` | Status      | Description                                                                  |
| -------------- | ----------- | ---------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Returns only have the `_relevance_score` column                              |
| `all`          | ✅ Supported | Returns have FTS(`score`) along with Hybrid Search score(`_relevance_score`) |


# Lance format
Source: https://docs.lancedb.com/lance

Open-source lakehouse format for multimodal AI.

[Lance](https://lance.org/) is an open-source lakehouse format, which provides the
foundation for LanceDB's capabilities. Lance combines the performance of Apache Arrow with advanced
features designed specifically for AI workloads.

<Card title="Lance format documentation" icon="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=1c7311e59aacc6a085345618f357d380" href="https://lance.org/quickstart">
  Learn more about the Lance format by reading the docs.
</Card>

## How Lance Enables the Multimodal Lakehouse

Lance is a file format, table format, and catalog spec for multimodal AI, allowing developers to build a
complete open lakehouse on top of object storage to power AI workflows. The format brings
high-performance vector search, full-text search, random access, and feature engineering capabilities
to a single unified system, eliminating the need for multiple specialized databases.

Unlike traditional vector databases that only store embeddings alongside the metadata, LanceDB's
multimodal lakehouse stores both the original data (including image, video or audio bytes)
and its vector representations alongside traditional tabular data in the same efficient format.

## Advantages of the Lance format

| Advantage          | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| Multimodal storage | Efficiently holds vectors, images, videos, audio, text, and more          |
| Version control    | Built-in data versioning for reproducible ML experiments and data lineage |
| ML-optimized       | Designed for training and inference workloads with fast random access     |
| Query performance  | Columnar storage enables blazing-fast vector search and analytics         |
| Cloud-native       | Seamless integration with cloud object stores (S3, GCS, Azure Blob)       |

## Key concepts

The following concepts are core to the Lance format:

<Steps>
  <Step>
    Data storage is **columnar** and is **interoperable** with other columnar formats (such as Parquet) via Arrow
  </Step>

  <Step>
    Data is divided into **fragments** that represent a subset of the data. Fragments are chunks of data in a Lance dataset. Each fragment includes multiple files that contain several columns in the chunk of data that it represents.
  </Step>

  <Step>
    Data is **versioned**, with each insert operation creating a new version of the dataset and an update to the manifest that tracks versions via metadata
  </Step>
</Steps>

### Data versioning

Data in Lance tables are versioned -- this helps keep LanceDB scalable and consistent.
We do not immediately blow away old versions when creating new ones because other clients might be
in the middle of querying the old version. It's important to retain older versions for as long as they
might be queried.

Each version contains metadata and just the new/updated data in your transaction. So if you have 100
versions, they aren't 100 duplicates of the same data. However, they do have 100x the metadata overhead
of a single version, which can result in slower queries.

### Data compaction

As you insert more data, your dataset will grow and you'll need to perform compaction to maintain query
throughput (i.e., keep latencies down to a minimum). Compaction is the process of merging fragments
together to reduce the amount of metadata that needs to be managed, and to reduce the number of files
that need to be opened while scanning the dataset.

### Performance Optimization Through Compaction

Compaction performs the following tasks in the background:

* Removes deleted rows from fragments
* Removes dropped columns from fragments
* Merges small fragments into larger ones

### Data deletion and recovery

Although Lance allows you to delete rows from a dataset, it does not actually delete the data immediately.
It simply marks the row as deleted in the `DataFile` that represents a fragment.

For a given version of the dataset, each fragment can have up to one deletion file (if no rows were ever
deleted from that fragment, it will not have a deletion file). This is important to keep in mind because
it means that the data is still there, and can be recovered if needed, as long as that version still
exists based on your backup policy.

<Card title="Learn more about Lance" icon="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=1c7311e59aacc6a085345618f357d380" href="https://lance.org/quickstart">
  Lance is a separate open source project. Check out its documentation to learn more.
</Card>


# Quickstart
Source: https://docs.lancedb.com/quickstart

Get started with LanceDB in minutes.

The easiest way to get started with LanceDB is the open source version, which is an embedded database that
runs in-process (like SQLite). Let's get started in just a few steps!

## 1. Install LanceDB

Install LanceDB in your client SDK.

<CodeGroup>
  ```bash Python icon=Python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  pip install lancedb  # or uv add lancedb
  ```

  ```bash TypeScript icon=js theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  npm install @lancedb/lancedb
  ```

  ```bash Rust icon=Rust theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  cargo add lancedb
  ```
</CodeGroup>

## 2. Connect to a LanceDB database

Using LanceDB's open source version is as simple as importing LanceDB as a library
and pointing to a local path -- no servers needed!

### Optional: LanceDB Cloud or Enterprise versions

If you're looking for a fully-managed solution,
you can use LanceDB Cloud, which provides managed infrastructure,
security, and automatic backups. Simply replace the local path with a remote `uri`
that points to where your data is stored, and you're ready to go.

For enormous scale and more advanced use cases beyond just search -- like
feature engineering, model training and more, check out [LanceDB Enterprise](/enterprise).

## 3. Obtain data and ingest into LanceDB

Let's look at an example. We have the following records of characters in an adventure board game.
The vector column holds 3-dimensional embeddings representing each character.

To ingest the data into LanceDB, obtain data of the required shape
and pass in the data object to the `create_table` method as shown below.
Note that LanceDB tables require a schema. If you don't provide one, LanceDB
will infer it from the data.

<Warning>
  The `vector` arrays here are synthetic and for demonstration purposes only. In your real-world
  applications, you'd generate these vectors from the raw text fields using a suitable embedding model.
</Warning>

## 4. Run a vector similarity search

Now, let's perform a vector similarity search. The query vector should have the same
dimensionality as your data vectors and be generated using the same embedding model.
The search returns the most similar vectors based on a chosen distance metric (default is L2,
or Euclidean distance).

Our query is a vector that represents a "warrior". Let's find the result that's most similar
to it!

The example for Python above shows how to convert results to a Polars DataFrame.
Depending on your language, you can collect query results as a list/array of objects or DataFrames
to be used downstream in your application.

<Accordion title="Pandas users in Python can get results as a Pandas DataFrame">
  Use the `to_pandas()` method to convert query results into a Pandas DataFrame.
</Accordion>

<Info>
  See the full code for these examples (including helper functions) in the
  `quickstart` file for the appropriate client language in the
  [docs repo](https://github.com/lancedb/docs/tree/main/tests).
</Info>

## What's next?

You've learned how to install LanceDB, connect, create a table, and run a first
vector search. In the real world, embeddings capture meaning and vector search
allows you to find the most relevant data based on semantic similarity.

Note that LanceDB is much more than "just a vector database" -- it's
[a multimodal lakehouse](https://lancedb.com/blog/multimodal-lakehouse/).
There's a lot more you can do with it! Continue
to the [Table management](/tables/) guide to build on
this example with schema options, appending data, updates, and versioning.

As you explore LanceDB further, you can combine vector search with other techniques like filtering based
on metadata fields, full-text search, hybrid search, and more. Check out the tutorials
and guides below to continue learning.

<Columns>
  <Card title="Basic table operations" icon="table" href="/tables">
    Build on this quickstart with table creation, updates, and schema tips.
  </Card>

  <Card title="LanceDB Cloud Quickstart" icon="cloud" href="/cloud/get-started">
    Get started with LanceDB Cloud in minutes.
  </Card>

  <Card title="Build a RAG App" icon="search" href="/tutorials/agents/">
    Learn how to build Retrieval-Augmented Generation (RAG) applications using LanceDB.
  </Card>
</Columns>


# Building Custom Rerankers
Source: https://docs.lancedb.com/reranking/custom-reranker

Learn how to create custom rerankers in LanceDB by extending the base Reranker class.

You can build your own custom reranker in LanceDB by subclassing the `Reranker` class and implementing the
`rerank_hybrid()` method. Optionally, you can also implement the `rerank_vector()` and `rerank_fts()`
methods if you want to support reranking for vector and FTS search separately.

## Interface

The `Reranker` base interface comes with a `merge_results()` method that can be used to combine the
results of semantic and full-text search. This is a vanilla merging algorithm that simply concatenates
the results and removes the duplicates without taking the scores into consideration. It only keeps the
first copy of the row encountered. This works well in cases that don't require the scores of semantic
and full-text search to combine the results. If you want to use the scores or want to support
`return_score="all"`, you'll need to implement your own merging algorithm.

Below, we show the pseudocode of a custom reranker that combines the results of semantic and full-text
search using a linear combination of the scores:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.rerankers import Reranker
  import pyarrow as pa

  class MyReranker(Reranker):
      def __init__(self, param1, param2, ..., return_score="relevance"):
          super().__init__(return_score)
          self.param1 = param1
          self.param2 = param2

      def rerank_hybrid(self, query: str, vector_results: pa.Table, fts_results: pa.Table):
          # Use the built-in merging function
          combined_result = self.merge_results(vector_results, fts_results)

          # Do something with the combined results
          # ...

          # Return the combined results
          return combined_result

      def rerank_vector(self, query: str, vector_results: pa.Table):
          # Do something with the vector results
          # ...

          # Return the vector results
          return vector_results

      def rerank_fts(self, query: str, fts_results: pa.Table):
          # Do something with the FTS results
          # ...

          # Return the FTS results
          return fts_results
  ```
</CodeGroup>

## Example

As an example, let's build custom reranker that enhances the Cohere Reranker by accepting a filter
query, and accepts any other `CohereReranker` params as `kwargs`.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from typing import List, Union
  import pandas as pd
  from lancedb.rerankers import CohereReranker

  class ModifiedCohereReranker(CohereReranker):
      def __init__(self, filters: Union[str, List[str]], **kwargs):
          super().__init__(**kwargs)
          filters = filters if isinstance(filters, list) else [filters]
          self.filters = filters

      def rerank_hybrid(self, query: str, vector_results: pa.Table, fts_results: pa.Table)-> pa.Table:
          combined_result = super().rerank_hybrid(query, vector_results, fts_results)
          df = combined_result.to_pandas()
          for filter in self.filters:
              df = df.query("not text.str.contains(@filter)")

          return pa.Table.from_pandas(df)

      def rerank_vector(self, query: str, vector_results: pa.Table)-> pa.Table:
          vector_results = super().rerank_vector(query, vector_results)
          df = vector_results.to_pandas()
          for filter in self.filters:
              df = df.query("not text.str.contains(@filter)")

          return pa.Table.from_pandas(df)

      def rerank_fts(self, query: str, fts_results: pa.Table)-> pa.Table:
          fts_results = super().rerank_fts(query, fts_results)
          df = fts_results.to_pandas()
          for filter in self.filters:
              df = df.query("not text.str.contains(@filter)")

          return pa.Table.from_pandas(df)
  ```
</CodeGroup>

<Card icon="lightbulb">
  Under the hood, `vector_results` and `fts_results` are PyArrow tables. You can learn more about
  PyArrow tables [here](https://arrow.apache.org/docs/python). The advantage of PyArrow tables is their
  interoperability -- you can easily convert them to Pandas/Polars DataFrames, `PyDict`, `PyList`, etc.

  The benefits are also bidirectional -- just as you can easily convert PyArrow tables *to* Pandas
  DataFrames using the `to_pandas()` method -- you can perform DataFrame transformations
  and just as easily convert the DataFrame back to PyArrow tables using `pa.Table.from_pandas()` method
  as shown in the example above.
</Card>


# Evaluating Hybrid Search Performance
Source: https://docs.lancedb.com/reranking/eval

Learn about evaluating hybrid search performance in LanceDB.

Hybrid search is an often misused and/or misunderstood term. In this section, we're using
the definition of "hybrid search" to mean using a combination of keyword-based and vector search.
Because the vector search operates in a dense embedding space and keyword-based search operate
in a sparse embedding space, their relevance scores cannot be directly compared.
Combining results from multiple searches thus requires a reranking step.

## Reranking strategies

There are two common approaches for reranking search results from multiple sources.

* **Score-based**: Calculate final relevance scores based on a weighted linear combination of individual search algorithm scores. Example: Weighted linear combination of semantic search & keyword-based search results.

* **Relevance-based**: Discards the existing scores and calculates the relevance of each search result-query pair. Example: Cross Encoder models

Even though there may many more strategies for reranking, there are no "universally best"
ones that work well for all cases, because they be dataset or application specific.
Evaluating whether a reranking strategy is a good one, is also a challenge. In the next
section, we discuss an example evaluation of different reranking strategies on a sample dataset.

## Example evaluation

The table below shows our evaluation results from an experiment comparing multiple rerankers on
\~800 hybrid search queries. This is a modified version of an evaluation script by
[LlamaIndex](https://github.com/run-llama/finetune-embedding/blob/main/evaluate.ipynb) that measures
hit-rate @ top-k.

### Using OpenAI `text-embedding-ada-002`

Vector Search baseline: **0.64**

| Reranker           | Top-3  | Top-5  | Top-10 |
| ------------------ | ------ | ------ | ------ |
| Linear Combination | `0.73` | `0.74` | `0.85` |
| Cross Encoder      | `0.71` | `0.70` | `0.77` |
| Cohere             | `0.81` | `0.81` | `0.85` |
| ColBERT            | `0.68` | `0.68` | `0.73` |

<img />

### Using OpenAI `text-embedding-3-small`

Vector Search baseline: **0.59**

| Reranker           | Top-3  | Top-5  | Top-10 |
| ------------------ | ------ | ------ | ------ |
| Linear Combination | `0.68` | `0.70` | `0.84` |
| Cross Encoder      | `0.72` | `0.72` | `0.79` |
| Cohere             | `0.79` | `0.79` | `0.84` |
| ColBERT            | `0.70` | `0.70` | `0.76` |

<img />

## Conclusion

The results show that the reranking methods can significantly improve the search relevance. However,
the improvement we saw was not consistent across all rerankers. In reality, the choice of reranker
likely depends on the dataset and the application.

It's also important to note that the reranking methods are not a
replacement for the search methods they supplement. They are complementary and it's likely that you'd
have to tune them together to get the best results. The latency vs. recall tradeoff is also an
important factor to consider when choosing the reranker. Hopefully this evaluation
gives you a starting point for your own experiments with hybrid search in LanceDB!


# Reranking Search Results
Source: https://docs.lancedb.com/reranking/index

Use a reranker to improve search relevance.

Reranking is the process of re-ordering search results to improve relevance, often using a
different model than the one used for the initial search. LanceDB has built-in support for reranking
with models from Cohere, Sentence-Transformers, and more.

### Quickstart

To use a reranker, you perform a search and then pass the results to the `rerank()` method.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  from lancedb.rerank import CohereReranker

  db = lancedb.connect("/tmp/lancedb")
  table = db.open_table("my_table")

  query = "what is the capital of france"

  # Search with reranking
  reranker = CohereReranker()
  reranked_results = table.search(query).limit(10).rerank(reranker=reranker).to_df()
  ```
</CodeGroup>

### Supported Rerankers

LanceDB supports several rerankers out of the box. Here are a few examples:

| Reranker               | Default Model                          |
| ---------------------- | -------------------------------------- |
| `CohereReranker`       | `rerank-english-v2.0`                  |
| `CrossEncoderReranker` | `cross-encoder/ms-marco-MiniLM-L-6-v2` |
| `ColbertReranker`      | `colbert-ir/colbertv2.0`               |

You can find more details about these and other rerankers in the [integrations](/integrations/reranking) section.

### Multi-vector reranking

Most rerankers support reranking based on multiple vectors. To rerank based on multiple vectors, you can pass a list of vectors to the `rerank` method. Here's an example of how to rerank based on multiple vector columns using the `CrossEncoderReranker`:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.rerankers import CrossEncoderReranker

  reranker = CrossEncoderReranker()

  query = "hello"

  res1 = table.search(query, vector_column_name="vector").limit(3)
  res2 = table.search(query, vector_column_name="text_vector").limit(3)
  res3 = table.search(query, vector_column_name="meta_vector").limit(3)

  reranked = reranker.rerank_multivector([res1, res2, res3],  deduplicate=True)
  ```
</CodeGroup>

## Creating Custom Rerankers

LanceDB also you to create custom rerankers by extending the base `Reranker` class. The custom reranker
should implement the `rerank` method that takes a list of search results and returns a reranked list of
search results. This is covered in more detail in the [creating custom rerankers](/reranking/custom-reranker/) section.


# Metadata Filtering in LanceDB
Source: https://docs.lancedb.com/search/filtering

Filter search results in LanceDB based on metadata fields.

LanceDB supports filtering features of query results based on metadata fields.
While joint vector and metadata search at scale presents a significant challenge,
LanceDB achieves sub-100ms latency at thousands of QPS, enabling efficient vector search
with filtering capabilities even on datasets containing billions of records.

**Pre-filtering is applied to top-k results by default** before executing the vector search. This narrow down the search space within large datasets, thereby reducing query latency.
You can also use **post-filtering** to refine results after the vector search completes.

## Example: Metadata Filtering

To illustrate filtering capabilities, let's try four data points with combinations of vectors and metadata:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  data = [
      {"vector": [3.1, 4.1], "item": "foo", "price": 10.0},
      {"vector": [5.9, 26.5], "item": "bar", "price": 20.0},
      {"vector": [10.2, 100.8], "item": "baz", "price": 30.0},
      {"vector": [1.4, 9.5], "item": "fred", "price": 40.0},
  ]
  table = db.create_table("metadata_filter_example", data=data, mode="overwrite")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const data = [
    { vector: [3.1, 4.1], item: "foo", price: 10.0 },
    { vector: [5.9, 26.5], item: "bar", price: 20.0 },
    { vector: [10.2, 100.8], item: "baz", price: 30.0 },
    { vector: [1.4, 9.5], item: "fred", price: 40.0 },
  ];

  const tableName = "metadata_filter_example";
  const table = await db.createTable(tableName, data, {
    mode: "overwrite",
  });
  ```
</CodeGroup>

### Filtering Without Vector Search

You can always filter your data without search. This is useful when you need to query based on metadata:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  filtered_no_search_result = (
      table.search()
      .where("(item IN ('foo', 'bar', 'baz')) AND (price > 15.0)")
      .limit(3)
      .to_arrow()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const filteredResult = await table
    .query()
    .where("(item IN ('foo', 'bar', 'baz')) AND (price > 15.0)")
    .limit(3)
    .toArray();
  ```
</CodeGroup>

<Warning>
  If your table is large, this could potentially return a very large amount of data. Please be sure to use a `limit` clause unless you're sure you want to return the whole result set.
</Warning>

### Pre-Filtering with Vector Search

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  filtered_result = (
      table.search([100, 102])
      .where("(item IN ('foo', 'bar')) AND (price > 15.0)")
      .limit(3)
      .to_arrow()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const results = await table
    .search([100, 102])
    .where("(item IN ('foo', 'bar')) AND (price > 15.0)")
    .toArray();
  ```
</CodeGroup>

### Post-Filtering with Vector Search

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  post_filtered_result = (
      table.search([100, 102])
      .where("(item IN ('foo', 'bar')) AND (price > 15.0)", prefilter=False)
      .limit(3)
      .to_arrow()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const postFilteredResult = await (table.search([100, 102]) as VectorQuery)
    .where("(item IN ('foo', 'bar')) AND (price > 15.0)")
    .postfilter()
    .limit(3)
    .toArray();
  ```
</CodeGroup>

<Warning>
  When querying large tables, omitting a `limit` clause may overwhelm resources and return excessive data. It can also increase costs as query pricing scales with data scanned and data returned ([LanceDB Cloud pricing](https://lancedb.com/pricing)).
</Warning>

## Filtering with SQL

Because it's built on top of DataFusion, LanceDB embraces the utilization of standard SQL expressions as predicates for filtering operations. SQL can be used during vector search,  update, and deletion operations.

LanceDB supports a growing list of SQL expressions:

| SQL Expression                                                                             | Description                 |
| :----------------------------------------------------------------------------------------- | :-------------------------- |
| `>, >=, <, <=, =`                                                                          | Comparison operators        |
| `AND`, `OR`, `NOT`                                                                         | Logical operators           |
| `IS NULL`, `IS NOT NULL`                                                                   | Null checks                 |
| `IS TRUE`, `IS NOT TRUE`, `IS FALSE`, `IS NOT FALSE`                                       | Boolean checks              |
| `IN`                                                                                       | Value matching from a set   |
| `LIKE`, `NOT LIKE`                                                                         | Pattern matching            |
| `CAST`                                                                                     | Type conversion             |
| `regexp_match(column, pattern)`                                                            | Regular expression matching |
| [DataFusion Functions](https://datafusion.apache.org/user-guide/sql/scalar_functions.html) | Additional SQL functions    |

### Simple SQL Filters

For example, the following filter string is acceptable:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  tbl.search([100, 102]).where(
      "(item IN ('foo', 'baz')) AND (price > 20.0)"
  ).to_arrow()
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  await table
    .search([100, 102])
    .where("(item IN ('foo', 'baz')) AND (price > 20.0)")
    .toArray();
  ```
</CodeGroup>

### Advanced SQL Filters

If your column name contains special characters, upper-case characters, or is a [SQL Keyword](https://docs.rs/sqlparser/latest/sqlparser/keywords/index.html),
you can use backtick (`` ` ``) to escape it. For nested fields, each segment of the
path must be wrapped in backticks.

```sql theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
`CUBE` = 10 AND `UpperCaseName` = '3' AND `column name with space` IS NOT NULL
AND `nested with space`.`inner with space` < 2
```

<Warning>
  Field names containing periods (.) are NOT supported.
</Warning>

### Dates, Timestamps, Decimals

Literals for dates, timestamps, and decimals can be written by writing the string
value after the type name. For example:

<CodeGroup>
  ```sql SQL icon="SQL" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  date_col = date '2021-01-01'
  and timestamp_col = timestamp '2021-01-01 00:00:00'
  and decimal_col = decimal(8,3) '1.000'
  ```
</CodeGroup>

For timestamp columns, the precision can be specified as a number in the type
parameter. Microsecond precision (6) is the default.

| SQL            | Time unit    |
| :------------- | :----------- |
| `timestamp(0)` | Seconds      |
| `timestamp(3)` | Milliseconds |
| `timestamp(6)` | Microseconds |
| `timestamp(9)` | Nanoseconds  |

## Apache Arrow Mapping

LanceDB internally stores data in [Apache Arrow](https://arrow.apache.org/) format.
The mapping from SQL types to Arrow types is:

| SQL type                                                  | Arrow type         |
| :-------------------------------------------------------- | :----------------- |
| `boolean`                                                 | `Boolean`          |
| `tinyint` / `tinyint unsigned`                            | `Int8` / `UInt8`   |
| `smallint` / `smallint unsigned`                          | `Int16` / `UInt16` |
| `int` or `integer` / `int unsigned` or `integer unsigned` | `Int32` / `UInt32` |
| `bigint` / `bigint unsigned`                              | `Int64` / `UInt64` |
| `float`                                                   | `Float32`          |
| `double`                                                  | `Float64`          |
| `decimal(precision, scale)`                               | `Decimal128`       |
| `date`                                                    | `Date32`           |
| `timestamp`                                               | `Timestamp` \[^1]  |
| `string`                                                  | `Utf8`             |
| `binary`                                                  | `Binary`           |

## Best Practices

**Scalar Indexes**: We strongly recommend creating scalar indices on columns used for filtering, whether combined with a search operation or applied independently (e.g., for updates or deletions).

For best performance with large tables or high query volumes:

* Build a scalar index on frequently filtered columns
* Use exact column names in filters (e.g., `user_id` instead of `USER_ID`)
* Avoid complex transformations in filter expressions (keep them simple)
* When running concurrent queries, use connection pooling for better throughput

For a column of type LIST(T), you can use `LABEL_LIST` to create a scalar index. Then you should leverage DataFusion's [array functions](https://datafusion.apache.org/user-guide/sql/scalar_functions.html#array-functions) like `array_has_any` or `array_has_all` for optimized filtering.

## Limitations

Both **pre-filtering** and **post-filtering** can yield false positives. For pre-filtering, if the filter is too selective, it might eliminate relevant items that the vector search would have otherwise identified as a good match. In this case, increasing `nprobes` parameter will help reduce such false positives. It is recommended to call `bypass_vector_index()` if you know that the filter is highly selective.

Similarly, a highly selective post-filter can lead to false positives. Increasing both `nprobes` and `refine_factor` can mitigate this issue. When deciding between pre-filtering and post-filtering, pre-filtering is generally the safer choice if you're uncertain.


# Full-Text Search (FTS)
Source: https://docs.lancedb.com/search/full-text-search

Learn how to implement full-text search in LanceDB using BM25 for keyword-based retrieval.

LanceDB provides support for Full-Text Search via Lance, allowing you to incorporate keyword-based search (based on BM25) in your retrieval solutions.

## Basic Usage

Consider that we have a LanceDB table named `my_table`, whose string column `text` we want to index and query via keyword search, the FTS index must be created before you can search via keywords.

### Table Setup

First, open or create the table you want to search:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  from lancedb.index import FTS

  uri = "data/sample-lancedb"
  db = lancedb.connect(uri)

  table = db.create_table(
      "my_table_fts",
      data=[
          {"vector": [3.1, 4.1], "text": "Frodo was a happy puppy"},
          {"vector": [5.9, 26.5], "text": "There are several kittens playing"},
      ],
  )
  ```

  ```ts TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb";
  const uri = "data/sample-lancedb"
  const db = await lancedb.connect(uri);

  const data = [
      { vector: [3.1, 4.1], text: "Frodo was a happy puppy" },
      { vector: [5.9, 26.5], text: "There are several kittens playing" },
  ];
  const tbl = await db.createTable("my_table", data, { mode: "overwrite" });
  {{< /code >}}

  {{< code language="rust" >}}
  let uri = "data/sample-lancedb";
  let db = connect(uri).execute().await?;
  let initial_data: Box<dyn RecordBatchReader + Send> = create_some_records()?;
  let tbl = db
      .create_table("my_table", initial_data)
      .execute()
      .await?;
  ```
</CodeGroup>

### Construct FTS Index

Create a full-text search index on your text column:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.create_fts_index("text")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  await tbl.createIndex("text", {
      config: lancedb.Index.fts(),
  });
  {{< /code >}}

  {{< code language="rust" >}}
  tbl
      .create_index(&["text"], Index::FTS(FtsIndexBuilder::default()))
      .execute()
      .await?;
  ```
</CodeGroup>

### Full-text Search

Perform full-text search and retrieve results:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  results = table.search("puppy")
      .limit(10)
      .select(["text"])
      .to_list()
  # [{'text': 'Frodo was a happy puppy', '_score': 0.6931471824645996}]
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const results = await tbl
      .search("puppy", "fts")
      .select(["text"])
      .limit(10)
      .toArray();
  ```

  ```rust Rust icon="Rust" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  let results = tbl
      .query()
      .full_text_search(FullTextSearchQuery::new("puppy".to_owned()))
      .select(lancedb::query::Select::Columns(vec!["text".to_owned()]))
      .limit(10)
      .execute()
      .await?;
  ```
</CodeGroup>

The search is conducted on all indexed columns by default, so it's useful when there are multiple indexed columns.

If you want to specify which columns to search use `fts_columns="text"`

<Note>
  LanceDB automatically searches on the existing FTS index if the input to the search is of type `str`. If you provide a vector as input, LanceDB will search the ANN index instead.
</Note>

## Advanced Usage

### Tokenize Table Data

By default, the text is tokenized by splitting on punctuation and whitespaces, and would filter out words that are longer than 40 characters. All words are converted to lowercase.

Stemming is useful for improving search results by reducing words to their root form, e.g. "running" to "run". LanceDB supports stemming for multiple languages. You should set the `base_tokenizer` parameter rather than `tokenizer_name` because you cannot customize the tokenizer if `tokenizer_name` is specified.

For example, to enable stemming for English:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.create_fts_index("text", language="English", replace=True)
  ```
</CodeGroup>

The tokenizer is customizable, you can specify how the tokenizer splits the text, and how it filters out words, etc.

**Default index parameters:**

* `base_tokenizer`: `"simple"`
* `language`: English
* `with_position`: false
* `max_token_length`: 40
* `lower_case`: true
* `stem`: true
* `remove_stop_words`: true
* `ascii_folding`: true

For example, for language with accents, you can specify the tokenizer to use `ascii_folding` to remove accents, e.g. 'é' to 'e':

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.create_fts_index(
          "text",
          language="French",
          stem=True,
          ascii_folding=True,
          replace=True,
      )
  ```
</CodeGroup>

### Filtering Options

LanceDB full text search supports to filter the search results by a condition, both pre-filtering and post-filtering are supported.

This can be invoked via the familiar `where` syntax.

With pre-filtering:

<CodeGroup>
  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  await tbl
  .search("puppy")
  .select(["id", "doc"])
  .limit(10)
  .where("meta='foo'")
  .prefilter(true)
  .toArray();
  ```

  ```rust Rust icon="Rust" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table
      .query()
      .full_text_search(FullTextSearchQuery::new("puppy".to_owned()))
      .select(lancedb::query::Select::Columns(vec!["doc".to_owned()]))
      .limit(10)
      .only_if("meta='foo'")
      .execute()
      .await?;
  ```
</CodeGroup>

With post-filtering:

<CodeGroup>
  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  await tbl
  .search("apple")
  .select(["id", "doc"])
  .limit(10)
  .where("meta='foo'")
  .prefilter(false)
  .toArray();
  ```

  ```rust Rust icon="Rust" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table
      .query()
      .full_text_search(FullTextSearchQuery::new(words[0].to_owned()))
      .select(lancedb::query::Select::Columns(vec!["doc".to_owned()]))
      .postfilter()
      .limit(10)
      .only_if("meta='foo'")
      .execute()
      .await?;
  ```
</CodeGroup>

### Phrase vs. Terms Queries

<Warning>
  Lance-based FTS doesn't support queries using boolean operators `OR`, `AND` in the search string.
</Warning>

For full-text search you can specify either a **phrase** query like `"the old man and the sea"`,
or a **terms** search query like `old man sea`.

To search for a phrase, the index must be created with `with_position=True` and `remove_stop_words=False`:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.create_fts_index("text", with_position=True, replace=True)
  ```
</CodeGroup>

This will allow you to search for phrases, but it will also significantly increase the index size and indexing time.

### Fuzzy Search

Fuzzy search allows you to find matches even when the search terms contain typos or slight variations.
LanceDB uses the classic [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
to find similar terms within a specified edit distance.

| Parameter       | Type | Default | Description                                                                                                                                                 |
| --------------- | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fuzziness       | int  | 0       | Maximum edit distance allowed for each term. If not specified, automatically set based on term length: 0 for length ≤ 2, 1 for length ≤ 5, 2 for length > 5 |
| max\_expansions | int  | 50      | Maximum number of terms to consider for fuzzy matching. Higher values may improve recall but increase search time                                           |

Let's create a sample table and build full-text search indices to demonstrate
fuzzy search capabilities and relevance boosting features.

### Search for Substring

LanceDB supports searching for substrings in the text column, you can set the `base_tokenizer` parameter to `"ngram"` to enable this feature, and use the parameters `ngram_min_length` and `ngram_max_length` to control the length of the substrings:

| Parameter          | Type | Default | Description                                        |
| ------------------ | ---- | ------- | -------------------------------------------------- |
| ngram\_min\_length | int  | 3       | Minimum length of the n-grams to search for        |
| ngram\_max\_length | int  | 3       | Maximum length of the n-grams to search for        |
| prefix\_only       | bool | false   | Whether to only search for prefixes of the n-grams |

## Example: Fuzzy Search

### Generate Data

First, let's create a table with sample text data for testing fuzzy search:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  import numpy as np
  import pandas as pd
  import random

  # Connect to LanceDB
  db = lancedb.connect(
      uri="db://your-project-slug",
      api_key="your-api-key",
      region="us-east-1"
  )

  # Generate sample data
  table_name = "fts-fuzzy-boosting-test"
  vectors = [np.random.randn(128) for _ in range(100)]
  text_nouns = ("puppy", "car")
  text2_nouns = ("rabbit", "girl", "monkey")
  verbs = ("runs", "hits", "jumps", "drives", "barfs")
  adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
  adj = ("adorable", "clueless", "dirty", "odd", "stupid")

  # Generate random text combinations
  text = [
      " ".join([
          text_nouns[random.randrange(0, len(text_nouns))],
          verbs[random.randrange(0, 5)],
          adv[random.randrange(0, 5)],
          adj[random.randrange(0, 5)],
      ])
      for _ in range(100)
  ]
  text2 = [
      " ".join([
          text2_nouns[random.randrange(0, len(text2_nouns))],
          verbs[random.randrange(0, 5)],
          adv[random.randrange(0, 5)],
          adj[random.randrange(0, 5)],
      ])
      for _ in range(100)
  ]
  count = [random.randint(1, 10000) for _ in range(100)]
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb"

  const db = await lancedb.connect({
      uri: "db://your-project-slug",
      apiKey: "your-api-key",
      region: "us-east-1"
  });

  // Generate sample data
  const tableName = "fts-fuzzy-boosting-test-ts";
  const n = 100;
  const vectors = Array.from({ length: n }, () => 
      Array.from({ length: 128 }, () => Math.random() * 2 - 1)
  );

  const textNouns = ["puppy", "car"];
  const text2Nouns = ["rabbit", "girl", "monkey"];
  const verbs = ["runs", "hits", "jumps", "drives", "barfs"];
  const adverbs = ["crazily", "dutifully", "foolishly", "merrily", "occasionally"];
  const adjectives = ["adorable", "clueless", "dirty", "odd", "stupid"];

  // Generate random text combinations
  const generateText = (nouns: string[]) => {
      const noun = nouns[Math.floor(Math.random() * nouns.length)];
      const verb = verbs[Math.floor(Math.random() * verbs.length)];
      const adv = adverbs[Math.floor(Math.random() * adverbs.length)];
      const adj = adjectives[Math.floor(Math.random() * adjectives.length)];
      return `${noun} ${verb} ${adv} ${adj}`;
  };

  const text = Array.from({ length: n }, () => generateText(textNouns));
  const text2 = Array.from({ length: n }, () => generateText(text2Nouns));
  const count = Array.from({ length: n }, () => Math.floor(Math.random() * 10000) + 1);
  ```
</CodeGroup>

### Create Table

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Create table with sample data
  table = db.create_table(
      table_name,
      data=pd.DataFrame({
          "vector": vectors,
          "id": [i % 2 for i in range(100)],
          "text": text,
          "text2": text2,
          "count": count,
      }),
      mode="overwrite"
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Create table with sample data
  const data = makeArrowTable(
      vectors.map((vector, i) => ({
          vector,
          id: i % 2,
          text: text[i],
          text2: text2[i],
          count: count[i],
      }))
  );

  const table = await db.createTable(tableName, data, { mode: "overwrite" });
  ```
</CodeGroup>

### Construct FTS Index

Create a full-text search index on the first text column:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Create FTS index on first text column
  table.create_fts_index("text")
  wait_for_index(table, "text_idx")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Create FTS index on first text column
  await table.createIndex("text", { config: Index.fts() });
  await waitForIndex(table, "text_idx");
  ```
</CodeGroup>

Then, create an index on the second text column:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Create FTS index on second text column
  table.create_fts_index("text2")
  wait_for_index(table, "text2_idx")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Create FTS index on second text column
  await table.createIndex("text2", { config: Index.fts() });
  await waitForIndex(table, "text2_idx");
  ```
</CodeGroup>

### Basic and Fuzzy Search

Now we can perform basic, fuzzy, and prefix match searches:

#### Basic Exact Search

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery

  # Basic match (exact search)
  basic_match_results = (
      table.search(MatchQuery("crazily", "text"))
      .select(["id", "text"])
      .limit(100)
      .to_pandas()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import { MatchQuery } from "@lancedb/lancedb";

  // Basic match (exact search)
  const basicMatchResults = await table.query()
      .fullTextSearch(new MatchQuery("crazily", "text"))
      .select(["id", "text"])
      .limit(100)
      .toArray();
  ```
</CodeGroup>

#### Fuzzy Search with Typos

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Fuzzy match (allows typos)
  fuzzy_results = (
      table.search(MatchQuery("craziou", "text", fuzziness=2))
      .select(["id", "text"])
      .limit(100)
      .to_pandas()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Fuzzy match (allows typos)
  const fuzzyResults = await table.query()
      .fullTextSearch(new MatchQuery("craziou", "text", {
          fuzziness: 2,
      }))
      .select(["id", "text"])
      .limit(100)
      .toArray();
  ```
</CodeGroup>

#### Prefix based Match

Prefix-based match allows you to search for documents containing words that start with a specific prefix.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Fuzzy match (allows typos)
  fuzzy_results = (
      table.search(MatchQuery("cra", "text", prefix_length=3))
      .select(["id", "text"])
      .limit(100)
      .to_pandas()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Fuzzy match (allows typos)
  const fuzzyResults = await table.query()
      .fullTextSearch(new MatchQuery("cra", "text", {
          prefixLength: 3,
      }))
      .select(["id", "text"])
      .limit(100)
      .toArray();
  ```
</CodeGroup>

### Phrase Match

Phrase matching enables you to search for exact sequences of words. Unlike regular text search
which matches individual terms independently, phrase matching requires words to appear in the
specified order with no intervening terms.

Phrase matching is particularly useful for:

* Searching for specific multi-word expressions
* Matching exact titles or quotes
* Finding precise word combinations in a specific order

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Exact phrase match
  from lancedb.query import PhraseQuery

  print("\n1. Exact phrase match for 'puppy runs':")
  phrase_results = (
      table.search(PhraseQuery("puppy runs", "text"))
      .select(["id", "text"])
      .limit(100)
      .to_pandas()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import { PhraseQuery } from "@lancedb/lancedb";

  // Exact phrase match
  console.log("\n1. Exact phrase match for 'puppy runs':");
  const phraseResults = await table.query()
    .fullTextSearch(new PhraseQuery("puppy runs", "text"))
    .select(["id", "text"])
    .limit(100)
    .toArray();
  ```
</CodeGroup>

#### Flexible Phrase Match

To provide more flexible phrase matching, LanceDB supports the `slop` parameter. This allows you to match phrases where the terms appear close to each other, even if they are not directly adjacent or in the exact order, as long as they are within the specified `slop` value.

For example, the phrase query "puppy merrily" would not return any results by default. However, if you set `slop=1`, it will match phrases like "puppy jumps merrily", "puppy runs merrily", and similar variations where one word appears between "puppy" and "merrily".

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Flexible phrase match with slop=1 for 'puppy merrily'
  from lancedb.query import PhraseQuery

  print("\n1. Flexible phrase match for 'puppy merrily' with slop=1:")
  phrase_results = (
      table.search(PhraseQuery("puppy merrily", "text", slop=1))
      .select(["id", "text"])
      .limit(100)
      .to_pandas()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import { PhraseQuery } from "@lancedb/lancedb";

  // Flexible phrase match with slop=1 for 'puppy runs'
  console.log("\n1. Flexible phrase match for 'puppy runs' with slop=1:");
  const phraseResults = await table.query()
    .fullTextSearch(new PhraseQuery("puppy runs", "text", { slop: 1 }))
    .select(["id", "text"])
    .limit(100)
    .toArray();
  ```
</CodeGroup>

### Search with Boosting

Boosting allows you to control the relative importance of different search terms or fields
in your queries. This feature is particularly useful when you need to:

* Prioritize matches in certain columns
* Promote specific terms while demoting others
* Fine-tune relevance scoring for better search results

| Parameter       | Type  | Default  | Description                                                        |
| --------------- | ----- | -------- | ------------------------------------------------------------------ |
| positive        | Query | required | The primary query terms to match and promote in results            |
| negative        | Query | required | Terms to demote in the search results                              |
| negative\_boost | float | 0.5      | Multiplier for negative matches (lower values = stronger demotion) |

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery, BoostQuery, MultiMatchQuery

  # Boost data with 'runs' in text more than 'puppy' in text
  print("\n2. Boosting data with 'runs' in text:")
  boosting_results = (
    table.search(
        BoostQuery(
            MatchQuery("runs", "text"),
            MatchQuery("puppy", "text"),
            negative_boost=0.2,
        ),
    )
    .select(["id", "text"])
    .limit(100)
    .to_pandas()
  )

  """Test searching across multiple fields."""
  print("\n=== Multi Match Query Examples ===")
  # Search across both text and text2
  print("\n1. Searching 'crazily' in both text and text2:")
  multi_match_results = (
      table.search(MultiMatchQuery("crazily", ["text", "text2"]))
      .select(["id", "text", "text2"])
      .limit(100)
      .to_pandas()
  )

  # Search with field boosting
  print("\n2. Searching with boosted text2 field:")
  multi_match_boosting_results = (
      table.search(
          MultiMatchQuery("crazily", ["text", "text2"], boosts=[1.0, 2.0]),
      )
      .select(["id", "text", "text2"])
      .limit(100)
      .to_pandas()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import { MatchQuery, BoostQuery, MultiMatchQuery } from "@lancedb/lancedb";

  // Boosting Example
  console.log("\n2. Boosting data with 'runs' in text:");
  const boostingResults = await table.query()
    .fullTextSearch(new BoostQuery(new MatchQuery("runs", "text"), new MatchQuery("puppy", "text"), {
      negativeBoost: 0.2,
    }))
    .select(["id", "text"])
    .limit(100)
    .toArray();

  // Multi Match Query Examples
  console.log("\n=== Multi Match Query Examples ===");

  // Search across both text fields
  console.log("\n1. Searching 'crazily' in both text and text2:");
  const multiMatchResults = await table.query()
    .fullTextSearch(new MultiMatchQuery("crazily", ["text", "text2"]))
    .select(["id", "text", "text2"])
    .limit(100)
    .toArray();

  // Search with field boosting
  console.log("\n2. Searching with boosted text2 field:");
  const multiMatchBoostingResults = await table.query()
    .fullTextSearch(new MultiMatchQuery("crazily", ["text", "text2"], {
      boosts: [1.0, 2.0],
    }))
    .select(["id", "text", "text2"])
    .limit(100)
    .toArray();
  ```
</CodeGroup>

<Card title="Best practices" icon="flag">
  * Use fuzzy search when handling user input that may contain typos or variations
  * Apply field boosting to prioritize matches in more important columns
  * Combine fuzzy search with boosting for robust and precise search results

  **Recommendations for optimal FTS performance:**

  * Create full-text search indices on text columns that will be frequently searched
  * For hybrid search combining text and vectors, see our [hybrid search guide](/search/hybrid-search/)
  * For performance benchmarks, check our [benchmark results](/enterprise/benchmarks/)
  * For complex queries, use SQL to combine FTS with other filter conditions
</Card>

### Boolean Queries

LanceDB supports boolean logic in full-text search, allowing you to combine multiple queries using `and` and `or` operators. This is useful when you want to match documents that satisfy multiple conditions (intersection) or at least one of several conditions (union).

#### Combining Two Match Queries

In Python, you can combine two MatchQuery objects using either the `and` function or the `&` operator (e.g., `MatchQuery("puppy", "text") and MatchQuery("merrily", "text")`); both methods are supported and yield the same result. Similarly, you can use either the `or` function or the `|` operator to perform an or query.

In TypeScript, boolean queries are constructed using the `BooleanQuery` class with a list of \[Occur, subquery] pairs. For example, to perform an AND query:

```sql SQL icon="code" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
BooleanQuery([
[Occur.Must, new MatchQuery("puppy", "text")],
[Occur.Must, new MatchQuery("merrily", "text")],
])
```

This approach allows you to specify complex boolean logic by combining multiple subqueries with different Occur values (such as `Must`, `Should`, or `MustNot`).

<Info>
  **Which queries are allowed?**

  A boolean query must include at least one `SHOULD` or `MUST` clause. Queries that contain only a `MUST_NOT` clause are not allowed.
</Info>

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery

  # Example: Find documents containing both "puppy" and "merrily"
  and_query = MatchQuery("puppy", "text") & MatchQuery("merrily", "text")
  and_results = (
      table.search(and_query)
      .select(["id", "text"])
      .limit(100)
      .to_pandas()
  )
  print("\nDocuments containing both 'puppy' and 'merrily':")
  print(and_results)

  # Example: Find documents containing either "puppy" or "merrily"
  or_query = MatchQuery("puppy", "text") | MatchQuery("merrily", "text")
  or_results = (
      table.search(or_query)
      .select(["id", "text"])
      .limit(100)
      .to_pandas()
  )
  print("\nDocuments containing either 'puppy' OR 'merrily':")
  print(or_results)
  ```

  ```typescript TypeScript icon="square-js" expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import { MatchQuery, BooleanQuery, Occur } from "@lancedb/lancedb";

  // Flexible boolean queries with MatchQuery

  // Find documents containing both "puppy" and "merrily"
  const mustResults = await table
      .search(
        new BooleanQuery([
          [Occur.Must, new MatchQuery("puppy", "text")],
          [Occur.Must, new MatchQuery("merrily", "text")],
        ]),
      )
      .select(["id", "text"])
      .limit(100)
      .toArray();
  console.log("\nDocuments containing both 'puppy' and 'merrily':");
  console.log(mustResults);

  // Find documents containing either "puppy" or "merrily"
  const shouldResults = await table
      .search(
        new BooleanQuery([
          [Occur.Should, new MatchQuery("puppy", "text")],
          [Occur.Should, new MatchQuery("merrily", "text")],
        ]),
      )
      .select(["id", "text"])
      .limit(100)
      .toArray();
  console.log("\nDocuments containing either 'puppy' or 'merrily':");
  console.log(shouldResults);
  ```
</CodeGroup>

<Info>
  **How to use booleans?**

  * Use `and`/`&`(Python), `Occur.Must`(Typescript) for intersection (documents must match all queries).
  * Use `or`/`|`(Python), `Occur.Should`(Typescript) for union (documents must match at least one query).
</Info>

## Example: Substring Search

LanceDB supports searching for substrings in text columns using n-gram tokenization. This is useful for finding partial matches within text content.

### Setting Up the Table

First, create a table with sample text data and configure n-gram tokenization:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import pyarrow as pa
  import lancedb

  db = lancedb.connect(":memory:")

  data = pa.table({"text": ["hello world", "lance database", "lance is cool"]})
  table = db.create_table("test", data=data)
  table.create_fts_index("text", base_tokenizer="ngram")
  ```
</CodeGroup>

### Basic Substring Search

With the default n-gram settings (minimum length of 3), you can search for substrings of length 3 or more:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  results = table.search("lan", query_type="fts").limit(10).to_list()
  assert len(results) == 2
  assert set(r["text"] for r in results) == {"lance database", "lance is cool"}

  results = (
      table.search("nce", query_type="fts").limit(10).to_list()
  )  # spellchecker:disable-line
  assert len(results) == 2
  assert set(r["text"] for r in results) == {"lance database", "lance is cool"}
  ```
</CodeGroup>

### Handling Short Substrings

By default, the minimum n-gram length is 3, so shorter substrings like "la" won't match:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  results = table.search("la", query_type="fts").limit(10).to_list()
  assert len(results) == 0
  ```
</CodeGroup>

### Customizing N-gram Parameters

You can customize the n-gram behavior by adjusting the minimum length and using prefix-only matching:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.create_fts_index(
      "text",
      base_tokenizer="ngram",
      replace=True,
      ngram_min_length=2,
      prefix_only=True,
  )
  ```
</CodeGroup>

### Testing Custom N-gram Settings

With the new settings, you can now search for shorter substrings and use prefix-only matching:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  results = table.search("lan", query_type="fts").limit(10).to_list()
  assert len(results) == 2
  assert set(r["text"] for r in results) == {"lance database", "lance is cool"}

  results = (
      table.search("nce", query_type="fts").limit(10).to_list()
  )  # spellchecker:disable-line
  assert len(results) == 0

  results = table.search("la", query_type="fts").limit(10).to_list()
  assert len(results) == 2
  assert set(r["text"] for r in results) == {"lance database", "lance is cool"}
  ```
</CodeGroup>

## Full-Text Search on Array Fields

LanceDB supports full-text search on string array columns, enabling efficient keyword-based search across multiple values within a single field (e.g., tags, keywords).

### Setting Up the Connection

Connect to your LanceDB instance:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb

  # Connect to LanceDB
  db = lancedb.connect(
    uri="db://your-project-slug",
    api_key="your-api-key",
    region="us-east-1"
  )
  ```

  ```typescript TypeScript icon="square-js" expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb"

  const db = await lancedb.connect({
    uri: "db://your-project-slug",
    apiKey: "your-api-key",
    region: "us-east-1"
  });
  ```
</CodeGroup>

### Defining the Schema

Create a schema that includes an array field for tags:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table_name = "fts-array-field-test"
  schema = pa.schema([
      pa.field("id", pa.string()),
      pa.field("tags", pa.list_(pa.string())),
      pa.field("description", pa.string())
  ])
  ```

  ```typescript TypeScript icon="square-js" expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const tableName = "fts-array-field-test-ts";

  // Create schema
  const schema = new Schema([
    new Field("id", new Utf8(), false),
    new Field("tags", new List(new Field("item", new Utf8()))),
    new Field("description", new Utf8(), false)
  ]);
  ```
</CodeGroup>

### Creating Sample Data

Generate sample data with array fields containing tags:

<CodeGroup>
  ```python Python icon="python" expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Generate sample data
  data = {
      "id": [f"doc_{i}" for i in range(10)],
      "tags": [
          ["python", "machine learning", "data science"],
          ["deep learning", "neural networks", "AI"],
          ["database", "indexing", "search"],
          ["vector search", "embeddings", "AI"],
          ["full text search", "indexing", "database"],
          ["python", "web development", "flask"],
          ["machine learning", "deep learning", "pytorch"],
          ["database", "SQL", "postgresql"],
          ["search engine", "elasticsearch", "indexing"],
          ["AI", "transformers", "NLP"]
      ],
      "description": [
          "Python for data science projects",
          "Deep learning fundamentals",
          "Database indexing techniques",
          "Vector search implementations",
          "Full-text search guide",
          "Web development with Python",
          "Machine learning with PyTorch",
          "Database management systems",
          "Search engine optimization",
          "AI and NLP applications"
      ]
  }
  ```

  ```typescript TypeScript icon="square-js" expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Generate sample data
  const data = makeArrowTable(
    Array(10).fill(0).map((_, i) => ({
      id: `doc_${i}`,
      tags: [
        ["python", "machine learning", "data science"],
        ["deep learning", "neural networks", "AI"],
        ["database", "indexing", "search"],
        ["vector search", "embeddings", "AI"],
        ["full text search", "indexing", "database"],
        ["python", "web development", "flask"],
        ["machine learning", "deep learning", "pytorch"],
        ["database", "SQL", "postgresql"],
        ["search engine", "elasticsearch", "indexing"],
        ["AI", "transformers", "NLP"]
      ][i],
      description: [
        "Python for data science projects",
        "Deep learning fundamentals",
        "Database indexing techniques",
        "Vector search implementations",
        "Full-text search guide",
        "Web development with Python",
        "Machine learning with PyTorch",
        "Database management systems",
        "Search engine optimization",
        "AI and NLP applications"
      ][i]
    })),
    { schema }
  );
  ```
</CodeGroup>

### Creating the Table and Adding Data

Create the table and populate it with the sample data:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Create table and add data
  table = db.create_table(table_name, schema=schema, mode="overwrite")
  table_data = pa.Table.from_pydict(data, schema=schema)
  table.add(table_data)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Create table
  const table = await db.createTable(tableName, data, { mode: "overwrite" });
  console.log(`Created table: ${tableName}`);
  ```
</CodeGroup>

### Building the Full-Text Search Index

Create an FTS index on the tags column to enable efficient text search:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Create FTS index
  table.create_fts_index("tags")
  wait_for_index(table, "tags_idx")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Create FTS index
  console.log("Creating FTS index on 'tags' column...");
  await table.createIndex("tags", {
    config: Index.fts()
  });

  // Wait for index
  const ftsIndexName = "tags_idx";
  await waitForIndex(table, ftsIndexName);
  ```
</CodeGroup>

### Performing Fuzzy Search

Search for terms with typos using fuzzy matching:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Search examples
  print("\nSearching for 'learning' in tags with a typo:")
  result = (
      table.search(MatchQuery("learnin", column="tags", fuzziness=1))
      .select(['id', 'tags', 'description'])
      .to_arrow()
  )
  ```

  ```typescript TypeScript icon="square-js"> theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Search examples
  console.log("\nSearching for 'learning' in tags with a typo:");
  const fuzzyResults = await table.query()
    .fullTextSearch(new MatchQuery("learnin", "tags", {
      fuzziness: 2,
    }))
    .select(["id", "tags", "description"])
    .toArray();
  console.log(fuzzyResults);
  ```
</CodeGroup>

### Performing Phrase Search

Search for exact phrases within the array fields:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  print("\nSearching for 'machine learning' in tags:")
  result = (
      table.search(PhraseQuery("machine learning", column="tags"))
      .select(['id', 'tags', 'description'])
      .to_arrow()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  console.log("\nSearching for 'machine learning' in tags:");
  const phraseResults = await table.query()
    .fullTextSearch(new PhraseQuery("machine learning", "tags"))
    .select(["id", "tags", "description"])
    .toArray();
  console.log(phraseResults);
  ```
</CodeGroup>


# Hybrid Search
Source: https://docs.lancedb.com/search/hybrid-search

Learn how to perform hybrid search in LanceDB by combining vector and full-text search techniques with reranking.

In certain cases, you may want to retrieve documents that are semantically similar to a given  query,
but also prioritize specific keywords. This is an example of **hybrid search**, a query method that combines
multiple search techniques.

For detailed examples, look at this [Python Notebook](https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/saas_examples/python_notebook/Hybrid_search.ipynb) or the [**TypeScript Example**](https://github.com/lancedb/vectordb-recipes/tree/main/examples/saas_examples/ts_example/hybrid-search)

## Example: Hybrid Search

### 1. Setup

Import the necessary libraries and dependencies for working with LanceDB, OpenAI embeddings, and reranking.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import os
  import lancedb
  import openai
  from lancedb.embeddings import get_registry
  from lancedb.pydantic import LanceModel, Vector
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb";
  import "@lancedb/lancedb/embedding/openai";
  import { Utf8 } from "apache-arrow";
  ```
</CodeGroup>

### 2. Connect to LanceDB Cloud

Establish a connection to your LanceDB instance, with different options for Cloud, Enterprise, and Open Source deployments.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  db = lancedb.connect(
    uri="db://your-project-slug",
    api_key="your-api-key",
    region="us-east-1"
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const db = await lancedb.connect({
    uri: "db://your-project-slug",
    apiKey: "your-api-key",
    region: "us-east-1",
  });
  ```
</CodeGroup>

For Open Source:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  uri = "data/sample-lancedb"
  db = lancedb.connect(uri)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb";
  import * as arrow from "apache-arrow";

  const db = await lancedb.connect(databaseDir);
  ```
</CodeGroup>

For LanceDB Enterprise, set the host override to your private cloud endpoint:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  host_override = os.environ.get("LANCEDB_HOST_OVERRIDE")

  db = lancedb.connect(
  uri=uri,
  api_key=api_key,
  region=region,
  host_override=host_override
  )
  ```
</CodeGroup>

### 3. Configure Embedding Model

Set up the any embedding model that will convert text into vector representations for semantic search.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  embeddings = get_registry().get("sentence-transformers").create()
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const embedFunc = lancedb.embedding.getRegistry().get("openai")?.create({
    model: "text-embedding-ada-002",
  }) as lancedb.embedding.EmbeddingFunction;
  ```
</CodeGroup>

### 4. Create Table & Schema

Define the data structure for your documents, including both the text content and its vector representation.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  class Documents(LanceModel):
      text: str = embeddings.SourceField()
      vector: Vector(embeddings.ndims()) = embeddings.VectorField()

  table_name = "hybrid_search_example"
  table = db.create_table(table_name, schema=Documents, mode="overwrite")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const documentSchema = lancedb.embedding.LanceSchema({
    text: embedFunc.sourceField(new Utf8()),
    vector: embedFunc.vectorField(),
  });

  const tableName = "hybrid_search_example";
  const table = await db.createEmptyTable(tableName, documentSchema, {
    mode: "overwrite",
  });
  ```
</CodeGroup>

### 5. Add Data

Insert sample documents into your table, which will be used for both semantic and keyword search.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  data = [
      {"text": "rebel spaceships striking from a hidden base"},
      {"text": "have won their first victory against the evil Galactic Empire"},
      {"text": "during the battle rebel spies managed to steal secret plans"},
      {"text": "to the Empire's ultimate weapon the Death Star"},
  ]
  table.add(data=data)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const data = [
    { text: "rebel spaceships striking from a hidden base" },
    { text: "have won their first victory against the evil Galactic Empire" },
    { text: "during the battle rebel spies managed to steal secret plans" },
    { text: "to the Empire's ultimate weapon the Death Star" },
  ];
  await table.add(data);
  console.log(`Created table: ${tableName} with ${data.length} rows`);
  ```
</CodeGroup>

### 6. Build Full Text Index

Create a full-text search index on the text column to enable keyword-based search capabilities.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.create_fts_index("text")
  wait_for_index(table, "text_idx")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  console.log("Creating full-text search index...");
  await table.createIndex("text", {
    config: lancedb.Index.fts(),
  });
  await waitForIndex(table as any, "text_idx");
  ```
</CodeGroup>

### 7. Set Reranker \[Optional]

Initialize the reranker that will combine and rank results from both semantic and keyword search. By default, lancedb uses RRF reranker, but you can choose other rerankers like `Cohere`, `CrossEncoder`, or others lister in integrations section.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  reranker = RRFReranker()
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const reranker = await lancedb.rerankers.RRFReranker.create();
  ```
</CodeGroup>

### 8. Hybrid Search

Perform a hybrid search query that combines semantic similarity with keyword matching, using the specified reranker to merge and rank the results.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  results = (
      table.search(
          "flower moon",
          query_type="hybrid",
          vector_column_name="vector",
          fts_columns="text",
      )
      .rerank(reranker)
      .limit(10)
      .to_pandas()
  )

  print("Hybrid search results:")
  print(results)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  console.log("Performing hybrid search...");
  const queryVector = await embedFunc.computeQueryEmbeddings("full moon in May");
  const hybridResults = await table
    .query()
    .fullTextSearch("flower moon")
    .nearestTo(queryVector)
    .rerank(reranker)
    .select(["text"])
    .limit(10)
    .toArray();

  console.log("Hybrid search results:");
  console.log(hybridResults);
  ```
</CodeGroup>

### 9. Hybrid Search - Explicit Vector and Text Query pattern

You can also pass the vector and text query explicitly. This is useful if you're not using the embedding API or if you're using a separate embedder service.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  vector_query = [0.1, 0.2, 0.3, 0.4, 0.5]
  text_query = "flower moon"
  (
      table.search(query_type="hybrid")
      .vector(vector_query)
      .text(text_query)
      .limit(5)
      .to_pandas()
  )
  ```
</CodeGroup>

## More on Reranking

You can perform hybrid search in LanceDB by combining the results of semantic and full-text search via a reranking algorithm of your choice. LanceDB comes with [**built-in rerankers**](https://lancedb.github.io/lancedb/reranking/) and you can implement your own **custom reranker** as well.

By default, LanceDB uses `RRFReranker()`, which uses reciprocal rank fusion score, to combine and rerank the results of semantic and full-text search. You can customize the hyperparameters as needed or write your own custom reranker. Here's how you can use any of the available rerankers:

| Argument    | Type       | Default   | Description                                                                                                                                                                     |
| :---------- | :--------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `normalize` | `str`      | `"score"` | The method to normalize the scores. Can be `rank` or `score`. If `rank`, the scores are converted to ranks and then normalized. If `score`, the scores are normalized directly. |
| `reranker`  | `Reranker` | `RRF()`   | The reranker to use. If not specified, the default reranker is used.                                                                                                            |


# Search
Source: https://docs.lancedb.com/search/index

Comprehensive guide to all search capabilities in LanceDB including vector search, full-text search, hybrid search, and more.

| Feature                                           | Description                                               |
| :------------------------------------------------ | :-------------------------------------------------------- |
| [Vector Search](/search/vector-search/)           | Semantic similarity search with multiple distance metrics |
| [Multivector Search](/search/multivector-search/) | Search using multiple vector embeddings per document      |
| [Full-Text Search](/search/full-text-search/)     | Keyword-based search with BM25 and pre-filtering          |
| [Hybrid Search](/search/hybrid-search/)           | Combines vector and full-text search with reranking       |
| [Filtering](/search/filtering/)                   | Filter results based on metadata fields                   |
| [SQL Queries](/search/sql/index)                  | SQL query capabilities for data exploration and analytics |


# Multivector Search
Source: https://docs.lancedb.com/search/multivector-search

Learn how to perform multivector search in LanceDB to handle multiple vector embeddings per document, ideal for late interaction models like ColBERT and ColPaLi.

LanceDB's multivector support enables you to store and search multiple vector embeddings for a single item.

This capability is particularly valuable when working with late interaction models like ColBERT and ColPaLi that generate multiple embeddings per document.

In this tutorial, you'll create a table with multiple vector embeddings per document and learn how to perform multivector search. [For all the code - open in Colab](https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/saas_examples/python_notebook/Multivector_on_LanceDB_Cloud.ipynb)

## Multivector Support

Each item in your dataset can have a column containing multiple vectors, which LanceDB can efficiently index and search. When performing a search, you can query using either a single vector embedding or multiple vector embeddings.

LanceDB also integrates with [ConteXtualized Token Retriever (XTR)](https://arxiv.org/abs/2304.01982), an advanced retrieval model that prioritizes the most semantically important document tokens during search. This integration enhances the quality of search results by focusing on the most relevant token matches.

<Tip>
  * Currently, only the `cosine` metric is supported for multivector search.
  * The vector value type can be `float16`, `float32`, or `float64`.
</Tip>

### Computing Similarity

MaxSim (Maximum Similarity) is a key concept in late interaction models that:

* Computes the maximum similarity between each query embedding and all document embeddings
* Sums these maximum similarities to get the final relevance score
* Effectively captures fine-grained semantic matches between query and document tokens

The MaxSim calculation can be expressed as:

$$
\text{MaxSim}(Q, D) = \sum_{i=1}^{|Q|} \max_{j=1}^{|D|} \text{sim}(q_i, d_j)
$$

Where $sim$ is the similarity function (e.g. cosine similarity).

$$
Q = \{q_1, q_2, ..., q_{|Q|}\}
$$

$Q$ represents the query vector, and $D = \{d_1, d_2, ..., d_{|D|}\}$ represents the document vectors.

<Warning>
  For now, you should use only the `cosine` metric for multivector search.
  The vector value type can be `float16`, `float32` or `float64`.
</Warning>

## Example: Multivector Search

### 1. Setup

Connect to LanceDB and import required libraries for data management.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  import numpy as np
  import pyarrow as pa

  db = lancedb.connect(
      uri="db://your-project-slug",
      api_key="your-api-key",
      region="your-cloud-region"
  )
  ```
</CodeGroup>

### 2. Define Schema

Define a schema that specifies a multivector field. A multivector field is a nested list structure where each document contains multiple vectors. In this case, we'll create a schema with:

1. An ID field as an integer (int64)
2. A vector field that is a list of lists of float32 values
   * The outer list represents multiple vectors per document
   * Each inner list is a 256-dimensional vector
   * Using float32 for memory efficiency while maintaining precision

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  db = lancedb.connect("data/multivector_demo")
  schema = pa.schema(
      [
          pa.field("id", pa.int64()),
          # float16, float32, and float64 are supported
          pa.field("vector", pa.list_(pa.list_(pa.float32(), 256))),
      ]
  )
  ```
</CodeGroup>

### 3. Generate Multivectors

Generate sample data where each document contains multiple vector embeddings, which could represent different aspects or views of the same document.

In this example, we create **1024 documents** where each document has **2 random vectors** of **dimension 256**, simulating a real-world scenario where you might have multiple embeddings per item.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  data = [
      {
          "id": i,
          "vector": np.random.random(size=(2, 256)).tolist(),  # Each document has 2 vectors
      }
      for i in range(1024)
  ]
  ```
</CodeGroup>

### 4. Create a Table

Create a table with the defined schema and sample data, which will store multiple vectors per document for similarity search.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  tbl = db.create_table("multivector_example", data=data, schema=schema)
  ```
</CodeGroup>

### 5. Build an Index

Only cosine similarity is supported as the distance metric for multivector search operations.
For faster search, build the standard `IVF_PQ` index over your vectors:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  tbl.create_index(metric="cosine", vector_column_name="vector")
  ```
</CodeGroup>

### 6. Query a Single Vector

When searching with a single query vector, it will be compared against all vectors in each document, and the similarity scores will be aggregated to find the most relevant documents.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  query = np.random.random(256)
  results_single = tbl.search(query).limit(5).to_pandas()
  ```
</CodeGroup>

### 7. Query Multiple Vectors

With multiple vector queries, LanceDB calculates similarity using late interaction - a technique that computes relevance by finding the best matching pairs between query and document vectors. This approach provides more nuanced matching while maintaining fast retrieval speeds.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  query_multi = np.random.random(size=(2, 256))
  results_multi = tbl.search(query_multi).limit(5).to_pandas()
  ```
</CodeGroup>

## What's Next?

If you still need more guidance, you can try the complete [Multivector Search Notebook](https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/saas_examples/python_notebook/Multivector_on_LanceDB_Cloud.ipynb).


# Optimize Query Performance
Source: https://docs.lancedb.com/search/optimize-queries

Analyze and optimize query performance in LanceDB.

LanceDB provides two powerful tools for query analysis and optimization: `explain_plan` and `analyze_plan`. Let's take a better look at how they work:

| Method         | Purpose            | Description                                                                                                                                                                                              |
| :------------- | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `explain_plan` | Query Analysis     | Print the resolved query plan to understand how the query will be executed. Helpful for identifying slow queries or unexpected query results.                                                            |
| `analyze_plan` | Performance Tuning | Execute the query and return a physical execution plan annotated with runtime metrics including execution time, number of rows processed, and I/O stats. Essential for performance tuning and debugging. |

## Query Analysis Tools

### explain\_plan

Reveals the logical query plan before execution, helping you identify potential issues with query structure and index usage. This tool is useful for:

* Verifying query optimization strategies
* Validating index selection
* Understanding query execution order
* Detecting missing indices

### analyze\_plan

Executes the query and provides detailed runtime metrics, including:

* Operation duration (`_elapsed_compute_`)
* Data processing statistics (`_output_rows_`, `_bytes_read_`)
* Index effectiveness (`_index_comparisons_`, `_indices_loaded_`)
* Resource utilization (`_iops_`, `_requests_`)

Together, these tools offer a comprehensive view of query performance, from planning to execution. Use `explain_plan` to verify your query structure and `analyze_plan` to measure and optimize actual performance.

## Reading the Execution Plan

To demonstrate query performance analysis, we'll use a table containing 1.2M rows sampled from the [Wikipedia dataset](https://huggingface.co/datasets/wikimedia/wikipedia). Initially, the table has no indices, allowing us to observe the impact of optimization.

Let's examine a vector search query that:

* Filters rows where `identifier` is between 0 and 1,000,000
* Returns the top 100 matches
* Projects specific columns: `chunk_index`, `title`, and `identifier`

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # explain_plan
  query_explain_plan = (
      table.search(query_embed)
      .where("identifier > 0 AND identifier < 1000000")
      .select(["chunk_index", "title", "identifier"])
      .limit(100)
      .explain_plan(True)
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // explain_plan
  const explainPlan = await table
      .search(queryEmbed)
      .where("identifier > 0 AND identifier < 1000000")
      .select(["chunk_index", "title", "identifier"])
      .limit(100)
      .explainPlan(true);
  ```
</CodeGroup>

### Execution Plan Components

The execution plan reveals the sequence of operations performed to execute your query. Let's examine each component:

```
ProjectionExec: expr=[chunk_index@4 as chunk_index, title@5 as title, identifier@1 as identifier, _distance@3 as _distance]
  RemoteTake: columns="vector, identifier, _rowid, _distance, chunk_index, title"
    CoalesceBatchesExec: target_batch_size=1024
      GlobalLimitExec: skip=0, fetch=100
        FilterExec: _distance@3 IS NOT NULL
          SortExec: TopK(fetch=100), expr=[_distance@3 ASC NULLS LAST], preserve_partitioning=[false]
            KNNVectorDistance: metric=l2
              FilterExec: identifier@1 > 0 AND identifier@1 < 1000000
                LanceScan: uri=***, projection=[vector, identifier], row_id=true, row_addr=false, ordered=false
```

#### 1. Base Layer (LanceScan)

* Initial data scan loading only specified columns to minimize I/O
* Unordered scan enabling parallel processing

```
LanceScan: 
- projection=[vector, identifier]
- row_id=true, row_addr=false, ordered=false
```

#### 2. First Filter

* Apply requested filter on `identifier` column
* Reduces the number of vectors that need KNN computation

```
FilterExec: identifier@1 > 0 AND identifier@1 < 1000000
```

#### 3. Vector Search

* Computes L2 (Euclidean) distances between query vector and all vectors that passed the filter

```
KNNVectorDistance: metric=l2
```

#### 4. Results Processing

* Filters out null distance results
* Sorts by distance and takes top 100 results
* Processes in batches of 1024 for optimal memory usage

```
SortExec: TopK(fetch=100)
- expr=[_distance@3 ASC NULLS LAST]
- preserve_partitioning=[false]
FilterExec: _distance@3 IS NOT NULL
GlobalLimitExec: skip=0, fetch=100
CoalesceBatchesExec: target_batch_size=1024
```

#### 5. Data Retrieval

* `RemoteTake` is a key component of Lance's I/O cache
* Handles efficient data retrieval from remote storage locations
* Fetches specific rows and columns needed for the final output
* Optimizes network bandwidth by only retrieving required data

```
RemoteTake: columns="vector, identifier, _rowid, _distance, chunk_index, title"
```

#### 6. Final Output

* Returns only requested columns and maintains column ordering

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
ProjectionExec: expr=[chunk_index@4 as chunk_index, title@5 as title, identifier@1 as identifier, _distance@3 as _distance]
```

This plan demonstrates a basic search without index optimizations: it performs a full scan and filter before vector search.

## Performance Analysis

Let's use `analyze_plan` to run the query and analyze the query performance, which will help us identify potential bottlenecks:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # analyze_plan
  query_analyze_plan = (
      table.search(query_embed)
      .where("identifier > 0 AND identifier < 1000000")
      .select(["chunk_index", "title", "identifier"])
      .limit(100)
      .analyze_plan()
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // analyze_plan
  const analyzePlan = await table
      .search(queryEmbed)
      .where("identifier > 0 AND identifier < 1000000")
      .select(["chunk_index", "title", "identifier"])
      .limit(100)
      .analyzePlan();
  ```
</CodeGroup>

### Performance Metrics Analysis

```
ProjectionExec: expr=[chunk_index@4 as chunk_index, title@5 as title, identifier@1 as identifier, _distance@3 as _distance], metrics=[output_rows=100, elapsed_compute=1.424µs]
    RemoteTake: columns="vector, identifier, _rowid, _distance, chunk_index, title", metrics=[output_rows=100, elapsed_compute=175.53097ms, output_batches=1, remote_takes=100]
      CoalesceBatchesExec: target_batch_size=1024, metrics=[output_rows=100, elapsed_compute=2.748µs]
        GlobalLimitExec: skip=0, fetch=100, metrics=[output_rows=100, elapsed_compute=1.819µs]
          FilterExec: _distance@3 IS NOT NULL, metrics=[output_rows=100, elapsed_compute=10.275µs]
            SortExec: TopK(fetch=100), expr=[_distance@3 ASC NULLS LAST], preserve_partitioning=[false], metrics=[output_rows=100, elapsed_compute=39.259451ms, row_replacements=546]
              KNNVectorDistance: metric=l2, metrics=[output_rows=1099508, elapsed_compute=56.783526ms, output_batches=1076]
                FilterExec: identifier@1 > 0 AND identifier@1 < 1000000, metrics=[output_rows=1099508, elapsed_compute=17.136819ms]
                  LanceScan: uri=***, projection=[vector, identifier], row_id=true, row_addr=false, ordered=false, metrics=[output_rows=1200000, elapsed_compute=21.348178ms, bytes_read=1852931072, iops=78, requests=78]
```

#### 1. Data Loading (LanceScan)

* Scanned 1,200,000 rows from the LanceDB table
* Read 1.86GB of data in 78 I/O operations
* Only loaded necessary columns (`vector` and `identifier`)
* Unordered scan for parallel processing

#### 2. Filtering & Search

* Applied prefilter condition (`identifier > 0 AND identifier < 1000000`)
* Reduced dataset from 1.2M to 1,099,508 rows
* KNN search used L2 (Euclidean) distance metric
* Vector comparisons processed in 1076 batches

#### 3. Results Processing

* KNN results sorted by distance (TopK with fetch=100)
* Null distances filtered out
* Batches coalesced to target size of 1024 rows
* Additional columns fetched for final results
* Remote take operation for 100 results
* Final projection of required columns

### Key Observations

* Vector search is the primary bottleneck (1,099,508 vector comparisons)
* Significant I/O overhead (1.86GB data read)
* Full table scan due to lack of indices
* Substantial optimization potential through proper index implementation

## Optimized Query Execution

After creating vector and scalar indices, the execution plan shows:

```
ProjectionExec: expr=[chunk_index@3 as chunk_index, title@4 as title, identifier@2 as identifier, _distance@0 as _distance]
  RemoteTake: columns="_distance, _rowid, identifier, chunk_index, title"
    CoalesceBatchesExec: target_batch_size=1024
      GlobalLimitExec: skip=0, fetch=100
        SortExec: TopK(fetch=100), expr=[_distance@0 ASC NULLS LAST], preserve_partitioning=[false]
          ANNSubIndex: name=vector_idx, k=100, deltas=1
            ANNIvfPartition: uuid=83916fd5-fc45-4977-bad9-1f0737539bb9, nprobes=20, deltas=1
            ScalarIndexQuery: query=AND(identifier > 0,identifier < 1000000)
```

### Optimized Plan Analysis

#### 1. Scalar Index Query

```
ScalarIndexQuery: query=AND(identifier > 0,identifier < 1000000)
metrics=[
    output_rows=2
    index_comparisons=2,301,824
    indices_loaded=2
    output_batches=1
    parts_loaded=562
    elapsed_compute=86.979354ms
]
```

* Range filter using scalar index
* Only 2 index files and 562 scalar index parts loaded
* 2.3M index comparisons for matches

#### 2. Vector Search

```
ANNSubIndex: name=vector_idx, k=100, deltas=1
metrics=[
    output_rows=2,000
    index_comparisons=25,893
    indices_loaded=0
    output_batches=20
    parts_loaded=20
    elapsed_compute=111.849043ms
]
```

* IVF index with 20 probes
* Only 20 index parts loaded
* 25,893 vector comparisons
* 2,000 matching vectors

#### 3. Results Processing

```
SortExec: TopK(fetch=100), expr=[_distance@0 ASC NULLS LAST], preserve_partitioning=[false]
GlobalLimitExec: skip=0, fetch=100
CoalesceBatchesExec: target_batch_size=1024
```

* Sorts by distance
* Limits to top 100 results
* Batches into groups of 1024

#### 4. Data Fetching

```
RemoteTake: columns="_distance, _rowid, identifier, chunk_index, title"
metrics=[output_rows=100, elapsed_compute=113.491859ms, output_batches=1, remote_takes=100]
```

* Single output batch
* One remote take per row

#### 5. Final Projection

```
ProjectionExec: expr=[chunk_index@3 as chunk_index, title@4 as title, identifier@2 as identifier, _distance@0 as _distance]
```

* Returns specified columns: chunk\_index, title, identifier, and distance

### Performance Improvements

#### 1. Initial Data Access

```
ScalarIndexQuery metrics:
- indices_loaded=2
- parts_loaded=562
- output_batches=1
```

* Before: Full table scan of 1.2M rows, 1.86GB data
* After: Only 2 indices and 562 scalar index parts loaded
* Benefit: Eliminated table scans for prefilter

#### 2. Vector Search Efficiency

```
ANNSubIndex:
- index_comparisons=25,893
- indices_loaded=0
- parts_loaded=20
- output_batches=20
```

* Before: L2 calculations on 1,099,508 vectors
* After:
  * 99.8% reduction in vector comparisons
  * Decreased output batches from 1,076 to 20

#### 3. Data Retrieval Optimization

```
RemoteTake:
- remote_takes=100
- output_batches=1
```

* RemoteTake operation remains consistent

## Performance Optimization Guide

### 1. Index Implementation

#### When to Create Indices

* Columns used in WHERE clauses
* Vector columns for similarity searches
* Join columns used in `merge_insert`

#### Index Type Selection

| Data Type   | Recommended Index     | Use Case                                 |
| ----------- | --------------------- | ---------------------------------------- |
| Vector      | IVF\_PQ/IVF\_HNSW\_SQ | Approximate nearest neighbor search      |
| Scalar      | B-Tree                | Range queries and sorting                |
| Categorical | Bitmap                | Multi-value filters and set operations   |
| `List`      | Label\_list           | Multi-label classification and filtering |

<Card title="Index Coverage Monitoring" icon="lightbulb">
  Use `table.index_stats()` to monitor index coverage.
  A well-optimized table should have `num_unindexed_rows ~ 0`.
</Card>

### 2. Query Plan Optimization

#### Common Patterns and Fixes

| Plan Pattern                                | Optimization                                 |
| ------------------------------------------- | -------------------------------------------- |
| LanceScan with high *bytes\_read* or *iops* | Add missing index                            |
|                                             | Use `select()` to limit returned columns     |
|                                             | Check whether the dataset has been compacted |
| Multiple sequential filters                 | Reorder filter conditions                    |

!!! note "Regular Performance Analysis"
Regularly analyze your query plans to identify and address performance bottlenecks.
The `analyze_plan` output provides detailed metrics to guide optimization efforts.

### 3. Getting Started with Optimization

For vector search performance:

* Create ANN index on your vector column(s) as described in the [index guide](/indexing/vector-index/)
* If you often filter by metadata, create [scalar indices](/indexing/scalar-index/) on those columns


# Full-Text Search with SQL
Source: https://docs.lancedb.com/search/sql/fts-sql

Use LanceDB's full-text search capabilities via SQL queries.

<Badge>Enterprise-only</Badge>

<Danger>
  This feature is currently in beta. The SQL syntax and JSON query format may change in future
  releases as we continue to refine and improve the FTS SQL interface. We recommend testing
  thoroughly and being prepared to update your queries as newer versions of LanceDB become available.
</Danger>

LanceDB provides support for full-text search via SQL queries using the `fts()` User-Defined Table Function (UDTF). This allows you to incorporate keyword-based search (based on BM25) in your SQL queries for powerful text retrieval.

## Table Setup

First, set up your FlightSQL client connection. See [SQL Queries documentation](/search/sql) for detailed client setup instructions.

For the examples below, we assume you have a `run_query()` helper function that executes SQL and returns results.

### Creating the Table

Create a table with text data:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  run_query("""
      CREATE TABLE my_docs (
          id INT,
          text STRING,
          category STRING,
          author STRING
      )
  """)
  ```
</CodeGroup>

### Inserting Data

Insert sample documents:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  run_query("""
      INSERT INTO my_docs VALUES
      (1, 'The happy puppy runs merrily in the park', 'animals', 'Alice'),
      (2, 'A curious kitten jumps quickly over the fence', 'animals', 'Bob'),
      (3, 'The puppy catches a ball with great enthusiasm', 'sports', 'Alice'),
      (4, 'Dogs and cats are wonderful companions', 'animals', 'Charlie'),
      (5, 'Puppy training requires patience and dedication', 'training', 'Alice'),
      (6, 'The clever cat runs crazily around the house', 'animals', 'Bob'),
      (7, 'Running in the park is excellent exercise', 'sports', 'Charlie'),
      (8, 'Machine learning models process text efficiently', 'technology', 'David'),
      (9, 'The fuzzy puppy loves to play with toys', 'animals', 'Alice'),
      (10, 'Natural language processing enables text search', 'technology', 'David')
  """)
  ```
</CodeGroup>

### Creating FTS Index

Create a full-text search index on the text column:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  run_query("CREATE INDEX ON my_docs USING fts (text)")
  ```
</CodeGroup>

<Card title="Phrase queries require position information" icon="lightbulb">
  To use phrase queries (exact phrase matching), create the index with `with_position = true`:
</Card>

<CodeGroup>
  ```sql SQL icon="SQL" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  CREATE INDEX ON my_docs USING fts (text) WITH (with_position = true)
  ```
</CodeGroup>

Without position information, phrase queries will not work. See the [Phrase Queries](#phrase-queries) section below for details.

## Basic Full-Text Search

Use the `fts()` UDTF in SQL queries with JSON-formatted search queries:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery

  # Create a match query and convert to JSON
  query = MatchQuery("puppy", "text")
  json_query = query.to_json()

  # Execute FTS query via SQL - returns top 5 matches in arbitrary order
  result = run_query(f"""
      SELECT id, text, category
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)

  print(result.to_pandas())
  # Output (4 documents match "puppy", showing all matches):
  #    id                                            text category
  # 0   1        The happy puppy runs merrily in the park  animals
  # 1   3  The puppy catches a ball with great enthusiasm   sports
  # 2   5 Puppy training requires patience and dedication training
  # 3   9         The fuzzy puppy loves to play with toys  animals
  ```
</CodeGroup>

<Card title="Understanding result ordering and relevance scores" icon="lightbulb">
  FTS queries compute a BM25 relevance score for each matching document and by default return the top 5 matching results in **arbitrary order**:
</Card>

**For exact ordering by relevance**, select the special `_score` column and order by it:

<CodeGroup>
  ```sql SQL icon="SQL" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  -- ✅ Returns top 5 matching results ordered by relevance (highest first)
  SELECT id, text, _score FROM fts('my_docs', 'query')
  ORDER BY _score DESC
  LIMIT 5
  ```
</CodeGroup>

<Info>
  **Key points:**

  * Without `ORDER BY _score DESC`, you get the top matching results but in arbitrary order
  * The `_score` column is optional - include it only when you need to see or order by relevance scores
  * `_score` uses the BM25 ranking algorithm to measure relevance
</Info>

## Advanced Query Types

### Fuzzy Search

Fuzzy search allows you to find matches even when the search terms contain typos:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery

  # Search with fuzzy matching (allows 2 character edits)
  query = MatchQuery("pupy", "text", fuzziness=2)
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)

  print(result.to_pandas())
  # Output - fuzzy matching finds "puppy" despite the typo "pupy":
  #    id                                            text
  # 0   9         The fuzzy puppy loves to play with toys
  # 1   1        The happy puppy runs merrily in the park
  # 2   5 Puppy training requires patience and dedication
  # 3   3  The puppy catches a ball with great enthusiasm
  ```
</CodeGroup>

### Phrase Queries

Search for exact phrases in documents:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import PhraseQuery

  # Search for exact phrase
  query = PhraseQuery("happy puppy", "text")
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)
  ```
</CodeGroup>

For phrase queries to work, the FTS index must be created with `with_position=true`:

<CodeGroup>
  ```sql SQL icon="SQL" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  CREATE INDEX ON my_docs USING fts (text) WITH (with_position = true)
  ```
</CodeGroup>

#### Phrase Queries with Slop

Allow some flexibility in phrase matching with the `slop` parameter:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import PhraseQuery

  # Allow up to 2 words between "puppy" and "park"
  query = PhraseQuery("puppy park", "text", slop=2)
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)
  ```
</CodeGroup>

### Boolean Queries

Combine multiple queries using boolean logic:

#### AND Queries

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery

  # Find documents containing both "puppy" AND "happy"
  query = MatchQuery("puppy", "text") & MatchQuery("happy", "text")
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)
  ```
</CodeGroup>

#### OR Queries

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery

  # Find documents containing either "puppy" OR "kitten"
  query = MatchQuery("puppy", "text") | MatchQuery("kitten", "text")
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text, category
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)

  print(result.to_pandas())
  # Output shows results matching either term:
  #    id                                            text category
  # 0   2   A curious kitten jumps quickly over the fence  animals
  # 1   9         The fuzzy puppy loves to play with toys  animals
  # 2   5 Puppy training requires patience and dedication training
  # 3   1        The happy puppy runs merrily in the park  animals
  # 4   3  The puppy catches a ball with great enthusiasm   sports
  ```
</CodeGroup>

### Boost Queries

Control relevance by boosting or demoting certain terms:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery, BoostQuery

  # Boost documents with "puppy", demote those with "kitten"
  query = BoostQuery(
      positive=MatchQuery("puppy", "text"),
      negative=MatchQuery("kitten", "text"),
      negative_boost=0.2
  )
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)
  ```
</CodeGroup>

### Multi-Match Queries

Search across multiple columns simultaneously:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MultiMatchQuery

  # Search "puppy" in both text and category columns
  query = MultiMatchQuery("puppy", ["text", "category"])
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text, category
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)
  ```
</CodeGroup>

#### Multi-Match with Field Boosting

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MultiMatchQuery

  # Boost matches in "text" column 2x more than "category"
  query = MultiMatchQuery("puppy", ["text", "category"], boosts=[2.0, 1.0])
  json_query = query.to_json()

  result = run_query(f"""
      SELECT id, text, category
      FROM fts('my_docs', '{json_query}')
      LIMIT 5
  """)
  ```
</CodeGroup>

## Combining FTS with SQL

FTS queries can be combined with standard SQL features like WHERE clauses, GROUP BY, and JOINs:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.query import MatchQuery

  query = MatchQuery("puppy", "text")
  json_query = query.to_json()

  # Combine FTS with WHERE clause to filter by category
  result = run_query(f"""
      SELECT id, text, category
      FROM fts('my_docs', '{json_query}')
      WHERE category = 'animals'
      LIMIT 5
  """)
  ```
</CodeGroup>

## Query Parameters Reference

For detailed information about query parameters and options for `MatchQuery`, `PhraseQuery`, `BoostQuery`, and `MultiMatchQuery`, see the [Full-Text Search documentation](/search/full-text-search/).

## Related Documentation

* [Full-text search](/search/full-text-search/) - Learn about FTS capabilities and query types
* [SQL queries](/search/sql) - General SQL query documentation
* [Hybrid search](/search/hybrid-search/) - Combine FTS with vector search


# Query with SQL
Source: https://docs.lancedb.com/search/sql/index

SQL query capabilities in LanceDB Enterprise for analytical queries and data exploration.

<Badge>Enterprise-only</Badge>

[LanceDB Enterprise](/enterprise) comes with an SQL endpoint that can be used for analytical queries and data exploration. The SQL endpoint is designed to be compatible with the
[Arrow FlightSQL protocol](https://arrow.apache.org/docs/format/FlightSql.html), which allows you to use any Arrow FlightSQL-compatible client to query your data.

## Installing the client

There are Flight SQL clients available for most languages and tools.  If you find that your
preferred language or tool is not listed here, please [reach out](mailto:contact@lancedb.com) to us and we can help you find a solution.  The following examples demonstrate how to install the Python and TypeScript
clients.

<CodeGroup>
  ```bash Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # The `flightsql-dbapi` package provides a Python DB API 2 interface to the
  # LanceDB SQL endpoint. You can use it to connect to the SQL endpoint and
  # execute queries directly and get back results in pyarrow format.

  pip install flightsql-dbapi
  ```

  ```bash TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # LanceDB maintains a TypeScript client for the Arrow FlightSQL protocol.
  # You can use it to connect to the SQL endpoint and execute queries directly.
  # Results are returned in Arrow format or as plain JS/TS objects.

  npm install --save @lancedb/flightsql-client
  ```
</CodeGroup>

## Usage

LanceDB uses the powerful DataFusion query engine to execute SQL queries.  This means that
you can use a wide variety of SQL syntax and functions to query your data.  For more detailed
information on the SQL syntax and functions supported by DataFusion, please refer to the
[DataFusion documentation](https://datafusion.apache.org/user-guide/sql/index.html).

### Setting Up the Client

Establish a connection to your LanceDB Enterprise SQL endpoint using your preferred FlightSQL client:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from flightsql import FlightSQLClient

  client = FlightSQLClient(
      host="your-enterprise-endpoint",
      port=10025,
      insecure=True,
      token="DATABASE_TOKEN",
      metadata={"database": "your-project-slug"},
      features={"metadata-reflection": "true"},
  )
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import { Client } from "@lancedb/flightsql-client";

  const client = await Client.connect({
      host: "your-enterprise-endpoint:10025",
      username: "lancedb",
      password: "password",
  });
  ```
</CodeGroup>

### Executing a Query

Run SQL queries against your LanceDB tables. Different clients may handle the FlightSQL protocol differently:

<CodeGroup>
  ```bash Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  def run_query(query: str):
      """Simple method to fully materialize query results"""
      info = client.execute(query)
      if len(info.endpoints) != 1:
          raise Error("Expected exactly one endpoint")
      ticket = info.endpoints[0].ticket
      reader = client.do_get(ticket)
      return reader.read_all()

  result = run_query("SELECT * FROM flights WHERE origin = 'SFO'")
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const result = await client.query("SELECT * FROM flights WHERE origin = 'SFO'");
  ```
</CodeGroup>

### Processing Results

Handle the query results returned by your FlightSQL client:

<CodeGroup>
  ```bash Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  print(result)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  // Results are returned as plain JS/TS objects and we create an interface
  // here for our expected structure so we can have strong typing.  This is
  // optional but recommended.
  interface FlightRecord {
      origin: string;
      destination: string;
  }

  const flights = (await result.collectToObjects()) as FlightRecord[];
  console.log(flights);
  ```
</CodeGroup>


# Vector Search
Source: https://docs.lancedb.com/search/vector-search

Learn how to run vector search queries in LanceDB. Includes best practices, tips and examples.

Vector search is a technique used to search for similar items based on their vector representations, called embeddings. It is also known as similarity search, nearest neighbor search, or approximate nearest neighbor search.

<img alt="" />

Raw data (e.g. text, images, audio, etc.) is converted into embeddings via an embedding model, which are then stored in a vector database like LanceDB. To perform similarity search at scale, an index is created on the stored embeddings, which can then used to perform fast lookups.

## Supported distance metrics

Distance metrics determine how LanceDB compares vectors to find similar matches. Euclidean or `l2` is the default, and used for general-purpose similarity, `cosine` for unnormalized embeddings, `dot` for normalized embeddings (best performance), or `hamming` for binary vectors.

<Warning>
  Ensure you always use the same distance metric that your embedding model was trained with. Most modern embedding models use cosine similarity, so `cosine` is often the best choice. However, if your vectors are normalized, you should use `dot` for best performance.
</Warning>

The right metric improves both search accuracy and query performance. Currently, LanceDB supports the following metrics:

| Metric    | Description                                                                                                                                                                                                                                                          | Default |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `l2`      | [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) - measures the straight-line distance between two points in vector space. Calculated as the square root of the sum of squared differences between corresponding vector components.            | ✓       |
| `cosine`  | [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) - measures the cosine of the angle between two vectors, ranging from -1 to 1. Computed as the dot product divided by the product of vector magnitudes. Use for unnormalized vectors.            | x       |
| `dot`     | [Dot product](https://en.wikipedia.org/wiki/Dot_product) - calculates the sum of products of corresponding vector components. Provides raw similarity scores without normalization, sensitive to vector magnitudes. Use for normalized vectors for best performance. | x       |
| `hamming` | [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) - counts the number of positions where corresponding bits differ between binary vectors. Only applicable to binary vectors stored as packed uint8 arrays.                                         | x       |

### Configure Distance Metric

By default, `l2` will be used as metric type. You can specify the metric type as
`cosine` or `dot` if required.

**Note:** You can configure the distance metric during search only if there’s no vector index. If a vector index exists, the distance metric will always be the one you specified when creating the index.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  tbl.search(np.random.random((1536))).distance_type("cosine").limit(10).to_list()
  ```

  ```ts TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const results2 = await (
    tbl.search(Array(128).fill(1.2)) as lancedb.VectorQuery
    )
    .distanceType("cosine")
    .limit(10)
    .toArray();
  ```
</CodeGroup>

Here you can see the same search but using `cosine` similarity instead of `l2` distance. The result focuses on vector direction rather than absolute distance, which works better for normalized embeddings.

## Vector Search With ANN Index

Instead of performing an exhaustive search on the entire database for each and every query, approximate nearest neighbour (ANN) algorithms use an index to narrow down the search space, which significantly reduces query latency.

The trade-off is that the results are not guaranteed to be the true nearest neighbors of the query, but are usually "good enough" for most use cases.

Use ANN search for large-scale applications where speed matters more than perfect recall. LanceDB uses approximate nearest neighbor algorithms to deliver fast results without examining every vector in your dataset.

### Tuning `nprobes`

* `nprobes` controls how many partitions are searched at query time.
* Higher `nprobes` typically improves recall but reduces performance.
* A common starting point is to choose `nprobes` in the range 10-20, for balanced recall and latency.
* After a certain threshold, increasing `nprobes` yields only marginal accuracy gains.
* LanceDB automatically chooses a sensible `nprobes` by default to maximize performance without noticeably affecting accuracy.

### Vector Search with Prefiltering

This is the default vector search setting. You can use prefiltering to boost query performance by reducing the search space before vector calculations begin. The system first applies your filter criteria to the dataset, then conducts vector search operations only on the remaining relevant subset.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  from datasets import load_dataset

  # Connect to LanceDB
  db = lancedb.connect(
    uri="db://your-project-slug",
    api_key="your-api-key",
    region="us-east-1"
  )

  # Load query vector from dataset
  query_dataset = load_dataset("sunhaozhepy/ag_news_sbert_keywords_embeddings", split="test[5000:5001]")
  print(f"Query keywords: {query_dataset[0]['keywords']}")
  query_embed = query_dataset["keywords_embeddings"][0]

  # Open table and perform search
  table_name = "lancedb-cloud-quickstart"
  table = db.open_table(table_name)

  # Vector search with filters (pre-filtering is the default)
  search_results = (
      table.search(query_embed)
      .where("label > 2")
      .select(["text", "keywords", "label"])
      .limit(5)
      .to_pandas()
  )

  print("Search results (with pre-filtering):")
  print(search_results)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb";

  // Connect to LanceDB
  const db = await lancedb.connect({
    uri: "db://your-project-slug",
    apiKey: "your-api-key",
    region: "us-east-1"
  });

  // Generate a sample 768-dimension embedding vector (typical for BERT-based models)
  // In real applications, you would get this from an embedding model
  const dimensions = 768;
  const queryEmbed = Array.from({ length: dimensions }, () => Math.random() * 2 - 1);

  // Open table and perform search
  const tableName = "lancedb-cloud-quickstart";
  const table = await db.openTable(tableName);

  // Vector search with filters (pre-filtering is the default)
  const vectorResults = await table.search(queryEmbed)
    .where("label > 2")
    .select(["text", "keywords", "label"])
    .limit(5)
    .toArray();

  console.log("Search results (with pre-filtering):");
  console.log(vectorResults);
  ```
</CodeGroup>

This filters out rows where label ≤ 2 before doing vector search, then picks specific columns from the top 5 matches.

The `.where("label > 2")` applies a filter before vector search, `.select(["text", "keywords", "label"])` chooses specific columns to return, and `.limit(5)` restricts results to the top `5` most similar vectors.

As a result, you'll see a pandas DataFrame with just the data you want from the most similar vectors.

### Vector Search with Postfiltering

Use postfiltering to prioritize vector similarity by searching the full dataset first, then applying metadata filters to the top results. This approach ensures you get the most similar vectors before filtering, which can be crucial when similarity is more important than metadata constraints.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  results_post_filtered = (
      table.search(query_embed)
      .where("label > 1", prefilter=False)
      .select(["text", "keywords", "label"])
      .limit(5)
      .to_pandas()
  )

  print("Vector search results with post-filter:")
  print(results_post_filtered)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  const vectorResultsWithPostFilter = await (table.search(queryEmbed) as VectorQuery)
    .where("label > 2")
    .postfilter()
    .select(["text", "keywords", "label"])
    .limit(5)
    .toArray();

  console.log("Vector search results with post-filter:");
  console.log(vectorResultsWithPostFilter);
  ```
</CodeGroup>

Here you can see how to do vector search first to get the most similar vectors, then filter by label > 1 on those results.

The `prefilter=False` parameter tells LanceDB to apply the filter after vector search instead of before, `.where("label > 1")` filters the top results by metadata, and `.select()` chooses which columns to include.

In the end, you receive a pandas DataFrame with the best matches that also meet your metadata requirements.

<Card icon="book">
  [Post-filtering](/search/filtering/#post-filtering-with-vector-search) in LanceDB applies
  the filter condition after obtaining the nearest neighbors based on vector similarity.
</Card>

## Multivector Search

Use multivector search when your documents contain multiple embeddings and you need sophisticated matching between query and document vector pairs. The late interaction approach finds the most relevant combinations across all available embeddings and provides nuanced similarity scoring.

Only `cosine` similarity is supported as the distance metric for multivector search operations.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  query_multi = np.random.random(size=(2, 256))
  results_multi = tbl.search(query_multi).limit(5).to_pandas()
  ```
</CodeGroup>

Here you can see how to take 2 query vectors and find the best matching pairs between them and document vectors using late interaction. The `np.random.random(size=(2, 256))` creates a 2×256 array with two random query vectors, `.limit(5)` returns the top 5 best document-query combinations, and `.to_pandas()` provides results in a DataFrame format.

**Read more:** [Multivector search](/search/multivector-search/)

## Advanced Search Scenarios

### Search With Distance Range

Use `distance_range` search when you need vectors within particular similarity bounds rather than just the closest neighbors. The system filters results to only include vectors that fall within your specified distance thresholds from the query.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  query = np.random.random(256)

  # Search for the vectors within the range of [0.1, 0.5)
  tbl.search(query).distance_range(0.1, 0.5).to_arrow()

  # Search for the vectors with the distance less than 0.5
  tbl.search(query).distance_range(upper_bound=0.5).to_arrow()

  # Search for the vectors with the distance greater or equal to 0.1
  tbl.search(query).distance_range(lower_bound=0.1).to_arrow()
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb";

  const results3 = await (
    tbl.search(Array(128).fill(1.2)) as lancedb.VectorQuery
  )
    .distanceType("cosine")
    .distanceRange(0.1, 0.2)
    .limit(10)
    .toArray();
  ```
</CodeGroup>

This shows three ways to search within distance ranges: bounded, upper bound only, and lower bound only.

The `distance_range()` method filters results by similarity thresholds - the first example finds vectors with distance between `0.1` and `0.5`, the second finds vectors closer than `0.5`, and the third finds vectors farther than `0.1`.

Each approach returns Arrow tables with vectors that fall within your specified distance thresholds.

### Search With Binary Vectors

Use binary vector search for scenarios involving binary embeddings, such as those produced by hashing algorithms. The system stores these efficiently as packed uint8 arrays and uses Hamming distance calculations to determine vector similarity.

<Tip>
  The number of dimensions of the binary vector must be a multiple of 8. A vector of dimensionality 128 will be stored as a `uint8` array of size 16.
</Tip>

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  import numpy as np
  import pyarrow as pa
  import pytest

  db = lancedb.connect("data/binary_lancedb")
  schema = pa.schema(
      [
          pa.field("id", pa.int64()),
          # for dim=256, lance stores every 8 bits in a byte
          # so the vector field should be a list of 256 / 8 = 32 bytes
          pa.field("vector", pa.list_(pa.uint8(), 32)),
      ]
  )
  tbl = db.create_table("my_binary_vectors", schema=schema)

  data = []
  for i in range(1024):
      vector = np.random.randint(0, 2, size=256)
      # pack the binary vector into bytes to save space
      packed_vector = np.packbits(vector)
      data.append(
          {
              "id": i,
              "vector": packed_vector,
          }
      )
  tbl.add(data)

  query = np.random.randint(0, 2, size=256)
  packed_query = np.packbits(query)
  tbl.search(packed_query).distance_type("hamming").to_arrow()
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb";

  import { Field, FixedSizeList, Int32, Schema, Uint8 } from "apache-arrow";

  const schema = new Schema([
    new Field("id", new Int32(), true),
    new Field("vec", new FixedSizeList(32, new Field("item", new Uint8()))),
  ]);
  const data = lancedb.makeArrowTable(
    Array(1_000)
      .fill(0)
      .map((_, i) => ({
        // the 256 bits would be store in 32 bytes,
        // if your data is already in this format, you can skip the packBits step
        id: i,
        vec: lancedb.packBits(Array(256).fill(i % 2)),
      })),
    { schema: schema },
  );

  const tbl = await db.createTable("binary_table", data);
  await tbl.createIndex("vec", {
    config: lancedb.Index.ivfFlat({
      numPartitions: 10,
      distanceType: "hamming",
    }),
  });

        const query = Array(32)
          .fill(1)
          .map(() => Math.floor(Math.random() * 255));
        const results = await tbl.query().nearestTo(query).limit(10).toArrow();
        // --8<-- [end:search_binary_data
        expect(results.numRows).toBe(10);
      }
    });
  });
  ```
</CodeGroup>

Here you can see how to set up a table for binary vectors, pack them efficiently into bytes, and search using Hamming distance.

The schema defines a 32-byte vector field (256 bits ÷ 8), `np.random.randint(0, 2, size=256)` creates binary vectors, `np.packbits()` compresses them to bytes, and `.distance_type("hamming")` specifies `hamming` distance for similarity calculation.

The search produces an Arrow table with binary vectors ranked by how many bits differ from the query.

## Scaling Vector Search

### Batch Search

Use batch search to handle multiple query vectors simultaneously. This gives you significant efficiency gains over individual queries. LanceDB processes all vectors in parallel and organizes results with a `query_index` field that maps each result set back to its originating query.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Load a batch of query embeddings
  query_dataset = load_dataset(
      "sunhaozhepy/ag_news_sbert_keywords_embeddings", split="test[5000:5005]"
  )
  query_embeds = query_dataset["keywords_embeddings"]
  batch_results = table.search(query_embeds).limit(5).to_pandas()
  print(batch_results)
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
   // Batch query
  console.log("Performing batch vector search...");
  const batchSize = 5;
  const queryVectors = Array.from(
    { length: batchSize },
    () => Array.from(
      { length: dimensions },
      () => Math.random() * 2 - 1,
    ),
  );
  let batchQuery = table.search(queryVectors[0]) as VectorQuery;
  for (let i = 1; i < batchSize; i++) {
    batchQuery = batchQuery.addQueryVector(queryVectors[i]);
  }
  const batchResults = await batchQuery
    .select(["text", "keywords", "label"])
    .limit(5)
    .toArray();
  console.log("Batch vector search results:");
  console.log(batchResults);
  ```
</CodeGroup>

This takes 5 query embeddings and finds the top 5 matches for each one in a single batch operation.

The `load_dataset()` loads embeddings from a Hugging Face dataset, `query_embeds` contains `5` query vectors, and `.search(query_embeds)` processes all queries simultaneously.

The final result is a pandas DataFrame with all results, including a `query_index` to tell you which query each result came from.

<Tip>
  When processing batch queries, the results include a `query_index` field
  to explicitly associate each result set with its corresponding query in
  the input batch.
</Tip>

### Search With Asynchronous Indexing

To optimize for speed over completeness, enable the `fast_search` flag in your query to skip searching unindexed data.

While vector indexing occurs asynchronously, newly added vectors are immediately
searchable through a fallback brute-force search mechanism. This ensures zero
latency between data insertion and searchability, though it may temporarily
increase query response times.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.search(embedding, fast_search=True).limit(5).to_pandas()
  ```

  ```ts TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  await table
    .query()
    .nearestTo(embedding)
    .fastSearch()
    .limit(5)
    .toArray();
  ```
</CodeGroup>

Here you can see how to turn on fast search mode to skip unindexed vectors and only look through indexed data for speed.

The `fast_search=True` parameter tells LanceDB to only search indexed vectors, skipping any recently added data that hasn't been indexed yet.

You'll obtain a pandas DataFrame with the top `5` matches from indexed vectors, but might miss data that was just added.

## Brute Force Search

### Search With No Index

The simplest way to perform vector search is to perform a brute force search, without an index, where the distance between the query vector and all the vectors in the database are computed, with the top-k closest vectors returned.

This is equivalent to a k-nearest neighbours (kNN) search in vector space.

Choose brute force search when you need guaranteed 100% recall, typically with smaller datasets where query speed isn't the primary concern. The system scans every vector in the table and calculates precise distances to find the exact nearest neighbors.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  tbl.search(np.random.random((1536))).limit(3).to_list()
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import * as lancedb from "@lancedb/lancedb";

  const db = await lancedb.connect(databaseDir);
  const tbl = await db.openTable("my_vectors");

  const results1 = await tbl.search(Array(128).fill(1.2)).limit(3).toArray();
  ```
</CodeGroup>

This carries out a brute force search through every vector in the table to find the 3 closest matches to a random 1536-dimensional query. You'll get back a list of the most similar vectors with exact distances.

<img alt="" />

As you can imagine, the brute force approach is not scalable for datasets larger than a few hundred thousand vectors, as the latency of the search grows linearly with the size of the dataset. This is where approximate nearest neighbour (ANN) algorithms come in.

### Bypass the Vector Index

Use `bypass_vector_index` to get exact, ground-truth results by performing exhaustive searches across all vectors. Instead of relying on approximate methods, the system directly compares your query against every vector in the table, ensuring 100% recall at the cost of increased query time.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table.search(embedding).bypass_vector_index().limit(5).to_pandas()
  ```

  ```typescript TypeScript icon="square-js" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  await table
    .query()
    .nearestTo(embedding)
    .bypassVectorIndex()
    .limit(5)
    .toArray();
  ```
</CodeGroup>

This skips the approximate index and checks every single vector for exact, ground-truth results.

The `.bypass_vector_index()` method forces LanceDB to perform an exhaustive search through all vectors instead of using the approximate nearest neighbor index, ensuring exact results but at the cost of slower performance.

The outcome is a pandas DataFrame with the top 5 exact matches, guaranteeing 100% recall but taking longer to run.

This approach is particularly useful when:

* Evaluating ANN index quality
* Calculating recall metrics to tune index parameters
* Ensuring exact results for critical applications


# Configuring Cloud Storage in LanceDB
Source: https://docs.lancedb.com/storage/configuration

Configure LanceDB to use S3, GCS, Azure Blob, and S3-compatible object stores with environment variables or storage options.

When using LanceDB OSS, you can choose where to store your data. The tradeoffs between storage options are covered in the [storage architecture guide](/storage). This page shows how to configure each backend.

## Object stores

LanceDB supports AWS S3 (and compatible stores), Azure Blob Storage, and Google Cloud Storage. The URI scheme in your `connect` call selects the backend.

### Configuration options

When running inside the target cloud with correct IAM bindings, LanceDB often needs no extra configuration. When running elsewhere, provide credentials via environment variables or `storage_options`.

<Info title="Storage option casing">
  Keys are case-insensitive. Use lowercase in `storage_options` and uppercase in environment variables.
</Info>

If you need the option to apply only to a specific table:

#### General object store options

| Key                          | Description                                                    |
| :--------------------------- | :------------------------------------------------------------- |
| `allow_http`                 | Allow non-TLS connections. Default: `false`.                   |
| `allow_invalid_certificates` | Skip certificate validation. Default: `false`.                 |
| `connect_timeout`            | Timeout for the connect phase. Default: `5s`.                  |
| `timeout`                    | Timeout for the full request. Default: `30s`.                  |
| `user_agent`                 | User agent string to send with requests.                       |
| `proxy_url`                  | Proxy URL to route requests through.                           |
| `proxy_ca_certificate`       | PEM-formatted CA certificate for proxy connections.            |
| `proxy_excludes`             | Comma-separated hosts that bypass the proxy (domains or CIDR). |

## AWS S3

<img alt="" />

Set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and optionally `AWS_SESSION_TOKEN` as environment variables or pass them in `storage_options`. Region is optional for AWS but required for most S3-compatible stores.

Minimum permissions usually include `s3:PutObject`, `s3:GetObject`, `s3:DeleteObject`, `s3:ListBucket`, and `s3:GetBucketLocation` scoped to the relevant bucket/prefix.

### S3-compatible stores

If the endpoint is `http://` (common in local development), also set `ALLOW_HTTP=true` or pass `allow_http=True` in `storage_options`.

### S3 Express

Consult AWS networking requirements for S3 Express before enabling.

### DynamoDB commit store for concurrent writes

S3 lacks atomic writes. To enable safe concurrent writers, use DynamoDB as a commit store by switching to the `s3+ddb` scheme and specifying the table name.

Create the DynamoDB table with hash key `base_uri` (string) and range key `version` (number). Small provisioned throughput (for example `ReadCapacityUnits=1`, `WriteCapacityUnits=1`) is sufficient for coordination.

<Tip title="Clean up failed multipart uploads">
  LanceDB aborts multipart uploads on graceful shutdown, but crashes can leave incomplete uploads. Add an S3 lifecycle rule to delete in-progress uploads after a few days.
</Tip>

## Google Cloud Storage

<img alt="" />

Provide credentials via `GOOGLE_SERVICE_ACCOUNT` (path to JSON) or include the path in `storage_options`. GCS defaults to HTTP/1; set `HTTP1_ONLY=false` if you need HTTP/2.

## Azure Blob Storage

<img alt="" />

Set `AZURE_STORAGE_ACCOUNT_NAME` and `AZURE_STORAGE_ACCOUNT_KEY` as environment variables, or pass them via `storage_options`.

Other supported keys include service principal credentials (`azure_client_id`, `azure_client_secret`, `azure_tenant_id`), SAS tokens, managed identities, and custom endpoints.

## Tigris Object Storage

<img alt="" />

Tigris exposes an S3-compatible API. Configure the endpoint and region:

Environment variables `AWS_ENDPOINT=https://t3.storage.dev` and `AWS_DEFAULT_REGION=auto` achieve the same configuration.


# Storage Architecture in LanceDB
Source: https://docs.lancedb.com/storage/index

Understand LanceDB storage backends, tradeoffs, and how to pick the right option for your latency, scale, and cost goals.

LanceDB is one of the few vector databases built on modular, disk-first components. That design makes it flexible enough to run across local NVMe, EBS, EFS, and any object store that exposes an S3-compatible API.

Choosing a backend is a balance between latency, scalability, cost, and operational complexity. Use this guide to pick the right fit for your workload.

## Storage backend selection guide

<img alt="" />

When architecting your system, ask yourself:

* **Latency**: How fast do I need results? What do the p50 and p95 look like?
* **Scalability**: Can I scale data volume and QPS easily?
* **Cost**: What is the all-in cost of storage plus serving?
* **Reliability/Availability**: How will replication and disaster recovery work?

## Storage backend comparison

Below is a high-level comparison ordered from lowest cost to lowest latency.

### 1. Object storage (S3 / GCS / Azure Blob)

* **Latency**: Highest; expect hundreds of milliseconds and higher p95.
* **Scalability**: Effectively unlimited storage; QPS bound by concurrency limits.
* **Cost**: Lowest overall.
* **Reliability/Availability**: Highly available, backed by cloud SLAs.

LanceDB separates storage and compute and writes immutable fragments, making it a strong fit for stateless, horizontally scalable deployments.

### 2. File storage (EFS / GCS Filestore / Azure File)

* **Latency**: Better than object storage; p95 under \~\<100ms is typical.
* **Scalability**: High, but limited by provisioned IOPS per volume.
* **Cost**: More than object storage but cheaper than in-memory options; cold data can tier down automatically.
* **Reliability/Availability**: Highly available; replication/backup must be managed separately.

Keep a copy of data in object storage for disaster recovery. If zero downtime is required, provision a second network file system with replicated data.

### 3. Third-party storage (e.g., MinIO, WekaFS)

* **Latency**: Similar to EFS; typically under \<100ms.
* **Scalability**: Determined by the chosen vendor’s cluster sizing.
* **Cost**: Higher than S3; may edge above EFS at larger scales.
* **Reliability/Availability**: Shareable across many nodes; replication depends on vendor capabilities.

### 4. Block storage (EBS / GCP Persistent Disk / Azure Managed Disk)

* **Latency**: Near-local performance; often \<30ms.
* **Scalability**: Not shareable across instances; shard or copy data when scaling.
* **Cost**: Higher than networked file systems, plus potential I/O charges.
* **Reliability/Availability**: Persists through instance restarts; backups and sharding must be managed.

### 5. Local storage (SSD / NVMe)

* **Latency**: Fastest; p95 often under \<10ms.
* **Scalability**: Hard to scale in cloud environments; requires sharding or additional copies for higher QPS.
* **Cost**: Highest; tightly coupling compute and storage makes horizontal scaling difficult.
* **Reliability/Availability**: Data is tied to the instance; backups must be rigorous.

Use local disk only when you need extremely low latency and are comfortable owning the operational overhead.


# Consistency
Source: https://docs.lancedb.com/tables/consistency

Learn about consistency settings and versioning in LanceDB tables.

You can set the `read_consistency_interval` parameter on connections to achieve different levels of read consistency. This parameter determines how frequently the database synchronizes with the underlying storage system to check for updates made by other processes. If another process updates a table, the database will not see the changes until the next synchronization.

There are three possible settings for `read_consistency_interval`:

1. **Unset (default)**: The database does not check for updates to tables made by other processes. This provides the best query performance, but means that clients may not see the most up-to-date data. This setting is suitable for applications where the data does not change during the lifetime of the table reference.
2. **Zero seconds (Strong consistency)**: The database checks for updates on every read. This provides the strongest consistency guarantees, ensuring that all clients see the latest committed data. However, it has the most overhead. This setting is suitable when consistency matters more than having high QPS.
3. **Custom interval (Eventual consistency)**: The database checks for updates at a custom interval, such as every 5 seconds. This provides eventual consistency, allowing for some lag between write and read operations. Performance-wise, this is a middle ground between strong consistency and no consistency check. This setting is suitable for applications where immediate consistency is not critical, but clients should see updated data eventually.

<Info>
  In LanceDB <Badge>Enterprise</Badge>, read consistency are tunable via the configuration
  settings. In LanceDB <Badge>Cloud</Badge>, readers are always strongly consistent.
</Info>

## Configuring Consistency Parameters

To set strong consistency, set the interval to 0:

For eventual consistency, use a custom interval:

By default, a `Table` will never check for updates from other writers. To manually check for updates you can use `checkout_latest`:

## Handling bad vectors

In LanceDB Python, you can use the `on_bad_vectors` parameter to choose how
invalid vector values are handled. Invalid vectors are vectors that are not valid
because:

1. They are the wrong dimension
2. They contain NaN values
3. They are null but are on a non-nullable field

By default, LanceDB will raise an error if it encounters a bad vector. You can
also choose one of the following options:

* `drop`: Ignore rows with bad vectors
* `fill`: Replace bad values (NaNs) or missing values (too few dimensions) with
  the fill value specified in the `fill_value` parameter. An input like
  `[1.0, NaN, 3.0]` will be replaced with `[1.0, 0.0, 3.0]` if `fill_value=0.0`.
* `null`: Replace bad vectors with null (only works if the column is nullable).
  A bad vector `[1.0, NaN, 3.0]` will be replaced with `null` if the column is
  nullable. If the vector column is non-nullable, then bad vectors will cause an
  error


# Ingesting Data
Source: https://docs.lancedb.com/tables/create

Learn about different methods to ingest data into tables in LanceDB, including from various data sources and empty tables.

In LanceDB, tables store records with a defined schema that specifies column names and types. You can create LanceDB tables from these data formats:

* Pandas DataFrames
* [Polars](https://pola.rs/) DataFrames
* Apache Arrow Tables

The Python SDK additionally supports:

* PyArrow schemas for explicit schema control
* `LanceModel` for Pydantic-based validation

## Create a LanceDB Table

Initialize a LanceDB connection and create a table

LanceDB allows ingesting data from various sources - `dict`, `list[dict]`, `pd.DataFrame`, `pa.Table` or a `Iterator[pa.RecordBatch]`. Let's take a look at some of the these.

### From list of tuples or dictionaries

### From a Pandas DataFrame

<Note title="Note">
  Data is converted to Arrow before being written to disk. For maximum control over how data is saved, either provide the PyArrow schema to convert to or else provide a PyArrow Table directly.
</Note>

<Note title="Vector Column Type">
  The **`vector`** column needs to be a [Vector](/integrations/data/pydantic#vector-field) (defined as [pyarrow.FixedSizeList](https://arrow.apache.org/docs/python/generated/pyarrow.list_.html)) type.
</Note>

#### From a custom schema

### From a Polars DataFrame

LanceDB supports [Polars](https://pola.rs/), a modern, fast DataFrame library
written in Rust. Just like in Pandas, the Polars integration is enabled by PyArrow
under the hood. A deeper integration between LanceDB Tables and Polars DataFrames
is on the way.

### From an Arrow Table

You can also create LanceDB tables directly from Arrow tables.
LanceDB supports float16 data type!

### From Pydantic Models

When you create an empty table without data, you must specify the table schema.
LanceDB supports creating tables by specifying a PyArrow schema or a specialized
Pydantic model called `LanceModel`.

For example, the following Content model specifies a table with 5 columns:
`movie_id`, `vector`, `genres`, `title`, and `imdb_id`. When you create a table, you can
pass the class as the value of the `schema` parameter to `create_table`.
The `vector` column is a `Vector` type, which is a specialized Pydantic type that
can be configured with the vector dimensions. It is also important to note that
LanceDB only understands subclasses of `lancedb.pydantic.LanceModel`
(which itself derives from `pydantic.BaseModel`).

#### Nested schemas

Sometimes your data model may contain nested objects. For example, you may want to store the document string and the document source name as a nested Document object:

This can be used as the type of a LanceDB table column:

This creates a struct column called "document" that has two subfields
called "content" and "source":

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
In [28]: tbl.schema
Out[28]:
id: string not null
vector: fixed_size_list<item: float>[1536] not null
    child 0, item: float
document: struct<content: string not null, source: string not null> not null
    child 0, content: string not null
    child 1, source: string not null
```

#### Validators

Because `LanceModel` inherits from Pydantic's `BaseModel`, you can combine them with Pydantic's
[field validators](https://docs.pydantic.dev/latest/concepts/validators). The example
below shows how to add a validator to ensure that only valid timezone-aware datetime objects are used
for a `created_at` field.

When you run this code it, should raise the `ValidationError`.

### Using Iterators / Writing Large Datasets

It is recommended to use iterators to add large datasets in batches when creating your table in one go. This does not create multiple versions of your dataset unlike manually adding batches using `table.add()`

LanceDB additionally supports PyArrow's `RecordBatch` Iterators or other generators producing supported data types.

Here's an example using using `RecordBatch` iterator for creating tables.

You can also use iterators of other types like Pandas DataFrame or Pylists directly in the above example.

## Open existing tables

If you forget the name of your table, you can always get a listing of all table names.

## Creating empty table

You can create an empty table for scenarios where you want to add data to the table later.
An example would be when you want to collect data from a stream/external file and then add it to a table in
batches.

An empty table can be initialized via a PyArrow schema.

Alternatively, you can also use Pydantic to specify the schema for the empty table. Note that we do not
directly import `pydantic` but instead use `lancedb.pydantic` which is a subclass of `pydantic.BaseModel`
that has been extended to support LanceDB specific types like `Vector`.

Once the empty table has been created, you can append to it or modify its contents,
as explained in the [updating and modifying tables](/tables/update) section.

## Drop a table

Use the `drop_table()` method on the database to remove a table.

This permanently removes the table and is not recoverable, unlike deleting rows.
By default, if the table does not exist an exception is raised. To suppress this,
you can pass in `ignore_missing=True`.


# Basic Table Operations
Source: https://docs.lancedb.com/tables/index

Create tables, search vectors, and append data in LanceDB.

Now that you've completed the [LanceDB quickstart](/quickstart), you're ready to
explore some more table operations you'll typically need when working with LanceDB.

* **Ingest data into tables** from JSON data (and in Python, Pandas or Polars DataFrames)
* **Create empty tables** by defining explicit Arrow schemas
* **Vector similarity search** with filtering and projections
* **Filtered queries** that can operate on nested structs
* **Interoperate with DuckDB** and run traditional SQL queries on an Arrow table (Python)

## Dataset

We'll work with this small dataset based on characters from the legends of Camelot. Note that
the `vector` column holds 4-dimensional embeddings, and the `stats` column is a nested struct
with several integer fields, indicating each character's attributes.

```json camelot.json icon="brackets-curly" expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
[
  {
    "id": 1,
    "name": "King Arthur",
    "role": "King of Camelot",
    "description": "The legendary ruler of Camelot, wielder of Excalibur, and leader of the Knights of the Round Table.",
    "vector": [0.72, -0.28, 0.60, 0.86],
    "stats": { "strength": 2, "courage": 5, "magic": 1, "wisdom": 4 }
  },
  {
    "id": 2,
    "name": "Merlin",
    "role": "Wizard and Advisor",
    "description": "A powerful wizard and prophet who mentors Arthur and shapes the destiny of Camelot through magic and foresight.",
    "vector": [0.05, 0.88, 0.62, 0.85],
    "stats": { "strength": 2, "courage": 4, "magic": 5, "wisdom": 5 }
  },
  {
    "id": 3,
    "name": "Queen Guinevere",
    "role": "Queen of Camelot",
    "description": "Arthur's queen, admired for her grace and diplomacy, whose romances and loyalties influence Camelot's fate.",
    "vector": [0.22, -0.22, 0.42, 0.82],
    "stats": { "strength": 1, "courage": 3, "magic": 1, "wisdom": 4 }
  },
  {
    "id": 4,
    "name": "Sir Lancelot",
    "role": "Knight of the Round Table",
    "description": "Arthur's most skilled knight, famed for unmatched combat prowess and his tragic love for Queen Guinevere.",
    "vector": [0.86, -0.35, 0.38, 0.55],
    "stats": { "strength": 5, "courage": 5, "magic": 1, "wisdom": 3 }
  },
  {
    "id": 5,
    "name": "Sir Gawain",
    "role": "Knight of the Round Table",
    "description": "A noble and honorable knight known for his courtesy and his encounter with the Green Knight.",
    "vector": [0.82, -0.32, 0.52, 0.60],
    "stats": { "strength": 4, "courage": 5, "magic": 1, "wisdom": 4 }
  },
  {
    "id": 6,
    "name": "Sir Galahad",
    "role": "Knight of the Round Table",
    "description": "The purest and most virtuous knight, chosen to achieve the Holy Grail due to his unwavering spiritual purity.",
    "vector": [0.80, -0.20, 0.70, 0.78],
    "stats": { "strength": 4, "courage": 5, "magic": 2, "wisdom": 5 }
  },
  {
    "id": 7,
    "name": "Sir Percival",
    "role": "Knight of the Round Table",
    "description": "A loyal and innocent knight whose bravery and sincerity make him one of the key seekers of the Holy Grail.",
    "vector": [0.78, -0.36, 0.48, 0.52],
    "stats": { "strength": 4, "courage": 4, "magic": 1, "wisdom": 3 }
  },
  {
    "id": 8,
    "name": "Mordred",
    "role": "Traitor Knight",
    "description": "Arthur's treacherous son or nephew who ultimately rebels against him, leading to Camelot's downfall.",
    "vector": [0.68, -0.30, -0.65, 0.20],
    "stats": { "strength": 4, "courage": 2, "magic": 1, "wisdom": 2 }
  }
]
```

<Warning>
  The `vector` arrays here are synthetic and for demonstration purposes only. In your real-world
  applications, you'd generate these vectors from the raw text fields using a suitable embedding model.
</Warning>

## Connect to a database

We start by connecting to a LanceDB database path.

If you're using LanceDB Cloud or Enterprise, replace the local connection string
with the appropriate remote URI and authentication details.

## Create a table and ingest data

### From JSON

LanceDB stores records in Lance tables. Each row is a record and each column
holds a field or related metadata. The simplest way to start is to obtain the source
data as a list of JSON records that includes a vector column and any metadata
fields you care about.

Load the data from the JSON file:

You can now create a LanceDB table from the loaded data. Use the `mode="overwrite"` to
replace any existing table with the same name and overwrite its data (useful during
initial testing).

<Warning>
  If you want to avoid overwriting an existing table, omit the overwrite mode.
</Warning>

### From Pandas DataFrames

<Badge>Python Only</Badge>

You can create LanceDB tables directly from [Pandas](https://pandas.pydata.org/) DataFrames. Simply
obtain the source data as a Pandas DataFrame, then create the table
and directly ingest to it.

### From Polars DataFrames

<Badge>Python Only</Badge>

You can also create LanceDB tables directly from [Polars](https://www.pola.rs/) DataFrames. Simply
obtain the source data as a Polars DataFrame, then create the table
and directly ingest to it.

### From an Arrow schema

If you want to create an *empty* table without any data -- say you want to
define the schema first and then incrementally add data later -- you can
do so by defining an Arrow schema explicitly.

Once the empty table is defined, LanceDB is ready to accept new data via
the `add` method, as shown in the next section.

<Card title="Display table schema" icon="book">
  LanceDB tables are type-aware, leveraging Apache Arrow under the hood.
  You can display a given table's schema using the `schema` property or
  method. For example, in Python, running `print(table.schema)` would show
  something like the following:

  ```txt expandable=true theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  id: int64
  name: string
  role: string
  description: string
  vector: fixed_size_list<item: float>[4]
    child 0, item: float
  stats: struct<courage: int64, magic: int64, strength: int64, wisdom: int64>
    child 0, courage: int64
    child 1, magic: int64
    child 2, strength: int64
    child 3, wisdom: int64
  ```
</Card>

## Append data to a table

LanceDB tables are mutable, and you can append new records to existing tables.
If you're starting with a fresh session, connect to the database and open the
existing table named `camelot`.

Prepare the new records to add. Here, we add two new magical characters
via the `add` method.

We now have two new records in the table. Let's begin to query our data!

## Vector search

It's straightforward to run vector similarity search in LanceDB. Let's answer
some questions about the data using vector search with projections (returning only
the desired columns).

> Q1: *Who are the characters similar to "wizard"?*

| name                 | role                      | description                     |
| -------------------- | ------------------------- | ------------------------------- |
| Merlin               | Wizard and Advisor        | A powerful wizard and prophet   |
| The Lady of the Lake | Mystical Guardian         | A mysterious supernatural figu… |
| Morgan le Fay        | Sorceress                 | A powerful enchantress, Arthur… |
| Queen Guinevere      | Queen of Camelot          | Arthur's queen, admired for he… |
| Sir Galahad          | Knight of the Round Table | The purest and most virtuous k… |

We have Merlin, The Lady of the Lake, and Morgan le Fay in the top results, who
all have magical abilities.

Next, let's try to answer a different question that involves vector search while
filtering on a nested struct field. Filtering is done using the `where` method,
into which you can pass SQL-like expressions.

> Q2: *Who are the characters similar to "wizard" with high magic stats?*

| name                 | role               | description                     |
| -------------------- | ------------------ | ------------------------------- |
| Merlin               | Wizard and Advisor | A powerful wizard and prophet   |
| The Lady of the Lake | Mystical Guardian  | A mysterious supernatural figu… |
| Morgan le Fay        | Sorceress          | A powerful enchantress, Arthur… |

Only three characters have magical abilities greater than 3. Merlin is
clearly the most magical of them all!

## Filtered search

You can also run traditional analytics-style search queries that do not
involve vectors. For example, let's find the strongest characters in
the dataset. In the query below, we leave the `search` method empty to indicate
that we don't want to use any vector for similarity search (in TypeScript/Rust,
use `query()` instead), and use the `where` method to filter on the `strength` field.

> Q3: *Who are the strongest characters?*

| name         | role                      | description                     |
| ------------ | ------------------------- | ------------------------------- |
| Sir Galahad  | Knight of the Round Table | The purest and most virtuous k… |
| Sir Gawain   | Knight of the Round Table | A noble and honorable knight k… |
| Sir Percival | Knight of the Round Table | A loyal and innocent knight wh… |
| Sir Lancelot | Knight of the Round Table | Arthur's most skilled knight, … |
| Mordred      | Traitor Knight            | Arthur's treacherous son or ne… |

Clearly, the strongest characters are all Knights of the Round Table!

## SQL queries using DuckDB

<Badge>Python Only</Badge>

You can leverage a full SQL engine like DuckDB to run more complex queries that involve
sorting, aggregations, joins, etc. To do this, you convert the LanceDB tables to an Arrow table,
which can be natively queried by DuckDB.

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Convert table to an Arrow table
  arrow_table = table.to_arrow()

  import duckdb

  # Query the Arrow table using SQL
  duckdb_tbl = duckdb.sql("SELECT name, role, description FROM arrow_table WHERE stats.strength > 3 ORDER BY power DESC LIMIT 5")
  print(duckdb_tbl)
  ```
</CodeGroup>

| name         | role                      | description                                     |
| ------------ | ------------------------- | ----------------------------------------------- |
| Sir Galahad  | Knight of the Round Table | The purest and most virtuous knight, chosen to… |
| Sir Lancelot | Knight of the Round Table | Arthur's most skilled knight, famed for unmatc… |
| Sir Gawain   | Knight of the Round Table | A noble and honorable knight known for his cou… |
| Sir Percival | Knight of the Round Table | A loyal and innocent knight whose bravery and … |
| Mordred      | Traitor Knight            | Arthur's treacherous son or nephew who ultimat… |

<Info>
  Under the hood, Lance tables are Arrow-based, leveraging Arrow's type system. This is why
  it's trivial to query a Lance table using DuckDB, which also natively supports Arrow tables.
</Info>

## Add column

We can also add new columns to an existing LanceDB table using the `add_columns` method.
For this example, let's add a new float column named `power` that shows the average
of each character's strength, courage, magic, and wisdom stats.

The example above sums up the individual stats and divides by 4 to compute the average.
The resulting average total stats is cast to an Arrow float type under the hood for the
Lance table.

We can display the results of this column in descending order of power.

> Q4: *Who are the most powerful characters?*

Note that LanceDB's `where` only filters rows, but doesn't sort them by applying an `ORDER BY`
clause that you may be used to when working with SQL databases.

You can also sort the results after converting them to a Polars DataFrame.
In TypeScript/Rust, you can sort the
returned array in application code.

```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Sort Polars DataFrame by power in descending order
print(r1.sort("power", descending=True).limit(5))
```

| name                 | role                      | description                     | power |
| -------------------- | ------------------------- | ------------------------------- | ----- |
| Merlin               | Wizard and Advisor        | A powerful wizard and prophet … | 4.0   |
| Sir Galahad          | Knight of the Round Table | The purest and most virtuous k… | 4.0   |
| The Lady of the Lake | Mystical Guardian         | A mysterious supernatural figu… | 3.75  |
| Sir Lancelot         | Knight of the Round Table | Arthur's most skilled knight, … | 3.5   |
| Sir Gawain           | Knight of the Round Table | A noble and honorable knight k… | 3.5   |

Merlin and Sir Galahad are the most powerful characters when considering the average of
all their abilities! Sir Lancelot and the Lady of the Lake follow closely behind.

## Delete data

You can delete rows from a LanceDB table using the `delete` method with
a filtering expression.

Say we want to remove Mordred, the traitor knight, from our table.

This will delete the row(s) where the `role` value matches "Traitor Knight".
You can verify that the row has been deleted by running a search query again,
and confirming that Mordred no longer appears in the results.

## Drop column

If you want to remove or delete a column from an existing LanceDB table, you can use
the `drop_columns` method.

This will remove the `power` column we added earlier from the table schema.

## Drop table

If you want to delete an entire table from the database, you can use the
`drop_table` method.

This will delete the `camelot` table from the connected LanceDB database.

<Info>
  See the full code for these examples (including helper functions) in the
  `basic_usage` file for the appropriate client language in the
  [docs repo](https://github.com/lancedb/docs/tree/main/tests).
</Info>

## What about vector indexes?

LanceDB supports vector indexes to speed up similarity search on large datasets.
For datasets up to a few hundred thousand vectors, LanceDB's highly efficient kNN
(brute-force) retrieval of nearest neighbors is often sufficient. As your dataset
grows larger, you can create vector indexes on your vector columns to accelerate
search. See the [indexing](/indexing/) documentation for details on how to create and use
vector indexes in LanceDB.

## What's next?

Now that you've learned the basics of creating tables, adding data, running
vector search, and modifying table schemas, you're ready to explore more
advanced features of LanceDB. Below are some suggested next pages.

<Columns>
  <Card title="Ingesting data" icon="cookie" href="/tables/create/">
    Learn the different approaches to creating and ingesting data into LanceDB tables from various sources.
  </Card>

  <Card title="Update and modify tables" icon="clone" href="/tables/update/">
    Learn how to update and modify existing LanceDB tables and their data.
  </Card>

  <Card title="Schema & data evolution" icon="boxes-stacked" href="/tables/schema/">
    Understand how to evolve your table schemas and data over time with LanceDB.
  </Card>

  <Card title="Versioning and time travel" icon="clock" href="/tables/versioning/">
    Explore LanceDB's built-in table versioning and time travel capabilities.
  </Card>
</Columns>


# Multimodal Data (Blobs)
Source: https://docs.lancedb.com/tables/multimodal

Learn how to store and query multimodal data (images, audio, video) directly in LanceDB using binary columns.

LanceDB handles multimodal data—images, audio, video, and PDF files—natively by storing the raw bytes in a binary column alongside your vectors and metadata. This approach simplifies your data infrastructure by keeping the raw assets and their embeddings in the same database, eliminating the need for separate object storage for many use cases.

This guide demonstrates how to ingest, store, and retrieve image data using standard binary columns, and also introduces the **Lance Blob API** for optimized handling of larger multimodal files.

## Storing binary data

To store binary data, you need to use the `pa.binary()` data type in your Arrow schema. In Python, this corresponds to `bytes` objects if you're using LanceDB's Pydantic `LanceModel` to define the schema.

### 1. Setup and imports

First, let's import the necessary libraries. We'll use `PIL` (Pillow) for image handling and `io` for byte conversion.

### 2. Preparing data

For this example, we'll create some dummy in-memory images. In a real application, you would read these from files or an API. The key is to convert your data (image, audio, etc.) into a raw `bytes` object.

### 3. Defining the schema

When creating the table, it is **highly recommended** to define the schema explicitly. This ensures that your binary data is correctly interpreted as a `binary` type by Arrow/LanceDB and not as a generic string or list.

### 4. Ingesting data

Now, create the table using the data and the defined schema.

## Retrieving and using blobs

When you search your LanceDB table, you can retrieve the binary column just like any other metadata.

### Converting bytes back to objects

Once you have the `bytes` data back from the search result, you can decode it back into its original format (e.g., a PIL Image, an Audio buffer, etc.).

## Large Blobs (Blob API)

For larger files like high-resolution images or videos, Lance provides a specialized **Blob API**. By using `pa.large_binary()` and specific metadata, you enable **lazy loading** and optimized encoding. This allows you to work with massive datasets without loading all binary data into memory upfront.

### 1. Defining a blob schema

To use the Blob API, you must mark the column with `{"lance-encoding:blob": "true"}` metadata.

### 2. Ingesting large blobs

You can then ingest data normally, and Lance will handle the optimized storage.

<Card>
  For more advanced usage, including random access and file-like reading of blobs, see the
  Lance format's [blob API documentation](https://lance.org/guide/blob/).
</Card>

## Other modalities

The `pa.binary()` and `pa.large_binary()` types are universal. You can use this same pattern for other types of multimodal data:

* **Audio:** Read `.wav` or `.mp3` files as bytes.
* **Video:** Store video transitions or full clips using the Blob API.
* **PDFs/Documents:** Store the raw file content for document search.


# Schema and Data Evolution
Source: https://docs.lancedb.com/tables/schema

Learn how to manage table schemas in LanceDB, including adding, altering, and dropping columns.

Schema evolution enables non-breaking modifications to a database table's structure — such as adding columns, altering data types, or dropping fields — to adapt to evolving data requirements without service interruptions.
LanceDB supports ACID-compliant schema evolution through granular operations (add/alter/drop columns), allowing you to:

* Iterate Safely: Modify schemas in production with versioned datasets and backward compatibility
* Scale Seamlessly: Handle ML model iterations, regulatory changes, or feature additions
* Optimize Continuously: Remove unused fields or enforce new constraints without downtime

## Schema Evolution Operations

LanceDB supports three primary schema evolution operations:

1. **Adding new columns**: Extend your table with additional attributes
2. **Altering existing columns**: Change column names, data types, or nullability
3. **Dropping columns**: Remove unnecessary columns from your schema

<Tip title="Schema Evolution Performance">
  Schema evolution operations are applied immediately but do not typically require rewriting all data. However, data type changes may involve more substantial operations.
</Tip>

## Adding New Columns

You can add new columns to a table with the [`add_columns`](https://lancedb.github.io/lancedb/python/python/#lancedb.table.Table.add_columns)
method in Python or [`addColumns`](https://lancedb.github.io/lancedb/js/classes/Table/#addcolumns) in TypeScript/JavaScript.
New columns are populated based on SQL expressions you provide.

### Setting Up the Example Table

First, let's create a sample table with product data to demonstrate schema evolution:

### Adding Calculated Columns

You can add new columns that are calculated from existing data using SQL expressions:

### Adding Columns with Default Values

Add boolean columns with default values for status tracking:

### Adding Nullable Columns

Add timestamp columns that can contain NULL values:

<Warning title="NULL Values in New Columns">
  When adding columns that should contain NULL values, be sure to cast the NULL to the appropriate type, e.g., `cast(NULL as timestamp)`.
</Warning>

## Altering Existing Columns

You can alter columns using the [`alter_columns`](https://lancedb.github.io/lancedb/python/python/#lancedb.table.Table.alter_columns)
method in Python or [`alterColumns`](https://lancedb.github.io/lancedb/js/classes/Table/#altercolumns) in TypeScript/JavaScript. This allows you to:

* Rename a column
* Change a column's data type
* Modify nullability (whether a column can contain NULL values)

### Setting Up the Example Table

Create a table with a custom schema to demonstrate column alterations:

### Renaming Columns

Change column names to better reflect their purpose:

### Changing Data Types

Convert column data types for better performance or compatibility:

### Making Columns Nullable

Allow columns to contain NULL values:

### Multiple Changes at Once

Apply several alterations in a single operation:

<Warning title="Data Type Changes">
  Changing data types requires rewriting the column data and may be resource-intensive for large tables. Renaming columns or changing nullability is more efficient as it only updates metadata.
</Warning>

## Dropping Columns

You can remove columns using the [`drop_columns`](https://lancedb.github.io/lancedb/python/python/#lancedb.table.Table.drop_columns)
method in Python or [`dropColumns`](https://lancedb.github.io/lancedb/js/classes/Table/#dropcolumns) in TypeScript/JavaScript.

### Setting Up the Example Table

Create a table with temporary columns that we'll remove:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
table_name = "schema_evolution_drop_example"

data = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1200.00,
        "temp_col1": "X",
        "temp_col2": 100,
        "vector": np.random.random(128).tolist(),
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 800.00,
        "temp_col1": "Y",
        "temp_col2": 200,
        "vector": np.random.random(128).tolist(),
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 150.00,
        "temp_col1": "Z",
        "temp_col2": 300,
        "vector": np.random.random(128).tolist(),
    },
]

table = db.create_table(table_name, data, mode="overwrite")
```

### Dropping Single Columns

Remove individual columns that are no longer needed:

### Dropping Multiple Columns

Remove several columns at once for efficiency:

<Warning title="Irreversible Column Deletion">
  Dropping columns cannot be undone. Make sure you have backups or are certain before removing columns.
</Warning>

## Vector Column Considerations

Vector columns (used for embeddings) have special considerations. When altering vector columns, you should ensure consistent dimensionality.

### Converting List to FixedSizeList

A common schema evolution task is converting a generic list column to a fixed-size list for performance:


# Updating and Modifying Table Data
Source: https://docs.lancedb.com/tables/update

Learn how to update and modify data in LanceDB. Includes incremental updates, batch modifications, and best practices for data maintenance.

Once you have created a table, there are several ways to modify its data. You can:

* Ingest and add new records to your table;
* Update existing records that match specific conditions;
* Use the powerful Merge Insert function for more complex operations like upserting or replacing ranges of data.

These operations allow you to keep your table data current and maintain it exactly as needed for your use case. Let's look at each of these operations in detail.

<Note>
  These examples demonstrate common usage patterns. For complete API details and advanced options, refer to our SDK [documentation page](/api-reference/) and navigate to your client language of choice.
</Note>

## Connecting to LanceDB

Before performing any operations, you'll need to connect to LanceDB. The connection method depends on whether you're using LanceDB Cloud or the open source version.

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import lancedb

# Connect to LanceDB Cloud
db = lancedb.connect(
    uri="db://your-project-slug",
    api_key="your-api-key",
    region="us-east-1"
)
```

You can also connect locally using LanceDB OSS:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import lancedb

# Connect to local LanceDB
db = lancedb.connect("./data")  # Local directory for data storage
```

## Data Insertion

### Adding data to a table

Say you created a LanceDB table by passing in a `schema`.
This is an *empty* table, with no data in it. To add or append data to a table, you can use the `table.add(data)`,
as shown below.

<Note title="Vector Column Type">
  The vector column needs to be a `pyarrow.FixedSizeList` type.
</Note>

### Using Pydantic Models

Pydantic models provide a more structured way to define your table schema:

### Using Nested Models

You can use nested Pydantic models to represent complex data structures.
For example, you may want to store the document string and the document source name as a nested Document object:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from pydantic import BaseModel

class Document(BaseModel):
    content: str
    source: str
```

This can be used as the type of a LanceDB table column:

This creates a struct column called `document` that has two subfields called `content` and `source`:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
In [28]: table.schema
Out[28]:
id: string not null
vector: fixed_size_list<item: float>[128] not null
    child 0, item: float
document: struct<content: string not null, source: string not null> not null
    child 0, content: string not null
    child 1, source: string not null
```

### Batch Data Insertion

It is recommended to use iterators to add large datasets in batches when creating
your table in one go. Data will be automatically compacted for the best query performance.

#### Python Batch Insertion

<Warning title="Batch size">
  LanceDB Cloud is a multi-tenant environment with a 100MB payload limit. Adjust your batch size accordingly.
</Warning>

## Data Modification

### Update Operations

This can be used to update zero to all rows depending on how many rows match the where clause. The update queries follow the form of a SQL UPDATE statement. The `where` parameter is a SQL filter that matches on the metadata columns. The `values` or `values_sql` parameters are used to provide the new values for the columns.

<Warning title="Warning">
  Updating nested columns is not yet supported.
</Warning>

| Parameter    | Type   | Description                                                                                                                                                                       |
| ------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `where`      | `str`  | The SQL where clause to use when updating rows. For example, `'x = 2'` or `'x IN (1, 2, 3)'`. The filter must not be empty, or it will error.                                     |
| `values`     | `dict` | The values to update. The keys are the column names and the values are the values to set.                                                                                         |
| `values_sql` | `dict` | The values to update. The keys are the column names and the values are the SQL expressions to set. For example, `{'x': 'x + 1'}` will increment the value of the `x` column by 1. |

<Note title="SQL syntax">
  See the [SQL queries](/search/sql/) page for more information on the supported SQL syntax.
</Note>

Output:

```json theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
    x  vector
0  1  [1.0, 2.0]
1  3  [5.0, 6.0]
2  2  [10.0, 10.0]
```

### Updating Using SQL

The `values` parameter is used to provide the new values for the columns as literal values. You can also use the `values_sql` / `valuesSql` parameter to provide SQL expressions for the new values. For example, you can use `values_sql="x + 1"` to increment the value of the `x` column by 1.

Output:

```json theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
    x  vector
0  2  [1.0, 2.0]
1  4  [5.0, 6.0]
2  3  [10.0, 10.0]
```

<Note title="Note">
  When rows are updated, they are moved out of the index. The row will still show up in ANN queries, but the query will not be as fast as it would be if the row was in the index. If you update a large proportion of rows, consider rebuilding the index afterwards.
</Note>

### Delete Operations

Remove rows that match a condition.

<Warning title="Soft Deletion">
  Delete operations soft delete rows. Rows are hard deleted later by compaction and cleanup operations that happen in the background on LanceDB Cloud and Enterprise. The default retention on Cloud is 30 days. During this time, these rows are still accessible to query or restore by accessing old table versions (see [Versioning & Reproducibility in LanceDB](/tables/versioning/)).
</Warning>

<Warning title="Index Deletion">
  If a table is emptied, its existing indexes are removed. Recreate indexes after ingesting new data.
</Warning>

## Merge Operations

The merge insert command is a flexible API that can be used to perform `upsert`,
`insert_if_not_exists`, and `replace_range_ operations`.

<Tip title="Use scalar indexes to speed up merge insert">
  The merge insert command performs a join between the input data and the target table `on` the key you provide. This requires scanning that entire column, which can be expensive for large tables. To speed up this operation, create a scalar index on the join column, which will allow LanceDB to find matches without scanning the whole table.

  Read more about scalar indices in the [Scalar Index](/indexing/scalar-index/) guide.
</Tip>

<Tip title="HTTP 400 on Merge Insert">
  You may receive an HTTP 400 error from merge insert: `Bad request: Merge insert cannot be performed because the number of unindexed rows exceeds the maximum of 10000`. Verify that the scalar index on the join column is up to date before retrying.
</Tip>

<Note title="Embedding Functions">
  Like the create table and add APIs, the merge insert API will automatically compute embeddings if the table has an embedding definition in its schema. If the input data doesn't contain the source column, or the vector column is already filled, the embeddings won't be computed.
</Note>

### Upsert

`upsert` updates rows if they exist and inserts them if they don't. To do this with merge insert,
enable both `when_matched_update_all()` and `when_not_matched_insert_all()`.

#### Setting Up the Example Table and Performing Upsert

### Insert-if-not-exists

This will only insert rows that do not have a match in the target table, thus
preventing duplicate rows. To do this with merge insert, enable just
`when_not_matched_insert_all()`.

#### Setting Up the Example Table and Performing Insert-if-not-exists

### Replace Range

You can also replace a range of rows in the target table with the input data.
For example, if you have a table of document chunks, where each chunk has both
a `doc_id` and a `chunk_id`, you can replace all chunks for a given `doc_id` with updated chunks.

This can be tricky otherwise because if you try to use `upsert` when the new data has fewer
chunks you will end up with extra chunks. To avoid this, add another clause to delete any chunks
for the document that are not in the new data, with `when_not_matched_by_source_delete`.

#### Setting Up the Example Table and Performing Replace Range

<Tip title="Batch Size Recommendation">
  We suggest the best batch size to be 500k for optimal performance.
</Tip>


# Versioning and Reproducibility
Source: https://docs.lancedb.com/tables/versioning

Learn how to implement versioning and ensure reproducibility in LanceDB. Includes version control, data snapshots, and audit trails.

LanceDB redefines data management for AI/ML workflows with built-in,
automatic versioning powered by the [Lance columnar format](https://github.com/lancedb/lance).
Every table mutation—appends, updates, deletions, or schema changes — is tracked with
zero configuration, enabling:

* Time-Travel Debugging: Pinpoint production issues by querying historical table states.
* Atomic Rollbacks: Revert terabyte-scale datasets to any prior version in seconds.
* ML Reproducibility: Exactly reproduce training snapshots (vectors + metadata).
* Branching Workflows: Conduct A/B tests on embeddings/models via lightweight table clones.

## Basic Versioning Example

Let's create a table with sample data to demonstrate LanceDB's versioning capabilities:

### Setting Up the Table

First, let's create a table with some sample data:

### Checking Initial Version

After creating the table, let's check the initial version information:

## Modifying Data

When you modify data through operations like update or delete, LanceDB automatically creates new versions.

### Updating Existing Data

Let's update some existing records to see versioning in action:

### Adding New Data

Now let's add more records to the table:

### Checking Version Changes

Let's see how the versions have changed after our modifications:

## Tracking Changes in Schema

LanceDB's versioning system automatically tracks every schema modification. This is critical when handling evolving embedding models. For example, adding a new `vector_minilm` column creates a fresh version, enabling seamless A/B testing between embedding generations without recreating the table.

### Preparing Data for Embeddings

First, let's get the data we want to embed:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import pyarrow as pa

# Get data from table
df = table.search().limit(5).to_pandas()
```

### Generating Embeddings

Now let's generate embeddings using the all-MiniLM-L6-v2 model:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Let's use "all-MiniLM-L6-v2" model to embed the quotes
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

# Generate embeddings for each quote and pair with IDs
vectors = model.encode(
    df["quote"].tolist(), convert_to_numpy=True, normalize_embeddings=True
)
vector_dim = vectors[0].shape[0]
print(f"Vector dimension: {vector_dim}")

# Add IDs to vectors array with proper column names
vectors_with_ids = [
    {"id": i + 1, "vector_minilm": vec.tolist()} for i, vec in enumerate(vectors)
]
```

### Adding Vector Column to Schema

Now let's add the vector column to our table schema:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Add vector column and merge data
table.add_columns(
  {"vector_minilm": f"arrow_cast(NULL, 'FixedSizeList({vector_dim}, Float32)')"}
)

table.merge_insert(
  "id"
).when_matched_update_all().when_not_matched_insert_all().execute(vectors_with_ids)
```

### Checking Version Changes After Schema Modification

Let's see how the schema change affected our versioning:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Check versions after schema change
versions = table.list_versions()
version_count_after_embed = len(versions)
version_after_embed = table.version
print(f"Number of versions after adding embeddings: {version_count_after_embed}")
print(f"Current version: {version_after_embed}")

# Verify the schema change
# The table should now include a vector_minilm column containing
# embeddings generated by the all-MiniLM-L6-v2 model
print(table.schema)
```

## Rollback to Previous Versions

LanceDB supports fast rollbacks to any previous version without data duplication.

### Viewing All Versions

First, let's see all the versions we've created:

### Rolling Back to a Previous Version

Now let's roll back to before we added the vector column:

## Making Changes from Previous Versions

After restoring a table to an earlier version, you can continue making modifications. In this example, we rolled back to a version before adding embeddings. This allows us to experiment with different embedding models and compare their performance.

### Switching to a Different Embedding Model

Let's try a different embedding model (all-mpnet-base-v2) to see how it performs:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Let's switch to the all-mpnet-base-v2 model to embed the quotes
model = SentenceTransformer("all-mpnet-base-v2", device="cpu")

# Generate embeddings for each quote and pair with IDs
vectors = model.encode(
    df["quote"].tolist(), convert_to_numpy=True, normalize_embeddings=True
)
vector_dim = vectors[0].shape[0]
print(f"Vector dimension: {vector_dim}")

# Add IDs to vectors array with proper column names
vectors_with_ids = [
    {"id": i + 1, "vector_mpnet": vec.tolist()} for i, vec in enumerate(vectors)
]
```

### Adding the New Vector Column

Now let's add the new vector column with the different model:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Add vector column and merge data
table.add_columns(
    {"vector_mpnet": f"arrow_cast(NULL, 'FixedSizeList({vector_dim}, Float32)')"}
)

table.merge_insert(
    "id"
).when_matched_update_all().when_not_matched_insert_all().execute(vectors_with_ids)
```

### Checking Version Changes

Let's see how this new model affects our versioning:

```python theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
# Check versions after schema change
versions = table.list_versions()
version_count_after_alter_embed = len(versions)
version_after_alter_embed = table.version
print(
    f"Number of versions after switching model: {version_count_after_alter_embed}"
)
print(f"Current version: {version_after_alter_embed}")

# The table should now include a vector_mpnet column containing
# embeddings generated by the all-mpnet-base-v2 model
print(table.schema)
```

## Delete Data From the Table

Let's demonstrate how deletions also create new versions:

### Going Back to Latest Version

First, let's return to the latest version:

### Deleting Data

Now let's delete some data to see how it affects versioning:

### Version History and Operations

Throughout this guide, we've demonstrated various operations that create new versions in LanceDB.
Here's a summary of the version history we created:

1. **Initial Creation** (v1): Created table with quotes data and basic schema
2. **First Update** (v2): Changed "Richard" to "Richard Daniel Sanchez"
3. **Data Append** (v3): Added new quotes from both characters
4. **Schema Evolution** (v4): Added `vector_minilm` column for embeddings
5. **Embedding Merge** (v5): Populated `vector_minilm` with embeddings
6. **Version Rollback** (v6): Restored to v3 (pre-vector state)
7. **Alternative Schema** (v7): Added `vector_mpnet` column
8. **Alternative Merge** (v8): Populated `vector_mpnet` embeddings
9. **Data Cleanup** (v9): Kept only Richard Daniel Sanchez quotes

Each version represents a distinct state of your data, allowing you to:

* Track changes over time
* Compare different embedding strategies
* Revert to previous states
* Maintain data lineage for ML reproducibility

<Note title="System Operations">
  System operations like index updates and table compaction automatically increment the table version number. These background processes are tracked in the version history, though their version numbers are omitted from this example for clarity.
</Note>


# Loading Data for Model Training
Source: https://docs.lancedb.com/training/index

Introduction to loading data, shuffling, and creating permutations for model training in LanceDB.

LanceDB makes an excellent data backend for training machine learning models. This section will describe the
`Permutation` API in LanceDB that's designed to facilitate the
process of training a model and explain how to use LanceDB as a data backend for training.

## Data loading

Most model training frameworks iterate through data in batches and feed this data into the model. This process is
often referred to as **data loading**. The simplest way to load data into a model is to iterate a LanceDB table in
a loop and feed the data into the model.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb

  db = lancedb.connect("file://some/db/path")
  table = db.open_table("some_table")

  for batch in table:
      print(batch.to_pydict())
  ```
</CodeGroup>

In practice, this is too simplistic for effective training. We may not want to load all the data, or we may want
to load the data in a different order, or we may need to apply some sort of processing to the data before training.
To achieve this, we will often want to create a `Permutation` of the table.

## Selecting rows

When training a model, we might not want to load all of the data. For example, we might filter out columns that
are not needed for training. We might also divide the data into training and validation sets. Or we could divide
the data into multiple sets for cross-validation.

Whenever we create a permutation of the table, we have to first decide which rows we want to include (and in what
order). This is stored in a **permutation table** which marks out the row ids that make up our data. Other decisions,
such as which columns to include, and what transformations to apply, can be defined at read time and don't require
a separate permutation table.

<Note>
  Permutation tables are tables, just like any other table in LanceDB. By default, they are
  stored in memory but they can be persisted to storage as well. This is useful when you want to share a permutation
  table across processes or nodes.
</Note>

## Selecting all rows

To select all rows, we can use the `Permutation.identity` method. This gives us a `Permutation` without requiring
us to create a separate permutation table. This allows us to refine our columns and apply transformations and can
be useful when the data loader itself is responsible for handling sampling and shuffling.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.permutation import Permutation

  # We can create an identity permutation without needing any separate permutation table.
  permutation = Permutation.identity(table)

  # This allows us to refine our columns and apply transformations
  permutation = permutation.select_columns(["id", "prompt"])
  ```
</CodeGroup>

## Filtering rows

If we only want to select a subset of rows, then we can use a filter. This will require us to create a permutation
table which identifies which rows we want to include.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.permutation import Permutation, permutation_builder

  # We can create a permutation table which identifies which rows we want to include.
  permutation_tbl = permutation_builder(table).filter("category = 'cat'").execute()

  # We can then use this permutation table to create a Permutation object
  permutation = Permutation.from_tables(table, permutation_tbl)
  ```
</CodeGroup>

## Creating splits

LanceDB also provides several different methods for creating splits. These allow us to divide our dataset into
smaller non-overlapping sets. The split can then be specified when creating the `Permutation` object to view
only a subset of the data.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.permutation import Permutation, permutation_builder

  # Here we create two splits, one for training and one for validation.  By default, splits have no
  # name and are accessed by index.
  permutation_tbl = permutation_builder(table).split_random(ratios=[0.95, 0.05]).execute()

  # Let's create a permutation object which views only the training data.
  permutation = Permutation.from_tables(table, permutation_tbl, split=0)

  # Splits can also be given names.  The names can then be used later to access the split instead of
  # requiring us to know the index.
  permutation_tbl = permutation_builder(table).split_random(ratios=[0.95, 0.05], split_names=["train", "test"]).execute()
  permutation = Permutation.from_tables(table, permutation_tbl, split="train")
  ```
</CodeGroup>

## Shuffling rows

By default, permutations will access the data in the order the data is stored in the table. This can cause our
model to learn artifacts specific to the order of the data. This is one of many ways we can "overfit" our model
to our data. To avoid this, we typically want to shuffle the data before training. Model training frameworks
(like PyTorch) will often provide a way to shuffle the data. If you are not using one of these frameworks, or if
you want to shuffle the data with LanceDB, you can shuffle the rows when you create a permutation table.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.permutation import Permutation, permutation_builder

  # We can shuffle the rows when we create the permutation table.
  permutation_tbl = permutation_builder(table).shuffle().execute()

  # We can then use this permutation table to create a Permutation object, this will now
  # access the data in a random order.
  permutation = Permutation.from_tables(table, permutation_tbl)
  ```
</CodeGroup>

## Selecting columns

By default, permutations will return all columns in the table. If you only need a subset of the columns, you can
significantly reduce your I/O requirements by selecting only the columns you need. This can be done on the
permutation object itself, and does not require us to create a separate permutation table.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.permutation import Permutation

  # We can select only the columns we need.
  permutation = Permutation.identity(table).select_columns(["id", "prompt"])
  ```
</CodeGroup>


# PyTorch Integration
Source: https://docs.lancedb.com/training/torch

Learn how to use LanceDB with PyTorch for training and inference.

LanceDB provides a seamless integration with PyTorch for training and inference. This allows you to use LanceDB as a backend for your PyTorch models, and to use PyTorch for training and inference. You can use LanceDB to store your data, and PyTorch to train your models.

## Quickstart

The `Table` class in LanceDB implements a contract for a PyTorch
[Dataset](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset).
This means you can simply use a LanceDB table in a PyTorch dataloader directly.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  import torch
  import pyarrow as pa

  mem_db = lancedb.connect("memory://")
  table = mem_db.create_table("test_table", pa.table({"a": range(1000)}))

  # Any LanceDB table can be used as a PyTorch Dataset
  dataloader = torch.utils.data.DataLoader(
      table, batch_size=1024, shuffle=True
  )

  for batch in dataloader:
      print(batch)
  ```
</CodeGroup>

Although the `Table` class in LanceDB implements the `torch.utils.data.Dataset` interface, you'll most likely find that using
a table [Permutation](/training/) is more efficient for training.

## Selecting columns

By default, the `Table` class will return all columns in the table when used as input to PyTorch. If you only need
a subset of columns, you can significantly reduce your I/O requirements by selecting only the columns you need.

<CodeGroup>
  ```py Python icon=Python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  from lancedb.permutation import Permutation

  permutation = Permutation.identity(table).select_columns(["id", "prompt"])
  dataloader = torch.utils.data.DataLoader(
      permutation, batch_size=1024, shuffle=True
  )

  for batch in dataloader:
      print(batch.schema)
  ```
</CodeGroup>


# Troubleshooting
Source: https://docs.lancedb.com/troubleshooting

Tips for troubleshooting basic LanceDB issues.

## Frequently-asked questions

For commonly asked questions about LanceDB, please refer to our [FAQ section](/faq).

## Getting technical support

If you're using LanceDB OSS or LanceDB Cloud, the best place to get help is in our
[Discord community](https://discord.gg/AUEWnJ7Txb),
under the relevant language channel for Python, TypeScript, or Rust.
By asking in the language-specific channel, you can get help from the community
and our engineering team.

If you are a LanceDB Enterprise user, please contact our support team at [support@lancedb.com](mailto:support@lancedb.com) for dedicated assistance.

## General issues

### Slow or unexpected query results

If you have slow queries or unexpected query results, it can be helpful to
print the resolved query plan.

LanceDB provides two powerful tools for query analysis and optimization: `explain_plan` and `analyze_plan`.

Read the full guide on [Query Optimization](/search/optimize-queries/).

### Python's multiprocessing module

Multiprocessing with `fork` is not supported. You should use `spawn` instead.

### Logging: LanceDB Cloud

To provide more information, especially for LanceDB Cloud related issues, enable
debug logging. You can set the `LANCEDB_LOG` environment variable:

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
export LANCEDB_LOG=debug
```

You can turn off colors and formatting in the logs by setting

```bash theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
export LANCEDB_LOG_STYLE=never
```


# RAG and Agents
Source: https://docs.lancedb.com/tutorials/agents/index

Explore a variety of RAG (Retrieval-Augmented Generation) and agent applications built with LanceDB.

The table below lists example notebooks we've prepared for a variety of RAG (Retrieval-Augmented Generation)
and agent applications built with LanceDB.

| Project                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                       |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Contextual RAG** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/Contextual-RAG/Anthropic_Contextual_RAG.ipynb"><img alt="Open In Colab" /></a>[View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/Contextual-RAG)                                | Improves retrieval by combatting the "lost in the middle" problem. This technique uses an LLM to generate succinct context for each document chunk, then prepends that context to the chunk before embedding, leading to more accurate retrieval. |
| **Matryoshka Embeddings** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/tutorials/RAG-with_MatryoshkaEmbed-Llamaindex/main.ipynb"><img alt="Open In Colab" /></a>[View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/tutorials/RAG-with_MatryoshkaEmbed-Llamaindex) | Demonstrates a RAG pipeline using Matryoshka Embeddings with LanceDB and LlamaIndex. This method allows for efficient storage and retrieval of nested, variable-sized embeddings.                                                                 |
| **HyDE (Hypothetical Document Embeddings)** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/Advance-RAG-with-HyDE/main.ipynb"><img alt="Open In Colab" /></a>[View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/Advance-RAG-with-HyDE)             | An advanced RAG technique that uses an LLM to generate a "hypothetical" document in response to a query. This hypothetical document is then used to retrieve actual, similar documents, improving relevance.                                      |
| **Late Chunking** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/Advanced_RAG_Late_Chunking/Late_Chunking_(Chunked_Pooling).ipynb"><img alt="Open In Colab" /></a>[View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/Advanced_RAG_Late_Chunking)  | An advanced RAG method where documents are retrieved first, and then chunking is performed on the retrieved documents just before synthesis. This helps maintain context that might be lost with pre-chunking.                                    |
| **Agentic RAG** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/tutorials/Agentic_RAG/main.ipynb"><img alt="Open In Colab" /></a>[View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/tutorials/Agentic_RAG)                                                           | This tutorial demonstrates how to build a RAG system where multiple AI agents collaborate to retrieve information and generate answers, leading to more robust and intelligent applications.                                                      |


# Multimodal Agent
Source: https://docs.lancedb.com/tutorials/agents/multimodal-agent/index

Build an AI agent that understands both text and images to help users find recipes using LanceDB and PydanticAI

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pxavAGoXa-KSh_4HxNpvP2AjHPcIRpbq?usp=sharing)

Ever wanted to combine the power of text and images in a single AI agent? In this tutorial,
you'll build an agent that can understand both text and images to help users discover recipes that are relevant to them. The approach shown combines LanceDB's multimodal capabilities with [Pydantic AI](https://ai.pydantic.dev/) for the agentic workflow.

## Key Technologies

* **LanceDB**: Multimodal vector database for efficient storage and retrieval
* **PydanticAI**: Modern AI agent framework with type safety
* **Sentence Transformers**: Text embeddings for semantic search
* **CLIP**: Vision-language model for image understanding
* **Streamlit**: Interactive web application framework

## Tutorial Overview

### Option 1: Notebook

The notebook shows how to work through the steps and prepare a small sample recipe dataset, generate both text and image
embeddings, store everything efficiently in LanceDB, and then build a PydanticAI agent with custom tools to
query it. You'll finish by testing the agent against a few example questions to see the full multimodal flow
end to end.

<Card title="Notebook" href="https://colab.research.google.com/drive/1pxavAGoXa-KSh_4HxNpvP2AjHPcIRpbq?usp=sharing">
  This simple tutorial provides a step-by-step workflow with a small demo dataset of 4 examples.
  No local setup required - just click and start learning about multimodal agents.
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pxavAGoXa-KSh_4HxNpvP2AjHPcIRpbq?usp=sharing)
</Card>

### Option 2: Demo Application (Local Setup)

The demo application is the full codebase: you'll download and process a real recipe dataset with thousands
of items, run a Streamlit chat interface that supports image upload, and follow a structure that includes
production-minded touches like error handling, logging, and monitoring. Everything you need to deploy is
included.

<Card icon="download" title="Download Tutorial Files" href="https://github.com/lancedb/vectordb-recipes/tree/main/applications/multimodal-recipe-agent">
  Download the files for the full demo application here.
</Card>

### Dataset Information

* **Source**: [Kaggle Recipe Dataset](https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images)
* **Size**: Thousands of recipes with images
* **Format**: CSV file with recipe data and image references

### Setup

<CodeGroup>
  ```bash bash icon="code" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # 1. Extract the downloaded files to a folder
  # 2. Navigate to the folder in terminal
  cd multimodal-recipe-agent

  # 3. Install dependencies with uv
  uv sync

  # 4. Download the Kaggle dataset
  # Visit: https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images
  # Extract recipes.csv to the data/ folder

  # 5. Import the dataset
  uv run python import.py

  # 6. Run the complete Streamlit chat application
  uv run streamlit run app.py
  ```
</CodeGroup>


# Time-Travel RAG with versioned data
Source: https://docs.lancedb.com/tutorials/agents/time-travel-rag/index

Learn how to build production-ready RAG systems with LanceDB's time-travel capabilities for regulatory compliance and audit trails.

<Tip>
  All the scripts and code for this tutorial are available in the
  [vectorDB recipes](https://github.com/lancedb/vectordb-recipes/tree/main/examples/time-travel-rag) repository.
</Tip>

## Use case: Financial services regulatory knowledge base

Imagine you're a major investment bank. Your team is tasked with building a critical Retrieval-Augmented Generation (RAG) system. This system must provide instant, accurate answers to compliance officers about ever-changing financial regulations. A wrong or out-of-date answer isn't just an inconvenience—it could lead to multi-million dollar fines, reputational damage, and regulatory audits.

Your knowledge base is a living entity, constantly evolving with:

* Daily regulatory updates from government bodies.
* New internal policy documents and interpretations.
* A/B testing of different embedding models and text chunking strategies to improve accuracy.

This dynamic environment creates a series of high-stakes challenges that traditional
vector databases are ill-equipped to handle.

## Pain points solved by LanceDB

1. "Our RAG gave different answers yesterday versus today. Which version was used in the official compliance report?" Without versioning, you can't prove what the AI knew at a specific point in time, making audits impossible.

2. "The new embedding model we deployed corrupted half the vectors. Can we instantly roll back our 10TB dataset?" With traditional systems, a rollback means a painful, hours-long (or days-long) process of re-indexing from a backup, leading to significant downtime.

3. "Regulators want to audit an AI-assisted decision from three months ago. How can we prove what data the model had access to at that exact moment?" Reproducibility is key for compliance. You must be able to reconstruct the exact state of the knowledge base for any historical query.

4. "We need to A/B test a new chunking strategy, but we can't disrupt the production system or duplicate the entire dataset." Experimentation is vital for improvement, but it can't come at the cost of production stability or a massive infrastructure bill.

LanceDB's [zero-cost data evolution](/tables/schema) and [time-travel capabilities](/tables/versioning#time-travel) directly address these critical enterprise pain points, providing the foundation for a reliable, auditable, and production-ready RAG system.

## Dataset: The U.S. Federal Register

To make this use case realistic, we'll use a perfect real-world dataset: The U.S. Federal Register, the official daily journal of the United States Government.

It contains all new rules, proposed rules, and notices from federal agencies. It is the canonical source for regulatory changes, and it's updated every business day. It even has a public API, allowing us to simulate the real-time ingestion of new documents.

An example output of the workflow defined in [main.py](https://github.com/lancedb/blog-lancedb/blob/main/content/docs/tutorials/rag/time-travel-rag/main.py)
is shown below.

```bash main.py expandable theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
--- Initializing Database Environment ---
Removed old database at ./lancedb
Loading embedding model: all-MiniLM-L6-v2...

--- STEP 1: Initial Data Ingestion ---

Fetching 500 documents for publication date: 2024-08-19...
Successfully fetched 86 documents.
Embedding 86 documents...
Batches: 100%|███████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00,  7.12it/s]
Successfully embedded 86 documents.

Creating table 'federal_register'...
✅ Table 'federal_register' created. Version: 1, Rows: 86

--- STEP 2: Simulating Sequential Daily Updates ---

Fetching 500 documents for publication date: 2024-08-20...
Successfully fetched 102 documents.
Embedding 102 documents...
Batches: 100%|███████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 10.66it/s]
Successfully embedded 102 documents.
✅ Data added to 'federal_register'. New Version: 2, Total Rows: 188

Fetching 500 documents for publication date: 2024-08-21...
Successfully fetched 114 documents.
Embedding 114 documents...
Batches: 100%|███████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 10.19it/s]
Successfully embedded 114 documents.
✅ Data added to 'federal_register'. New Version: 3, Total Rows: 302


========================================================
= PART 1: AUDITING KNOWLEDGE BASE ACROSS TIME  =
========================================================

Running audit for query: 'cybersecurity reporting requirements for public companies'

Attempting to open 'federal_register' and checkout version 1...
✅ Successfully checked out Version 1 of 'federal_register'. Total rows: 86
Querying table 'federal_register' (Version 1)...

--- Top Result for Version: V1 (all-MiniLM-L6-v2) ---
📄 Title: Public Company Accounting Oversight Board; Extension of Approval Periods for Proposed Rules on a Firm's System of Quality Control and Related Amendments to PCAOB Standards, Proposed Rules on Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form, and Proposed Rules on Amendment to PCAOB Rule 3502 Governing Contributory Liability
🗓️  Date: 2024-08-19
📏 Distance: 1.1667
📝 Abstract:
[No abstract available for this document]
--------------------------------------

Attempting to open 'federal_register' and checkout version 2...
✅ Successfully checked out Version 2 of 'federal_register'. Total rows: 188
Querying table 'federal_register' (Version 2)...

--- Top Result for Version: V2 (all-MiniLM-L6-v2) ---
📄 Title: Information Collection Being Reviewed by the Federal Communications Commission Under Delegated Authority
🗓️  Date: 2024-08-20
📏 Distance: 1.1436
📝 Abstract:
As part of its continuing effort to reduce paperwork burdens, and as required by the Paperwork
Reduction Act (PRA) of 1995, the Federal Communications Commission (FCC or the Commission) invites
the general public and other Federal agencies to take this opportunity to comment on the following
information collection. Comments are requested concerning: whether the proposed collection of
information is necessary for the proper performance of the functions of the Commission, including
whether the information shall have practical utility; the accuracy of the Commission's burden
estimate; ways to enhance the quality, utility, and clarity of the information collected; ways to
minimize the burden of the collection of information on the respondents, including the use of
automated collection techniques or other forms of information technology; and ways to further reduce
the information collection burden on small business concerns with fewer than 25 employees. The FCC
may not conduct or sponsor a collection of information unless it displays a currently valid control
number. No person shall be subject to any penalty for failing to comply with a collection of
information subject to the PRA that does not display a valid Office of Management and Budget (OMB)
control number.
--------------------------------------

Attempting to open 'federal_register' and checkout version 3...
✅ Successfully checked out Version 3 of 'federal_register'. Total rows: 302
Querying table 'federal_register' (Version 3)...

--- Top Result for Version: V3 (all-MiniLM-L6-v2) ---
📄 Title: Equipment, Systems, and Network Information Security Protection
🗓️  Date: 2024-08-21
📏 Distance: 1.0942
📝 Abstract:
This proposed rulemaking would impose new design standards to address cybersecurity threats for
transport category airplanes, engines, and propellers. The intended effect of this proposed action
is to standardize the FAA's criteria for addressing cybersecurity threats, reducing certification
costs and time while maintaining the same level of safety provided by current special conditions.
--------------------------------------

✅ Date-based audit complete. Results show how knowledge evolves over time. This demonstrates LanceDB's powerful [versioning capabilities](/tutorials/tables/consistency#versioning) for maintaining audit trails.


=============================================================
= PART 2: A/B TESTING DIFFERENT EMBEDDING MODELS  =
=============================================================
Loading embedding model: all-mpnet-base-v2...
Embedding 302 documents...
Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  2.55it/s]
Successfully embedded 302 documents.

Creating table 'federal_register_experimental'...
✅ Table 'federal_register_experimental' created. Version: 1, Rows: 302

Comparing search results for the same data with different models:
Querying table 'federal_register' (Version 3)...

--- Top Result for Version: Latest Prod V3 (all-MiniLM-L6-v2) ---
📄 Title: Equipment, Systems, and Network Information Security Protection
🗓️  Date: 2024-08-21
📏 Distance: 1.0942
📝 Abstract:
This proposed rulemaking would impose new design standards to address cybersecurity threats for
transport category airplanes, engines, and propellers. The intended effect of this proposed action
is to standardize the FAA's criteria for addressing cybersecurity threats, reducing certification
costs and time while maintaining the same level of safety provided by current special conditions.
--------------------------------------
Querying table 'federal_register_experimental' (Version 1)...

--- Top Result for Version: Experimental (all-mpnet-base-v2) ---
📄 Title: Commission Information Collection Activities (FERC-725B); Comment Request; Extension
🗓️  Date: 2024-08-20
📏 Distance: 1.0827
📝 Abstract:
In compliance with the requirements of the Paperwork Reduction Act of 1995, the Federal Energy
Regulatory Commission (Commission or FERC) is soliciting public comment on the currently approved
information collection, FERC-725B, Mandatory Reliability Standards, Critical Infrastructure
Protection (CIP) (Update for CIP-012-1 to version CIP-012-02) Cyber Security--Communications between
Control Centers. The 60-day notice comment period ended on July 23, 2024, with no comments received.
--------------------------------------

✅ A/B test complete. Notice the difference in relevance (distance score) between models. This showcases how LanceDB enables [experimentation with different embedding models](/docs/embeddings/) without disrupting production systems.
```


# Feature Engineering
Source: https://docs.lancedb.com/tutorials/feature-engineering/index

Learn how to build features for your data in LanceDB.

| Example                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Feature Engineering 101** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/tutorials/feature-engineering/feature-engineering-101.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/tutorials/feature-engineering/feature-engineering-101.ipynb) | This example demonstrates how to use LanceDB's feature engineering platform to add new derived features. |
| **Materialized Views** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/tutorials/feature-engineering/materialized-views.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/tutorials/feature-engineering/materialized-views.ipynb)                | This example shows how to create materialized views: query results persisted as physical tables.         |

## Read the docs

The relevant section of the documentation are listed below.

| Feature                                               | Description                                                    |
| :---------------------------------------------------- | :------------------------------------------------------------- |
| [Feature Engineering](/geneva/)                       | Learn the fundamentals of feature engineering.                 |
| [Materialized Views](/geneva/jobs/materialized-views) | Learn more about creating materialized views.                  |
| [Contexts](/geneva/jobs/contexts)                     | Learn how to run your job on a Ray cluster for production use. |


# Tutorials
Source: https://docs.lancedb.com/tutorials/index

Step-by-step tutorials for building applications with LanceDB

Explore tutorials organized by use case:

| Tutorial                                          | Description                                                                                   |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| [Search & advanced retrieval](/tutorials/search/) | Learn how to perform vector search and use advanced retrieval techniques.                     |
| [Agents](/tutorials/agents/)                      | Build Retrieval-Augmented Generation (RAG) applications and agents with LanceDB.              |
| [Working with tables in LanceDB](/tables/)        | Learn the basics of working with tables in LanceDB: creation, ingestion and schema evolution. |

## Recipes

If you're looking for ideas and hands-on code examples, we've worked on a collection of practical
projects in the repository linked below.

<Card icon="code" title="VectorDB recipes" href="https://github.com/lancedb/vectordb-recipes">
  Check out past code examples and tutorials [here](https://github.com/lancedb/vectordb-recipes)
  on GitHub.
</Card>


# Search Tutorials
Source: https://docs.lancedb.com/tutorials/search/index

Learn how vector, full-text and hybrid search work in LanceDB.

The table below shows examples of applications built with LanceDB for search use cases.

| Example                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hybrid search & reranking on BEIR** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/Inbuilt-Hybrid-Search/Inbuilt_Hybrid_Search_with_LanceDB.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/Inbuilt-Hybrid-Search)             | This example demonstrates how to use LanceDB's built-in hybrid search feature, which combines the strengths of both semantic and full-text search. By using the BEIR dataset, it shows how to achieve more relevant results by searching for both the meaning of a query and the specific keywords it contains.                                       |
| **Semantic search across videos** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/v-jepa-video-search/intra-video.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/v-jepa-video-search)                                            | Learn how to build a video search application using V-JEPA (Video Joint Embedding Predictive Architecture) and LanceDB. This example shows how to generate vector embeddings for videos and then use LanceDB to perform similarity searches, allowing you to find videos that are visually similar to a given query.                                  |
| **Semantic result merging** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/Vector-Arithmetic-with-LanceDB/main.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/Vector-Arithmetic-with-LanceDB)                                   | Explore the concept of vector arithmetic with LanceDB. This notebook demonstrates how you can manipulate vector embeddings to capture more complex relationships in your data. For instance, you can modify a search query by adding or subtracting vector representations of different concepts, enabling more nuanced and powerful semantic search. |
| **Reddit concept summarizer** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/Reddit-summarization-and-search/subreddit_summarization_querying.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/Reddit-summarization-and-search)   | This project showcases a complete pipeline for acquiring text data from Reddit, transforming it into meaningful vector representations using embeddings, and then storing and managing those vectors in LanceDB. It demonstrates how to build applications on top of this data, such as summarization and powerful semantic search.                   |
| **NER-powered vector search** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/tutorials/NER-powered-Semantic-Search/NER_powered_Semantic_Search_with_LanceDB.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/tutorials/NER-powered-Semantic-Search) | This example demonstrates how to use Named Entity Recognition (NER) to power vector search. By extracting entities (like people, places, and organizations) from text and creating vector embeddings of them, you can significantly improve the accuracy of your search results.                                                                      |
| **Multivector search with XTR** <br /> <a href="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/multivector_xtr/main.ipynb"><img alt="Open In Colab" /></a> [View on GitHub](https://github.com/lancedb/vectordb-recipes/tree/main/examples/multivector_xtr)                                                             | This notebook dives into LanceDB's advanced multivector search capabilities, enhanced by the XTR (ConteXtualized Token Retriever) technique. It shows how to represent complex data with multiple vectors for more nuanced meaning and how XTR speeds up retrieval by prioritizing the most important tokens.                                         |

## Read the docs

The relevant section of the documentation are listed below.

| Feature                                            | Description                                                                                                                                      |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| [Vector search](/search/vector-search/)            | Learn the fundamentals of vector search, including how to perform similarity searches, use different distance metrics, and optimize performance. |
| [Hybrid search](/search/hybrid-search/)            | Combine keyword-based search with vector search to improve retrieval accuracy and relevance.                                                     |
| [Full-text search](/search/full-text-search/)      | Perform full-text search on your text data, and combine it with vector search for a powerful hybrid search experience.                           |
| [Reranking](/reranking/)                           | Refine your search results using reranking models to improve the relevance of the top-k results.                                                 |
| [Multi-vector search](/search/multivector-search/) | Use multiple vector embeddings per document to perform more nuanced and accurate searches.                                                       |


