# Source: https://docs.vast.ai/api-reference/billing/show-deposit.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show deposit

> Retrieves the deposit details for a specified instance.

CLI Usage: `vastai show deposit <id>`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/instances/balance/{id}/
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
  /api/v0/instances/balance/{id}/:
    get:
      tags:
        - Billing
      summary: show deposit
      description: |-
        Retrieves the deposit details for a specified instance.

        CLI Usage: `vastai show deposit <id>`
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the instance.
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
                  refundable_deposit:
                    type: number
                    description: The refundable deposit amount.
                    example: 100
                  total_discount:
                    type: number
                    description: The total discount applied.
                    example: 10
                  discount_months:
                    type: integer
                    description: The number of months the discount applies.
                    example: 3
        '404':
          description: Instance Not Found
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