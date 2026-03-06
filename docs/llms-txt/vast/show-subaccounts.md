# Source: https://docs.vast.ai/api-reference/accounts/show-subaccounts.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show subaccounts

> Retrieve a list of subaccounts associated with the authenticated user's account.

CLI Usage: `vastai show subaccounts`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/subaccounts/
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
  /api/v0/subaccounts/:
    get:
      tags:
        - Accounts
      summary: show subaccounts
      description: >-
        Retrieve a list of subaccounts associated with the authenticated user's
        account.


        CLI Usage: `vastai show subaccounts`
      responses:
        '200':
          description: A list of subaccounts.
          content:
            application/json:
              schema:
                type: object
                properties:
                  users:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          description: The unique identifier of the subaccount.
                        parent_id:
                          type: integer
                          description: The ID of the parent account.
                        key_id:
                          type: integer
                          description: The API key ID associated with the subaccount.
                        created_at:
                          type: string
                          format: date-time
                          description: The timestamp when the subaccount was created.
                        deleted_at:
                          type: string
                          format: date-time
                          nullable: true
                          description: >-
                            The timestamp when the subaccount was deleted, if
                            applicable.
        '401':
          description: Unauthorized access due to invalid or missing authentication token.
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
                    example: API requests too frequent endpoint threshold=2.1
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