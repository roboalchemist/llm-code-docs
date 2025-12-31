# Source: https://docs.lancedb.com/tables/create.md

# Ingesting Data

> Learn about different methods to ingest data into tables in LanceDB, including from various data sources and empty tables.

export const TablesTzValidator = "from datetime import datetime\nfrom zoneinfo import ZoneInfo\n\nfrom lancedb.pydantic import LanceModel\nfrom pydantic import Field, ValidationError, ValidationInfo, field_validator\n\ntzname = \"America/New_York\"\ntz = ZoneInfo(tzname)\n\nclass TestModel(LanceModel):\n    dt_with_tz: datetime = Field(json_schema_extra={\"tz\": tzname})\n\n    @field_validator(\"dt_with_tz\")\n    @classmethod\n    def tz_must_match(cls, dt: datetime) -> datetime:\n        assert dt.tzinfo == tz\n        return dt\n\nok = TestModel(dt_with_tz=datetime.now(tz))\n\ntry:\n    TestModel(dt_with_tz=datetime.now(ZoneInfo(\"Asia/Shanghai\")))\n    assert 0 == 1, \"this should raise ValidationError\"\nexcept ValidationError:\n    print(\"A ValidationError was raised.\")\n    pass\n";

export const TablesDocumentModel = "from pydantic import BaseModel\n\nclass Document(BaseModel):\n    content: str\n    source: str\n";

export const TablesBasicConnect = "import lancedb\n\nuri = \"data/sample-lancedb\"\ndb = lancedb.connect(uri)\n";

export const DropTable = "db = tmp_db\n# Create a table first\ndata = [{\"vector\": [1.1, 1.2], \"lat\": 45.5}]\ndb.create_table(\"my_table\", data, mode=\"overwrite\")\n\n# Drop the table\ndb.drop_table(\"my_table\")\n";

export const CreateEmptyTablePydantic = "import lancedb\nfrom lancedb.pydantic import LanceModel, Vector\n\nclass Item(LanceModel):\n    vector: Vector(2)\n    item: str\n    price: float\n\ndb = tmp_db\ntbl = db.create_table(\n    \"test_empty_table_new\", schema=Item.to_arrow_schema(), mode=\"overwrite\"\n)\n";

export const CreateEmptyTable = "import lancedb\nimport pyarrow as pa\n\nschema = pa.schema(\n    [\n        pa.field(\"vector\", pa.list_(pa.float32(), 2)),\n        pa.field(\"item\", pa.string()),\n        pa.field(\"price\", pa.float32()),\n    ]\n)\ndb = tmp_db\ntbl = db.create_table(\"test_empty_table\", schema=schema, mode=\"overwrite\")\n";

export const OpenExistingTable = "db = tmp_db\n# Create a table first\ndata = [{\"vector\": [1.1, 1.2], \"lat\": 45.5, \"long\": -122.7}]\ndb.create_table(\"test_table\", data, mode=\"overwrite\")\n\n# List table names\nprint(db.table_names())\n\n# Open existing table\ntbl = db.open_table(\"test_table\")\n";

export const CreateTableFromIterator = "import pyarrow as pa\n\ndef make_batches():\n    for i in range(5):\n        yield pa.RecordBatch.from_arrays(\n            [\n                pa.array(\n                    [[3.1, 4.1, 5.1, 6.1], [5.9, 26.5, 4.7, 32.8]],\n                    pa.list_(pa.float32(), 4),\n                ),\n                pa.array([\"foo\", \"bar\"]),\n                pa.array([10.0, 20.0]),\n            ],\n            [\"vector\", \"item\", \"price\"],\n        )\n\nschema = pa.schema(\n    [\n        pa.field(\"vector\", pa.list_(pa.float32(), 4)),\n        pa.field(\"item\", pa.utf8()),\n        pa.field(\"price\", pa.float32()),\n    ]\n)\ndb = tmp_db\ndb.create_table(\"batched_tale\", make_batches(), schema=schema, mode=\"overwrite\")\n";

