# Source: https://docs.aimlapi.com/capabilities/image-to-text-vision.md

# Vision in Text Models (Image-To-Text)

This article describes a specific capability of text models: vision, which enables image-to-text conversion. A list of models that support it is provided at the end of this page.

## Example

{% code overflow="wrap" %}

```python
import requests
import json

url = "https://api.aimlapi.com/chat/completions"

payload = json.dumps({
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>'
}

response = requests.post(url, headers=headers, data=payload)
print(response.json())

```

{% endcode %}

## Text Models That Support Vision

* [alibaba/qwen3-vl-32b-instruct](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-vl-32b-instruct)
* [alibaba/qwen3-vl-32b-thinking](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen3-vl-32b-thinking)
* [claude-3-haiku-20240307](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3-haiku)
* [claude-3-opus-20240229](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3-opus)
* [claude-3-5-haiku-20241022](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3.5-haiku)
* [claude-3-7-sonnet-20250219](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-3.7-sonnet)
* [claude-sonnet-4-20250514](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4-sonnet)
* [claude-opus-4-20250514](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4-opus)
* [anthropic/claude-opus-4.1](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-opus-4.1)
* [anthropic/claude-sonnet-4.5](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4-5-sonnet)
* [anthropic/claude-opus-4-5](https://docs.aimlapi.com/api-references/text-models-llm/anthropic/claude-4.5-opus)
* [gemini-2.0-flash-exp](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash-exp)
* [google/gemini-2.0-flash](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash)
* [google/gemini-2.5-flash](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.5-flash)
* [google/gemini-2.5-pro](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.5-pro)
* [google/gemma-3-4b-it](https://docs.aimlapi.com/api-references/text-models-llm/google/gemma-3)
* [google/gemma-3-27b-it](https://docs.aimlapi.com/api-references/text-models-llm/google/gemma-3)
* [meta-llama/Llama-Guard-3-11B-Vision-Turbo](https://docs.aimlapi.com/api-references/moderation-safety-models/meta/llama-guard-3-11b-vision-turbo)
* [meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/meta-llama-3.1-405b-instruct-turbo)
* [meta-llama/llama-4-scout](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-4-maverick)
* [meta-llama/llama-4-maverick](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-4-maverick)
* [MiniMax-Text-01](https://docs.aimlapi.com/api-references/text-models-llm/minimax/text-01)
* [chatgpt-4o-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4-turbo](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-turbo)
* [gpt-4-turbo-2024-04-09](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-turbo)
* [gpt-4o](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-05-13](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-08-06](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini)
* [gpt-4o-mini-2024-07-18](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini)
* [openai/gpt-4.1-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1)
* [openai/gpt-4.1-mini-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1-mini)
* [openai/gpt-4.1-nano-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1-nano)
* [openai/o4-mini-2025-04-16](https://docs.aimlapi.com/api-references/text-models-llm/openai/o4-mini)
* [openai/o3-2025-04-16](https://docs.aimlapi.com/api-references/text-models-llm/openai/o3)
* [o1](https://docs.aimlapi.com/api-references/text-models-llm/openai/o1)
* [openai/gpt-5-2025-08-07](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5)
* [openai/gpt-5-mini-2025-08-07](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-mini)
* [openai/gpt-5-nano-2025-08-0](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-nano)
* [openai/gpt-5-chat-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-chat)
* ​[openai/gpt-5-1​](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1)
* [​openai/gpt-5-1-chat-latest​](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1-chat-latest)
* [​openai/gpt-5-1-codex​](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1-codex)
* [​openai/gpt-5-1-codex-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-1-codex-mini)
* [openai/gpt-5-2](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5.2)
* [openai/gpt-5-2-chat-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5.2-chat-latest)
* [perplexity/sonar](https://docs.aimlapi.com/api-references/text-models-llm/perplexity/sonar)
* [perplexity/sonar-pro](https://docs.aimlapi.com/api-references/text-models-llm/perplexity/sonar-pro)
* [x-ai/grok-4-fast-non-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-fast-non-reasoning)
* [x-ai/grok-4-fast-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-fast-reasoning)
* [x-ai/grok-4-1-fast-non-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-1-fast-non-reasoning)
* [x-ai/grok-4-1-fast-reasoning](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-4-1-fast-reasoning)
