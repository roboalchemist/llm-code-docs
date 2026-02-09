# Source: https://docs.pinecone.io/reference/api/2025-10/assistant/chat_completion_assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat through an OpenAI-compatible interface

> Chat with an assistant. This endpoint is based on the OpenAI Chat Completion API, a commonly used and adopted API. 

It is useful if you need inline citations or OpenAI-compatible responses, but has limited functionality compared to the standard chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

<RequestExample>
  ```bash curl | Default theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ]
  }'
  ```

  ```bash curl | Streaming theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "stream": true
  }'
  ```
</RequestExample>

<ResponseExample>
  ```JSON Default response theme={null}
  {"chat_completion":
    {
      "id":"chatcmpl-9OtJCcR0SJQdgbCDc9JfRZy8g7VJR",
      "choices":[
        {
          "finish_reason":"stop",
          "index":0,
          "message":{
            "role":"assistant",
            "content":"The maximum height of a red pine (Pinus resinosa) is up to 25 meters."
          }
        }
      ],
      "model":"my_assistant"
    }
  }
  ```

  ```shell Streaming response theme={null}
  {
    'id': '000000000000000009de65aa87adbcf0', 
    'choices': [
        {
        'index': 0, 
        'delta': 
          {
          'role': 'assistant', 
          'content': 'The'
          }, 
        'finish_reason': None
        }
      ], 
    'model': 'gpt-4o-2024-05-13'
  }

  ...

  {
    'id': '00000000000000007a927260910f5839',
    'choices': [
        {
        'index': 0,
        'delta':
          {
            'role': '', 
            'content': 'The'
          }, 
        'finish_reason': None
        }
      ], 
    'model': 'gpt-4o-2024-05-13'
  }

  ...

  {
    'id': '00000000000000007a927260910f5839', 
    'choices': [
      {
        'index': 0, 
        'delta': 
          {
          'role': None, 
          'content': None
          }, 
        'finish_reason': 'stop'
        }
      ], 
    'model': 'gpt-4o-2024-05-13'
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/assistant_data_2025-10.oas.yaml post /chat/{assistant_name}/chat/completions
openapi: 3.0.3
info:
  title: Pinecone Assistant Data Plane API
  description: >-
    Pinecone Assistant Engine is a context engine to store and retrieve relevant
    knowledge from millions of documents at scale. This API supports
    interactions with assistants.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://{assistant_host}
    variables:
      assistant_host:
        default: unknown
        description: host of the created assistant
security:
  - ApiKeyAuth: []
tags:
  - name: Manage Assistants
    description: Actions that manage Assistants
paths:
  /chat/{assistant_name}/chat/completions:
    post:
      tags:
        - Manage Assistants
      summary: Chat through an OpenAI-compatible interface
      description: >-
        Chat with an assistant. This endpoint is based on the OpenAI Chat
        Completion API, a commonly used and adopted API. 


        It is useful if you need inline citations or OpenAI-compatible
        responses, but has limited functionality compared to the standard chat
        interface.


        For guidance and examples, see [Chat with an
        assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).
      operationId: chat_completion_assistant
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: path
          name: assistant_name
          description: The name of the assistant to be described.
          required: true
          schema:
            type: string
          example: test-assistant
          style: simple
      requestBody:
        description: The desired configuration to chat an assistant.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SearchCompletions'
        required: true
      responses:
        '200':
          description: Search request successful.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatCompletionModel'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/StreamChatCompletionChunkModel'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                files-validation-error:
                  summary: Validation error on ingest.
                  value:
                    error:
                      code: INVALID_ARGUMENT
                      message: >-
                        Uploaded file can only currently be either a pdf or txt
                        file
                    status: 400
        '401':
          description: 'Unauthorized. Possible causes: Invalid API key.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                unauthorized:
                  summary: Unauthorized
                  value:
                    error:
                      code: UNAUTHENTICATED
                      message: Invalid API key.
                    status: 401
        '404':
          description: Assistant not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                assistant-not-found:
                  summary: Assistant not found.
                  value:
                    error:
                      code: NOT_FOUND
                      message: Assistant "example-assistant" not found.
                    status: 404
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                internal-server-error:
                  summary: Internal server error
                  value:
                    error:
                      code: UNKNOWN
                      message: Internal server error
                    status: 500
components:
  schemas:
    SearchCompletions:
      description: The list of queries / chats to chat an assistant
      type: object
      properties:
        messages:
          type: array
          items:
            $ref: '#/components/schemas/MessageModel'
        stream:
          description: >-
            If false, the assistant will return a single JSON response. If true,
            the assistant will return a stream of responses.
          default: false
          type: boolean
        model:
          description: The large language model to use for answer generation
          default: gpt-4o
          x-enum:
            - gpt-4o
            - gpt-4.1
            - o4-mini
            - claude-3-5-sonnet
            - claude-3-7-sonnet
            - gemini-2.5-pro
          type: string
        temperature:
          description: >-
            Controls the randomness of the model's output: lower values make
            responses more deterministic, while higher values increase
            creativity and variability. If the model does not support a
            temperature parameter, the parameter will be ignored.
          default: 0
          type: number
          format: float
        filter:
          example:
            genre:
              $ne: documentary
          description: >-
            Optionally filter which documents can be retrieved using the
            following metadata fields.
          type: object
      required:
        - messages
    ChatCompletionModel:
      description: Describes the response format of a chat request.
      type: object
      properties:
        id:
          type: string
        choices:
          type: array
          items:
            $ref: '#/components/schemas/ChoiceModel'
        model:
          type: string
        usage:
          $ref: '#/components/schemas/UsageModel'
    StreamChatCompletionChunkModel:
      description: Describes the response format of a chat request.
      type: object
      properties:
        id:
          type: string
        choices:
          type: array
          items:
            $ref: '#/components/schemas/ChoiceChunkModel'
        model:
          type: string
    ErrorResponse:
      example:
        error:
          code: QUOTA_EXCEEDED
          message: >-
            The index exceeds the project quota of 5 pods by 2 pods. Upgrade
            your account or change the project settings to increase the quota.
        status: 429
      description: The response shape used for all error responses.
      type: object
      properties:
        status:
          example: 500
          description: The HTTP status code of the error.
          type: integer
        error:
          example:
            code: INVALID_ARGUMENT
            message: Uploaded file can only currently be either a pdf or txt file
          description: Detailed information about the error that occurred.
          type: object
          properties:
            code:
              x-enum:
                - OK
                - UNKNOWN
                - INVALID_ARGUMENT
                - DEADLINE_EXCEEDED
                - QUOTA_EXCEEDED
                - NOT_FOUND
                - ALREADY_EXISTS
                - PERMISSION_DENIED
                - UNAUTHENTICATED
                - RESOURCE_EXHAUSTED
                - FAILED_PRECONDITION
                - ABORTED
                - OUT_OF_RANGE
                - UNIMPLEMENTED
                - INTERNAL
                - UNAVAILABLE
                - DATA_LOSS
                - FORBIDDEN
              type: string
            message:
              example: >-
                Index name must contain only lowercase alphanumeric characters
                or hyphens, and must not begin or end with a hyphen.
              type: string
            details:
              description: >-
                Additional information about the error. This field is not
                guaranteed to be present.
              type: object
          required:
            - code
            - message
      required:
        - status
        - error
    MessageModel:
      description: Describes the format of a message in a chat.
      type: object
      properties:
        role:
          description: Role of the message such as 'user' or 'assistant'
          type: string
        content:
          description: Content of the message
          type: string
    ChoiceModel:
      description: Describes a single choice in a chat completion response.
      type: object
      properties:
        finish_reason:
          x-enum:
            - stop
            - length
            - content_filter
            - function_call
          type: string
        index:
          type: integer
        message:
          $ref: '#/components/schemas/MessageModel'
    UsageModel:
      description: Describes the usage of a chat completion.
      type: object
      properties:
        prompt_tokens:
          type: integer
        completion_tokens:
          type: integer
        total_tokens:
          type: integer
    ChoiceChunkModel:
      description: Describes a single choice in a chat completion response.
      type: object
      properties:
        finish_reason:
          x-enum:
            - stop
            - length
            - content_filter
            - function_call
          type: string
        index:
          type: integer
        delta:
          description: Chat completion message
          type: object
          properties:
            role:
              type: string
            content:
              type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: Pinecone API Key

````