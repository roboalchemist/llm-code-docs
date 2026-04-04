# Source: https://docs.pinecone.io/reference/api/2025-10/admin/create_project.md

# Source: https://docs.pinecone.io/reference/api/2025-10/admin-assistant/create_project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new project

> Creates a new project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl "https://api.pinecone.io/admin/projects" \
      -H "X-Pinecone-Api-Version: 2025-10" \
  	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
  	-d '{
          "name":"example-project"
          }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "example-project",
    "max_pods": 0,
    "force_encryption_with_cmek": false,
    "organization_id": "string",
    "created_at": "2025-03-16T22:46:45.030Z"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/admin_2025-10.oas.yaml post /admin/projects
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
  /admin/projects:
    post:
      tags:
        - Projects
      summary: Create a new project
      description: Creates a new project.
      operationId: create_project
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
        description: The details of the new project.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateProjectRequest'
        required: true
      responses:
        '200':
          description: The project was successfully created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Project'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                index-metric-validation-error:
                  summary: Validation error
                  value:
                    error:
                      code: INVALID_ARGUMENT
                      message: >-
                        Bad request. The request body included invalid request
                        parameters.
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
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
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
    CreateProjectRequest:
      type: object
      properties:
        name:
          example: chatbot-prod
          description: The name of the new project.
          type: string
          minLength: 1
          maxLength: 512
        max_pods:
          description: >
            The maximum number of Pods that can be created in the project.
            Default is `0` (serverless only).
          type: integer
        force_encryption_with_cmek:
          description: >
            Whether to force encryption with a customer-managed encryption key
            (CMEK). Default is `false`.
          type: boolean
      required:
        - name
    Project:
      description: The details of a project.
      type: object
      properties:
        id:
          description: The unique ID of the project.
          type: string
          format: uuid
        name:
          description: The name of the project.
          type: string
          minLength: 1
          maxLength: 512
        max_pods:
          description: The maximum number of Pods that can be created in the project.
          type: integer
        force_encryption_with_cmek:
          description: >-
            Whether to force encryption with a customer-managed encryption key
            (CMEK).
          type: boolean
        organization_id:
          description: The unique ID of the organization that the project belongs to.
          type: string
        created_at:
          description: The date and time when the project was created.
          type: string
          format: date-time
      required:
        - id
        - name
        - max_pods
        - force_encryption_with_cmek
        - organization_id
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