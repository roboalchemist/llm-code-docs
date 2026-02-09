# Source: https://infisical.com/docs/api-reference/endpoints/dynamic-secrets/list-leases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Leases



## OpenAPI

````yaml GET /api/v1/dynamic-secrets/{name}/leases
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
  /api/v1/dynamic-secrets/{name}/leases:
    get:
      tags:
        - Dynamic Secrets
      parameters:
        - schema:
            type: string
            minLength: 1
          in: query
          name: projectSlug
          required: true
          description: The slug of the project to create dynamic secret in.
        - schema:
            type: string
            default: /
          in: query
          name: path
          required: false
          description: The path to list folders from.
        - schema:
            type: string
            minLength: 1
          in: query
          name: environmentSlug
          required: true
          description: The slug of the environment to list folders from.
        - schema:
            type: string
            minLength: 1
          in: path
          name: name
          required: true
          description: The name of the dynamic secret.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  leases:
                    type: array
                    items:
                      type: object
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
                required:
                  - leases
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

````