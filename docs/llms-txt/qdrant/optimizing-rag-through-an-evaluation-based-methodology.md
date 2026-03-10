# Optimizing RAG Through an Evaluation-Based Methodology

Atita Arora

·

June 12, 2024

![Optimizing RAG Through an Evaluation-Based Methodology](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/preview/title.jpg)

In today’s fast-paced, information-rich world, AI is revolutionizing knowledge management. The systematic process of capturing, distributing, and effectively using knowledge within an organization is one of the fields in which AI provides exceptional value today.

> The potential for AI-powered knowledge management increases when leveraging [Retrieval Augmented Generation (RAG)](https://qdrant.tech/rag/rag-evaluation-guide/), a methodology that enables LLMs to access a vast, diverse repository of factual information from knowledge stores, such as vector databases.

This process enhances the accuracy, relevance, and reliability of generated text, thereby mitigating the risk of faulty, incorrect, or nonsensical results sometimes associated with traditional LLMs. This method not only ensures that the answers are contextually relevant but also up-to-date, reflecting the latest insights and data available.

While RAG enhances the accuracy, relevance, and reliability of traditional LLM solutions, **an evaluation strategy can further help teams ensure their AI products meet these benchmarks of success.**

## [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#relevant-tools-for-this-experiment) Relevant tools for this experiment

In this article, we’ll break down a RAG Optimization workflow experiment that demonstrates that evaluation is essential to build a successful RAG strategy. We will use Qdrant and Quotient for this experiment.

[Qdrant](https://qdrant.tech/) is a vector database and vector similarity search engine designed for efficient storage and retrieval of high-dimensional vectors. Because Qdrant offers efficient indexing and searching capabilities, it is ideal for implementing RAG solutions, where quickly and accurately retrieving relevant information from extremely large datasets is crucial. Qdrant also offers a wealth of additional features, such as quantization, multivector support and multi-tenancy.

Alongside Qdrant we will use Quotient, which provides a seamless way to evaluate your RAG implementation, accelerating and improving the experimentation process.

[Quotient](https://www.quotientai.co/) is a platform that provides tooling for AI developers to build [evaluation frameworks](https://qdrant.tech/rag/rag-evaluation-guide/) and conduct experiments on their products. Evaluation is how teams surface the shortcomings of their applications and improve performance in key benchmarks such as faithfulness, and semantic similarity. Iteration is key to building innovative AI products that will deliver value to end users.

> 💡 The [accompanying notebook](https://github.com/qdrant/qdrant-rag-eval/tree/master/workshop-rag-eval-qdrant-quotient) for this exercise can be found on GitHub for future reference.

## [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#summary-of-key-findings) Summary of key findings

1. **Irrelevance and Hallucinations**: When the documents retrieved are irrelevant, evidenced by low scores in both Chunk Relevance and Context Relevance, the model is prone to generating inaccurate or fabricated information.
2. **Optimizing Document Retrieval**: By retrieving a greater number of documents and reducing the chunk size, we observed improved outcomes in the model’s performance.
3. **Adaptive Retrieval Needs**: Certain queries may benefit from accessing more documents. Implementing a dynamic retrieval strategy that adjusts based on the query could enhance accuracy.
4. **Influence of Model and Prompt Variations**: Alterations in language models or the prompts used can significantly impact the quality of the generated responses, suggesting that fine-tuning these elements could optimize performance.

Let us walk you through how we arrived at these findings!

## [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#building-a-rag-pipeline) Building a RAG pipeline

To evaluate a RAG pipeline, we will have to build a RAG Pipeline first. In the interest of simplicity, we are building a Naive RAG in this article. There are certainly other versions of RAG :

![shades_of_rag.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/shades_of_rag.png)

The illustration below depicts how we can leverage a [RAG Evaluation framework](https://qdrant.tech/rag/rag-evaluation-guide/) to assess the quality of RAG Application.

![qdrant_and_quotient.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/qdrant_and_quotient.png)

We are going to build a RAG application using Qdrant’s Documentation and the premeditated [hugging face dataset](https://huggingface.co/datasets/atitaarora/qdrant_doc).
We will then assess our RAG application’s ability to answer questions about Qdrant.

To prepare our knowledge store we will use Qdrant, which can be leveraged in 3 different ways as below :

```python
client = qdrant_client.QdrantClient(
    os.environ.get("QDRANT_URL"),
    api_key=os.environ.get("QDRANT_API_KEY"),
)

```

We will be using [Qdrant Cloud](https://cloud.qdrant.io/login) so it is a good idea to provide the `QDRANT_URL` and `QDRANT_API_KEY` as environment variables for easier access.

Moving on, we will need to define the collection name as :

```python
COLLECTION_NAME = "qdrant-docs-quotient"

```

In this case , we may need to create different collections based on the experiments we conduct.

To help us provide seamless embedding creations throughout the experiment, we will use Qdrant’s own embeddings library [Fastembed](https://qdrant.github.io/fastembed/) which supports [many different models](https://qdrant.github.io/fastembed/examples/Supported_Models/) including dense as well as sparse vector models.

Before implementing RAG, we need to prepare and index our data in Qdrant.

This involves converting textual data into vectors using a suitable encoder (e.g., sentence transformers), and storing these vectors in Qdrant for retrieval.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document as LangchainDocument

## Load the dataset with qdrant documentation
dataset = load_dataset("atitaarora/qdrant_doc", split="train")

## Dataset to langchain document
langchain_docs = [\
    LangchainDocument(page_content=doc["text"], metadata={"source": doc["source"]})\
    for doc in dataset\
]

len(langchain_docs)

#Outputs
#240

```

You can preview documents in the dataset as below :

```python
## Here's an example of what a document in our dataset looks like
print(dataset[100]['text'])

```

## [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#evaluation-dataset) Evaluation dataset

To measure the quality of our RAG setup, we will need a representative evaluation dataset. This dataset should contain realistic questions and the expected answers.

Additionally, including the expected contexts for which your RAG pipeline is designed to retrieve information would be beneficial.

We will be using a [prebuilt evaluation dataset](https://huggingface.co/datasets/atitaarora/qdrant_doc_qna).

If you are struggling to make an evaluation dataset for your use case , you can use your documents and some techniques described in this [notebook](https://github.com/qdrant/qdrant-rag-eval/blob/master/synthetic_qna/notebook/Synthetic_question_generation.ipynb)

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#building-the-rag-pipeline) Building the RAG pipeline

We establish the data preprocessing parameters essential for the RAG pipeline and configure the Qdrant vector database according to the specified criteria.

Key parameters under consideration are:

- **Chunk size**
- **Chunk overlap**
- **Embedding model**
- **Number of documents retrieved (retrieval window)**

Following the ingestion of data in Qdrant, we proceed to retrieve pertinent documents corresponding to each query. These documents are then seamlessly integrated into our evaluation dataset, enriching the contextual information within the designated **`context`** column to fulfil the evaluation aspect.

Next we define methods to take care of logistics with respect to adding documents to Qdrant

```python
import uuid

from qdrant_client import models

def add_documents(client, collection_name, chunk_size, chunk_overlap, embedding_model_name):
    """
    This function adds documents to the desired Qdrant collection given the specified RAG parameters.
    """

    ## Processing each document with desired TEXT_SPLITTER_ALGO, CHUNK_SIZE, CHUNK_OVERLAP
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
        separators=["\n\n", "\n", ".", " ", ""],
    )

    docs_processed = []
    for doc in langchain_docs:
        docs_processed += text_splitter.split_documents([doc])

    ## Processing documents to be encoded by Fastembed
    docs_contents = []
    docs_metadatas = []

    for doc in docs_processed:
        if hasattr(doc, 'page_content') and hasattr(doc, 'metadata'):
            docs_contents.append(doc.page_content)
            docs_metadatas.append(doc.metadata)
        else:
            # Handle the case where attributes are missing
            print("Warning: Some documents do not have 'page_content' or 'metadata' attributes.")

    print("processed: ", len(docs_processed))
    print("content: ", len(docs_contents))
    print("metadata: ", len(docs_metadatas))

    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
        )

    client.upsert(
        collection_name=collection_name,
        points=[\
            models.PointStruct(\
                id=uuid.uuid4().hex,\
                vector=models.Document(text=content, model=embedding_model_name),\
                payload={"metadata": metadata, "document": content},\
            )\
            for metadata, content in zip(docs_metadatas, docs_contents)\
        ],
    )

```

and retrieving documents from Qdrant during our RAG Pipeline assessment.

```python
def get_documents(collection_name, query, num_documents=3):
    """
    This function retrieves the desired number of documents from the Qdrant collection given a query.
    It returns a list of the retrieved documents.
    """
    search_results = client.query_points(
        collection_name=collection_name,
        query=models.Document(text=query, model=embedding_model_name),
        limit=num_documents,
    ).points

    results = [r.payload["document"] for r in search_results]
    return results

```

### [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#setting-up-quotient) Setting up Quotient

You will need an account log in, which you can get by requesting access on [Quotient’s website](https://www.quotientai.co/). Once you have an account, you can create an API key by running the `quotient authenticate` CLI command.

**Once you have your API key, make sure to set it as an environment variable called `QUOTIENT_API_KEY`**

```python