# Source: https://docs.promptlayer.com/reference/list-workflows.md

# Get All Workflows / Agents

Get a list of all workflows/agents in the system.


## OpenAPI

````yaml GET /workflows
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /workflows:
    get:
      tags:
        - workflow
      summary: List Workflows
      operationId: listWorkflows
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: Your API key for authentication.
        - name: page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            default: 1
          description: Page number for pagination.
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 30
          description: Number of items per page.
      responses:
        '200':
          description: List of workflows retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  items:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          description: Unique identifier for the workflow
                        workspace_id:
                          type: integer
                          description: ID of the workspace this workflow belongs to
                        user_id:
                          type: integer
                          nullable: true
                          description: ID of the user who created this workflow
                        name:
                          type: string
                          description: Name of the workflow
                        is_deleted:
                          type: boolean
                          description: Whether the workflow is deleted
                        latest_version_number:
                          type: integer
                          nullable: true
                          description: The latest version number of the workflow
                        release_labels:
                          type: array
                          items:
                            type: string
                          description: >-
                            Array of release label names associated with the
                            workflow
                      required:
                        - id
                        - workspace_id
                        - name
                        - is_deleted
                        - release_labels
                  page:
                    type: integer
                    description: Current page number
                  per_page:
                    type: integer
                    description: Number of items per page
                  total:
                    type: integer
                    nullable: true
                    description: Total number of items
                  pages:
                    type: integer
                    description: Total number of pages
                  has_next:
                    type: boolean
                    description: Whether there is a next page
                  has_prev:
                    type: boolean
                    description: Whether there is a previous page
                  next_num:
                    type: integer
                    nullable: true
                    description: Next page number if available
                  prev_num:
                    type: integer
                    nullable: true
                    description: Previous page number if available
                required:
                  - items
                  - page
                  - per_page
                  - pages
                  - has_next
                  - has_prev
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  message:
                    type: string
                    example: Invalid pagination parameters
                required:
                  - success
                  - message
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  message:
                    type: string
                    example: Invalid API key
                required:
                  - success
                  - message

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt