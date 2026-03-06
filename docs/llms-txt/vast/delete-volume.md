# Source: https://docs.vast.ai/api-reference/volumes/delete-volume.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# delete volume

> Delete a volume by its ID.

CLI Usage: `vastai delete volume <volume_id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/volumes/
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
  /api/v0/volumes/:
    delete:
      tags:
        - Volumes
      summary: delete volume
      description: |-
        Delete a volume by its ID.

        CLI Usage: `vastai delete volume <volume_id>`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - id
              properties:
                id:
                  type: integer
                  description: ID of the volume to delete
                  example: 100
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
                    example: Please provide a valid volume ID.
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
                      - no_such_volume
                  msg:
                    type: string
                    example: Volume with that ID does not exist.
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