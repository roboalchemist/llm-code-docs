# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/attach-tags.md

# Attach tags

> Attach tags to a secret

## OpenAPI

````yaml POST /api/v3/secrets/tags/{secretName}
paths:
  path: /api/v3/secrets/tags/{secretName}
  method: post
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
      path:
        secretName:
          schema:
            - type: string
              required: true
              description: The name of the secret to attach tags to.
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
                    description: The slug of the project where the secret is located.
              environment:
                allOf:
                  - type: string
                    description: The slug of the environment where the secret is located
              secretPath:
                allOf:
                  - type: string
                    default: /
                    description: The path of the secret to attach tags to.
              type:
                allOf:
                  - type: string
                    enum:
                      - shared
                      - personal
                    default: shared
                    description: >-
                      The type of the secret to attach tags to.
                      (shared/personal)
              tagSlugs:
                allOf:
                  - type: array
                    items:
                      type: string
                    minItems: 1
                    description: An array of existing tag slugs to attach to the secret.
            required: true
            requiredProperties:
              - projectSlug
              - environment
              - tagSlugs
            additionalProperties: false
        examples:
          example:
            value:
              projectSlug: <string>
              environment: <string>
              secretPath: /
              type: shared
              tagSlugs:
                - <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              secret:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      version:
                        type: number
                        default: 1
                      type:
                        type: string
                        default: shared
                      secretKeyCiphertext:
                        type: string
                      secretKeyIV:
                        type: string
                      secretKeyTag:
                        type: string
                      secretValueCiphertext:
                        type: string
                      secretValueIV:
                        type: string
                      secretValueTag:
                        type: string
                      secretCommentCiphertext:
                        type: string
                        nullable: true
                      secretCommentIV:
                        type: string
                        nullable: true
                      secretCommentTag:
                        type: string
                        nullable: true
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
                      algorithm:
                        type: string
                        default: aes-256-gcm
                      keyEncoding:
                        type: string
                        default: utf8
                      metadata:
                        nullable: true
                      userId:
                        type: string
                        format: uuid
                        nullable: true
                      folderId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      tags:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                              format: uuid
                            slug:
                              type: string
                            color:
                              type: string
                              nullable: true
                            name:
                              type: string
                          required:
                            - id
                            - slug
                            - name
                          additionalProperties: false
                    required:
                      - id
                      - secretKeyCiphertext
                      - secretKeyIV
                      - secretKeyTag
                      - secretValueCiphertext
                      - secretValueIV
                      - secretValueTag
                      - folderId
                      - createdAt
                      - updatedAt
                      - tags
                    additionalProperties: false
            requiredProperties:
              - secret
            additionalProperties: false
        examples:
          example:
            value:
              secret:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                version: 1
                type: shared
                secretKeyCiphertext: <string>
                secretKeyIV: <string>
                secretKeyTag: <string>
                secretValueCiphertext: <string>
                secretValueIV: <string>
                secretValueTag: <string>
                secretCommentCiphertext: <string>
                secretCommentIV: <string>
                secretCommentTag: <string>
                secretReminderNote: <string>
                secretReminderRepeatDays: 123
                skipMultilineEncoding: false
                algorithm: aes-256-gcm
                keyEncoding: utf8
                metadata: <any>
                userId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                folderId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                tags:
                  - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    slug: <string>
                    color: <string>
                    name: <string>
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