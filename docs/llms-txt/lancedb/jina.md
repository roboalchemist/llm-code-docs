# Source: https://docs.lancedb.com/integrations/reranking/jina.md

# Source: https://docs.lancedb.com/integrations/embedding/jina.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Jina

export const PyEmbeddingJinaMultimodal = "import os\nimport tempfile\nfrom pathlib import Path\n\nimport lancedb\nimport pandas as pd\nimport requests\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\nos.environ[\"JINA_API_KEY\"] = os.environ.get(\"JINA_API_KEY\", \"jina_*\")\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"jina-images\"))\nfunc = get_registry().get(\"jina\").create()\n\nclass Images(LanceModel):\n    label: str\n    image_uri: str = func.SourceField()\n    image_bytes: bytes = func.SourceField()\n    vector: Vector(func.ndims()) = func.VectorField()\n    vec_from_bytes: Vector(func.ndims()) = func.VectorField()\n\ntable = db.create_table(\"images\", schema=Images)\nlabels = [\"cat\", \"cat\", \"dog\", \"dog\", \"horse\", \"horse\"]\nuris = [\n    \"http://farm1.staticflickr.com/53/167798175_7c7845bbbd_z.jpg\",\n    \"http://farm1.staticflickr.com/134/332220238_da527d8140_z.jpg\",\n    \"http://farm9.staticflickr.com/8387/8602747737_2e5c2a45d4_z.jpg\",\n    \"http://farm5.staticflickr.com/4092/5017326486_1f46057f5f_z.jpg\",\n    \"http://farm9.staticflickr.com/8216/8434969557_d37882c42d_z.jpg\",\n    \"http://farm6.staticflickr.com/5142/5835678453_4f3a4edb45_z.jpg\",\n]\nimage_bytes = [requests.get(uri).content for uri in uris]\ntable.add(\n    pd.DataFrame({\"label\": labels, \"image_uri\": uris, \"image_bytes\": image_bytes})\n)\n";

export const PyEmbeddingJinaText = "import os\nimport tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.embeddings import EmbeddingFunctionRegistry\nfrom lancedb.pydantic import LanceModel, Vector\n\nos.environ[\"JINA_API_KEY\"] = os.environ[\"JINA_API_KEY\"]\n\njina_embed = (\n    EmbeddingFunctionRegistry.get_instance()\n    .get(\"jina\")\n    .create(name=\"jina-embeddings-v2-base-en\")\n)\n\nclass TextModel(LanceModel):\n    text: str = jina_embed.SourceField()\n    vector: Vector(jina_embed.ndims()) = jina_embed.VectorField()\n\ndata = [{\"text\": \"hello world\"}, {\"text\": \"goodbye world\"}]\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"jina-text\"))\ntbl = db.create_table(\"test\", schema=TextModel, mode=\"overwrite\")\n\ntbl.add(data)\n";

## Text Embedding Models

Jina embeddings are used to generate embeddings for text and image data.
You also need to set the `JINA_API_KEY` environment variable to use the Jina API.

You can find a list of supported models under [https://jina.ai/embeddings/](https://jina.ai/embeddings/)

Supported parameters (to be passed in `create` method) are:

| Parameter | Type  | Default Value    | Description                           |
| --------- | ----- | ---------------- | ------------------------------------- |
| `name`    | `str` | `"jina-clip-v1"` | The model ID of the jina model to use |

Usage Example:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingJinaText}
  </CodeBlock>
</CodeGroup>

## Multimodal Embedding Models

Jina embeddings can also be used to embed both text and image data, only some of the models support image data and you can check the list
under [https://jina.ai/embeddings/](https://jina.ai/embeddings/)

Supported parameters (to be passed in `create` method) are:

| Parameter | Type  | Default Value    | Description                           |
| --------- | ----- | ---------------- | ------------------------------------- |
| `name`    | `str` | `"jina-clip-v1"` | The model ID of the jina model to use |

Usage Example:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingJinaMultimodal}
  </CodeBlock>
</CodeGroup>
