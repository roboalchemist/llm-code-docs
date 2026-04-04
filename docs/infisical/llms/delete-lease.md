# Source: https://infisical.com/docs/api-reference/endpoints/dynamic-secrets/delete-lease.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Lease



## OpenAPI

````yaml DELETE /api/v1/dynamic-secrets/leases/{leaseId}
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
  /api/v1/dynamic-secrets/leases/{leaseId}:
    delete:
      tags:
        - Dynamic Secrets
      parameters:
        - schema:
            type: string
            minLength: 1
          in: path
          name: leaseId
          required: true
          description: The ID of the dynamic secret lease.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                projectSlug:
                  type: string
                  minLength: 1
                  description: The slug of the project of the dynamic secret in.
                path:
                  type: string
                  minLength: 1
                  default: /
                  description: The path of the dynamic secret in.
                environmentSlug:
                  type: string
                  minLength: 1
                  description: The slug of the environment of the dynamic secret in.
                isForced:
                  type: boolean
                  default: false
                  description: >-
                    A boolean flag to delete the the dynamic secret from
                    Infisical without trying to remove it from external
                    provider. Used when the dynamic secret got modified
                    externally.
              required:
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
                required:
                  - lease
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