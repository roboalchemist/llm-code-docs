# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-microsoft-excel.html

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
    * Local AI Chat with Microsoft Excel  [ Local AI Chat with Microsoft Excel  ](use-local-ai-models-to-privately-chat-with-microsoft-excel.html) Table of contents 
      * Attach Microsoft Excel to your GPT4All Conversation 
      * How It Works 
      * Limitations 
    * [ Local AI Chat with your Google Drive  ](use-local-ai-models-to-privately-chat-with-google-drive.html)
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

  * Attach Microsoft Excel to your GPT4All Conversation 
  * How It Works 
  * Limitations 

# Using GPT4All to Privately Chat with your Microsoft Excel Spreadsheets

Local and Private AI Chat with your Microsoft Excel Spreadsheets

Microsoft Excel allows you to create, manage, and analyze data in spreadsheet
format. By attaching your spreadsheets directly to GPT4All, you can privately
chat with the AI to query and explore the data, enabling you to summarize,
generate reports, and glean insights from your filesâall within your
conversation.

## Attach Microsoft Excel to your GPT4All Conversation

Attach Microsoft Excel to your GPT4All Conversation

  1. **Install GPT4All and Open** :

     * Go to [nomic.ai/gpt4all](https://nomic.ai/gpt4all) to install GPT4All for your operating system.

     * Navigate to the Chats view within GPT4All.

![Chat view](../../assets/chat_window.png)  
---  
  
  2. **Example Spreadsheet** :

![Spreadsheet view](../../assets/disney_spreadsheet.png)  
---  
  
  3. **Attach to GPT4All conversration** ![Attach view](../../assets/attach_spreadsheet.png)  
---  
  
  4. **Have GPT4All Summarize and Generate a Report** ![Attach view](../../assets/spreadsheet_chat.png)  
---  
  

## How It Works

GPT4All parses your attached excel spreadsheet into Markdown, a format
understandable to LLMs, and adds the markdown text to the context for your LLM
chat. You can view the code that converts `.xslx` to Markdown
[here](https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-
chat/src/xlsxtomd.cpp) in the GPT4All github repo.

For example, the above spreadsheet titled `disney_income_stmt.xlsx` would be
formatted the following way:

    
    
    ## disney_income_stmt
    
    |Walt Disney Co.|||||||
    |---|---|---|---|---|---|---|
    |Consolidated Income Statement|||||||
    |||||||||
    |US$ in millions|||||||
    |12 months ended:|2023-09-30 00:00:00|2022-10-01 00:00:00|2021-10-02 00:00:00|2020-10-03 00:00:00|2019-09-28 00:00:00|2018-09-29 00:00:00|
    |Services|79562|74200|61768|59265|60542|50869|
    ...
    ...
    ...
    

## Limitations

It is important to double-check the claims LLMs make about the spreadsheets
you provide. LLMs can make mistakes about the data they are presented,
particularly for the LLMs with smaller parameter counts (~8B) that fit within
the memory of consumer hardware.

