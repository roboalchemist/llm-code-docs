# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/organizations/projects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Projects

> Return projects in organization that user is apart of



## OpenAPI

````yaml GET /api/v2/organizations/{organizationId}/workspaces
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
  /api/v2/organizations/{organizationId}/workspaces:
    get:
      tags:
        - Organizations
      description: Return projects in organization that user is apart of
      operationId: listOrgProjects
      parameters:
        - schema:
            type: string
          in: path
          name: organizationId
          required: true
          description: The ID of the organization to get projects from.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  workspaces:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                        slug:
                          type: string
                        organization:
                          type: string
                        environments:
                          type: array
                          items:
                            type: object
                            properties:
                              name:
                                type: string
                              slug:
                                type: string
                            required:
                              - name
                              - slug
                            additionalProperties: false
                      required:
                        - id
                        - name
                        - slug
                        - organization
                        - environments
                      additionalProperties: false
                required:
                  - workspaces
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