# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/create-one-or-more-environment-variables.md

# Create one or more environment variables

> Create one or more environment variables for a project by passing its `key`, `value`, `type` and `target` and by specifying the project by either passing the project `id` or `name` in the URL. If you include `upsert=true` as a query parameter, a new environment variable will not be created if it already exists but, the existing variable's value will be updated.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{idOrName}/env
paths:
  path: /v10/projects/{idOrName}/env
  method: post
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
        upsert:
          schema:
            - type: string
              required: false
              description: Allow override of environment variable if it already exists
              example: 'true'
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              key:
                allOf:
                  - &ref_0
                    description: The name of the environment variable
                    type: string
                    example: API_URL
              value:
                allOf:
                  - &ref_1
                    description: The value of the environment variable
                    type: string
                    example: https://api.vercel.com
              type:
                allOf:
                  - &ref_2
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
                allOf:
                  - &ref_3
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
                allOf:
                  - &ref_4
                    description: >-
                      If defined, the git branch of the environment variable
                      (must have target=preview)
                    type: string
                    maxLength: 250
                    example: feature-1
                    nullable: true
              comment:
                allOf:
                  - &ref_5
                    type: string
                    description: >-
                      A comment to add context on what this environment variable
                      is for
                    example: database connection string for production
                    maxLength: 500
              customEnvironmentIds:
                allOf:
                  - &ref_6
                    type: array
                    description: >-
                      The custom environment IDs associated with the environment
                      variable
                    items:
                      type: string
                      example: env_1234567890
            required: true
            requiredProperties:
              - key
              - value
              - type
              - target
          - type: object
            properties:
              key:
                allOf:
                  - *ref_0
              value:
                allOf:
                  - *ref_1
              type:
                allOf:
                  - *ref_2
              target:
                allOf:
                  - *ref_3
              gitBranch:
                allOf:
                  - *ref_4
              comment:
                allOf:
                  - *ref_5
              customEnvironmentIds:
                allOf:
                  - *ref_6
            required: true
            requiredProperties:
              - key
              - value
              - type
              - customEnvironmentIds
          - type: array
            items:
              allOf:
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
            required: true
        examples:
          example:
            value:
              key: API_URL
              value: https://api.vercel.com
              type: plain
              target:
                - preview
              gitBranch: feature-1
              comment: database connection string for production
              customEnvironmentIds:
                - env_1234567890
    codeSamples:
      - label: createProjectEnv
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.CreateProjectEnv(ctx, operations.CreateProjectEnvRequest{\n        IDOrName: \"prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA\",\n        Upsert: vercel.String(\"true\"),\n        RequestBody: vercel.Pointer(operations.CreateCreateProjectEnvRequestBodyCreateProjectEnvRequestBody1(\n            operations.CreateCreateProjectEnvRequestBody1CreateProjectEnv12(\n                operations.CreateProjectEnv12{\n                    Key: \"API_URL\",\n                    Value: \"https://api.vercel.com\",\n                    Type: operations.CreateProjectEnv1TypePlain,\n                    Target: []operations.CreateProjectEnv1Target{\n                        operations.CreateProjectEnv1TargetPreview,\n                    },\n                    GitBranch: vercel.String(\"feature-1\"),\n                    Comment: vercel.String(\"database connection string for production\"),\n                },\n            ),\n        )),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createProjectEnv
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.createProjectEnv({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              upsert: "true",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                key: "API_URL",
                value: "https://api.vercel.com",
                type: "plain",
                target: [
                  "preview",
                ],
                gitBranch: "feature-1",
                comment: "database connection string for production",
                customEnvironmentIds: [
                  "env_1234567890",
                ],
              },
            });

            console.log(result);
          }

          run();
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              created:
                allOf:
                  - oneOf:
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
                                  encrypted with a special key to make
                                  decryption possible in the subscriber Lambda.
                            required:
                              - type
                              - encryptedValue
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
                        required:
                          - type
                          - value
                          - key
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
                                    encrypted with a special key to make
                                    decryption possible in the subscriber
                                    Lambda.
                              required:
                                - type
                                - encryptedValue
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
                          required:
                            - type
                            - value
                            - key
                          type: object
                        type: array
              failed:
                allOf:
                  - items:
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
            requiredProperties:
              - created
              - failed
        examples:
          example:
            value:
              created:
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
              failed:
                - error:
                    code: <string>
                    message: <string>
                    key: <string>
                    envVarId: <string>
                    envVarKey: <string>
                    action: <string>
                    link: <string>
                    value: <string>
                    gitBranch: <string>
                    target:
                      - production
                    project: <string>
        description: The environment variable was created successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              One of the provided values in the request body is invalid.

              One of the provided values in the request query is invalid.

              The environment variable coudn't be created because an ongoing
              update env update is already happening

              The environment variable coudn't be created because project
              document is too large
        examples: {}
        description: >-
          One of the provided values in the request body is invalid.

          One of the provided values in the request query is invalid.

          The environment variable coudn't be created because an ongoing update
          env update is already happening

          The environment variable coudn't be created because project document
          is too large
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '402':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The account was soft-blocked for an unhandled reason.
              The account is missing a payment so payment method must be updated
        examples: {}
        description: |-
          The account was soft-blocked for an unhandled reason.
          The account is missing a payment so payment method must be updated
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              You do not have permission to access this resource.

              The environment variable cannot be created because it already
              exists

              Additional permissions are required to create production
              environment variables
        examples: {}
        description: >-
          You do not have permission to access this resource.

          The environment variable cannot be created because it already exists

          Additional permissions are required to create production environment
          variables
    '404': {}
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The project is being transfered and creating an environment
              variable is not possible
        examples: {}
        description: >-
          The project is being transfered and creating an environment variable
          is not possible
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````