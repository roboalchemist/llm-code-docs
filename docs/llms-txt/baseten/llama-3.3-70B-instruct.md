# Source: https://docs.baseten.co/examples/models/llama/llama-3.3-70B-instruct.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Llama 3.3 70B Instruct

> Llama 3.3 70B Instruct is a large language model that is optimized for instruction following.

export const MetaIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M4.13523 13.5079C4.13523 10.377 5.77224 7.10995 7.69395 7.10995C8.76157 7.10995 9.61566 7.72251 10.968 9.56021C9.68683 11.466 8.90391 12.623 8.90391 12.623C7.19573 15.2094 6.62633 15.7539 5.70107 15.7539C4.7758 15.822 4.13523 15.0052 4.13523 13.5079ZM15.3096 12.3508L14.0996 10.445C13.8149 9.96859 13.4591 9.49215 13.1744 9.08377C14.242 7.51832 15.0961 6.70157 16.1637 6.70157C18.2989 6.70157 20.0071 9.7644 20.0071 13.5759C20.0071 15.0052 19.5089 15.822 18.5125 15.822C17.516 15.822 17.1601 15.2094 15.3096 12.3508ZM12.2491 7.72251C10.6833 5.74869 9.33096 5 7.76512 5C4.4911 5 2 9.15183 2 13.5079C2 16.2304 3.35231 17.9319 5.62989 17.9319C7.2669 17.9319 8.40569 17.1832 10.5409 13.644C10.5409 13.644 11.395 12.1466 12.0356 11.1257C12.2491 11.466 12.4626 11.8063 12.6762 12.2147L13.6726 13.8482C15.5943 16.9791 16.6619 18 18.5836 18C20.79 18 22 16.2304 22 13.4398C21.9288 8.81152 19.3665 5 16.3061 5C14.669 5 13.3879 6.22513 12.2491 7.72251Z" fill="#0081FB" />
</svg>} horizontal />;

<MetaIconCard title="Deploy Llama 3.3 70B Instruct" href="https://app.baseten.co/deploy/llama-3-3-70b-instruct" />

# Example usage

Llama is OpenAI compatible and can be called using the OpenAI client.

```python  theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What was the role of Llamas in the Inca empire?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

**JSON Output**

```json  theme={"system"}
["streaming", "output", "text"]
```
