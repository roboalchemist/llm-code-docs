# [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#navigate-your-codebase-with-semantic-search-and-qdrant) Navigate Your Codebase with Semantic Search and Qdrant

| Time: 45 min | Level: Intermediate | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qdrant/examples/blob/master/code-search/code-search.ipynb) |  |
| --- | --- | --- | --- |

You too can enrich your applications with Qdrant semantic search. In this
tutorial, we describe how you can use Qdrant to navigate a codebase, to help
you find relevant code snippets. As an example, we will use the [Qdrant](https://github.com/qdrant/qdrant)
source code itself, which is mostly written in Rust.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#the-approach) The approach

We want to search codebases using natural semantic queries, and searching for code based on similar logic. You can set up these tasks with embeddings:

1. General usage neural encoder for Natural Language Processing (NLP), in our case
`sentence-transformers/all-MiniLM-L6-v2`.
2. Specialized embeddings for code-to-code similarity search. We use the
`jina-embeddings-v2-base-code` model.

To prepare our code for `all-MiniLM-L6-v2`, we preprocess the code to text that
more closely resembles natural language. The Jina embeddings model supports a
variety of standard programming languages, so there is no need to preprocess the
snippets. We can use the code as is.

NLP-based search is based on function signatures, but code search may return
smaller pieces, such as loops. So, if we receive a particular function signature
from the NLP model and part of its implementation from the code model, we merge
the results and highlight the overlap.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#data-preparation) Data preparation

Chunking the application sources into smaller parts is a non-trivial task. In
general, functions, class methods, structs, enums, and all the other language-specific
constructs are good candidates for chunks. They are big enough to
contain some meaningful information, but small enough to be processed by
embedding models with a limited context window. You can also use docstrings,
comments, and other metadata can be used to enrich the chunks with additional
information.

![Code chunking strategy](https://qdrant.tech/documentation/tutorials/code-search/data-chunking.png)

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#parsing-the-codebase) Parsing the codebase

While our example uses Rust, you can use our approach with any other language.
You can parse code with a [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) ( **LSP**)
compatible tool. You can use an LSP to build a graph of the codebase, and then extract chunks.
We did our work with the [rust-analyzer](https://rust-analyzer.github.io/).
We exported the parsed codebase into the [LSIF](https://microsoft.github.io/language-server-protocol/specifications/lsif/0.4.0/specification/)
format, a standard for code intelligence data. Next, we used the LSIF data to
navigate the codebase and extract the chunks. For details, see our [code search\\
demo](https://github.com/qdrant/demo-code-search).

We then exported the chunks into JSON documents with not only the code itself,
but also context with the location of the code in the project. For example, see
the description of the `await_ready_for_timeout` function from the `IsReady`
struct in the `common` module:

```json
{
   "name":"await_ready_for_timeout",
   "signature":"fn await_ready_for_timeout (& self , timeout : Duration) -> bool",
   "code_type":"Function",
   "docstring":"= \" Return `true` if ready, `false` if timed out.\"",
   "line":44,
   "line_from":43,
   "line_to":51,
   "context":{
      "module":"common",
      "file_path":"lib/collection/src/common/is_ready.rs",
      "file_name":"is_ready.rs",
      "struct_name":"IsReady",
      "snippet":"    /// Return `true` if ready, `false` if timed out.\n    pub fn await_ready_for_timeout(&self, timeout: Duration) -> bool {\n        let mut is_ready = self.value.lock();\n        if !*is_ready {\n            !self.condvar.wait_for(&mut is_ready, timeout).timed_out()\n        } else {\n            true\n        }\n    }\n"
   }
}

```

You can examine the Qdrant structures, parsed in JSON, in the [`structures.jsonl`\\
file](https://storage.googleapis.com/tutorial-attachments/code-search/structures.jsonl)
in our Google Cloud Storage bucket. Download it and use it as a source of data for our code search.

```shell
wget https://storage.googleapis.com/tutorial-attachments/code-search/structures.jsonl

```

Next, load the file and parse the lines into a list of dictionaries:

```python
import json

structures = []
with open("structures.jsonl", "r") as fp:
    for i, row in enumerate(fp):
        entry = json.loads(row)
        structures.append(entry)

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#code-to-natural-language-conversion) Code to _natural language_ conversion

Each programming language has its own syntax which is not a part of the natural
language. Thus, a general-purpose model probably does not understand the code
as is. We can, however, normalize the data by removing code specifics and
including additional context, such as module, class, function, and file name.
We took the following steps:

1. Extract the signature of the function, method, or other code construct.
2. Divide camel case and snake case names into separate words.
3. Take the docstring, comments, and other important metadata.
4. Build a sentence from the extracted data using a predefined template.
5. Remove the special characters and replace them with spaces.

As input, expect dictionaries with the same structure. Define a `textify`
function to do the conversion. We’ll use an `inflection` library to convert
with different naming conventions.

```shell
pip install inflection

```

Once all dependencies are installed, we define the `textify` function:

```python
import inflection
import re

from typing import Dict, Any

def textify(chunk: Dict[str, Any]) -> str:
    # Get rid of all the camel case / snake case
    # - inflection.underscore changes the camel case to snake case
    # - inflection.humanize converts the snake case to human readable form
    name = inflection.humanize(inflection.underscore(chunk["name"]))
    signature = inflection.humanize(inflection.underscore(chunk["signature"]))

    # Check if docstring is provided
    docstring = ""
    if chunk["docstring"]:
        docstring = f"that does {chunk['docstring']} "

    # Extract the location of that snippet of code
    context = (
        f"module {chunk['context']['module']} "
        f"file {chunk['context']['file_name']}"
    )
    if chunk["context"]["struct_name"]:
        struct_name = inflection.humanize(
            inflection.underscore(chunk["context"]["struct_name"])
        )
        context = f"defined in struct {struct_name} {context}"

    # Combine all the bits and pieces together
    text_representation = (
        f"{chunk['code_type']} {name} "
        f"{docstring}"
        f"defined as {signature} "
        f"{context}"
    )

    # Remove any special characters and concatenate the tokens
    tokens = re.split(r"\W", text_representation)
    tokens = filter(lambda x: x, tokens)
    return " ".join(tokens)

```

Now we can use `textify` to convert all chunks into text representations:

```python
text_representations = list(map(textify, structures))

```

This is how the `await_ready_for_timeout` function description appears:

```text
Function Await ready for timeout that does Return true if ready false if timed out defined as Fn await ready for timeout self timeout duration bool defined in struct Is ready module common file is_ready rs

```

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#ingestion-pipeline) Ingestion pipeline

Next, we’ll build a pipeline for vectorizing the data and set up a semantic search mechanism for both embedding models.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#building-qdrant-collection) Building Qdrant collection

We use the `qdrant-client` library with the `fastembed` extra to interact with the Qdrant server and generate vector embeddings locally. Let’s install it:

```shell
pip install "qdrant-client[fastembed]"

```

Of course, we need a running Qdrant server for vector search. If you need one,
you can [use a local Docker container](https://qdrant.tech/documentation/quick-start/)
or deploy it using the [Qdrant Cloud](https://cloud.qdrant.io/).
You can use either to follow this tutorial. Configure the connection parameters:

```python
QDRANT_URL = "https://my-cluster.cloud.qdrant.io:6333" # http://localhost:6333 for local instance
QDRANT_API_KEY = "THIS_IS_YOUR_API_KEY" # None for local instance

```

Then use the library to create a collection:

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(QDRANT_URL, api_key=QDRANT_API_KEY)
client.create_collection(
    "qdrant-sources",
    vectors_config={
        "text": models.VectorParams(
            size=client.get_embedding_size(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            ),
            distance=models.Distance.COSINE,
        ),
        "code": models.VectorParams(
            size=client.get_embedding_size(
                model_name="jinaai/jina-embeddings-v2-base-code"
            ),
            distance=models.Distance.COSINE,
        ),
    },
)

```

Our newly created collection is ready to accept the data. Let’s upload the embeddings:

```python
import uuid