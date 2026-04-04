# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/remove-a-custom-environment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove a custom environment

> Remove a custom environment for the project. Must not be named 'Production' or 'Preview'.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
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
  /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}:
    delete:
      tags:
        - environment
      summary: Remove a custom environment
      description: >-
        Remove a custom environment for the project. Must not be named
        'Production' or 'Preview'.
      operationId: removeCustomEnvironment
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            type: string
        - name: environmentSlugOrId
          description: The unique custom environment identifier within the project
          in: path
          required: true
          schema:
            description: The unique custom environment identifier within the project
            type: string
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
              properties:
                deleteUnassignedEnvironmentVariables:
                  description: >-
                    Delete Environment Variables that are not assigned to any
                    environments.
                  type: boolean
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                    description: >-
                      Unique identifier for the custom environment (format:
                      env_*)
                  slug:
                    type: string
                    description: URL-friendly name of the environment
                  type:
                    type: string
                    enum:
                      - production
                      - preview
                      - development
                    description: >-
                      The type of environment (production, preview, or
                      development)
                  description:
                    type: string
                    description: Optional description of the environment's purpose
                  branchMatcher:
                    properties:
                      type:
                        type: string
                        enum:
                          - endsWith
                          - startsWith
                          - equals
                        description: The type of matching to perform
                      pattern:
                        type: string
                        description: The pattern to match against branch names
                    required:
                      - pattern
                      - type
                    type: object
                    description: >-
                      Configuration for matching git branches to this
                      environment
                  domains:
                    items:
                      properties:
                        name:
                          type: string
                        apexName:
                          type: string
                        projectId:
                          type: string
                        redirect:
                          nullable: true
                          type: string
                        redirectStatusCode:
                          nullable: true
                          type: number
                          enum:
                            - 301
                            - 302
                            - 307
                            - 308
                        gitBranch:
                          nullable: true
                          type: string
                        customEnvironmentId:
                          nullable: true
                          type: string
                        updatedAt:
                          type: number
                        createdAt:
                          type: number
                        verified:
                          type: boolean
                          enum:
                            - false
                            - true
                          description: >-
                            `true` if the domain is verified for use with the
                            project. If `false` it will not be used as an alias
                            on this project until the challenge in
                            `verification` is completed.
                        verification:
                          items:
                            properties:
                              type:
                                type: string
                              domain:
                                type: string
                              value:
                                type: string
                              reason:
                                type: string
                            required:
                              - domain
                              - reason
                              - type
                              - value
                            type: object
                            description: >-
                              A list of verification challenges, one of which
                              must be completed to verify the domain for use on
                              the project. After the challenge is complete `POST
                              /projects/:idOrName/domains/:domain/verify` to
                              verify the domain. Possible challenges: - If
                              `verification.type = TXT` the
                              `verification.domain` will be checked for a TXT
                              record matching `verification.value`.
                          type: array
                          description: >-
                            A list of verification challenges, one of which must
                            be completed to verify the domain for use on the
                            project. After the challenge is complete `POST
                            /projects/:idOrName/domains/:domain/verify` to
                            verify the domain. Possible challenges: - If
                            `verification.type = TXT` the `verification.domain`
                            will be checked for a TXT record matching
                            `verification.value`.
                      required:
                        - apexName
                        - name
                        - projectId
                        - verified
                      type: object
                      description: List of domains associated with this environment
                    type: array
                    description: List of domains associated with this environment
                  currentDeploymentAliases:
                    items:
                      type: string
                    type: array
                    description: List of aliases for the current deployment
                  createdAt:
                    type: number
                    description: Timestamp when the environment was created
                  updatedAt:
                    type: number
                    description: Timestamp when the environment was last updated
                required:
                  - createdAt
                  - id
                  - slug
                  - type
                  - updatedAt
                type: object
                description: >-
                  Internal representation of a custom environment with all
                  required properties
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
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