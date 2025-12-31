# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/update-team-directory-sync-role-mappings.md

# Update Team Directory Sync Role Mappings

> Update the Directory Sync role mappings for a Team. This endpoint allows updating the mapping between directory groups and team roles or access groups.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/dsync-roles
openapi: 3.0.3
info:
  title: Vercel SDK
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
  /v1/teams/{teamId}/dsync-roles:
    post:
      tags:
        - teams
      summary: Update Team Directory Sync Role Mappings
      description: >-
        Update the Directory Sync role mappings for a Team. This endpoint allows
        updating the mapping between directory groups and team roles or access
        groups.
      operationId: postTeamDsyncRoles
      parameters:
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
              required:
                - roles
              properties:
                roles:
                  type: object
                  description: Directory groups to role or access group mappings.
                  additionalProperties:
                    anyOf:
                      - type: string
                        enum:
                          - OWNER
                          - MEMBER
                          - DEVELOPER
                          - SECURITY
                          - BILLING
                          - VIEWER
                          - VIEWER_FOR_PLUS
                          - CONTRIBUTOR
                      - type: object
                        additionalProperties: false
                        required:
                          - accessGroupId
                        properties:
                          accessGroupId:
                            type: string
                            pattern: ^ag_[A-z0-9_ -]+$
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  ok:
                    type: boolean
                required:
                  - ok
                type: object
        '400':
          description: One of the provided values in the request body is invalid.
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt