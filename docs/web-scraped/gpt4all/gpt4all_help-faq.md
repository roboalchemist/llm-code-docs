# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_help/faq.html

---

[ ![logo](../assets/nomic.png) ](../index.html "GPT4All") GPT4All

[ nomic-ai/gpt4all  ](https://github.com/nomic-ai/gpt4all "Go to repository")

  * [ GPT4All Documentation  ](../index.html)
  * [ Quickstart  ](../gpt4all_desktop/quickstart.html)
  * [ Chats  ](../gpt4all_desktop/chats.html)
  * [ Models  ](../gpt4all_desktop/models.html)
  * [ LocalDocs  ](../gpt4all_desktop/localdocs.html)
  * [ Settings  ](../gpt4all_desktop/settings.html)
  * [ Chat Templates  ](../gpt4all_desktop/chat_templates.html)
  * Cookbook  Cookbook 
    * [ Local AI Chat with Microsoft Excel  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-microsoft-excel.html)
    * [ Local AI Chat with your Google Drive  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-google-drive.html)
    * [ Local AI Chat with your Obsidian Vault  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-Obsidian.html)
    * [ Local AI Chat with your OneDrive  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-One-Drive.html)
  * API Server  API Server 
    * [ GPT4All API Server  ](../gpt4all_api_server/home.html)
  * Python SDK  Python SDK 
    * [ GPT4All Python SDK  ](../gpt4all_python/home.html)
    * [ Monitoring  ](../gpt4all_python/monitoring.html)
    * [ SDK Reference  ](../gpt4all_python/ref.html)
  * Help  Help 
    * FAQ  [ FAQ  ](faq.html) Table of contents 
      * Models 
        * Which language models are supported? 
        * Which embedding models are supported? 
      * Software 
        * What software do I need? 
        * Which SDK languages are supported? 
        * Is there an API? 
        * Can I monitor a GPT4All deployment? 
        * Is there a command line interface (CLI)? 
      * Hardware 
        * What hardware do I need? 
        * What are the system requirements? 
    * [ Troubleshooting  ](troubleshooting.html)

Table of contents

  * Models 
    * Which language models are supported? 
    * Which embedding models are supported? 
  * Software 
    * What software do I need? 
    * Which SDK languages are supported? 
    * Is there an API? 
    * Can I monitor a GPT4All deployment? 
    * Is there a command line interface (CLI)? 
  * Hardware 
    * What hardware do I need? 
    * What are the system requirements? 

# Frequently Asked Questions

## Models

### Which language models are supported?

We support models with a `llama.cpp` implementation which have been uploaded
to [HuggingFace](https://huggingface.co/).

### Which embedding models are supported?

We support SBert and Nomic Embed Text v1 & v1.5.

## Software

### What software do I need?

All you need is to [install GPT4all](../index.html) onto you Windows, Mac, or
Linux computer.

### Which SDK languages are supported?

Our SDK is in Python for usability, but these are light bindings around
[`llama.cpp`](https://github.com/ggerganov/llama.cpp) implementations that we
contribute to for efficiency and accessibility on everyday computers.

### Is there an API?

Yes, you can run your model in server-mode with our [OpenAI-compatible
API](https://platform.openai.com/docs/api-reference/completions), which you
can configure in [settings](../gpt4all_desktop/settings.html#application-
settings)

### Can I monitor a GPT4All deployment?

Yes, GPT4All [integrates](../gpt4all_python/monitoring.html) with
[OpenLIT](https://github.com/openlit/openlit) so you can deploy LLMs with user
interactions and hardware usage automatically monitored for full
observability.

### Is there a command line interface (CLI)?

[Yes](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-bindings/cli), we
have a lightweight use of the Python client as a CLI. We welcome further
contributions!

## Hardware

### What hardware do I need?

GPT4All can run on CPU, Metal (Apple Silicon M1+), and GPU.

### What are the system requirements?

Your CPU needs to support [AVX or AVX2
instructions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) and
you need enough RAM to load a model into memory.

