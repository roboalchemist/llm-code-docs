# GPT4All Documentation

Source: https://docs.gpt4all.io

---

[ ![logo](assets/nomic.png) ](index.html "GPT4All") GPT4All

[ nomic-ai/gpt4all  ](https://github.com/nomic-ai/gpt4all "Go to repository")

  * [ GPT4All Documentation  ](index.html)
  * [ Quickstart  ](gpt4all_desktop/quickstart.html)
  * [ Chats  ](gpt4all_desktop/chats.html)
  * [ Models  ](gpt4all_desktop/models.html)
  * [ LocalDocs  ](gpt4all_desktop/localdocs.html)
  * [ Settings  ](gpt4all_desktop/settings.html)
  * [ Chat Templates  ](gpt4all_desktop/chat_templates.html)
  * Cookbook  Cookbook 
    * [ Local AI Chat with Microsoft Excel  ](gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-microsoft-excel.html)
    * [ Local AI Chat with your Google Drive  ](gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-google-drive.html)
    * [ Local AI Chat with your Obsidian Vault  ](gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-Obsidian.html)
    * [ Local AI Chat with your OneDrive  ](gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-One-Drive.html)
  * API Server  API Server 
    * [ GPT4All API Server  ](gpt4all_api_server/home.html)
  * Python SDK  Python SDK 
    * [ GPT4All Python SDK  ](gpt4all_python/home.html)
    * [ Monitoring  ](gpt4all_python/monitoring.html)
    * [ SDK Reference  ](gpt4all_python/ref.html)
  * Help  Help 
    * [ FAQ  ](gpt4all_help/faq.html)
    * [ Troubleshooting  ](gpt4all_help/troubleshooting.html)

# GPT4All Documentation

GPT4All runs large language models (LLMs) privately on everyday desktops &
laptops.

No API calls or GPUs required - you can just download the application and [get
started](gpt4all_desktop/quickstart.html#quickstart).

Desktop Application

GPT4All runs LLMs as an application on your computer. Nomic's embedding models
can bring information from your local documents and files into your chats.
It's fast, on-device, and completely **private**.

[Download for Windows](https://gpt4all.io/installers/gpt4all-installer-
win64.exe)      [Download for Mac](https://gpt4all.io/installers/gpt4all-
installer-darwin.dmg)      [Download for
Linux](https://gpt4all.io/installers/gpt4all-installer-linux.run)

Python SDK

Use GPT4All in Python to program with LLMs implemented with the
[`llama.cpp`](https://github.com/ggerganov/llama.cpp) backend and [Nomic's C
backend](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-backend). Nomic
contributes to open source software like
[`llama.cpp`](https://github.com/ggerganov/llama.cpp) to make LLMs accessible
and efficient **for all**.

    
    
    pip install gpt4all
    
    
    
    from gpt4all import GPT4All
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
    with model.chat_session():
        print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))
    

