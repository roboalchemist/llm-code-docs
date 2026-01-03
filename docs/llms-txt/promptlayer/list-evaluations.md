# Source: https://docs.promptlayer.com/reference/list-evaluations.md

# List Evaluations

Retrieve a paginated list of evaluations in your workspace.

### Authentication

This endpoint requires JWT or API key authentication.

### Filtering by Name

Use the `name` parameter to search for evaluations by name. The search is case-insensitive and matches partial names. This is useful for discovering existing evaluations programmatically.

### Filtering by Status

Use the `status` parameter to control which evaluations are returned based on their deletion status:

* `active` (default): Returns only active evaluations
* `deleted`: Returns only deleted/archived evaluations
* `all`: Returns both active and deleted evaluations


## OpenAPI

````yaml GET /api/public/v2/evaluations
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /api/public/v2/evaluations:
    get:
      tags:
        - evaluations
      summary: List Evaluations
      operationId: listEvaluations
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: >-
            API key or JWT token for authentication. Use 'X-API-KEY' header for
            API key or 'Authorization: Bearer' header for JWT.
        - name: workspace_id
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
          description: >-
            Filter by specific workspace ID. If not provided, uses the current
            user's workspace
        - name: name
          in: query
          required: false
          schema:
            type: string
          description: Filter evaluations by name (case-insensitive partial match)
        - name: status
          in: query
          required: false
          schema:
            type: string
            enum:
              - active
              - deleted
              - all
            default: active
          description: >-
            Filter evaluations by status: 'active' (default) returns only active
            evaluations, 'deleted' returns only deleted/archived evaluations,
            'all' returns both
        - name: page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            default: 1
          description: Page number for pagination
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 10
          description: Number of items per page
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                  evaluations:
                    type: array
                    items:
                      $ref: '#/components/schemas/Evaluation'
                  page:
                    type: integer
                  per_page:
                    type: integer
                  total:
                    type: integer
                  pages:
                    type: integer
                required:
                  - success
                  - message
                  - evaluations
                  - page
                  - per_page
                  - total
                  - pages
        '400':
          description: Invalid workspace_id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Evaluation:
      type: object
      properties:
        id:
          type: integer
          description: Unique identifier for the evaluation
        name:
          type: string
          description: Name of the evaluation
        comment:
          type: string
          nullable: true
          description: Optional comment or description for the evaluation
        created_at:
          type: string
          format: date-time
          description: Timestamp when the evaluation was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the evaluation was last updated
        workspace_id:
          type: integer
          description: ID of the workspace this evaluation belongs to
        folder_id:
          type: integer
          nullable: true
          description: ID of the folder containing this evaluation
        user_id:
          type: integer
          nullable: true
          description: ID of the user who created this evaluation
      required:
        - id
        - name
        - workspace_id
    ErrorResponse:
      type: object
      properties:
        success:
          type: boolean
          default: false
          description: Indicates that the request failed.
        error:
          type: string
          description: Error message explaining why the request failed.
      required:
        - success
        - error
      description: Error response format.

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt