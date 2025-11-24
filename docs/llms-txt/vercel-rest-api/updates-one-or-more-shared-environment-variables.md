# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/updates-one-or-more-shared-environment-variables.md

# Updates one or more shared environment variables

> Updates a given Shared Environment Variable for a Team.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/env
paths:
  path: /v1/env
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
      path: {}
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
              updates:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      additionalProperties: false
                      properties:
                        key:
                          description: The name of the Shared Environment Variable
                          type: string
                          example: API_URL
                        value:
                          description: The value of the Shared Environment Variable
                          type: string
                          example: https://api.vercel.com
                        target:
                          description: >-
                            The target environment of the Shared Environment
                            Variable
                          type: array
                          items:
                            enum:
                              - production
                              - preview
                              - development
                          example:
                            - production
                            - preview
                        projectId:
                          description: Associate a Shared Environment Variable to projects.
                          type: array
                          items:
                            type: string
                          example:
                            - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                            - prj_2WjyKQmM8ZnGcJsPWMrHRCRV
                        projectIdUpdates:
                          description: >-
                            Incrementally update project associations without
                            specifying the full list
                          type: object
                          additionalProperties: false
                          properties:
                            link:
                              description: Project IDs to add to this environment variable
                              type: array
                              items:
                                type: string
                              example:
                                - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                            unlink:
                              description: >-
                                Project IDs to remove from this environment
                                variable
                              type: array
                              items:
                                type: string
                              example:
                                - prj_2WjyKQmM8ZnGcJsPWMrHRCRV
                        type:
                          description: The new type of the Shared Environment Variable
                          type: string
                          enum:
                            - encrypted
                            - sensitive
                          example: encrypted
                        comment:
                          type: string
                          description: >-
                            A comment to add context on what this Shared
                            Environment Variable is for
                          example: database connection string for production
                          maxLength: 500
            requiredProperties:
              - updates
            additionalProperties: false
        examples:
          example:
            value:
              updates: {}
    codeSamples:
      - label: updateSharedEnvVariable
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.environment.updateSharedEnvVariable({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                updates: {

                },
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
              updated:
                allOf:
                  - items:
                      properties:
                        created:
                          type: string
                          format: date-time
                          description: The date when the Shared Env Var was created.
                          example: '2021-02-10T13:11:49.180Z'
                        key:
                          type: string
                          description: The name of the Shared Env Var.
                          example: my-api-key
                        ownerId:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the owner (team) the Shared
                            Env Var was created for.
                          example: team_LLHUOMOoDlqOp8wPE4kFo9pE
                        id:
                          type: string
                          description: The unique identifier of the Shared Env Var.
                          example: env_XCG7t7AIHuO2SBA8667zNUiM
                        createdBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who created the
                            Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        deletedBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who deleted the
                            Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        updatedBy:
                          nullable: true
                          type: string
                          description: >-
                            The unique identifier of the user who last updated
                            the Shared Env Var.
                          example: 2qDDuGFTWXBLDNnqZfWPDp1A
                        createdAt:
                          type: number
                          description: Timestamp for when the Shared Env Var was created.
                          example: 1609492210000
                        deletedAt:
                          type: number
                          description: >-
                            Timestamp for when the Shared Env Var was (soft)
                            deleted.
                          example: 1609492210000
                        updatedAt:
                          type: number
                          description: >-
                            Timestamp for when the Shared Env Var was last
                            updated.
                          example: 1609492210000
                        value:
                          type: string
                          description: The value of the Shared Env Var.
                        projectId:
                          items:
                            type: string
                          type: array
                          description: >-
                            The unique identifiers of the projects which the
                            Shared Env Var is linked to.
                          example:
                            - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
                            - prj_2WjyKQmM8ZnGcJsPWMrasEFg
                        type:
                          type: string
                          enum:
                            - encrypted
                            - sensitive
                            - system
                            - plain
                          description: >-
                            The type of this cosmos doc instance, if blank,
                            assume secret.
                          example: encrypted
                        target:
                          items:
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
                          type: boolean
                          description: >-
                            whether or not this env varible applies to custom
                            environments
                        decrypted:
                          type: boolean
                          description: whether or not this env variable is decrypted
                        comment:
                          type: string
                          description: >-
                            A user provided comment that describes what this
                            Shared Env Var is for.
                        lastEditedByDisplayName:
                          type: string
                          description: The last editor full name or username.
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
              - updated
              - failed
        examples:
          example:
            value:
              updated:
                - created: '2021-02-10T13:11:49.180Z'
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
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
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
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````