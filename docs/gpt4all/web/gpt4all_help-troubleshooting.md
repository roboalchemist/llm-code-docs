# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_help/troubleshooting.html

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
    * [ FAQ  ](faq.html)
    * Troubleshooting  [ Troubleshooting  ](troubleshooting.html) Table of contents 
      * Error Loading Models 
      * Bad Responses 
        * Responses Incoherent 
        * Responses Incorrect 
        * LocalDocs Issues 

Table of contents

  * Error Loading Models 
  * Bad Responses 
    * Responses Incoherent 
    * Responses Incorrect 
    * LocalDocs Issues 

# Troubleshooting

## Error Loading Models

It is possible you are trying to load a model from HuggingFace whose weights
are not compatible with our [backend](https://github.com/nomic-
ai/gpt4all/tree/main/gpt4all-bindings).

Try downloading one of the officially supported models listed on the main
models page in the application. If the problem persists, please share your
experience on our [Discord](https://discord.com/channels/1076964370942267462).

## Bad Responses

Try the [example chats](../gpt4all_desktop/chats.html) to double check that
your system is implementing models correctly.

### Responses Incoherent

If you are seeing something **not at all** resembling the [example
chats](../gpt4all_desktop/chats.html) \- for example, if the responses you are
seeing look nonsensical - try [downloading a different
model](../gpt4all_desktop/models.html), and please share your experience on
our [Discord](https://discord.com/channels/1076964370942267462).

### Responses Incorrect

LLMs can be unreliable. It's helpful to know what their training data was -
they are less likely to be correct when asking about data they were not
trained on unless you give the necessary information in the prompt as
**context**.

Giving LLMs additional context, like chatting using
[LocalDocs](../gpt4all_desktop/localdocs.html), can help merge the language
model's ability to understand text with the files that you trust to contain
the information you need.

Including information in a prompt is not a guarantee that it will be used
correctly, but the more clear and concise your prompts, and the more relevant
your prompts are to your files, the better.

### LocalDocs Issues

Occasionally a model - particularly a smaller or overall weaker LLM - may not
use the relevant text snippets from the files that were referenced via
LocalDocs. If you are seeing this, it can help to use phrases like "in the
docs" or "from the provided files" when prompting your model.

