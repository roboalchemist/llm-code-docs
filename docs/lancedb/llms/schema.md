# Source: https://docs.lancedb.com/tables/schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Schema and Data Evolution

> Learn how to manage table schemas in LanceDB, including adding, altering, and dropping columns.

export const AlterVectorColumn = "vector_dim = 768  # Your embedding dimension\ntable_name = \"vector_alter_example\"\ndb = tmp_db\ndata = [\n    {\n        \"id\": 1,\n        \"embedding\": np.random.random(vector_dim).tolist(),\n    },\n]\ntable = db.create_table(table_name, data, mode=\"overwrite\")\n\ntable.alter_columns(\n    dict(path=\"embedding\", data_type=pa.list_(pa.float32(), vector_dim))\n)\n";

export const DropColumnsMultiple = "# Remove the second temporary column\ntable.drop_columns([\"temp_col2\"])\n";

export const DropColumnsSingle = "# Remove the first temporary column\ntable.drop_columns([\"temp_col1\"])\n";

export const AlterColumnsMultiple = "# Rename, change type, and make nullable in one operation\ntable.alter_columns(\n    {\n        \"path\": \"sale_price\",\n        \"rename\": \"final_price\",\n        \"data_type\": pa.float64(),\n        \"nullable\": True,\n    }\n)\n";

export const AlterColumnsNullable = "# Make the name column nullable\ntable.alter_columns({\"path\": \"name\", \"nullable\": True})\n";

export const AlterColumnsDataType = "# Change price from int32 to int64 for larger numbers\ntable.alter_columns({\"path\": \"price\", \"data_type\": pa.int64()})\n";

export const AlterColumnsRename = "# Rename discount_price to sale_price\ntable.alter_columns({\"path\": \"discount_price\", \"rename\": \"sale_price\"})\n";

export const SchemaAlterSetup = "table_name = \"schema_evolution_alter_example\"\nif data is None:\n    data = [\n        {\n            \"id\": 1,\n            \"name\": \"Laptop\",\n            \"price\": 1200,\n            \"discount_price\": 1080.0,\n            \"vector\": np.random.random(128).tolist(),\n        },\n        {\n            \"id\": 2,\n            \"name\": \"Smartphone\",\n            \"price\": 800,\n            \"discount_price\": 720.0,\n            \"vector\": np.random.random(128).tolist(),\n        },\n    ]\nschema = pa.schema(\n    {\n        \"id\": pa.int64(),\n        \"name\": pa.string(),\n        \"price\": pa.int32(),\n        \"discount_price\": pa.float64(),\n        \"vector\": pa.list_(pa.float32(), 128),\n    }\n)\ntable = tmp_db.create_table(table_name, data, schema=schema, mode=\"overwrite\")\n";

export const AddColumnsNullable = "# Add a nullable timestamp column\ntable.add_columns({\"last_ordered\": \"cast(NULL as timestamp)\"})\n";

export const AddColumnsDefaultValues = "# Add a stock status column with default value\ntable.add_columns({\"in_stock\": \"cast(true as boolean)\"})\n";

export const AddColumnsCalculated = "# Add a discounted price column (10% discount)\ntable.add_columns({\"discounted_price\": \"cast((price * 0.9) as float)\"})\n";

export const SchemaAddSetup = "table_name = \"schema_evolution_add_example\"\nif data is None:\n    data = [\n        {\n            \"id\": 1,\n            \"name\": \"Laptop\",\n            \"price\": 1200.00,\n            \"vector\": np.random.random(128).tolist(),\n        },\n        {\n            \"id\": 2,\n            \"name\": \"Smartphone\",\n            \"price\": 800.00,\n            \"vector\": np.random.random(128).tolist(),\n        },\n        {\n            \"id\": 3,\n            \"name\": \"Headphones\",\n            \"price\": 150.00,\n            \"vector\": np.random.random(128).tolist(),\n        },\n    ]\ntable = tmp_db.create_table(table_name, data, mode=\"overwrite\")\n";

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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {SchemaAddSetup}
  </CodeBlock>
</CodeGroup>

### Adding Calculated Columns

You can add new columns that are calculated from existing data using SQL expressions:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AddColumnsCalculated}
  </CodeBlock>
</CodeGroup>

### Adding Columns with Default Values

Add boolean columns with default values for status tracking:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AddColumnsDefaultValues}
  </CodeBlock>
</CodeGroup>

### Adding Nullable Columns

Add timestamp columns that can contain NULL values:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AddColumnsNullable}
  </CodeBlock>
</CodeGroup>

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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {SchemaAlterSetup}
  </CodeBlock>
</CodeGroup>

### Renaming Columns

Change column names to better reflect their purpose:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AlterColumnsRename}
  </CodeBlock>
</CodeGroup>

### Changing Data Types

Convert column data types for better performance or compatibility:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AlterColumnsDataType}
  </CodeBlock>
</CodeGroup>

### Making Columns Nullable

Allow columns to contain NULL values:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AlterColumnsNullable}
  </CodeBlock>
</CodeGroup>

### Multiple Changes at Once

Apply several alterations in a single operation:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AlterColumnsMultiple}
  </CodeBlock>
</CodeGroup>

<Warning title="Data Type Changes">
  Changing data types requires rewriting the column data and may be resource-intensive for large tables. Renaming columns or changing nullability is more efficient as it only updates metadata.
</Warning>

## Dropping Columns

You can remove columns using the [`drop_columns`](https://lancedb.github.io/lancedb/python/python/#lancedb.table.Table.drop_columns)
method in Python or [`dropColumns`](https://lancedb.github.io/lancedb/js/classes/Table/#dropcolumns) in TypeScript/JavaScript.

### Setting Up the Example Table

Create a table with temporary columns that we'll remove:

```python  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {DropColumnsSingle}
  </CodeBlock>
</CodeGroup>

### Dropping Multiple Columns

Remove several columns at once for efficiency:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {DropColumnsMultiple}
  </CodeBlock>
</CodeGroup>

<Warning title="Irreversible Column Deletion">
  Dropping columns cannot be undone. Make sure you have backups or are certain before removing columns.
</Warning>

## Vector Column Considerations

Vector columns (used for embeddings) have special considerations. When altering vector columns, you should ensure consistent dimensionality.

### Converting List to FixedSizeList

A common schema evolution task is converting a generic list column to a fixed-size list for performance:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {AlterVectorColumn}
  </CodeBlock>
</CodeGroup>
