# Source: https://docs.vast.ai/api-reference/billing/show-earnings.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# show earnings

> Retrieves the earnings history for a specified time range and optionally per machine.

CLI Usage: `vastai show earnings [options]`



## OpenAPI

````yaml api-reference/openapi.json get /api/v0/users/{user_id}/machine-earnings/
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
  /api/v0/users/{user_id}/machine-earnings/:
    get:
      tags:
        - Billing
      summary: show earnings
      description: >-
        Retrieves the earnings history for a specified time range and optionally
        per machine.


        CLI Usage: `vastai show earnings [options]`
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the user.
        - name: sday
          in: query
          schema:
            type: integer
          description: Start day for the earnings report.
        - name: eday
          in: query
          schema:
            type: integer
          description: End day for the earnings report.
        - name: machid
          in: query
          schema:
            type: integer
          description: Optional machine ID to filter earnings.
        - name: last_days
          in: query
          schema:
            type: integer
          description: Number of days to look back from today.
      responses:
        '200':
          description: Success response
          content:
            application/json:
              schema:
                type: object
                properties:
                  summary:
                    type: object
                    properties:
                      total_gpu:
                        type: number
                      total_stor:
                        type: number
                      total_bwu:
                        type: number
                      total_bwd:
                        type: number
                  username:
                    type: string
                  email:
                    type: string
                  fullname:
                    type: string
                  address1:
                    type: string
                  address2:
                    type: string
                  city:
                    type: string
                  zip:
                    type: string
                  country:
                    type: string
                  taxinfo:
                    type: string
                  current:
                    type: object
                    properties:
                      balance:
                        type: number
                      service_fee:
                        type: number
                      total:
                        type: number
                      credit:
                        type: number
                  per_machine:
                    type: array
                    items:
                      type: object
                      properties:
                        machine_id:
                          type: integer
                        gpu_earn:
                          type: number
                        sto_earn:
                          type: number
                        bwu_earn:
                          type: number
                        bwd_earn:
                          type: number
                  per_day:
                    type: array
                    items:
                      type: object
                      properties:
                        day:
                          type: integer
                        gpu_earn:
                          type: number
                        sto_earn:
                          type: number
                        bwu_earn:
                          type: number
                        bwd_earn:
                          type: number
        '400':
          description: Bad Request - Invalid input syntax
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
                    example: API requests too frequent endpoint threshold=2.0
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