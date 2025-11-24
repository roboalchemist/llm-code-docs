# Source: https://docs.pinecone.io/reference/api/2025-04/admin/list_api_keys.md

# Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/list_api_keys.md

# List API keys

> List all API keys in a project.

## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/projects/{project_id}/api-keys
paths:
  path: /admin/projects/{project_id}/api-keys
  method: get
  servers:
    - url: https://api.pinecone.io
      description: Production API endpoints
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >
                An [access
                token](https://docs.pinecone.io/guides/organizations/manage-service-accounts#retrieve-an-access-token)
                must be provided in the `Authorization` header using the
                `Bearer` scheme.
          cookie: {}
    parameters:
      path:
        project_id:
          schema:
            - type: string
              required: true
              description: Project ID
              format: uuid
          style: simple
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/APIKey'
        examples:
          example:
            value:
              data:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  name: <string>
                  project_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  roles:
                    - ProjectEditor
        description: A list of API keys.
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_0
                    example: 500
                    description: The HTTP status code of the error.
                    type: integer
              error:
                allOf:
                  - &ref_1
                    example:
                      code: INVALID_ARGUMENT
                      message: >-
                        Index name must contain only lowercase alphanumeric
                        characters or hyphens, and must not begin or end with a
                        hyphen.
                    description: Detailed information about the error that occurred.
                    type: object
                    properties:
                      code:
                        description: >-
                          The error code.

                          Possible values: `OK`, `UNKNOWN`, `INVALID_ARGUMENT`,
                          `DEADLINE_EXCEEDED`, `QUOTA_EXCEEDED`, `NOT_FOUND`,
                          `ALREADY_EXISTS`, `PERMISSION_DENIED`,
                          `UNAUTHENTICATED`, `RESOURCE_EXHAUSTED`,
                          `FAILED_PRECONDITION`, `ABORTED`, `OUT_OF_RANGE`,
                          `UNIMPLEMENTED`, `INTERNAL`, `UNAVAILABLE`,
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
                          Index name must contain only lowercase alphanumeric
                          characters or hyphens, and must not begin or end with
                          a hyphen.
                        type: string
                      details:
                        description: >-
                          Additional information about the error. This field is
                          not guaranteed to be present.
                        type: object
                    required:
                      - code
                      - message
            description: The response shape used for all error responses.
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_2
              - status
              - error
            example: &ref_3
              error:
                code: QUOTA_EXCEEDED
                message: >-
                  The index exceeds the project quota of 5 pods by 2 pods.
                  Upgrade your account or change the project settings to
                  increase the quota.
              status: 429
        examples:
          unauthorized:
            summary: Unauthorized
            value:
              error:
                code: UNAUTHENTICATED
                message: Invalid API key.
              status: 401
        description: 'Unauthorized. Possible causes: Invalid API key.'
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_0
              error:
                allOf:
                  - *ref_1
            description: The response shape used for all error responses.
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
            example: *ref_3
        examples:
          internal-server-error:
            summary: Internal server error
            value:
              error:
                code: UNKNOWN
                message: Internal server error
              status: 500
        description: Internal server error.
    4XX:
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_0
              error:
                allOf:
                  - *ref_1
            description: The response shape used for all error responses.
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
            example: *ref_3
        examples:
          example:
            value:
              error:
                code: QUOTA_EXCEEDED
                message: >-
                  The index exceeds the project quota of 5 pods by 2 pods.
                  Upgrade your account or change the project settings to
                  increase the quota.
              status: 429
        description: Unexpected error on request.
  deprecated: false
  type: path
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

````