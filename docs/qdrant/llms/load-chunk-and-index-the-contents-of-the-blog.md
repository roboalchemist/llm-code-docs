# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

```

### [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#chunking-data) Chunking data

When dealing with large documents, such as a blog post exceeding 42,000 characters, it’s crucial to manage the data efficiently for processing. Many models have a limited context window and struggle with long inputs, making it difficult to extract or find relevant information. To overcome this, the document is divided into smaller chunks. This approach enhances the model’s ability to process and retrieve the most pertinent sections of the document effectively.

In this scenario, the document is split into chunks using the `RecursiveCharacterTextSplitter` with a specified chunk size and overlap. This method ensures that no critical information is lost between chunks. Following the splitting, these chunks are then indexed into Qdrant—a vector database for efficient similarity search and storage of embeddings. The `Qdrant.from_documents` function is utilized for indexing, with documents being the split chunks and embeddings generated through `OpenAIEmbeddings`. The entire process is facilitated within an in-memory database, signifying that the operations are performed without the need for persistent storage, and the collection is named “lilianweng” for reference.

This chunking and indexing strategy significantly improves the management and retrieval of information from large documents, making it a practical solution for handling extensive texts in data processing workflows.

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

vectorstore = Qdrant.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(),
    collection_name="lilianweng",
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
)

```

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#retrieve-and-generate-content) Retrieve and generate content

The `vectorstore` is used as a retriever to fetch relevant documents based on vector similarity. The `hub.pull("rlm/rag-prompt")` function is used to pull a specific prompt from a repository, which is designed to work with retrieved documents and a question to generate a response.

The `format_docs` function formats the retrieved documents into a single string, preparing them for further processing. This formatted string, along with a question, is passed through a chain of operations. Firstly, the context (formatted documents) and the question are processed by the retriever and the prompt. Then, the result is fed into a large language model ( `llm`) for content generation. Finally, the output is parsed into a string format using `StrOutputParser()`.

This chain of operations demonstrates a sophisticated approach to information retrieval and content generation, leveraging both the semantic understanding capabilities of vector search and the generative prowess of large language models.

Now, retrieve and generate data using relevant snippets from the blogL

```python
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

```

### [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#invoking-the-rag-chain) Invoking the RAG Chain

```python
rag_chain.invoke("What is Task Decomposition?")

```

## [Anchor](https://qdrant.tech/documentation/examples/rag-chatbot-scaleway/\#next-steps) Next steps:

We built a solid foundation for a simple chatbot, but there is still a lot to do. If you want to make the
system production-ready, you should consider implementing the mechanism into your existing stack. We recommend

Our vector database can easily be hosted on [Scaleway](https://www.scaleway.com/), our trusted [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) partner. This means that Qdrant can be run from your Scaleway region, but the database itself can still be managed from within Qdrant Cloud’s interface. Both products have been tested for compatibility and scalability, and we recommend their [managed Kubernetes](https://www.scaleway.com/en/kubernetes-kapsule/) service.
Their French deployment regions e.g. France are excellent for network latency and data sovereignty. For hosted GPUs, try [rendering with L4 GPU instances](https://www.scaleway.com/en/l4-gpu-instance/).

If you have any questions, feel free to ask on our [Discord community](https://qdrant.to/discord).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/rag-chatbot-scaleway.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/rag-chatbot-scaleway.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-63-lllmstxt|>
## operator-configuration
- [Documentation](https://qdrant.tech/documentation/)
- [Hybrid cloud](https://qdrant.tech/documentation/hybrid-cloud/)
- Configure the Qdrant Operator