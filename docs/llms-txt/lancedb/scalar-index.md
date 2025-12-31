# Source: https://docs.lancedb.com/indexing/scalar-index.md

# Scalar Indexes

> Learn how to use scalar indexes in LanceDB for efficient metadata filtering and query optimization.

export const ScalarIndexUuidUpsert = "new_users = [\n    {\"id\": uuid.uuid4().bytes, \"name\": \"Hannah D.\"},\n    {\"id\": uuid.uuid4().bytes, \"name\": \"Ian B.\"},\n]\n# Insert or update using the UUID index\ntable.merge_insert(\n    \"id\"\n).when_matched_update_all().when_not_matched_insert_all().execute(new_users)\n";

export const ScalarIndexUuidWait = "index_name = \"id_idx\"\ntable.create_scalar_index(\"id\")\ntable.wait_for_index([index_name])\n";

export const ScalarIndexUuidTable = "table_name = \"index-on-uuid\"\n\nuuid_array = pa.array(uuids, pa.uuid())\nname_array = pa.array(names, pa.string())\nschema = pa.schema(\n    [\n        pa.field(\"id\", pa.uuid()),\n        pa.field(\"name\", pa.string()),\n    ]\n)\ndata_table = pa.Table.from_arrays([uuid_array, name_array], schema=schema)\ntable = db.create_table(table_name, data=data_table, mode=\"overwrite\")\n";

export const ScalarIndexUuidData = "def generate_random_names():\n    base_names = [\"Alice\", \"Bob\", \"Carla\", \"David\", \"Eve\", \"Frank\", \"Grace\"]\n    letter = random.choice(string.ascii_uppercase)\n    return f\"{random.choice(base_names)} {letter}.\"\n\ndef generate_uuids(num_items):\n    return [uuid.uuid4().bytes for _ in range(num_items)]\n\n# Generate some UUIDs and random names\nn = 7\nuuids = generate_uuids(n)\nnames = [generate_random_names() for _ in range(n)]\n";

export const ScalarIndexUuidType = "import pyarrow as pa\n";

export const ScalarIndexPrefilter = "table = db.open_table(\"book_with_embeddings\")\ntable.search([1.2] * 2).where(\"book_id != 3\").limit(10).to_pandas()\n";

export const ScalarIndexFilter = "table = db.open_table(\"books\")\nresult = table.search().where(\"book_id = 2\").limit(10).to_pandas()\n";

export const ScalarIndexOptimize = "table.add([{\"vector\": [7, 8], \"book_id\": 4}])\ntable.optimize()\n";

export const ScalarIndexWait = "index_name = \"label_idx\"\ntable.wait_for_index([index_name])\n";

export const ScalarIndexBuild = "tbl = db.open_table(\"scalar_index_build\")\ntbl.create_scalar_index(\"book_id\")\ntbl.create_scalar_index(\"publisher\", index_type=\"BITMAP\")\n";

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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexBuild}
  </CodeBlock>
</CodeGroup>

<Note title="LanceDB Cloud and Enterprise">
  If you are using Cloud or Enterprise, the `create_scalar_index` API returns immediately, but the building of the scalar index is asynchronous. To wait until all data is fully indexed, you can specify the `wait_timeout` parameter on `create_scalar_index()` or call `wait_for_index()` on the table.
</Note>

### 2. Check Index Status

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexWait}
  </CodeBlock>
</CodeGroup>

### 3. Update the Index

Updating the table data (adding, deleting, or modifying records) requires that you also update the scalar index. This can be done by calling `optimize`, which will trigger an update to the existing scalar index.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexOptimize}
  </CodeBlock>
</CodeGroup>

<Note title="LanceDB Cloud">
  New data added after creating the scalar index will still appear in search results if optimize is not used, but with increased latency due to a flat search on the unindexed portion. LanceDB Cloud automates the optimize process, minimizing the impact on search speed.
</Note>

### 4. Run Indexed Searches

The following scan will be faster if the column `book_id` has a scalar index:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexFilter}
  </CodeBlock>
</CodeGroup>

Scalar indexes can also speed up scans containing a vector search or full text search, and a prefilter:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexPrefilter}
  </CodeBlock>
</CodeGroup>

## Index UUID Columns

LanceDB supports scalar indexes on UUID columns (stored as `FixedSizeBinary(16)`), enabling efficient lookups and filtering on UUID-based primary keys.

<Note>
  **To use `FixedSizeBinary`, ensure you have:**

  * Python SDK version `0.22.0` or later
  * TypeScript SDK version `0.19.0` or later
</Note>

### 1. Define UUID Type

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexUuidType}
  </CodeBlock>
</CodeGroup>

### 2. Generate UUID Data

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexUuidData}
  </CodeBlock>
</CodeGroup>

### 3. Create Table with UUID Column

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexUuidTable}
  </CodeBlock>
</CodeGroup>

### 4. Create and Wait for the Index

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexUuidWait}
  </CodeBlock>
</CodeGroup>

### 5. Perform Operations with the UUID Index

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ScalarIndexUuidUpsert}
  </CodeBlock>
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt