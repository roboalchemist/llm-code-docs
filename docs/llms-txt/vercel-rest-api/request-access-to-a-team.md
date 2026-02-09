# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/request-access-to-a-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Request access to a team

> Request access to a team as a member. An owner has to approve the request. Only 10 users can request access to a team at the same time.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/request
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
  /v1/teams/{teamId}/request:
    post:
      tags:
        - teams
      summary: Request access to a team
      description: >-
        Request access to a team as a member. An owner has to approve the
        request. Only 10 users can request access to a team at the same time.
      operationId: requestAccessToTeam
      parameters:
        - name: teamId
          in: path
          required: true
          schema:
            type: string
            description: The unique team identifier
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              required:
                - joinedFrom
              properties:
                joinedFrom:
                  type: object
                  additionalProperties: false
                  required:
                    - origin
                  properties:
                    origin:
                      type: string
                      enum:
                        - import
                        - teams
                        - github
                        - gitlab
                        - bitbucket
                        - feedback
                        - organization-teams
                      description: The origin of the request.
                      example: github
                    commitId:
                      type: string
                      description: The commit sha if the origin is a git provider.
                      example: f498d25d8bd654b578716203be73084b31130cd7
                    repoId:
                      type: string
                      description: The ID of the repository for the given Git provider.
                      example: '67753070'
                    repoPath:
                      type: string
                      description: The path to the repository for the given Git provider.
                      example: jane-doe/example
                    gitUserId:
                      description: >-
                        The ID of the Git account of the user who requests
                        access.
                      example: 103053343
                      oneOf:
                        - type: string
                        - type: number
                    gitUserLogin:
                      type: string
                      description: >-
                        The login name for the Git account of the user who
                        requests access.
                      example: jane-doe
        required: true
      responses:
        '200':
          description: Successfuly requested access to the team.
          content:
            application/json:
              schema:
                properties:
                  teamSlug:
                    type: string
                  teamName:
                    type: string
                  confirmed:
                    type: boolean
                    enum:
                      - false
                      - true
                  joinedFrom:
                    properties:
                      origin:
                        type: string
                        enum:
                          - teams
                          - link
                          - import
                          - mail
                          - github
                          - gitlab
                          - bitbucket
                          - saml
                          - dsync
                          - feedback
                          - organization-teams
                          - nsnb-auto-approve
                      commitId:
                        type: string
                      repoId:
                        type: string
                      repoPath:
                        type: string
                      gitUserId:
                        oneOf:
                          - type: string
                          - type: number
                      gitUserLogin:
                        type: string
                      ssoUserId:
                        type: string
                      ssoConnectedAt:
                        type: number
                      idpUserId:
                        type: string
                      dsyncUserId:
                        type: string
                      dsyncConnectedAt:
                        type: number
                    required:
                      - origin
                    type: object
                  accessRequestedAt:
                    type: number
                  github:
                    nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                  gitlab:
                    nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                  bitbucket:
                    nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                required:
                  - bitbucket
                  - github
                  - gitlab
                  - teamName
                  - teamSlug
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: The team was not found.
        '503':
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