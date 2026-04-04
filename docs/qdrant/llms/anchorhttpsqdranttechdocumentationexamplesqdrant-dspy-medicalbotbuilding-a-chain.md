# [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#building-a-chain-of-thought-medical-chatbot-with-qdrant-and-dspy) Building a Chain-of-Thought Medical Chatbot with Qdrant and DSPy

Accessing medical information from LLMs can lead to hallucinations or outdated information. Relying on this type of information can result in serious medical consequences. Building a trustworthy and context-aware medical chatbot can solve this.

In this article, we will look at how to tackle these challenges using:

- **Retrieval-Augmented Generation (RAG)**: Instead of answering the questions from scratch, the bot retrieves the information from medical literature before answering questions.
- **Filtering**: Users can filter the results by specialty and publication year, ensuring the information is accurate and up-to-date.

Let’s discover the technologies needed to build the medical bot.

## [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#tech-stack-overview) Tech Stack Overview

To build a robust and trustworthy medical chatbot, we will combine the following technologies:

- [**Qdrant Cloud**](https://qdrant.tech/cloud/): Qdrant is a high-performance vector search engine for storing and retrieving large collections of embeddings. In this project, we will use it to enable fast and accurate search across millions of medical documents, supporting dense and multi-vector (ColBERT) retrieval for context-aware answers.
- [**Stanford DSPy**](https://qdrant.tech/documentation/frameworks/dspy/) **:** DSPy is the AI framework we will use to obtain the final answer. It allows the medical bot to retrieve the relevant information and reason step-by-step to produce accurate and explainable answers.

![medicalbot flow chart](https://qdrant.tech/articles_data/Qdrant-DSPy-medicalbot/medicalbot.png)

## [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#dataset-preparation-and-indexing) Dataset Preparation and Indexing

A medical chatbot is only as good as the knowledge it has access to. For this project, we will leverage the [MIRIAD medical dataset](https://huggingface.co/datasets/miriad/miriad-5.8M), a large-scale collection of medical passages enriched with metadata such as publication year and specialty.

### [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#indexing-with-dense-and-colbert-multivectors) Indexing with Dense and ColBERT Multivectors

To enable high-quality retrieval, we will embed each medical passage with two models:

- **Dense Embeddings**: These are generated using the `BAAI/bge-small-en` model and capture the passages’ general semantic meaning.
- **ColBERT Multivectors**: These provide more fine-grained representations, enabling precise ranking of results.

```python
dense_documents = [\
    models.Document(text=doc, model="BAAI/bge-small-en") for doc in ds["passage_text"]\
]

colbert_documents = [\
    models.Document(text=doc, model="colbert-ir/colbertv2.0")\
    for doc in ds["passage_text"]\
]

collection_name = "miriad"