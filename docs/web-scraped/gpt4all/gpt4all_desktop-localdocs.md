# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_desktop/localdocs.html

---

[ ![logo](../assets/nomic.png) ](../index.html "GPT4All") GPT4All

[ nomic-ai/gpt4all  ](https://github.com/nomic-ai/gpt4all "Go to repository")

  * [ GPT4All Documentation  ](../index.html)
  * [ Quickstart  ](quickstart.html)
  * [ Chats  ](chats.html)
  * [ Models  ](models.html)
  * LocalDocs  [ LocalDocs  ](localdocs.html) Table of contents 
    * Create LocalDocs 
    * How It Works 
  * [ Settings  ](settings.html)
  * [ Chat Templates  ](chat_templates.html)
  * Cookbook  Cookbook 
    * [ Local AI Chat with Microsoft Excel  ](cookbook/use-local-ai-models-to-privately-chat-with-microsoft-excel.html)
    * [ Local AI Chat with your Google Drive  ](cookbook/use-local-ai-models-to-privately-chat-with-google-drive.html)
    * [ Local AI Chat with your Obsidian Vault  ](cookbook/use-local-ai-models-to-privately-chat-with-Obsidian.html)
    * [ Local AI Chat with your OneDrive  ](cookbook/use-local-ai-models-to-privately-chat-with-One-Drive.html)
  * API Server  API Server 
    * [ GPT4All API Server  ](../gpt4all_api_server/home.html)
  * Python SDK  Python SDK 
    * [ GPT4All Python SDK  ](../gpt4all_python/home.html)
    * [ Monitoring  ](../gpt4all_python/monitoring.html)
    * [ SDK Reference  ](../gpt4all_python/ref.html)
  * Help  Help 
    * [ FAQ  ](../gpt4all_help/faq.html)
    * [ Troubleshooting  ](../gpt4all_help/troubleshooting.html)

Table of contents

  * Create LocalDocs 
  * How It Works 

# LocalDocs

LocalDocs brings the information you have from files on-device into your LLM
chats - **privately**.

## Create LocalDocs

Create LocalDocs

  1. Click `+ Add Collection`.

  2. Name your collection and link it to a folder.

![new GOT Docs](../assets/new_docs_annotated.png) |  ![new GOT Docs filled out](../assets/new_docs_annotated_filled.png)  
---|---  
  
  3. Click `Create Collection`. Progress for the collection is displayed on the LocalDocs page. 

![](../assets/baelor.png)Embedding in progress

You will see a green `Ready` indicator when the entire collection is ready.

Note: you can still chat with the files that are ready before the entire
collection is ready.

![](../assets/got_done.png)Embedding complete

Later on if you modify your LocalDocs settings you can rebuild your
collections with your new settings.

  4. In your chats, open `LocalDocs` with button in top-right corner to give your LLM context from those files.

![](../assets/syrio_snippets.png)LocalDocs result

  5. See which files were referenced by clicking `Sources` below the LLM responses.

![](../assets/open_sources.png)Sources

## How It Works

A LocalDocs collection uses Nomic AI's free and fast on-device embedding
models to index your folder into text snippets that each get an **embedding
vector**. These vectors allow us to find snippets from your files that are
semantically similar to the questions and prompts you enter in your chats. We
then include those semantically similar snippets in the prompt to the LLM.

To try the embedding models yourself, we recommend using the [Nomic Python
SDK](https://docs.nomic.ai/atlas/capabilities/embeddings)

