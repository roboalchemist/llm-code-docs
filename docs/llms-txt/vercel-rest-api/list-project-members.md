# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projectmembers/list-project-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# List project members

> Lists all members of a project.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/members
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
  /v1/projects/{idOrName}/members:
    get:
      tags:
        - projectMembers
      summary: List project members
      description: Lists all members of a project.
      operationId: getProjectMembers
      parameters:
        - name: idOrName
          description: The ID or name of the Project.
          in: path
          required: true
          schema:
            type: string
            description: The ID or name of the Project.
            example: prj_pavWOn1iLObbXLRiwVvzmPrTWyTf
        - name: limit
          description: Limit how many project members should be returned
          in: query
          required: false
          schema:
            description: Limit how many project members should be returned
            example: 20
            type: integer
            minimum: 1
            maximum: 100
        - name: since
          description: Timestamp in milliseconds to only include members added since then.
          in: query
          required: false
          schema:
            description: >-
              Timestamp in milliseconds to only include members added since
              then.
            example: 1540095775951
            type: integer
        - name: until
          description: Timestamp in milliseconds to only include members added until then.
          in: query
          required: false
          schema:
            description: >-
              Timestamp in milliseconds to only include members added until
              then.
            example: 1540095775951
            type: integer
        - name: search
          description: Search project members by their name, username, and email.
          in: query
          required: false
          schema:
            description: Search project members by their name, username, and email.
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
          description: Paginated list of members for the project.
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                  - properties:
                      members:
                        items:
                          properties:
                            avatar:
                              type: string
                              description: ID of the file for the Avatar of this member.
                              example: 123a6c5209bc3778245d011443644c8d27dc2c50
                            email:
                              type: string
                              description: The email of this member.
                              example: jane.doe@example.com
                            role:
                              type: string
                              enum:
                                - ADMIN
                                - PROJECT_DEVELOPER
                                - PROJECT_VIEWER
                                - PROJECT_GUEST
                              description: Role of this user in the project.
                              example: ADMIN
                            computedProjectRole:
                              type: string
                              enum:
                                - ADMIN
                                - PROJECT_DEVELOPER
                                - PROJECT_VIEWER
                                - PROJECT_GUEST
                              description: Role of this user in the project.
                              example: ADMIN
                            uid:
                              type: string
                              description: The ID of this user.
                              example: zTuNVUXEAvvnNN3IaqinkyMw
                            username:
                              type: string
                              description: The unique username of this user.
                              example: jane-doe
                            name:
                              type: string
                              description: The name of this user.
                              example: Jane Doe
                            createdAt:
                              type: number
                              description: >-
                                Timestamp in milliseconds when this member was
                                added.
                              example: 1588720733602
                            teamRole:
                              type: string
                              enum:
                                - OWNER
                                - MEMBER
                                - DEVELOPER
                                - SECURITY
                                - BILLING
                                - VIEWER
                                - VIEWER_FOR_PLUS
                                - CONTRIBUTOR
                              description: The role of this user in the team.
                              example: CONTRIBUTOR
                          required:
                            - computedProjectRole
                            - createdAt
                            - email
                            - role
                            - teamRole
                            - uid
                            - username
                          type: object
                        type: array
                      pagination:
                        properties:
                          hasNext:
                            type: boolean
                            enum:
                              - false
                              - true
                          count:
                            type: number
                            description: Amount of items in the current page.
                            example: 20
                          next:
                            nullable: true
                            type: number
                            description: >-
                              Timestamp that must be used to request the next
                              page.
                            example: 1540095775951
                          prev:
                            nullable: true
                            type: number
                            description: >-
                              Timestamp that must be used to request the
                              previous page.
                            example: 1540095775951
                        required:
                          - count
                          - hasNext
                          - next
                          - prev
                        type: object
                    required:
                      - members
                      - pagination
                    type: object
                    description: Paginated list of members for the project.
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