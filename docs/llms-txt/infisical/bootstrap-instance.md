# Source: https://infisical.com/docs/api-reference/endpoints/admin/bootstrap-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bootstrap Instance

<Note>
  For guidance, check out the docs for [Programmatic
  Provisioning](/self-hosting/guides/automated-bootstrapping).
</Note>


## OpenAPI

````yaml POST /api/v1/admin/bootstrap
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
  /api/v1/admin/bootstrap:
    post:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                  format: email
                  minLength: 1
                password:
                  type: string
                  minLength: 1
                organization:
                  type: string
                  minLength: 1
              required:
                - email
                - password
                - organization
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
                  message:
                    type: string
                  user:
                    type: object
                    properties:
                      username:
                        type: string
                      firstName:
                        type: string
                        nullable: true
                      lastName:
                        type: string
                        nullable: true
                      email:
                        type: string
                        nullable: true
                      id:
                        type: string
                        format: uuid
                      superAdmin:
                        type: boolean
                        default: false
                        nullable: true
                    required:
                      - username
                      - id
                    additionalProperties: false
                  organization:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      slug:
                        type: string
                    required:
                      - id
                      - name
                      - slug
                    additionalProperties: false
                  identity:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      credentials:
                        type: object
                        properties:
                          token:
                            type: string
                        required:
                          - token
                        additionalProperties: false
                    required:
                      - id
                      - name
                      - credentials
                    additionalProperties: false
                required:
                  - message
                  - user
                  - organization
                  - identity
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