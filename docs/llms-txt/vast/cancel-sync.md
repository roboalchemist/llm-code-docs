# Source: https://docs.vast.ai/api-reference/instances/cancel-sync.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# cancel sync

> Cancels an in-progress remote sync operation identified by the destination instance ID.
This operation cannot be resumed once canceled and must be restarted if needed.

CLI Usage: `vastai cancel sync --dst_id <destination_id>`



## OpenAPI

````yaml api-reference/openapi.json delete /api/v0/commands/rclone/
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
  /api/v0/commands/rclone/:
    delete:
      tags:
        - Instances
      summary: cancel sync
      description: >-
        Cancels an in-progress remote sync operation identified by the
        destination instance ID.

        This operation cannot be resumed once canceled and must be restarted if
        needed.


        CLI Usage: `vastai cancel sync --dst_id <destination_id>`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                dst_id:
                  type: integer
                  description: The destination instance ID of the sync operation to cancel.
              required:
                - dst_id
      responses:
        '200':
          description: Sync operation canceled successfully.
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
                    example: >-
                      Remote copy canceled - check instance status bar for
                      progress updates (~30 seconds delayed).
        '400':
          description: Invalid request due to missing or incorrect parameters.
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
          description: Instance not found.
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
                    example: no_such_instance
                  msg:
                    type: string
                    example: No such instance.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````