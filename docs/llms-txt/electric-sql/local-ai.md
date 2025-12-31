# Source: https://electric-sql.com/use-cases/local-ai.md

---
url: /use-cases/local-ai.md
description: >-
  Sync data for local AI from your existing business systems. For zero latency
  retrieval and zero inference cost.
---

## Low-latency data retrieval for local RAG

Local AI applications are apps that run AI models locally. Local AI models need context data. Especially for retrieval-augmented generation (RAG):

![]()

### Latency and UX

Retrieving data adds latency to the AI experience. For example, if you're making a voice agent and you have high latency, it feels like an old satellite phone call, with lots of delays and talking over each other.

### Inference latency

There are two ways to reduce AI latency:

* reducing **inference latency** — how long the model takes
* reducing **data latency** — how long context retrieval takes

Reducing inference latency is complex and expensive.

### Data latency

This is why having local data, on device, for the local AI to use as context data, is so important. Because local data avoids network latency when retrieving data.

### Live local data

If you have local data, you need to keep it live, just like you do for a [local cache](/use-cases/cache-invalidation).

For example, if you use LangChain to load a data corpus, it's static. The context data is stale and can easily go out of date.

### Relational systems

Live data for most business applications lives in a relational database like Postgres. So the challenge is how to connect the AI to live, local, relational data.

## Electric sync

Electric provides live data retrieval for local RAG applications, using hybrid vector-relational sync, from your existing Postgres systems.

### Live data retrieval

Using Electric, you can sync live data, locally, for low-latency retrieval.

![](/img/use-cases/local-rag-workflow.png)

Electric's [Shapes](/docs/guides/shapes) allow you to sync the right data onto the local device. This controls the shape of the local knowledge base. This allows your model to find the right context data for the prompt, with context discovery across the relational data model.

You can then feed the context data it into the model in the best way and distill the results to maximise model performance. Because the data is synced locally, you eliminate network latency from the data retrieval time.

### Hybrid vector-relational sync

Electric syncs data from Postgres into local data stores, including [PGlite](/product/pglite). Postgres and PGlite both support [pgvector](https://github.com/pgvector/pgvector).

This allows you to sync vector and relational data in the same data model. So rather than having one structured / relational store and one vector database, you can combine the two to build semantic search and other AI experiences that run directly off your live transactional data.

## Example

### Low-latency RAG with Intel AI PC

Electric collaborated with Intel to build a ultra-low-latency local RAG stack, using hybrid-vector relational sync with Intel's hardware acceleration for local LLMs.

## Next steps

Get in touch if you're interested in exploring local AI applications with Electric.
