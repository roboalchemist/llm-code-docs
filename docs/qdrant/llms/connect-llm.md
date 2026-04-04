# connect LLM
from llama_index.llms.huggingface import HuggingFaceInferenceAPI

mixtral_llm = HuggingFaceInferenceAPI(
    model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1",
    token=os.getenv("HF_INFERENCE_API_KEY"),
)

```

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#prepare-data-for-rag) Prepare data for RAG

This example will use household appliance manuals, which are generally available as PDF documents.
LlamaPar
In the `data` folder, we have three documents, and we will use it to extract the textual content from the PDF and use it as a knowledge base in a simple RAG.

The free LlamaIndex Cloud plan is sufficient for our example:

```python
import nest_asyncio
nest_asyncio.apply()
from llama_parse import LlamaParse

llamaparse_api_key = os.getenv("LLAMA_CLOUD_API_KEY")

llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data([\
    "data/DJ68-00682F_0.0.pdf",\
    "data/F500E_WF80F5E_03445F_EN.pdf",\
    "data/O_ME4000R_ME19R7041FS_AA_EN.pdf"\
])

```

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#store-data-into-qdrant) Store data into Qdrant

The code below does the following:

- create a vector store with Qdrant client;
- get an embedding for each chunk using Jina Embeddings API;
- combines `sparse` and `dense` vectors for hybrid search;
- stores all data into Qdrant;

Hybrid search with Qdrant must be enabled from the beginning - we can simply set `enable_hybrid=True`.

```python