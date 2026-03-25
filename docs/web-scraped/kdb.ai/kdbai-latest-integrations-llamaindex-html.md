# Source: https://code.kx.com/kdbai/latest/integrations/llamaindex.html

Title: KDB.AI LlamaIndex - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/integrations/llamaindex.html

Markdown Content:
_This page explains how to integrate KDB.AI with LlamaIndex._

The KDB.AI integration with LlamaIndex enhances your Large Language Model (LLM) applications with data scalability, flexibility, and efficient storage. This allows you to build robust, data-augmented applications that significantly improve decision making and user engagement.

LlamaIndex (GPT Index) is a data framework for LLM applications. Building with LlamaIndex typically involves working with LlamaIndex core and a chosen set of integrations (or plugins). - [LlamaIndex GitLab Repository](https://github.com/run-llama/llama_index)

LlamaIndex provides the following tools:

*   **Data connectors** that allow you to ingest data from various sources and formats (PDFs, APIs, SQL).
*   **Data indexes** that are both easy to work with and performant for large language models (LLMs) to consume.
*   **Advanced retrieval/query interface**; feed in LLM input prompts to get back human-like, knowledge-augmented.
*   **Data agents** that enhance your data processing capabilities and easily integrate with other application frameworks, such as [Docker](https://www.docker.com/), [LangChain](https://www.langchain.com/), [Flask](https://flask.palletsprojects.com/), or [ChatGPT](https://openai.com/chatgpt/).

Advanced RAG capabilities
-------------------------

Applications referred to as Retrieval-Augmented Generation (RAG) systems leverage LlamaIndex to enhance text generation accuracy.

You can use the integration between KDB.AI and LlamaIndex to:

*   Create data-augmented chatbots
*   Index knowledge bases and task lists
*   Query structured data warehouse using natural language interfaces

This efficient exploration and analysis of data makes it easier to extract valuable insights.

Now let's explore a few advanced RAG capabilities you can use with KDB.AI and LlamaIndex:

1.   Multi-modality - process images and audio in addition to unstructured text.

2.   Hybrid search - combine [dense](https://code.kx.com/kdbai/latest/reference/hybrid.html#dense-vectors) and [sparse vector](https://code.kx.com/kdbai/latest/reference/hybrid.html#sparse-vectors) searches, [tokenization](https://code.kx.com/kdbai/latest/reference/hybrid.html#tokenization) and the [Best Matching 25 (BM25)](https://code.kx.com/kdbai/latest/reference/hybrid.html#the-best-matching-25-bm25-algorithm) algorithm.

3.   Sub question query engine - decompose a question into multiple sub-questions that can be searched across separate data sources.

### 1. Multi-modality

This feature helps you reduce an AI model's reliance on a single type of data. For example, instead of searching just text, or pictures, or videos, you can search both pictures and text. Use it to enhance accuracy and reliability, broaden the range of your applications' scope and make outcomes contextually more relevant.

Follow the steps in our sample [Multi-modality notebook](https://github.com/KxSystems/kdbai-samples/blob/main/LlamaIndex_samples/Multimodal_RAG_LLamaIndex_CLIP_KDBAI.ipynb) or run it in [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/LlamaIndex_samples/Multimodal_RAG_LLamaIndex_CLIP_KDBAI.ipynb).

### 2. Hybrid search

[Hybrid search](https://code.kx.com/kdbai/latest/reference/hybrid.html) combines multiple search algorithms to improve the accuracy and relevance of the results. In KDB.AI, hybrid search leverages the power of keyword and semantic searches by combining sparse vectors with dense vectors.

Follow the steps in our sample [Hybrid search notebook](https://github.com/KxSystems/kdbai-samples/blob/main/LlamaIndex_samples/Hybrid_Search_LlamaIndex_KDBAI.ipynb) or run it in [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/LlamaIndex_samples/Hybrid_Search_LlamaIndex_KDBAI.ipynb).

### 3. Sub question query engine

This feature allows customers to decompose a question into multiple sub-questions that can be searched across separate data sources. You'll find this particularly useful when dealing with large datasets or databases, improving both the efficiency and quality of results.

Follow the steps in our sample [Sub question query engine notebook](https://github.com/KxSystems/kdbai-samples/blob/main/LlamaIndex_samples/Sub_Question_Query_Engine_LlamaIndex_KDBAI.ipynb) or run it in [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/LlamaIndex_samples/Sub_Question_Query_Engine_LlamaIndex_KDBAI.ipynb).

If you need help with the integration, feel free to reach out to the KDB.AI [Slack community](http://kx.com/slack) or email [support@kdb.ai](mailto:support@kdb.ai).

Next steps
----------

For more details about KDB.AI and LlamaIndex, check out the following resources:

*   LlamaIndex [GitHub repository](https://github.com/run-llama/llama_index) and [Sample notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/vector_stores/KDBAI_Advanced_RAG_Demo.ipynb).
*   LlamaIndex and KDB.AI Advanced RAG samples in the [KX GitHub repository](https://github.com/KxSystems/kdbai-samples/tree/main/LlamaIndex_advanced_RAG).
*   Advanced RAG with temporal filters [Sample notebook](https://github.com/KxSystems/kdbai-samples/blob/main/LlamaIndex_advanced_RAG/KDBAI_Advanced_RAG_Demo.ipynb) that you can run [Google Colab](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/LlamaIndex_advanced_RAG/KDBAI_Advanced_RAG_Demo.ipynb).
*   Blog post titled [Build RAG-enabled applications with LlamaIndex and KDB.AI](https://kx.com/blog/build-rag-enabled-applications-with-llamaindex-and-kdb-ai/).
