# Source: https://docs.lancedb.com/integrations/embedding/instructor.md

# Instructor

export const PyEmbeddingInstructorUsage = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\ninstructor = (\n    get_registry()\n    .get(\"instructor\")\n    .create(\n        source_instruction=\"represent the document for retrieval\",\n        query_instruction=\"represent the document for retrieving the most similar documents\",\n    )\n)\n\nclass Schema(LanceModel):\n    vector: Vector(instructor.ndims()) = instructor.VectorField()\n    text: str = instructor.SourceField()\n\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"instructor-demo\"))\ntbl = db.create_table(\"test\", schema=Schema, mode=\"overwrite\")\n\ntexts = [\n    {\n        \"text\": \"Capitalism has been dominant in the Western world since the end of feudalism.\"\n    },\n    {\n        \"text\": \"The disparate impact theory is especially controversial under the Fair Housing Act.\"\n    },\n    {\n        \"text\": \"Disparate impact in United States labor law refers to practices in employment.\"\n    },\n]\n\ntbl.add(texts)\n";

[Instructor](https://instructor-embedding.github.io/) is an instruction-finetuned text embedding model that can generate text embeddings tailored to any task (e.g. classification, retrieval, clustering, text evaluation, etc.) and domains (e.g. science, finance, etc.) by simply providing the task instruction, without any finetuning.

If you want to calculate customized embeddings for specific sentences, you can follow the unified template to write instructions.

<Info>
  Represent the `domain` `text_type` for `task_objective`:

  * `domain` is optional, and it specifies the domain of the text, e.g. science, finance, medicine, etc.
  * `text_type` is required, and it specifies the encoding unit, e.g. sentence, document, paragraph, etc.
  * `task_objective` is optional, and it specifies the objective of embedding, e.g. retrieve a document, classify the sentence, etc.
</Info>

More information about the model can be found at the [source URL](https://github.com/xlang-ai/instructor-embedding).

| Argument               | Type   | Default                                                              | Description                                               |
| ---------------------- | ------ | -------------------------------------------------------------------- | --------------------------------------------------------- |
| `name`                 | `str`  | "hkunlp/instructor-base"                                             | The name of the model to use                              |
| `batch_size`           | `int`  | `32`                                                                 | The batch size to use when generating embeddings          |
| `device`               | `str`  | `"cpu"`                                                              | The device to use when generating embeddings              |
| `show_progress_bar`    | `bool` | `True`                                                               | Whether to show a progress bar when generating embeddings |
| `normalize_embeddings` | `bool` | `True`                                                               | Whether to normalize the embeddings                       |
| `quantize`             | `bool` | `False`                                                              | Whether to quantize the model                             |
| `source_instruction`   | `str`  | `"represent the document for retrieval"`                             | The instruction for the source column                     |
| `query_instruction`    | `str`  | `"represent the document for retrieving the most similar documents"` | The instruction for the query                             |

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingInstructorUsage}
  </CodeBlock>
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt