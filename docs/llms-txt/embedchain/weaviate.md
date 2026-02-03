# Source: https://docs.embedchain.ai/components/vector-databases/weaviate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Weaviate

In order to use Weaviate as a vector database, set the environment variables `WEAVIATE_ENDPOINT` and `WEAVIATE_API_KEY` which you can find on [Weaviate dashboard](https://console.weaviate.cloud/dashboard).

<CodeGroup>
  ```python main.py theme={null}
  from embedchain import App

  # load weaviate configuration from yaml file
  app = App.from_config(config_path="config.yaml")
  ```

  ```yaml config.yaml theme={null}
  vectordb:
    provider: weaviate
    config:
      collection_name: my_weaviate_index
  ```
</CodeGroup>

<Snippet file="missing-vector-db-tip.mdx" />
