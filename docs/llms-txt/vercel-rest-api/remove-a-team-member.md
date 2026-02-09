# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/remove-a-team-member.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove a Team Member

> Remove a Team Member from the Team, or dismiss a user that requested access, or leave a team.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/members/{uid}
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
  /v1/teams/{teamId}/members/{uid}:
    delete:
      tags:
        - teams
      summary: Remove a Team Member
      description: >-
        Remove a Team Member from the Team, or dismiss a user that requested
        access, or leave a team.
      operationId: removeTeamMember
      parameters:
        - name: uid
          description: The user ID of the member.
          in: path
          required: true
          schema:
            type: string
            description: The user ID of the member.
            example: ndlgr43fadlPyCtREAqxxdyFK
        - name: newDefaultTeamId
          description: >-
            The ID of the team to set as the new default team for the Northstar
            user.
          in: query
          required: false
          schema:
            type: string
            description: >-
              The ID of the team to set as the new default team for the
              Northstar user.
            example: team_nllPyCtREAqxxdyFKbbMDlxd
        - name: teamId
          in: path
          required: true
          schema:
            type: string
            description: The unique team identifier
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      responses:
        '200':
          description: Successfully removed a member of the team.
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
            Not authorized to update the team.
        '404':
          description: ''
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