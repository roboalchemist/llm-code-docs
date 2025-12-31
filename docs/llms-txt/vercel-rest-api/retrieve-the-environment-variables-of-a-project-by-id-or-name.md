# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name.md

# Retrieve the environment variables of a project by id or name

> Retrieve the environment variables for a given project by passing either the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v10/projects/{idOrName}/env
paths:
  path: /v10/projects/{idOrName}/env
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrName:
          schema:
            - type: string
              required: true
              description: The unique project identifier or the project name
              example: prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA
      query:
        gitBranch:
          schema:
            - type: string
              required: false
              description: >-
                If defined, the git branch of the environment variable to filter
                the results (must have target=preview)
              maxLength: 250
              example: feature-1
        decrypt:
          schema:
            - type: enum<string>
              enum:
                - 'true'
                - 'false'
              required: false
              description: If true, the environment variable value will be decrypted
              deprecated: true
              example: 'true'
        source:
          schema:
            - type: string
              required: false
              description: The source that is calling the endpoint.
              example: vercel-cli:pull
        customEnvironmentId:
          schema:
            - type: string
              required: false
              description: The unique custom environment identifier within the project
              example: env_123abc4567
        customEnvironmentSlug:
          schema:
            - type: string
              required: false
              description: The custom environment slug (name) within the project
              example: my-custom-env
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: filterProjectEnvs
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.filterProjectEnvs({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              gitBranch: "feature-1",
              decrypt: "true",
              source: "vercel-cli:pull",
              customEnvironmentId: "env_123abc4567",
              customEnvironmentSlug: "my-custom-env",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              target:
                allOf:
                  - oneOf:
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
                allOf:
                  - type: string
                    enum:
                      - system
                      - encrypted
                      - plain
                      - sensitive
                      - secret
              sunsetSecretId:
                allOf:
                  - type: string
                    description: >-
                      This is used to identiy variables that have been migrated
                      from type secret to sensitive.
              decrypted:
                allOf:
                  - type: boolean
              value:
                allOf:
                  - type: string
              vsmValue:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              key:
                allOf:
                  - type: string
              configurationId:
                allOf:
                  - nullable: true
                    type: string
              createdAt:
                allOf:
                  - type: number
              updatedAt:
                allOf:
                  - type: number
              createdBy:
                allOf:
                  - nullable: true
                    type: string
              updatedBy:
                allOf:
                  - nullable: true
                    type: string
              gitBranch:
                allOf:
                  - type: string
              edgeConfigId:
                allOf:
                  - nullable: true
                    type: string
              edgeConfigTokenId:
                allOf:
                  - nullable: true
                    type: string
              contentHint:
                allOf:
                  - nullable: true
                    oneOf:
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - redis-rest-api-read-only-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - blob-read-write-token
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-non-pooling
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-prisma-url
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-user
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-host
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-password
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-database
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - postgres-url-no-ssl
                          storeId:
                            type: string
                        required:
                          - type
                          - storeId
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
                          - type
                          - storeId
                          - integrationId
                          - integrationProductId
                          - integrationConfigurationId
                        type: object
                      - properties:
                          type:
                            type: string
                            enum:
                              - flags-connection-string
                          projectId:
                            type: string
                        required:
                          - type
                          - projectId
                        type: object
              internalContentHint:
                allOf:
                  - nullable: true
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
                      - type
                      - encryptedValue
                    type: object
                    description: >-
                      Similar to `contentHints`, but should not be exposed to
                      the user.
              comment:
                allOf:
                  - type: string
              customEnvironmentIds:
                allOf:
                  - items:
                      type: string
                    type: array
              system:
                allOf:
                  - type: boolean
            requiredProperties:
              - type
              - value
              - key
          - type: object
            properties:
              envs:
                allOf:
                  - items:
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
                            - system
                            - encrypted
                            - plain
                            - sensitive
                            - secret
                        sunsetSecretId:
                          type: string
                          description: >-
                            This is used to identiy variables that have been
                            migrated from type secret to sensitive.
                        decrypted:
                          type: boolean
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
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-read-only-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - blob-read-write-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-non-pooling
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-prisma-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-user
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-host
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-password
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-database
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-no-ssl
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
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
                                - type
                                - storeId
                                - integrationId
                                - integrationProductId
                                - integrationConfigurationId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - flags-connection-string
                                projectId:
                                  type: string
                              required:
                                - type
                                - projectId
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
                            - type
                            - encryptedValue
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
                      required:
                        - type
                        - value
                        - key
                      type: object
                    type: array
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            requiredProperties:
              - envs
              - pagination
          - type: object
            properties:
              envs:
                allOf:
                  - items:
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
                            - system
                            - encrypted
                            - plain
                            - sensitive
                            - secret
                        sunsetSecretId:
                          type: string
                          description: >-
                            This is used to identiy variables that have been
                            migrated from type secret to sensitive.
                        decrypted:
                          type: boolean
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
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - redis-rest-api-read-only-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - blob-read-write-token
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-non-pooling
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-prisma-url
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-user
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-host
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-password
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-database
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - postgres-url-no-ssl
                                storeId:
                                  type: string
                              required:
                                - type
                                - storeId
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
                                - type
                                - storeId
                                - integrationId
                                - integrationProductId
                                - integrationConfigurationId
                              type: object
                            - properties:
                                type:
                                  type: string
                                  enum:
                                    - flags-connection-string
                                projectId:
                                  type: string
                              required:
                                - type
                                - projectId
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
                            - type
                            - encryptedValue
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
                      required:
                        - type
                        - value
                        - key
                      type: object
                    type: array
            description: The list of environment variables for the given project
            requiredProperties:
              - envs
        examples:
          example:
            value:
              target:
                - production
              type: system
              sunsetSecretId: <string>
              decrypted: true
              value: <string>
              vsmValue: <string>
              id: <string>
              key: <string>
              configurationId: <string>
              createdAt: 123
              updatedAt: 123
              createdBy: <string>
              updatedBy: <string>
              gitBranch: <string>
              edgeConfigId: <string>
              edgeConfigTokenId: <string>
              contentHint:
                type: redis-url
                storeId: <string>
              internalContentHint:
                type: flags-secret
                encryptedValue: <string>
              comment: <string>
              customEnvironmentIds:
                - <string>
              system: true
        description: The list of environment variables for the given project
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
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

````