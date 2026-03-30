# Source: https://docs.vast.ai/api-reference/volumes/rent-volume.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# rent volume

> Rent/create a new volume with specified parameters.

CLI Usage: `vastai create volume <id> --size <size_gb>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/volumes/
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
    put:
      tags:
        - Volumes
      summary: rent volume
      description: |-
        Rent/create a new volume with specified parameters.

        CLI Usage: `vastai create volume <id> --size <size_gb>`
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
                  description: ID for the volume
                  example: 420
                size:
                  type: integer
                  description: Size in GB (Defaults to 15)
                  example: 15
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
                  volume_name:
                    type: string
                    description: Name of the created/resized volume
                    example: V.20118481
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````