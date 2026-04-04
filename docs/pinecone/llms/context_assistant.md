# Source: https://docs.pinecone.io/reference/api/2025-10/assistant/context_assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve context from an assistant

> Retrieve context snippets from an assistant to use as part of RAG or any agentic flow.

For guidance and examples, see [Retrieve context snippets](https://docs.pinecone.io/guides/assistant/retrieve-context-snippets).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/context" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "query": "Who is the CFO of Netflix?"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "snippets":
      [
          {
              "type":"text",
              "content":"EXHIBIT 31.3\nCERTIFICATION OF CHIEF FINANCIAL OFFICER\nPURSUANT TO SECTION 302 OF THE SARBANES-OXLEY ACT OF 2002\nI, Spencer Neumann, certify that: ...",
              "score":0.9960699,
              "reference":
              {
                  "type":"pdf",
                  "file":
                  {
                      "status":"Available","id":"e6034e51-0bb9-4926-84c6-70597dbd07a7",
                      "name":"Netflix-10-K-01262024.pdf", 
                      "size":1073470,
                      "metadata":null,
                      "updated_on":"2024-11-21T22:59:10.426001030Z",
                      "created_on":"2024-11-21T22:58:35.879120257Z", 
                      "percent_done":1.0,
                      "signed_url":"https://storage.googleapis.com...",
                      "error_message":null
                      },
                  "pages":[78]
              }
          },
  {
      "type":"text",
      "content":"EXHIBIT 32.1\n..."
  ...
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/assistant_data_2025-10.oas.yaml post /chat/{assistant_name}/context
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
  /chat/{assistant_name}/context:
    post:
      tags:
        - Manage Assistants
      summary: Retrieve context from an assistant
      description: >-
        Retrieve context snippets from an assistant to use as part of RAG or any
        agentic flow.


        For guidance and examples, see [Retrieve context
        snippets](https://docs.pinecone.io/guides/assistant/retrieve-context-snippets).
      operationId: context_assistant
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
        description: The desired configuration to retrieve context from an assistant.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ContextRequest'
        required: true
      responses:
        '200':
          description: Context retrieval process successful.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ContextModel'
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
    ContextRequest:
      description: Parameters to retrieve context from an assistant.
      type: object
      properties:
        query:
          description: >-
            The query that is used to generate the context. Exactly one of query
            or messages should be provided.
          type: string
        filter:
          example:
            genre:
              $ne: documentary
          description: >-
            Optionally filter which documents can be retrieved using the
            following metadata fields.
          type: object
        messages:
          description: >-
            The list of messages to use for generating the context. Exactly one
            of query or messages should be provided.
          type: array
          items:
            $ref: '#/components/schemas/MessageModel'
        top_k:
          example: 20
          description: >-
            The maximum number of context snippets to return. Default is 16.
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
            Whether or not to retrieve image-related context snippets. If
            `false`, only text snippets are returned.
          default: true
          type: boolean
        include_binary_content:
          description: >-
            If image-related context snippets are returned, this field
            determines whether or not they should include base64 image data. If
            `false`, only the image captions are returned. Only available when
            `multimodal=true`.
          default: true
          type: boolean
    ContextModel:
      description: The response format containing the context from an assistant.
      type: object
      properties:
        id:
          type: string
        snippets:
          type: array
          items:
            $ref: '#/components/schemas/SnippetModel'
        usage:
          $ref: '#/components/schemas/UsageModel'
      required:
        - snippets
        - usage
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
    SnippetModel:
      description: Represents a part of a document that is relevant to the user query.
      discriminator:
        propertyName: type
        mapping:
          text: '#/components/schemas/TextSnippetModel'
          multimodal: '#/components/schemas/MultiModalSnippetModel'
      type: object
      oneOf:
        - $ref: '#/components/schemas/TextSnippetModel'
        - $ref: '#/components/schemas/MultiModalSnippetModel'
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
    TextSnippetModel:
      description: Represents a text context snippet.
      type: object
      properties:
        type:
          description: The type of context snippet.
          type: string
        content:
          type: string
        score:
          type: number
          format: float
        reference:
          $ref: '#/components/schemas/TypedReferenceModel'
      required:
        - type
        - content
        - score
        - reference
    MultiModalSnippetModel:
      description: Represents a multimodal context snippet.
      type: object
      properties:
        type:
          description: The type of context snippet.
          type: string
        content:
          type: array
          items:
            $ref: '#/components/schemas/MultiModalContentBlocksModel'
        score:
          type: number
          format: float
        reference:
          $ref: '#/components/schemas/TypedReferenceModel'
      required:
        - type
        - content
        - score
        - reference
    TypedReferenceModel:
      description: Represents a reference for the information provided.
      discriminator:
        propertyName: type
        mapping:
          text: '#/components/schemas/TextReferenceModel'
          json: '#/components/schemas/JsonReferenceModel'
          markdown: '#/components/schemas/MarkdownReferenceModel'
          pdf: '#/components/schemas/PdfReferenceModel'
          doc_x: '#/components/schemas/DocxReferenceModel'
      type: object
      oneOf:
        - $ref: '#/components/schemas/TextReferenceModel'
        - $ref: '#/components/schemas/JsonReferenceModel'
        - $ref: '#/components/schemas/MarkdownReferenceModel'
        - $ref: '#/components/schemas/PdfReferenceModel'
        - $ref: '#/components/schemas/DocxReferenceModel'
    MultiModalContentBlocksModel:
      description: Represents a block in the multimodal content of a context snippet.
      discriminator:
        propertyName: type
        mapping:
          text: '#/components/schemas/MultiModalContentTextBlockModel'
          image: '#/components/schemas/MultiModalContentImageBlockModel'
      type: object
      oneOf:
        - $ref: '#/components/schemas/MultiModalContentTextBlockModel'
        - $ref: '#/components/schemas/MultiModalContentImageBlockModel'
    TextReferenceModel:
      description: Represents a reference to a part of a text document.
      type: object
      properties:
        type:
          description: The type of reference. Always "text".
          type: string
        file:
          $ref: '#/components/schemas/AssistantFileModel'
      required:
        - type
        - file
    JsonReferenceModel:
      description: Represents a reference to a json document.
      type: object
      properties:
        type:
          description: The type of reference. Always "json".
          type: string
        file:
          $ref: '#/components/schemas/AssistantFileModel'
      required:
        - type
        - file
    MarkdownReferenceModel:
      description: Represents a reference to a part of a markdown document.
      type: object
      properties:
        type:
          description: The type of reference. Always "markdown".
          type: string
        file:
          $ref: '#/components/schemas/AssistantFileModel'
      required:
        - type
        - file
    PdfReferenceModel:
      description: Represents a reference to a part of a PDF document.
      type: object
      properties:
        type:
          description: The type of reference. Always "pdf".
          type: string
        file:
          $ref: '#/components/schemas/AssistantFileModel'
        pages:
          type: array
          items:
            type: integer
      required:
        - type
        - file
        - pages
    DocxReferenceModel:
      description: Represents a reference to a part of a docx document.
      type: object
      properties:
        type:
          description: The type of reference. Always "doc_x".
          type: string
        file:
          $ref: '#/components/schemas/AssistantFileModel'
        pages:
          type: array
          items:
            type: integer
      required:
        - type
        - file
        - pages
    MultiModalContentTextBlockModel:
      description: Represents a text block in a multimodal context snippet.
      type: object
      properties:
        type:
          description: The type of multimodal content block.
          type: string
        text:
          type: string
      required:
        - type
        - text
    MultiModalContentImageBlockModel:
      description: Represents an image block in a multimodal context snippet.
      type: object
      properties:
        type:
          description: The type of multimodal content block.
          type: string
        caption:
          type: string
        image:
          $ref: '#/components/schemas/ImageModel'
      required:
        - type
        - caption
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
    ImageModel:
      nullable: true
      description: Represents the data for an image.
      type: object
      properties:
        type:
          description: The format of the image data. Currently, this is always "base64".
          type: string
        mime_type:
          description: The MIME type of the image (e.g., "image/jpeg").
          type: string
        data:
          description: The image data. Currently, this is always a base64-encoded string.
          type: string
      required:
        - type
        - mime_type
        - data
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: Pinecone API Key

````