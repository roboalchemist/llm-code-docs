# Source: https://docs.pinecone.io/reference/architecture/assistant-architecture.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Pinecone Assistant architecture

This page describes the architecture for [Pinecone Assistant](/guides/assistant/overview).

## Overview

[Pinecone Assistant](/guides/assistant/overview) runs as a managed service on the Pinecone platform. It uses a combination of machine learning models and information retrieval techniques to provide responses that are informed by your documents. The assistant is designed to be easy to use, requiring minimal setup and no machine learning expertise.

Pinecone Assistant simplifies complex tasks like data chunking, vector search, embedding, and querying while ensuring privacy and security.

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fac1ffcff3fc58b8c48abb41070f76bd" data-og-width="1520" width="1520" data-og-height="1320" height="1320" data-path="images/assistant-architecture_light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=da402176da803658c8ffbdda0287e1d8 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=05a4da048111f0f38a919f39252e2cc1 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=47eb95307afaca43eea69a8914f52ec1 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=96dfe1589dda495073c114a8fc01b9fd 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=1bc84f97b47498ae2ab7c6969c4ab37d 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_light.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=52df04932cfe358add8585cdbfcca0f4 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=52f8183973f02f2f1eb8f88d929035c8" data-og-width="1520" width="1520" data-og-height="1320" height="1320" data-path="images/assistant-architecture_dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6f77677652e9e12a46ad36facc47c8e4 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c51b5d995b5f8c5125a7f3f1bbd12995 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9d1740644d873ac940d8fb5340c9becb 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=cdfa4ba7f3ae803cdcdd807455cfb165 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c431d99fde890a6f016b06ae1a7f985f 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/assistant-architecture_dark.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3c4cbac2096c93879d340740a731d119 2500w" />

## Data ingestion

When a [document is uploaded](/guides/assistant/manage-files), the assistant processes the content by chunking it into smaller parts and generating [vector embeddings](https://www.pinecone.io/learn/vector-embeddings-for-developers/) for each chunk. These embeddings are stored in an [index](/guides/index-data/indexing-overview), making them ready for retrieval.

## Data retrieval

During a [chat](/guides/assistant/chat-with-assistant), the assistant processes the message to formulate relevant search queries, which are used to query the index and identify the most relevant chunks from the uploaded content.

## Response generation

After retrieving these chunks, the assistant performs a ranking step to determine which information is most relevant. This [context](/guides/assistant/context-snippets-overview), along with the chat history and [assistant instructions](/guides/assistant/manage-assistants#add-instructions-to-an-assistant), is then used by a large language model (LLM) to generate responses that are informed by your documents.
