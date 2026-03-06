# Source: https://docs.vast.ai/api-reference/serverless/show-workergroup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show workergroup

> Retrieves the list of workergroups associated with the authenticated user.

CLI Usage: `vastai show workergroups`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/workergroups/
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
  /api/v0/workergroups/:
    get:
      tags:
        - Serverless
      summary: show workergroup
      description: >-
        Retrieves the list of workergroups associated with the authenticated
        user.


        CLI Usage: `vastai show workergroups`
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 123
                        min_load:
                          type: number
                          example: 1
                        target_util:
                          type: number
                          example: 0.9
                        cold_mult:
                          type: number
                          example: 3
                        test_workers:
                          type: integer
                          example: 3
                        template_hash:
                          type: string
                          example: abc123def456
                        template_id:
                          type: integer
                          example: 456
                        search_query:
                          type: object
                          description: Parsed search parameters as JSON object
                          example: verified=true rentable=true rented=false
                        launch_args:
                          type: string
                          example: '--env VAR=value'
                        gpu_ram:
                          type: number
                          example: 24
                        endpoint_name:
                          type: string
                          example: my_endpoint
                        endpoint_id:
                          type: integer
                          example: 789
                        api_key:
                          type: string
                          example: your_api_key_here
                        created_at:
                          type: string
                          format: date-time
                          example: '2023-10-01T12:00:00Z'
                        user_id:
                          type: integer
                          example: 456
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
                  error:
                    type: string
                  msg:
                    type: string
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
                  error:
                    type: string
                  msg:
                    type: string
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=2.0
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````