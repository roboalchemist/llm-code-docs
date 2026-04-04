# Source: https://docs.vast.ai/api-reference/serverless/create-endpoint.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# create endpoint

> This endpoint creates a new job processing endpoint with specified parameters.

CLI Usage: `vastai create endpoint [options]`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/endptjobs/
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
    post:
      tags:
        - Serverless
      summary: create endpoint
      description: >-
        This endpoint creates a new job processing endpoint with specified
        parameters.


        CLI Usage: `vastai create endpoint [options]`
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                min_load:
                  type: number
                  description: Minimum load for the endpoint.
                  default: 10
                  example: 50
                target_util:
                  type: number
                  description: Target utilization for the endpoint.
                  default: 0.9
                  example: 0.75
                cold_mult:
                  type: number
                  description: Multiplier for cold start.
                  default: 2.5
                  example: 2
                cold_workers:
                  type: integer
                  description: Number of cold workers.
                  default: 5
                  example: 5
                max_workers:
                  type: integer
                  description: Maximum number of workers.
                  default: 20
                  example: 20
                endpoint_name:
                  type: string
                  description: Name of the endpoint.
                  default: default-endpoint
                  example: my_endpoint
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
                  result:
                    type: integer
                    description: The ID of the created endpoint
                    example: 12345
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/Error'
                    properties:
                      error:
                        type: string
                        enum:
                          - invalid_args
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden
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