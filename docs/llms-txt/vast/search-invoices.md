# Source: https://docs.vast.ai/api-reference/billing/search-invoices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# search invoices

> This endpoint allows users to search and retrieve invoices based on specified filters.

CLI Usage: `vastai search invoices`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/invoices
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
  /api/v0/invoices:
    get:
      tags:
        - Billing
      summary: search invoices
      description: >-
        This endpoint allows users to search and retrieve invoices based on
        specified filters.


        CLI Usage: `vastai search invoices`
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                type:
                  type: string
                  description: Type of invoices to retrieve
                  example: charge
                select_filters:
                  type: object
                  description: Filters to apply to the invoice selection.
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    type:
                      type: string
                      example: charge
                    description:
                      type: string
                      example: 'Instance 123 GPU charge: hours * $/hr'
                    timestamp:
                      type: integer
                      example: 1633036800
                    quantity:
                      type: string
                      example: '10.000'
                    rate:
                      type: string
                      example: '0.1000'
                    amount:
                      type: string
                      example: '1.000'
                    instance_id:
                      type: integer
                      example: 123
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