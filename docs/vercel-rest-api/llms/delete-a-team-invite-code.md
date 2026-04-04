# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/delete-a-team-invite-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Team invite code

> Delete an active Team invite code.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/invites/{inviteId}
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
  /v1/teams/{teamId}/invites/{inviteId}:
    delete:
      tags:
        - teams
      summary: Delete a Team invite code
      description: Delete an active Team invite code.
      operationId: deleteTeamInviteCode
      parameters:
        - name: inviteId
          description: The Team invite code ID.
          in: path
          required: true
          schema:
            type: string
            description: The Team invite code ID.
            example: 2wn2hudbr4chb1ecywo9dvzo7g9sscs6mzcz8htdde0txyom4l
        - name: teamId
          description: The Team identifier to perform the request on behalf of.
          in: path
          required: true
          schema:
            type: string
            description: The Team identifier to perform the request on behalf of.
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      responses:
        '200':
          description: Successfully deleted Team invite code.
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                    description: ID of the team.
                required:
                  - id
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: |-
            You do not have permission to access this resource.
            Invite managed by directory sync
            Not authorized to access this team.
        '404':
          description: Team invite code not found.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````