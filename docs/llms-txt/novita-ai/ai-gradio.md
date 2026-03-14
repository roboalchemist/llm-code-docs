# Source: https://novita.ai/docs/guides/ai-gradio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Gradio 

> Explore ai-gradio and Novita AI to build interactive AI demos effortlessly with powerful large language models.

AI-gradio simplifies AI development with its intuitive Python package, built on Gradio's framework. Pairing it with Novita AI unlocks powerful capabilities through cutting-edge large language models, which deliver exceptional value through Novita AI's reliable APIs, optimized performance, and cost-effective pricing—all within AI-gradio's user-friendly interface.

This step-by-step guide will access Novita AI's LLMs API on ai-gradio including methods to install ai-gradio and use Novita AI's LLMs in ai-gradio.

## How to Install ai-gradio

```python  theme={"system"}
# Install core package
pip install ai-gradio

# Install with specific provider support
pip install 'ai-gradio[openai]'     # OpenAI support
pip install 'ai-gradio[gemini]'     # Google Gemini support
pip install 'ai-gradio[anthropic]'  # Anthropic Claude support
pip install 'ai-gradio[groq]'       # Groq support

# Install all providers
pip install 'ai-gradio[all]'
```

## How to use Novita AI's LLMs in ai-gradio

### Step 1: Set up environment variables.

* Set NOVITA\_API\_KEY to your Novita API key.

```python  theme={"system"}
export NOVITA_API_KEY=<your api key>
```

### Step 2: Modify the app.py entry file.

```python  theme={"system"}
import gradio as gr
import ai_gradio
gr.load(
    name='novita:deepseek/deepseek-r1',
    src=ai_gradio.registry,
).launch()
```

### Step 3: Run the app.py file with python.[​](https://novita.ai/docs/guides/third-party-langflow-guide#accessing-novita-ai-llm-api-on-langflow)


Built with [Mintlify](https://mintlify.com).