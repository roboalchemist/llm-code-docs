# Source: https://infisical.com/docs/api-reference/endpoints/dynamic-secrets/delete-lease.md

# Delete Lease

## OpenAPI

````yaml DELETE /api/v1/dynamic-secrets/leases/{leaseId}
paths:
  path: /api/v1/dynamic-secrets/leases/{leaseId}
  method: delete
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
    parameters:
      path:
        leaseId:
          schema:
            - type: string
              required: true
              description: The ID of the dynamic secret lease.
              minLength: 1
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              projectSlug:
                allOf:
                  - type: string
                    minLength: 1
                    description: The slug of the project of the dynamic secret in.
              path:
                allOf:
                  - type: string
                    minLength: 1
                    default: /
                    description: The path of the dynamic secret in.
              environmentSlug:
                allOf:
                  - type: string
                    minLength: 1
                    description: The slug of the environment of the dynamic secret in.
              isForced:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      A boolean flag to delete the the dynamic secret from
                      Infisical without trying to remove it from external
                      provider. Used when the dynamic secret got modified
                      externally.
            required: true
            requiredProperties:
              - projectSlug
              - environmentSlug
            additionalProperties: false
        examples:
          example:
            value:
              projectSlug: <string>
              path: /
              environmentSlug: <string>
              isForced: false
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              lease:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      version:
                        type: number
                      externalEntityId:
                        type: string
                      expireAt:
                        type: string
                        format: date-time
                      status:
                        type: string
                        nullable: true
                      statusDetails:
                        type: string
                        nullable: true
                      dynamicSecretId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      config:
                        nullable: true
                    required:
                      - id
                      - version
                      - externalEntityId
                      - expireAt
                      - dynamicSecretId
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            requiredProperties:
              - lease
            additionalProperties: false
        examples:
          example:
            value:
              lease:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                version: 123
                externalEntityId: <string>
                expireAt: '2023-11-07T05:31:56Z'
                status: <string>
                statusDetails: <string>
                dynamicSecretId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                config: <any>
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````