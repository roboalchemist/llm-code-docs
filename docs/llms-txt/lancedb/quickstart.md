# Source: https://docs.lancedb.com/quickstart.md

# Source: https://docs.lancedb.com/embedding/quickstart.md

# Source: https://docs.lancedb.com/quickstart.md

# Source: https://docs.lancedb.com/embedding/quickstart.md

# Embeddings: Quickstart

> Quickstart guide for generating and working with embeddings.

export const TsOpenaiEmbeddings = "const db = await lancedb.connect(databaseDir);\nconst func = getRegistry()\n  .get(\"openai\")\n  ?.create({ model: \"text-embedding-ada-002\" }) as EmbeddingFunction;\n\nconst wordsSchema = LanceSchema({\n  text: func.sourceField(new Utf8()),\n  vector: func.vectorField(),\n});\nconst tbl = await db.createEmptyTable(\"words\", wordsSchema, {\n  mode: \"overwrite\",\n});\nawait tbl.add([{ text: \"hello world\" }, { text: \"goodbye world\" }]);\n\nconst query = \"greetings\";\nconst actual = (await tbl.search(query).limit(1).toArray())[0];\n";

export const PyOpenaiEmbeddings = "db = lancedb.connect(\"/tmp/db\")\nfunc = get_registry().get(\"openai\").create(name=\"text-embedding-ada-002\")\n\nclass Words(LanceModel):\n    text: str = func.SourceField()\n    vector: Vector(func.ndims()) = func.VectorField()\n\ntable = db.create_table(\"words\", schema=Words, mode=\"overwrite\")\ntable.add([{\"text\": \"hello world\"}, {\"text\": \"goodbye world\"}])\n\nquery = \"greetings\"\nactual = table.search(query).limit(1).to_pydantic(Words)[0]\nprint(actual.text)\n";

export const TsImports = "import * as lancedb from \"@lancedb/lancedb\";\nimport \"@lancedb/lancedb/embedding/openai\";\nimport { LanceSchema, getRegistry, register } from \"@lancedb/lancedb/embedding\";\nimport { EmbeddingFunction } from \"@lancedb/lancedb/embedding\";\nimport { type Float, Float32, Utf8 } from \"apache-arrow\";\n";

export const PyImports = "from lancedb.pydantic import LanceModel, Vector\nfrom lancedb.embeddings import get_registry\n";

LanceDB will automatically vectorize the data both at ingestion and query time. All you need to do is specify which model to use.

We support popular embedding models like OpenAI, Hugging Face, Sentence Transformers, CLIP, and more.

## Step 1: Import Required Libraries

First, import the necessary LanceDB components:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  import lancedb
  from lancedb.pydantic import LanceModel, Vector
  from lancedb.embeddings import get_registry
  ```
</CodeGroup>

* `lancedb`: The main database connection and operations
* `LanceModel`: Pydantic model for defining table schemas
* `Vector`: Field type for storing vector embeddings
* `get_registry()`: Access to the embedding function registry. It has all the supported as well custom embedding functions registered by the user

## Step 2: Connect to LanceDB Cloud

Establish a connection to your LanceDB instance:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  # Enter your LanceDB connection URI for OSS, Cloud or Enterprise here
  db = lancedb.connect(...)
  ```
</CodeGroup>

## Step 3: Initialize the Embedding Function

Choose and configure your embedding model:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  model = get_registry().get("sentence-transformers").create(name="BAAI/bge-small-en-v1.5", )
  ```
</CodeGroup>

This creates a Sentence Transformers embedding function using the BGE model. You can:

* Change `"sentence-transformers"` to other providers like `"openai"`, `"cohere"`, etc.
* Modify the model name for different embedding models
* Set `device="cuda"` for GPU acceleration if available

## Step 4: Define Your Schema

Create a Pydantic model that defines your table structure:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  class Words(LanceModel):
      text: str = model.SourceField()  
      vector: Vector(model.ndims()) = model.VectorField()
  ```
</CodeGroup>

* `SourceField()`: This field will be embedded
* `VectorField()`: This stores the embeddings
* `model.ndims()`: Sets vector dimensions for your model

## Step 5: Create Table and Ingest Data

Create a table with your schema and add data:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  table = db.create_table("words", schema=Words)
  table.add([
      {"text": "hello world"},
      {"text": "goodbye world"}
  ])
  ```
</CodeGroup>

The `table.add()` call automatically:

* Takes the text from each document
* Generates embeddings using your chosen model
* Stores both the original text and the vector embeddings

## Step 6: Query with Automatic Embedding

Note: On LanceDB cloud, automatic query embedding is not supported. You need to pass the embedding vector directly.

Search your data using natural language queries:

<CodeGroup>
  ```python Python icon="python" theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
  query = "greetings"
  actual = table.search(query).limit(1).to_pydantic(Words)[0]
  print(actual.text)
  ```
</CodeGroup>

The search process:

1. Automatically converts your query text to embeddings
2. Finds the most similar vectors in your table
3. Returns the matching documents

## Examples

LanceDB currently supports the via SDKs in [Python, Typescript and Rust](/api-reference/).

<CodeGroup>
  <CodeBlock filename="Python" language="python" icon="python">
    {PyImports}
  </CodeBlock>

  <CodeBlock filename="TypeScript" language="typescript" icon="square-js">
    {TsImports}
  </CodeBlock>
</CodeGroup>

Below are some examples of generating and querying embeddings when using the embedding registry.

<CodeGroup>
  <CodeBlock filename="Python" language="python" icon="python">
    {PyOpenaiEmbeddings}
  </CodeBlock>

  <CodeBlock filename="TypeScript" language="typescript" icon="square-js">
    {TsOpenaiEmbeddings}
  </CodeBlock>
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt