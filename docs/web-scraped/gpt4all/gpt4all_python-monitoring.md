# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_python/monitoring.html

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
    * [ GPT4All Python SDK  ](home.html)
    * Monitoring  [ Monitoring  ](monitoring.html) Table of contents 
      * Setup Monitoring 
      * Visualization 
        * OpenLIT UI 
        * Grafana, DataDog, & Other Integrations 
    * [ SDK Reference  ](ref.html)
  * Help  Help 
    * [ FAQ  ](../gpt4all_help/faq.html)
    * [ Troubleshooting  ](../gpt4all_help/troubleshooting.html)

Table of contents

  * Setup Monitoring 
  * Visualization 
    * OpenLIT UI 
    * Grafana, DataDog, & Other Integrations 

# GPT4All Monitoring

GPT4All integrates with [OpenLIT](https://github.com/openlit/openlit)
OpenTelemetry auto-instrumentation to perform real-time monitoring of your LLM
application and GPU hardware.

Monitoring can enhance your GPT4All deployment with auto-generated traces and
metrics for

  * **Performance Optimization:** Analyze latency, cost and token usage to ensure your LLM application runs efficiently, identifying and resolving performance bottlenecks swiftly.

  * **User Interaction Insights:** Capture each prompt and response to understand user behavior and usage patterns better, improving user experience and engagement.

  * **Detailed GPU Metrics:** Monitor essential GPU parameters such as utilization, memory consumption, temperature, and power usage to maintain optimal hardware performance and avert potential issues.

## Setup Monitoring

Setup Monitoring

With [OpenLIT](https://github.com/openlit/openlit), you can automatically
monitor traces and metrics for your LLM deployment:

    
    
    pip install openlit
    
    
    
    from gpt4all import GPT4All
    import openlit
    
    openlit.init()  # start
    # openlit.init(collect_gpu_stats=True)  # Optional: To configure GPU monitoring
    
    model = GPT4All(model_name='orca-mini-3b-gguf2-q4_0.gguf')
    
    # Start a chat session and send queries
    with model.chat_session():
        response1 = model.generate(prompt='hello', temp=0)
        response2 = model.generate(prompt='write me a short poem', temp=0)
        response3 = model.generate(prompt='thank you', temp=0)
    
        print(model.current_chat_session)
    

## Visualization

### OpenLIT UI

Connect to OpenLIT's UI to start exploring the collected LLM performance
metrics and traces. Visit the OpenLIT [Quickstart
Guide](https://docs.openlit.io/latest/quickstart) for step-by-step details.

### Grafana, DataDog, & Other Integrations

You can also send the data collected by OpenLIT to popular monitoring tools
like Grafana and DataDog. For detailed instructions on setting up these
connections, please refer to the OpenLIT [Connections
Guide](https://docs.openlit.io/latest/connections/intro).

