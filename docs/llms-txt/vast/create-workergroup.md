# Source: https://docs.vast.ai/api-reference/serverless/create-workergroup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create workergroup

> Creates a new workergroup configuration that manages worker instances for a serverless endpoint.

CLI Usage: `vastai create workergroup --template_hash <hash> --endpoint_name <name> [options]`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/workergroups/
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
    post:
      tags:
        - Serverless
      summary: create workergroup
      description: >-
        Creates a new workergroup configuration that manages worker instances
        for a serverless endpoint.


        CLI Usage: `vastai create workergroup --template_hash <hash>
        --endpoint_name <name> [options]`
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                endpoint_name:
                  type: string
                  description: Name of the endpoint group
                  example: vLLM-Qwen3-8B
                endpoint_id:
                  type: integer
                  description: ID of existing endpoint group (alternative to endpoint_name)
                  example: 123
                template_hash:
                  type: string
                  description: Hash ID of template to use for worker instances
                  example: abc123def456
                template_id:
                  type: integer
                  description: ID of template (alternative to template_hash)
                  example: 456
                search_params:
                  type: string
                  description: >-
                    Search query for finding worker instances (alternative to
                    template)
                  default: verified=true rentable=true rented=false
                  example: gpu_name=RTX_3090 rentable=true
                launch_args:
                  type: string
                  description: Additional launch arguments for worker instances
                  example: '--env VAR=value'
                min_load:
                  type: number
                  description: Minimum load threshold for scaling
                  default: 1
                  example: 1
                target_util:
                  type: number
                  description: Target GPU utilization
                  default: 0.9
                  example: 0.9
                cold_mult:
                  type: number
                  description: Cold start multiplier
                  default: 3
                  example: 3
                cold_workers:
                  type: integer
                  description: Number of cold workers to maintain
                  default: 3
                  example: 3
                max_workers:
                  type: integer
                  description: Maximum number of worker instances
                  default: 20
                  example: 20
                test_workers:
                  type: integer
                  description: Number of test workers
                  default: 3
                  example: 3
                gpu_ram:
                  type: integer
                  description: Minimum GPU RAM in GB
                  default: 24
                  example: 24
      responses:
        '200':
          description: Successfully created workergroup
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  id:
                    type: integer
                    description: ID of created autoscaling job
                    example: 789
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
                    enum:
                      - invalid_args
                  msg:
                    type: string
                    example: >-
                      Please assign your workergroup to a valid endpoint
                      identifier
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
                    example: API requests too frequent endpoint threshold=4.0
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