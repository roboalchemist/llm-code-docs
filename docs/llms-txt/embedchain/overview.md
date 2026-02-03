# Source: https://docs.embedchain.ai/components/data-sources/overview.md

# Source: https://docs.embedchain.ai/api-reference/app/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# App

Create a RAG app object on Embedchain. This is the main entrypoint for a developer to interact with Embedchain APIs. An app configures the llm, vector database, embedding model, and retrieval strategy of your choice.

### Attributes

<ParamField path="local_id" type="str">
  App ID
</ParamField>

<ParamField path="name" type="str" optional>
  Name of the app
</ParamField>

<ParamField path="config" type="BaseConfig">
  Configuration of the app
</ParamField>

<ParamField path="llm" type="BaseLlm">
  Configured LLM for the RAG app
</ParamField>

<ParamField path="db" type="BaseVectorDB">
  Configured vector database for the RAG app
</ParamField>

<ParamField path="embedding_model" type="BaseEmbedder">
  Configured embedding model for the RAG app
</ParamField>

<ParamField path="chunker" type="ChunkerConfig">
  Chunker configuration
</ParamField>

<ParamField path="client" type="Client" optional>
  Client object (used to deploy an app to Embedchain platform)
</ParamField>

<ParamField path="logger" type="logging.Logger">
  Logger object
</ParamField>

## Usage

You can create an app instance using the following methods:

### Default setting

```python Code Example theme={null}
from embedchain import App
app = App()
```

### Python Dict

```python Code Example theme={null}
from embedchain import App

config_dict = {
  'llm': {
    'provider': 'gpt4all',
    'config': {
      'model': 'orca-mini-3b-gguf2-q4_0.gguf',
      'temperature': 0.5,
      'max_tokens': 1000,
      'top_p': 1,
      'stream': False
    }
  },
  'embedder': {
    'provider': 'gpt4all'
  }
}

# load llm configuration from config dict
app = App.from_config(config=config_dict)
```

### YAML Config

<CodeGroup>
  ```python main.py theme={null}
  from embedchain import App

  # load llm configuration from config.yaml file
  app = App.from_config(config_path="config.yaml")
  ```

  ```yaml config.yaml theme={null}
  llm:
    provider: gpt4all
    config:
      model: 'orca-mini-3b-gguf2-q4_0.gguf'
      temperature: 0.5
      max_tokens: 1000
      top_p: 1
      stream: false

  embedder:
    provider: gpt4all
  ```
</CodeGroup>

### JSON Config

<CodeGroup>
  ```python main.py theme={null}
  from embedchain import App

  # load llm configuration from config.json file
  app = App.from_config(config_path="config.json")
  ```

  ```json config.json theme={null}
  {
    "llm": {
      "provider": "gpt4all",
      "config": {
        "model": "orca-mini-3b-gguf2-q4_0.gguf",
        "temperature": 0.5,
        "max_tokens": 1000,
        "top_p": 1,
        "stream": false
      }
    },
    "embedder": {
      "provider": "gpt4all"
    }
  }
  ```
</CodeGroup>
