# setting embed_model to Jina and llm model to Mixtral
from llama_index.core import Settings
Settings.embed_model = jina_embedding_model
Settings.llm = mixtral_llm

from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client

client = qdrant_client.QdrantClient(
    url=os.getenv("QDRANT_HOST"),
    api_key=os.getenv("QDRANT_API_KEY")
)

vector_store = QdrantVectorStore(
    client=client, collection_name="demo", enable_hybrid=True, batch_size=20
)
Settings.chunk_size = 512

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents=llama_parse_documents,
    storage_context=storage_context
)

```

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#prepare-a-prompt) Prepare a prompt

Here we will create a custom prompt template. This prompt asks the LLM to use only the context information retrieved from Qdrant. When querying with hybrid mode, we can set `similarity_top_k` and `sparse_top_k` separately:

- `sparse_top_k` represents how many nodes will be retrieved from each dense and sparse query.
- `similarity_top_k` controls the final number of returned nodes. In the above setting, we end up with 10 nodes.

Then, we assemble the query engine using the prompt.

```python
from llama_index.core import PromptTemplate

qa_prompt_tmpl = (
    "Context information is below.\n"
    "-------------------------------"
    "{context_str}\n"
    "-------------------------------"
    "Given the context information and not prior knowledge,"
    "answer the query. Please be concise, and complete.\n"
    "If the context does not contain an answer to the query,"
    "respond with \"I don't know!\"."
    "Query: {query_str}\n"
    "Answer: "
)
qa_prompt = PromptTemplate(qa_prompt_tmpl)

from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer
from llama_index.core import Settings
Settings.embed_model = jina_embedding_model
Settings.llm = mixtral_llm