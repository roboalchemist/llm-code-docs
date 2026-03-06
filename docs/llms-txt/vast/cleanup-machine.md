# Source: https://docs.vast.ai/api-reference/machines/cleanup-machine.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# cleanup machine

> This endpoint removes expired contracts on a specified machine, freeing up space.

CLI Usage: `vastai cleanup machine <machine_id>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/machines/{machine_id}/cleanup/
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
  /api/v0/machines/{machine_id}/cleanup/:
    put:
      tags:
        - Machines
      summary: cleanup machine
      description: >-
        This endpoint removes expired contracts on a specified machine, freeing
        up space.


        CLI Usage: `vastai cleanup machine <machine_id>`
      parameters:
        - name: machine_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the machine to clean up.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: An empty JSON object is expected.
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
                  ctime:
                    type: number
                    format: float
                    example: 1633036800
                  machine_id:
                    type: integer
                    example: 123
                  user_id:
                    type: integer
                    example: 456
                  num_deleted:
                    type: integer
                    example: 5
                  msg:
                    type: string
                    example: deleted 5 expired contracts on machine 123
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
                    example: API requests too frequent endpoint threshold=8
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