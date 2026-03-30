# Source: https://docs.vast.ai/api-reference/serverless/get-workergroup-workers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# get workergroup workers

> Retrieves the current list and status of workers for a specific workergroup.
Useful for monitoring, debugging connectivity issues, and understanding resource usage within a workergroup.

CLI Usage: `vastai get workergroup workers <id>`



## OpenAPI

````yaml api-reference/openapi.json post /get_workergroup_workers/
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
  /get_workergroup_workers/:
    post:
      tags:
        - Serverless
      summary: get workergroup workers
      description: >-
        Retrieves the current list and status of workers for a specific
        workergroup.

        Useful for monitoring, debugging connectivity issues, and understanding
        resource usage within a workergroup.


        CLI Usage: `vastai get workergroup workers <id>`
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
                  description: ID of the workergroup to monitor
                  default: 12345
                  example: 12345
                  minimum: 1
      responses:
        '200':
          description: Workers successfully retrieved.
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success - Workers Retrieved
                    type: object
                    properties:
                      workers:
                        type: array
                        description: List of workers in this workergroup
                        items:
                          type: object
                          properties:
                            id:
                              type: integer
                              description: Workergroup instance ID
                              example: 67890
                            status:
                              type: string
                              description: Current worker status
                              example: running
                            url:
                              type: string
                              description: Worker instance URL
                              example: http://192.168.1.10:8000
                            created_at:
                              type: string
                              description: When the worker was created
                              example: '2023-10-01T12:00:00Z'
                  - title: Error Response
                    type: string
                    description: >-
                      Error message when workergroup not found or authentication
                      fails
                    example: >-
                      authenticate_workergroup_apikey: invalid api_key or
                      workergroup 12345 not found
      security:
        - BearerAuth: []
      servers:
        - url: https://run.vast.ai
          description: Production server
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: API key must be provided in the Authorization header

````