# Source: https://docs.anyscale.com/rag/quickstart.md

# RAG quickstart on Anyscale

[View Markdown](/rag/quickstart.md)

# RAG quickstart on Anyscale

This guide shows you how to build and scale a production-ready Retrieval-Augmented Generation (RAG) pipeline on Anyscale, from data ingestion and embedding to LLM deployment and evaluation.

## Deploy scalable RAG on Anyscale[​](#deploy "Direct link to Deploy scalable RAG on Anyscale")

Access and use the Anyscale RAG template to deploy production-ready RAG systems that require high availability and scalability. The template provides a comprehensive tutorial that takes you from a basic prototype to a production-grade system.

### Use the Anyscale template[​](#template "Direct link to Use the Anyscale template")

To deploy RAG on Anyscale, follow these steps:

1. Sign up for an [Anyscale account](https://console.anyscale.com/).
2. Navigate to the **Templates** or **Examples** section in the Anyscale console.
3. Find the [Distributed RAG pipeline template](https://console.anyscale.com/template-preview/e2e-rag-deepdive).
4. Click **Launch** to deploy the workspace.
5. Follow the template instructions and customize the deployment for your use case.

The template includes a notebook tutorial series covering the following topics:

| **#** | **Notebook**                         | **Description**                                                                                                                                                                  |
| ----- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | A simple RAG data ingestion pipeline | Build a basic RAG ingestion pipeline using standard libraries such as LangChain and Chroma DB. Learn about fundamental RAG components and identify performance bottlenecks.      |
| 2     | Scaling RAG data ingestion with Ray  | Rebuild the data ingestion pipeline using Ray Data to parallelize document parsing, chunking, and embedding across a multi-node, heterogeneous (CPU and GPU) cluster.            |
| 3     | Deploying LLMs with Ray Serve        | Deploy large open-source models as scalable, OpenAI-compatible API endpoints using Ray Serve LLM.                                                                                |
| 4     | Building the RAG query pipeline      | Connect all components to build a user query pipeline that takes user queries, embeds them, queries the vector store, and passes context to your deployed LLM.                   |
| 5     | Advanced prompt engineering for RAG  | Refine your system to handle real-world complexity, including chat history, citations, and safety filters for ambiguous or malicious queries.                                    |
| 6     | Evaluating RAG                       | Run a simple evaluation loop using online inference to understand why this approach is slow, costly, and can destabilize production services.                                    |
| 7     | Scalable evaluation with Ray Data    | Use Ray Data to run batch-inference evaluations that generate embeddings, retrieve context, and get LLM responses for thousands of test questions in parallel with Ray Data LLM. |

## Additional resources[​](#additional-resources "Direct link to Additional resources")

The following are additional resources for learning about RAG on Anyscale:

* [Building Scalable RAG Pipelines with Ray and Anyscale](https://www.anyscale.com/blog/rag-pipelines-how-to)
* [Why RAG Breaks at Scale | Anyscale Webinar](https://www.youtube.com/watch?v=uTz7Jyunb98)
* [Building RAG-based LLM Applications for Production](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1)
* [RAG at Scale: 10x Cheaper Embedding Computations with Anyscale and Pinecone](https://www.anyscale.com/blog/rag-at-scale-10x-cheaper-embedding-computations-with-anyscale-and-pinecone)
* [Building a RAG Batch Inference Pipeline with Anyscale and Union](https://www.anyscale.com/blog/anyscale-union-batch-inference-pipeline)
