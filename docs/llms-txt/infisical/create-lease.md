# Source: https://infisical.com/docs/api-reference/endpoints/dynamic-secrets/kubernetes/create-lease.md

# Source: https://infisical.com/docs/api-reference/endpoints/dynamic-secrets/create-lease.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Lease



## OpenAPI

````yaml POST /api/v1/dynamic-secrets/leases
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
  /api/v1/dynamic-secrets/leases:
    post:
      tags:
        - Dynamic Secrets
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                dynamicSecretName:
                  type: string
                  minLength: 1
                  description: The name of the dynamic secret.
                projectSlug:
                  type: string
                  minLength: 1
                  description: The slug of the project of the dynamic secret in.
                ttl:
                  type: string
                  description: >-
                    The lease lifetime TTL. If not provided the default TTL of
                    dynamic secret will be used.
                path:
                  type: string
                  default: /
                  description: The path of the dynamic secret in.
                environmentSlug:
                  type: string
                  minLength: 1
                  description: The slug of the environment of the dynamic secret in.
                config: {}
              required:
                - dynamicSecretName
                - projectSlug
                - environmentSlug
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
                  lease:
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
                  data: {}
                required:
                  - lease
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