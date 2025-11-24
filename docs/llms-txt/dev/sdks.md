# Source: https://dev.writer.com/home/sdks.md

# SDKs

> Install and use Writer SDKs for Python and Node.js. Get started with code examples and learn how to integrate Writer AI into your applications.

This guide helps you get started with the Writer SDKs. Follow these steps to install the SDKs and perform basic operations.

### Prerequisites

<Tabs>
  <Tab title="Python SDK">
    * Python 3.7+
    * [pip](https://pypi.org/project/pip/)
    * A Writer API key
  </Tab>

  <Tab title="Node SDK">
    * Node.js
    * [`npm`](https://www.npmjs.com/get-npm)
    * A Writer API key
  </Tab>
</Tabs>

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

### Install the SDK

Open your terminal or command prompt and install the Writer SDK:

<CodeGroup>
  ```sh Python theme={null}
  pip install writer-sdk
  ```

  ```sh Node theme={null}
  npm install writer-sdk
  ```
</CodeGroup>

## Initialize the client

To initialize the client, import the Writer SDK and create an instance of the `Writer` class.

We recommend setting your API key in an environment variable called `WRITER_API_KEY`. When you initialize the Writer client, the client looks for the `WRITER_API_KEY` environment variable automatically. You can also pass your API key directly to the client.

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()
  ```

  ```js JavaScript theme={null}
  import { Writer } from 'writer-sdk';
  // Initialize the client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();
  ```
</CodeGroup>

## Make a chat completion request

Once you've initialized the client, you can make a request to the Writer API. The following example shows how to make a [chat completion request](/home/chat-completion) to generate a poem:

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  client = Writer()

  response = client.chat.chat(
      messages=[{ "content": "Write a short poem about Python", "role": 'user' }],
      model="palmyra-x5"
  )

  print(response.choices[0].message.content)
  ```

  ```js JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  const client = new Writer();

  const response = await client.chat.chat({
      messages: [{ content: "Write a short poem about JavaScript", role: 'user' }],
      model: "palmyra-x5"
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Next steps

Now that you're set up with the SDKs, start building with [chat completions](/home/chat-completion) or [text generation](/home/text-generation).

You can also use the [API reference](/api-reference) to learn more detailed information about available endpoints.
