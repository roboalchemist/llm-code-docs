# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-google-drive.html

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
    * Local AI Chat with your Google Drive  [ Local AI Chat with your Google Drive  ](use-local-ai-models-to-privately-chat-with-google-drive.html) Table of contents 
      * Download Google Drive for Desktop 
      * Connect Google Drive to LocalDocs 
      * How It Works 
    * [ Local AI Chat with your Obsidian Vault  ](use-local-ai-models-to-privately-chat-with-Obsidian.html)
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

  * Download Google Drive for Desktop 
  * Connect Google Drive to LocalDocs 
  * How It Works 

# Using GPT4All to Privately Chat with your Google Drive Data

Local and Private AI Chat with your Google Drive Data

Google Drive for Desktop allows you to sync and access your Google Drive files
directly on your computer. By connecting your synced directory to LocalDocs,
you can start using GPT4All to privately chat with data stored in your Google
Drive.

## Download Google Drive for Desktop

Download Google Drive for Desktop

  1. **Download Google Drive for Desktop** :
  2. Visit [drive.google.com](https://drive.google.com) and sign in with your Google account.
  3. Navigate to the **Settings** (gear icon) and select **Settings** from the dropdown menu.
  4. Scroll down to **Google Drive for desktop** and click **Download**.

  5. **Install Google Drive for Desktop**

  6. Run the installer file you downloaded.
  7. Follow the prompts to complete the installation process.

  8. **Sign in and Sync**

  9. Once installed, sign in to Google Drive for Desktop with your Google account credentials.
  10. Choose the folders you want to sync to your computer.

For advanced help, see [Setting up Google Drive for
Desktop](https://support.google.com/drive/answer/10838124?hl=en)

## Connect Google Drive to LocalDocs

Connect Google Drive to LocalDocs

  1. **Install GPT4All and Open LocalDocs** :

     * Go to [nomic.ai/gpt4all](https://nomic.ai/gpt4all) to install GPT4All for your operating system.

     * Navigate to the LocalDocs feature within GPT4All to configure it to use your synced directory.

![Screenshot 2024-07-09 at 3 15 35 PM](https://github.com/nomic-
ai/gpt4all/assets/132290469/d8fb2d79-2063-45d4-bcce-7299fb75b144)  
---  
  
  2. **Add Collection** :

     * Click on **\+ Add Collection** to begin linking your Google Drive folders.

![Screenshot 2024-07-09 at 3 17 24 PM](https://github.com/nomic-
ai/gpt4all/assets/132290469/39063615-9eb6-4c47-bde7-c9f04f9b168b)  
---  
  
     * Name Collection
  3. **Create Collection** :

     * Click **Create Collection** to initiate the embedding process. Progress will be displayed within the LocalDocs interface.
  4. **Access Files in Chats** :

     * Load a model to chat with your files (Llama 3 Instruct performs best)

     * In your chat, open 'LocalDocs' with the button in the top-right corner to provide context from your synced Google Drive files.

![Screenshot 2024-07-09 at 3 20 53 PM](https://github.com/nomic-
ai/gpt4all/assets/132290469/ce68811f-9abd-451b-ac0a-fb941e185d7a)  
---  
  
  5. **Interact With Your Drive:**

     * Use the model to interact with your files

![Screenshot 2024-07-09 at 3 36 51 PM](https://github.com/nomic-
ai/gpt4all/assets/132290469/bc55bc36-e613-419d-a568-adb1cd993854)  
---  
  
![Screenshot 2024-07-11 at 11 34 00 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/1c0fd19a-5a22-4726-a841-d26c1bea81fc)  
---  
  
  6. **View Referenced Files** :

     * Click on **Sources** below LLM responses to see which Google Drive files were referenced.

  
![Screenshot 2024-07-11 at 11 34 37 AM](https://github.com/nomic-
ai/gpt4all/assets/132290469/78527d30-8d24-4b4c-8311-b611a2d66fcd)  
---  
  

## How It Works

Google Drive for Desktop syncs your Google Drive files to your computer, while
LocalDocs maintains a database of these synced files for use by your local
LLM. As your Google Drive updates, LocalDocs will automatically detect file
changes and get up to date. LocalDocs is powered by [Nomic
Embedding](https://docs.nomic.ai/atlas/capabilities/embeddings) models which
find semantically similar snippets from your files to enhance the context of
your interactions.

