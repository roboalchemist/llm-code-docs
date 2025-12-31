# Source: https://docs.lancedb.com/integrations/data/polars_arrow.md

# Polars

export const PyPlatformsPolarsVectorSearch = "polars_results = (\n    polars_table.search([0.1, 0.2, 0.3])\n    .select([\"text\", \"_distance\"])\n    .limit(1)\n    .to_polars()\n)\nprint(polars_results)\n";

export const PyPlatformsPolarsPydantic = "class BirdModel(LanceModel):\n    text: str\n    vector: Vector(3)\n\nschema_table = polars_db.create_table(\n    \"birds_schema\", schema=BirdModel, mode=\"overwrite\"\n)\nschema_table.add(birds.to_dicts())\n";

export const PyPlatformsPolarsLazyframe = "lazy_frame = polars_table.to_polars().lazy()\nprint(lazy_frame.select([\"text\"]).collect())\n";

export const PyPlatformsPolarsImports = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nimport polars as pl\nfrom lancedb.pydantic import LanceModel, Vector\n";

export const PyPlatformsPolarsCreateTable = "birds = pl.DataFrame(\n    {\n        \"text\": [\"phoenix\", \"sparrow\"],\n        \"vector\": [\n            [0.1, 0.2, 0.3],\n            [0.8, 0.6, 0.5],\n        ],\n    }\n)\npolars_db = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"polars-demo\"))\npolars_table = polars_db.create_table(\n    \"birds\", data=birds.to_arrow(), mode=\"overwrite\"\n)\n";

LanceDB supports [Polars](https://github.com/pola-rs/polars), a blazingly fast DataFrame library for Python written in Rust. Under the hood, both Lance and Polars speak Arrow, so passing data back and forth stays zero-copy and ergonomic.

## Create & Query a Table

Import the required libraries, including the optional Pydantic helpers if you plan to define schemas.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPolarsImports}
</CodeBlock>

Build a Polars `DataFrame`, convert it to Arrow, and use it directly when creating a LanceDB table.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPolarsCreateTable}
</CodeBlock>

Run vector search and keep the results as a Polars `DataFrame` for further processing or visualization.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPolarsVectorSearch}
</CodeBlock>

## Work with LazyFrames

When you want to operate on the entire table (potentially larger than RAM), convert to a Polars `LazyFrame` so you can chain transformations without loading everything at once.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPolarsLazyframe}
</CodeBlock>

## Define Schemas with Pydantic

You can also describe your table via `LanceModel` and continue ingesting data from Polars. This is useful when multiple teams share a schema or when you want validation.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPolarsPydantic}
</CodeBlock>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt