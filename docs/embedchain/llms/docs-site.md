# Source: https://docs.embedchain.ai/components/data-sources/docs-site.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📚 Code Docs website

To add any code documentation website as a loader, use the data\_type as `docs_site`. Eg:

```python  theme={null}
from embedchain import App

app = App()
app.add("https://docs.embedchain.ai/", data_type="docs_site")
app.query("What is Embedchain?")
# Answer: Embedchain is a platform that utilizes various components, including paid/proprietary ones, to provide what is believed to be the best configuration available. It uses LLM (Language Model) providers such as OpenAI, Anthpropic, Vertex_AI, GPT4ALL, Azure_OpenAI, LLAMA2, JINA, Ollama, Together and COHERE. Embedchain allows users to import and utilize these LLM providers for their applications.'
```
