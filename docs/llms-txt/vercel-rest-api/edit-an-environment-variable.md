# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/edit-an-environment-variable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit an environment variable

> Edit a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/env/{id}
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v9/projects/{idOrName}/env/{id}:
    patch:
      tags:
        - projects
      summary: Edit an environment variable
      description: >-
        Edit a specific environment variable for a given project by passing the
        environment variable identifier and either passing the project `id` or
        `name` in the URL.
      operationId: editProjectEnv
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            type: string
            example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
        - name: id
          description: The unique environment variable identifier
          in: path
          required: true
          schema:
            description: The unique environment variable identifier
            type: string
            example: XMbOEya1gUUO1ir4
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              properties:
                key:
                  description: The name of the environment variable
                  type: string
                  example: GITHUB_APP_ID
                target:
                  description: The target environment of the environment variable
                  type: array
                  items:
                    enum:
                      - production
                      - preview
                      - development
                  example:
                    - preview
                gitBranch:
                  description: >-
                    If defined, the git branch of the environment variable (must
                    have target=preview)
                  type: string
                  maxLength: 250
                  example: feature-1
                  nullable: true
                type:
                  description: The type of environment variable
                  type: string
                  enum:
                    - system
                    - secret
                    - encrypted
                    - plain
                    - sensitive
                  example: plain
                value:
                  description: The value of the environment variable
                  type: string
                  example: bkWIjbnxcvo78
                customEnvironmentIds:
                  type: array
                  description: >-
                    The custom environments that the environment variable should
                    be synced to
                  items:
                    type: string
                    example: env_1234567890
                comment:
                  type: string
                  description: A comment to add context on what this env var is for
                  example: database connection string for production
                  maxLength: 500
        required: true
      responses:
        '200':
          description: The environment variable was successfully edited
          content:
            application/json:
              schema:
                nullable: true
                properties:
                  type:
                    type: string
                    enum:
                      - secret
                      - system
                      - encrypted
                      - plain
                      - sensitive
                  value:
                    type: string
                  edgeConfigId:
                    nullable: true
                    type: string
                  edgeConfigTokenId:
                    nullable: true
                    type: string
                  createdAt:
                    type: number
                  updatedAt:
                    type: number
                  id:
                    type: string
                  createdBy:
                    nullable: true
                    type: string
                  target:
                    oneOf:
                      - items:
                          type: string
                          enum:
                            - production
                            - preview
                            - development
                            - preview
                            - development
                        type: array
                      - type: string
                        enum:
                          - production
                          - preview
                          - development
                          - preview
                          - development
                  key:
                    type: string
                  gitBranch:
                    type: string
                  updatedBy:
                    nullable: true
                    type: string
                  sunsetSecretId:
                    type: string
                    description: >-
                      This is used to identify variables that have been migrated
                      from type secret to sensitive.
                  legacyValue:
                    type: string
                    description: >-
                      Legacy now-encryption ciphertext, present after migration
                      swaps value/vsmValue
                  decrypted:
                    type: boolean
                    enum:
                      - false
                      - true
                  configurationId:
                    nullable: true
                    type: string
                  contentHint:
                    nullable: true
                    oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-url
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-url
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-token
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-read-only-token
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - blob-read-write-token
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-non-pooling
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-prisma-url
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-user
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-host
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-password
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-database
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-no-ssl
                          storeId:
                            type: string
                        required:
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - integration-store-secret
                          storeId:
                            type: string
                          integrationId:
                            type: string
                          integrationProductId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - integrationConfigurationId
                          - integrationId
                          - integrationProductId
                          - storeId
                          - type
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags-connection-string
                          projectId:
                            type: string
                        required:
                          - projectId
                          - type
                        type: object
                  internalContentHint:
                    nullable: true
                    properties:
                      type:
                        type: string
                        enum:
                          - flags-secret
                      encryptedValue:
                        type: string
                        description: >-
                          Contains the `value` of the env variable, encrypted
                          with a special key to make decryption possible in the
                          subscriber Lambda.
                    required:
                      - encryptedValue
                      - type
                    type: object
                    description: >-
                      Similar to `contentHints`, but should not be exposed to
                      the user.
                  comment:
                    type: string
                  customEnvironmentIds:
                    items:
                      type: string
                    type: array
                required:
                  - key
                  - type
                  - value
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
            At least one environment variable failed validation
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '409':
          description: >-
            The project is being transfered and removing an environment variable
            is not possible
        '429':
          description: ''
        '500':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````