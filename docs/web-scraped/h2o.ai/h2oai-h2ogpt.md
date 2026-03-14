# Source: https://github.com/h2oai/h2ogpt

Title: GitHub - h2oai/h2ogpt: Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://gpt-docs.h2o.ai/

URL Source: https://github.com/h2oai/h2ogpt

Markdown Content:
Turn ★ into ⭐ (top-right corner) if you like the project!

Query and summarize your documents or just chat with local private GPT LLMs using h2oGPT, an Apache V2 open-source project.

Check out a long CoT Open-o1 open 🍓strawberry🍓 project: [https://github.com/pseudotensor/open-strawberry](https://github.com/pseudotensor/open-strawberry)

Try Enterprise Version for Free
-------------------------------

[](https://github.com/h2oai/h2ogpt#try-enterprise-version-for-free)
[Enterprise h2oGPTe](https://h2ogpte.genai.h2o.ai/)

Video Demo
----------

[](https://github.com/h2oai/h2ogpt#video-demo)

demo2.mp4

[![Image 1: img-small.png](https://github.com/h2oai/h2ogpt/raw/main/docs/img-small.png) YouTube 4K Video](https://www.youtube.com/watch?v=_iktbj4obAI)

Features
--------

[](https://github.com/h2oai/h2ogpt#features)
*   **Private** offline database of any documents [(PDFs, Excel, Word, Images, Video Frames, YouTube, Audio, Code, Text, MarkDown, etc.)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LangChain.md#supported-datatypes)
    *   **Persistent** database (Chroma, Weaviate, or in-memory FAISS) using accurate embeddings (instructor-large, all-MiniLM-L6-v2, etc.)
    *   **Efficient** use of context using instruct-tuned LLMs (no need for LangChain's few-shot approach)
    *   **Parallel** summarization and extraction, reaching an output of 80 tokens per second with the 13B LLaMa2 model
    *   **HYDE** (Hypothetical Document Embeddings) for enhanced retrieval based upon LLM responses
    *   **Semantic Chunking** for better document splitting (requires GPU)

*   **Variety** of models supported (LLaMa2, Mistral, Falcon, Vicuna, WizardLM. With AutoGPTQ, 4-bit/8-bit, LORA, etc.) 
    *   **GPU** support from HF and LLaMa.cpp GGML models, and **CPU** support using HF, LLaMa.cpp, and GPT4ALL models
    *   **Attention Sinks** for [arbitrarily long](https://github.com/tomaarsen/attention_sinks) generation (LLaMa-2, Mistral, MPT, Pythia, Falcon, etc.)

*   **Gradio UI** or CLI with streaming of all models 
    *   **Upload** and **View** documents through the UI (control multiple collaborative or personal collections)
    *   **Vision Models** LLaVa, Claude-3, Gemini-Pro-Vision, GPT-4-Vision
    *   **Image Generation** Stable Diffusion (sdxl-turbo, sdxl, SD3), PlaygroundAI (playv2), and Flux
    *   **Voice STT** using Whisper with streaming audio conversion
    *   **Voice TTS** using MIT-Licensed Microsoft Speech T5 with multiple voices and Streaming audio conversion
    *   **Voice TTS** using MPL2-Licensed TTS including Voice Cloning and Streaming audio conversion
    *   **AI Assistant Voice Control Mode** for hands-free control of h2oGPT chat
    *   **Bake-off** UI mode against many models at the same time
    *   **Easy Download** of model artifacts and control over models like LLaMa.cpp through the UI
    *   **Authentication** in the UI by user/password via Native or Google OAuth
    *   **State Preservation** in the UI by user/password

*   **Open Web UI** with h2oGPT as backend via OpenAI Proxy 
    *   See [Start-up Docs](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#open-web-ui).
    *   Chat completion with streaming
    *   Document Q/A using h2oGPT ingestion with advanced OCR from DocTR
    *   Vision models
    *   Audio Transcription (STT)
    *   Audio Generation (TTS)
    *   Image generation
    *   Authentication
    *   State preservation

*   **Linux, Docker, macOS, and Windows** support
*   **Inference Servers**[support](https://github.com/h2oai/h2ogpt/blob/main/docs/README_InferenceServers.md) for oLLaMa, HF TGI server, vLLM, Gradio, ExLLaMa, Replicate, Together.ai, OpenAI, Azure OpenAI, Anthropic, MistralAI, Google, and Groq
*   **OpenAI compliant**
    *   Server Proxy [API](https://github.com/h2oai/h2ogpt/blob/main/docs/README_CLIENT.md) (h2oGPT acts as drop-in-replacement to OpenAI server)
    *   Chat and Text Completions (streaming and non-streaming)
    *   Audio Transcription (STT)
    *   Audio Generation (TTS)
    *   Image Generation
    *   Embedding
    *   Function tool calling w/auto tool selection
    *   AutoGen Code Execution Agent

*   **JSON Mode**
    *   Strict schema control for vLLM via its use of outlines
    *   Strict schema control for OpenAI, Anthropic, Google Gemini, MistralAI models
    *   JSON mode for some older OpenAI or Gemini models with schema control if model is smart enough (e.g. gemini 1.5 flash)
    *   Any model via code block extraction

*   **Web-Search** integration with Chat and Document Q/A
*   **Agents** for Search, Document Q/A, Python Code, CSV frames 
    *   High quality Agents via OpenAI proxy server on separate port
    *   Code-first agent that generates plots, researches, evaluates images via vision model, etc. (client code openai_server/openai_client.py).
    *   No UI for this, just API

*   **Evaluate** performance using reward models
*   **Quality** maintained with over 1000 unit and integration tests taking over 24 GPU-hours

Get Started
-----------

[](https://github.com/h2oai/h2ogpt#get-started)
[![Image 2: GitHub license](https://camo.githubusercontent.com/953f6d4373c0939af093d52eaed2136a447555d9f03acf4af3631ddfa56ca754/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f4e56494449412f6e76696469612d646f636b65723f7374796c653d666c61742d737175617265)](https://github.com/h2oai/h2ogpt/blob/main/LICENSE)[![Image 3: Linux](https://camo.githubusercontent.com/13ecf8308dd447edcef2bafd36de23b6539b35f24c18be96fd53d12241ec7db0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e75782d4643433632343f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e7578266c6f676f436f6c6f723d626c61636b)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LINUX.md)[![Image 4: macOS](https://camo.githubusercontent.com/13e95ab09a5058b9726da132e53608bb9d3f8f29933614976344ebcc2715d915/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61632532306f732d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d6d61636f73266c6f676f436f6c6f723d463046304630)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_MACOS.md)[![Image 5: Windows](https://camo.githubusercontent.com/60fe9cb6780952597b2a6887ab3dfaa2f461f30aa6f4946f683b84ca60692cba/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f57696e646f77732d3030373844363f7374796c653d666f722d7468652d6261646765266c6f676f3d77696e646f7773266c6f676f436f6c6f723d7768697465)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_WINDOWS.md)[![Image 6: Docker](https://camo.githubusercontent.com/97af73d098e049bf2d11e027500814d62dd2c840ce11d1cb5270607ae9949b2f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f636b65722d2532333064623765642e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_DOCKER.md)

### Install h2oGPT

[](https://github.com/h2oai/h2ogpt#install-h2ogpt)
Docker is recommended for Linux, Windows, and MAC for full capabilities. Linux Script also has full capability, while Windows and MAC scripts have less capabilities than using Docker.

*   [Docker Build and Run Docs (Linux, Windows, MAC)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_DOCKER.md)
*   [Linux Install and Run Docs](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LINUX.md)
*   [Windows 10/11 Installation Script](https://github.com/h2oai/h2ogpt/blob/main/docs/README_WINDOWS.md)
*   [MAC Install and Run Docs](https://github.com/h2oai/h2ogpt/blob/main/docs/README_MACOS.md)
*   [Quick Start on any Platform](https://github.com/h2oai/h2ogpt/blob/main/docs/README_quickstart.md)

* * *

### Collab Demos

[](https://github.com/h2oai/h2ogpt#collab-demos)
*   [![Image 7](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667) h2oGPT CPU](https://colab.research.google.com/drive/13RiBdAFZ6xqDwDKfW6BG_-tXfXiqPNQe?usp=sharing)
*   [![Image 8](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667) h2oGPT GPU](https://colab.research.google.com/drive/143-KFHs2iCqXTQLI2pFCDiR69z0dR8iE?usp=sharing)

### Resources

[](https://github.com/h2oai/h2ogpt#resources)
*   [FAQs](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md)
*   [README for LangChain](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LangChain.md)
*   [Discord](https://discord.gg/WKhYMWcVbq)
*   [Models (LLaMa-2, Falcon 40, etc.) at 🤗](https://huggingface.co/h2oai/)
*   [YouTube: 100% Offline ChatGPT Alternative?](https://www.youtube.com/watch?v=Coj72EzmX20)
*   [YouTube: Ultimate Open-Source LLM Showdown (6 Models Tested) - Surprising Results!](https://www.youtube.com/watch?v=FTm5C_vV_EY)
*   [YouTube: Blazing Fast Falcon 40b 🚀 Uncensored, Open-Source, Fully Hosted, Chat With Your Docs](https://www.youtube.com/watch?v=H8Dx-iUY49s)
*   [Technical Paper: https://arxiv.org/pdf/2306.08161.pdf](https://arxiv.org/pdf/2306.08161.pdf)

### Docs Guide

[](https://github.com/h2oai/h2ogpt#docs-guide)
*   [Get Started](https://github.com/h2oai/h2ogpt#get-started)
    *   [Linux (CPU or CUDA)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LINUX.md)
    *   [macOS (CPU or M1/M2)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_MACOS.md)
    *   [Windows 10/11 (CPU or CUDA)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_WINDOWS.md)
    *   [GPU (CUDA, AutoGPTQ, exllama) Running Details](https://github.com/h2oai/h2ogpt/blob/main/docs/README_GPU.md)
    *   [CPU Running Details](https://github.com/h2oai/h2ogpt/blob/main/docs/README_CPU.md)
    *   [CLI chat](https://github.com/h2oai/h2ogpt/blob/main/docs/README_CLI.md)
    *   [Gradio UI](https://github.com/h2oai/h2ogpt/blob/main/docs/README_ui.md)
    *   [Client API (Gradio, OpenAI-Compliant)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_CLIENT.md)
    *   [Inference Servers (oLLaMa, HF TGI server, vLLM, Groq, Anthropic, Google, Mistral, Gradio, ExLLaMa, Replicate, OpenAI, Azure OpenAI)](https://github.com/h2oai/h2ogpt/blob/main/docs/README_InferenceServers.md)
    *   [Build Python Wheel](https://github.com/h2oai/h2ogpt/blob/main/docs/README_WHEEL.md)
    *   [Offline Installation](https://github.com/h2oai/h2ogpt/blob/main/docs/README_offline.md)
    *   [Low Memory](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#low-memory-mode)
    *   [Docker](https://github.com/h2oai/h2ogpt/blob/main/docs/README_DOCKER.md)

*   [LangChain Document Support](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LangChain.md)
*   [Compare to PrivateGPT et al.](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LangChain.md#what-is-h2ogpts-langchain-integration-like)
*   [Roadmap](https://github.com/h2oai/h2ogpt#roadmap)
*   [Development](https://github.com/h2oai/h2ogpt#development)
*   [Help](https://github.com/h2oai/h2ogpt#help)
    *   [LangChain file types supported](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LangChain.md#supported-datatypes)
    *   [CLI Database control](https://github.com/h2oai/h2ogpt/blob/main/docs/README_LangChain.md#database-creation)
    *   [FAQ](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md)
        *   [Model Usage Notes](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#model-usage-notes)
        *   [Adding LLM Models (including using GGUF and Attention Sinks)](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#adding-models)
        *   [Adding Embedding Models](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#add-new-embedding-model)
        *   [Adding Prompts](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#adding-prompt-templates)
        *   [In-Context Learning](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#in-context-learning-via-prompt-engineering)
        *   [Multiple GPUs](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#multiple-gpus)
        *   [Low-Memory Usage](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#low-memory-mode)
        *   [Environment Variables](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#what-envs-can-i-pass-to-control-h2ogpt)
        *   [HTTPS access for server and client](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#https-access-for-server-and-client)

    *   [Useful Links](https://github.com/h2oai/h2ogpt/blob/main/docs/LINKS.md)
    *   [Fine-Tuning](https://github.com/h2oai/h2ogpt/blob/main/docs/FINETUNE.md)
    *   [Triton](https://github.com/h2oai/h2ogpt/blob/main/docs/TRITON.md)
    *   [Commercial viability](https://github.com/h2oai/h2ogpt/blob/main/docs/FAQ.md#commercial-viability)

*   [Acknowledgements](https://github.com/h2oai/h2ogpt#acknowledgements)
*   [Why H2O.ai?](https://github.com/h2oai/h2ogpt#why-h2oai)
*   [Disclaimer](https://github.com/h2oai/h2ogpt#disclaimer)

### Development

[](https://github.com/h2oai/h2ogpt#development)
*   To create a development environment for training and generation, follow the [installation instructions](https://github.com/h2oai/h2ogpt/blob/main/docs/INSTALL.md).
*   To fine-tune any LLM models on your data, follow the [fine-tuning instructions](https://github.com/h2oai/h2ogpt/blob/main/docs/FINETUNE.md).
*   To run h2oGPT tests: pip install requirements-parser pytest-instafail pytest-random-order playsound==1.3.0
conda install -c conda-forge gst-python -y
sudo apt-get install gstreamer-1.0
pip install pygame
GPT_H2O_AI=0 CONCURRENCY_COUNT=1 pytest --instafail -s -v tests
# for openai server test on already-running local server
pytest -s -v -n 4 openai_server/test_openai_server.py::test_openai_client  or tweak/run `tests/test4gpus.sh` to run tests in parallel.

### Acknowledgements

[](https://github.com/h2oai/h2ogpt#acknowledgements)
*   Some training code was based upon March 24 version of [Alpaca-LoRA](https://github.com/tloen/alpaca-lora/).
*   Used high-quality created data by [OpenAssistant](https://open-assistant.io/).
*   Used base models by [EleutherAI](https://www.eleuther.ai/).
*   Used OIG data created by [LAION](https://laion.ai/blog/oig-dataset/).

### Why H2O.ai?

[](https://github.com/h2oai/h2ogpt#why-h2oai)
Our [Makers](https://h2o.ai/company/team/) at [H2O.ai](https://h2o.ai/) have built several world-class Machine Learning, Deep Learning and AI platforms:

*   #1 open-source machine learning platform for the enterprise [H2O-3](https://github.com/h2oai/h2o-3)
*   The world's best AutoML (Automatic Machine Learning) with [H2O Driverless AI](https://h2o.ai/platform/ai-cloud/make/h2o-driverless-ai/)
*   No-Code Deep Learning with [H2O Hydrogen Torch](https://h2o.ai/platform/ai-cloud/make/hydrogen-torch/)
*   Document Processing with Deep Learning in [Document AI](https://h2o.ai/platform/ai-cloud/make/document-ai/)

We also built platforms for deployment and monitoring, and for data wrangling and governance:

*   [H2O MLOps](https://h2o.ai/platform/ai-cloud/operate/h2o-mlops/) to deploy and monitor models at scale
*   [H2O Feature Store](https://h2o.ai/platform/ai-cloud/make/feature-store/) in collaboration with AT&T
*   Open-source Low-Code AI App Development Frameworks [Wave](https://wave.h2o.ai/) and [Nitro](https://nitro.h2o.ai/)
*   Open-source Python [datatable](https://github.com/h2oai/datatable/) (the engine for H2O Driverless AI feature engineering)

Many of our customers are creating models and deploying them enterprise-wide and at scale in the [H2O AI Cloud](https://h2o.ai/platform/ai-cloud/):

*   Multi-Cloud or on Premises
*   [Managed Cloud (SaaS)](https://h2o.ai/platform/ai-cloud/managed)
*   [Hybrid Cloud](https://h2o.ai/platform/ai-cloud/hybrid)
*   [AI Appstore](https://docs.h2o.ai/h2o-ai-cloud/)

We are proud to have over 25 (of the world's 280) [Kaggle Grandmasters](https://h2o.ai/company/team/kaggle-grandmasters/) call H2O home, including three Kaggle Grandmasters who have made it to world #1.

### Disclaimer

[](https://github.com/h2oai/h2ogpt#disclaimer)
Please read this disclaimer carefully before using the large language model provided in this repository. Your use of the model signifies your agreement to the following terms and conditions.

*   Biases and Offensiveness: The large language model is trained on a diverse range of internet text data, which may contain biased, racist, offensive, or otherwise inappropriate content. By using this model, you acknowledge and accept that the generated content may sometimes exhibit biases or produce content that is offensive or inappropriate. The developers of this repository do not endorse, support, or promote any such content or viewpoints.
*   Limitations: The large language model is an AI-based tool and not a human. It may produce incorrect, nonsensical, or irrelevant responses. It is the user's responsibility to critically evaluate the generated content and use it at their discretion.
*   Use at Your Own Risk: Users of this large language model must assume full responsibility for any consequences that may arise from their use of the tool. The developers and contributors of this repository shall not be held liable for any damages, losses, or harm resulting from the use or misuse of the provided model.
*   Ethical Considerations: Users are encouraged to use the large language model responsibly and ethically. By using this model, you agree not to use it for purposes that promote hate speech, discrimination, harassment, or any form of illegal or harmful activities.
*   Reporting Issues: If you encounter any biased, offensive, or otherwise inappropriate content generated by the large language model, please report it to the repository maintainers through the provided channels. Your feedback will help improve the model and mitigate potential issues.
*   Changes to this Disclaimer: The developers of this repository reserve the right to modify or update this disclaimer at any time without prior notice. It is the user's responsibility to periodically review the disclaimer to stay informed about any changes.

By using the large language model provided in this repository, you agree to accept and comply with the terms and conditions outlined in this disclaimer. If you do not agree with any part of this disclaimer, you should refrain from using the model and any content generated by it.

Star History
------------

[](https://github.com/h2oai/h2ogpt#star-history)
[![Image 9: Star History Chart](https://camo.githubusercontent.com/7951ee86b074006d0042204af1ed8e76eed04d74d72c3e21c67d5939178d0f10/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d68326f61692f68326f67707426747970653d54696d656c696e65)](https://star-history.com/#h2oai/h2ogpt&Timeline)
