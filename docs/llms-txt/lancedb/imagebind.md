# Source: https://docs.lancedb.com/integrations/embedding/imagebind.md

# ImageBind

export const PyEmbeddingImagebindTextSearch = "query = \"an animal which flies and tweets\"\nactual = table.search(query).limit(1).to_pydantic(ImageBindModel)[0]\nprint(actual.text == \"bird\")\n";

export const PyEmbeddingImagebindAudioSearch = "query_audio = \"./assets/car_audio2.wav\"\nactual = table.search(query_audio).limit(1).to_pydantic(ImageBindModel)[0]\nprint(actual.text == \"car\")\n";

export const PyEmbeddingImagebindImageSearch = "query_image = \"./assets/dog_image2.jpg\"\nactual = table.search(query_image).limit(1).to_pydantic(ImageBindModel)[0]\nprint(actual.text == \"dog\")\n";

export const PyEmbeddingImagebindSetup = "import lancedb\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\ndb = lancedb.connect(\"/tmp/imagebind-db\")\nfunc = get_registry().get(\"imagebind\").create()\n\nclass ImageBindModel(LanceModel):\n    text: str\n    image_uri: str = func.SourceField()\n    audio_path: str\n    vector: Vector(func.ndims()) = func.VectorField()\n\ntext_list = [\"A dog.\", \"A car\", \"A bird\"]\nimage_paths = [\n    \"./assets/dog_image.jpg\",\n    \"./assets/car_image.jpg\",\n    \"./assets/bird_image.jpg\",\n]\naudio_paths = [\n    \"./assets/dog_audio.wav\",\n    \"./assets/car_audio.wav\",\n    \"./assets/bird_audio.wav\",\n]\n\ninputs = [\n    {\"text\": a, \"audio_path\": b, \"image_uri\": c}\n    for a, b, c in zip(text_list, audio_paths, image_paths)\n]\n\ntable = db.create_table(\"img_bind\", schema=ImageBindModel)\ntable.add(inputs)\n";

We have support for [imagebind](https://github.com/facebookresearch/ImageBind) model embeddings. You can download our version of the packaged model via - `pip install imagebind-packaged==0.1.2`.

This function is registered as `imagebind` and supports Audio, Video and Text modalities(extending to Thermal,Depth,IMU data):

| Parameter   | Type   | Default Value      | Description                                                    |
| ----------- | ------ | ------------------ | -------------------------------------------------------------- |
| `name`      | `str`  | `"imagebind_huge"` | Name of the model.                                             |
| `device`    | `str`  | `"cpu"`            | The device to run the model on. Can be `"cpu"` or `"gpu"`.     |
| `normalize` | `bool` | `False`            | set to `True` to normalize your inputs before model ingestion. |

Below is an example demonstrating how the API works:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingImagebindSetup}
  </CodeBlock>
</CodeGroup>

Now, we can search using any modality:

#### image search

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingImagebindImageSearch}
  </CodeBlock>
</CodeGroup>

#### audio search

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingImagebindAudioSearch}
  </CodeBlock>
</CodeGroup>

#### Text search

You can add any input query and fetch the result as follows:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingImagebindTextSearch}
  </CodeBlock>
</CodeGroup>

If you have any questions about the embeddings API, supported models, or see a relevant model missing, please raise an issue [on GitHub](https://github.com/lancedb/lancedb/issues).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt