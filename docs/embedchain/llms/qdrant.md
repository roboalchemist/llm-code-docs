# Source: https://docs.embedchain.ai/components/vector-databases/qdrant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Qdrant

In order to use Qdrant as a vector database, set the environment variables `QDRANT_URL` and `QDRANT_API_KEY` which you can find on [Qdrant Dashboard](https://cloud.qdrant.io/).

<CodeGroup>
  ```python main.py theme={null}
  from embedchain import App

  # load qdrant configuration from yaml file
  app = App.from_config(config_path="config.yaml")
  ```

  ```yaml config.yaml theme={null}
  vectordb:
    provider: qdrant
    config:
      collection_name: my_qdrant_index
  ```
</CodeGroup>

<Snippet file="missing-vector-db-tip.mdx" />
