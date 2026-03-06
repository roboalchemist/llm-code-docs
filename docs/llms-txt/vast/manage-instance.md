# Source: https://docs.vast.ai/api-reference/instances/manage-instance.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# manage instance

> Manage instance state and labels. The operation is determined by the request body parameters.

CLI Usage:
- To stop: `vastai stop instance <id>`
- To start: `vastai start instance <id>`
- To label: `vastai label instance <id> <label>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/instances/{id}/
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
    put:
      tags:
        - Instances
      summary: manage instance
      description: >-
        Manage instance state and labels. The operation is determined by the
        request body parameters.


        CLI Usage:

        - To stop: `vastai stop instance <id>`

        - To start: `vastai start instance <id>`

        - To label: `vastai label instance <id> <label>`
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the instance to modify
          example: 1234
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: At least one of these parameters should be provided
              properties:
                state:
                  type: string
                  description: Change instance state (optional)
                  enum:
                    - stopped
                    - running
                  example: stopped
                label:
                  type: string
                  description: Text label to assign to the instance (optional)
                  maxLength: 1024
                  example: My ML Training Job
      responses:
        '200':
          description: Operation completed successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SimpleBooleanSuccessResponse'
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
        '404':
          description: Not Found
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
                    example: API requests too frequent endpoint threshold=1.0
      security:
        - BearerAuth: []
components:
  schemas:
    SimpleBooleanSuccessResponse:
      type: object
      properties:
        success:
          type: boolean
          example: true
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