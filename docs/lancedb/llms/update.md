# Source: https://docs.lancedb.com/tables/update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating and Modifying Table Data

> Learn how to update and modify data in LanceDB. Includes incremental updates, batch modifications, and best practices for data maintenance.

export const ReplaceRangeOperation = "# Create example table with document chunks\ntable = db.create_table(\n    \"chunks\",\n    [\n        {\"doc_id\": 0, \"chunk_id\": 0, \"text\": \"Hello\"},\n        {\"doc_id\": 0, \"chunk_id\": 1, \"text\": \"World\"},\n        {\"doc_id\": 1, \"chunk_id\": 0, \"text\": \"Foo\"},\n        {\"doc_id\": 1, \"chunk_id\": 1, \"text\": \"Bar\"},\n        {\"doc_id\": 2, \"chunk_id\": 0, \"text\": \"Baz\"},\n    ],\n    mode=\"overwrite\",\n)\n\n# New data - replacing all chunks for doc_id 1 with just one chunk\nnew_chunks = [\n    {\"doc_id\": 1, \"chunk_id\": 0, \"text\": \"Zoo\"},\n]\n\n# Replace all chunks for doc_id 1\n(\n    table.merge_insert([\"doc_id\"])\n    .when_matched_update_all()\n    .when_not_matched_insert_all()\n    .when_not_matched_by_source_delete(\"doc_id = 1\")\n    .execute(new_chunks)\n)\n\n# Verify count for doc_id = 1 - should be 1\nprint(f\"Chunks for doc_id = 1: {table.count_rows('doc_id = 1')}\")  # 1\n";

export const InsertIfNotExists = "# Create example table\ntable = db.create_table(\n    \"domains\",\n    [\n        {\"domain\": \"google.com\", \"name\": \"Google\"},\n        {\"domain\": \"github.com\", \"name\": \"GitHub\"},\n    ],\n    mode=\"overwrite\",\n)\n\n# Prepare new data - one existing and one new record\nnew_domains = [\n    {\"domain\": \"google.com\", \"name\": \"Google\"},\n    {\"domain\": \"facebook.com\", \"name\": \"Facebook\"},\n]\n\n# Insert only if domain doesn't exist\ntable.merge_insert(\"domain\").when_not_matched_insert_all().execute(new_domains)\n\n# Verify count - should be 3 (original 2 plus 1 new)\nprint(f\"Total domains: {table.count_rows()}\")  # 3\n";

export const UpsertOperation = "# Create example table\nusers_table_name = \"users_example\"\ntable = db.create_table(\n    users_table_name,\n    [\n        {\"id\": 0, \"name\": \"Alice\"},\n        {\"id\": 1, \"name\": \"Bob\"},\n    ],\n    mode=\"overwrite\",\n)\nprint(f\"Created users table with {table.count_rows()} rows\")\n\n# Prepare data for upsert\nnew_users = [\n    {\"id\": 1, \"name\": \"Bobby\"},  # Will update existing record\n    {\"id\": 2, \"name\": \"Charlie\"},  # Will insert new record\n]\n\n# Upsert by id\n(\n    table.merge_insert(\"id\")\n    .when_matched_update_all()\n    .when_not_matched_insert_all()\n    .execute(new_users)\n)\n\n# Verify results - should be 3 records total\nprint(f\"Total users: {table.count_rows()}\")  # 3\n";

export const DeleteOperation = "# delete data\npredicate = \"price = 30.0\"\ntable.delete(predicate)\n";

export const UpdateUsingSql = "import pandas as pd\n\n# Create a table from a pandas DataFrame\ndata = pd.DataFrame({\"x\": [1, 2, 3], \"vector\": [[1, 2], [3, 4], [5, 6]]})\ntbl = db.create_table(\"test_table\", data, mode=\"overwrite\")\n# Update all rows: increment x by 1\ntbl.update(values_sql={\"x\": \"x + 1\"})\nprint(tbl.to_pandas())\n";

export const UpdateOperation = "import pandas as pd\n\n# Create a table from a pandas DataFrame\ndata = pd.DataFrame({\"x\": [1, 2, 3], \"vector\": [[1, 2], [3, 4], [5, 6]]})\ntbl = db.create_table(\"test_table\", data, mode=\"overwrite\")\n# Update the table where x = 2\ntbl.update(where=\"x = 2\", values={\"vector\": [10, 10]})\n# Get the updated table as a pandas DataFrame\ndf = tbl.to_pandas()\nprint(df)\n";

export const BatchDataInsertion = "import pyarrow as pa\n\ndef make_batches():\n    for i in range(5):  # Create 5 batches\n        yield pa.RecordBatch.from_arrays(\n            [\n                pa.array([[3.1, 4.1], [5.9, 26.5]], pa.list_(pa.float32(), 2)),\n                pa.array([f\"item{i*2+1}\", f\"item{i*2+2}\"]),\n                pa.array([float((i * 2 + 1) * 10), float((i * 2 + 2) * 10)]),\n            ],\n            [\"vector\", \"item\", \"price\"],\n        )\n\nschema = pa.schema(\n    [\n        pa.field(\"vector\", pa.list_(pa.float32(), 2)),\n        pa.field(\"item\", pa.utf8()),\n        pa.field(\"price\", pa.float32()),\n    ]\n)\n# Create table with batches\ntable_name = \"batch_ingestion_example\"\ntable = db.create_table(table_name, make_batches(), schema=schema, mode=\"overwrite\")\n";