export const CreateTableNestedSchema = "from lancedb.pydantic import LanceModel, Vector\n\n# --8<-- [start:tables_document_model]\nfrom pydantic import BaseModel\n\nclass Document(BaseModel):\n    content: str\n    source: str\n\n# --8<-- [end:tables_document_model]\n\nclass NestedSchema(LanceModel):\n    id: str\n    vector: Vector(1536)\n    document: Document\n\ndb = tmp_db\ntbl = db.create_table(\"nested_table\", schema=NestedSchema, mode=\"overwrite\")\n";

export const CreateTableFromPydantic = "from lancedb.pydantic import LanceModel, Vector\n\nclass Content(LanceModel):\n    movie_id: int\n    vector: Vector(128)\n    genres: str\n    title: str\n    imdb_id: int\n\n    @property\n    def imdb_url(self) -> str:\n        return f\"https://www.imdb.com/title/tt{self.imdb_id}\"\n\ndb = tmp_db\ntbl = db.create_table(\"movielens_small\", schema=Content, mode=\"overwrite\")\n";

export const CreateTableFromArrow = "import numpy as np\nimport pyarrow as pa\n\ndim = 16\ntotal = 2\nschema = pa.schema(\n    [pa.field(\"vector\", pa.list_(pa.float16(), dim)), pa.field(\"text\", pa.string())]\n)\ndata = pa.Table.from_arrays(\n    [\n        pa.array(\n            [np.random.randn(dim).astype(np.float16) for _ in range(total)],\n            pa.list_(pa.float16(), dim),\n        ),\n        pa.array([\"foo\", \"bar\"]),\n    ],\n    [\"vector\", \"text\"],\n)\ndb = tmp_db\ntbl = db.create_table(\"f16_tbl\", data, schema=schema, mode=\"overwrite\")\n";

export const CreateTableFromPolars = "import polars as pl\n\ndata = pl.DataFrame(\n    {\n        \"vector\": [[3.1, 4.1], [5.9, 26.5]],\n        \"item\": [\"foo\", \"bar\"],\n        \"price\": [10.0, 20.0],\n    }\n)\ndb = tmp_db\ntbl = db.create_table(\"my_table_pl\", data, mode=\"overwrite\")\n";

export const CreateTableCustomSchema = "import pyarrow as pa\n\ncustom_schema = pa.schema(\n    [\n        pa.field(\"vector\", pa.list_(pa.float32(), 4)),\n        pa.field(\"lat\", pa.float32()),\n        pa.field(\"long\", pa.float32()),\n    ]\n)\n\ndata = [\n    {\"vector\": [1.1, 1.2, 1.3, 1.4], \"lat\": 45.5, \"long\": -122.7},\n    {\"vector\": [0.2, 1.8, 0.4, 3.6], \"lat\": 40.1, \"long\": -74.1},\n]\ndb = tmp_db\ntbl = db.create_table(\n    \"my_table_custom_schema\", data, schema=custom_schema, mode=\"overwrite\"\n)\n";

export const CreateTableFromPandas = "import pandas as pd\n\ndata = pd.DataFrame(\n    {\n        \"vector\": [[1.1, 1.2, 1.3, 1.4], [0.2, 1.8, 0.4, 3.6]],\n        \"lat\": [45.5, 40.1],\n        \"long\": [-122.7, -74.1],\n    }\n)\ndb = tmp_db\ndb.create_table(\"my_table_pandas\", data, mode=\"overwrite\")\ndb[\"my_table_pandas\"].head()\n";

export const CreateTableFromDicts = "data = [\n    {\"vector\": [1.1, 1.2], \"lat\": 45.5, \"long\": -122.7},\n    {\"vector\": [0.2, 1.8], \"lat\": 40.1, \"long\": -74.1},\n]\ndb = tmp_db\ndb.create_table(\"test_table\", data, mode=\"overwrite\")\ntbl = db[\"test_table\"]\ntbl.head()\n";

In LanceDB, tables store records with a defined schema that specifies column names and types. You can create LanceDB tables from these data formats:

