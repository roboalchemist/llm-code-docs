# Source: https://docs.vast.ai/api-reference/machines/cancel-maint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# cancel maint

> Cancel a scheduled maintenance window for a specified machine.

CLI Usage: `vastai cancel maint <machine_id>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/machines/{machine_id}/cancel_maint/
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
  /api/v0/machines/{machine_id}/cancel_maint/:
    put:
      tags:
        - Machines
      summary: cancel maint
      description: |-
        Cancel a scheduled maintenance window for a specified machine.

        CLI Usage: `vastai cancel maint <machine_id>`
      parameters:
        - name: machine_id
          in: path
          required: true
          description: ID of the machine to cancel maintenance for.
          schema:
            type: integer
      responses:
        '200':
          description: Maintenance window successfully canceled.
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  ctime:
                    type: number
                    format: float
                    description: Current time in seconds since the epoch.
                  machine_id:
                    type: integer
                    description: ID of the machine.
                  msg:
                    type: string
                    example: deleted 1 scheduled maintenance window(s) on machine 1234
        '404':
          description: Machine not found or does not belong to the user.
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
                    example: No such machine id
                  machine_id:
                    type: integer
                  user_id:
                    type: integer
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````