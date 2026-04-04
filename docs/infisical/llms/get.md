# Source: https://infisical.com/docs/api-reference/endpoints/service-tokens/get.md

# Source: https://infisical.com/docs/api-reference/endpoints/organization-roles/get.md

# Source: https://infisical.com/docs/api-reference/endpoints/groups/get.md

# Source: https://infisical.com/docs/api-reference/endpoints/dynamic-secrets/get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get



## OpenAPI

````yaml GET /api/v1/dynamic-secrets/{name}
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
  /api/v1/dynamic-secrets/{name}:
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
                      inputs: {}
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
                  - dynamicSecret
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