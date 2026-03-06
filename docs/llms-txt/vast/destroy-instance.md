# Source: https://docs.vast.ai/api-reference/instances/destroy-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# destroy instance

> Destroys/deletes an instance permanently. This is irreversible and will delete all data.

CLI Usage: `vastai destroy instance <id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/instances/{id}/
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
  /api/v0/instances/{id}/:
    delete:
      tags:
        - Instances
      summary: destroy instance
      description: >-
        Destroys/deletes an instance permanently. This is irreversible and will
        delete all data.


        CLI Usage: `vastai destroy instance <id>`
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: integer
          description: ID of the instance to destroy
          example: 4242
      responses:
        '200':
          description: Instance destroyed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                    description: Whether the destruction was successful
                  msg:
                    type: string
                    description: Optional status message
                    example: Instance destroyed successfully
        '400':
          description: Bad request - invalid instance ID
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
                    example: invalid instance_id
        '404':
          description: Instance not found
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
                    example: not_found
                  msg:
                    type: string
                    example: Instance not found
        '429':
          description: Too many requests
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
                    example: rate_limit_exceeded
                  msg:
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