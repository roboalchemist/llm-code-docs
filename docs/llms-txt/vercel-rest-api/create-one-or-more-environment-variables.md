# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/create-one-or-more-environment-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create one or more environment variables

> Create one or more environment variables for a project by passing its `key`, `value`, `type` and `target` and by specifying the project by either passing the project `id` or `name` in the URL. If you include `upsert=true` as a query parameter, a new environment variable will not be created if it already exists but, the existing variable's value will be updated.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{idOrName}/env
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
  /v10/projects/{idOrName}/env:
    post:
      tags:
        - projects
      summary: Create one or more environment variables
      description: >-
        Create one or more environment variables for a project by passing its
        `key`, `value`, `type` and `target` and by specifying the project by
        either passing the project `id` or `name` in the URL. If you include
        `upsert=true` as a query parameter, a new environment variable will not
        be created if it already exists but, the existing variable's value will
        be updated.
      operationId: createProjectEnv
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            type: string
            example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
        - name: upsert
          description: Allow override of environment variable if it already exists
          in: query
          required: false
          schema:
            description: Allow override of environment variable if it already exists
            type: string
            example: 'true'
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
              oneOf:
                - type: object
                  required:
                    - key
                    - value
                    - type
                  anyOf:
                    - required:
                        - target
                    - required:
                        - customEnvironmentIds
                  properties:
                    key:
                      description: The name of the environment variable
                      type: string
                      example: API_URL
                    value:
                      description: The value of the environment variable
                      type: string
                      example: https://api.vercel.com
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
                        If defined, the git branch of the environment variable
                        (must have target=preview)
                      type: string
                      maxLength: 250
                      example: feature-1
                      nullable: true
                    comment:
                      type: string
                      description: >-
                        A comment to add context on what this environment
                        variable is for
                      example: database connection string for production
                      maxLength: 500
                    customEnvironmentIds:
                      type: array
                      description: >-
                        The custom environment IDs associated with the
                        environment variable
                      items:
                        type: string
                        example: env_1234567890
                - type: array
                  items:
                    type: object
                    required:
                      - key
                      - value
                      - type
                    anyOf:
                      - required:
                          - target
                      - required:
                          - customEnvironmentIds
                    properties:
                      key:
                        description: The name of the environment variable
                        type: string
                        example: API_URL
                      value:
                        description: The value of the environment variable
                        type: string
                        example: https://api.vercel.com
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
                          If defined, the git branch of the environment variable
                          (must have target=preview)
                        type: string
                        maxLength: 250
                        example: feature-1
                        nullable: true
                      comment:
                        type: string
                        description: >-
                          A comment to add context on what this environment
                          variable is for
                        example: database connection string for production
                        maxLength: 500
                      customEnvironmentIds:
                        type: array
                        description: >-
                          The custom environment IDs associated with the
                          environment variable
                        items:
                          type: string
                          example: env_1234567890
        required: true
      responses:
        '201':
          description: The environment variable was created successfully
          content:
            application/json:
              schema:
                properties:
                  created:
                    oneOf:
                      - properties:
                          target:
                            oneOf:
                              - items:
                                  type: string
                                  enum:
                                    - production
                                    - preview
                                    - development
                                type: array
                              - type: string
                                enum:
                                  - production
                                  - preview
                                  - development
                          type:
                            type: string
                            enum:
                              - secret
                              - system
                              - encrypted
                              - plain
                              - sensitive
                          sunsetSecretId:
                            type: string
                            description: >-
                              This is used to identify variables that have been
                              migrated from type secret to sensitive.
                          legacyValue:
                            type: string
                            description: >-
                              Legacy now-encryption ciphertext, present after
                              migration swaps value/vsmValue
                          decrypted:
                            type: boolean
                            enum:
                              - false
                              - true
                          value:
                            type: string
                          vsmValue:
                            type: string
                          id:
                            type: string
                          key:
                            type: string
                          configurationId:
                            nullable: true
                            type: string
                          createdAt:
                            type: number
                          updatedAt:
                            type: number
                          createdBy:
                            nullable: true
                            type: string
                          updatedBy:
                            nullable: true
                            type: string
                          gitBranch:
                            type: string
                          edgeConfigId:
                            nullable: true
                            type: string
                          edgeConfigTokenId:
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
                                  Contains the `value` of the env variable,
                                  encrypted with a special key to make
                                  decryption possible in the subscriber Lambda.
                            required:
                              - encryptedValue
                              - type
                            type: object
                            description: >-
                              Similar to `contentHints`, but should not be
                              exposed to the user.
                          comment:
                            type: string
                          customEnvironmentIds:
                            items:
                              type: string
                            type: array
                          system:
                            type: boolean
                            enum:
                              - false
                              - true
                        required:
                          - key
                          - type
                          - value
                        type: object
                      - items:
                          properties:
                            target:
                              oneOf:
                                - items:
                                    type: string
                                  type: array
                                - type: string
                                  enum:
                                    - production
                                    - preview
                                    - development
                            type:
                              type: string
                              enum:
                                - secret
                                - system
                                - encrypted
                                - plain
                                - sensitive
                            sunsetSecretId:
                              type: string
                              description: >-
                                This is used to identify variables that have
                                been migrated from type secret to sensitive.
                            legacyValue:
                              type: string
                              description: >-
                                Legacy now-encryption ciphertext, present after
                                migration swaps value/vsmValue
                            decrypted:
                              type: boolean
                              enum:
                                - false
                                - true
                            value:
                              type: string
                            vsmValue:
                              type: string
                            id:
                              type: string
                            key:
                              type: string
                            configurationId:
                              nullable: true
                              type: string
                            createdAt:
                              type: number
                            updatedAt:
                              type: number
                            createdBy:
                              nullable: true
                              type: string
                            updatedBy:
                              nullable: true
                              type: string
                            gitBranch:
                              type: string
                            edgeConfigId:
                              nullable: true
                              type: string
                            edgeConfigTokenId:
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
                                    Contains the `value` of the env variable,
                                    encrypted with a special key to make
                                    decryption possible in the subscriber
                                    Lambda.
                              required:
                                - encryptedValue
                                - type
                              type: object
                              description: >-
                                Similar to `contentHints`, but should not be
                                exposed to the user.
                            comment:
                              type: string
                            customEnvironmentIds:
                              items:
                                type: string
                              type: array
                            system:
                              type: boolean
                              enum:
                                - false
                                - true
                          required:
                            - key
                            - type
                            - value
                          type: object
                        type: array
                  failed:
                    items:
                      properties:
                        error:
                          properties:
                            code:
                              type: string
                            message:
                              type: string
                            key:
                              type: string
                            envVarId:
                              type: string
                            envVarKey:
                              type: string
                            action:
                              type: string
                            link:
                              type: string
                            value:
                              oneOf:
                                - type: string
                                - items:
                                    type: string
                                    enum:
                                      - production
                                      - preview
                                      - development
                                  type: array
                            gitBranch:
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
                            project:
                              type: string
                          required:
                            - code
                            - message
                          type: object
                      required:
                        - error
                      type: object
                    type: array
                required:
                  - created
                  - failed
                type: object
        '400':
          description: >-
            One of the provided values in the request body is invalid.

            One of the provided values in the request query is invalid.

            The environment variable coudn't be created because an ongoing
            update env update is already happening

            The environment variable coudn't be created because project document
            is too large
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: >-
            You do not have permission to access this resource.

            The environment variable cannot be created because it already exists

            Additional permissions are required to create production environment
            variables
        '404':
          description: ''
        '409':
          description: >-
            The project is being transfered and creating an environment variable
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