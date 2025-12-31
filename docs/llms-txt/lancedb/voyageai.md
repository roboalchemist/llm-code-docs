# Source: https://docs.lancedb.com/integrations/reranking/voyageai.md

# Source: https://docs.lancedb.com/integrations/embedding/voyageai.md

# Source: https://docs.lancedb.com/integrations/reranking/voyageai.md

# Source: https://docs.lancedb.com/integrations/embedding/voyageai.md

# VoyageAI

export const PyEmbeddingVoyageaiUsage = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.embeddings import EmbeddingFunctionRegistry\nfrom lancedb.pydantic import LanceModel, Vector\n\nvoyageai = (\n    EmbeddingFunctionRegistry.get_instance().get(\"voyageai\").create(name=\"voyage-3\")\n)\n\nclass TextModel(LanceModel):\n    text: str = voyageai.SourceField()\n    vector: Vector(voyageai.ndims()) = voyageai.VectorField()\n\ndata = [{\"text\": \"hello world\"}, {\"text\": \"goodbye world\"}]\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"voyageai-demo\"))\ntbl = db.create_table(\"test\", schema=TextModel, mode=\"overwrite\")\n\ntbl.add(data)\n";

Voyage AI provides cutting-edge embedding and rerankers.

Using voyageai API requires voyageai package, which can be installed using `pip install voyageai`. Voyage AI embeddings are used to generate embeddings for text data. The embeddings can be used for various tasks like semantic search, clustering, and classification.
You also need to set the `VOYAGE_API_KEY` environment variable to use the VoyageAI API.

Supported models are:

* voyage-context-3
* voyage-3.5
* voyage-3.5-lite
* voyage-3
* voyage-3-lite
* voyage-finance-2
* voyage-multilingual-2
* voyage-law-2
* voyage-code-2

Supported parameters (to be passed in `create` method) are:

| Parameter    | Type   | Default Value | Description                                                                                                                                                                |
| ------------ | ------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`       | `str`  | `None`        | The model ID of the model to use. Supported base models for Text Embeddings: voyage-3, voyage-3-lite, voyage-finance-2, voyage-multilingual-2, voyage-law-2, voyage-code-2 |
| `input_type` | `str`  | `None`        | Type of the input text. Default to None. Other options: query, document.                                                                                                   |
| `truncation` | `bool` | `True`        | Whether to truncate the input texts to fit within the context length.                                                                                                      |

Usage Example:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingVoyageaiUsage}
  </CodeBlock>
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt