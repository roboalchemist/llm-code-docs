# Source: https://docs.vast.ai/api-reference/volumes/unlist-volume.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# unlist volume

> Remove a volume listing from the marketplace.

CLI Usage: `vastai unlist volume <volume_id>`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/volumes/unlist/
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
  /api/v0/volumes/unlist/:
    post:
      tags:
        - Volumes
      summary: unlist volume
      description: |-
        Remove a volume listing from the marketplace.

        CLI Usage: `vastai unlist volume <volume_id>`
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
                  description: ID of the volume listing to unlist
                  example: 2029
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
                  msg:
                    type: string
                    description: Success message
                    example: Unlisted Volume 2029.
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
                  msg:
                    type: string
                    enum:
                      - You must pass in `id` in the body of the request
                      - Volume listing does not exist
                      - Unable to delete active volume listing
                      - Unable to delete volume listing.
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: API requests too frequent endpoint threshold=5.0
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````