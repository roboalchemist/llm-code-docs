# Source: https://infisical.com/docs/api-reference/endpoints/dynamic-secrets/get-lease.md

# Get Lease

## OpenAPI

````yaml GET /api/v1/dynamic-secrets/leases/{leaseId}
paths:
  path: /api/v1/dynamic-secrets/leases/{leaseId}
  method: get
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
      query:
        projectSlug:
          schema:
            - type: string
              required: true
              description: The slug of the project to create dynamic secret in.
              minLength: 1
        path:
          schema:
            - type: string
              required: false
              description: The path to list folders from.
              default: /
        environmentSlug:
          schema:
            - type: string
              required: true
              description: The slug of the environment to list folders from.
              minLength: 1
      header: {}
      cookie: {}
    body: {}
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
                      dynamicSecret:
                        type: object
                        properties:
                          id:
                            type: string
                            format: uuid
                          name:
                            type: string
                          version:
                            type: number
                          type:
                            type: string
                          defaultTTL:
                            type: string
                          maxTTL:
                            type: string
                            nullable: true
                          folderId:
                            type: string
                            format: uuid
                          status:
                            type: string
                            nullable: true
                          statusDetails:
                            type: string
                            nullable: true
                          createdAt:
                            type: string
                            format: date-time
                          updatedAt:
                            type: string
                            format: date-time
                          projectGatewayId:
                            type: string
                            format: uuid
                            nullable: true
                          gatewayId:
                            type: string
                            format: uuid
                            nullable: true
                          usernameTemplate:
                            type: string
                            nullable: true
                          gatewayV2Id:
                            type: string
                            format: uuid
                            nullable: true
                          metadata:
                            type: array
                            items:
                              type: object
                              properties:
                                key:
                                  type: string
                                  minLength: 1
                                value:
                                  type: string
                                  default: ''
                              required:
                                - key
                              additionalProperties: false
                        required:
                          - id
                          - name
                          - version
                          - type
                          - defaultTTL
                          - folderId
                          - createdAt
                          - updatedAt
                        additionalProperties: false
                    required:
                      - id
                      - version
                      - externalEntityId
                      - expireAt
                      - dynamicSecretId
                      - createdAt
                      - updatedAt
                      - dynamicSecret
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
                dynamicSecret:
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  name: <string>
                  version: 123
                  type: <string>
                  defaultTTL: <string>
                  maxTTL: <string>
                  folderId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  status: <string>
                  statusDetails: <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  projectGatewayId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  gatewayId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  usernameTemplate: <string>
                  gatewayV2Id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  metadata:
                    - key: <string>
                      value: ''
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