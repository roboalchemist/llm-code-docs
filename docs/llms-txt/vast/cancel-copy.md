# Source: https://docs.vast.ai/api-reference/instances/cancel-copy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# cancel copy

> Cancel a remote copy operation specified by the destination ID (dst_id).

CLI Usage: `vastai cancel copy --dst_id <destination_id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/commands/copy_direct/
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
  /api/v0/commands/copy_direct/:
    delete:
      tags:
        - Instances
      summary: cancel copy
      description: |-
        Cancel a remote copy operation specified by the destination ID (dst_id).

        CLI Usage: `vastai cancel copy --dst_id <destination_id>`
      operationId: cancelRemoteRsync
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                dst_id:
                  type: string
                  description: ID of the copy instance target to cancel.
              required:
                - dst_id
      responses:
        '200':
          description: Remote copy canceled successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
        '400':
          description: Invalid arguments provided.
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
                    example: invalid_args
                  msg:
                    type: string
                    example: Invalid dst_id.
        '404':
          description: Destination ID not found or access denied.
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
                    example: no_such_user
                  msg:
                    type: string
                    example: No such user.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````