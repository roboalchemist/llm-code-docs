# Source: https://upstash.com/docs/vector/integrations/langflow.md

# Langflow with Upstash Vector

Langflow provides an intuitive, visual interface to design LLM workflows. You can seamlessly integrate Upstash Vector into your Langflow projects to enable vector-based semantic search and context retrieval.

<Frame>
  <img src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=ea87c9c85e8f1056936977926f733bfa" data-og-width="3010" width="3010" data-og-height="938" height="938" data-path="img/vector/integrations/langflow/final-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=d0936f6c197eaa5a2b269c615d76aacc 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=3febb6b3efad45baefe89f27f6473ff7 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=1e0a279e78bf1bd2faa1cd2f639b8000 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=931c8710ec67580a5a0c1572bc927fc8 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=e7f63e844cfa54de57408b5a35060913 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8f31bc3e9a675d386beaeb5dad53620c 2500w" />
</Frame>

## Install

To get started, install Langflow and Upstash Vector locally or use the Langflow dashboard from [DataStax](https://www.datastax.com/products/langflow). For local installation, run:

```bash  theme={"system"}
pip install langflow upstash-vector
```

## Usage

### Creating an Upstash Vector Index

Visit the [Upstash Console](https://console.upstash.com/vector) to create a vector index. To learn more about index creation, you can check out [this page](https://docs.upstash.com/vector/overall/getstarted).

### Adding Upstash Vector to Langflow

In Langflow, you can integrate Upstash Vector for document indexing and semantic search. Use the following steps:

1. Create a workflow with the **File**, **Split**, and **Upstash** components to process and store documents in the Upstash Vector index.
2. Perform a vector search by connecting the **Upstash** component to your query input.

<Frame>
  <img src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/insert-workflow.png?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=a4bc2af35c8ad7c2108ea300dd8c4b43" data-og-width="2228" width="2228" data-og-height="1308" height="1308" data-path="img/vector/integrations/langflow/insert-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/insert-workflow.png?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=06f0d1a70ba3c7aa02c8ad47f56b3bfa 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/insert-workflow.png?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=7524fba40a0ec5b3bfb564a2d021ac69 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/insert-workflow.png?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8a6d5d6246e66739ca377c731fd2909e 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/insert-workflow.png?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c133b9d44f1f18161d0d454e71b18907 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/insert-workflow.png?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=a7449fc8666288a9d6d09e62aecbe78d 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/insert-workflow.png?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c5b7fe0f66bc88e3dbddbd09b4a1bd61 2500w" />
</Frame>

### Example Workflow

Enhance your chatbot by combining Langflow’s OpenAI integration with Upstash Vector. Create a RAG workflow to retrieve relevant context from your index and use it to answer user queries.

<Frame>
  <img src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=ea87c9c85e8f1056936977926f733bfa" data-og-width="3010" width="3010" data-og-height="938" height="938" data-path="img/vector/integrations/langflow/final-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=d0936f6c197eaa5a2b269c615d76aacc 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=3febb6b3efad45baefe89f27f6473ff7 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=1e0a279e78bf1bd2faa1cd2f639b8000 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=931c8710ec67580a5a0c1572bc927fc8 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=e7f63e844cfa54de57408b5a35060913 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/integrations/langflow/final-workflow.png?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8f31bc3e9a675d386beaeb5dad53620c 2500w" />
</Frame>

## Learn More

For a detailed guide on building a RAG chatbot with Langflow and Upstash Vector, check out this [blog post](https://upstash.com/blog/langflow-upstash-vector).
