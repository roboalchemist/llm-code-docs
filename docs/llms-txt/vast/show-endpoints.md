# Source: https://docs.vast.ai/api-reference/serverless/show-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show endpoints

> Retrieve a list of endpoint jobs for the authenticated user.

CLI Usage: `vastai show endpoints`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/endptjobs/
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
  /api/v0/endptjobs/:
    get:
      tags:
        - Serverless
      summary: show endpoints
      description: |-
        Retrieve a list of endpoint jobs for the authenticated user.

        CLI Usage: `vastai show endpoints`
      responses:
        '200':
          description: A list of endpoint jobs
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
                          example: 0
                        target_util:
                          type: number
                          example: 0.9
                        cold_mult:
                          type: number
                          example: 2.5
                        cold_workers:
                          type: integer
                          example: 5
                        max_workers:
                          type: integer
                          example: 20
                        endpoint_name:
                          type: string
                          example: vLLM-Qwen3-8B
                        api_key:
                          type: string
                          example: your_api_key_here
                        user_id:
                          type: integer
                          example: 456
                        created_at:
                          type: string
                          format: date-time
                          example: '2023-10-01T12:00:00Z'
                        endpoint_state:
                          type: string
                          example: active
        '400':
          description: Bad request
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
                    example: invalid_args
                  msg:
                    type: string
                    example: No endpoints for user found
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
                    example: API requests too frequent endpoint threshold=3.0
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````