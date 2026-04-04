# Source: https://docs.pinecone.io/troubleshooting/pinecone-attribute-errors-with-langchain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# PineconeAttribute errors with LangChain

## Problem

When using an outdated version of LangChain, you may encounter errors like the following:

```console  theme={null}
Pinecone has no attribute 'from_texts'
```

```console  theme={null}
Pinecone has no attribute `from_documents'
```

## Solution

Previously, the Python classes for both LangChain and Pinecone had objects named `Pinecone`, but this is no longer an issue in the latest LangChain version. To resolve these errors, upgrade LangChain to >=0.0.3:

```shell  theme={null}
pip install --upgrade langchain-pinecone
```

Depending on which version of LangChain you are upgrading from, you may need to update your code. You can find more information about using LangChain with Pinecone in our [documentation](/integrations/langchain#4-initialize-a-langchain-vector-store).
