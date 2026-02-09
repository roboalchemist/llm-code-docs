# Source: https://docs.lancedb.com/integrations/reranking/rrf.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reciprocal Rank Fusion Reranker

> Learn about LanceDB's default Reciprocal Rank Fusion (RRF) reranker for hybrid search. Implements the Cormack et al. algorithm for optimal search result ranking.

export const PyRerankingRrfUsage = "import lancedb\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\nfrom lancedb.rerankers import RRFReranker\n\nembedder = get_registry().get(\"sentence-transformers\").create()\ndb = lancedb.connect(\"~/.lancedb\")\n\nclass Schema(LanceModel):\n    text: str = embedder.SourceField()\n    vector: Vector(embedder.ndims()) = embedder.VectorField()\n\ndata = [\n    {\"text\": \"hello world\"},\n    {\"text\": \"goodbye world\"},\n]\ntbl = db.create_table(\"test\", schema=Schema, mode=\"overwrite\")\ntbl.add(data)\nreranker = RRFReranker()\n\n# Run hybrid search with a reranker\ntbl.create_fts_index(\"text\", replace=True)\nresult = (\n    tbl.search(\"hello\", query_type=\"hybrid\").rerank(reranker=reranker).to_list()\n)\n";

# Reciprocal Rank Fusion Reranker

This is the default reranker used by LanceDB hybrid search. Reciprocal Rank Fusion (RRF) is an algorithm that evaluates the search scores by leveraging the positions/rank of the documents. The implementation follows this [paper](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf).

> **Note:** Supported query type – Hybrid search.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyRerankingRrfUsage}
  </CodeBlock>
</CodeGroup>

## Accepted Arguments

| Argument       | Type  | Default       | Description                                                                                                                                                                                                             |
| -------------- | ----- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `K`            | `int` | `60`          | A constant used in the RRF formula (default is 60). Experiments indicate that k = 60 was near-optimal, but that the choice is not critical.                                                                             |
| `return_score` | `str` | `"relevance"` | Options are "relevance" or "all". The type of score to return. If "relevance", will return only the `_relevance_score`. If "all", will return all scores from the vector and FTS search along with the relevance score. |

## Supported Scores for each query type

You can specify the type of scores you want the reranker to return. The following are the supported scores for each query type:

### Hybrid Search

| `return_score` | Status      | Description                                                                                                 |
| -------------- | ----------- | ----------------------------------------------------------------------------------------------------------- |
| `relevance`    | ✅ Supported | Returned rows only have the `_relevance_score` column.                                                      |
| `all`          | ✅ Supported | Returned rows have vector(`_distance`) and FTS(`score`) along with Hybrid Search score(`_relevance_score`). |
