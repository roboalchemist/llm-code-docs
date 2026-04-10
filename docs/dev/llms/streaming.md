# Source: https://dev.writer.com/home/streaming.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream responses from the API

> Stream API responses in real-time with Server-Sent Events. Reduce latency and display generated content as it's created for better user experience.

The Writer API supports streaming responses from the API. Streams use [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents) so that you can display content as the API generates it in real time.

Streaming improves user experience by reducing latency from the time the user submits a request to the time the response is available.

## Overview

To stream a response from the API, set the `stream` parameter to `true` in the request body.

The following endpoints support streaming:

* [Text generation](/api-reference/completion-api/text-generation#body-stream)
* [Chat completions](/api-reference/completion-api/chat-completion#body-stream)
* [Generate from no-code agent](/api-reference/application-api/applications#body-stream): Currently, only no-code research agents support streaming.
* [Knowledge Graph question](/api-reference/kg-api/question#body-stream)
* [Web search](/home/web-search#streaming-response)

## Sample request and response

The code below shows a streaming request and response from a text generation request using `curl`. The response is a stream of [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents).

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/completions' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --data '{
    "model": "palmyra-x5",
    "prompt": "Respond to a customer chat request about a delayed shipment with a message that apologizes for the delay, offers a tracking number, and provides a new estimated delivery date.",
    "stream": true
  }'
  ```
</CodeGroup>

```json response theme={null}
data: {"value":""}

data: {"value":"Hello"}

data: {"value":" ["}

data: {"value":"Customer"}

data: {"value":"'s"}

data: {"value":" Name"}
...
```

<Note>
  If you're using the chat completions endpoint instead of text generation, the streamed response format is slightly different. The content for each chunk appears in `choices[0].delta.content`. See the [Generate chat completions](/home/chat-completion#streaming-response) guide for the full streaming response object.
</Note>

## Streaming with SDKs

When you stream a response using a Writer SDK, the SDK creates an iterator that yields chunks of the response. You can iterate over the stream to receive the response.

See below for examples of streaming with the Python and JavaScript SDKs for each endpoint that supports streaming.

<Tabs>
  <Tab title="Text Generation">
    <CodeGroup>
      ```python Python theme={null}
      from writerai import Writer

      # Initialize the client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      text_generation = client.completions.create(
        model="palmyra-x5",
        prompt="Respond to a customer chat request about a delayed shipment with a message that apologizes for the delay, offers a tracking number, and provides a new estimated delivery date.",
        stream=True
      )

      for chunk in text_generation:
          if chunk.value:  # Only print non-empty chunks
              print(chunk.value, end="", flush=True)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from 'writer-sdk';

      // Initialize the client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const stream = await client.completions.create({
        model: 'palmyra-x5',
        prompt: 'Respond to a customer chat request about a delayed shipment with a message that apologizes for the delay, offers a tracking number, and provides a new estimated delivery date.',
        stream: true 
      });

      for await (const chunk of stream) {
        process.stdout.write(chunk.value);
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions">
    <CodeGroup>
      ```python Python theme={null}
      from writerai import Writer

      # Initialize the client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      stream = client.chat.chat(
        model="palmyra-x5",
        messages=[{"role": "user", "content": "Respond to a customer chat request about a delayed shipment with a message that apologizes for the delay, offers a tracking number, and provides a new estimated delivery date."}],
        stream=True
      )

      for chunk in stream:
          if chunk.choices[0].delta.content:
              print(chunk.choices[0].delta.content, end="", flush=True)
      ```

      ```javascript JavaScript     theme={null}
      import { Writer } from 'writer-sdk';

      // Initialize the client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const stream = await client.chat.chat({
        model: 'palmyra-x5',
        messages: [{ role: 'user', content: 'Respond to a customer chat request about a delayed shipment with a message that apologizes for the delay, offers a tracking number, and provides a new estimated delivery date.' }],
        stream: true 
      });

      for await (const chunk of stream) {
        if (chunk.choices[0]?.delta?.content) {
          process.stdout.write(chunk.choices[0].delta.content);
        }
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Generate from no-code agent">
    <CodeGroup>
      ```python Python theme={null}
      from writerai import Writer

      # Initialize the client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      stream = client.applications.generate_content(
          application_id="<application-id>",
          inputs=[
              {
                  "id": "query",
                  "value": ["Provide a list of three hotels in San Francisco near Union Square within the price range of $100 to $200 per night"]
              }
          ],
          stream=True
      )

      for chunk in stream:
          if chunk.delta.content:
              print(chunk.delta.content, end="", flush=True)
          elif chunk.delta.stages:
              print(chunk.delta.stages[0].content)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from 'writer-sdk';

      // Initialize the client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const stream = await client.applications.generateContent(
          "<application-id>", 
          { 
              inputs: [
                  {
                      id: "query",
                      value: ["Provide a list of three hotels in San Francisco near Union Square within the price range of $100 to $200 per night"]
                  }
              ],
              stream: true
          } 
      );

      for await (const chunk of stream) {
          if (chunk.delta.content) {
              process.stdout.write(chunk.delta.content);
          } else if (chunk.delta.stages) {
              process.stdout.write(chunk.delta.stages[0].content);
          }
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Knowledge Graph question">
    <CodeGroup>
      ```python Python theme={null}
      from writerai import Writer

      # Initialize the client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      stream = client.graphs.question(
          graph_ids=["<graph-id>"],
          question="What is the generic name for the drug Bavencio?",
          stream=True
      )

      for chunk in stream:
          if chunk.answer:  # Only print non-empty answers
              print(chunk.answer, end="", flush=True)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from 'writer-sdk';

      // Initialize the client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const stream = await client.graphs.question({
          graph_ids: ["<graph-id>"],
          question: "What is the generic name for the drug Bavencio?",
          stream: true
      });

      for await (const chunk of stream) {
          process.stdout.write(chunk.answer);
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Streaming helpers for chat completions

The Python and Node SDKs include streaming helpers for chat completions. These helpers provide more granular details about the streaming events and accumulate the response.

To use the streaming helpers, call `client.chat.stream`. Then, include all the same parameters as you would for a non-streaming chat completion request, except omit the `stream` parameter.

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  with client.chat.stream(
    model="palmyra-x5",
    messages=[{"role": "user", "content": "Respond to a customer chat request about a delayed shipment with a message that apologizes for the delay, offers a tracking number, and provides a new estimated delivery date."}]
  ) as stream:
      for event in stream:
          if event.type == "content.delta":
              print(event.delta, end="", flush=True)

  # print the final response
  completion = stream.get_final_completion()
  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const stream = client.chat.stream({
    model: 'palmyra-x5',
    messages: [{ role: 'user', content: 'Respond to a customer chat request about a delayed shipment with a message that apologizes for the delay, offers a tracking number, and provides a new estimated delivery date.' }],
  })
  .on('content', (diff) => process.stdout.write(diff));

  // print the final response
  const completion = await stream.finalChatCompletion();
  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

For more information about the streaming helpers for chat completions, see the [Python](https://github.com/writer/writer-python/blob/main/helpers.md) and [Node](https://github.com/writer/writer-node/blob/main/helpers.md) SDKs.
