# Source: https://docs.embedchain.ai/components/vector-databases/chromadb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ChromaDB

<CodeGroup>
  ```python main.py theme={null}
  from embedchain import App

  # load chroma configuration from yaml file
  app = App.from_config(config_path="config1.yaml")
  ```

  ```yaml config1.yaml theme={null}
  vectordb:
    provider: chroma
    config:
      collection_name: 'my-collection'
      dir: db
      allow_reset: true
  ```

  ```yaml config2.yaml theme={null}
  vectordb:
    provider: chroma
    config:
      collection_name: 'my-collection'
      host: localhost
      port: 5200
      allow_reset: true
  ```
</CodeGroup>

<Snippet file="missing-vector-db-tip.mdx" />
