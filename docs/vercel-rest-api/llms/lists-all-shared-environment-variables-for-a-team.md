# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/lists-all-shared-environment-variables-for-a-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Lists all Shared Environment Variables for a team

> Lists all Shared Environment Variables for a team, taking into account optional filters.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/env
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
    get:
      tags:
        - environment
      summary: Lists all Shared Environment Variables for a team
      description: >-
        Lists all Shared Environment Variables for a team, taking into account
        optional filters.
      operationId: listSharedEnvVariable
      parameters:
        - name: search
          in: query
          schema:
            type: string
        - name: projectId
          description: Filter SharedEnvVariables that belong to a project
          in: query
          schema:
            description: Filter SharedEnvVariables that belong to a project
            type: string
            example: prj_2WjyKQmM8ZnGcJsPWMrHRHrE
        - name: ids
          description: Filter SharedEnvVariables based on comma separated ids
          in: query
          schema:
            description: Filter SharedEnvVariables based on comma separated ids
            type: string
            example: env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV
        - name: exclude_ids
          description: Filter SharedEnvVariables based on comma separated ids
          in: query
          schema:
            description: Filter SharedEnvVariables based on comma separated ids
            type: string
            example: env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV
        - name: exclude-ids
          description: Filter SharedEnvVariables based on comma separated ids
          in: query
          schema:
            description: Filter SharedEnvVariables based on comma separated ids
            type: string
            example: env_2WjyKQmM8ZnGcJsPWMrHRHrE,env_2WjyKQmM8ZnGcJsPWMrHRCRV
        - name: exclude_projectId
          description: Filter SharedEnvVariables that belong to a project
          in: query
          schema:
            description: Filter SharedEnvVariables that belong to a project
            type: string
            example: prj_2WjyKQmM8ZnGcJsPWMrHRHrE
        - name: exclude-projectId
          description: Filter SharedEnvVariables that belong to a project
          in: query
          schema:
            description: Filter SharedEnvVariables that belong to a project
            type: string
            example: prj_2WjyKQmM8ZnGcJsPWMrHRHrE
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
          description: ''
          content:
            application/json:
              schema:
                properties:
                  data:
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
                  pagination:
                    $ref: '#/components/schemas/Pagination'
                required:
                  - data
                  - pagination
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
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