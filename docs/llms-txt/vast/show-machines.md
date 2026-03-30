# Source: https://docs.vast.ai/api-reference/machines/show-machines.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show machines

> Fetches data for multiple machines associated with the authenticated user.

CLI Usage: `vastai show machines [--user_id <user_id>]`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/machines/
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
  /api/v0/machines/:
    get:
      tags:
        - Machines
      summary: show machines
      description: >-
        Fetches data for multiple machines associated with the authenticated
        user.


        CLI Usage: `vastai show machines [--user_id <user_id>]`
      operationId: getMachines
      parameters:
        - name: user_id
          in: query
          required: true
          description: The ID of the user whose machines are being requested.
          schema:
            type: string
      responses:
        '200':
          description: A list of machines
          content:
            application/json:
              schema:
                type: object
                properties:
                  machines:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The unique identifier for the machine.
                        name:
                          type: string
                          description: The name of the machine.
        '401':
          description: Unauthorized - User authentication failed
        '429':
          description: Too Many Requests - Rate limit exceeded
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````