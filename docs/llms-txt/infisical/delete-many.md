# Source: https://infisical.com/docs/api-reference/endpoints/secrets/delete-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/delete-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/secrets/delete-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/delete-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/secrets/delete-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/delete-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/secrets/delete-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/delete-many.md

# Bulk Delete

> Delete many secrets

## OpenAPI

````yaml DELETE /api/v3/secrets/batch/raw
paths:
  path: /api/v3/secrets/batch/raw
  method: delete
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: An access token in Infisical
          cookie: {}
    parameters:
      path: {}
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
                    description: The slug of the project to delete the secret in.
              workspaceId:
                allOf:
                  - type: string
                    description: The ID of the project where the secret is located.
              environment:
                allOf:
                  - type: string
                    description: The slug of the environment where the secret is located.
              secretPath:
                allOf:
                  - type: string
                    default: /
                    description: The path of the secret.
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        secretKey:
                          type: string
                          description: The name of the secret to delete.
                        type:
                          type: string
                          enum:
                            - shared
                            - personal
                          default: shared
                      required:
                        - secretKey
                      additionalProperties: false
                    minItems: 1
            required: true
            requiredProperties:
              - environment
              - secrets
            additionalProperties: false
        examples:
          example:
            value:
              projectSlug: <string>
              workspaceId: <string>
              environment: <string>
              secretPath: /
              secrets:
                - secretKey: <string>
                  type: shared
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              secrets:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        _id:
                          type: string
                        workspace:
                          type: string
                        environment:
                          type: string
                        version:
                          type: number
                        type:
                          type: string
                        secretKey:
                          type: string
                        secretValue:
                          type: string
                        secretComment:
                          type: string
                        secretReminderNote:
                          type: string
                          nullable: true
                        secretReminderRepeatDays:
                          type: number
                          nullable: true
                        skipMultilineEncoding:
                          type: boolean
                          default: false
                          nullable: true
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                        actor:
                          type: object
                          properties:
                            actorId:
                              type: string
                              nullable: true
                            actorType:
                              type: string
                              nullable: true
                            name:
                              type: string
                              nullable: true
                            membershipId:
                              type: string
                              nullable: true
                            groupId:
                              type: string
                              nullable: true
                          additionalProperties: false
                          nullable: true
                        isRotatedSecret:
                          type: boolean
                        rotationId:
                          type: string
                          format: uuid
                          nullable: true
                        secretValueHidden:
                          type: boolean
                      required:
                        - id
                        - _id
                        - workspace
                        - environment
                        - version
                        - type
                        - secretKey
                        - secretValue
                        - secretComment
                        - createdAt
                        - updatedAt
                        - secretValueHidden
                      additionalProperties: false
            requiredProperties:
              - secrets
            additionalProperties: false
          - type: object
            properties:
              approval:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      policyId:
                        type: string
                        format: uuid
                      hasMerged:
                        type: boolean
                        default: false
                      status:
                        type: string
                        default: open
                      conflicts:
                        nullable: true
                      slug:
                        type: string
                      folderId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      isReplicated:
                        type: boolean
                        nullable: true
                      committerUserId:
                        type: string
                        format: uuid
                        nullable: true
                      statusChangedByUserId:
                        type: string
                        format: uuid
                        nullable: true
                      bypassReason:
                        type: string
                        nullable: true
                    required:
                      - id
                      - policyId
                      - slug
                      - folderId
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            description: When secret protection policy is enabled
            requiredProperties:
              - approval
            additionalProperties: false
        examples:
          example:
            value:
              secrets:
                - id: <string>
                  _id: <string>
                  workspace: <string>
                  environment: <string>
                  version: 123
                  type: <string>
                  secretKey: <string>
                  secretValue: <string>
                  secretComment: <string>
                  secretReminderNote: <string>
                  secretReminderRepeatDays: 123
                  skipMultilineEncoding: false
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  actor:
                    actorId: <string>
                    actorType: <string>
                    name: <string>
                    membershipId: <string>
                    groupId: <string>
                  isRotatedSecret: true
                  rotationId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  secretValueHidden: true
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