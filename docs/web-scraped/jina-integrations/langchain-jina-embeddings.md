# Source: https://python.langchain.com/docs/integrations/text_embedding/jina/

Jina - Docs by LangChain Skip to main content Docs by LangChain home page LangChain + LangGraph Search... ⌘ K
- Ask AI
- GitHub
- Try LangSmith
- Try LangSmith Search... Navigation Jina LangChain LangGraph Deep Agents Integrations Learn Reference Contribute
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
- Embed text and queries with jina embedding models through JinaAI API
- Embed images and queries with jina CLIP through JinaAI API

# Jina Copy page Copy page You can check the list of available models from here .

## ​ Installation and setup Install requirements Copy

```text
`pip install - U langchain - community `
```

Import libraries Copy

```text
`import requests from langchain_community.embeddings import JinaEmbeddings from numpy import dot from numpy.linalg import norm from PIL import Image `
```

## ​ Embed text and queries with jina embedding models through JinaAI API Copy

```text
`text_embeddings = JinaEmbeddings( jina_api_key = "jina_*" , model_name = "jina-embeddings-v2-base-en" ) `
```

Copy

```text
`text = "This is a test document." `
```

Copy

```text
`query_result = text_embeddings.embed_query(text) `
```

Copy

```text
`print (query_result) `
```

Copy

```text
`doc_result = text_embeddings.embed_documents([text]) `
```

Copy

```text
`print (doc_result) `
```

## ​ Embed images and queries with jina CLIP through JinaAI API Copy

```text
`multimodal_embeddings = JinaEmbeddings( jina_api_key = "jina_*" , model_name = "jina-clip-v1" ) `
```

Copy

```text
`image = "https://avatars.githubusercontent.com/u/126733545?v=4" description = "Logo of a parrot and a chain on green background" im = Image.open(requests.get(image, stream = True ).raw) print ( "Image:" ) display(im) `
```

Copy

```text
`image_result = multimodal_embeddings.embed_images([image]) `
```

Copy

```text
`print (image_result) `
```

Copy

```text
`description_result = multimodal_embeddings.embed_documents([description]) `
```

Copy

```text
`print (description_result) `
```

Copy

```text
`cosine_similarity = dot(image_result[ 0 ], description_result[ 0 ]) / ( norm(image_result[ 0 ]) * norm(description_result[ 0 ]) ) `
```

Copy

```text
`print (cosine_similarity) `
```

Edit this page on GitHub or file an issue . Connect these docs to Claude, VSCode, and more via MCP for real-time answers.
Was this page helpful?
Yes No ⌘ I Docs by LangChain home page github x linkedin youtube
Resources
Forum Changelog LangChain Academy Trust Center
Company
About Careers Blog github x linkedin youtube Powered by