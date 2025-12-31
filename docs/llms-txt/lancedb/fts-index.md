# Source: https://docs.lancedb.com/indexing/fts-index.md

# Full-Text Search (FTS) Index

> Create and tune BM25-based full-text search indexes in LanceDB.

export const FtsIndexWait = "table_name = \"fts-index-wait\"\n\ntable = db.open_table(table_name)\ntable.create_fts_index(\"text\")\n\nindex_name = \"text_idx\"\ntable.wait_for_index([index_name])\n";

export const FtsIndexCreate = "table_name = \"fts-index-create\"\ntable = db.open_table(table_name)\ntable.create_fts_index(\"text\")\n";

export const FtsIndexAsync = "import asyncio\n\nimport lancedb\nimport polars as pl\nfrom lancedb.index import FTS\n\ndata = pl.DataFrame(\n    {\n        \"id\": [1, 2],\n        \"text\": [\n            \"His first language is spanish\",\n            \"Her first language is english\",\n        ],\n    }\n)\n\nasync def main(data: pl.DataFrame):\n    uri = \"ex_lancedb\"\n    db = await lancedb.connect_async(uri)\n    tbl = await db.create_table(\"my_text\", data=data, mode=\"overwrite\")\n\n    await tbl.create_index(\"text\", config=FTS(language=\"English\"))\n\n    response = await tbl.search(\"spanish\", query_type=\"fts\")\n    result = await response.limit(1).to_polars()\n    print(result)\n    return result\n\nif __name__ == \"__main__\":\n    asyncio.run(main(data))\n";

LanceDB Cloud and Enterprise provide performant full-text search based on BM25, allowing you to incorporate keyword-based search in your retrieval solutions.

<Note>
  The `create_fts_index` API returns immediately, but index building happens asynchronously.
</Note>

## Creating FTS Indexes

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {FtsIndexCreate}
  </CodeBlock>
</CodeGroup>

Check FTS index status using the API:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {FtsIndexWait}
  </CodeBlock>
</CodeGroup>

<Note>
  In LanceDB OSS, `create_fts_index` is not supported with `AsyncTable`. When working with async connections, use `create_index` with the `FTS` configuration instead.

  <Expandable title="Code Example">
    <CodeGroup>
      <CodeBlock filename="Python" language="Python" icon="python">
        {FtsIndexAsync}
      </CodeBlock>
    </CodeGroup>
  </Expandable>
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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt