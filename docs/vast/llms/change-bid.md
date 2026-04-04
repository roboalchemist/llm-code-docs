# Source: https://docs.vast.ai/api-reference/instances/change-bid.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# change bid

> Change the current bid price of an instance to a specified price.

CLI Usage: `vastai change bid <id> --price <price>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/instances/bid_price/{id}/
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
  /api/v0/instances/bid_price/{id}/:
    put:
      tags:
        - Instances
      summary: change bid
      description: |-
        Change the current bid price of an instance to a specified price.

        CLI Usage: `vastai change bid <id> --price <price>`
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: Instance ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - client_id
                - price
              properties:
                client_id:
                  type: string
                  description: Client identifier (usually "me")
                  example: me
                price:
                  type: number
                  description: Bid price in $/hour
                  minimum: 0.001
                  maximum: 32
                  example: 0.17
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
                    enum:
                      - invalid_args
                  msg:
                    type: string
                    example: Please set a bid price >= 0.001.
        '404':
          description: Not Found
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
                    enum:
                      - no_such_instance
                  msg:
                    type: string
                    example: Instance with that ID does not exist.
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=5.5
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````