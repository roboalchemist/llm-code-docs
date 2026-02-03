# Source: https://infisical.com/docs/api-reference/endpoints/groups/list-group-machine-identities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Group Machine Identities



## OpenAPI

````yaml GET /api/v1/groups/{id}/machine-identities
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
  /api/v1/groups/{id}/machine-identities:
    get:
      tags:
        - Groups
      operationId: listGroupMachineIdentities
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
            10th identity.
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 10
          in: query
          name: limit
          required: false
          description: The number of identities to return.
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: The text string that machine identity name will be filtered by.
        - schema:
            type: string
            enum:
              - assignedMachineIdentities
              - nonAssignedMachineIdentities
          in: query
          name: filter
          required: false
          description: >-
            Whether to filter the list of returned identities.
            'assignedMachineIdentities' will only return identities assigned to
            the group, 'nonAssignedMachineIdentities' will only return
            identities not assigned to the group, undefined will return all
            identities in the organization.
        - schema:
            type: string
          in: path
          name: id
          required: true
          description: The ID of the group to list identities for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  machineIdentities:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        name:
                          type: string
                        isPartOfGroup:
                          type: boolean
                        joinedGroupAt:
                          type: string
                          format: date-time
                          nullable: true
                      required:
                        - id
                        - name
                        - isPartOfGroup
                        - joinedGroupAt
                      additionalProperties: false
                  totalCount:
                    type: number
                required:
                  - machineIdentities
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