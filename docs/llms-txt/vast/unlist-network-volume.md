# Source: https://docs.vast.ai/api-reference/network-volumes/unlist-network-volume.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# unlist network-volume

> Unlists a network volume for rent.

CLI Usage: `vastai unlist volume <offer_id>`



## OpenAPI

````yaml api-reference/openapi.json post /api/v0/network_volumes/unlist/
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
  /api/v0/network_volumes/unlist/:
    post:
      tags:
        - Network Volumes
      summary: unlist network-volume
      description: |-
        Unlists a network volume for rent.

        CLI Usage: `vastai unlist volume <offer_id>`
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
                  description: ID of network volume ask being unlisted
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  id:
                    type: integer
                    description: id of unlisted network volume ask
                  msg:
                    type: string
                    description: status message
                example:
                  success: true
                  id: 6
                  msg: Deleted network volume listing
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: invalid_args
                  msg:
                    type: string
                    example: You must pass in `id` in the body of the request
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: not_authorized
                  msg:
                    type: string
                    example: >-
                      Authorization Error. Check that you have proper privileges
                      to perform this action.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````