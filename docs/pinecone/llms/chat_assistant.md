# Source: https://docs.pinecone.io/reference/api/2025-10/assistant/chat_assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat with an assistant

> Chat with an assistant and get back citations in structured form. 

This is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references than the OpenAI-compatible chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

<RequestExample>
  ```bash curl | Default theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the inciting incident of Pride and Prejudice?"
      }
    ],
    "stream": false,
    "model": "gpt-4o"
  }'
  ```

  ```bash curl | Streaming theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the inciting incident of Pride and Prejudice?"
      }
    ],
    "stream": true,
    "model": "gpt-4o"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Default response theme={null}
  {
    "finish_reason": "stop",
    "message": {
      "role": "assistant",
      "content": "The inciting incident of \"Pride and Prejudice\" occurs when Mrs. Bennet informs Mr. Bennet that Netherfield Park has been let at last, and she is eager to share the news about the new tenant, Mr. Bingley, who is wealthy and single. This sets the stage for the subsequent events of the story, including the introduction of Mr. Bingley and Mr. Darcy to the Bennet family and the ensuing romantic entanglements."
    },
    "id": "00000000000000004ac3add5961aa757",
    "model": "gpt-4o-2024-05-13",
    "usage": {
      "prompt_tokens": 9736,
      "completion_tokens": 105,
      "total_tokens": 9841
    },
    "citations": [
      {
        "position": 406,
        "references": [
          {
            "file": {
              "status": "Available",
              "id": "ae79e447-b89e-4994-994b-3232ca52a654",
              "name": "Pride-and-Prejudice.pdf",
              "size": 2973077,
              "metadata": null,
              "updated_on": "2024-06-14T15:01:57.385425746Z",
              "created_on": "2024-06-14T15:01:02.910452398Z",
              "percent_done": 0,
              "signed_url": "https://storage.googleapis.com/...",
              "error_message": null
            },
            "pages": [
              1
            ]
          }
        ]
      }
    ]
  }

  ```

  ```shell Streaming response theme={null}
  data:{
    "type":"message_start",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "role":"assistant"
  }

  data:
  {
    "type":"content_chunk",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "delta":
    {
      "content":"The"
      }
  }

  ...

  data:
  {
    "type":"citation",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "citation":
    {
      "position":406,
      "references":
      [
        {
          "file":{
            "status":"Available",
            "id":"ae79e447-b89e-4994-994b-3232ca52a654",
            "name":"Pride-and-Prejudice.pdf",
            "size":2973077,
            "metadata":null,
            "updated_on":"2024-06-14T15:01:57.385425746Z", 
            "created_on":"2024-06-14T15:01:02.910452398Z",
            "percent_done":0.0,
            "signed_url":"https://storage.googleapis.com/...",
            "error_message":null
            }, 
        "pages":[1]
        }
      ]
    }
  }

  data:
  {
    "type":"message_end",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "finish_reason":"stop",
    "usage":
    {
      "prompt_tokens":9736,
      "completion_tokens":102,
      "total_tokens":9838
      }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/assistant_data_2025-10.oas.yaml post /chat/{assistant_name}
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
  /chat/{assistant_name}:
    post:
      tags:
        - Manage Assistants
      summary: Chat with an assistant
      description: >-
        Chat with an assistant and get back citations in structured form. 


        This is the recommended way to chat with an assistant, as it offers more
        functionality and control over the assistant's responses and references
        than the OpenAI-compatible chat interface.


        For guidance and examples, see [Chat with an
        assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).
      operationId: chat_assistant
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
              $ref: '#/components/schemas/ChatRequest'
        required: true
      responses:
        '200':
          description: Search request successful.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatModel'
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
    ChatRequest:
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
        json_response:
          description: >-
            If true, the assistant will be instructed to return a JSON response.
            Cannot be used with streaming.
          default: false
          type: boolean
        include_highlights:
          description: >-
            If true, the assistant will be instructed to return highlights from
            the referenced documents that support its response.
          default: false
          type: boolean
        context_options:
          $ref: '#/components/schemas/ContextOptionsModel'
      required:
        - messages
    ChatModel:
      description: Describes the response format of a chat request from the citation API.
      type: object
      properties:
        id:
          type: string
        finish_reason:
          x-enum:
            - stop
            - length
            - content_filter
            - function_call
          type: string
        message:
          $ref: '#/components/schemas/MessageModel'
        model:
          type: string
        citations:
          type: array
          items:
            $ref: '#/components/schemas/CitationModel'
        usage:
          $ref: '#/components/schemas/UsageModel'
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
    ContextOptionsModel:
      description: Controls the context snippets sent to the LLM.
      type: object
      properties:
        top_k:
          example: 20
          description: >-
            The maximum number of context snippets to use. Default is 16.
            Maximum is 64.
          type: integer
        snippet_size:
          example: 4096
          description: >-
            The maximum context snippet size. Default is 2048 tokens. Minimum is
            512 tokens. Maximum is 8192 tokens.
          type: integer
        multimodal:
          description: >-
            Whether or not to send image-related context snippets to the LLM. If
            `false`, only text context snippets are sent.
          default: true
          type: boolean
        include_binary_content:
          description: >-
            If image-related context snippets are sent to the LLM, this field
            determines whether or not they should include base64 image data. If
            `false`, only the image caption is sent. Only available when
            `multimodal=true`.
          default: true
          type: boolean
    CitationModel:
      description: Describes a single cited source returned by a chat request.
      type: object
      properties:
        position:
          description: The index position of the citation in the complete text response.
          type: integer
        references:
          type: array
          items:
            $ref: '#/components/schemas/ReferenceModel'
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
    ReferenceModel:
      description: Describes a single reference in a citation.
      type: object
      properties:
        file:
          $ref: '#/components/schemas/AssistantFileModel'
        pages:
          type: array
          items:
            type: integer
        highlight:
          $ref: '#/components/schemas/HighlightModel'
    AssistantFileModel:
      description: The response format for a successful file upload request.
      type: object
      properties:
        name:
          type: string
        id:
          type: string
          format: uuid
        metadata:
          nullable: true
          type: object
        created_on:
          type: string
          format: date-time
        updated_on:
          type: string
          format: date-time
        status:
          description: >-
            The current state of the uploaded file. Possible values:

            - `Processing`: File is being processed (parsed, chunked, embedded)

            - `Available`: Processing completed successfully; file is ready for
            use

            - `Deleting`: Deletion has been initiated but not yet completed

            - `ProcessingFailed`: Processing failed with an error


            Note: Once a file is deleted, the API returns 404 Not Found instead
            of a file object.
          x-enum:
            - Processing
            - Available
            - Deleting
            - ProcessingFailed
          type: string
        percent_done:
          nullable: true
          description: The percentage of the file that has been processed
          type: number
          format: double
        signed_url:
          nullable: true
          example: https://storage.googleapis.com/bucket/file.pdf?...
          description: >-
            A [signed
            URL](https://cloud.google.com/storage/docs/access-control/signed-urls)
            that provides temporary, read-only access to the underlying file.
            Anyone with the link can access the file, so treat it as sensitive
            data. Expires after a short time.
          type: string
        error_message:
          nullable: true
          description: >-
            A message describing any error during file processing. Provided only
            if an error occurs.
          type: string
        multimodal:
          description: Indicates whether the file was processed as multimodal.
          type: boolean
      required:
        - id
        - name
    HighlightModel:
      nullable: true
      description: >-
        Represents a portion of a referenced document that directly supports or
        is relevant to the response.
      type: object
      properties:
        type:
          description: The type of the highlight. Currently it is always text.
          type: string
        content:
          type: string
      required:
        - type
        - content
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: Pinecone API Key

````