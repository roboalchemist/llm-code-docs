# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/edit-an-environment-variable.md

# Edit an environment variable

> Edit a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/env/{id}
paths:
  path: /v9/projects/{idOrName}/env/{id}
  method: patch
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
        id:
          schema:
            - type: string
              required: true
              description: The unique environment variable identifier
              example: XMbOEya1gUUO1ir4
      query:
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
                  - description: The name of the environment variable
                    type: string
                    example: GITHUB_APP_ID
              target:
                allOf:
                  - description: The target environment of the environment variable
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
                  - description: >-
                      If defined, the git branch of the environment variable
                      (must have target=preview)
                    type: string
                    maxLength: 250
                    example: feature-1
                    nullable: true
              type:
                allOf:
                  - description: The type of environment variable
                    type: string
                    enum:
                      - system
                      - secret
                      - encrypted
                      - plain
                      - sensitive
                    example: plain
              value:
                allOf:
                  - description: The value of the environment variable
                    type: string
                    example: bkWIjbnxcvo78
              customEnvironmentIds:
                allOf:
                  - type: array
                    description: >-
                      The custom environments that the environment variable
                      should be synced to
                    items:
                      type: string
                      example: env_1234567890
              comment:
                allOf:
                  - type: string
                    description: A comment to add context on what this env var is for
                    example: database connection string for production
                    maxLength: 500
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              key: GITHUB_APP_ID
              target:
                - preview
              gitBranch: feature-1
              type: plain
              value: bkWIjbnxcvo78
              customEnvironmentIds:
                - env_1234567890
              comment: database connection string for production
    codeSamples:
      - label: editProjectEnv
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Projects.EditProjectEnv(ctx, operations.EditProjectEnvRequest{\n        IDOrName: \"prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA\",\n        ID: \"XMbOEya1gUUO1ir4\",\n        RequestBody: &operations.EditProjectEnvRequestBody{\n            Key: vercel.String(\"GITHUB_APP_ID\"),\n            Target: []operations.EditProjectEnvTarget{\n                operations.EditProjectEnvTargetPreview,\n            },\n            GitBranch: vercel.String(\"feature-1\"),\n            Type: operations.EditProjectEnvTypePlain.ToPointer(),\n            Value: vercel.String(\"bkWIjbnxcvo78\"),\n            CustomEnvironmentIds: []string{\n                \"env_1234567890\",\n            },\n            Comment: vercel.String(\"database connection string for production\"),\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: editProjectEnv
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.projects.editProjectEnv({
              idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",
              id: "XMbOEya1gUUO1ir4",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                key: "GITHUB_APP_ID",
                target: [
                  "preview",
                ],
                gitBranch: "feature-1",
                type: "plain",
                value: "bkWIjbnxcvo78",
                customEnvironmentIds: [
                  "env_1234567890",
                ],
                comment: "database connection string for production",
              },
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
                        type: array
                      - type: string
                        enum:
                          - production
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
            requiredProperties:
              - type
              - value
              - key
          - type: object
            properties: {}
        examples:
          example:
            value:
              target:
                - <string>
              type: system
              sunsetSecretId: <string>
              decrypted: true
              value: <string>
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
        description: The environment variable was successfully edited
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              At least one environment variable failed validation
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          At least one environment variable failed validation
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
    '404': {}
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: >-
              The project is being transfered and removing an environment
              variable is not possible
        examples: {}
        description: >-
          The project is being transfered and removing an environment variable
          is not possible
    '429': {}
    '500': {}
  deprecated: false
  type: path
components:
  schemas: {}

````