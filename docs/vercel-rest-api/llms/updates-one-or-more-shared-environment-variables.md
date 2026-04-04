# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/updates-one-or-more-shared-environment-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Updates one or more shared environment variables

> Updates a given Shared Environment Variable for a Team.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/env
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
  /v1/env:
    patch:
      tags:
        - environment
      summary: Updates one or more shared environment variables
      description: Updates a given Shared Environment Variable for a Team.
      operationId: updateSharedEnvVariable
      parameters:
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
              additionalProperties: false
              type: object
              required:
                - updates
              properties:
                updates:
                  description: >-
                    An object where each key is an environment variable ID (not
                    the key name) and the value is the update to apply
                  type: object
                  example:
                    env_2WjyKQmM8ZnGcJsPWMrHRHrE:
                      key: API_URL
                      value: https://api.vercel.com
                      target:
                        - production
                        - preview
                      projectIdUpdates:
                        link:
                          - prj_2WjyKQmM8ZnGcJsPWMrHRHrE
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
                          Incrementally update project linking without
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  updated:
                    items:
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
                            example: production
                            description: environments this env variable targets
                          type: array
                          description: environments this env variable targets
                          example: production
                        applyToAllCustomEnvironments:
                          type: boolean
                          enum:
                            - false
                            - true
                          description: >-
                            whether or not this env varible applies to custom
                            environments
                        decrypted:
                          type: boolean
                          enum:
                            - false
                            - true
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
                required:
                  - failed
                  - updated
                type: object
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````