# Source: https://docs.together.ai/docs/chat-overview.md

> Learn how to query our open-source chat models.

# Chat

## Playground

The Playground is a web application offered by Together AI to allow our customers to run inference without having to use our API. The playground can be used with standard models, or a selection of fine-tuned models.

You can access the Playground at [api.together.xyz/playground](https://api.together.xyz/playground).

## API Usage

You can use Together's APIs to send individual queries or have long-running conversations with chat models. You can also configure a system prompt to customize how a model should respond.

Queries run against a model of your choice. For most use cases, we recommend using Meta Llama 3.

## Running a single query

Use `chat.completions.create` to send a single query to a chat model:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: "What are some fun things to do in New York?" }],
  });

  console.log(response.choices[0].message.content)
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	]
       }'
  ```
</CodeGroup>

The `create` method takes in a model name and a `messages` array. Each `message` is an object that has the content of the query, as well as a role for the message's author.

In the example above, you can see that we're using "user" for the role. The "user" role tells the model that this message comes from the end user of our system – for example, a customer using your chatbot app.

The other two roles are "assistant" and "system", which we'll talk about next.

## Having a long-running conversation

Every query to a chat model is self-contained. This means that new queries won't automatically have access to any queries that may have come before them. This is exactly why the "assistant" role exists.

The "assistant" role is used to provide historical context for how a model has responded to prior queries. This makes it perfect for building apps that have long-running conversations, like chatbots.

To provide a chat history for a new query, pass the previous messages to the `messages` array, denoting the user-provided queries with the "user" role, and the model's responses with the "assistant" role:

<CodeGroup>
  ```python Python theme={null}
  import os
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          },
          {
              "role": "assistant",
              "content": "You could go to the Empire State Building!",
          },
          {"role": "user", "content": "That sounds fun! Where is it?"},
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [
      { role: "user", content: "What are some fun things to do in New York?" },
      { role: "assistant", content: "You could go to the Empire State Building!"},
      { role: "user", content: "That sounds fun! Where is it?" },
    ],
  });

  console.log(response.choices[0].message.content);
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
          {"role": "user", "content": "What are some fun things to do in New York?"},
          {"role": "assistant", "content": "You could go to the Empire State Building!"},
          {"role": "user", "content": "That sounds fun! Where is it?" }
       	]
       }'
  ```
</CodeGroup>

How your app stores historical messages is up to you.

## Customizing how the model responds

While you can query a model just by providing a user message, typically you'll want to give your model some context for how you'd like it to respond. For example, if you're building a chatbot to help your customers with travel plans, you might want to tell your model that it should act like a helpful travel guide.

To do this, provide an initial message that uses the "system" role:

<CodeGroup>
  ```python Python theme={null}
  import os
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {"role": "system", "content": "You are a helpful travel guide."},
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          },
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [
      {"role": "system", "content": "You are a helpful travel guide."},
      { role: "user", content: "What are some fun things to do in New York?" },
    ],
  });

  console.log(response.choices[0].message.content);
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "system", "content": "You are a helpful travel guide."},
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	]
       }'
  ```
</CodeGroup>

## Streaming responses

Since models can take some time to respond to a query, Together's APIs support streaming back responses in chunks. This lets you display results from each chunk while the model is still running, instead of having to wait for the entire response to finish.

To return a stream, set the `stream` option to true.

<CodeGroup>
  ```python Python theme={null}
  import os
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```

  ```shell HTTP theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	],
        "stream": true
       }'
       
  ## Response will be a stream of Server-Sent Events with JSON-encoded payloads. For example:
  ## 
  ## data: {"choices":[{"index":0,"delta":{"content":" A"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":330,"text":" A","logprob":1,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}
  ## data: {"choices":[{"index":0,"delta":{"content":":"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":28747,"text":":","logprob":0,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}
  ## data: {"choices":[{"index":0,"delta":{"content":" Sure"}}],"id":"85ffbb8a6d2c4340-EWR","token":{"id":12875,"text":" Sure","logprob":-0.00724411,"special":false},"finish_reason":null,"generated_text":null,"stats":null,"usage":null,"created":1709700707,"object":"chat.completion.chunk"}
  ```
</CodeGroup>

## A note on async support in Python

Since I/O in Python is synchronous, multiple queries will execute one after another in sequence, even if they are independent.

If you have multiple independent calls that you want to run in parallel, you can use our Python library's `AsyncTogether` module:

```python Python theme={null}
import os, asyncio
from together import AsyncTogether

async_client = AsyncTogether()
messages = [
    "What are the top things to do in San Francisco?",
    "What country is Paris in?",
]


async def async_chat_completion(messages):
    async_client = AsyncTogether(api_key=os.environ.get("TOGETHER_API_KEY"))
    tasks = [
        async_client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": message}],
        )
        for message in messages
    ]
    responses = await asyncio.gather(*tasks)

    for response in responses:
        print(response.choices[0].message.content)


asyncio.run(async_chat_completion(messages))
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt