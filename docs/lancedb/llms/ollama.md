# Source: https://docs.lancedb.com/integrations/embedding/ollama.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ollama

export const PyEmbeddingOllamaUsage = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"ollama-demo\"))\nfunc = get_registry().get(\"ollama\").create(name=\"nomic-embed-text\")\n\nclass Words(LanceModel):\n    text: str = func.SourceField()\n    vector: Vector(func.ndims()) = func.VectorField()\n\ntable = db.create_table(\"words\", schema=Words, mode=\"overwrite\")\ntable.add(\n    [\n        {\"text\": \"hello world\"},\n        {\"text\": \"goodbye world\"},\n    ]\n)\n\nquery = \"greetings\"\nactual = table.search(query).limit(1).to_pydantic(Words)[0]\nprint(actual.text)\n";

Generate embeddings via the [ollama](https://github.com/ollama/ollama-python) python library. More details:

* [Ollama docs on embeddings](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings)
* [Ollama blog on embeddings](https://ollama.com/blog/embedding-models)

| Parameter              | Type                       | Default Value            | Description                                                                                      |
| ---------------------- | -------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------ |
| `name`                 | `str`                      | `nomic-embed-text`       | The name of the model.                                                                           |
| `host`                 | `str`                      | `http://localhost:11434` | The Ollama host to connect to.                                                                   |
| `options`              | `ollama.Options` or `dict` | `None`                   | Additional model parameters listed in the documentation for the Modelfile such as `temperature`. |
| `keep_alive`           | `float` or `str`           | `"5m"`                   | Controls how long the model will stay loaded into memory following the request.                  |
| `ollama_client_kwargs` | `dict`                     | `{}`                     | kwargs that can be past to the `ollama.Client`.                                                  |

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingOllamaUsage}
  </CodeBlock>
</CodeGroup>
