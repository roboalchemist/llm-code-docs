# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve the environment variables of a project by id or name

> Retrieve the environment variables for a given project by passing either the project `id` or `name` in the URL.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v10/projects/{idOrName}/env
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
    get:
      tags:
        - projects
      summary: Retrieve the environment variables of a project by id or name
      description: >-
        Retrieve the environment variables for a given project by passing either
        the project `id` or `name` in the URL.
      operationId: filterProjectEnvs
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            type: string
            example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
        - name: gitBranch
          description: >-
            If defined, the git branch of the environment variable to filter the
            results (must have target=preview)
          in: query
          required: false
          schema:
            description: >-
              If defined, the git branch of the environment variable to filter
              the results (must have target=preview)
            type: string
            maxLength: 250
            example: feature-1
        - name: decrypt
          description: If true, the environment variable value will be decrypted
          in: query
          required: false
          schema:
            description: If true, the environment variable value will be decrypted
            type: string
            enum:
              - 'true'
              - 'false'
            example: 'true'
            deprecated: true
        - name: source
          description: The source that is calling the endpoint.
          in: query
          required: false
          schema:
            description: The source that is calling the endpoint.
            type: string
            example: vercel-cli:pull
        - name: customEnvironmentId
          description: The unique custom environment identifier within the project
          in: query
          required: false
          schema:
            description: The unique custom environment identifier within the project
            type: string
            example: env_123abc4567
        - name: customEnvironmentSlug
          description: The custom environment slug (name) within the project
          in: query
          required: false
          schema:
            type: string
            description: The custom environment slug (name) within the project
            example: my-custom-env
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
      responses:
        '200':
          description: The list of environment variables for the given project
          content:
            application/json:
              schema:
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
                              encrypted with a special key to make decryption
                              possible in the subscriber Lambda.
                        required:
                          - encryptedValue
                          - type
                        type: object
                        description: >-
                          Similar to `contentHints`, but should not be exposed
                          to the user.
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
                  - properties:
                      envs:
                        items:
                          properties:
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
                      pagination:
                        $ref: '#/components/schemas/Pagination'
                    required:
                      - envs
                      - pagination
                    type: object
                  - properties:
                      envs:
                        items:
                          properties:
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
                    required:
                      - envs
                    type: object
                    description: The list of environment variables for the given project
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  schemas:
    Pagination:
      properties:
        count:
          type: number
          description: Amount of items in the current page.
          example: 20
        next:
          nullable: true
          type: number
          description: Timestamp that must be used to request the next page.
          example: 1540095775951
        prev:
          nullable: true
          type: number
          description: Timestamp that must be used to request the previous page.
          example: 1540095775951
      required:
        - count
        - next
        - prev
      type: object
      description: >-
        This object contains information related to the pagination of the
        current request, including the necessary parameters to get the next or
        previous page of data.
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````