# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/get-access-request-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get access request status

> Check the status of a join request. It'll respond with a 404 if the request has been declined. If no `userId` path segment was provided, this endpoint will instead return the status of the authenticated user.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/teams/{teamId}/request/{userId}
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
  /v1/teams/{teamId}/request/{userId}:
    get:
      tags:
        - teams
      summary: Get access request status
      description: >-
        Check the status of a join request. It'll respond with a 404 if the
        request has been declined. If no `userId` path segment was provided,
        this endpoint will instead return the status of the authenticated user.
      operationId: getTeamAccessRequest
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: string
            description: The unique user identifier
        - name: teamId
          in: path
          required: true
          schema:
            type: string
            description: The unique team identifier
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      responses:
        '200':
          description: Successfully
          content:
            application/json:
              schema:
                properties:
                  teamSlug:
                    type: string
                    description: The slug of the team.
                    example: my-team
                  teamName:
                    type: string
                    description: The name of the team.
                    example: My Team
                  confirmed:
                    type: boolean
                    enum:
                      - false
                      - true
                    description: >-
                      Current status of the membership. Will be `true` if
                      confirmed, if pending it'll be `false`.
                    example: false
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
                    description: >-
                      A map that describes the origin from where the user
                      joined.
                  accessRequestedAt:
                    type: number
                    description: >-
                      Timestamp in milliseconds when the user requested access
                      to the team.
                    example: 1588720733602
                  github:
                    nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected GitHub account.
                  gitlab:
                    nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected GitLab account.
                  bitbucket:
                    nullable: true
                    properties:
                      login:
                        type: string
                    type: object
                    description: Map of the connected Bitbucket account.
                required:
                  - accessRequestedAt
                  - bitbucket
                  - confirmed
                  - github
                  - gitlab
                  - joinedFrom
                  - teamName
                  - teamSlug
                type: object
        '400':
          description: >-
            One of the provided values in the request query is invalid.

            User is already a confirmed member of the team and did not request
            access. Only visible when the authenticated user does have access to
            the team.
        '401':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: |-
            The provided user doesn't have a membership.
            Team was not found.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````