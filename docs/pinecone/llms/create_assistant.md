# Source: https://docs.pinecone.io/reference/api/2025-10/assistant/create_assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an assistant

> Create an assistant. This is where you specify the underlying training model, which cloud provider you would like to deploy with, and more.

For guidance and examples, see [Create an assistant](https://docs.pinecone.io/guides/assistant/create-assistant)

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.0"},
    "region":"us"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "metadata": {"team": "customer-support", "version": "1.0"},
    "status": "Initializing",
    "host": "https://prod-1-data.ke.pinecone.io",
    "created_at": "2025-10-01T12:30:00Z",
    "updated_at": "2025-10-01T12:30:00Z"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/assistant_control_2025-10.oas.yaml post /assistants
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
  /assistants:
    post:
      tags:
        - Manage Assistants
      summary: Create an assistant
      description: >-
        Create an assistant. This is where you specify the underlying training
        model, which cloud provider you would like to deploy with, and more.


        For guidance and examples, see [Create an
        assistant](https://docs.pinecone.io/guides/assistant/create-assistant)
      operationId: create_assistant
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
      requestBody:
        description: The desired configuration to create an assistant.
        content:
          application/json:
            schema:
              description: The configuration needed to create an assistant.
              type: object
              properties:
                name:
                  example: example-assistant
                  description: >
                    The name of the assistant. Resource name must be 1-63
                    characters long, start and end with an alphanumeric
                    character, and consist only of lower case alphanumeric
                    characters or '-'.
                  type: string
                  minLength: 1
                  maxLength: 63
                instructions:
                  nullable: true
                  description: >-
                    Description or directive for the assistant to apply to all
                    responses. Maximum 16 KB.
                  type: string
                metadata:
                  description: >-
                    Optional metadata associated with the assistant. Metadata is
                    a JSON object that can store custom organizational data,
                    tags, and attributes. Maximum size is 16KB.
                  type: object
                region:
                  description: >-
                    The region to deploy the assistant in. Our current options
                    are either us or eu. Defaults to us.
                  x-enum:
                    - us
                    - eu
                  type: string
              required:
                - name
        required: true
      responses:
        '200':
          description: Create request successful.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Assistant'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                upload-validation-error:
                  summary: Validation error on ingest
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
        '429':
          description: Assistant of given name already exists.
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