export const AddDataNestedModel = "from lancedb.pydantic import LanceModel, Vector\nfrom pydantic import BaseModel\n\nclass Document(BaseModel):\n    content: str\n    source: str\n\nclass NestedSchema(LanceModel):\n    id: str\n    vector: Vector(128)\n    document: Document\n\n# Create table with nested schema\ntable_name = \"nested_model_example\"\ntable = db.create_table(table_name, schema=NestedSchema, mode=\"overwrite\")\n";

export const AddDataPydanticModel = "from lancedb.pydantic import LanceModel, Vector\n\n# Define a Pydantic model\nclass Content(LanceModel):\n    movie_id: int\n    vector: Vector(128)\n    genres: str\n    title: str\n    imdb_id: int\n\n    @property\n    def imdb_url(self) -> str:\n        return f\"https://www.imdb.com/title/tt{self.imdb_id}\"\n\n# Create table with Pydantic model schema\ntable_name = \"pydantic_example\"\ntable = db.create_table(table_name, schema=Content, mode=\"overwrite\")\n";

export const AddDataToTable = "import pyarrow as pa\n\n# create an empty table with schema\ndata = [\n    {\"vector\": [3.1, 4.1], \"item\": \"foo\", \"price\": 10.0},\n    {\"vector\": [5.9, 26.5], \"item\": \"bar\", \"price\": 20.0},\n    {\"vector\": [10.2, 100.8], \"item\": \"baz\", \"price\": 30.0},\n    {\"vector\": [1.4, 9.5], \"item\": \"fred\", \"price\": 40.0},\n]\n\nschema = pa.schema(\n    [\n        pa.field(\"vector\", pa.list_(pa.float32(), 2)),\n        pa.field(\"item\", pa.utf8()),\n        pa.field(\"price\", pa.float32()),\n    ]\n)\n\ntable_name = \"basic_ingestion_example\"\ntable = db.create_table(table_name, schema=schema, mode=\"overwrite\")\n# Add data\ntable.add(data)\n";

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

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import lancedb

# Connect to LanceDB Cloud
db = lancedb.connect(
    uri="db://your-project-slug",
    api_key="your-api-key",
    region="us-east-1"
)
```

You can also connect locally using LanceDB OSS:

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import lancedb

# Connect to local LanceDB
db = lancedb.connect("./data")  # Local directory for data storage
```

## Data Insertion

### Adding data to a table

Say you created a LanceDB table by passing in a `schema`.
This is an *empty* table, with no data in it. To add or append data to a table, you can use the `table.add(data)`,
as shown below.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AddDataToTable}
  </CodeBlock>
</CodeGroup>

<Note title="Vector Column Type">
  The vector column needs to be a `pyarrow.FixedSizeList` type.
</Note>

### Using Pydantic Models

Pydantic models provide a more structured way to define your table schema:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AddDataPydanticModel}
  </CodeBlock>
</CodeGroup>

### Using Nested Models

You can use nested Pydantic models to represent complex data structures.
For example, you may want to store the document string and the document source name as a nested Document object:

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
from pydantic import BaseModel

class Document(BaseModel):
    content: str
    source: str
```

This can be used as the type of a LanceDB table column:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AddDataNestedModel}
  </CodeBlock>
</CodeGroup>

This creates a struct column called `document` that has two subfields called `content` and `source`:

```bash  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {BatchDataInsertion}
  </CodeBlock>
</CodeGroup>

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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {UpdateOperation}
  </CodeBlock>
</CodeGroup>

Output:

```json  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
    x  vector
0  1  [1.0, 2.0]
1  3  [5.0, 6.0]
2  2  [10.0, 10.0]
```

### Updating Using SQL

The `values` parameter is used to provide the new values for the columns as literal values. You can also use the `values_sql` / `valuesSql` parameter to provide SQL expressions for the new values. For example, you can use `values_sql="x + 1"` to increment the value of the `x` column by 1.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {UpdateUsingSql}
  </CodeBlock>
</CodeGroup>

Output:

```json  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {DeleteOperation}
  </CodeBlock>
</CodeGroup>

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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {UpsertOperation}
  </CodeBlock>
</CodeGroup>

### Insert-if-not-exists

This will only insert rows that do not have a match in the target table, thus
preventing duplicate rows. To do this with merge insert, enable just
`when_not_matched_insert_all()`.

#### Setting Up the Example Table and Performing Insert-if-not-exists

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {InsertIfNotExists}
  </CodeBlock>
</CodeGroup>

### Replace Range

You can also replace a range of rows in the target table with the input data.
For example, if you have a table of document chunks, where each chunk has both
a `doc_id` and a `chunk_id`, you can replace all chunks for a given `doc_id` with updated chunks.

This can be tricky otherwise because if you try to use `upsert` when the new data has fewer
chunks you will end up with extra chunks. To avoid this, add another clause to delete any chunks
for the document that are not in the new data, with `when_not_matched_by_source_delete`.

#### Setting Up the Example Table and Performing Replace Range

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ReplaceRangeOperation}
  </CodeBlock>
</CodeGroup>

<Tip title="Batch Size Recommendation">
  We suggest the best batch size to be 500k for optimal performance.
</Tip>
