# Source: https://docs.vast.ai/api-reference/machines/set-defjob.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# set defjob

> Creates default jobs (background instances) for a specified machine with the given parameters.

CLI Usage: `vastai set defjob <machine_id> --price_gpu <price> --price_inetu <price> --price_inetd <price> --image <image> [--args <args>]`



## OpenAPI

````yaml api-reference/openapi.json put /api/v0/machines/create_bids/
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
  /api/v0/machines/create_bids/:
    put:
      tags:
        - Machines
      summary: set defjob
      description: >-
        Creates default jobs (background instances) for a specified machine with
        the given parameters.


        CLI Usage: `vastai set defjob <machine_id> --price_gpu <price>
        --price_inetu <price> --price_inetd <price> --image <image> [--args
        <args>]`
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - machine
                - price_gpu
                - price_inetu
                - price_inetd
                - image
              properties:
                machine:
                  type: integer
                  description: ID of the machine to create jobs for.
                  example: 12345
                price_gpu:
                  type: number
                  format: float
                  description: Price per GPU per day.
                  example: 0.5
                price_inetu:
                  type: number
                  format: float
                  description: Price for internet upload.
                  example: 0.1
                price_inetd:
                  type: number
                  format: float
                  description: Price for internet download.
                  example: 0.1
                image:
                  type: string
                  description: Docker image to use for the job.
                  example: vastai/tensorflow
                args:
                  type: array
                  items:
                    type: string
                  description: Arguments for the Docker image.
                  example:
                    - '--arg1'
                    - '--arg2'
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
                  machine_id:
                    type: integer
                    example: 12345
                  user_id:
                    type: integer
                    example: 67890
                  you_sent:
                    type: object
                    description: The original request JSON.
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden
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
                    example: API requests too frequent endpoint threshold=2.8
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