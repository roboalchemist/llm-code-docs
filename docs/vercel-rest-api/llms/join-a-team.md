# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/join-a-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Join a team

> Join a team with a provided invite code or team ID.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/members/teams/join
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
  /v1/teams/{teamId}/members/teams/join:
    post:
      tags:
        - teams
      summary: Join a team
      description: Join a team with a provided invite code or team ID.
      operationId: joinTeam
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
              properties:
                inviteCode:
                  type: string
                  description: The invite code to join the team.
                  example: fisdh38aejkeivn34nslfore9vjtn4ls
        required: true
      responses:
        '200':
          description: Successfully joined a team.
          content:
            application/json:
              schema:
                properties:
                  teamId:
                    type: string
                    description: The ID of the team the user joined.
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
                  slug:
                    type: string
                    description: The slug of the team the user joined.
                    example: my-team
                  name:
                    type: string
                    description: The name of the team the user joined.
                    example: My Team
                  from:
                    type: string
                    description: The origin of how the user joined.
                    example: email
                required:
                  - from
                  - name
                  - slug
                  - teamId
                type: object
                description: Successfully joined a team.
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: ''
        '402':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
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