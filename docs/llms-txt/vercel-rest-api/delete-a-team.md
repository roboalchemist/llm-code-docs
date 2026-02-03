# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/delete-a-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Team

> Delete a team under your account. You need to send a `DELETE` request with the desired team `id`. An optional array of reasons for deletion may also be sent.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}
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
  /v1/teams/{teamId}:
    delete:
      tags:
        - teams
      summary: Delete a Team
      description: >-
        Delete a team under your account. You need to send a `DELETE` request
        with the desired team `id`. An optional array of reasons for deletion
        may also be sent.
      operationId: deleteTeam
      parameters:
        - name: newDefaultTeamId
          description: Id of the team to be set as the new default team
          in: query
          required: false
          schema:
            type: string
            description: Id of the team to be set as the new default team
            example: team_LLHUOMOoDlqOp8wPE4kFo9pE
        - description: The Team identifier to perform the request on behalf of.
          in: path
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
          required: true
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
              additionalProperties: false
              properties:
                reasons:
                  type: array
                  description: >-
                    Optional array of objects that describe the reason why the
                    team is being deleted.
                  items:
                    type: object
                    description: >-
                      An object describing the reason why the team is being
                      deleted.
                    required:
                      - slug
                      - description
                    additionalProperties: false
                    properties:
                      slug:
                        type: string
                        description: >-
                          Idenitifier slug of the reason why the team is being
                          deleted.
                      description:
                        type: string
                        description: >-
                          Description of the reason why the team is being
                          deleted.
        required: true
      responses:
        '200':
          description: The Team was successfully deleted
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                    description: The ID of the deleted Team
                    example: team_LLHUOMOoDlqOp8wPE4kFo9pE
                  newDefaultTeamIdError:
                    type: boolean
                    enum:
                      - false
                      - true
                    description: >-
                      Signifies whether the default team update has failed, when
                      newDefaultTeamId is provided in request query.
                    example: true
                required:
                  - id
                type: object
                description: The Team was successfully deleted
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: ''
        '403':
          description: |-
            You do not have permission to access this resource.
            The authenticated user can't access the team
        '409':
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