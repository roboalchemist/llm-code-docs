# Source: https://docs.vast.ai/api-reference/machines/schedule-maint.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# schedule maint

> Schedules a maintenance window for a specified machine and notifies clients.

CLI Usage: `vastai schedule maint <machine_id> --sdate <sdate> --duration <duration>`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/machines/{machine_id}/dnotify
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
  /api/v0/machines/{machine_id}/dnotify:
    put:
      tags:
        - Machines
      summary: schedule maint
      description: >-
        Schedules a maintenance window for a specified machine and notifies
        clients.


        CLI Usage: `vastai schedule maint <machine_id> --sdate <sdate>
        --duration <duration>`
      parameters:
        - name: machine_id
          in: path
          required: true
          description: ID of the machine to schedule maintenance for.
          schema:
            type: integer
            example: 12345
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - sdate
                - duration
              properties:
                sdate:
                  type: string
                  format: date-time
                  description: Start date and time of the maintenance window.
                  example: '2023-10-30T14:00:00Z'
                duration:
                  type: integer
                  description: Duration of the maintenance window in hours.
                  example: 2
                maintenance_reason:
                  type: string
                  description: Reason for the maintenance.
                  example: Routine hardware check
                maintenance_category:
                  type: string
                  description: Category of the maintenance.
                  enum:
                    - power
                    - internet
                    - disk
                    - gpu
                    - software
                    - other
                  example: software
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
                  you_sent:
                    type: string
                    example: 2 notifications sent
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '422':
          description: Unprocessable Entity
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
                    example: API requests too frequent endpoint threshold=2.5
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