# Source: https://docs.lancedb.com/integrations/embedding/ibm.md

# IBM watsonx

export const PyEmbeddingIbmUsage = "import os\nimport tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.embeddings import EmbeddingFunctionRegistry\nfrom lancedb.pydantic import LanceModel, Vector\n\nwatsonx_embed = (\n    EmbeddingFunctionRegistry.get_instance()\n    .get(\"watsonx\")\n    .create(\n        name=\"ibm/slate-125m-english-rtrvr\",\n        api_key=os.environ.get(\"WATSONX_API_KEY\"),\n        project_id=os.environ.get(\"WATSONX_PROJECT_ID\"),\n    )\n)\n\nclass TextModel(LanceModel):\n    text: str = watsonx_embed.SourceField()\n    vector: Vector(watsonx_embed.ndims()) = watsonx_embed.VectorField()\n\ndata = [\n    {\"text\": \"hello world\"},\n    {\"text\": \"goodbye world\"},\n]\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"watsonx-demo\"))\ntbl = db.create_table(\"watsonx_test\", schema=TextModel, mode=\"overwrite\")\ntbl.add(data)\n\nrs = tbl.search(\"hello\").limit(1).to_pandas()\nprint(rs.head())\n";

Generate text embeddings using IBM's watsonx.ai platform.

## Supported Models

You can find a list of supported models at [IBM watsonx.ai Documentation](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models-embed.html?context=wx). The currently supported model names are:

* `ibm/slate-125m-english-rtrvr`
* `ibm/slate-30m-english-rtrvr`
* `sentence-transformers/all-minilm-l12-v2`
* `intfloat/multilingual-e5-large`

## Parameters

The following parameters can be passed to the `create` method:

| Parameter   | Type | Default Value                  | Description                                               |
| ----------- | ---- | ------------------------------ | --------------------------------------------------------- |
| name        | str  | "ibm/slate-125m-english-rtrvr" | The model ID of the watsonx.ai model to use               |
| api\_key    | str  | None                           | Optional IBM Cloud API key (or set `WATSONX_API_KEY`)     |
| project\_id | str  | None                           | Optional watsonx project ID (or set `WATSONX_PROJECT_ID`) |
| url         | str  | None                           | Optional custom URL for the watsonx.ai instance           |
| params      | dict | None                           | Optional additional parameters for the embedding model    |

## Usage Example

First, the watsonx.ai library is an optional dependency, so must be installed seperately:

```
pip install ibm-watsonx-ai
```

Optionally set environment variables (if not passing credentials to `create` directly):

```sh  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
export WATSONX_API_KEY="YOUR_WATSONX_API_KEY"
export WATSONX_PROJECT_ID="YOUR_WATSONX_PROJECT_ID"
```

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingIbmUsage}
  </CodeBlock>
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt