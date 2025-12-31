# Source: https://infisical.com/docs/api-reference/endpoints/groups/list-group-projects.md

# List Group Projects



## OpenAPI

````yaml GET /api/v1/groups/{id}/projects
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
  /api/v1/groups/{id}/projects:
    get:
      tags:
        - Groups
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
            10th project.
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 10
          in: query
          name: limit
          required: false
          description: The number of projects to return.
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: The text string that project name or slug will be filtered by.
        - schema:
            type: string
            enum:
              - assignedProjects
              - unassignedProjects
          in: query
          name: filter
          required: false
          description: >-
            Whether to filter the list of returned projects. 'assignedProjects'
            will only return projects assigned to the group,
            'unassignedProjects' will only return projects not assigned to the
            group, undefined will return all projects in the organization.
        - schema:
            type: string
            enum:
              - name
            default: name
          in: query
          name: orderBy
          required: false
          description: The column to order projects by.
        - schema:
            type: string
            enum:
              - asc
              - desc
            default: asc
          in: query
          name: orderDirection
          required: false
          description: The direction to order projects in.
        - schema:
            type: string
          in: path
          name: id
          required: true
          description: The ID of the group to list projects for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  projects:
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
                        description:
                          type: string
                          nullable: true
                        type:
                          type: string
                        joinedGroupAt:
                          type: string
                          format: date-time
                          nullable: true
                      required:
                        - id
                        - name
                        - slug
                        - type
                        - joinedGroupAt
                      additionalProperties: false
                  totalCount:
                    type: number
                required:
                  - projects
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://infisical.com/docs/llms.txt