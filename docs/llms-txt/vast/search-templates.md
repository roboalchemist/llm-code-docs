# Source: https://docs.vast.ai/api-reference/search/search-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# search templates

> Searches for templates using filter-based queries.

Use `select_filters` to search by specific field conditions. Results include both your own templates and publicly shared templates.

**Available filter fields:** `creator_id`, `created_at`, `count_created`, `default_tag`, `docker_login_repo`, `id`, `image`, `jup_direct`, `hash_id`, `name`, `recent_create_date`, `recommended_disk_space`, `recommended`, `ssh_direct`, `tag`, `use_ssh`

**Operators:** `eq`, `neq`, `lt`, `lte`, `gt`, `gte`, `in`, `notin`

For detailed usage, see [Creating and Using Templates with API](/api-reference/creating-and-using-templates-with-api).

CLI Usage: `vastai search templates`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/template/
openapi: 3.1.0
info:
  title: Vast.ai API
  description: >-
    Welcome to Vast.ai 's API documentation. Our API allows you to
    programmatically manage GPU instances, handle machine operations, and
    automate your AI/ML workflow. Whether you're running individual GPU
    instances or managing a fleet of machines, our API provides comprehensive
    control over all Vast.ai  platform features.
  version: 1.0.0
  contact:
    name: Vast.ai Support
    url: https://discord.gg/vast
servers:
  - url: https://console.vast.ai
    description: Production server
security:
  - BearerAuth: []
paths:
  /api/v0/template/:
    get:
      tags:
        - Search
      summary: search templates
      description: >-
        Searches for templates using filter-based queries.


        Use `select_filters` to search by specific field conditions. Results
        include both your own templates and publicly shared templates.


        **Available filter fields:** `creator_id`, `created_at`,
        `count_created`, `default_tag`, `docker_login_repo`, `id`, `image`,
        `jup_direct`, `hash_id`, `name`, `recent_create_date`,
        `recommended_disk_space`, `recommended`, `ssh_direct`, `tag`, `use_ssh`


        **Operators:** `eq`, `neq`, `lt`, `lte`, `gt`, `gte`, `in`, `notin`


        For detailed usage, see [Creating and Using Templates with
        API](/api-reference/creating-and-using-templates-with-api).


        CLI Usage: `vastai search templates`
      parameters:
        - name: select_filters
          in: query
          required: false
          schema:
            type: string
          description: >
            JSON-encoded filter object. Format: `{"field": {"op": value}}`.
            Example: `{"use_ssh": {"eq": true}, "recommended": {"eq": true}}` or
            `{"count_created": {"gt": 100}}`
        - name: select_cols
          in: query
          required: false
          schema:
            type: string
          description: >
            JSON-encoded array of columns to return. Example: `["*"]` for all
            columns or `["id", "name", "hash_id"]` for specific columns.
        - name: order_by
          in: query
          required: false
          schema:
            type: string
          description: Column to order the results by.
      responses:
        '200':
          description: Successfully retrieved templates
          content:
            application/json:
              schema:
                type: object
                required:
                  - success
                  - templates_found
                  - templates
                properties:
                  success:
                    type: boolean
                    example: true
                  templates_found:
                    type: integer
                    description: Number of templates found.
                    example: 5
                  templates:
                    type: array
                    description: List of templates matching the search criteria.
                    items:
                      $ref: '#/components/schemas/Template'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=3.0
      security:
        - BearerAuth: []
components:
  schemas:
    Template:
      type: object
      properties:
        id:
          type: integer
          description: Template ID
        name:
          type: string
          description: Template name
        image:
          type: string
          description: Docker image name
    Error:
      type: object
      properties:
        success:
          type: boolean
          example: false
        error:
          type: string
        msg:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````