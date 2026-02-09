# Source: https://docs.pinecone.io/reference/api/2025-10/assistant/describe_assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Check assistant status

> Get the status of an assistant.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#get-the-status-of-an-assistant)

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \ 
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.0"},
    "status": "Ready",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-10-01T12:30:00Z",
    "updated_at": "2025-10-01T12:45:00Z"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/assistant_control_2025-10.oas.yaml get /assistants/{assistant_name}
openapi: 3.0.3
info:
  title: Pinecone Assistant Control Plane API
  description: >-
    Pinecone Assistant Engine is a context engine to store and retrieve relevant
    knowledge  from millions of documents at scale. This API supports creating
    and managing assistants. 
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://api.pinecone.io/assistant
    description: Production API endpoints
security:
  - ApiKeyAuth: []
tags:
  - name: Manage Assistants
    description: Actions that manage Assistants
paths:
  /assistants/{assistant_name}:
    get:
      tags:
        - Manage Assistants
      summary: Check assistant status
      description: >-
        Get the status of an assistant.


        For guidance and examples, see [Manage
        assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#get-the-status-of-an-assistant)
      operationId: get_assistant
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
          description: The name of the assistant to get a status on.
          required: true
          schema:
            type: string
          example: test-model
          style: simple
      responses:
        '200':
          description: Poll request successful.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Assistant'
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
    Assistant:
      description: Describes the configuration and status of a Pinecone Assistant.
      type: object
      properties:
        name:
          example: example-assistant
          description: >
            The name of the assistant. Resource name must be 1-63 characters
            long, start and end with an alphanumeric character, and consist only
            of lower case alphanumeric characters or '-'.
          type: string
          minLength: 1
          maxLength: 63
        instructions:
          nullable: true
          description: >-
            Description or directive for the assistant to apply to all
            responses.
          type: string
        metadata:
          description: >-
            Optional metadata associated with the assistant. Metadata is a JSON
            object that can store custom organizational data, tags, and
            attributes.
          nullable: true
          type: object
        status:
          x-enum:
            - Initializing
            - Failed
            - Ready
            - Terminating
            - InitializationFailed
          type: string
        host:
          description: The host where the assistant is deployed.
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
      required:
        - name
        - status
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: Pinecone API Key

````