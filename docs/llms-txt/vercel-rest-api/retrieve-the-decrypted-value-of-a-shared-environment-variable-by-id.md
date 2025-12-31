# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id.md

# Retrieve the decrypted value of a Shared Environment Variable by id.

> Retrieve the decrypted value of a Shared Environment Variable by id.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/env/{id}
paths:
  path: /v1/env/{id}
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
        id:
          schema:
            - type: string
              required: true
              description: >-
                The unique ID for the Shared Environment Variable to get the
                decrypted value.
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
    body: {}
    codeSamples:
      - label: getSharedEnvVar
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.getSharedEnvVar({
              id: "<id>",
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
              created:
                allOf:
                  - type: string
                    format: date-time
                    description: The date when the Shared Env Var was created.
                    example: '2021-02-10T13:11:49.180Z'
              key:
                allOf:
                  - type: string
                    description: The name of the Shared Env Var.
                    example: my-api-key
              ownerId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the owner (team) the Shared Env
                      Var was created for.
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
              id:
                allOf:
                  - type: string
                    description: The unique identifier of the Shared Env Var.
                    example: env_XCG7t7AIHuO2SBA8667zNUiM
              createdBy:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the user who created the Shared
                      Env Var.
                    example: 2qDDuGFTWXBLDNnqZfWPDp1A
              deletedBy:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the user who deleted the Shared
                      Env Var.
                    example: 2qDDuGFTWXBLDNnqZfWPDp1A
              updatedBy:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the user who last updated the
                      Shared Env Var.
                    example: 2qDDuGFTWXBLDNnqZfWPDp1A
              createdAt:
                allOf:
                  - type: number
                    description: Timestamp for when the Shared Env Var was created.
                    example: 1609492210000
              deletedAt:
                allOf:
                  - type: number
                    description: Timestamp for when the Shared Env Var was (soft) deleted.
                    example: 1609492210000
              updatedAt:
                allOf:
                  - type: number
                    description: Timestamp for when the Shared Env Var was last updated.
                    example: 1609492210000
              value:
                allOf:
                  - type: string
                    description: The value of the Shared Env Var.
              projectId:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: >-
                      The unique identifiers of the projects which the Shared
                      Env Var is linked to.
                    example:
                      - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                      - prj_2WjyKQmM8ZnGcJsPWMrasEFg
              type:
                allOf:
                  - type: string
                    enum:
                      - encrypted
                      - sensitive
                      - system
                      - plain
                    description: >-
                      The type of this cosmos doc instance, if blank, assume
                      secret.
                    example: encrypted
              target:
                allOf:
                  - items:
                      type: string
                      enum:
                        - production
                        - preview
                        - development
                      description: environments this env variable targets
                      example: production
                    type: array
                    description: environments this env variable targets
                    example: production
              applyToAllCustomEnvironments:
                allOf:
                  - type: boolean
                    description: >-
                      whether or not this env varible applies to custom
                      environments
              decrypted:
                allOf:
                  - type: boolean
                    description: whether or not this env variable is decrypted
              comment:
                allOf:
                  - type: string
                    description: >-
                      A user provided comment that describes what this Shared
                      Env Var is for.
              lastEditedByDisplayName:
                allOf:
                  - type: string
                    description: The last editor full name or username.
        examples:
          example:
            value:
              created: '2021-02-10T13:11:49.180Z'
              key: my-api-key
              ownerId: team_LLHUOMOoDlqOp8wPE4kFo9pE
              id: env_XCG7t7AIHuO2SBA8667zNUiM
              createdBy: 2qDDuGFTWXBLDNnqZfWPDp1A
              deletedBy: 2qDDuGFTWXBLDNnqZfWPDp1A
              updatedBy: 2qDDuGFTWXBLDNnqZfWPDp1A
              createdAt: 1609492210000
              deletedAt: 1609492210000
              updatedAt: 1609492210000
              value: <string>
              projectId:
                - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                - prj_2WjyKQmM8ZnGcJsPWMrasEFg
              type: encrypted
              target: production
              applyToAllCustomEnvironments: true
              decrypted: true
              comment: <string>
              lastEditedByDisplayName: <string>
        description: ''
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
  schemas: {}

````