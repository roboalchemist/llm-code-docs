# Implementing semantic search with LangChain
Source: https://www.meilisearch.com/docs/guides/langchain

This guide shows you how to implement semantic search using LangChain and similarity search.

In this guide, you’ll use OpenAI’s text embeddings to measure the similarity between document properties. Then, you’ll use the LangChain framework to seamlessly integrate Meilisearch and create an application with semantic search.

## Requirements

This guide assumes a basic understanding of Python and LangChain. Beginners to LangChain will still find the tutorial accessible.

* Python (LangChain requires >= 3.8.1 and \< 4.0) and the pip CLI
* A [Meilisearch >= 1.6 project](/learn/getting_started/cloud_quick_start)
* An [OpenAI API key](https://platform.openai.com/account/api-keys)

## Creating the application

Create a folder for your application with an empty `setup.py` file.

Before writing any code, install the necessary dependencies:

```bash theme={null}
pip install langchain openai meilisearch python-dotenv
```

First create a .env to store our credentials:

```