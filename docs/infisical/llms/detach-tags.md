# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/secrets/detach-tags.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Detach tags

> Detach tags from a secret



## OpenAPI

````yaml DELETE /api/v3/secrets/tags/{secretName}
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
  /api/v3/secrets/tags/{secretName}:
    delete:
      tags:
        - Secrets
      description: Detach tags from a secret
      parameters:
        - schema:
            type: string
          in: path
          name: secretName
          required: true
          description: The name of the secret to detach tags from.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                projectSlug:
                  type: string
                  description: The slug of the project where the secret is located.
                environment:
                  type: string
                  description: The slug of the environment where the secret is located.
                secretPath:
                  type: string
                  default: /
                  description: The path of the secret to detach tags from.
                type:
                  type: string
                  enum:
                    - shared
                    - personal
                  default: shared
                  description: The type of the secret to attach tags to. (shared/personal)
                tagSlugs:
                  type: array
                  items:
                    type: string
                  minItems: 1
                  description: An array of existing tag slugs to detach from the secret.
              required:
                - projectSlug
                - environment
                - tagSlugs
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  secret:
                    type: object
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
                required:
                  - secret
                additionalProperties: false
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