# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/update-a-project-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a project domain

> Update a project domain's configuration, including the name, git branch and redirect of the domain.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/domains/{domain}
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
  /v9/projects/{idOrName}/domains/{domain}:
    patch:
      tags:
        - projects
      summary: Update a project domain
      description: >-
        Update a project domain's configuration, including the name, git branch
        and redirect of the domain.
      operationId: updateProjectDomain
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            type: string
        - name: domain
          description: The project domain name
          in: path
          required: true
          schema:
            description: The project domain name
            type: string
            example: www.example.com
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
              properties:
                gitBranch:
                  description: Git branch to link the project domain
                  example: null
                  type: string
                  maxLength: 250
                  nullable: true
                redirect:
                  description: Target destination domain for redirect
                  example: foobar.com
                  type: string
                  nullable: true
                redirectStatusCode:
                  description: Status code for domain redirect
                  example: 307
                  type: integer
                  enum:
                    - null
                    - 301
                    - 302
                    - 307
                    - 308
                  nullable: true
              type: object
        required: true
      responses:
        '200':
          description: The domain was updated successfuly
          content:
            application/json:
              schema:
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
                      `true` if the domain is verified for use with the project.
                      If `false` it will not be used as an alias on this project
                      until the challenge in `verification` is completed.
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
                        A list of verification challenges, one of which must be
                        completed to verify the domain for use on the project.
                        After the challenge is complete `POST
                        /projects/:idOrName/domains/:domain/verify` to verify
                        the domain. Possible challenges: - If `verification.type
                        = TXT` the `verification.domain` will be checked for a
                        TXT record matching `verification.value`.
                    type: array
                    description: >-
                      A list of verification challenges, one of which must be
                      completed to verify the domain for use on the project.
                      After the challenge is complete `POST
                      /projects/:idOrName/domains/:domain/verify` to verify the
                      domain. Possible challenges: - If `verification.type =
                      TXT` the `verification.domain` will be checked for a TXT
                      record matching `verification.value`.
                required:
                  - apexName
                  - name
                  - projectId
                  - verified
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
            The domain redirect is not valid
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '409':
          description: The project is currently being transferred
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````