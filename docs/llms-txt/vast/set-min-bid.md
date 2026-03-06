# Source: https://docs.vast.ai/api-reference/machines/set-min-bid.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# set min-bid

> Sets the minimum bid price for a specified machine.

CLI Usage: `vastai set min-bid <machine_id> --price <price>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/machines/{machine_id}/minbid/
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
  /api/v0/machines/{machine_id}/minbid/:
    put:
      tags:
        - Machines
      summary: set min-bid
      description: |-
        Sets the minimum bid price for a specified machine.

        CLI Usage: `vastai set min-bid <machine_id> --price <price>`
      parameters:
        - name: machine_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the machine.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - price
              properties:
                price:
                  type: number
                  format: float
                  description: Minimum bid price for the machine.
                  example: 0.5
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
                  you_sent:
                    type: object
                    description: The original request JSON.
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '422':
          description: Unprocessable Entity
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
                    example: API requests too frequent endpoint threshold=1.5
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