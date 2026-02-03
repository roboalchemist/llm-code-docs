# Source: https://dev.writer.com/api-reference/tool-api/comprehend-medical.md

# Source: https://dev.writer.com/api-reference/migration-guides/comprehend-medical.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from medical comprehend API to LLM tool

This guide shows you how to migrate from the deprecated [medical comprehend API endpoint](/api-reference/tool-api/comprehend-medical) to chat completions that can [delegate medical analysis tasks to the `palmyra-med` model](/home/model-delegation). After completing these steps, you can analyze medical text using the `palmyra-med` model, which provides medical analysis capabilities within a chat completion workflow.

## Compare the APIs

The medical comprehend API and the LLM tool with the `palmyra-med` model both provide medical text analysis capabilities, but the LLM tool integrates medical analysis into conversational workflows and supports more flexible configuration and output options. The table below compares the two approaches.

| Aspect                | Medical comprehend API                                                                               | LLM tool with `palmyra-med` model                                                                                                                                                                                                                                        |
| --------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Endpoint**          | `/v1/tools/comprehend/medical`                                                                       | `/v1/chat` with [LLM tool specification](/home/model-delegation) in the `tools` array                                                                                                                                                                                    |
| **Request structure** | Pass text and analysis parameters such as `content` and `response_type` directly in the request body | Provide the medical text as part of the conversation `messages` and specify the analysis tool and model in the `tools` array. Additional parameters (such as custom instructions or output schema) are included in the tool configuration, not as direct request fields. |
| **Response format**   | Structured JSON with a fixed schema (predefined medical entities and types)                          | Answer in `choices[0].message.content` as either natural language or structured JSON (including custom schemas or user-defined formats)                                                                                                                                  |
| **Parameter control** | Explicit API parameters for each entity and type supported by the API                                | Most analysis details are defined by the message prompt and tool configuration; you can specify formats, schema, or request conversational output as needed                                                                                                              |

## Choose your migration approach

Choose your migration approach based on the type of output you need:

* Select the [LLM tool with structured output](/home/structured-output) if you require clearly defined, machine-readable results (for example, extracting predefined medical entities like `RxNorm`, `ICD-10-CM`, or `SNOMED CT`). This option closely matches the original medical comprehend API response format and is best for downstream systems that depend on standardized data.

* Choose conversational analysis with natural language responses if your use case benefits from more flexible or descriptive outputs, or if you want to define your own entity or analysis formats that are not supported by the original API. This approach is ideal for interactive workflows or when you want the model to summarize, explain, or provide guidance in plain language.

### Extract entities and generate structured output

