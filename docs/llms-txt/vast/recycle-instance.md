# Source: https://docs.vast.ai/api-reference/instances/recycle-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# recycle instance

> Destroys and recreates container in place (from newly pulled image) without losing GPU priority.
Updates container status to 'recycling' and executes docker stop/remove commands on the host machine.

CLI Usage: `vastai recycle instance <id>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/instances/recycle/{id}/
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
  /api/v0/instances/recycle/{id}/:
    put:
      tags:
        - Instances
      summary: recycle instance
      description: >-
        Destroys and recreates container in place (from newly pulled image)
        without losing GPU priority.

        Updates container status to 'recycling' and executes docker stop/remove
        commands on the host machine.


        CLI Usage: `vastai recycle instance <id>`
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the instance to recycle
          example: 1234
      responses:
        '200':
          description: Instance recycle initiated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
        '400':
          description: Bad Request - Invalid instance ID
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
                      - invalid_id
                  msg:
                    type: string
                    example: Invalid instance id.
        '401':
          description: Unauthorized
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