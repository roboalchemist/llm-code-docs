# Source: https://docs.lancedb.com/integrations/embedding/openclip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenCLIP

export const PyEmbeddingOpenclipImageSearch = "import io\n\nfrom PIL import Image\n\nquery_image_uri = \"http://farm1.staticflickr.com/200/467715466_ed4a31801f_z.jpg\"\nimage_bytes = requests.get(query_image_uri).content\nquery_image = Image.open(io.BytesIO(image_bytes))\nactual = table.search(query_image).limit(1).to_pydantic(Images)[0]\nprint(actual.label == \"dog\")\n\nother = (\n    table.search(query_image, vector_column_name=\"vec_from_bytes\")\n    .limit(1)\n    .to_pydantic(Images)[0]\n)\nprint(other.label)\n";

export const PyEmbeddingOpenclipTextSearch = "actual = table.search(\"man's best friend\").limit(1).to_pydantic(Images)[0]\nprint(actual.label)\n\nfrombytes = (\n    table.search(\"man's best friend\", vector_column_name=\"vec_from_bytes\")\n    .limit(1)\n    .to_pydantic(Images)[0]\n)\nprint(frombytes.label)\n";

export const PyEmbeddingOpenclipSetup = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nimport pandas as pd\nimport requests\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"openclip-demo\"))\nfunc = get_registry().get(\"open-clip\").create()\n\nclass Images(LanceModel):\n    label: str\n    image_uri: str = func.SourceField()\n    image_bytes: bytes = func.SourceField()\n    vector: Vector(func.ndims()) = func.VectorField()\n    vec_from_bytes: Vector(func.ndims()) = func.VectorField()\n\ntable = db.create_table(\"images\", schema=Images)\nlabels = [\"cat\", \"cat\", \"dog\", \"dog\", \"horse\", \"horse\"]\nuris = [\n    \"http://farm1.staticflickr.com/53/167798175_7c7845bbbd_z.jpg\",\n    \"http://farm1.staticflickr.com/134/332220238_da527d8140_z.jpg\",\n    \"http://farm9.staticflickr.com/8387/8602747737_2e5c2a45d4_z.jpg\",\n    \"http://farm5.staticflickr.com/4092/5017326486_1f46057f5f_z.jpg\",\n    \"http://farm9.staticflickr.com/8216/8434969557_d37882c42d_z.jpg\",\n    \"http://farm6.staticflickr.com/5142/5835678453_4f3a4edb45_z.jpg\",\n]\nimage_bytes = [requests.get(uri).content for uri in uris]\ntable.add(\n    pd.DataFrame({\"label\": labels, \"image_uri\": uris, \"image_bytes\": image_bytes})\n)\n";

We support CLIP model embeddings using the open source alternative, [open-clip](https://github.com/mlfoundations/open_clip) which supports various customizations. It is registered as `open-clip` and supports the following customizations:

| Parameter    | Type   | Default Value         | Description                                                             |
| ------------ | ------ | --------------------- | ----------------------------------------------------------------------- |
| `name`       | `str`  | `"ViT-B-32"`          | The name of the model.                                                  |
| `pretrained` | `str`  | `"laion2b_s34b_b79k"` | The name of the pretrained model to load.                               |
| `device`     | `str`  | `"cpu"`               | The device to run the model on. Can be `"cpu"` or `"gpu"`.              |
| `batch_size` | `int`  | `64`                  | The number of images to process in a batch.                             |
| `normalize`  | `bool` | `True`                | Whether to normalize the input images before feeding them to the model. |

This embedding function supports ingesting images as both bytes and urls. You can query them using both test and other images.

<Info>
  LanceDB supports ingesting images directly from accessible links.
</Info>

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingOpenclipSetup}
  </CodeBlock>
</CodeGroup>

Now we can search using text from both the default vector column and the custom vector column

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingOpenclipTextSearch}
  </CodeBlock>
</CodeGroup>

Because we're using a multimodal embedding function, we can also search using images

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingOpenclipImageSearch}
  </CodeBlock>
</CodeGroup>
