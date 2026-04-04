# Source: https://docs.embedchain.ai/components/vector-databases/opensearch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenSearch

Install related dependencies using the following command:

```bash  theme={null}
pip install --upgrade 'embedchain[opensearch]'
```

<CodeGroup>
  ```python main.py theme={null}
  from embedchain import App

  # load opensearch configuration from yaml file
  app = App.from_config(config_path="config.yaml")
  ```

  ```yaml config.yaml theme={null}
  vectordb:
    provider: opensearch
    config:
      collection_name: 'my-app'
      opensearch_url: 'https://localhost:9200'
      http_auth:
        - admin
        - admin
      vector_dimension: 1536
      use_ssl: false
      verify_certs: false
  ```
</CodeGroup>

<Snippet file="missing-vector-db-tip.mdx" />
