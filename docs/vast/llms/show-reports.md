# Source: https://docs.vast.ai/api-reference/machines/show-reports.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show reports

> Retrieves a list of the most recent reports for a given machine. Each report includes details such as the problem identified, a message describing the issue, and the timestamp when the report was created.

CLI Usage: `vastai reports <machine_id>`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/machines/{machine_id}/reports/
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
  /api/v0/machines/{machine_id}/reports/:
    get:
      tags:
        - Machines
      summary: show reports
      description: >-
        Retrieves a list of the most recent reports for a given machine. Each
        report includes details such as the problem identified, a message
        describing the issue, and the timestamp when the report was created.


        CLI Usage: `vastai reports <machine_id>`
      parameters:
        - name: machine_id
          in: path
          required: true
          schema:
            type: integer
          description: The unique identifier of the machine.
      responses:
        '200':
          description: An array of reports for the specified machine.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    problem:
                      type: string
                      description: The type of problem reported.
                    message:
                      type: string
                      description: Detailed message describing the problem.
                    created_at:
                      type: string
                      format: date-time
                      description: Timestamp when the report was created.
        '404':
          description: Machine not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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