# Source: https://docs.baseten.co/examples/models/gemma/gemma-3-27b-it.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemma 3 27B IT

> Instruct-tuned open model by Google with excellent ELO/size tradeoff and vision capabilities

export const GoogleIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M23 12.245C23 11.34 22.925 10.68 22.764 9.995H12.224V14.078H18.41C18.286 15.092 17.613 16.62 16.116 17.647L16.095 17.783L19.427 20.313L19.657 20.335C21.779 18.417 23 15.593 23 12.245Z" fill="#4285F4" />
<path d="M12.225 23C15.255 23 17.799 22.022 19.658 20.335L16.116 17.647C15.168 18.295 13.896 18.747 12.225 18.747C10.8164 18.7471 9.44319 18.3063 8.29791 17.4863C7.15263 16.6664 6.29277 15.5084 5.83899 14.175L5.70699 14.186L2.24199 16.814L2.19699 16.938C4.04299 20.531 7.83499 23 12.225 23Z" fill="#34A853" />
<path d="M5.84 14.175C5.59404 13.4761 5.46662 12.7409 5.463 12C5.463 11.242 5.601 10.509 5.824 9.825L5.818 9.678L2.31 7.008L2.195 7.062C1.41079 8.58997 1.00119 10.2825 1 12C1 13.772 1.436 15.447 2.197 16.938L5.84 14.175Z" fill="#FBBC05" />
<path d="M12.225 5.253C14.333 5.253 15.754 6.145 16.565 6.891L19.732 3.86C17.787 2.088 15.255 1 12.225 1C7.83399 1 4.04299 3.469 2.19699 7.062L5.82699 9.825C6.28468 8.49166 7.14717 7.33445 8.29413 6.51484C9.44108 5.69522 10.8153 5.25409 12.225 5.253Z" fill="#EB4335" />
</svg>} horizontal />;

<GoogleIconCard title="Deploy Gemma 3 27B IT" href="https://app.baseten.co/deploy/gemma_3_27b_it" />

# Example usage

Gemma 3 is an OpenAI-compatible model and can be called using the OpenAI SDK in any language.

```python  theme={"system"}
from openai import OpenAI
import os

model_url = "" # Copy in from API pane in Baseten model dashboard

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url=model_url
)

# Chat completion
response_chat = client.chat.completions.create(
    model="",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://picsum.photos/id/237/200/300",
                },
            },
        ],
    }],
    temperature=0.3,
    max_tokens=512,
)
print(response_chat)
```

**JSON Output**

```json  theme={"system"}
{
  "id": "143",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "[Model output here]",
        "role": "assistant",
        "audio": null,
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1741224586,
  "model": "",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "completion_tokens": 145,
    "prompt_tokens": 38,
    "total_tokens": 183,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```
