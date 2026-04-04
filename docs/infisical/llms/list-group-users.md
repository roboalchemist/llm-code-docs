# Source: https://infisical.com/docs/api-reference/endpoints/groups/list-group-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Group Users



## OpenAPI

````yaml GET /api/v1/groups/{id}/users
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/groups/{id}/users:
    get:
      tags:
        - Groups
      operationId: listGroupUsers
      parameters:
        - schema:
            type: number
            minimum: 0
            default: 0
          in: query
          name: offset
          required: false
          description: >-
            The offset to start from. If you enter 10, it will start from the
            10th user.
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 10
          in: query
          name: limit
          required: false
          description: The number of users to return.
        - schema:
            type: string
          in: query
          name: username
          required: false
          description: The username to search for.
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: The text string that user email or name will be filtered by.
        - schema:
            type: string
            enum:
              - existingMembers
              - nonMembers
          in: query
          name: filter
          required: false
          description: >-
            Whether to filter the list of returned users. 'existingMembers' will
            only return existing users in the group, 'nonMembers' will only
            return users not in the group, undefined will return all users in
            the organization.
        - schema:
            type: string
          in: path
          name: id
          required: true
          description: The ID of the group to list users for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  users:
                    type: array
                    items:
                      type: object
                      properties:
                        email:
                          type: string
                          nullable: true
                        username:
                          type: string
                        firstName:
                          type: string
                          nullable: true
                        lastName:
                          type: string
                          nullable: true
                        id:
                          type: string
                          format: uuid
                        isPartOfGroup:
                          type: boolean
                        joinedGroupAt:
                          type: string
                          format: date-time
                          nullable: true
                      required:
                        - username
                        - id
                        - isPartOfGroup
                        - joinedGroupAt
                      additionalProperties: false
                  totalCount:
                    type: number
                required:
                  - users
                  - totalCount
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false

````