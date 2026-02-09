# Source: https://docs.lancedb.com/integrations/reranking/colbert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ColBERT Reranker

> Enhance search results with ColBERT's contextual reranking in LanceDB. Features efficient model deployment, device optimization, and flexible scoring options for vector, FTS, and hybrid search.

export const PyRerankingColbertUsage = "import lancedb\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\nfrom lancedb.rerankers import ColbertReranker\n\nembedder = get_registry().get(\"sentence-transformers\").create()\ndb = lancedb.connect(\"~/.lancedb\")\n\nclass Schema(LanceModel):\n    text: str = embedder.SourceField()\n    vector: Vector(embedder.ndims()) = embedder.VectorField()\n\ndata = [\n    {\"text\": \"hello world\"},\n    {\"text\": \"goodbye world\"},\n]\ntbl = db.create_table(\"test\", schema=Schema, mode=\"overwrite\")\ntbl.add(data)\nreranker = ColbertReranker()\n\n# Run vector search with a reranker\nresult = tbl.search(\"hello\").rerank(reranker=reranker).to_list()\n\n# Run FTS search with a reranker\nresult = tbl.search(\"hello\", query_type=\"fts\").rerank(reranker=reranker).to_list()\n\n# Run hybrid search with a reranker\ntbl.create_fts_index(\"text\", replace=True)\nresult = (\n    tbl.search(\"hello\", query_type=\"hybrid\").rerank(reranker=reranker).to_list()\n)\n";

# ColBERT Reranker

This reranker uses ColBERT model to rerank the search results. You can use this reranker by passing `ColbertReranker()` to the `rerank()` method.

> **Note:** Supported query types – Hybrid, Vector, and FTS.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyRerankingColbertUsage}
  </CodeBlock>
</CodeGroup>

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
