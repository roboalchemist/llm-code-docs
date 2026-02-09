# Source: https://python.langchain.com/docs/integrations/providers/jina/

Jina AI - Docs by LangChain Skip to main content Docs by LangChain home page LangChain + LangGraph Search... ⌘ K
- Ask AI
- GitHub
- Try LangSmith
- Try LangSmith Search... Navigation Jina AI LangChain LangGraph Deep Agents Integrations Learn Reference Contribute
Python

- LangChain integrations
- All providers

##### Popular Providers

- OpenAI
- Anthropic (Claude)
- Google
- AWS (Amazon)
- Hugging Face
- Microsoft
- Ollama
- Groq

##### Integrations by component

- Chat models
- Tools and toolkits
- Middleware
- Retrievers
- Text splitters
- Embedding models
- Vector stores
- Document loaders
- Key-value stores On this page
- Installation and setup
- Chat models
- Embedding models
- Document transformers
- Jina rerank

# Jina AI Copy page Copy page Jina AI is a search AI company. `Jina `helps businesses and developers unlock multimodal data with a better search. For proper compatibility, please ensure you are using the `openai `SDK at version 0.x .

## ​ Installation and setup

- Get a Jina AI API token from here and set it as an environment variable ( `JINA_API_TOKEN `)

## ​ Chat models Copy

```text
`from langchain_community.chat_models import JinaChat `
```

See a usage examples .

## ​ Embedding models You can check the list of available models from here Copy

```text
`from langchain_community.embeddings import JinaEmbeddings `
```

See a usage examples .

## ​ Document transformers

### ​ Jina rerank Copy

```text
`from langchain_community.document_compressors import JinaRerank `
```

See a usage examples . Edit this page on GitHub or file an issue . Connect these docs to Claude, VSCode, and more via MCP for real-time answers.
Was this page helpful?
Yes No ⌘ I Docs by LangChain home page github x linkedin youtube
Resources
Forum Changelog LangChain Academy Trust Center
Company
About Careers Blog github x linkedin youtube Powered by