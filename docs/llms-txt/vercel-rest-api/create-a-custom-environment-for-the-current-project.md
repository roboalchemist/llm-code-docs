# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/create-a-custom-environment-for-the-current-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a custom environment for the current project.

> Creates a custom environment for the current project. Cannot be named 'Production' or 'Preview'.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v9/projects/{idOrName}/custom-environments
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
    post:
      tags:
        - environment
      summary: Create a custom environment for the current project.
      description: >-
        Creates a custom environment for the current project. Cannot be named
        'Production' or 'Preview'.
      operationId: createCustomEnvironment
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
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
                slug:
                  description: The slug of the custom environment to create.
                  type: string
                  maxLength: 32
                description:
                  description: Description of the custom environment. This is optional.
                  type: string
                  maxLength: 256
                branchMatcher:
                  required:
                    - type
                    - pattern
                  description: >-
                    How we want to determine a matching branch. This is
                    optional.
                  type: object
                  properties:
                    type:
                      description: >-
                        Type of matcher. One of \"equals\", \"startsWith\", or
                        \"endsWith\".
                      enum:
                        - equals
                        - startsWith
                        - endsWith
                    pattern:
                      description: Git branch name or portion thereof.
                      type: string
                      maxLength: 100
                copyEnvVarsFrom:
                  description: Where to copy environment variables from. This is optional.
                  type: string
      responses:
        '201':
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
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: You do not have permission to access this resource.
        '500':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````