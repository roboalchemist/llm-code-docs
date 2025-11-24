# Source: https://dev.writer.com/home/applications-tool-calling.md

# Use no-code agents as tools

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>

You can use deployed [no-code agents](/no-code/introduction) as tools in [chat completions](/api-reference/completion-api/chat-completion) with Palmyra X4 and X5.

This approach allows you to:

* Use no-code agents alongside other tools
* Chain multiple no-code agents together
* Combine outputs with other API calls or business logic

If you don't have a deployed no-code agent, build one with [text generation](/no-code/text-generation) or [research](/no-code/research) capabilities in AI Studio and [deploy it](/no-code/deploying-an-agent) to get an application ID.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Tool structure

To use a no-code agent as a tool, define the tool in a `tools` array when making the request to the [chat endpoint](/home/chat-completion).

The `tools` array contains an object with the following parameters:

| Parameter                        | Type   | Description                                                                                                                      |
| -------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `type`                           | string | The type of tool, which is `function` for a no-code agent                                                                        |
| `function`                       | object | An object containing the tool's description and application ID                                                                   |
| `function.name`                  | string | The name of the tool                                                                                                             |
| `function.description`           | string | A description of what the tool will be used for                                                                                  |
| `function.parameters`            | object | An object containing the tool's input parameters                                                                                 |
| `function.parameters.type`       | string | The string `object`                                                                                                              |
| `function.parameters.properties` | object | An object containing the tool's parameters in the form of a [JSON schema](https://json-schema.org/). See below for more details. |
| `function.parameters.required`   | array  | An array of the tool's required parameters                                                                                       |

### function.parameters.properties

The `function.parameters.properties` object contains the tool's parameter definitions as a [JSON schema](https://json-schema.org/). The object's keys should be the names of the parameters, and the values should be objects containing the parameter's type and description.

When the model decides you should use the tool to answer the user's question, it will return the parameters that you should use when calling the function you've defined.

Below is an example of a tool definition for a no-code agent that generates product descriptions.

<CodeGroup>
  ```python Python theme={null}
  tools = [
      {
          "type": "function",
          "function": {
              "name": "generate_product_description",
              "description": "A function that will invoke an agent for text-generation, specialized in generating product descriptions. Any user request asking for product descriptions should use this tool.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "product_name": {
                          "type": "string",
                          "description": "The name of the product"
                      }
                  },
                  "required": ["product_name"]
              }
          }
      }
  ]
  ```

  ```javascript JavaScript theme={null}
  const tools = [
      {
          type: "function",
          function: {
              name: "generate_product_description",
              description: "A function that will invoke an AI agent for text-generation, specialized in generating product descriptions. Any user request asking for product descriptions should use this tool.",
              parameters: {
                  type: "object",
                  properties: {
                      product_name: {
                          type: "string",
                          description: "The name of the product"
                      }
                  },
                  required: ["product_name"]
              }
          }
      }
  ];
  ```
</CodeGroup>

<Note>
  To help the model understand when to use the tool, follow these best practices for the `function.description` parameter:

  * Indicate that the tool is a function that invokes a no-code agent
  * Specify the agent's purpose and capabilities
  * Describe when the tool should be used

  An example description for a tool that invokes an agent with text-generation:

  > "A function that invokes an AI agent for text-generation, specialized in generating product descriptions. Any user request asking for product descriptions should use this tool."
</Note>

### Response format

When the model decides to use a custom tool, the response from the tool call is returned in the `tool_calls` object. The `tool_calls` object contains the following fields:

| Parameter                          | Type   | Description                                                              |
| ---------------------------------- | ------ | ------------------------------------------------------------------------ |
| `tool_calls[0].id`                 | string | The ID of the tool call                                                  |
| `tool_calls[0].function`           | object | An object containing the function to call                                |
| `tool_calls[0].function.type`      | string | The type of tool, which is `function` for a no-code agent                |
| `tool_calls[0].function.name`      | string | The name of the function to call                                         |
| `tool_calls[0].function.arguments` | string | A JSON-formatted string containing the arguments to pass to the function |

Here is an example of a chat completion response that includes a tool call. In this example, the model decides to use the `generate_product_description` tool to answer the user's question, and provides the arguments to pass to the function.

```json sample response[expandable] {11} theme={null}
{
"content": null,
"refusal": null,
"role": "assistant",
"graph_data": {
"sources": null,
"status": null,
"subqueries": null
},
"llm_data": null,
"tool_calls": [
{
    "id": "chatcmpl-tool-123",
    "function": {
    "arguments": "{\"product_name\": \"Terra running shoe\"}",
    "name": "generate_product_description"
    },
    "type": "function",
    "index": null
}
],
"image_data": null
}
```

