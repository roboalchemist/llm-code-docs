# Source: https://docs.together.ai/docs/openai-api-compatibility.md

> Together's API is compatible with OpenAI's libraries, making it easy to try out our open-source models on existing applications.

# OpenAI Compatibility

Together's API endpoints for chat, vision, images, embeddings, speech are fully compatible with OpenAI's API.

If you have an application that uses one of OpenAI's client libraries, you can easily configure it to point to Together's API servers, and start running your existing applications using our open-source models.

## Configuring OpenAI to use Together's API

To start using Together with OpenAI's client libraries, pass in your Together API key to the `api_key` option, and change the `base_url` to `https://api.together.xyz/v1`:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: "https://api.together.xyz/v1",
  });
  ```
</CodeGroup>

You can find your API key in [your settings page](https://api.together.xyz/settings/api-keys). If you don't have an account, you can [register for free](https://api.together.ai/).

## Querying a chat model

Now that your OpenAI client is configured to point to Together, you can start using one of our open-source models for your inference queries.

For example, you can query one of our [chat models](/docs/serverless-models#chat-models), like Llama 3.1 8B:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
          {
              "role": "system",
              "content": "You are a travel agent. Be descriptive and helpful.",
          },
          {
              "role": "user",
              "content": "Tell me the top 3 things to do in San Francisco",
          },
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await client.chat.completions.create({
    model: 'openai/gpt-oss-20b',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Streaming a response

You can also use OpenAI's streaming capabilities to stream back your response:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  stream = client.chat.completions.create(
      model="Qwen/Qwen3-Next-80B-A3B-Instruct",
      messages=[
          {
              "role": "system",
              "content": "You are a travel agent. Be descriptive and helpful.",
          },
          {"role": "user", "content": "Tell me about San Francisco"},
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  async function run() {
    const stream = await client.chat.completions.create({
      model: 'Qwen/Qwen3-Next-80B-A3B-Instruct',
      messages: [
        { role: 'system', content: 'You are an AI assistant' },
        { role: 'user', content: 'Who won the world series in 2020?' },
      ],
      stream: true,
    });

    for await (const chunk of stream) {
      // use process.stdout.write instead of console.log to avoid newlines
      process.stdout.write(chunk.choices[0]?.delta?.content || '');
    }
  }

  run();
  ```
</CodeGroup>

## Using Vision Models

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What's in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await openai.chat.completions.create({
      model: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages: [{
          role: "user",
          content: [
              { type: "text", text: "What is in this image?" },
              {
                  type: "image_url",
                  image_url: {
                      url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                  },
              },
          ],
      }],
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

Output:

```text Text theme={null}
The image depicts a serene and idyllic scene of a wooden boardwalk winding through a lush, green field on a sunny day.

*   **Sky:**
    *   The sky is a brilliant blue with wispy white clouds scattered across it.
    *   The clouds are thin and feathery, adding to the overall sense of tranquility.
*   **Boardwalk:**
    *   The boardwalk is made of weathered wooden planks, worn smooth by time and use.
    *   It stretches out into the distance, disappearing into the horizon.
    *   The boardwalk is flanked by tall grasses and reeds that reach up to the knees.
*   **Field:**
    *   The field is filled with tall, green grasses and reeds that sway gently in the breeze.
    *   The grasses are so tall that they almost obscure the boardwalk, creating a sense of mystery and adventure.
    *   In the distance, trees and bushes can be seen, adding depth and texture to the scene.
*   **Atmosphere:**
    *   The overall atmosphere is one of peace and serenity, inviting the viewer to step into the tranquil world depicted in the image.
    *   The warm sunlight and gentle breeze create a sense of comfort and relaxation.

In summary, the image presents a picturesque scene of a wooden boardwalk meandering through a lush, green field on a sunny day, evoking feelings of peace and serenity.
```

