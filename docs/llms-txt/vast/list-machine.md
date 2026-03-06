# Source: https://docs.vast.ai/api-reference/machines/list-machine.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# list machine

> Creates or updates ask contracts for a machine to list it for rent on the vast.ai platform.
Allows setting pricing, minimum GPU requirements, end date and discount rates.

CLI Usage: `vastai list machine <machine_id> [options]`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/machines/create_asks/
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
  /api/v0/machines/create_asks/:
    put:
      tags:
        - Machines
      summary: list machine
      description: >-
        Creates or updates ask contracts for a machine to list it for rent on
        the vast.ai platform.

        Allows setting pricing, minimum GPU requirements, end date and discount
        rates.


        CLI Usage: `vastai list machine <machine_id> [options]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - machine
              properties:
                machine:
                  type: integer
                  description: ID of the machine to list
                price_gpu:
                  type: number
                  format: float
                  description: Price per GPU per hour
                price_disk:
                  type: number
                  format: float
                  description: Price per GB of disk storage
                price_inetu:
                  type: number
                  format: float
                  description: Price per GB of upload bandwidth
                price_inetd:
                  type: number
                  format: float
                  description: Price per GB of download bandwidth
                price_min_bid:
                  type: number
                  format: float
                  description: Minimum bid price allowed
                min_chunk:
                  type: integer
                  description: Minimum number of GPUs that must be rented together
                  default: 1
                end_date:
                  type: number
                  format: float
                  description: Unix timestamp for when the listing expires
                credit_discount_max:
                  type: number
                  format: float
                  description: Maximum discount rate allowed for prepaid credits
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
                  extended:
                    type: integer
                    description: Number of client contracts extended to new end date
                  msg:
                    type: string
                    description: Status message if success is false
                example:
                  success: true
                  extended: 2
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
                    example: Invalid machine id or parameters
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
                    example: Only machine owner can create ask contracts
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````