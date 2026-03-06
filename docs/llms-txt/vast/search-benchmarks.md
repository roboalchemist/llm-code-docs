# Source: https://docs.vast.ai/api-reference/search/search-benchmarks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# search benchmarks

> Retrieve benchmark data based on search parameters.

CLI Usage: `vastai search benchmarks`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/benchmarks/
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
  /api/v0/benchmarks/:
    get:
      tags:
        - Search
      summary: search benchmarks
      description: |-
        Retrieve benchmark data based on search parameters.

        CLI Usage: `vastai search benchmarks`
      parameters:
        - name: query
          in: query
          required: false
          schema:
            type: string
          description: Search query string to filter benchmarks.
          example: score>1000
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    contract_id:
                      type: integer
                      description: ID of instance/contract reporting benchmark
                    id:
                      type: integer
                      description: Benchmark unique ID
                    image:
                      type: string
                      description: Image used for benchmark
                    last_update:
                      type: number
                      format: float
                      description: Date of benchmark
                    machine_id:
                      type: integer
                      description: ID of machine benchmarked
                    model:
                      type: string
                      description: Name of model used in benchmark
                    name:
                      type: string
                      description: Name of benchmark
                    num_gpus:
                      type: integer
                      description: Number of GPUs used in benchmark
                    score:
                      type: number
                      format: float
                      description: Benchmark score result
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