## Image Generation

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  prompt = """
  A children's book drawing of a veterinarian using a stethoscope to 
  listen to the heartbeat of a baby otter.
  """

  result = client.images.generate(
      model="black-forest-labs/FLUX.1-dev", prompt=prompt
  )

  print(result.data[0].url)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const prompt = `
  A children's book drawing of a veterinarian using a stethoscope to 
  listen to the heartbeat of a baby otter.
  `;

  async function main() {
    const response = await client.images.generate({
      model: "black-forest-labs/FLUX.1-dev",
      prompt: prompt,
    });

    console.log(response.data[0].url);
  }

  main();
  ```
</CodeGroup>

Output:

<div style={{textAlign: 'center'}}>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=840c30380735f6bad166e6fda2c0375b" style={{width: '300px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=12e0c9ecdac254c9a57ef97fe5136ad1 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=95e37cf0394bbb531d4ed1123e2df599 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e3fcdaaa3da32ab990a7af7fa98228a0 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=23629c234356a16d96096fabb9a5f89f 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f1d11281b1809e98b6c28e64139c550c 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c1cf869e56065ef72ed5d1fd432a9c37 2500w" />
</div>

## Text-to-Speech

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  speech_file_path = "speech.mp3"

  response = client.audio.speech.create(
      model="hexgrad/Kokoro-82M",
      input="Today is a wonderful day to build something people love!",
      voice="helpful woman",
  )

  response.stream_to_file(speech_file_path)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';
  import { createWriteStream } from 'fs';
  import { pipeline } from 'stream/promises';

  const client = new OpenAI({
      apiKey: process.env.TOGETHER_API_KEY,
      baseURL: 'https://api.together.xyz/v1',
    });

  const speechFilePath = 'speech.mp3';

  async function main() {
      const response = await client.audio.speech.create({
        model: 'hexgrad/Kokoro-82M',
        input: 'Today is a wonderful day to build!',
        voice: 'helpful woman',
      });

      const buffer = Buffer.from(await response.arrayBuffer());
      await require('fs').promises.writeFile(speechFilePath, buffer);
    }

  main();
  ```
</CodeGroup>

Output:

<iframe src="https://drive.google.com/file/d/1zpUdy_UlCeveGJP1z4ddj_Uh3uKnSovT/preview" />

## Generating vector embeddings

Use our [embedding models](/docs/serverless-models#embedding-models) to generate an embedding for some text input:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.embeddings.create(
      model="togethercomputer/m2-bert-80M-8k-retrieval",
      input="Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  )

  print(response.data[0].embedding)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await client.embeddings.create({
    model: 'togethercomputer/m2-bert-80M-32k-retrieval',
    input: 'Our solar system orbits the Milky Way galaxy at about 515,000 mph',
  });

  console.log(response.data[0].embedding);
  ```
</CodeGroup>

Output

```text Text theme={null}
[0.2633975, 0.13856211, 0.14047204,... ]
```

## Structured Outputs

```python Python theme={null}
from pydantic import BaseModel
from openai import OpenAI
import os, json

client = OpenAI(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
)


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday. Answer in JSON",
        },
    ],
    response_format={
        "type": "json_schema",
        "schema": CalendarEvent.model_json_schema(),
    },
)

output = json.loads(completion.choices[0].message.content)
print(json.dumps(output, indent=2))
```

Output:

```text Text theme={null}
{
  "name": "Alice and Bob",
  "date": "Friday",
  "participants": [
    "Alice",
    "Bob"
  ]
}
```

## Function Calling

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  import os, json

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current temperature for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City and country e.g. Bogotá, Colombia",
                      }
                  },
                  "required": ["location"],
                  "additionalProperties": False,
              },
              "strict": True,
          },
      }
  ]

  completion = client.chat.completions.create(
      model="zai-org/GLM-4.5-Air-FP8",
      messages=[
          {"role": "user", "content": "What is the weather like in Paris today?"}
      ],
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          completion.choices[0].message.model_dump()["tool_calls"], indent=2
      )
  )
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const tools = [{
      "type": "function",
      "function": {
          "name": "get_weather",
          "description": "Get current temperature for a given location.",
          "parameters": {
              "type": "object",
              "properties": {
                  "location": {
                      "type": "string",
                      "description": "City and country e.g. Bogotá, Colombia"
                  }
              },
              "required": [
                  "location"
              ],
              "additionalProperties": false
          },
          "strict": true
      }
  }];

  const completion = await openai.chat.completions.create({
      model: "zai-org/GLM-4.5-Air-FP8",
      messages: [{ role: "user", content: "What is the weather like in Paris today?" }],
      tools,
      store: true,
  });

  console.log(completion.choices[0].message.tool_calls);
  ```
</CodeGroup>

Output:

```text Text theme={null}
[
  {
    "id": "call_nu2ifnvqz083p5kngs3a3aqz",
    "function": {
      "arguments": "{\"location\":\"Paris, France\"}",
      "name": "get_weather"
    },
    "type": "function",
    "index": 0
  }
]
```

## Community libraries

The Together API is also supported by most [OpenAI libraries built by the community](https://platform.openai.com/docs/libraries/community-libraries).

Feel free to [reach out to support](https://www.together.ai/contact) if you come across some unexpected behavior when using our API.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt