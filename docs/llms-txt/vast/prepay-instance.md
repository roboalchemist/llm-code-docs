# Source: https://docs.vast.ai/api-reference/instances/prepay-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# prepay instance

> Deposit credits into a reserved instance to receive usage discounts.
The discount rate is calculated based on how many months of usage the prepaid amount covers. Maximum discount is typically 40%.

CLI Usage: `vastai prepay instance <id> <amount>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/instances/prepay/{id}/
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
  /api/v0/instances/prepay/{id}/:
    put:
      tags:
        - Instances
      summary: prepay instance
      description: >-
        Deposit credits into a reserved instance to receive usage discounts.

        The discount rate is calculated based on how many months of usage the
        prepaid amount covers. Maximum discount is typically 40%.


        CLI Usage: `vastai prepay instance <id> <amount>`
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: integer
          description: ID of the instance to prepay for
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - amount
              properties:
                amount:
                  type: number
                  format: float
                  description: Amount of credits to prepay
                  example: 500
      responses:
        '200':
          description: Successfully applied prepayment
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  timescale:
                    type: number
                    format: float
                    description: Number of months the prepayment will cover
                    example: 3.5
                  discount_rate:
                    type: number
                    format: float
                    description: Applied discount rate (0.0-0.4)
                    example: 0.3
        '400':
          description: Invalid instance ID
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  msg:
                    type: string
                    example: No such instance
        '411':
          description: Insufficient credit balance
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                  msg:
                    type: string
                    example: Insufficient credit
        '429':
          description: Rate limit exceeded
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