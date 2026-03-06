# Source: https://docs.vast.ai/api-reference/serverless/update-workergroup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# update workergroup

> Updates the properties of an existing workergroup based on the provided parameters.

CLI Usage: `vastai update workergroup <id> [options]`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/workergroups/{id}/
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
  /api/v0/workergroups/{id}/:
    put:
      tags:
        - Serverless
      summary: update workergroup
      description: >-
        Updates the properties of an existing workergroup based on the provided
        parameters.


        CLI Usage: `vastai update workergroup <id> [options]`
      parameters:
        - name: id
          in: path
          required: true
          description: The ID of the workergroup to update.
          schema:
            type: integer
            example: 4242
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                min_load:
                  type: number
                  description: Minimum load for the workergroup.
                  example: 1
                target_util:
                  type: number
                  description: Target utilization for the workergroup.
                  example: 0.9
                cold_mult:
                  type: number
                  description: Cold multiplier for the workergroup.
                  example: 3
                test_workers:
                  type: integer
                  description: Number of test workers for performance estimation.
                  default: 3
                  example: 3
                template_hash:
                  type: string
                  description: Template hash for the workergroup.
                  example: abc123def456
                template_id:
                  type: integer
                  description: Template ID for the workergroup.
                  example: 456
                search_params:
                  type: string
                  description: Search parameters for offers (JSON object or query string).
                  default: verified=true rentable=true rented=false
                  example: gpu_name=RTX_3090 rentable=true
                launch_args:
                  type: string
                  description: Launch arguments for creating instances.
                  example: '--env VAR=value'
                gpu_ram:
                  type: number
                  description: Estimated GPU RAM requirement.
                  example: 24
                endpoint_name:
                  type: string
                  description: Deployment endpoint name.
                  example: vLLM-Qwen3-8B
                endpoint_id:
                  type: integer
                  description: Deployment endpoint ID.
                  example: 123
      responses:
        '200':
          description: Successfully updated the workergroup.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
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
                    example: invalid_args
                  msg:
                    type: string
                    example: Workgroup not found for user
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