* Pandas DataFrames
* [Polars](https://pola.rs/) DataFrames
* Apache Arrow Tables

The Python SDK additionally supports:

* PyArrow schemas for explicit schema control
* `LanceModel` for Pydantic-based validation

## Create a LanceDB Table

Initialize a LanceDB connection and create a table

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {TablesBasicConnect}
  </CodeBlock>
</CodeGroup>

LanceDB allows ingesting data from various sources - `dict`, `list[dict]`, `pd.DataFrame`, `pa.Table` or a `Iterator[pa.RecordBatch]`. Let's take a look at some of the these.

### From list of tuples or dictionaries

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableFromDicts}
  </CodeBlock>
</CodeGroup>

### From a Pandas DataFrame

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableFromPandas}
  </CodeBlock>
</CodeGroup>

<Note title="Note">
  Data is converted to Arrow before being written to disk. For maximum control over how data is saved, either provide the PyArrow schema to convert to or else provide a PyArrow Table directly.
</Note>

<Note title="Vector Column Type">
  The **`vector`** column needs to be a [Vector](/integrations/data/pydantic#vector-field) (defined as [pyarrow.FixedSizeList](https://arrow.apache.org/docs/python/generated/pyarrow.list_.html)) type.
</Note>

#### From a custom schema

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableCustomSchema}
  </CodeBlock>
</CodeGroup>

### From a Polars DataFrame

LanceDB supports [Polars](https://pola.rs/), a modern, fast DataFrame library
written in Rust. Just like in Pandas, the Polars integration is enabled by PyArrow
under the hood. A deeper integration between LanceDB Tables and Polars DataFrames
is on the way.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableFromPolars}
  </CodeBlock>
</CodeGroup>

### From an Arrow Table

You can also create LanceDB tables directly from Arrow tables.
LanceDB supports float16 data type!

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableFromArrow}
  </CodeBlock>
</CodeGroup>

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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableFromPydantic}
  </CodeBlock>
</CodeGroup>

#### Nested schemas

Sometimes your data model may contain nested objects. For example, you may want to store the document string and the document source name as a nested Document object:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {TablesDocumentModel}
  </CodeBlock>
</CodeGroup>

This can be used as the type of a LanceDB table column:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableNestedSchema}
  </CodeBlock>
</CodeGroup>

This creates a struct column called "document" that has two subfields
called "content" and "source":

```bash  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
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

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {TablesTzValidator}
  </CodeBlock>
</CodeGroup>

When you run this code it, should raise the `ValidationError`.

### Using Iterators / Writing Large Datasets

It is recommended to use iterators to add large datasets in batches when creating your table in one go. This does not create multiple versions of your dataset unlike manually adding batches using `table.add()`

LanceDB additionally supports PyArrow's `RecordBatch` Iterators or other generators producing supported data types.

Here's an example using using `RecordBatch` iterator for creating tables.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateTableFromIterator}
  </CodeBlock>
</CodeGroup>

You can also use iterators of other types like Pandas DataFrame or Pylists directly in the above example.

## Open existing tables

If you forget the name of your table, you can always get a listing of all table names.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {OpenExistingTable}
  </CodeBlock>
</CodeGroup>

## Creating empty table

You can create an empty table for scenarios where you want to add data to the table later.
An example would be when you want to collect data from a stream/external file and then add it to a table in
batches.

An empty table can be initialized via a PyArrow schema.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateEmptyTable}
  </CodeBlock>
</CodeGroup>

Alternatively, you can also use Pydantic to specify the schema for the empty table. Note that we do not
directly import `pydantic` but instead use `lancedb.pydantic` which is a subclass of `pydantic.BaseModel`
that has been extended to support LanceDB specific types like `Vector`.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateEmptyTablePydantic}
  </CodeBlock>
</CodeGroup>

Once the empty table has been created, you can append to it or modify its contents,
as explained in the [updating and modifying tables](/tables/update) section.

## Drop a table

Use the `drop_table()` method on the database to remove a table.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {DropTable}
  </CodeBlock>
</CodeGroup>

This permanently removes the table and is not recoverable, unlike deleting rows.
By default, if the table does not exist an exception is raised. To suppress this,
you can pass in `ignore_missing=True`.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt