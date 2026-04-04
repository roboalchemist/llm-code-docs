# Structured Output
When utilizing LLMs as agents or steps within a lengthy process, chain, or pipeline, it is often necessary for the outputs to adhere to a specific structured format. JSON is the most commonly used format for this purpose.

We offer a reliable method to obtain structured output in your desired format.

Our system includes a built-in mode for JSON output, along with the capability to use custom structured outputs.

:::warning
For JSON mode, it is essential to explicitly instruct the model in your prompt to output JSON and specify the desired format.

Custom structured outputs are more reliable and are recommended whenever possible. However, it is still advisable to iterate on your prompts.  
Use JSON mode when more flexibility in the output is required while maintaining a JSON structure, and customize it if you want to enforce a clearer format to improve reliability.
:::

## Structured Outputs
- [Custom](../custom_structured_output)
- [JSON](../json_mode)


[Text and Chat Completions]
Source: https://docs.mistral.ai/docs/capabilities/text_and_chat_completions

The Mistral models allows you to chat with a model that has been fine-tuned to follow 
instructions and respond to natural language prompts. 
A prompt is the input that you provide to the Mistral model. 
It can come in various forms, such as asking a question, giving an instruction, 
or providing a few examples of the task you want the model to perform. 
Based on the prompt, the Mistral model generates a text output as a response.

The [chat completion API](https://docs.mistral.ai/api/#tag/chat) accepts a list of chat messages as input and 
generates a response. This response is in the form of a new chat message with
the role "assistant" as output, the "content" of each response can either be a `string` or a `list` of chunks with different kinds of chunk types for different features. Visit our [API spec](https://docs.mistral.ai/api) for more details.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

**No streaming**
```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

print(chat_response.choices[0].message.content)
```

**With streaming**
```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

stream_response = client.chat.stream(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

for chunk in stream_response:
    print(chunk.data.choices[0].delta.content)
```

**With async and without streaming**
```python


from mistralai import Mistral
from mistralai.models import UserMessage


async def main():
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    chat_response = await client.chat.complete_async(
        model=model,
        messages=[UserMessage(content="What is the best French cheese?")],
    )

    print(chat_response.choices[0].message.content)


if __name__ == "__main__":
    asyncio.run(main())
```

**With async and with streaming**
```python


from mistralai import Mistral


async def main():
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    response = await client.chat.stream_async(
        model=model,
        messages=[
             {
                  "role": "user",
                  "content": "Who is the best French painter? Answer in JSON.",
              },
        ],
    )
    async for chunk in response:
        if chunk.data.choices[0].delta.content is not None:
            print(chunk.data.choices[0].delta.content, end="")


if __name__ == "__main__":
    asyncio.run(main())
```

  </TabItem>
  <TabItem value="typescript" label="typescript">

**No streaming**
```typescript


dotenv.config();

const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({apiKey: apiKey});

async function main() {
    const chatResponse = await client.chat.complete({
        model: "mistral-large-latest",
        messages: [{role: 'user', content: 'What is the best French cheese?'}]
    });

    console.log('Chat:', chatResponse.choices?.[0]?.message?.content);
}

main();
```

**With streaming**
```typescript


dotenv.config();

const apiKey = process.env["MISTRAL_API_KEY"];

const client = new Mistral({ apiKey: apiKey });

async function main() {

    const result = await client.chat.stream({
        model: "mistral-large-latest",
        messages: [{ role: "user", content: "What is the best French cheese?" }],
    });

    for await (const chunk of result) {
        const streamText = chunk.data.choices[0].delta.content;
        if (typeof streamText === "string") {
            process.stdout.write(streamText);
        }
    }
}

main()
```

  </TabItem>
  <TabItem value="curl" label="curl">
```bash
curl --location "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "mistral-large-latest",
    "messages": [
     {
        "role": "user",
        "content": "What is the best French cheese?"
      }
    ]
  }'
```
  </TabItem>
</Tabs>

## Chat messages

Chat messages (`messages`) are a collection of prompts or messages, with each message having a specific role assigned to it, such as "system," "user," "assistant," or "tool." 

- A _system message_ is an *optional* message that sets the behavior and context for an AI assistant in a 
  conversation, such as modifying its personality or providing specific instructions. A system message can 
  include task instructions, personality traits, contextual information, creativity constraints, and other 
  relevant guidelines to help the AI better understand and respond to the user's input. See the 
  [API reference](../../api) for explanations on how to set up a custom system prompt.
- A _user message_ is a message sent from the perspective of the human in a conversation with an AI assistant. 
  It typically provides a request, question, or comment that the AI assistant should respond to. User prompts 
  allow the human to initiate and guide the conversation, and they can be used to request information, ask for 
  help, provide feedback, or engage in other types of interaction with the AI.
- An _assistant message_ is a message sent by the AI assistant back to the user. It is usually meant to reply to a 
  previous user message by following its instructions, but you can also find it at the beginning of a conversation,
  for example to greet the user.
- A _tool message_ only appears in the context of _function calling_, it is used at the final response formulation
  step when the model has to format the tool call's output for the user. To learn more about function calling, see
  the [guide](../function_calling).


:::tip[When to use `user` prompt vs. `system` message then `user` message?]

- You can either combine your `system` message and `user` message into a single `user` message or separate them into two distinct messages. 
- We recommend you experiment with both ways to determine which one works better for your specific use case. 

:::

## Other useful features

- The `prefix` flag enables prepending content to the assistant's response content. When used in a message, it allows the addition of an assistant's message at the end of the list, which will be prepended to the assistant's response. For more details on how it works see [prefix](/guides/prefix).
- The `safe_prompt` flag is used to force chat completion to be moderated against sensitive content (see [Guardrailing](../guardrailing)).
- A `stop` sequence allows forcing the model to stop generating after one or more chosen tokens or strings.
    <details>
    <summary><b>Stop Sequence Example</b></summary>

    ```bash
    curl --location "https://api.mistral.ai/v1/chat/completions" \
        --header 'Content-Type: application/json' \
        --header 'Accept: application/json' \
        --header "Authorization: Bearer $MISTRAL_API_KEY" \
        --data '{
        "model": "mistral-large-latest",
        "messages": [
        {
            "role": "user",
            "content": "What is the capital of France?"
          }
        ],
        "stop": ["Paris"]
      }'
    ```
    </details>


[Vision]
Source: https://docs.mistral.ai/docs/capabilities/vision

Vision capabilities enable models to analyze images and provide insights based on visual content in addition to text. This multimodal approach opens up new possibilities for applications that require both textual and visual understanding.

For more specific use cases regarding document parsing and data extraction we recommend taking a look at our Document AI stack [here](../OCR/document_ai_overview).

## Models with Vision Capabilities:
- Pixtral 12B (`pixtral-12b-latest`)
- Pixtral Large 2411 (`pixtral-large-latest`)
- Mistral Medium 2505 (`mistral-medium-latest`)
- Mistral Small 2503 (`mistral-small-latest`)

## Passing an Image URL
If the image is hosted online, you can simply provide the URL of the image in the request. This method is straightforward and does not require any encoding.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python

from mistralai import Mistral