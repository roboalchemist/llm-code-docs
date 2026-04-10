# Source: https://docs.dify.ai/api-reference/completion/create-completion-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Completion Message

> Send a request to the text generation application.



## OpenAPI

````yaml en/api-reference/openapi_completion.json post /completion-messages
openapi: 3.0.1
info:
  title: Completion App API
  description: >-
    The text generation application offers non-session support and is ideal for
    translation, article writing, summarization AI, and more.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Completion App API. Replace {api_base_url} with the
      actual API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Completion
    description: Operations related to text generation and completion.
  - name: Files
    description: Operations related to file management.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: Operations related to user feedback.
  - name: TTS
    description: Operations related to Text-to-Speech.
  - name: Application
    description: Operations to retrieve application settings and information.
paths:
  /completion-messages:
    post:
      tags:
        - Completion
      summary: Create Completion Message
      description: Send a request to the text generation application.
      operationId: createCompletionMessage
      requestBody:
        description: Request body to create a completion message.
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompletionRequest'
            examples:
              streaming_example:
                summary: Streaming mode example
                value:
                  inputs:
                    query: Hello, world!
                  response_mode: streaming
                  user: abc-123
              blocking_example:
                summary: Blocking mode example
                value:
                  inputs:
                    query: 'Translate this to French: Hello'
                  response_mode: blocking
                  user: def-456
      responses:
        '200':
          description: >-
            Successful response. The content type and structure depend on the
            `response_mode` parameter in the request.

            - If `response_mode` is `blocking`, returns `application/json` with
            a `CompletionResponse` object.

            - If `response_mode` is `streaming`, returns `text/event-stream`
            with a `ChunkCompletionResponse` stream.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompletionResponse'
              examples:
                blockingResponse:
                  summary: Example of a blocking mode response
                  value:
                    event: message
                    message_id: 9da23599-e713-473b-982c-4328d4f5c78a
                    mode: completion
                    answer: Hello World!...
                    metadata:
                      usage:
                        prompt_tokens: 1033
                        prompt_unit_price: '0.001'
                        prompt_price_unit: '0.001'
                        prompt_price: '0.0010330'
                        completion_tokens: 128
                        completion_unit_price: '0.002'
                        completion_price_unit: '0.001'
                        completion_price: '0.0002560'
                        total_tokens: 1161
                        total_price: '0.0012890'
                        currency: USD
                        latency: 0.7682376249867957
                    created_at: 1705407629
            text/event-stream:
              schema:
                type: string
                description: >-
                  A stream of Server-Sent Events. Each event is a JSON object
                  prefixed with 'data: ' and suffixed with '\n\n'. See
                  `ChunkCompletionEvent` for possible event structures.
              examples:
                streamingResponse:
                  summary: Example of a streaming mode response
                  value: >+
                    data: {"event": "message", "message_id":
                    "5ad4cb98-f0c7-4085-b384-88c403be6290", "answer": " I",
                    "created_at": 1679586595}


                    data: {"event": "message", "message_id":
                    "5ad4cb98-f0c7-4085-b384-88c403be6290", "answer": "'m",
                    "created_at": 1679586595}


                    data: {"event": "message_end", "id":
                    "5e52ce04-874b-4d27-9045-b3bc80def685", "metadata":
                    {"usage": {"prompt_tokens": 1033, "prompt_unit_price":
                    "0.001", "prompt_price_unit": "0.001", "prompt_price":
                    "0.0010330", "completion_tokens": 135,
                    "completion_unit_price": "0.002", "completion_price_unit":
                    "0.001", "completion_price": "0.0002700", "total_tokens":
                    1168, "total_price": "0.0013030", "currency": "USD",
                    "latency": 1.381760165997548}}}


                    data: {"event": "tts_message", "task_id":
                    "3bf8a0bb-e73b-4690-9e66-4e429bad8ee7", "message_id":
                    "a8bdc41c-13b2-4c18-bfd9-054b9803038c", "created_at":
                    1721205487, "audio": "base64encodedaudio..."}


                    data: {"event": "tts_message_end", "task_id":
                    "3bf8a0bb-e73b-4690-9e66-4e429bad8ee7", "message_id":
                    "a8bdc41c-13b2-4c18-bfd9-054b9803038c", "created_at":
                    1721205487, "audio": ""}

        '400':
          description: >-
            Bad Request. Possible error codes:

            - `invalid_param`: Abnormal parameter input.

            - `app_unavailable`: App configuration unavailable.

            - `provider_not_initialize`: No available model credential
            configuration.

            - `provider_quota_exceeded`: Model invocation quota insufficient.

            - `model_currently_not_support`: Current model unavailable.

            - `completion_request_error`: Text generation failed.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Conversation does not exist.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    CompletionRequest:
      type: object
      properties:
        inputs:
          type: object
          description: >-
            Allows the entry of various variable values defined by the App. The
            `inputs` parameter contains multiple key/value pairs, with each key
            corresponding to a specific variable and each value being the
            specific value for that variable. The text generation application
            requires at least one key/value pair to be inputted.
          required:
            - query
          properties:
            query:
              type: string
              description: The input text, the content to be processed.
          additionalProperties:
            type: string
          example:
            query: Translate 'hello' to Spanish.
        response_mode:
          type: string
          enum:
            - streaming
            - blocking
          description: >-
            The mode of response return.

            - `streaming`: Streaming mode (recommended), implements a
            typewriter-like output through SSE ([Server-Sent
            Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)).

            - `blocking`: Blocking mode, returns result after execution is
            complete. (Requests may be interrupted if the process is long). *Due
            to Cloudflare restrictions, the request will be interrupted without
            a return after 100 seconds in blocking mode for long processes.*
          example: streaming
        user:
          type: string
          description: >-
            User identifier, used to define the identity of the end-user for
            retrieval and statistics. Should be uniquely defined by the
            developer within the application.
          example: user-12345
        files:
          type: array
          items:
            $ref: '#/components/schemas/InputFileObject'
          description: >-
            File list, suitable for inputting files (images) combined with text
            understanding and answering questions, available only when the model
            supports Vision capability.
      required:
        - inputs
    CompletionResponse:
      type: object
      description: Response object for blocking mode completion.
      properties:
        event:
          type: string
          description: Event type, for blocking mode this is typically 'message'.
          example: message
        message_id:
          type: string
          format: uuid
          description: Unique message ID.
        mode:
          type: string
          description: >-
            App mode, fixed as `completion` for this response type (Note: MD
            also mentions 'chat', using 'completion' from example).
          example: completion
        answer:
          type: string
          description: Complete response content.
        metadata:
          type: object
          properties:
            usage:
              $ref: '#/components/schemas/Usage'
            retriever_resources:
              type: array
              items:
                $ref: '#/components/schemas/RetrieverResource'
              description: Citation and Attribution List.
        created_at:
          type: integer
          format: int64
          description: Message creation timestamp (Unix epoch).
          example: 1705395332
    ErrorResponse:
      type: object
      properties:
        status:
          type: integer
          description: HTTP status code.
        code:
          type: string
          description: Error code specific to the application.
        message:
          type: string
          description: A human-readable error message.
    InputFileObject:
      type: object
      required:
        - type
        - transfer_method
      properties:
        type:
          type: string
          enum:
            - image
          description: 'Supported type: `image` (currently only supports image type).'
        transfer_method:
          type: string
          enum:
            - remote_url
            - local_file
          description: >-
            Transfer method, `remote_url` for image URL / `local_file` for file
            upload
        url:
          type: string
          format: url
          description: Image URL (when the transfer method is `remote_url`)
        upload_file_id:
          type: string
          description: >-
            Uploaded file ID, which must be obtained by uploading through the
            File Upload API in advance (when the transfer method is
            `local_file`)
      anyOf:
        - properties:
            transfer_method:
              enum:
                - remote_url
            url:
              type: string
              format: url
          required:
            - url
          not:
            required:
              - upload_file_id
        - properties:
            transfer_method:
              enum:
                - local_file
            upload_file_id:
              type: string
          required:
            - upload_file_id
          not:
            required:
              - url
      example:
        type: image
        transfer_method: remote_url
        url: https://example.com/image.png
    Usage:
      type: object
      description: Model usage information.
      properties:
        prompt_tokens:
          type: integer
        prompt_unit_price:
          type: string
          format: decimal
        prompt_price_unit:
          type: string
          format: decimal
        prompt_price:
          type: string
          format: decimal
        completion_tokens:
          type: integer
        completion_unit_price:
          type: string
          format: decimal
        completion_price_unit:
          type: string
          format: decimal
        completion_price:
          type: string
          format: decimal
        total_tokens:
          type: integer
        total_price:
          type: string
          format: decimal
        currency:
          type: string
          example: USD
        latency:
          type: number
          format: double
    RetrieverResource:
      type: object
      description: Citation and Attribution information for a resource.
      properties:
        document_id:
          type: string
          description: ID of the retrieved document.
        segment_id:
          type: string
          description: ID of the specific segment within the document.
        score:
          type: number
          format: float
          description: Relevance score of the resource.
        content:
          type: string
          description: Content snippet from the resource.
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        API Key authentication. For all API requests, include your API Key in
        the `Authorization` HTTP Header, prefixed with 'Bearer '. Example:
        `Authorization: Bearer {API_KEY}`. **Strongly recommend storing your API
        Key on the server-side, not shared or stored on the client-side, to
        avoid possible API-Key leakage that can lead to serious consequences.**

````

Built with [Mintlify](https://mintlify.com).