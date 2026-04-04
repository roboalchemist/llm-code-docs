# Source: https://console.groq.com/docs/gradio

---
description: Learn how to use Gradio with Groq to build fast, interactive web interfaces and demos for your LLM-powered applications.
title: Gradio + Groq: Fast, Interactive Web Interfaces - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [🎨 Gradio + Groq: Easily Build Web Interfaces](#-gradio--groq-easily-build-web-interfaces)

[Gradio](https://www.gradio.app/) is a powerful library for creating web interfaces for your applications that enables you to quickly build interactive demos for your fast Groq apps with features such as:

* **Interface Builder:** Create polished UIs with just a few lines of code, supporting text, images, audio, and more
* **Interactive Demos:** Build demos that showcase your LLM applications with multiple input/output components
* **Shareable Apps:** Deploy and share your Groq-powered applications with a single click

### [Quick Start (2 minutes to hello world)](#quick-start-2-minutes-to-hello-world)

#### [1\. Install the packages:](#1-install-the-packages)

curl

```
pip install groq-gradio
```

#### [2\. Set up your API key:](#2-set-up-your-api-key)

curl

```
export GROQ_API_KEY="your-groq-api-key"
```

#### [3\. Create your first Gradio chat interface:](#3-create-your-first-gradio-chat-interface)

The following code creates a simple chat interface with `llama-3.3-70b-versatile` that includes a clean UI.

Python

```
import gradio as gr
import groq_gradio
import os

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

gr.load(
    name='llama-3.3-70b-versatile', # The specific model powered by Groq to use
    src=groq_gradio.registry, # Tells Gradio to use our custom interface registry as the source
    title='Groq-Gradio Integration', # The title shown at the top of our UI
    description="Chat with the Llama 3.3 70B model powered by Groq.", # Subtitle
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"] # Pre-written prompts users can click to try
).launch() # Creates and starts the web server!
```

**Challenge**: Enhance the above example to create a multi-modal chatbot that leverages text, audio, and vision models powered by Groq and displayed on a customized UI built with Gradio blocks!

For more information on building robust applications with Gradio and Groq, see:

* [Official Documentation: Gradio](https://www.gradio.app/docs)
* [Tutorial: Automatic Voice Detection with Groq](https://www.gradio.app/guides/automatic-voice-detection)
* [Groq API Cookbook: Groq and Gradio for Realtime Voice-Powered AI Applications](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/groq-gradio/groq-gradio-tutorial.ipynb)
* [Webinar: Building a Multimodal Voice Enabled Calorie Tracking App with Groq and Gradio](https://youtu.be/azXaioGdm2Q?si=sXPJW1IerbghsCKU)