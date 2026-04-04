# Source: https://infisical.com/docs/api-reference/endpoints/secrets/create-many.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/create-many.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Create

> Create many secrets



## OpenAPI

````yaml POST /api/v3/secrets/batch/raw
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v3/secrets/batch/raw:
    post:
      tags:
        - Secrets
      description: Create many secrets
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                projectSlug:
                  type: string
                  description: The slug of the project to update the secret in.
                workspaceId:
                  type: string
                  description: The ID of the project to update the secret in.
                environment:
                  type: string
                  description: The slug of the environment to create the secret in.
                secretPath:
                  type: string
                  default: /
                  description: The path to create the secret in.
                secrets:
                  type: array
                  items:
                    type: object
                    properties:
                      secretKey:
                        type: string
                        minLength: 1
                        description: The name of the secret to create.
                      secretValue:
                        type: string
                        description: The value of the secret to create.
                      secretComment:
                        type: string
                        default: ''
                        description: Attach a comment to the secret.
                      skipMultilineEncoding:
                        type: boolean
                        description: Skip multiline encoding for the secret value.
                      metadata:
                        type: object
                        additionalProperties:
                          type: string
                      secretMetadata:
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
                            isEncrypted:
                              type: boolean
                              default: false
                          required:
                            - key
                          additionalProperties: false
                      tagIds:
                        type: array
                        items:
                          type: string
                        description: >-
                          The ID of the tags to be attached to the created
                          secret.
                    required:
                      - secretKey
                      - secretValue
                    additionalProperties: false
                  minItems: 1
              required:
                - environment
                - secrets
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                anyOf:
                  - type: object
                    properties:
                      secrets:
                        type: array
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
                          additionalProperties: false
                    required:
                      - secrets
                    additionalProperties: false
                  - type: object
                    properties:
                      approval:
                        type: object
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
                    required:
                      - approval
                    additionalProperties: false
                    description: When secret protection policy is enabled
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````