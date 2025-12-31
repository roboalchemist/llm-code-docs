# Source: https://docs.lancedb.com/integrations/data/pydantic.md

# Pydantic

export const PyFrameworksPydanticVectorField = "import pyarrow as pa\nimport pydantic\nfrom lancedb.pydantic import Vector, pydantic_to_schema\n\nclass MyModel(pydantic.BaseModel):\n    id: int\n    url: str\n    embeddings: Vector(768)\n\nschema = pydantic_to_schema(MyModel)\nassert schema == pa.schema(\n    [\n        pa.field(\"id\", pa.int64(), False),\n        pa.field(\"url\", pa.utf8(), False),\n        pa.field(\"embeddings\", pa.list_(pa.float32(), 768)),\n    ]\n)\n";

export const PyFrameworksPydanticTypeConversion = "from typing import List, Optional\n\nimport pyarrow as pa\nimport pydantic\nfrom lancedb.pydantic import Vector, pydantic_to_schema\n\nclass FooModel(pydantic.BaseModel):\n    id: int\n    s: str\n    vec: Vector(1536)  # fixed_size_list<item: float32>[1536]\n    li: List[int]\n\nschema = pydantic_to_schema(FooModel)\nassert schema == pa.schema(\n    [\n        pa.field(\"id\", pa.int64(), False),\n        pa.field(\"s\", pa.utf8(), False),\n        pa.field(\"vec\", pa.list_(pa.float32(), 1536)),\n        pa.field(\"li\", pa.list_(pa.int64()), False),\n    ]\n)\n";

export const PyFrameworksPydanticSetUrl = "db = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"pydantic-docs\"))\n";

export const PyFrameworksPydanticImports = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.pydantic import LanceModel, Vector\n";

export const PyFrameworksPydanticBaseModel = "class LanceDocs(LanceModel):\n    text: str\n    vector: Vector(2)\n";

export const PyFrameworksPydanticBaseExample = "table = db.create_table(\"docs\", schema=LanceDocs, mode=\"overwrite\")\ntable.add(\n    [\n        {\"text\": \"hello world\", \"vector\": [1.0, 0.0]},\n        {\"text\": \"goodbye world\", \"vector\": [0.0, 1.0]},\n    ]\n)\nresults = table.search(\"hello world\").limit(1).to_pydantic(LanceDocs)\nprint(results[0].text)\n";

[Pydantic](https://docs.pydantic.dev/latest/) is a data validation library in Python.
LanceDB integrates with Pydantic for schema inference, data ingestion, and query result casting.
Using `lancedb.pydantic.LanceModel`, users can seamlessly
integrate Pydantic with the rest of the LanceDB APIs.

First, import the necessary LanceDB and Pydantic modules:

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksPydanticImports}
</CodeBlock>

Next, define your Pydantic model by inheriting from `LanceModel` and specifying your fields including a vector field:

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksPydanticBaseModel}
</CodeBlock>

Set the database connection URL:

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksPydanticSetUrl}
</CodeBlock>

Now you can create a table, add data, and perform vector search operations:

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksPydanticBaseExample}
</CodeBlock>

## Vector Field

LanceDB provides a `lancedb.pydantic.Vector` method to define a
vector Field in a Pydantic Model.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksPydanticVectorField}
</CodeBlock>

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

<CodeBlock filename="Python" language="Python" icon="python">
  {PyFrameworksPydanticTypeConversion}
</CodeBlock>

This example shows a more complex Pydantic model with various field types and demonstrates how LanceDB handles:

* Basic types: `int` and `str` fields
* Vector fields: `Vector(1536)` creates a fixed-size list of 1536 float32 values
* List fields: `List[int]` becomes a variable-length list of int64 values
* Schema generation: The `pydantic_to_schema()` function automatically converts all these types to their Arrow equivalents


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt