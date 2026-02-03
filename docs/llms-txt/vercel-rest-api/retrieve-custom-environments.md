# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/retrieve-custom-environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve custom environments

> Retrieve custom environments for the project. Must not be named 'Production' or 'Preview'.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/custom-environments
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
  /v9/projects/{idOrName}/custom-environments:
    get:
      tags:
        - environment
      summary: Retrieve custom environments
      description: >-
        Retrieve custom environments for the project. Must not be named
        'Production' or 'Preview'.
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            type: string
        - name: gitBranch
          description: Fetch custom environments for a specific git branch
          in: query
          required: false
          schema:
            description: Fetch custom environments for a specific git branch
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  accountLimit:
                    properties:
                      total:
                        type: number
                    required:
                      - total
                    type: object
                    description: >-
                      The maximum number of custom environments allowed either
                      by the team's plan type or a custom override.
                  environments:
                    items:
                      properties:
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
                        createdAt:
                          type: number
                          description: Timestamp when the environment was created
                        updatedAt:
                          type: number
                          description: Timestamp when the environment was last updated
                        id:
                          type: string
                          description: >-
                            Unique identifier for the custom environment
                            (format: env_*)
                        slug:
                          type: string
                          description: URL-friendly name of the environment
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
                                  `true` if the domain is verified for use with
                                  the project. If `false` it will not be used as
                                  an alias on this project until the challenge
                                  in `verification` is completed.
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
                                    A list of verification challenges, one of
                                    which must be completed to verify the domain
                                    for use on the project. After the challenge
                                    is complete `POST
                                    /projects/:idOrName/domains/:domain/verify`
                                    to verify the domain. Possible challenges: -
                                    If `verification.type = TXT` the
                                    `verification.domain` will be checked for a
                                    TXT record matching `verification.value`.
                                type: array
                                description: >-
                                  A list of verification challenges, one of
                                  which must be completed to verify the domain
                                  for use on the project. After the challenge is
                                  complete `POST
                                  /projects/:idOrName/domains/:domain/verify` to
                                  verify the domain. Possible challenges: - If
                                  `verification.type = TXT` the
                                  `verification.domain` will be checked for a
                                  TXT record matching `verification.value`.
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
                      required:
                        - createdAt
                        - id
                        - slug
                        - type
                        - updatedAt
                      type: object
                    type: array
                required:
                  - accountLimit
                  - environments
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
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