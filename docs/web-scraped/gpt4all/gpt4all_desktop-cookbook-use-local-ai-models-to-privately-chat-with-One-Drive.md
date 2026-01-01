# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-One-Drive.html

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
    * [ Local AI Chat with your Obsidian Vault  ](use-local-ai-models-to-privately-chat-with-Obsidian.html)
    * Local AI Chat with your OneDrive  [ Local AI Chat with your OneDrive  ](use-local-ai-models-to-privately-chat-with-One-Drive.html) Table of contents 
      * Download OneDrive for Desktop 
      * Connect OneDrive to LocalDocs 
      * How It Works 
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

  * Download OneDrive for Desktop 
  * Connect OneDrive to LocalDocs 
  * How It Works 

# Using GPT4All to Privately Chat with your OneDrive Data

Local and Private AI Chat with your OneDrive Data

OneDrive for Desktop allows you to sync and access your OneDrive files
directly on your computer. By connecting your synced directory to LocalDocs,
you can start using GPT4All to privately chat with data stored in your
OneDrive.

## Download OneDrive for Desktop

Download OneDrive for Desktop

  1. **Download OneDrive for Desktop** :
  2. Visit [Microsoft OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/download).
  3. Press 'download' for your respective device type.
  4. Download the OneDrive for Desktop application.

  5. **Install OneDrive for Desktop**

  6. Run the installer file you downloaded.
  7. Follow the prompts to complete the installation process.

  8. **Sign in and Sync**

  9. Once installed, sign in to OneDrive for Desktop with your Microsoft account credentials.
  10. Choose the folders you want to sync to your computer.

## Connect OneDrive to LocalDocs

Connect OneDrive to LocalDocs

  1. **Install GPT4All and Open LocalDocs** :

     * Go to [nomic.ai/gpt4all](https://nomic.ai/gpt4all) to install GPT4All for your operating system.

     * Navigate to the LocalDocs feature within GPT4All to configure it to use your synced OneDrive directory.

![Screenshot 2024-07-10 at 10 55 41 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/54254bc0-d9a0-40c4-9fd1-5059abaad583)  
---  
  
  2. **Add Collection** :

     * Click on **\+ Add Collection** to begin linking your OneDrive folders.

![Screenshot 2024-07-10 at 10 56 29 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/7f12969a-753a-4757-bb9e-9b607cf315ca)  
---  
  
     * Name the Collection and specify the OneDrive folder path.
  3. **Create Collection** :

     * Click **Create Collection** to initiate the embedding process. Progress will be displayed within the LocalDocs interface.
  4. **Access Files in Chats** :

     * Load a model within GPT4All to chat with your files.

     * In your chat, open 'LocalDocs' using the button in the top-right corner to provide context from your synced OneDrive files.

![Screenshot 2024-07-10 at 10 58 55 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/b5a67fe6-0d6a-42ae-b3b8-cc0f91cbf5b1)  
---  
  
  5. **Interact With Your OneDrive** :

     * Use the model to interact with your files directly from OneDrive.

![Screenshot 2024-07-10 at 11 04 55 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/2c9815b8-3d1c-4179-bf76-3ddbafb193bf)  
---  
  
![Screenshot 2024-07-11 at 11 21 46 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/ce8be292-b025-415a-bd54-f11868e0cd0a)  
---  
  
  6. **View Referenced Files** :

     * Click on **Sources** below responses to see which OneDrive files were referenced.

![Screenshot 2024-07-11 at 11 22 49 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/6fe3f10d-2791-4153-88a7-2198ab3ac945)  
---  
  

## How It Works

OneDrive for Desktop syncs your OneDrive files to your computer, while
LocalDocs maintains a database of these synced files for use by your local
GPT4All model. As your OneDrive updates, LocalDocs will automatically detect
file changes and stay up to date. LocalDocs leverages [Nomic
Embedding](https://docs.nomic.ai/atlas/capabilities/embeddings) models to find
semantically similar snippets from your files, enhancing the context of your
interactions.

