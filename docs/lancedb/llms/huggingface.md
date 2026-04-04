# Source: https://docs.lancedb.com/integrations/embedding/huggingface.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hugging Face

export const PyEmbeddingHuggingfaceUsage = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nimport pandas as pd\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"huggingface-demo\"))\nmodel = get_registry().get(\"huggingface\").create(name=\"facebook/bart-base\")\n\nclass Words(LanceModel):\n    text: str = model.SourceField()\n    vector: Vector(model.ndims()) = model.VectorField()\n\ndf = pd.DataFrame({\"text\": [\"hi hello sayonara\", \"goodbye world\"]})\ntable = db.create_table(\"greets\", schema=Words)\ntable.add(df)\nquery = \"old greeting\"\nactual = table.search(query).limit(1).to_pydantic(Words)[0]\nprint(actual.text)\n";

We offer support for all Hugging Face models (which can be loaded via [transformers](https://huggingface.co/docs/transformers/en/index) library). The default model is `colbert-ir/colbertv2.0` which also has its own special callout - `registry.get("colbert")`. Some Hugging Face models might require custom models defined on the HuggingFace Hub in their own modeling files. You may enable this by setting `trust_remote_code=True`. This option should only be set to True for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine.

Example usage:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingHuggingfaceUsage}
  </CodeBlock>
</CodeGroup>
