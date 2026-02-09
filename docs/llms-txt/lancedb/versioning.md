# Source: https://docs.lancedb.com/tables/versioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Versioning and Reproducibility

> Learn how to implement versioning and ensure reproducibility in LanceDB. Includes version control, data snapshots, and audit trails.

export const VersioningDeleteData = "# Let's delete data from the table\ntable.delete(\"author != 'Richard Daniel Sanchez'\")\nrows_after_deletion = table.count_rows()\nprint(f\"Number of rows after deletion: {rows_after_deletion}\")\n";

export const VersioningCheckoutLatest = "# Go back to the latest version\ntable.checkout_latest()\n";

export const VersioningRollback = "# Let's roll back to before we added the vector column\n# We'll use the version after modifications but before adding embeddings\ntable.restore(version_after_mod)\n\n# Notice we have one more version now, not less!\nversions = table.list_versions()\nversion_count_after_rollback = len(versions)\nprint(f\"Total number of versions after rollback: {version_count_after_rollback}\")\n";

export const VersioningListAllVersions = "# Let's see all versions\nversions = table.list_versions()\nfor v in versions:\n    print(f\"Version {v['version']}, created at {v['timestamp']}\")\n";

export const VersioningCheckVersionsAfterMod = "# Check versions after modifications\nversions = table.list_versions()\nversion_count_after_mod = len(versions)\nversion_after_mod = table.version\nprint(f\"Number of versions after modifications: {version_count_after_mod}\")\nprint(f\"Current version: {version_after_mod}\")\n";

export const VersioningAddData = "# Add more data\nmore_data = [\n    {\n        \"id\": 4,\n        \"author\": \"Richard Daniel Sanchez\",\n        \"quote\": \"That's the way the news goes!\",\n    },\n    {\"id\": 5, \"author\": \"Morty\", \"quote\": \"Aww geez, Rick!\"},\n]\ntable.add(more_data)\n";

export const VersioningUpdateData = "# Update author names to be more specific\ntable.update(where=\"author='Richard'\", values={\"author\": \"Richard Daniel Sanchez\"})\nrows_after_update = table.count_rows()\nprint(f\"Number of rows after update: {rows_after_update}\")\n";

export const VersioningCheckInitialVersion = "# View the initial version\nversions = table.list_versions()\nprint(f\"Number of versions after creation: {len(versions)}\")\nprint(f\"Current version: {table.version}\")\n";

export const VersioningBasicSetup = "import lancedb\nimport numpy as np\nimport pandas as pd\nimport pyarrow as pa\n\n# Connect to LanceDB\ndb = tmp_db\n\n# Create a table with initial data\ntable_name = \"quotes_versioning_example\"\ndata = [\n    {\"id\": 1, \"author\": \"Richard\", \"quote\": \"Wubba Lubba Dub Dub!\"},\n    {\"id\": 2, \"author\": \"Morty\", \"quote\": \"Rick, what's going on?\"},\n    {\n        \"id\": 3,\n        \"author\": \"Richard\",\n        \"quote\": \"I turned myself into a pickle, Morty!\",\n    },\n]\n\n# Define schema\nschema = pa.schema(\n    [\n        pa.field(\"id\", pa.int64()),\n        pa.field(\"author\", pa.string()),\n        pa.field(\"quote\", pa.string()),\n    ]\n)\n\ntable = db.create_table(table_name, data, schema=schema, mode=\"overwrite\")\n";

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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningBasicSetup}
  </CodeBlock>
</CodeGroup>

### Checking Initial Version

After creating the table, let's check the initial version information:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningCheckInitialVersion}
  </CodeBlock>
</CodeGroup>

## Modifying Data

When you modify data through operations like update or delete, LanceDB automatically creates new versions.

### Updating Existing Data

Let's update some existing records to see versioning in action:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningUpdateData}
  </CodeBlock>
</CodeGroup>

### Adding New Data

Now let's add more records to the table:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningAddData}
  </CodeBlock>
</CodeGroup>

### Checking Version Changes

Let's see how the versions have changed after our modifications:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningCheckVersionsAfterMod}
  </CodeBlock>
</CodeGroup>

## Tracking Changes in Schema

LanceDB's versioning system automatically tracks every schema modification. This is critical when handling evolving embedding models. For example, adding a new `vector_minilm` column creates a fresh version, enabling seamless A/B testing between embedding generations without recreating the table.

### Preparing Data for Embeddings

First, let's get the data we want to embed:

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
import pyarrow as pa

# Get data from table
df = table.search().limit(5).to_pandas()
```

### Generating Embeddings

Now let's generate embeddings using the all-MiniLM-L6-v2 model:

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningListAllVersions}
  </CodeBlock>
</CodeGroup>

### Rolling Back to a Previous Version

Now let's roll back to before we added the vector column:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningRollback}
  </CodeBlock>
</CodeGroup>

## Making Changes from Previous Versions

After restoring a table to an earlier version, you can continue making modifications. In this example, we rolled back to a version before adding embeddings. This allows us to experiment with different embedding models and compare their performance.

### Switching to a Different Embedding Model

Let's try a different embedding model (all-mpnet-base-v2) to see how it performs:

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningCheckoutLatest}
  </CodeBlock>
</CodeGroup>

### Deleting Data

Now let's delete some data to see how it affects versioning:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {VersioningDeleteData}
  </CodeBlock>
</CodeGroup>

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
