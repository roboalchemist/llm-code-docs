# Source: https://docs.lancedb.com/integrations/reranking/openai.md

# Source: https://docs.lancedb.com/integrations/embedding/openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI

export const PyEmbeddingOpenaiBasic = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\ndb_path = Path(tempfile.mkdtemp()) / \"openai-embeddings\"\ndb = lancedb.connect(str(db_path))\nfunc = get_registry().get(\"openai\").create(name=\"text-embedding-ada-002\")\n\nclass Words(LanceModel):\n    text: str = func.SourceField()\n    vector: Vector(func.ndims()) = func.VectorField()\n\ntable = db.create_table(\"words\", schema=Words, mode=\"overwrite\")\ntable.add(\n    [\n        {\"text\": \"hello world\"},\n        {\"text\": \"goodbye world\"},\n    ]\n)\n\nquery = \"greetings\"\nactual = table.search(query).limit(1).to_pydantic(Words)[0]\nprint(actual.text)\n";

LanceDB registers the OpenAI embeddings function in the registry by default, as `openai`. Below are the parameters that you can customize when creating the instances:

| Parameter   | Type  | Default Value              | Description                                                                                                                             |
| ----------- | ----- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `name`      | `str` | `"text-embedding-ada-002"` | The name of the model.                                                                                                                  |
| `dim`       | `int` | Model default              | For OpenAI's newer text-embedding-3 model, we can specify a dimensionality that is smaller than the 1536 size. This feature supports it |
| `use_azure` | bool  | `False`                    | Set true to use Azure OpenAPI SDK                                                                                                       |

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingOpenaiBasic}
  </CodeBlock>
</CodeGroup>
