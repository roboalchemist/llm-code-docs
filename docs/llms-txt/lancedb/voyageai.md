# Source: https://docs.lancedb.com/integrations/reranking/voyageai.md

# Source: https://docs.lancedb.com/integrations/embedding/voyageai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VoyageAI

export const PyEmbeddingVoyageaiMultimodal = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.embeddings import EmbeddingFunctionRegistry\nfrom lancedb.pydantic import LanceModel, Vector\n\n# Create multimodal embedding function with custom dimension\nvoyageai = (\n    EmbeddingFunctionRegistry.get_instance()\n    .get(\"voyageai\")\n    .create(name=\"voyage-multimodal-3.5\", output_dimension=512)\n)\n\nclass ImageModel(LanceModel):\n    image_uri: str = voyageai.SourceField()\n    vector: Vector(voyageai.ndims()) = voyageai.VectorField()\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"voyageai-multimodal\"))\ntbl = db.create_table(\"images\", schema=ImageModel, mode=\"overwrite\")\n\n# Add images using URLs\ntbl.add(\n    [\n        {\"image_uri\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/300px-PNG_transparency_demonstration_1.png\"},\n    ]\n)\n\n# Search with text query\nresults = tbl.search(\"dice\").limit(1).to_list()\nprint(results)\n";

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
* voyage-multimodal-3.5 (multimodal - supports text, images, and video)

<Info>
  **Multimodal Model:** `voyage-multimodal-3.5` supports text, images, and video inputs. It outputs 1024-dimensional embeddings by default, configurable via the `output_dimension` parameter (256, 512, 1024, 2048). See the [VoyageAI multimodal embeddings documentation](https://docs.voyageai.com/docs/multimodal-embeddings) for more details.
</Info>

Supported parameters (to be passed in `create` method) are:

| Parameter          | Type   | Default Value | Description                                                                                                                                                                                                             |
| ------------------ | ------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`             | `str`  | `None`        | The model ID of the model to use. Supported models: voyage-3, voyage-3-lite, voyage-3.5, voyage-3.5-lite, voyage-context-3, voyage-finance-2, voyage-multilingual-2, voyage-law-2, voyage-code-2, voyage-multimodal-3.5 |
| `input_type`       | `str`  | `None`        | Type of the input text. Default to None. Other options: query, document.                                                                                                                                                |
| `truncation`       | `bool` | `True`        | Whether to truncate the input texts to fit within the context length.                                                                                                                                                   |
| `output_dimension` | `int`  | `None`        | Output embedding dimension. Only supported by `voyage-multimodal-3.5`. Valid options: 256, 512, 1024 (default), 2048.                                                                                                   |

Usage Example:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingVoyageaiUsage}
  </CodeBlock>
</CodeGroup>

### Multimodal Example

The `voyage-multimodal-3.5` model can embed text alongside images. You can use image URLs, file paths, or PIL Image objects:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingVoyageaiMultimodal}
  </CodeBlock>
</CodeGroup>