If you need structured entity extraction similar to the medical comprehend API, use the [structured output feature](/home/structured-output) with the LLM tool to get JSON responses:

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/chat' \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --data '{
      "model": "palmyra-x5",
      "messages": [
        {
          "role": "user",
          "content": "Extract medical entities from this text: the symptoms are soreness, a temperature and cough"
        }
      ],
      "tool_choice": "auto",
      "tools": [
        {
          "type": "llm",
          "function": {
            "description": "A function that invokes the Palmyra Med model, specialized in analyzing medical text. Any user request for medical analysis should use this tool.",
            "model": "palmyra-med"
          }
        }
      ],
      "response_format": {
        "type": "json_schema",
        "json_schema": {
          "name": "medical_entities",
          "schema": {
            "type": "object",
            "properties": {
              "entities": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "text": {"type": "string"},
                    "category": {"type": "string"},
                    "score": {"type": "number"}
                  },
                  "required": ["text", "category", "score"],
                  "additionalProperties": false
                }
              }
            },
            "required": ["entities"],
            "additionalProperties": false
          },
          "strict": true
        }
      }
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  messages = [{"role": "user", "content": "Extract medical entities from this text: the symptoms are soreness, a temperature and cough"}]

  tools = [{
    "type": "llm",
    "function": {
      "description": "A function that invokes the Palmyra Med model, specialized in analyzing medical text. Any user request for medical analysis should use this tool.",
      "model": "palmyra-med"
    }
  }]

  # The response_format below configures the API to return structured data
  # in a predefined JSON schema matching expected entities: an array of objects with text, category, and score fields.
  response_format = {
    "type": "json_schema",
    "json_schema": {
      "name": "medical_entities",
      "schema": {
        "type": "object",
        "properties": {
          "entities": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "text": {"type": "string"},
                "category": {"type": "string"},
                "score": {"type": "number"}
              },
              "required": ["text", "category", "score"],
              "additionalProperties": False
            }
          }
        },
        "required": ["entities"],
        "additionalProperties": False
      },
      "strict": True
    }
  }

  response = client.chat.chat(
    model="palmyra-x5", 
    messages=messages, 
    tools=tools,
    tool_choice="auto",
    response_format=response_format  # Ensures the output matches the medical_entities schema above
  )

  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "Extract medical entities from this text: the symptoms are soreness, a temperature and cough"}];

  const tools = [{
    type: "llm",
    function: {
      description: "A function that invokes the Palmyra Med model, specialized in analyzing medical text. Any user request for medical analysis should use this tool.",
      model: "palmyra-med"
    }
  }];

  /*
    The responseFormat object below configures the API to return a machine-readable, structured JSON response
    matching this schema:
      {
        "entities": [
          {
            "text": "...",
            "category": "...",
            "score": ...
          }
        ]
      }
    Each extracted entity contains the fields text, category, and score.
  */
  const responseFormat = {
    type: "json_schema",
    json_schema: {
      name: "medical_entities",
      schema: {
        type: "object",
        properties: {
          entities: {
            type: "array",
            items: {
              type: "object",
              properties: {
                text: {type: "string"},
                category: {type: "string"},
                score: {type: "number"}
              },
              required: ["text", "category", "score"],
              additionalProperties: false
            }
          }
        },
        required: ["entities"],
        additionalProperties: false
      },
      strict: true
    }
  };

  const response = await client.chat.chat({
    model: "palmyra-x5", 
    messages: messages, 
    tools: tools,
    tool_choice: "auto",
    response_format: responseFormat // Request the response as structured JSON for downstream processing
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

### Analyze medical text with natural language responses

If you need conversational medical analysis and interpretation, use the LLM tool without structured output:

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/chat' \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --data '{
      "model": "palmyra-x5",
      "messages": [
        {
          "role": "user",
          "content": "Analyze the following medical text and identify key symptoms and conditions: the symptoms are soreness, a temperature and cough"
        }
      ],
      "tool_choice": "auto",
      "tools": [
        {
          "type": "llm",
          "function": {
            "description": "A function that invokes the Palmyra Med model, specialized in analyzing medical text and providing medical insights. Any user request for medical analysis should use this tool.",
            "model": "palmyra-med"
          }
        }
      ]
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  messages = [{"role": "user", "content": "Analyze the following medical text and identify key symptoms and conditions: the symptoms are soreness, a temperature and cough"}]

  tools = [{
    "type": "llm",
    "function": {
      "description": "A function that invokes the Palmyra Med model, specialized in analyzing medical text and providing medical insights. Any user request for medical analysis should use this tool.",
      "model": "palmyra-med"
    }
  }]

  response = client.chat.chat(
    model="palmyra-x5", 
    messages=messages, 
    tools=tools,
    tool_choice="auto"
  )

  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "Analyze the following medical text and identify key symptoms and conditions: the symptoms are soreness, a temperature and cough"}];

  const tools = [{
    type: "llm",
    function: {
      description: "A function that invokes the Palmyra Med model, specialized in analyzing medical text and providing medical insights. Any user request for medical analysis should use this tool.",
      model: "palmyra-med"
    }
  }];

  const response = await client.chat.chat({
    model: "palmyra-x5", 
    messages: messages, 
    tools: tools,
    tool_choice: "auto"
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Migrate your code

The tabs below show a request using the medical comprehend API and the same request using the LLM tool with the `palmyra-med` model.

<Tabs>
  <Tab title="Before: Medical comprehend API">
    The medical comprehend API accepts medical text and a response type:

    <CodeGroup>
      ```bash cURL theme={null}
      curl --location 'https://api.writer.com/v1/tools/comprehend/medical' \
        --header 'Content-Type: application/json' \
        --header "Authorization: Bearer $WRITER_API_KEY" \
        --data '{
          "content": "the symptoms are soreness, a temperature and cough", 
          "response_type": "Entities"
        }'
      ```

      ```python Python theme={null}
      from writerai import Writer

      # Initialize the Writer client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      medical = client.tools.comprehend.medical(
        content="the symptoms are soreness, a temperature and cough",
        response_type="Entities"
      )

      print(medical.entities)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from "writer-sdk";

      // Initialize the Writer client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const medical = await client.tools.comprehend.medical({
        content: "the symptoms are soreness, a temperature and cough",
        response_type: "Entities"
      });

      console.log(medical.entities);
      ```
    </CodeGroup>

    **Response:**

    ```json  theme={null}
    {
      "entities": [
        {
          "category": "MEDICAL_CONDITION",
          "text": "soreness",
          "score": 0.95,
          "traits": []
        },
        {
          "category": "MEDICAL_CONDITION",
          "text": "temperature",
          "score": 0.92,
          "traits": []
        },
        {
          "category": "MEDICAL_CONDITION",
          "text": "cough",
          "score": 0.98,
          "traits": []
        }
      ]
    }
    ```
  </Tab>

  <Tab title="After: LLM tool with structured output">
    The LLM tool with `palmyra-med` and structured output provides similar functionality:

    <CodeGroup>
      ```python Python theme={null}
      import json
      from writerai import Writer

      # Initialize the Writer client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      messages = [{"role": "user", "content": "Extract medical entities from this text: the symptoms are soreness, a temperature and cough"}]

      tools = [{
        "type": "llm",
        "function": {
          "description": "A function that invokes the Palmyra Med model, specialized in analyzing medical text. Any user request for medical analysis should use this tool.",
          "model": "palmyra-med"
        }
      }]

      response_format = {
        "type": "json_schema",
        "json_schema": {
          "name": "medical_entities",
          "schema": {
            "type": "object",
            "properties": {
              "entities": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "text": {"type": "string"},
                    "category": {"type": "string"},
                    "score": {"type": "number"}
                  },
                  "required": ["text", "category", "score"],
                  "additionalProperties": False
                }
              }
            },
            "required": ["entities"],
            "additionalProperties": False
          },
          "strict": True
        }
      }

      response = client.chat.chat(
        model="palmyra-x5", 
        messages=messages, 
        tools=tools,
        tool_choice="auto",
        response_format=response_format
      )

      # Parse the JSON response
      entities = json.loads(response.choices[0].message.content)
      print(entities)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from "writer-sdk";

      // Initialize the Writer client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const messages = [{role: "user", content: "Extract medical entities from this text: the symptoms are soreness, a temperature and cough"}];

      const tools = [{
        type: "llm",
        function: {
          description: "A function that invokes the Palmyra Med model, specialized in analyzing medical text. Any user request for medical analysis should use this tool.",
          model: "palmyra-med"
        }
      }];

      const responseFormat = {
        type: "json_schema",
        json_schema: {
          name: "medical_entities",
          schema: {
            type: "object",
            properties: {
              entities: {
                type: "array",
                items: {
                  type: "object",
                  properties: {
                    text: {type: "string"},
                    category: {type: "string"},
                    score: {type: "number"}
                  },
                  required: ["text", "category", "score"],
                  additionalProperties: false
                }
              }
            },
            required: ["entities"],
            additionalProperties: false
          },
          strict: true
        }
      };

      const response = await client.chat.chat({
        model: "palmyra-x5", 
        messages: messages, 
        tools: tools,
        tool_choice: "auto",
        response_format: responseFormat
      });

      // Parse the JSON response
      const entities = JSON.parse(response.choices[0].message.content);
      console.log(entities);
      ```
    </CodeGroup>

    **Response:**

    ```json  theme={null}
    {
      "id": "1234",
      "object": "chat.completion",
      "choices": [
        {
          "index": 0,
          "finish_reason": "stop",
          "message": {
            "content": "{\"entities\":[{\"text\":\"soreness\",\"category\":\"MEDICAL_CONDITION\",\"score\":0.93},{\"text\":\"temperature\",\"category\":\"MEDICAL_CONDITION\",\"score\":0.89},{\"text\":\"cough\",\"category\":\"MEDICAL_CONDITION\",\"score\":0.96}]}",
            "role": "assistant",
            "tool_calls": null,
            "graph_data": {
              "sources": null,
              "status": null,
              "subqueries": null
            },
            "llm_data": {
              "prompt": "Extract medical entities from this text: the symptoms are soreness, a temperature and cough",
              "model": "palmyra-med"
            },
            "image_data": null,
            "translation_data": null,
            "refusal": null
          },
          "logprobs": null
        }
      ],
      "created": 1741970653,
      "model": "palmyra-x5",
      "usage": {
        "prompt_tokens": 259,
        "total_tokens": 305,
        "completion_tokens": 46,
        "prompt_token_details": null,
        "completion_tokens_details": null
      },
      "system_fingerprint": "v1",
      "service_tier": null
    }
    ```

    The structured output is returned as a JSON string in `choices[0].message.content`, which you can parse:

    ```json  theme={null}
    {
      "entities": [
        {
          "text": "soreness",
          "category": "MEDICAL_CONDITION",
          "score": 0.93
        },
        {
          "text": "temperature",
          "category": "MEDICAL_CONDITION",
          "score": 0.89
        },
        {
          "text": "cough",
          "category": "MEDICAL_CONDITION",
          "score": 0.96
        }
      ]
    }
    ```
  </Tab>
</Tabs>

## Access LLM metadata

The LLM tool response includes metadata in the `llm_data` field:

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  messages = [{"role": "user", "content": "Extract medical entities from this text: the symptoms are soreness, a temperature and cough"}]

  tools = [{
    "type": "llm",
    "function": {
      "description": "A function that invokes the Palmyra Med model, specialized in analyzing medical text. Any user request for medical analysis should use this tool.",
      "model": "palmyra-med"
    }
  }]

  response = client.chat.chat(
    model="palmyra-x5", 
    messages=messages, 
    tools=tools,
    tool_choice="auto"
  )

  # Get the analysis result
  analysis = response.choices[0].message.content

  # Get LLM metadata
  llm_metadata = response.choices[0].message.llm_data
  prompt = llm_metadata.prompt
  model_used = llm_metadata.model

  print(f"Analysis from {model_used}: {analysis}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "Extract medical entities from this text: the symptoms are soreness, a temperature and cough"}];

  const tools = [{
    type: "llm",
    function: {
      description: "A function that invokes the Palmyra Med model, specialized in analyzing medical text. Any user request for medical analysis should use this tool.",
      model: "palmyra-med"
    }
  }];

  const response = await client.chat.chat({
    model: "palmyra-x5", 
    messages: messages, 
    tools: tools,
    tool_choice: "auto"
  });

  // Get the analysis result
  const analysis = response.choices[0].message.content;

  // Get LLM metadata
  const llmMetadata = response.choices[0].message.llm_data;
  const prompt = llmMetadata.prompt;
  const modelUsed = llmMetadata.model;

  console.log(`Analysis from ${modelUsed}: ${analysis}`);
  ```
</CodeGroup>

## Explore related features

Learn more about the LLM tool and related features:

* [LLM tool guide (model delegation)](/home/model-delegation)
* [Structured output](/home/structured-output)
* [Chat completion guide](/home/chat-completion)
* [Palmyra Med model](/home/models#palmyra-med)
