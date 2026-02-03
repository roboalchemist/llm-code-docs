# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/verify-project-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify project domain

> Attempts to verify a project domain with `verified = false` by checking the correctness of the project domain's `verification` challenge.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v9/projects/{idOrName}/domains/{domain}/verify
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
  /v9/projects/{idOrName}/domains/{domain}/verify:
    post:
      tags:
        - projects
      summary: Verify project domain
      description: >-
        Attempts to verify a project domain with `verified = false` by checking
        the correctness of the project domain's `verification` challenge.
      operationId: verifyProjectDomain
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            description: The unique project identifier or the project name
            type: string
        - name: domain
          description: The domain name you want to verify
          in: path
          required: true
          schema:
            description: The domain name you want to verify
            type: string
            example: example.com
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
          description: |-
            The project domain was verified successfully
            Domain is already verified
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
                required:
                  - apexName
                  - name
                  - projectId
                  - verified
                type: object
        '400':
          description: >-
            One of the provided values in the request query is invalid.

            There is an existing TXT record on the domain verifying it for
            another project

            The domain does not have a TXT record that attempts to verify the
            project domain

            The TXT record on the domain does not match the expected challenge
            for the project domain

            Project domain is not assigned to project
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