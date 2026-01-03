# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-Obsidian.html

---

[ ![logo](../../assets/nomic.png) ](../../index.html "GPT4All") GPT4All

[ nomic-ai/gpt4all  ](https://github.com/nomic-ai/gpt4all "Go to repository")

  * [ GPT4All Documentation  ](../../index.html)
  * [ Quickstart  ](../quickstart.html)
  * [ Chats  ](../chats.html)
  * [ Models  ](../models.html)
  * [ LocalDocs  ](../localdocs.html)
  * [ Settings  ](../settings.html)
  * [ Chat Templates  ](../chat_templates.html)
  * Cookbook  Cookbook 
    * [ Local AI Chat with Microsoft Excel  ](use-local-ai-models-to-privately-chat-with-microsoft-excel.html)
    * [ Local AI Chat with your Google Drive  ](use-local-ai-models-to-privately-chat-with-google-drive.html)
    * Local AI Chat with your Obsidian Vault  [ Local AI Chat with your Obsidian Vault  ](use-local-ai-models-to-privately-chat-with-Obsidian.html) Table of contents 
      * Download Obsidian for Desktop 
      * Connect Obsidian to LocalDocs 
      * How It Works 
    * [ Local AI Chat with your OneDrive  ](use-local-ai-models-to-privately-chat-with-One-Drive.html)
  * API Server  API Server 
    * [ GPT4All API Server  ](../../gpt4all_api_server/home.html)
  * Python SDK  Python SDK 
    * [ GPT4All Python SDK  ](../../gpt4all_python/home.html)
    * [ Monitoring  ](../../gpt4all_python/monitoring.html)
    * [ SDK Reference  ](../../gpt4all_python/ref.html)
  * Help  Help 
    * [ FAQ  ](../../gpt4all_help/faq.html)
    * [ Troubleshooting  ](../../gpt4all_help/troubleshooting.html)

Table of contents

  * Download Obsidian for Desktop 
  * Connect Obsidian to LocalDocs 
  * How It Works 

# Using GPT4All to Privately Chat with your Obsidian Vault

Obsidian for Desktop is a powerful management and note-taking software
designed to create and organize markdown notes. This tutorial allows you to
sync and access your Obsidian note files directly on your computer. By
connecting it to LocalDocs, you can integrate these files into your LLM chats
for private access and enhanced context.

## Download Obsidian for Desktop

Download Obsidian for Desktop

  1. **Download Obsidian for Desktop** :

     * Visit the [Obsidian website](https://obsidian.md) and create an account account.
     * Click the Download button in the center of the homepage
     * For more help with installing Obsidian see [Getting Started with Obsidian](https://help.obsidian.md/Getting+started/Download+and+install+Obsidian)
  2. **Set Up Obsidian** :

     * Launch Obsidian from your Applications folder (macOS), Start menu (Windows), or equivalent location (Linux).
     * On the welcome screen, you can either create a new vault (a collection of notes) or open an existing one.
     * To create a new vault, click Create a new vault, name your vault, choose a location on your computer, and click Create.
  3. **Sign in and Sync** : \- Once installed, you can start adding and organizing notes. \- Choose the folders you want to sync to your computer.

## Connect Obsidian to LocalDocs

Connect Obsidian to LocalDocs

  1.      * Navigate to the LocalDocs feature within GPT4All.

**Open LocalDocs** :

![LocalDocs interface](https://github.com/nomic-
ai/gpt4all/assets/132290469/d8fb2d79-2063-45d4-bcce-7299fb75b144)  
---  
  
  2. **Add Collection** :

     * Click on **\+ Add Collection** to begin linking your Obsidian Vault.

![Screenshot of adding collection](https://raw.githubusercontent.com/nomic-
ai/gpt4all/124ef867a9d9afd9e14d3858cd77bce858f79773/gpt4all-
bindings/python/docs/assets/obsidian_adding_collection.png)  
---  
  
     * Name your collection
  3. **Create Collection** :

     * Click **Create Collection** to initiate the embedding process. Progress will be displayed within the LocalDocs interface.
  4. **Access Files in Chats** :

     * Load a model to chat with your files (Llama 3 Instruct is the fastest)
     * In your chat, open 'LocalDocs' with the button in the top-right corner to provide context from your synced Obsidian notes.

![Accessing LocalDocs in chats](https://raw.githubusercontent.com/nomic-
ai/gpt4all/124ef867a9d9afd9e14d3858cd77bce858f79773/gpt4all-
bindings/python/docs/assets/obsidian_docs.png)  
---  
  
  5. **Interact With Your Notes:**

     * Use the model to interact with your files  ![osbsidian user interaction](https://raw.githubusercontent.com/nomic-ai/gpt4all/124ef867a9d9afd9e14d3858cd77bce858f79773/gpt4all-bindings/python/docs/assets/osbsidian_user_interaction.png)  
---  
![osbsidian GPT4ALL response](https://raw.githubusercontent.com/nomic-
ai/gpt4all/124ef867a9d9afd9e14d3858cd77bce858f79773/gpt4all-
bindings/python/docs/assets/obsidian_response.png)  
---  
  6. **View Referenced Files** :

     * Click on **Sources** below LLM responses to see which Obsidian Notes were referenced.

![Referenced Files](https://raw.githubusercontent.com/nomic-
ai/gpt4all/124ef867a9d9afd9e14d3858cd77bce858f79773/gpt4all-
bindings/python/docs/assets/obsidian_sources.png)  
---  
  

## How It Works

Obsidian for Desktop syncs your Obsidian notes to your computer, while
LocalDocs integrates these files into your LLM chats using embedding models.
These models find semantically similar snippets from your files to enhance the
context of your interactions.

To learn more about embedding models and explore further, refer to the [Nomic
Python SDK
documentation](https://docs.nomic.ai/atlas/capabilities/embeddings).

