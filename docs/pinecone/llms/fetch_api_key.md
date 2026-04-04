# Source: https://docs.pinecone.io/reference/api/2025-10/admin/fetch_api_key.md

# Source: https://docs.pinecone.io/reference/api/2025-10/admin-assistant/fetch_api_key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get API key details

> Get the details of an API key, excluding the API key secret.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PINECONE_API_KEY_ID="3fa85f64-5717-4562-b3fc-2c963f66afa6"

  curl -X GET "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      -H "accept: application/json" \
      -H "X-Pinecone-Api-Version: 2025-10"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "roles": [
      "ProjectEditor"
    ]
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/admin_2025-10.oas.yaml get /admin/api-keys/{api_key_id}
openapi: 3.0.3
info:
  title: Pinecone Admin API
  description: |
    Provides an API for managing a Pinecone organization and its resources.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://api.pinecone.io
    description: Production API endpoints
security:
  - BearerAuth: []
tags:
  - name: API Keys
    description: Actions that manage API Keys.
  - name: Organizations
    description: Actions that manage organizations.
  - name: Projects
    description: Actions that manage projects.
paths:
  /admin/api-keys/{api_key_id}:
    get:
      tags:
        - API Keys
      summary: Get API key details
      description: Get the details of an API key, excluding the API key secret.
      operationId: fetch_api_key
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
          name: api_key_id
          description: API key ID
          required: true
          schema:
            type: string
            format: uuid
          style: simple
      responses:
        '200':
          description: The details of the API key, excluding the API key secret.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIKey'
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
          description: Not found
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
        4XX:
          description: Unexpected error on request.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    APIKey:
      description: The details of an API key, without the secret.
      type: object
      properties:
        id:
          description: The unique ID of the API key.
          type: string
          format: uuid
        name:
          description: The name of the API key.
          type: string
        project_id:
          description: The ID of the project containing the API key.
          type: string
          format: uuid
        roles:
          description: The roles assigned to the API key.
          type: array
          items:
            example: ProjectEditor
            description: >-
              A role that can be assigned to an API key.

              Possible values: `ProjectEditor`, `ProjectViewer`,
              `ControlPlaneEditor`, `ControlPlaneViewer`, `DataPlaneEditor`, or
              `DataPlaneViewer`.
            x-enum:
              - ProjectEditor
              - ProjectViewer
              - ControlPlaneEditor
              - ControlPlaneViewer
              - DataPlaneEditor
              - DataPlaneViewer
            type: string
      required:
        - id
        - name
        - project_id
        - roles
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
            message: >-
              Index name must contain only lowercase alphanumeric characters or
              hyphens, and must not begin or end with a hyphen.
          description: Detailed information about the error that occurred.
          type: object
          properties:
            code:
              description: >-
                The error code.

                Possible values: `OK`, `UNKNOWN`, `INVALID_ARGUMENT`,
                `DEADLINE_EXCEEDED`, `QUOTA_EXCEEDED`, `NOT_FOUND`,
                `ALREADY_EXISTS`, `PERMISSION_DENIED`, `UNAUTHENTICATED`,
                `RESOURCE_EXHAUSTED`, `FAILED_PRECONDITION`, `ABORTED`,
                `OUT_OF_RANGE`, `UNIMPLEMENTED`, `INTERNAL`, `UNAVAILABLE`,
                `DATA_LOSS`, `FORBIDDEN`, or `UNPROCESSABLE_ENTITY`.        
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
                - UNPROCESSABLE_ENTITY
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
    BearerAuth:
      type: http
      scheme: bearer
      description: >
        An [access
        token](https://docs.pinecone.io/guides/organizations/manage-service-accounts#retrieve-an-access-token)
        must be provided in the `Authorization` header using the `Bearer`
        scheme.

````