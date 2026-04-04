# Source: https://infisical.com/docs/api-reference/endpoints/groups/list-group-members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Group Members



## OpenAPI

````yaml GET /api/v1/groups/{id}/members
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
  /api/v1/groups/{id}/members:
    get:
      tags:
        - Groups
      operationId: listGroupMembers
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
            10th member.
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 10
          in: query
          name: limit
          required: false
          description: The number of members to return.
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: >-
            The text string that member email(in case of users) or name(in case
            of machine identities) will be filtered by.
        - schema:
            type: string
            enum:
              - name
            default: name
          in: query
          name: orderBy
          required: false
          description: The column to order members by.
        - schema:
            type: string
            enum:
              - asc
              - desc
          in: query
          name: orderDirection
          required: false
          description: The direction to order members in.
        - schema:
            anyOf:
              - type: string
                enum:
                  - users
                  - machineIdentities
              - type: array
                items:
                  type: string
                  enum:
                    - users
                    - machineIdentities
          in: query
          name: memberTypeFilter
          required: false
          description: >-
            Filter members by type. Can be a single value ('users' or
            'machineIdentities') or an array of values. If not specified, both
            users and machine identities will be returned.
        - schema:
            type: string
          in: path
          name: id
          required: true
          description: The ID of the group to list members for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  members:
                    type: array
                    items:
                      anyOf:
                        - type: object
                          properties:
                            id:
                              type: string
                            joinedGroupAt:
                              type: string
                              format: date-time
                              nullable: true
                            type:
                              type: string
                              enum:
                                - user
                            user:
                              type: object
                              properties:
                                id:
                                  type: string
                                  format: uuid
                                firstName:
                                  type: string
                                  nullable: true
                                lastName:
                                  type: string
                                  nullable: true
                                email:
                                  type: string
                                  nullable: true
                                username:
                                  type: string
                              required:
                                - id
                                - username
                              additionalProperties: false
                          required:
                            - id
                            - joinedGroupAt
                            - type
                            - user
                          additionalProperties: false
                        - type: object
                          properties:
                            id:
                              type: string
                            joinedGroupAt:
                              type: string
                              format: date-time
                              nullable: true
                            type:
                              type: string
                              enum:
                                - machineIdentity
                            machineIdentity:
                              type: object
                              properties:
                                id:
                                  type: string
                                  format: uuid
                                name:
                                  type: string
                              required:
                                - id
                                - name
                              additionalProperties: false
                          required:
                            - id
                            - joinedGroupAt
                            - type
                            - machineIdentity
                          additionalProperties: false
                  totalCount:
                    type: number
                required:
                  - members
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