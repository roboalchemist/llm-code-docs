# Source: https://docs.lancedb.com/integrations/data/pandas_and_pyarrow.md

# Pandas and PyArrow

export const PyPlatformsPandasVectorSearch = "pandas_results = (\n    pandas_table.search([0.9, 0.1, 0.3])\n    .select([\"text\", \"_distance\"])\n    .limit(1)\n    .to_pandas()\n)\nprint(pandas_results)\n";

export const PyPlatformsPandasImports = "import asyncio\nimport tempfile\nfrom pathlib import Path\n\nimport lancedb\nimport pandas as pd\n";

export const PyPlatformsPandasCreateTable = "pandas_df = pd.DataFrame(\n    [\n        {\"id\": \"1\", \"text\": \"dragon\", \"vector\": [0.9, 0.1, 0.3]},\n        {\"id\": \"2\", \"text\": \"griffin\", \"vector\": [0.4, 0.5, 0.2]},\n        {\"id\": \"3\", \"text\": \"phoenix\", \"vector\": [0.7, 0.3, 0.6]},\n    ]\n)\npandas_db = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"pandas-demo\"))\npandas_table = pandas_db.create_table(\"creatures\", data=pandas_df, mode=\"overwrite\")\n";

export const PyPlatformsPandasAsyncExample = "async def run_pandas_async_example() -> None:\n    async_db = await lancedb.connect_async(\n        str(Path(tempfile.mkdtemp()) / \"pandas-async\")\n    )\n    async_df = pd.DataFrame(\n        [\n            {\"id\": \"10\", \"text\": \"sage\", \"vector\": [0.6, 0.4, 0.8]},\n            {\"id\": \"11\", \"text\": \"bard\", \"vector\": [0.2, 0.7, 0.3]},\n        ]\n    )\n    async_table = await async_db.create_table(\n        \"creatures_async\", data=async_df, mode=\"overwrite\"\n    )\n    async_results = await (\n        async_table.search([0.6, 0.4, 0.8])\n        .select([\"text\", \"_distance\"])\n        .limit(1)\n        .to_pandas()\n    )\n    print(async_results)\n\nasyncio.run(run_pandas_async_example())\n";

Because Lance is built on top of [Apache Arrow](https://arrow.apache.org/),
LanceDB fits naturally into Pandas-first workflows. You can ingest a `DataFrame`,
query it with LanceDB's vector operators, and keep working in Pandas without any glue code.

## Create a dataset

Start by importing LanceDB alongside your usual Pandas utilities and connect to a temporary database.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPandasImports}
</CodeBlock>

Use the familiar `pd.DataFrame` API to prepare your rows, then pass the entire frame to `db.create_table`.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPandasCreateTable}
</CodeBlock>

## Vector search

Queries can return Pandas frames as well, so you can immediately inspect the results or pipe them into downstream analytics.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPandasVectorSearch}
</CodeBlock>

## Async API

For web services or background jobs that already rely on `asyncio`, use the asynchronous helpers to keep everything non-blocking.

<CodeBlock filename="Python" language="Python" icon="python">
  {PyPlatformsPandasAsyncExample}
</CodeBlock>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt