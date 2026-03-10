# [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#send-s3-data-to-qdrant-vector-store-with-langchain) Send S3 Data to Qdrant Vector Store with LangChain

| Time: 30 min | Level: Beginner |  |  |
| --- | --- | --- | --- |

**Data ingestion into a vector store** is essential for building effective search and retrieval algorithms, especially since nearly 80% of data is unstructured, lacking any predefined format.

In this tutorial, we’ll create a streamlined data ingestion pipeline, pulling data directly from **AWS S3** and feeding it into Qdrant. We’ll dive into vector embeddings, transforming unstructured data into a format that allows you to search documents semantically. Prepare to discover new ways to uncover insights hidden within unstructured data!

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#ingestion-workflow-architecture) Ingestion Workflow Architecture

We’ll set up a powerful document ingestion and analysis pipeline in this workflow using cloud storage, natural language processing (NLP) tools, and embedding technologies. Starting with raw data in an S3 bucket, we’ll preprocess it with LangChain, apply embedding APIs for both text and images and store the results in Qdrant – a vector database optimized for similarity search.

**Figure 1: Data Ingestion Workflow Architecture**

![data-ingestion-beginners-5](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-5.png)

Let’s break down each component of this workflow:

- **S3 Bucket:** This is our starting point—a centralized, scalable storage solution for various file types like PDFs, images, and text.
- **LangChain:** Acting as the pipeline’s orchestrator, LangChain handles extraction, preprocessing, and manages data flow for embedding generation. It simplifies processing PDFs, so you won’t need to worry about applying OCR (Optical Character Recognition) here.
- **Qdrant:** As your vector database, Qdrant stores embeddings and their [payloads](https://qdrant.tech/documentation/concepts/payload/), enabling efficient similarity search and retrieval across all content types.

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#prerequisites) Prerequisites

![data-ingestion-beginners-11](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-11.png)

In this section, you’ll get a step-by-step guide on ingesting data from an S3 bucket. But before we dive in, let’s make sure you’re set up with all the prerequisites:

|  |  |
| --- | --- |
| Sample Data | We’ll use a sample dataset, where each folder includes product reviews in text format along with corresponding images. |
| AWS Account | An active [AWS account](https://aws.amazon.com/free/) with access to S3 services. |
| Qdrant Cloud | A [Qdrant Cloud account](https://cloud.qdrant.io/) with access to the WebUI for managing collections and running queries. |
| LangChain | You will use this [popular framework](https://www.langchain.com/) to tie everything together. |

#### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#supported-document-types) Supported Document Types

The documents used for ingestion can be of various types, such as PDFs, text files, or images. We will organize a structured S3 bucket with folders with the supported document types for testing and experimentation.

#### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#python-environment) Python Environment

Ensure you have a Python environment (Python 3.9 or higher) with these libraries installed:

```python
boto3
langchain-community
langchain
python-dotenv
unstructured
unstructured[pdf]
qdrant_client
fastembed

```

* * *

**Access Keys:** Store your AWS access key, S3 secret key, and Qdrant API key in a .env file for easy access. Here’s a sample `.env` file.

```text
ACCESS_KEY = ""
SECRET_ACCESS_KEY = ""
QDRANT_KEY = ""

```

* * *

## [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#step-1-ingesting-data-from-s3) Step 1: Ingesting Data from S3

![data-ingestion-beginners-9.png](https://qdrant.tech/documentation/examples/data-ingestion-beginners/data-ingestion-9.png)

The LangChain framework makes it easy to ingest data from storage services like AWS S3, with built-in support for loading documents in formats such as PDFs, images, and text files.

To connect LangChain with S3, you’ll use the `S3DirectoryLoader`, which lets you load files directly from an S3 bucket into LangChain’s pipeline.

### [Anchor](https://qdrant.tech/documentation/data-ingestion-beginners/\#example-configuring-langchain-to-load-files-from-s3) Example: Configuring LangChain to Load Files from S3

Here’s how to set up LangChain to ingest data from an S3 bucket:

```python
from langchain_community.document_loaders import S3DirectoryLoader