## Usage example

The following example demonstrates how to use a no-code agent that performs text generation tasks as a tool in a chat completion. The example uses a hypothetical product description agent, but you can use any no-code agent in this way.

### Create a function that calls your deployed agent

First, create a function that calls your deployed agent. You will use this function if the LLM you're chatting with decides to use the tool.

The function below takes a `product_name` parameter, invokes the no-code agent with the agent's required input fields, and returns the generated product description.

If you are unfamiliar with how to invoke a no-code agent with the SDK, see the [no-code agent guide](/home/applications).

<CodeGroup>
  ```python Python theme={null}
  def generate_product_description(product_name):
      response = client.applications.generate_content(
          application_id="your-application-id",
          inputs=[
              {
                  "id": "Product name",
                  "value": [product_name]
              }
          ]
      )
      return response.suggestion
  ```

  ```javascript JavaScript theme={null}
  async function generateProductDescription(productName) {
      const response = await client.applications.generateContent(
          "your-application-id",
          {
              inputs: [
                  {
                      id: "Product name",
                      value: [productName]
                  }
              ]
          }
      );
      return response.suggestion;
  }
  ```
</CodeGroup>

### Define your agent as a tool

Next, define your agent as a tool so the LLM knows when to use it. See the [tool structure](#tool-structure) section for more details on the tool object.

<CodeGroup>
  ```python Python theme={null}
  tools = [
      {
          "type": "function",
          "function": {
              "name": "generate_product_description",
              "description": "A function that will invoke an agent for text-generation, specialized in generating product descriptions. Any user request asking for product descriptions should use this tool.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "product_name": {
                          "type": "string",
                          "description": "The name of the product"
                      }
                  },
                  "required": ["product_name"]
              }
          }
      }
  ]
  ```

  ```javascript JavaScript theme={null}
  const tools = [
      {
          type: "function",
          function: {
              name: "generate_product_description",
              description: "A function that will invoke an agent for text-generation, specialized in generating product descriptions. Any user request asking for product descriptions should use this tool.",
              parameters: {
                  type: "object",
                  properties: {
                      product_name: {
                          type: "string",
                          description: "The name of the product"
                      }
                  },
                  required: ["product_name"]
              }
          }
      }
  ];
  ```
</CodeGroup>

### Use your agent as a tool in a chat completion

Add the tools array to the chat endpoint call along with your array of messages. Setting `tool_choice` to `auto` allows the model to choose when to use the no-code agent tool, based on the user's question and the description of the tool.

When the model decides to use the tool you've defined, it will indicate that in the `tool_calls` object of the response.

This example uses a non-streaming response. For a streaming implementation, and to learn more about processing custom tool call responses, see the [tool calling guide](/home/tool-calling#processing-tool-calls).

<CodeGroup>
  ```python Python theme={null}
  import json
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `apiKey` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  messages = [{"role": "user", "content": "Generate a description for the Terra running shoe"}]

  # Send the request
  response = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      tools=tools,
      tool_choice="auto",
      stream=False
  )

  # Process the response
  response_message = response.choices[0].message
  # Check if the response contains tool calls,
  #and if so, call the custom function
  tool_calls = response_message.tool_calls
  if tool_calls:
      tool_call = tool_calls[0]
      tool_call_id = tool_call.id
      function_name = tool_call.function.name
      function_args = json.loads(tool_call.function.arguments)

      if function_name == "generate_product_description":
          function_response = generate_product_description(function_args["product_name"])
          
          messages.append({
              "role": "tool",
              "tool_call_id": tool_call_id,
              "name": function_name,
              "content": function_response
          })

  final_response = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      stream=False
  )

  print(final_response.choices[0].message.content)
  # Here's a product description for the Terra running shoe: ...
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{ role: "user", content: "Generate a description for the Terra running shoe" }];

  const response = await client.chat.chat({
      model: "palmyra-x5",
      messages: messages,
      tools: tools,
      tool_choice: "auto",
      stream: false
  });

  const responseMessage = response.choices[0].message;
  const toolCalls = responseMessage.tool_calls;
  // Check if the response contains tool calls,
  // and if so, call the custom function
  if (toolCalls && toolCalls.length > 0) {
      const toolCall = toolCalls[0];
      const toolCallId = toolCall.id;
      const functionName = toolCall.function.name;
      const functionArgs = JSON.parse(toolCall.function.arguments);

      if (functionName === "generate_product_description") {
          const functionResponse = await generateProductDescription(
              functionArgs.product_name
          );
          
          messages.push({
              role: "tool",
              tool_call_id: toolCallId,
              name: functionName,
              content: functionResponse
          });
      }

      const finalResponse = await client.chat.chat({
          model: "palmyra-x5",
          messages: messages,
          stream: false
      });

      console.log(finalResponse.choices[0].message.content);
      // Here's a product description for the Terra running shoe: ...
  }
  ```
</CodeGroup>

Here is the full code example:

<CodeGroup>
  ```python Python [expandable] theme={null}
  import json
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `apiKey` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  def generate_product_description(product_name):
      response = client.applications.generate_content(
          application_id="your-application-id",
          inputs=[
              {
                  "id": "Product name",
                  "value": [product_name]
              }
          ]
      )
      return response.suggestion

  tools = [
      {
          "type": "function",
          "function": {
              "name": "generate_product_description",
              "description": "A function that will invoke an agent for text-generation, specialized in generating product descriptions. Any user request asking for product descriptions should use this tool.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "product_name": {
                          "type": "string",
                          "description": "The name of the product"
                      }
                  },
                  "required": ["product_name"]
              }
          }
      }
  ]

  messages = [{"role": "user", "content": "Generate a description for the Terra running shoe"}]

  # Send the request
  response = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      tools=tools,
      tool_choice="auto",
      stream=False
  )

  # Process the response
  response_message = response.choices[0].message
  # Check if the response contains tool calls,
  #and if so, call the custom function
  tool_calls = response_message.tool_calls
  if tool_calls:
      tool_call = tool_calls[0]
      tool_call_id = tool_call.id
      function_name = tool_call.function.name
      function_args = json.loads(tool_call.function.arguments)

      if function_name == "generate_product_description":
          function_response = generate_product_description(function_args["product_name"])
          
          messages.append({
              "role": "tool",
              "tool_call_id": tool_call_id,
              "name": function_name,
              "content": function_response
          })

  final_response = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      stream=False
  )

  print(final_response.choices[0].message.content)
  # Here's a product description for the Terra running shoe: ...
  ```

  ```javascript JavaScript [expandable] theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  async function generateProductDescription(productName) {
      const response = await client.applications.generateContent(
          "your-application-id",
          {
              inputs: [
                  {
                      id: "Product name",
                      value: [productName]
                  }
              ]
          }
      );
      return response.suggestion;
  }

  const tools = [
      {
          type: "function",
          function: {
              name: "generate_product_description",
              description: "A function that will invoke an agent for text generation, specialized in generating product descriptions. Any user request asking for product descriptions should use this tool.",
              parameters: {
                  type: "object",
                  properties: {
                      product_name: {
                          type: "string",
                          description: "The name of the product"
                      }
                  },
                  required: ["product_name"]
              }
          }
      }
  ];

  const messages = [{ role: "user", content: "Generate a description for the Terra running shoe" }];

  const response = await client.chat.chat({
      model: "palmyra-x5",
      messages: messages,
      tools: tools,
      tool_choice: "auto",
      stream: false
  });

  const responseMessage = response.choices[0].message;
  const toolCalls = responseMessage.tool_calls;
  // Check if the response contains tool calls,
  // and if so, call the custom function
  if (toolCalls && toolCalls.length > 0) {
      const toolCall = toolCalls[0];
      const toolCallId = toolCall.id;
      const functionName = toolCall.function.name;
      const functionArgs = JSON.parse(toolCall.function.arguments);

      if (functionName === "generate_product_description") {
          const functionResponse = await generateProductDescription(
              functionArgs.product_name
          );
          
          messages.push({
              role: "tool",
              tool_call_id: toolCallId,
              name: functionName,
              content: functionResponse
          });
      }

      const finalResponse = await client.chat.chat({
          model: "palmyra-x5",
          messages: messages,
          stream: false
      });

      console.log(finalResponse.choices[0].message.content);
      // Here's a product description for the Terra running shoe: ...
  }
  ```
</CodeGroup>

## Next steps

Now that you've defined a custom tool, learn about prebuilt tools and how to use them in your applications:

* [Ask questions to a Knowledge Graph in a chat](/home/kg-chat)
* [Delegate questions to domain-specific LLMs](/home/model-delegation)
* [Analyze images in a chat](/home/vision-tool)
* [Translate text in a chat](/home/translation-tool)
