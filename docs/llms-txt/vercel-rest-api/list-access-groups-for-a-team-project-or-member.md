# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/list-access-groups-for-a-team-project-or-member.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List access groups for a team, project or member

> List access groups



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups
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
  /v1/access-groups:
    get:
      tags:
        - access-groups
      summary: List access groups for a team, project or member
      description: List access groups
      operationId: listAccessGroups
      parameters:
        - name: projectId
          description: Filter access groups by project.
          in: query
          schema:
            description: Filter access groups by project.
            example: prj_pavWOn1iLObbx3RowVvzmPrTWyTf
            type: string
        - name: search
          description: Search for access groups by name.
          in: query
          schema:
            description: Search for access groups by name.
            example: example
            type: string
        - name: membersLimit
          description: Number of members to include in the response.
          in: query
          schema:
            description: Number of members to include in the response.
            example: 20
            type: integer
            minimum: 1
            maximum: 100
        - name: projectsLimit
          description: Number of projects to include in the response.
          in: query
          schema:
            description: Number of projects to include in the response.
            example: 20
            type: integer
            minimum: 1
            maximum: 100
        - name: limit
          description: Limit how many access group should be returned.
          in: query
          schema:
            description: Limit how many access group should be returned.
            example: 20
            type: integer
            minimum: 1
            maximum: 100
        - name: next
          description: Continuation cursor to retrieve the next page of results.
          in: query
          schema:
            description: Continuation cursor to retrieve the next page of results.
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                  - properties:
                      accessGroups:
                        items:
                          properties:
                            members:
                              items:
                                type: string
                              type: array
                            projects:
                              items:
                                type: string
                              type: array
                            entitlements:
                              items:
                                type: string
                              type: array
                            teamPermissions:
                              items:
                                type: string
                              type: array
                            isDsyncManaged:
                              type: boolean
                              enum:
                                - false
                                - true
                            name:
                              type: string
                              description: The name of this access group.
                              example: my-access-group
                            createdAt:
                              type: string
                              description: >-
                                Timestamp in milliseconds when the access group
                                was created.
                              example: 1588720733602
                            teamId:
                              type: string
                              description: >-
                                ID of the team that this access group belongs
                                to.
                              example: team_123a6c5209bc3778245d011443644c8d27dc2c50
                            updatedAt:
                              type: string
                              description: >-
                                Timestamp in milliseconds when the access group
                                was last updated.
                              example: 1588720733602
                            accessGroupId:
                              type: string
                              description: ID of the access group.
                              example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
                            membersCount:
                              type: number
                              description: Number of members in the access group.
                              example: 5
                            projectsCount:
                              type: number
                              description: Number of projects in the access group.
                              example: 2
                            teamRoles:
                              items:
                                type: string
                              type: array
                              description: Roles that the team has in the access group.
                              example:
                                - DEVELOPER
                                - BILLING
                          required:
                            - accessGroupId
                            - createdAt
                            - isDsyncManaged
                            - membersCount
                            - name
                            - projectsCount
                            - teamId
                            - updatedAt
                          type: object
                        type: array
                      pagination:
                        properties:
                          count:
                            type: number
                          next:
                            nullable: true
                            type: string
                        required:
                          - count
                          - next
                        type: object
                    required:
                      - accessGroups
                      - pagination
                    type: object
        '400':
          description: One of the provided values in the request query is invalid.
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