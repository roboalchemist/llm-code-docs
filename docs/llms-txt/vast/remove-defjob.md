# Source: https://docs.vast.ai/api-reference/machines/remove-defjob.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# remove defjob

> Deletes the default job (background instances) for a specified machine.

CLI Usage: `vastai remove defjob <machine_id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/machines/{machine_id}/defjob/
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
  /api/v0/machines/{machine_id}/defjob/:
    delete:
      tags:
        - Machines
      summary: remove defjob
      description: |-
        Deletes the default job (background instances) for a specified machine.

        CLI Usage: `vastai remove defjob <machine_id>`
      parameters:
        - name: machine_id
          in: path
          required: true
          description: ID of the machine to remove the default job from.
          schema:
            type: integer
            example: 12345
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
                  machine_id:
                    type: integer
                    example: 12345
                  user_id:
                    type: integer
                    example: 67890
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
                    example: API requests too frequent endpoint threshold=1.2
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