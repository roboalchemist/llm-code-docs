# Source: https://exa.ai/docs/reference/openai-sdk.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.


## # OpenAI SDK Compatibility

> Use Exa's endpoints as a drop-in replacement for OpenAI - supporting both chat completions and responses APIs.

***

## Overview

Exa provides OpenAI-compatible endpoints that work seamlessly with the OpenAI SDK:

| Endpoint            | OpenAI Interface     | Models Available                          | Use Case                     |
| ------------------- | -------------------- | ----------------------------------------- | ---------------------------- |
| `/chat/completions` | Chat Completions API | `exa`, `exa-research`, `exa-research-pro` | Traditional chat interface   |
| `/responses`        | Responses API        | `exa-research`, `exa-research-pro`        | Modern, simplified interface |

<Info>
  {" "}

  Exa will parse through your messages and send only the last message to `/answer`
  or `/research`.
</Info>

## Answer

To use Exa's `/answer` endpoint via the chat completions interface:

1. Replace base URL with `https://api.exa.ai`
2. Replace API key with your Exa API key
3. Replace model name with `exa`.

<Info>
  {" "}

  See the full `/answer` endpoint reference [here](/reference/answer).{" "}
</Info>

<Info>
  {" "}

  Need custom behavior when routing through `/answer`? Contact us at [hello@exa.ai](mailto:hello@exa.ai) and we can help tailor the integration.{" "}
</Info>

<CodeGroup>

  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(
    base_url="https://api.exa.ai", # use exa as the base url
    api_key="YOUR_EXA_API_KEY", # update your api key
  )

  completion = client.chat.completions.create(
    model="exa",
    messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What are the latest developments in quantum computing?"}
  ],

  # use extra_body to pass extra parameters to the /answer endpoint

    extra_body={
      "text": True # include full text from sources
    }
  )

  print(completion.choices[0].message.content)  # print the response content
  print(completion.choices[0].message.citations)  # print the citations
```text

  ```javascript JavaScript theme={null}
  import OpenAI from "openai";

  const openai = new OpenAI({
    baseURL: "https://api.exa.ai", // use exa as the base url
    apiKey: "YOUR_EXA_API_KEY", // update your api key
  });

  async function main() {
    const completion = await openai.chat.completions.create({
      model: "exa",
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        {
          role: "user",
          content: "What are the latest developments in quantum computing?",
        },
      ],
      store: true,
      stream: true,
      extra_body: {
        text: true, // include full text from sources
      },
    });

    for await (const chunk of completion) {
      console.log(chunk.choices[0].delta.content);
    }
  }

  main();
```text

  ```bash Curl theme={null}
  curl https://api.exa.ai/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $YOUR_EXA_API_KEY" \
    -d '{
      "model": "exa",
      "messages": [
        {
          "role": "system",
          "content": "You are a helpful assistant."
        },
        {
          "role": "user",
          "content": "What are the latest developments in quantum computing?"
        }
      ],
      "extra_body": {
        "text": true
      }
    }'
```text

</CodeGroup>

## Research

To use Exa's research models via the chat completions interface:

1. Replace base URL with `https://api.exa.ai`
2. Replace API key with your Exa API key
3. Replace model name with `exa-research` or `exa-research-pro`

<Info>
  {" "}

  See the full `/research` endpoint reference [here](/reference/research/create-a-task).{" "}
</Info>

<CodeGroup>

  ```python Python theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.exa.ai",
      api_key=os.environ["EXA_API_KEY"],
  )

  completion = client.chat.completions.create(
      model="exa-research", # or exa-research-pro
      messages=[
          {"role": "user", "content": "What makes some LLMs so much better than others?"}
      ],
      stream=True,
  )

  for chunk in completion:
      if chunk.choices and chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="", flush=True)
```text

  ```javascript JavaScript theme={null}
  import { OpenAI } from "openai";

  async function main() {
    const openai = new OpenAI({
      apiKey: process.env.EXA_API_KEY,
      baseURL: "https://api.exa.ai",
    });

    const stream = await openai.chat.completions.create({
      model: "exa-research", // or exa-research-pro
      messages: [
        {
          role: "user",
          content: "What are ants",
        },
      ],
      stream: true,
    });

    for await (const chunk of stream) {
      const content = chunk.choices?.[0]?.delta?.content;
      if (content) {
        process.stdout.write(content);
      }
    }
  }

  main().catch((err) => {
    console.error("Chat completion example failed:", err);
    process.exit(1);
  });
```text

  ```bash Curl theme={null}
  curl https://api.exa.ai/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $YOUR_EXA_API_KEY" \
    -d '{
      "model": "exa-research",
      "messages": [
        {
          "role": "user",
          "content": "What makes some LLMs so much better than others?"
        }
      ],
      "stream": true
    }'
```text

</CodeGroup>

## Research via Responses API

You can also access Exa's research models using OpenAI's newer Responses API format:

<CodeGroup>

  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.exa.ai",
      api_key="YOUR_EXA_API_KEY"
  )

  response = client.responses.create(
      model="exa-research",  # or "exa-research-pro"
      input="Summarize the impact of CRISPR on gene therapy with recent developments"
  )

  print(response.output)
```text

  ```javascript JavaScript theme={null}
  import OpenAI from "openai";

  const openai = new OpenAI({
    baseURL: "https://api.exa.ai",
    apiKey: "YOUR_EXA_API_KEY",
  });

  async function main() {
    const response = await openai.responses.create({
      model: "exa-research", // or "exa-research-pro"
      input:
        "Summarize the impact of CRISPR on gene therapy with recent developments",
    });

    console.log(response.output);
  }

  main();
```text

  ```bash cURL theme={null}
  curl --location 'https://api.exa.ai/responses' \
  --header 'x-api-key: YOUR_EXA_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
      "input": "Summarize the impact of CRISPR on gene therapy with recent developments",
      "model": "exa-research"
  }'
```text

</CodeGroup>

<Note>
  The Responses API provides a simpler interface for single-turn research tasks.
  For more details on using Exa with OpenAI's Responses API, including web
  search tool integration, see the [OpenAI Responses API
  guide](/reference/openai-responses-api-with-exa).
</Note>

## Chat Wrapper

Exa provides a Python wrapper that automatically enhances any OpenAI chat completion with RAG capabilities. With one line of code, you can turn any OpenAI chat completion into an Exa-powered RAG system that handles search, chunking, and prompting automatically.

<CodeGroup>

  ```python Python theme={null}
  from openai import OpenAI
  from exa_py import Exa

  # Initialize clients
  openai = OpenAI(api_key='OPENAI_API_KEY')
  exa = Exa('EXA_API_KEY')

  # Wrap the OpenAI client
  exa_openai = exa.wrap(openai)

  # Use exactly like the normal OpenAI client

  completion = exa_openai.chat.completions.create(
      model="gpt-4o",
      messages=[{"role": "user", "content": "What is the latest climate tech news?"}]
  )

  print(completion.choices[0].message.content)
```text

</CodeGroup>

The wrapped client works exactly like the native OpenAI client, except it automatically improves your completions with relevant search results when needed.

The wrapper supports any parameters from the `exa.search()` function.

```python  theme={null}
completion = exa_openai.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    use_exa="auto",              # "auto", "required", or "none"
    num_results=5,               # defaults to 3
    result_max_len=1024,         # defaults to 2048 characters
    include_domains=["arxiv.org"],
    category="research paper",
    start_published_date="2019-01-01"
)
```text
