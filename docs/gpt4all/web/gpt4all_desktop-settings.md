# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_desktop/settings.html

---

[ ![logo](../assets/nomic.png) ](../index.html "GPT4All") GPT4All

[ nomic-ai/gpt4all  ](https://github.com/nomic-ai/gpt4all "Go to repository")

  * [ GPT4All Documentation  ](../index.html)
  * [ Quickstart  ](quickstart.html)
  * [ Chats  ](chats.html)
  * [ Models  ](models.html)
  * [ LocalDocs  ](localdocs.html)
  * Settings  [ Settings  ](settings.html) Table of contents 
    * Application Settings 
    * Model Settings 
      * Clone 
      * Sampling Settings 
    * LocalDocs Settings 
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

  * Application Settings 
  * Model Settings 
    * Clone 
    * Sampling Settings 
  * LocalDocs Settings 

# Settings

## Application Settings

General Application Settings

Setting | Description | Default Value  
---|---|---  
**Theme** | Color theme for the application. Options are `Light`, `Dark`, and `LegacyDark` | `Light`  
**Font Size** | Font size setting for text throughout the application. Options are Small, Medium, and Large | Small  
**Language and Locale** | The language and locale of that language you wish to use | System Locale  
**Device** | Device that will run your models. Options are `Auto` (GPT4All chooses), `Metal` (Apple Silicon M1+), `CPU`, and `GPU` | `Auto`  
**Default Model** | Choose your preferred LLM to load by default on startup | Auto  
**Suggestion Mode** | Generate suggested follow up questions at the end of responses | When chatting with LocalDocs  
**Download Path** | Select a destination on your device to save downloaded models | Windows: `C:\Users\{username}\AppData\Local\nomic.ai\GPT4All`  
  
Mac: `/Users/{username}/Library/Application Support/nomic.ai/GPT4All/`  
  
Linux: `/home/{username}/.local/share/nomic.ai/GPT4All`  
**Enable Datalake** | Opt-in to sharing interactions with GPT4All community (**anonymous** and **optional**) | Off  
  
Advanced Application Settings

Setting | Description | Default Value  
---|---|---  
**CPU Threads** | Number of concurrently running CPU threads (more can speed up responses) | 4  
**Enable System Tray** | The application will minimize to the system tray / taskbar when the window is closed | Off  
**Enable Local Server** | Allow any application on your device to use GPT4All via an OpenAI-compatible GPT4All API | Off  
**API Server Port** | Local HTTP port for the local API server | 4891  
  
## Model Settings

Model / Character Settings

Setting | Description | Default Value  
---|---|---  
**Name** | Unique name of this model / character | set by model uploader  
**Model File** | Filename (.gguf) of the model | set by model uploader  
**System Message** | General instructions for the chats this model will be used for | set by model uploader  
**Chat Template** | Format of user <-> assistant interactions for the chats this model will be used for | set by model uploader  
**Chat Name Prompt** | Prompt used to automatically generate chat names | Describe the above conversation in seven words or less.  
**Suggested FollowUp Prompt** | Prompt used to automatically generate follow up questions after a chat response | Suggest three very short factual follow-up questions that have not been answered yet or cannot be found inspired by the previous conversation and excerpts.  
  
### Clone

You can **clone** an existing model, which allows you to save a configuration
of a model file with different prompt templates and sampling settings.

### Sampling Settings

Model Sampling Settings

Setting | Description | Default Value  
---|---|---  
**Context Length** | Maximum length of input sequence in tokens | 2048  
**Max Length** | Maximum length of response in tokens | 4096  
**Prompt Batch Size** | Token batch size for parallel processing | 128  
**Temperature** | Lower temperature gives more likely generations | 0.7  
**Top P** | Prevents choosing highly unlikely tokens | 0.4  
**Top K** | Size of selection pool for tokens | 40  
**Min P** | Minimum relative probability | 0  
**Repeat Penalty Tokens** | Length to apply penalty | 64  
**Repeat Penalty** | Penalize repetitiveness | 1.18  
**GPU Layers** | How many model layers to load into VRAM | 32  
  
## LocalDocs Settings

General LocalDocs Settings

Setting | Description | Default Value  
---|---|---  
**Allowed File Extensions** | Choose which file types will be indexed into LocalDocs collections as text snippets with embedding vectors | `.txt`, `.pdf`, `.md`, `.rst`  
**Use Nomic Embed API** | Use Nomic API to create LocalDocs collections fast and off-device; [Nomic API Key](https://atlas.nomic.ai/) required | Off  
**Embeddings Device** | Device that will run embedding models. Options are `Auto` (GPT4All chooses), `Metal` (Apple Silicon M1+), `CPU`, and `GPU` | `Auto`  
**Show Sources** | Titles of source files retrieved by LocalDocs will be displayed directly in your chats. | On  
  
Advanced LocalDocs Settings

Note that increasing these settings can increase the likelihood of factual
responses, but may result in slower generation times.

Setting | Description | Default Value  
---|---|---  
**Document Snippet Size** | Number of string characters per document snippet | 512  
**Maximum Document Snippets Per Prompt** | Upper limit for the number of snippets from your files LocalDocs can retrieve for LLM context | 3

