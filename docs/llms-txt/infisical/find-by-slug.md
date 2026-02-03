# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v2/find-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v1/find-by-slug.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Find By Slug

> Retrieve details of a specific privilege by privilege slug.



## OpenAPI

````yaml GET /api/v1/additional-privilege/identity/{privilegeSlug}
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
  /api/v1/additional-privilege/identity/{privilegeSlug}:
    get:
      tags:
        - Identity Specific Privileges
      description: Retrieve details of a specific privilege by privilege slug.
      parameters:
        - schema:
            type: string
            minLength: 1
          in: query
          name: identityId
          required: true
          description: The ID of the machine identity to list.
        - schema:
            type: string
            minLength: 1
          in: query
          name: projectSlug
          required: true
          description: The slug of the project of the identity in.
        - schema:
            type: string
            minLength: 1
          in: path
          name: privilegeSlug
          required: true
          description: The slug of the privilege.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  privilege:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      slug:
                        type: string
                      projectMembershipId:
                        type: string
                        format: uuid
                      isTemporary:
                        type: boolean
                        default: false
                      temporaryMode:
                        type: string
                        nullable: true
                      temporaryRange:
                        type: string
                        nullable: true
                      temporaryAccessStartTime:
                        type: string
                        format: date-time
                        nullable: true
                      temporaryAccessEndTime:
                        type: string
                        format: date-time
                        nullable: true
                      permissions:
                        type: array
                        items:
                          type: object
                          properties:
                            subject:
                              anyOf:
                                - type: string
                                  minLength: 1
                                - type: array
                                  items:
                                    type: string
                            action:
                              anyOf:
                                - type: string
                                  minLength: 1
                                - type: array
                                  items:
                                    type: string
                            conditions: {}
                            inverted:
                              type: boolean
                          required:
                            - action
                          additionalProperties: false
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                    required:
                      - id
                      - slug
                      - projectMembershipId
                      - permissions
                      - createdAt
                      - updatedAt
                    additionalProperties: false
                required:
                  - privilege
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
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````