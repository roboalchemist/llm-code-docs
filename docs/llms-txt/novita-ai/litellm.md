# Source: https://novita.ai/docs/guides/litellm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LiteLLM

> Supercharge Your AI Applications with Novita AI and LiteLLM.

LiteLLM is an open-source Python library and proxy server that provides access, spend tracking, and fallbacks to over 100 LLMs through a unified interface in the OpenAI format. By leveraging Novita AI's cutting-edge models, the integration with LiteLLM empowers your AI applications with seamless model switching, dependable fallbacks, and intelligent request routing—all through a standardized completion API that ensures compatibility across multiple providers.

This guide will show you how to quickly get started with integrating Novita AI and LiteLLM, enabling you to set up this powerful combination and streamline your workflow with ease.

## **How to Integrate Novita AI with LiteLLM**

### Step 1: Install LiteLLM

* Install the LiteLLM library using pip to create a unified interface for working with different language models.

```bash  theme={"system"}
pip install litellm
```

### Step 2: Set Up Your API Credentials

* Log in to [the key management page](https://novita.ai/settings/key-management) in Novita AI and click `Add New Key`to generate your API key.

  <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/images/-VisitthekeymanagementpageandselectAddNewKeytogenerateyourAPIkey..png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=ba76fbe63ca9f6246b5b7254ced54252" alt="Visitthekeymanagementpageandselect Add New Keytogenerateyour AP Ikey Pn" width="1280" height="689" data-path="images/-VisitthekeymanagementpageandselectAddNewKeytogenerateyourAPIkey..png" />

### Step 3: Structure Your Basic API Call

* Create a completion request to Novita AI's models through LiteLLM's standardized interface.

```python  theme={"system"}
from litellm import completion
import os

## set ENV variables. Visit https://novita.ai/settings/key-management to get your API key
os.environ["NOVITA_API_KEY"] = "novita-api-key"

response = completion(
  model="novita/deepseek/deepseek-r1",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

### Step 4: Implement Streaming for Better User Experience

* Enable streaming mode for more interactive applications or when handling longer responses.

```python  theme={"system"}
from litellm import completion
import os

## set ENV variables. Visit https://novita.ai/settings/key-management to get your API key
os.environ["NOVITA_API_KEY"] = "novita_api_key"

response = completion(
  model="novita/deepseek/deepseek-r1",
  messages = [{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```


Built with [Mintlify](https://mintlify.com).