# Source: https://docs.lancedb.com/integrations/embedding/gemini.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini

export const PyEmbeddingGeminiUsage = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nimport pandas as pd\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\nmodel = get_registry().get(\"gemini-text\").create()\n\nclass TextModel(LanceModel):\n    text: str = model.SourceField()\n    vector: Vector(model.ndims()) = model.VectorField()\n\ndf = pd.DataFrame({\"text\": [\"hello world\", \"goodbye world\"]})\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"gemini-demo\"))\ntbl = db.create_table(\"test\", schema=TextModel, mode=\"overwrite\")\n\ntbl.add(df)\nrs = tbl.search(\"hello\").limit(1).to_pandas()\nprint(rs.head())\n";

With Google's Gemini, you can represent text (words, sentences, and blocks of text) in a vectorized form, making it easier to compare and contrast embeddings. For example, two texts that share a similar subject matter or sentiment should have similar embeddings, which can be identified through mathematical comparison techniques such as cosine similarity. For more on how and why you should use embeddings, refer to the Embeddings guide.
The Gemini Embedding Model API supports various task types:

| Task Type               | Description                                                                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "`retrieval_query`"     | Specifies the given text is a query in a search/retrieval setting.                                                                                         |
| "`retrieval_document`"  | Specifies the given text is a document in a search/retrieval setting. Using this task type requires a title but is automatically proided by Embeddings API |
| "`semantic_similarity`" | Specifies the given text will be used for Semantic Textual Similarity (STS).                                                                               |
| "`classification`"      | Specifies that the embeddings will be used for classification.                                                                                             |
| "`clusering`"           | Specifies that the embeddings will be used for clustering.                                                                                                 |

Usage Example:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingGeminiUsage}
  </CodeBlock>
</CodeGroup>
